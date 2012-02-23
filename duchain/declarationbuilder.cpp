/*****************************************************************************
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 * Copyright 2007 Andreas Pakulat <apaku@gmx.de>                             *
 * Copyright 2010 Sven Brauch <svenbrauch@googlemail.com>                    *
 *                                                                           *
 * Permission is hereby granted, free of charge, to any person obtaining     *
 * a copy of this software and associated documentation files (the           *
 * "Software"), to deal in the Software without restriction, including       *
 * without limitation the rights to use, copy, modify, merge, publish,       *
 * distribute, sublicense, and/or sell copies of the Software, and to        *
 * permit persons to whom the Software is furnished to do so, subject to     *
 * the following conditions:                                                 *
 *                                                                           *
 * The above copyright notice and this permission notice shall be            *
 * included in all copies or substantial portions of the Software.           *
 *                                                                           *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,           *
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF        *
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND                     *
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE    *
 * LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION    *
 * OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION     *
 * WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.           *
 *****************************************************************************/
#include <QByteArray>
#include <QtGlobal>
#include <KUrl>

#include <language/duchain/functiondeclaration.h>
#include <language/duchain/classfunctiondeclaration.h>
#include <language/duchain/declaration.h>
#include <language/duchain/duchain.h>
#include <language/duchain/duchainlock.h>
#include <language/duchain/types/functiontype.h>
#include <language/duchain/types/alltypes.h>
#include <language/duchain/types/abstracttype.h>
#include <language/duchain/types/integraltype.h>
#include <language/duchain/classdeclaration.h>
#include <language/duchain/classfunctiondeclaration.h>
#include <language/duchain/classmemberdeclaration.h>
#include <language/duchain/classmemberdeclarationdata.h>
#include <language/duchain/types/unsuretype.h>
#include <language/duchain/builders/abstracttypebuilder.h>
#include <language/duchain/aliasdeclaration.h>
#include <language/duchain/declaration.h>
#include <language/duchain/duchainutils.h>
#include <language/backgroundparser/backgroundparser.h>
#include <language/backgroundparser/parsejob.h>
#include <interfaces/ilanguagecontroller.h>

#include "duchain/declarations/decorator.h"
#include "contextbuilder.h"
#include "declarationbuilder.h"
#include "pythoneditorintegrator.h"
#include "expressionvisitor.h"
#include "helpers.h"
#include "types/variablelengthcontainer.h"
#include "types/hintedtype.h"
#include "types/unsuretype.h"
#include "duchain/declarations/functiondeclaration.h"
#include "duchain/declarations/classdeclaration.h"

using namespace KTextEditor;

using namespace KDevelop;

namespace Python
{

DeclarationBuilder::DeclarationBuilder()
        : DeclarationBuilderBase()
{
    kDebug() << "Building Declarations";
}

DeclarationBuilder::DeclarationBuilder( PythonEditorIntegrator* editor )
        : DeclarationBuilderBase( )
{
    setEditor(editor);
    kDebug() << "Building Declarations";
}

DeclarationBuilder:: ~DeclarationBuilder()
{
}

void DeclarationBuilder::setPrebuilding(bool prebuilding)
{
    m_prebuilding = prebuilding;
}

ReferencedTopDUContext DeclarationBuilder::build(const IndexedString& url, Ast* node, ReferencedTopDUContext updateContext)
{
    if ( ! m_prebuilding ) {
        kDebug() << "building, but running pre-builder first";
        DeclarationBuilder* prebuilder = new DeclarationBuilder(editor());
        prebuilder->m_currentlyParsedDocument = currentlyParsedDocument();
        prebuilder->setPrebuilding(true);
        prebuilder->m_futureModificationRevision = m_futureModificationRevision;
        updateContext = prebuilder->build(url, node, updateContext);
        kDebug() << "pre-builder finished";
        delete prebuilder;
    }
    else {
        kDebug() << "prebuilding";
    }
    return DeclarationBuilderBase::build(url, node, updateContext);
}

void DeclarationBuilder::closeDeclaration()
{
    if ( lastContext() )
    {
        DUChainReadLocker lock( DUChain::lock() );
        currentDeclaration()->setKind( Declaration::Type );
    }
    
    Q_ASSERT(currentDeclaration()->alwaysForceDirect());

    eventuallyAssignInternalContext();

    DeclarationBuilderBase::closeDeclaration();
}

template<typename T> T* DeclarationBuilder::visitVariableDeclaration(Ast* node, Declaration* previous)
{
    if ( node->astType == Ast::NameAstType ) {
        NameAst* currentVariableDefinition = static_cast<NameAst*>(node);
        // those contexts can invoke a variable declaration
        // this prevents "bar" from being declared in something like "foo = bar"
        QList<ExpressionAst::Context> declaringContexts;
        declaringContexts << ExpressionAst::Store << ExpressionAst::Parameter << ExpressionAst::AugStore;
        if ( ! declaringContexts.contains(currentVariableDefinition->context) ) {
                return 0;
        }
        Identifier* id = currentVariableDefinition->identifier;
        return visitVariableDeclaration<T>(id, currentVariableDefinition, previous);
    }
    else {
        kWarning() << "cannot create variable declaration for non-name AST, this is a programming error";
        return static_cast<T*>(0);
    }
}

template<typename T> T* DeclarationBuilder::visitVariableDeclaration(Identifier* node, RangeInRevision range)
{
    Ast* pseudo = new Ast();
    pseudo->startLine = range.start.line; pseudo->startCol = range.start.column;
    pseudo->endLine = range.end.line; pseudo->endCol = range.end.column;
    T* result = visitVariableDeclaration<T>(node, pseudo, 0);
    delete pseudo;
    return result;
}

typedef QPair<Declaration*, int> p;
/*
 * WARNING: This will return a nullpointer if another than the expected type of variable was found!
 * */
template<typename T> T* DeclarationBuilder::visitVariableDeclaration(Identifier* node, Ast* originalAst, Declaration* previous)
{
    DUChainWriteLocker lock(DUChain::lock());
    Q_ASSERT(node);
    Ast* rangeNode = originalAst ? originalAst : node;
    
    kDebug() << "Parsing variable declaration: " << node->value;
    
    Declaration* dec = 0;
    QList<Declaration*> existingDeclarations;
    // specified from outside
    if ( previous ) {
        existingDeclarations << previous;
        kDebug() << previous->toString();
    }
    // find decls by ourselves
    else {
        /**DBG**/
        kDebug() << "Current context: " << currentContext()->scopeIdentifier() << currentContext()->range().castToSimpleRange();
        kDebug() << "Looking for node identifier:" << identifierForNode(node) << identifierForNode(node).last();
        /** /DBG **/
        existingDeclarations = currentContext()->findDeclarations(identifierForNode(node).last(),  // <- WARNING first / last?
                                                                    CursorInRevision::invalid(), 0, 
                                                                    DUContext::DontSearchInParent);
        // append arguments context
        if ( m_mostRecentArgumentsContext ) {
            QList<Declaration*> args = m_mostRecentArgumentsContext->findDeclarations(identifierForNode(node).last(),
                                                                                      CursorInRevision::invalid(), 0, DUContext::DontSearchInParent);
            existingDeclarations.append(args);
        }
        kDebug() << "Found " << existingDeclarations.length() << "declarations";
    }
    QList<Declaration*> remainingDeclarations;
    bool declarationOpened = false;
    foreach ( Declaration* d, existingDeclarations ) {
        Declaration* fitting = dynamic_cast<T*>(d);
        kDebug() << "last one: " << d << d->toString() << dynamic_cast<T*>(d) << wasEncountered(d);
        bool invalidType = d && d->abstractType() && lastType() && lastType()->whichType() != AbstractType::TypeFunction && d->isFunctionDeclaration();
        if ( fitting && ! wasEncountered(d) && ! invalidType ) {
            if ( d->topContext() == currentContext()->topContext() ) {
                kDebug() << "Opening previously existing declaration for " << d->toString();
                openDeclarationInternal(d);
                d->setRange(editorFindRange(rangeNode, rangeNode));
                declarationOpened = true;
            }
            else {
                kDebug() << "Not opening previously existing declaration because it's in another top context";
            }
            setEncountered(d);
            dec = d;
        }
        else if ( fitting && ! invalidType ) {
           remainingDeclarations << fitting;
        }
    }
    existingDeclarations = remainingDeclarations;
    
    kDebug() << "VARIABLE CONTEXT: " << currentContext()->scopeIdentifier() << currentContext()->range().castToSimpleRange() << currentContext()->type() << DUContext::Class;
    
    // tells whether the declaration found for updating is in the same top context
    bool inSameTopContext = true;
    // tells whether there's fitting declarations to update (update is not the same as re-open! one is for
    // code which uses the same variable twice, the other is for multiple passes of the parser)
    bool noFittingDeclaration = true;
    if ( ! existingDeclarations.isEmpty() ) {
        if ( Helper::resolveAliasDeclaration(existingDeclarations.last())->topContext() != topContext() ) {
            inSameTopContext = false;
        }
        if ( dynamic_cast<T*>(existingDeclarations.last()) ) {
            noFittingDeclaration = false;
        }
    }
    if ( currentContext() && currentContext()->type() == DUContext::Class && noFittingDeclaration ) {
        kDebug() << "Creating class member declaration for " << node->value << node->startLine << ":" << node->startCol;
        kDebug() << "Context type: " << currentContext()->scopeIdentifier() << currentContext()->range().castToSimpleRange();
        if ( ! dec ) {
            dec = openDeclaration<ClassMemberDeclaration>(node, originalAst ? originalAst : node);
            declarationOpened = true;
        }
        if ( declarationOpened ) {
            DeclarationBuilderBase::closeDeclaration();
        }
        dec->setType(lastType());
        dec->setKind(KDevelop::Declaration::Instance);
    } else if ( noFittingDeclaration ) {
        RangeInRevision range = editorFindRange(rangeNode, rangeNode);
        kDebug() << "Creating variable declaration for " << range;
        kDebug() << "which has type" << ( dec && dec->abstractType() ? dec->abstractType()->toString() : "none" );
        if ( ! dec ) {
            kDebug() << "This declaration is a new one, with range" << range;
            dec = openDeclaration<T>(node, rangeNode);
            declarationOpened = true;
        }
        else {
            dec->setRange(range);
        }
        /*
        else {
            kDebug() << "This declaration is old, and has the following type: " << dec->abstractType()->toString();
        }
        */
        if ( declarationOpened ) {
            DeclarationBuilderBase::closeDeclaration();
        }
        UnsureType::Ptr hints = Helper::extractTypeHints(dec->abstractType(), topContext());
        kDebug() << "Type Hints: " << hints->toString();
        AbstractType::Ptr newType = Helper::mergeTypes(hints.cast<AbstractType>(), lastType(), topContext());
        kDebug() << "Resulting type: " << newType->toString();
        dec->setType(newType);
        dec->setKind(KDevelop::Declaration::Instance); // everything is an object in python
    }
    else if ( inSameTopContext ) {
        kDebug() << "Existing declarations are not empty. count: " << existingDeclarations.count();
        dec = existingDeclarations.last();
        AbstractType::Ptr currentType = dec->abstractType();
        AbstractType::Ptr newType = lastType();
        if ( newType ) {
            if ( currentType && !currentType->equals(newType.unsafeData()) ) {
                IntegralType::Ptr integral = IntegralType::Ptr::dynamicCast(currentType);
                if ( integral &&  integral->dataType() == IntegralType::TypeMixed ) {
                    dec->setType(newType);
                } else {
                    dec->setType(Helper::mergeTypes(currentType, newType, topContext()));
                }
            } else {
                kDebug() << "Existing declaration with no type from last declaration.";
                dec->setType(lastType());
            }
        } else {
            kDebug() << "Existing declaration with no type.";
        }
    }
    
    T* result = dynamic_cast<T*>(dec);
    if ( ! result ) kWarning() << "variable declaration does not have the expected type";
    return result;
}

void DeclarationBuilder::visitCode(CodeAst* node)
{
    Q_ASSERT(currentlyParsedDocument().toUrl().isValid());
    m_unresolvedImports.clear();
    DeclarationBuilderBase::visitCode(node);
}

void DeclarationBuilder::visitExceptionHandler(ExceptionHandlerAst* node)
{
    if ( dynamic_cast<NameAst*>(node->name) ) {
        DUChainReadLocker lock(DUChain::lock());
        ExpressionVisitor v(currentContext(), editor());
        v.visitNode(node->type);
        openType(v.lastType());
        setLastType(v.lastType());
        lock.unlock();
        visitVariableDeclaration<Declaration>(node->name); // except Error as <vardecl>
        lock.lock();
        closeType();
    }
    DeclarationBuilderBase::visitExceptionHandler(node);
}

void DeclarationBuilder::visitWith(WithAst* node)
{
    if ( node->optionalVars ) {
        DUChainReadLocker lock(DUChain::lock());
        ExpressionVisitor v(currentContext(), editor());
        v.visitNode(node->contextExpression);
        setLastType(v.lastType());
        lock.unlock();
        visitVariableDeclaration<Declaration>(node->optionalVars);
    }
    Python::ContextBuilder::visitWith(node);
}

void DeclarationBuilder::visitFor(ForAst* node)
{
    DUChainWriteLocker lock(DUChain::lock());
    ExpressionVisitor v(currentContext(), editor());
    v.visitNode(node->iterator);
    lock.unlock();
    VariableLengthContainer::Ptr type = v.lastType().cast<VariableLengthContainer>();
    if ( node->target->astType == Ast::NameAstType ) {
        if ( type && type->contentType() ) {
            setLastType(type->contentType().abstractType());
        }
        else {
            setLastType(AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed)));
        }
        visitVariableDeclaration<Declaration>(node->target);
    }
    else if ( node->target->astType == Ast::TupleAstType ) {
        short atElement = 0;
        foreach ( ExpressionAst* tupleMember, dynamic_cast<TupleAst*>(node->target)->elements ) {
            if ( tupleMember->astType == Ast::NameAstType ) {
                if ( atElement == 0 && type && type->keyType() ) {
                    setLastType(type->keyType().abstractType());
                }
                else if ( atElement == 1 && type && type->contentType() ) {
                    setLastType(type->contentType().abstractType());
                }
                else {
                    setLastType(AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed)));
                }
                visitVariableDeclaration<Declaration>(tupleMember);
            }
            ++atElement;
        }
    }
    Python::ContextBuilder::visitFor(node);
}

Declaration* DeclarationBuilder::findDeclarationInContext(QStringList dottedNameIdentifier, TopDUContext* ctx) const
{
    DUChainReadLocker lock(DUChain::lock());
    DUContext* currentContext = ctx;
    Q_ASSERT(currentContext);
    Declaration* lastAccessedDeclaration = 0;
    foreach ( QString currentIdentifier, dottedNameIdentifier ) {
        QList<Declaration*> declarations = currentContext->findDeclarations(QualifiedIdentifier(currentIdentifier).first(),
                                                                            CursorInRevision::invalid(), 0, DUContext::DontSearchInParent);
        // break if the list of identifiers is not yet totally worked through and no declaration with an internal context was found
        if ( declarations.isEmpty() || ( ! declarations.first()->internalContext() && currentIdentifier != dottedNameIdentifier.last() ) ) {
            kDebug() << "Declaration not found: " << dottedNameIdentifier << "in top context" << ctx->url().toUrl().path();
            return 0;
        }
        else {
            lastAccessedDeclaration = declarations.first();
            currentContext = lastAccessedDeclaration->internalContext();
        }
    }
    return lastAccessedDeclaration;
}

void DeclarationBuilder::visitImportFrom(ImportFromAst* node)
{
    Python::AstDefaultVisitor::visitImportFrom(node);
    QString moduleName;
    foreach ( AliasAst* name, node->names ) {
        if ( node->module ) {
            moduleName = node->module->value + "." + name->name->value;
        }
        else {
            moduleName = "." + name->name->value;
        }
        Identifier* declarationIdentifier = 0;
        if ( name->asName ) {
            declarationIdentifier = name->asName;
        }
        else {
            declarationIdentifier = name->name;
        }
        Declaration* success = createModuleImportDeclaration(moduleName, declarationIdentifier, 0, DontCreateProblems);
        if ( not success and node->module ) {
            moduleName = node->module->value + ".__init__." + name->name->value;
            createModuleImportDeclaration(moduleName, declarationIdentifier);
        }
    }
}

void DeclarationBuilder::visitComprehension(ComprehensionAst* node)
{
    Python::AstDefaultVisitor::visitComprehension(node);
    kDebug() << "visiting comprehension" << currentContext()->range();
    RangeInRevision declarationRange(currentContext()->range().start, currentContext()->range().start);
    declarationRange.end.column -= 1;
    kDebug() << "declaration range: " << declarationRange;
    
    AbstractType::Ptr targetType;
    if ( node->iterator ) {
        DUChainReadLocker lock(DUChain::lock());
        ExpressionVisitor v(currentContext());
        v.visitNode(node->iterator);
        lock.unlock();
        if ( VariableLengthContainer* container = dynamic_cast<VariableLengthContainer*>(v.lastType().unsafeData()) ) {
            targetType = container->contentType().abstractType();
        }
    }
    
    if ( node->target->astType == Ast::NameAstType ) {
        Declaration* d = visitVariableDeclaration<Declaration>(static_cast<NameAst*>(node->target)->identifier, declarationRange);
        DUChainWriteLocker lock(DUChain::lock());
        if ( d and targetType ) {
            d->setAbstractType(targetType);
        }
        else {
            d->setAbstractType(AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed)));
        }
    }
    if ( node->target->astType == Ast::TupleAstType ) {
        foreach ( ExpressionAst* tupleElt, static_cast<TupleAst*>(node->target)->elements ) {
            if ( tupleElt->astType == Ast::NameAstType ) {
                NameAst* n = static_cast<NameAst*>(tupleElt);
                Declaration* d = visitVariableDeclaration<Declaration>(n->identifier, declarationRange);
                // TODO: Fix this as soon as tuple type support is implemented.
                DUChainWriteLocker lock(DUChain::lock());
                d->setAbstractType(AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed)));
//                 if ( d and targetType ) {
//                     d->setAbstractType(targetType);
//                 }
//                 else {
//                     d->setAbstractType(AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed)));
//                 }
            }
        }
    }
}

void DeclarationBuilder::visitImport(ImportAst* node)
{
    Python::ContextBuilder::visitImport(node);
    DUChainWriteLocker lock(DUChain::lock());
    foreach ( AliasAst* name, node->names ) {
        QString moduleName = name->name->value;
        // use alias if available, name otherwise
        Identifier* declarationIdentifier = name->asName ? name->asName : name->name;
        createModuleImportDeclaration(moduleName, declarationIdentifier);
    }
}

Declaration* DeclarationBuilder::createModuleImportDeclaration(QString dottedName, Identifier* declarationIdentifier, Ast* rangeNode, ProblemPolicy createProblem)
{
    QPair<KUrl, QStringList> moduleInfo = findModulePath(dottedName);
    kDebug() << dottedName;
    RangeInRevision range(RangeInRevision::invalid());
    if ( rangeNode ) {
        range = rangeForNode(rangeNode, false);
    }
    else {
        range = rangeForNode(declarationIdentifier, false);
    }
    Q_ASSERT(range.isValid());
    
    kDebug() << "Found module path [path/path in file]: " << moduleInfo;
    kDebug() << "Declaration identifier:" << declarationIdentifier->value;
    DUChainWriteLocker lock(DUChain::lock());
    ReferencedTopDUContext moduleContext = DUChain::self()->chainForDocument(IndexedString(moduleInfo.first));
    lock.unlock();
    Declaration* resultingDeclaration = 0;
    if ( ! moduleInfo.first.isValid() ) {
        kDebug() << "invalid or non-existent URL:" << moduleInfo;
        if ( createProblem != DontCreateProblems ) {
            KDevelop::Problem *p = new KDevelop::Problem();
            p->setFinalLocation(DocumentRange(currentlyParsedDocument(), range.castToSimpleRange())); // TODO ok?
            p->setSource(KDevelop::ProblemData::SemanticAnalysis);
            p->setSeverity(KDevelop::ProblemData::Warning);
            p->setDescription(i18n("Module \"%1\" not found", dottedName));
            {
                DUChainWriteLocker wlock(DUChain::lock());
                ProblemPointer ptr(p);
                topContext()->addProblem(ptr);
            }
        }
        return 0;
    }
    if ( ! moduleContext ) {
        // schedule the include file for parsing, and schedule the current one for reparsing after that is done
        kDebug() << "No module context, recompiling";
        m_unresolvedImports.append(moduleInfo.first);
        if ( KDevelop::ICore::self()->languageController()->backgroundParser()->isQueued(moduleInfo.first) ) {
            KDevelop::ICore::self()->languageController()->backgroundParser()->removeDocument(moduleInfo.first);
        }
        KDevelop::ICore::self()->languageController()->backgroundParser()
                                   ->addDocument(moduleInfo.first, TopDUContext::AllDeclarationsContextsAndUses, m_ownPriority - 1,
                                                 0, ParseJob::RespectsSequentialProcessing);
//         KDevelop::ICore::self()->languageController()->backgroundParser()->parseDocuments();
//         DUChain::self()->updateContextForUrl(IndexedString(moduleInfo.first), TopDUContext::AllDeclarationsContextsAndUses, 0, m_ownPriority - 1);
        return 0;
    }
    if ( moduleInfo.second.isEmpty() ) {
        // import the whole module
        kDebug() << "Got module, importing it" << declarationIdentifier->value;
        Declaration* lastDeclaration = 0;
        QStringList nameComponents = declarationIdentifier->value.split('.');
        int depth = 0;
        
        for ( int i = nameComponents.length() - 1; i >= 0; i-- ) {
            QStringList currentName;
            for ( int j = 0; j < i; j++ ) {
                currentName.append(nameComponents.at(j));
            }
            lastDeclaration = findDeclarationInContext(currentName, topContext());
            if ( lastDeclaration and lastDeclaration->range() < range ) {
                depth = i;
                break;
            }
        }
        
        DUContext* extendingPreviousImportCtx = 0;
        QStringList remainingNameComponents;
        bool injectingContext = false;
        if ( lastDeclaration and lastDeclaration->internalContext() ) {
            kDebug() << "Found existing import statement while creating declaration for " << declarationIdentifier->value;
            for ( int i = depth; i < nameComponents.length(); i++ ) {
                remainingNameComponents.append(nameComponents.at(i));
            }
            extendingPreviousImportCtx = lastDeclaration->internalContext();
            injectContext(extendingPreviousImportCtx);
            injectingContext = true;
        }
        else {
            remainingNameComponents = nameComponents;
            extendingPreviousImportCtx = topContext();
        }
        
        // now, proceed normally
        QList<Declaration*> openedDeclarations;
        QList<StructureType::Ptr> openedTypes;
        QList<DUContext*> openedContexts;
//         bool extendingPreviousImports = true;
        
        DUChainWriteLocker lock(DUChain::lock());
        for ( int i = 0; i < remainingNameComponents.length(); i++ ) {
            const QString& component = remainingNameComponents.at(i);
            kDebug() << "creating context for " << component;
            Identifier* temporaryIdentifier = new Identifier(component);
            Declaration* d = 0;
            StructureType::Ptr moduleType;
            moduleType = StructureType::Ptr(new StructureType());
            temporaryIdentifier->copyRange(declarationIdentifier);
            temporaryIdentifier->endCol = temporaryIdentifier->startCol - 1;
            openType(moduleType);
            d = visitVariableDeclaration<Declaration>(temporaryIdentifier);
            delete temporaryIdentifier;
            if ( d ) {
                if ( topContext() != extendingPreviousImportCtx ) {
                    d->setRange(RangeInRevision(extendingPreviousImportCtx->range().start, extendingPreviousImportCtx->range().start));
                }
                d->setAutoDeclaration(true);
                currentContext()->createUse(d->ownIndex(), editorFindRange(declarationIdentifier, declarationIdentifier));
            }
            openedContexts.append(openContext(declarationIdentifier, KDevelop::DUContext::Other));
            if ( i == remainingNameComponents.length() - 1 ) {
                currentContext()->addImportedParentContext(moduleContext);
            }
            // TODO this sucks
            currentContext()->setLocalScopeIdentifier(QualifiedIdentifier("__kdevpythonlanguagesupport_import_helper"));
            openedDeclarations.append(d);
            openedTypes.append(moduleType);
        }
        for ( int i = remainingNameComponents.length() - 1; i >= 0; i-- ) {
            kDebug() << "closing context";
            closeType();
            closeContext();
            Declaration* d = openedDeclarations.at(i);
            if ( d ) {
                openedTypes[i]->setDeclaration(d);
                d->setType(openedTypes.at(i));
                d->setInternalContext(openedContexts.at(i));
            }
        }
        
        if ( injectingContext ) {
            closeInjectedContext();
        }
    }
    else {
        // import a specific declaration from the given file
        lock.lock();
        if ( declarationIdentifier->value == "*" ) {
            kDebug() << "Importing * from module";
            currentContext()->addImportedParentContext(moduleContext);
        }
        else {
            kDebug() << "Got module, importing declaration: " << moduleInfo.second;
            Declaration* originalDeclaration = findDeclarationInContext(moduleInfo.second, moduleContext);
            kDebug() << "Result: " << originalDeclaration;
            if ( originalDeclaration ) {
                DUChainWriteLocker lock(DUChain::lock());
                resultingDeclaration = visitVariableDeclaration<AliasDeclaration>(declarationIdentifier, range);
                if ( dynamic_cast<AliasDeclaration*>(resultingDeclaration) ) {
                    static_cast<AliasDeclaration*>(resultingDeclaration)->setAliasedDeclaration(originalDeclaration);
                    kDebug() << "Resulting alias: " << resultingDeclaration->toString();
                }
                else
                    kWarning() << "import declaration is being overwritten!";
            }
            else if ( createProblem != DontCreateProblems ) {
                KDevelop::Problem *p = new KDevelop::Problem();
                p->setFinalLocation(DocumentRange(currentlyParsedDocument(), range.castToSimpleRange())); // TODO ok?
                p->setSource(KDevelop::ProblemData::SemanticAnalysis);
                p->setSeverity(KDevelop::ProblemData::Warning);
                p->setDescription(i18n("Declaration for \"%1\" not found in specified module", moduleInfo.second.join(".")));
                ProblemPointer ptr(p);
                topContext()->addProblem(ptr);
            }
        }
    }
    return resultingDeclaration;
}

void DeclarationBuilder::visitYield(YieldAst* node)
{
    AstDefaultVisitor::visitYield(node);
    kDebug() << "visiting yield statement";
    DUChainReadLocker lock(DUChain::lock());
    ExpressionVisitor v(currentContext(), editor());
    v.visitNode(node->value);
    lock.unlock();
    setLastType(v.lastType());
    AbstractType::Ptr encountered = v.lastType();
    if ( node->value ) {
        if ( hasCurrentType() ) {
            if ( TypePtr<FunctionType> t = currentType<FunctionType>() ) {
                if ( VariableLengthContainer::Ptr previous = t->returnType().cast<VariableLengthContainer>() ) {
                    previous->addContentType(encountered);
                    t->setReturnType(previous.cast<AbstractType>());
                }
                else {
                    VariableLengthContainer::Ptr container = ExpressionVisitor::typeObjectForIntegralType("list", currentContext());
                    if ( container ) {
                        openType<VariableLengthContainer>(container);
                        container->addContentType(encountered);
                        t->setReturnType(Helper::mergeTypes(t->returnType(), container.cast<AbstractType>()));
                        closeType();
                    }
                }
            }
        }
    }
    setLastType(AbstractType::Ptr(0));
}

void DeclarationBuilder::visitLambda(LambdaAst* node)
{
    Python::AstDefaultVisitor::visitLambda(node);
    DUChainWriteLocker lock(DUChain::lock());
    openContext(node, editorFindRange(node, node->body), DUContext::Other);
    foreach ( ExpressionAst* argument, node->arguments->arguments ) {
        if ( argument->astType == Ast::NameAstType ) {
            Declaration* d = visitVariableDeclaration<Declaration>(static_cast<NameAst*>(argument));
            if ( d )  {
                d->setAbstractType(AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed)));
            }
        }
    }
    closeContext();
}

void DeclarationBuilder::visitCall(CallAst* node)
{
    Python::AstDefaultVisitor::visitCall(node);
    KDEBUG_BLOCK
    kDebug() << "Visiting call";
    DUChainReadLocker lock(DUChain::lock());
    ExpressionVisitor functionVisitor(currentContext(), editor());
    functionVisitor.visitNode(node);
    lock.unlock();
    kDebug() << functionVisitor.lastDeclaration();
    if ( node->function && node->function->astType == Ast::AttributeAstType && functionVisitor.lastDeclaration() ) {
        kDebug() << "Checking for list content updates...";
        lock.lock();
        ExpressionVisitor v(currentContext(), editor());
        v.visitNode(static_cast<AttributeAst*>(node->function)->value);
        lock.unlock();
        if ( VariableLengthContainer::Ptr container = v.lastType().cast<VariableLengthContainer>() ) {
            if ( v.lastDeclaration() ) {
//                 /// DEBUG
//                 kDebug() << "Got container type for eventual update: " << container->toString();
//                 kDebug() << "Eventual function declaration: " << functionVisitor.lastFunctionDeclaration()->toString();
//                 kDebug() << functionVisitor.lastFunctionDeclaration()->isFunctionDeclaration();
//                 /// END DEBUG
                if ( functionVisitor.lastDeclaration()->isFunctionDeclaration() ) {
                    FunctionDeclaration* f = static_cast<FunctionDeclaration*>(functionVisitor.lastDeclaration().data());
                    if ( const Decorator* d = Helper::findDecoratorByName<FunctionDeclaration>(f, "addsTypeOfArg") ) {
                        register const int offset = d->additionalInformation().str().toInt();
                        if ( node->arguments.length() > offset ) {
                            lock.lock();
                            ExpressionVisitor argVisitor(currentContext(), editor());
                            argVisitor.visitNode(node->arguments.at(offset));
                            lock.unlock();
                            if ( argVisitor.lastType() ) {
                                DUChainWriteLocker wlock(DUChain::lock());
                                kDebug() << "Adding content type: " << argVisitor.lastType()->toString();
                                container->addContentType(argVisitor.lastType());
                                v.lastDeclaration()->setType(container);
                            }
                        }
                    }
                    if ( const Decorator* d = Helper::findDecoratorByName<FunctionDeclaration>(f, "addsTypeOfArgContent") ) {
                        register const int offset = d->additionalInformation().str().toInt();
                        if ( node->arguments.length() > offset ) {
                            DUChainWriteLocker wlock(DUChain::lock());
                            ExpressionVisitor argVisitor(currentContext(), editor());
                            argVisitor.visitNode(node->arguments.at(offset));
                            if ( argVisitor.lastType() ) {
                                if ( VariableLengthContainer::Ptr sourceContainer = argVisitor.lastType().cast<VariableLengthContainer>() ) {
                                    if ( AbstractType::Ptr contentType = sourceContainer->contentType().abstractType() ) {
                                        kDebug() << "Adding content type: " << contentType->toString();
                                        container->addContentType(contentType);
                                        v.lastDeclaration()->setType(container);
                                    }
                                }
                                else if ( argVisitor.lastType()->whichType() == AbstractType::TypeUnsure ) {
                                    UnsureType::Ptr sourceUnsure = argVisitor.lastType().cast<UnsureType>();
                                    FOREACH_FUNCTION ( const IndexedType& type, sourceUnsure->types ) {
                                        if ( AbstractType::Ptr p = type.abstractType() ) {
                                            if ( VariableLengthContainer::Ptr sourceContainer = p.cast<VariableLengthContainer>() ) {
                                                if ( AbstractType::Ptr contentType = sourceContainer->contentType().abstractType() ) {
                                                    kDebug() << "Adding content type: " << contentType->toString();
                                                    container->addContentType(contentType);
                                                    v.lastDeclaration()->setType(container);
                                                }
                                            }
                                        }
                                    }
                                    v.lastDeclaration()->setType(container);
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    if ( ! m_prebuilding ) {
        return;
    }
    kDebug() << "--";
    kDebug() << "Trying to update function argument types based on call";
    
    lock.lock();   
    QPair<FunctionDeclaration::Ptr, bool> lastFunctionDeclarationP = Helper::functionDeclarationForCalledDeclaration(functionVisitor.lastDeclaration());
    FunctionDeclaration::Ptr lastFunctionDeclaration = lastFunctionDeclarationP.first;
    bool isConstructor = lastFunctionDeclarationP.second;
    
    if ( lastFunctionDeclaration ) {
        kDebug() << "got declaration:" << lastFunctionDeclaration->toString();
        if ( lastFunctionDeclaration->topContext()->url() == IndexedString(Helper::getDocumentationFile()) ) {
            kDebug() << "in documentation file, not modifying args";
            return;
        }
        kDebug() << "... and yep, it's a function declaration";
        DUContext* args = DUChainUtils::getArgumentContext(lastFunctionDeclaration.data());
        FunctionType::Ptr functiontype = lastFunctionDeclaration->type<FunctionType>();
        if ( args && functiontype ) {
            kDebug() << "got arguments";
            QVector<Declaration*> parameters = args->localDeclarations();
            if ( ( lastFunctionDeclaration->context()->type() == DUContext::Class || isConstructor ) && ! parameters.isEmpty() ) {
                parameters.remove(0);
            }
            int atParam = 0;
            if ( parameters.size() >= node->arguments.size() &&
                    functiontype->arguments().length() + static_cast<FunctionDeclarationPointer>(lastFunctionDeclaration)
                                                         ->defaultParametersSize() 
                        >= (uint) node->arguments.size() )
            {
                kDebug() << "... and they match the parameter size";
                lock.unlock();
                DUChainWriteLocker wlock(DUChain::lock());
                foreach ( ExpressionAst* arg, node->arguments ) {
                    if ( atParam >= functiontype->arguments().size() || atParam >= parameters.size() ) {
                        break;
                    }
                    ExpressionVisitor argumentVisitor(currentContext(), editor());
                    argumentVisitor.visitNode(arg);
                    kDebug() << "Got type for function argument: " << argumentVisitor.lastType();
                    if ( argumentVisitor.lastType() && Helper::isUsefulType(argumentVisitor.lastType().cast<AbstractType>()) ) {
                        kDebug() << "last type: " << argumentVisitor.lastType()->toString();
                        HintedType::Ptr addType = HintedType::Ptr(new HintedType());
                        openType(addType);
                        addType->setType(argumentVisitor.lastType());
                        addType->setCreatedBy(topContext(), m_futureModificationRevision);
                        closeType();
                        AbstractType::Ptr newType = Helper::mergeTypes(parameters.at(atParam)->abstractType(), 
                                                                        addType.cast<AbstractType>(), topContext());
                        kDebug() << "new type: " << newType->toString();
                        functiontype->removeArgument(atParam);
                        functiontype->addArgument(newType, atParam);
                        lastFunctionDeclaration->setAbstractType(functiontype.cast<AbstractType>());
                        parameters.at(atParam)->setType(newType);
                    }
                    atParam++;
                }
                lock.unlock();
            }
            else {
                kDebug() << "Arguments size mismatch, not updating type" << parameters << node->arguments;
            }
        }
    }
    else kDebug() << "No declaration for function, not setting arg types";
}

void DeclarationBuilder::visitAssignment(AssignmentAst* node)
{
    KDEBUG_BLOCK
    kDebug();
    AstDefaultVisitor::visitAssignment(node);
    QList<ExpressionAst*> realTargets;
    QList<AbstractType::Ptr> realValues;
    QList<DeclarationPointer> realDeclarations;
    QList<bool> isAlias;
    QList<Ast*> realNodes;
    
    foreach ( ExpressionAst* target, node->targets ) {
        if ( target->astType == Ast::TupleAstType ) {
            TupleAst* tuple = static_cast<TupleAst*>(target);
            foreach ( ExpressionAst* ast, tuple->elements ) {
                realTargets << ast;
            }
        }
        else {
            realTargets << target;
        }
    }
    
    if ( node->value && node->value->astType == Ast::TupleAstType ) {
        DUChainReadLocker lock(DUChain::lock());
        foreach ( ExpressionAst* value, static_cast<TupleAst*>(node->value)->elements ) {
            ExpressionVisitor v(currentContext(), editor());
            v.visitNode(value);
            realValues << v.lastType();
            realNodes << value;
            realDeclarations << v.lastDeclaration();
            isAlias << v.m_isAlias;
        }
        lock.unlock();
    }
    else {
        DUChainReadLocker lock(DUChain::lock());
        ExpressionVisitor v(currentContext(), editor());
        v.visitNode(node->value);
        lock.unlock();
        realValues << v.lastType();
        realNodes << node->value;
        realDeclarations << v.lastDeclaration();
        isAlias << v.m_isAlias;
        if ( node->value && node->value->astType == Ast::CallAstType && ! node->targets.isEmpty() ) {
            if ( v.lastType() && v.lastType()->whichType() == AbstractType::TypeIntegral 
                              && v.lastType().cast<IntegralType>()->dataType() == (uint) IntegralType::TypeVoid ) {
                KDevelop::Problem *p = new KDevelop::Problem();
                p->setFinalLocation(DocumentRange(currentlyParsedDocument(), simpleRangeForNode(node->targets.at(0), true)));
                p->setSource(KDevelop::ProblemData::SemanticAnalysis);
                p->setSeverity(KDevelop::ProblemData::Hint);
                p->setDescription(i18n("Assignment to call returning nothing"));
                ProblemPointer ptr(p);
                kDebug() << "Not adding return hint, documentation data is not good enough yet";
//                 topContext()->addProblem(ptr);
            }
        }
        lock.lock();
        kDebug() << ( v.lastType() ? v.lastType()->toString() : "< no last type >" ) << ( v.lastDeclaration() ? v.lastDeclaration()->toString() : "< no last declaration >" );
    }
    
    AbstractType::Ptr tupleElementType(0);
    DeclarationPointer tupleElementDeclaration(0);
    bool canUnpack = realTargets.length() == realValues.length();
    bool currentIsAlias = false;
    int i = 0;
    foreach ( ExpressionAst* target, realTargets ) {
        if ( canUnpack ) {
            tupleElementType = realValues.at(i);
            tupleElementDeclaration = realDeclarations.at(i);
            currentIsAlias = isAlias.at(i);
        }
        else if ( realTargets.length() == 1 ) {
            DUChainReadLocker lock(DUChain::lock());
            ExpressionVisitor v(currentContext());
            v.visitNode(node->value);
            lock.unlock();
            tupleElementType = v.lastType();
            tupleElementDeclaration = v.lastDeclaration();
            currentIsAlias = v.m_isAlias;
        }
        else {
            // add code for unpacking tuples here, once those are implemented.
            tupleElementType = AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed));
            tupleElementDeclaration = 0;
        }
        /** DEBUG **/
        if ( tupleElementType ) {
            VariableLengthContainer* d = dynamic_cast<VariableLengthContainer*>(tupleElementType.unsafeData());
            if ( d ) {
                DUChainReadLocker lock(DUChain::lock());
                kDebug() << "Got container type for declaration creation: " << tupleElementType << d->contentType();
                if ( d->contentType() ) {
                    kDebug() << "Content type: " << d->contentType().abstractType()->toString();
                }
            }
        }
        /** END DEBUG **/
        setLastType(tupleElementType); // TODO fix this for x, y = a, b, i.e. if node->value->astType == TupleAstType
        // "a = 3"
        if ( target->astType == Ast::NameAstType ) {
            if ( currentIsAlias ) {
                DUChainWriteLocker lock(DUChain::lock());
                kDebug() << "creating alias declaration for " << static_cast<NameAst*>(target)->identifier->value;
                AliasDeclaration* decl = openDeclaration<AliasDeclaration>(static_cast<NameAst*>(target)->identifier, target);
                decl->setAliasedDeclaration(tupleElementDeclaration.data());
                closeDeclaration();
            }
            else {
                DUChainWriteLocker lock(DUChain::lock());
                kDebug() << "Creating normal declaration with type" << ( tupleElementType ? tupleElementType->toString() : "<none>" );
                Declaration* dec = visitVariableDeclaration<Declaration>(target);
                /** DEBUG **/
                if ( tupleElementType && dec ) {
                    VariableLengthContainer* type = dynamic_cast<VariableLengthContainer*>(dec->abstractType().unsafeData());
                    kDebug() << "type is: " << dec->abstractType().unsafeData() << type << dynamic_cast<VariableLengthContainer*>(tupleElementType.unsafeData());
                    kDebug() << "Container: " << dynamic_cast<VariableLengthContainer*>(dec->abstractType().unsafeData());
                    Q_ASSERT(dec->abstractType());
                }
                /** END DEBUG **/
            }
        }
        // a[0] = 3
        else if ( target->astType == Ast::SubscriptAstType ) {
            SubscriptAst* subscript = static_cast<SubscriptAst*>(target);
            ExpressionAst* v = subscript->value;
            if ( tupleElementType ) {
                DUChainReadLocker lock(DUChain::lock());
                ExpressionVisitor targetVisitor(currentContext());
                targetVisitor.visitNode(v);
                VariableLengthContainer::Ptr cont = VariableLengthContainer::Ptr::dynamicCast(targetVisitor.lastType());
                if ( cont ) {
                    kDebug() << "has key type:" << cont->hasKeyType() << cont->toString();
                    kDebug() << cont.unsafeData();
                }
                if ( cont ) {
                    cont->addContentType(tupleElementType);
                }
                if ( cont and cont->hasKeyType() ) {
                    if ( subscript->slice and subscript->slice->astType == Ast::IndexAstType ) {
                        ExpressionVisitor keyVisitor(currentContext());
                        keyVisitor.visitNode(static_cast<IndexAst*>(subscript->slice)->value);
                        AbstractType::Ptr key = keyVisitor.lastType();
                        if ( key ) {
                            cont->addKeyType(key);
                        }
                    }
                }
                lock.unlock();
                if ( DeclarationPointer lastDecl = targetVisitor.lastDeclaration() ) {
                    DUChainWriteLocker wlock(DUChain::lock());
                    lastDecl->setAbstractType(cont.cast<AbstractType>());
                }
            }
        }
        // a.b = 3
        else if ( target->astType == Ast::AttributeAstType ) {
            AttributeAst* attrib = static_cast<AttributeAst*>(target);
            kDebug() << "Visiting attribute: " << attrib->attribute->value;
            // check whether the current attribute is undeclared, but the previos ones known
            // like in X.Y.Z = 3 where X and Y are defined, but Z isn't; then declare Z.
            DUChainReadLocker lock(DUChain::lock());
            ExpressionVisitor checkForUnknownAttribute(currentContext(), editor());
            checkForUnknownAttribute.visitNode(attrib);
            DeclarationPointer unknown = checkForUnknownAttribute.lastDeclaration();
            
            // declare the attribute.
            // however, if there's an earlier declaration which does not match the current position
            // (so it's really a different declaration) we skip this.
            Declaration* haveDeclaration = 0;
            if ( unknown ) {
                kDebug() << "Declaration is already created";
                haveDeclaration = unknown.data();
            }
            
            ExpressionVisitor checkPreviousAttributes(currentContext(), editor());
            checkPreviousAttributes.visitNode(attrib->value); // go "down one level", so only visit "X.Y"
            lock.unlock();
            
            DUContextPointer internal(0);
            DeclarationPointer parentObjectDeclaration = checkPreviousAttributes.lastDeclaration();
            AbstractType::Ptr type = checkPreviousAttributes.lastType();
            
            if ( ! parentObjectDeclaration ) {
                kDebug() << "No declaration for attribute base, aborting creation of attribute";
                continue;
            }
            // if foo is a class, this is like foo.bar = 3
            if ( parentObjectDeclaration->internalContext() ) {
                kDebug() << "Accessing class type directly";
                internal = parentObjectDeclaration->internalContext();
            }
            // while this is like A = foo(); A.bar = 3
            else {
                kDebug() << "Accessing class type through an instance, searching original declaration of type...";
                type = parentObjectDeclaration->abstractType();
                StructureType::Ptr structure(dynamic_cast<StructureType*>(type.unsafeData()));
                if ( ! structure || ! structure->declaration(topContext()) )
                    continue;
                parentObjectDeclaration = structure->declaration(topContext());
                internal = parentObjectDeclaration->internalContext();
                kDebug() << "... ok!";
            }
            if ( ! internal ) {
                kDebug() << "No internal context for structure type, aborting creation of attribute declaration";
                continue;
            }
            kDebug() << "Fine, got an internal context.";
            
            DUContext* previousContext = currentContext();
            
            bool isAlreadyOpen = contextAlreayOpen(internal);
            if ( isAlreadyOpen ) {
                activateAlreadyOpenedContext(internal);
                visitVariableDeclaration<ClassMemberDeclaration>(attrib->attribute, target, haveDeclaration);
                closeAlreadyOpenedContext(internal);
            }
            else {
                injectContext(internal.data());
                
                Declaration* dec = visitVariableDeclaration<ClassMemberDeclaration>(attrib->attribute, target, haveDeclaration);
                if ( dec ) {
                    dec->setRange(RangeInRevision(internal->range().start, internal->range().start));
                    dec->setAutoDeclaration(true);
                    DUChainWriteLocker lock(DUChain::lock());
                    previousContext->createUse(dec->ownIndex(), editorFindRange(attrib, attrib));
                    lock.unlock();
                }
                else kWarning() << "No declaration created for " << attrib->attribute << "as parent is not a class";
                
                closeInjectedContext();
            }
        }
        i += 1;
    }
}

void DeclarationBuilder::visitClassDefinition( ClassDefinitionAst* node )
{
    kDebug() << "opening class definition";
    
    DUChainWriteLocker lock(DUChain::lock());
    ClassDeclaration* dec = openDeclaration<ClassDeclaration>(identifierForNode(node->name),
                                                              editorFindRange(node->name, node->name));
    visitDecorators<ClassDeclaration>(node->decorators, dec);
    eventuallyAssignInternalContext();
    
    dec->setKind(KDevelop::Declaration::Type);
    dec->clearBaseClasses();
    dec->setClassType(ClassDeclarationData::Class);
    
    foreach ( ExpressionAst* c, node->baseClasses ) {
        ExpressionVisitor v(currentContext());
        v.visitNode(c);
        if ( v.lastType() && v.lastType()->whichType() == AbstractType::TypeStructure ) {
            StructureType::Ptr baseClassType = v.lastType().cast<StructureType>();
            BaseClassInstance base;
            base.baseClass = baseClassType->indexed();
            base.access = KDevelop::Declaration::Public;
            dec->addBaseClass(base);
        }
    }
    
    // check whether this is a type container (list, dict, ...) or just a "normal" class
    StructureType::Ptr type(0);
    const Decorator* d = Helper::findDecoratorByName<ClassDeclaration>(dec, "TypeContainer");
    if ( d ) {
        VariableLengthContainer* container = new VariableLengthContainer();
        if ( Helper::findDecoratorByName<ClassDeclaration>(dec, "hasTypedKeys") ) {
            container->setHasKeyType(true);
        }
        type = StructureType::Ptr(container);
    }
    if ( ! type ) {
        type = StructureType::Ptr(new StructureType());
    }
    type->setDeclaration(dec);
    dec->setType(type);
    
    openType(type);
    
    // needs to be done here, so the assignment of the internal context happens before visiting the body
    
    openContextForClassDefinition(node);
    dec->setInternalContext(currentContext());
    // yes, we do not call the context builder here, because contexts are already open
    lock.unlock();
    AstDefaultVisitor::visitClassDefinition( node );
    lock.lock();
    kDebug() << " --- closing CLASS context: " << currentContext()->range().castToSimpleRange();
    closeContext();
    
    closeType();
    
    closeDeclaration();
    
    dec->setComment(getDocstring(node->body));
}

template<typename T> void DeclarationBuilder::visitDecorators(QList< Python::ExpressionAst* > decorators, T* addTo) {
    foreach ( ExpressionAst* decorator, decorators ) {
        AstDefaultVisitor::visitNode(decorator);
        kDebug() << "decorator type: " << decorator->astType << "(name: " << Ast::NameAstType << ", call: " << Ast::CallAstType << ")";
        if ( decorator->astType == Ast::CallAstType ) {
            CallAst* call = static_cast<CallAst*>(decorator);
            Decorator d;
            if ( call->function->astType != Ast::NameAstType ) {
                continue;
            }
            d.setName(*static_cast<NameAst*>(call->function)->identifier);
            foreach ( ExpressionAst* arg, call->arguments ) {
                if ( arg->astType == Ast::NumberAstType ) {
                    d.setAdditionalInformation(static_cast<NumberAst*>(arg)->value);
                }
                else if ( arg->astType == Ast::StringAstType ) {
                    d.setAdditionalInformation(static_cast<StringAst*>(arg)->value);
                }
                break; // we only need the first argument for documentation analysis
            }
            kDebug() << "call decorator identifier: " << d.name() << *static_cast<NameAst*>(call->function)->identifier;
            addTo->addDecorator(d);
        }
        else if ( decorator->astType == Ast::NameAstType ) {
            NameAst* name = static_cast<NameAst*>(decorator);
            Decorator d;
            d.setName(*(name->identifier));
            kDebug() << "name decorator identifier: " << d.name() << *(name->identifier);
            addTo->addDecorator(d);
        }
    }
}

void DeclarationBuilder::visitFunctionDefinition( FunctionDefinitionAst* node )
{
    kDebug() << "opening function definition" << node->startLine << node->endLine;
    DeclarationPointer eventualParentDeclaration(currentDeclaration()); // an eventual containing class declaration
    FunctionType::Ptr type;
    
    DUChainWriteLocker lock(DUChain::lock());
    kDebug() << identifierForNode(node->name).toString();
    FunctionDeclaration* dec = openDeclaration<FunctionDeclaration>(identifierForNode(node->name),
                                                                    editorFindRange(node->name, node->name));
    Q_ASSERT(dec->isFunctionDeclaration());
    
    type = FunctionType::Ptr(new FunctionType());
    kDebug() << " <<< open function type";
    openType(type);
    dec->setInSymbolTable(false);
    kDebug() << "Declaration in symbol table:" << dec->inSymbolTable();
    dec->setType(type);
    
//     bool hasFirstArgument = false;
    
    visitDecorators<FunctionDeclaration>(node->decorators, dec);
    visitFunctionArguments(node);
    
    // this must be done here, because the type of self must be known when parsing the body
    kDebug() << "Checking whether we have to change argument types...";
    kDebug() <<  eventualParentDeclaration.data() << currentType<FunctionType>()->arguments().length() 
             << m_firstAttributeDeclaration.data() << currentContext()->type() << DUContext::Class;
    if ( eventualParentDeclaration && currentType<FunctionType>()->arguments().length() 
            && m_firstAttributeDeclaration.data() && currentContext()->type() == DUContext::Class ) {
        kDebug() << "Changing self argument type";
        kDebug() << "Arguments left: " << currentType<FunctionType>()->arguments().count();
        currentType<FunctionType>()->removeArgument(0);
        kDebug() << "Arguments left: " << currentType<FunctionType>()->arguments().count();
        DUChainWriteLocker lock(DUChain::lock());
        m_firstAttributeDeclaration->setAbstractType(eventualParentDeclaration->abstractType());
//         hasFirstArgument = true;
    }
        
    visitFunctionBody(node);

    closeDeclaration();
    eventuallyAssignInternalContext();

    kDebug() << " >>> close function type";
    closeType();
    
    // python methods don't have their parents attributes directly inside them
    if ( eventualParentDeclaration && eventualParentDeclaration->internalContext() && dec->internalContext() ) {
        dec->internalContext()->removeImportedParentContext(eventualParentDeclaration->internalContext());
    }
    
    {
        DUChainWriteLocker lock(DUChain::lock());
        if ( ! type->returnType() ) {
            type->setReturnType(AbstractType::Ptr(new IntegralType(IntegralType::TypeVoid)));
        }
        dec->setType(type);
    }
    
    DUContext* args = DUChainUtils::getArgumentContext(dec);
    if ( args )  {
        QVector<Declaration*> parameters = args->localDeclarations();

        if ( currentContext()->type() == DUContext::Class && ! parameters.isEmpty() ) {
            if ( parameters[0]->identifier().identifier() != IndexedString("self") ) {
                kDebug() << "argument is not called self, but instead:" << parameters[0]->identifier().identifier().str();
                KDevelop::Problem *p = new KDevelop::Problem();
                p->setFinalLocation(DocumentRange(currentlyParsedDocument(), SimpleRange(node->startLine, node->startCol, node->startLine, 10000)));
                p->setSource(KDevelop::ProblemData::SemanticAnalysis);
                p->setSeverity(KDevelop::ProblemData::Warning);
                p->setDescription(i18n("First argument of class method is not called self, this is deprecated"));
                ProblemPointer ptr(p);
                topContext()->addProblem(ptr);
            }
            m_firstAttributeDeclaration = DeclarationPointer(0);
        }
        else if ( currentContext()->type() == DUContext::Class && parameters.isEmpty() ) {
            DUChainWriteLocker lock(DUChain::lock());
            KDevelop::Problem *p = new KDevelop::Problem();
            p->setFinalLocation(DocumentRange(currentlyParsedDocument(), SimpleRange(node->startLine, node->startCol, node->startLine, 10000))); // only mark first line
            p->setSource(KDevelop::ProblemData::SemanticAnalysis);
            p->setSeverity(KDevelop::ProblemData::Warning);
            p->setDescription(i18n("Non-static class method without arguments, must have at least one (self)"));
            ProblemPointer ptr(p);
            topContext()->addProblem(ptr);
        }
    }
    
    // check for documentation
    dec->setComment(getDocstring(node->body));
    dec->setInSymbolTable(true);
}

QString DeclarationBuilder::getDocstring(QList< Ast* > body)
{
    if ( body.length() && body.first()->astType == Ast::ExpressionAstType 
            && static_cast<ExpressionAst*>(body.first())->value->astType == Ast::StringAstType ) {
        StringAst* docstring = static_cast<StringAst*>(static_cast<ExpressionAst*>(body.first())->value);
        kDebug() << "Got docstring for declaration";
        return docstring->value.trimmed();
    }
    return QString("");
}

void DeclarationBuilder::visitReturn(ReturnAst* node)
{
    kDebug() << "visiting return statement";
    DUChainReadLocker lock(DUChain::lock());
    ExpressionVisitor v(currentContext(), editor());
    v.visitNode(node->value);
    lock.unlock();
    setLastType(v.lastType());
    if ( node->value ) {
        if ( ! hasCurrentType() ) {
            DUChainWriteLocker lock(DUChain::lock());
            KDevelop::Problem *p = new KDevelop::Problem();
            p->setFinalLocation(DocumentRange(currentlyParsedDocument(), SimpleRange(node->startLine, node->startCol, node->endLine, node->endCol))); // only mark first line
            p->setSource(KDevelop::ProblemData::SemanticAnalysis);
            p->setDescription(i18n("Return statement not within function declaration"));
            ProblemPointer ptr(p);
            topContext()->addProblem(ptr);
            return;
        }
        TypePtr<FunctionType> t = currentType<FunctionType>();
        AbstractType::Ptr encountered = v.lastType();
//         kDebug() << "Found type: " << encountered->toString();
        t->setReturnType(Helper::mergeTypes(t->returnType(), encountered));
    }
    setLastType(AbstractType::Ptr(0));
    DeclarationBuilderBase::visitReturn(node);
}

void DeclarationBuilder::visitArguments( ArgumentsAst* node )
{
    DUChainWriteLocker lock(DUChain::lock());
    kDebug() << "Current context for parameters: " << currentContext();
    kDebug() << currentContext()->scopeIdentifier().toString();
    if ( currentDeclaration() ) kDebug() << currentDeclaration()->identifier().toString();
    
    
    if ( currentDeclaration() and currentDeclaration()->isFunctionDeclaration() ) {
        static_cast<FunctionDeclaration*>(currentDeclaration())->clearDefaultParameters();
        if ( hasCurrentType() and currentType<FunctionType>() ) {
            FunctionType::Ptr type = currentType<FunctionType>();
            NameAst* realParam = 0;
            bool isFirst = true;
            int defaultParametersCount = node->defaultValues.length();
            int parametersCount = node->arguments.length();
            int firstDefaultParameterOffset = parametersCount - defaultParametersCount;
            int currentIndex = 0;
            kDebug() << "variable argument ranges: " << node->arg_lineno << node->arg_col_offset << node->vararg_lineno << node->vararg_col_offset;
            foreach ( ExpressionAst* expression, node->arguments ) {
                currentIndex += 1;
                realParam = dynamic_cast<NameAst*>(expression);
                
                if ( ! realParam || realParam->context != ExpressionAst::Parameter ) continue;
                
                setLastType(AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed)));
                Declaration* paramDeclaration = visitVariableDeclaration<Declaration>(realParam);
                
                if ( type && paramDeclaration && currentIndex > firstDefaultParameterOffset ) {
                    kDebug() << "Adding default argument: " << realParam->identifier->value << paramDeclaration->abstractType();
                    // find type of given default value
                    ExpressionVisitor v(currentContext());
                    v.visitNode(node->defaultValues.at(currentIndex - firstDefaultParameterOffset - 1));
                    if ( v.lastType() ) {
                        type->addArgument(v.lastType());
                    }
                    else {
                        type->addArgument(AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed)));
                    }
                    static_cast<FunctionDeclaration*>(currentDeclaration())->addDefaultParameter(paramDeclaration->identifier().identifier());
                    kDebug() << "Arguments count: " << type->arguments().length();
                }
                else {
                    kDebug() << "Not a default argument: " << realParam->identifier->value;
                    type->addArgument(AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed)));
                }
                if ( isFirst ) {
                    m_firstAttributeDeclaration = DeclarationPointer(paramDeclaration);
                    isFirst = false;
                }
            }
            if ( node->vararg ) {
                DUChainReadLocker lock(DUChain::lock());
                AbstractType::Ptr listType = ExpressionVisitor::typeObjectForIntegralType("list", currentContext()).cast<AbstractType>();
                lock.unlock();
                type->addArgument(listType);
                node->vararg->startCol = node->vararg_col_offset; node->vararg->endCol = node->vararg_col_offset + node->vararg->value.length() - 1;
                node->vararg->startLine = node->vararg_lineno; node->vararg->endLine = node->vararg_lineno;
                Declaration* d = visitVariableDeclaration<Declaration>(node->vararg);
                Q_ASSERT(d);
                d->setAbstractType(listType);
            }
            if ( node->kwarg ) {
                DUChainReadLocker lock(DUChain::lock());
                AbstractType::Ptr dictType = ExpressionVisitor::typeObjectForIntegralType("dict", currentContext()).cast<AbstractType>();
                lock.unlock();
                type->addArgument(dictType);
                node->kwarg->startCol = node->arg_col_offset; node->kwarg->endCol = node->arg_col_offset + node->kwarg->value.length() - 1;
                node->kwarg->startLine = node->arg_lineno; node->kwarg->endLine = node->arg_lineno;
                Declaration* d = visitVariableDeclaration<Declaration>(node->kwarg);
                Q_ASSERT(d);
                d->setAbstractType(dictType);
            }
        }
    }
    
    DeclarationBuilderBase::visitArguments(node);
}

}


