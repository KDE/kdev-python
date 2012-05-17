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
#include <language/duchain/declaration.h>
#include <language/duchain/duchain.h>
#include <language/duchain/types/alltypes.h>
#include <language/duchain/classdeclaration.h>
#include <language/duchain/declaration.h>
#include <language/duchain/builders/abstracttypebuilder.h>
#include <language/duchain/aliasdeclaration.h>
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

DeclarationBuilder::DeclarationBuilder(PythonEditorIntegrator* editor)
        : DeclarationBuilderBase( )
{
    setEditor(editor);
    kDebug() << "Building Declarations";
}

DeclarationBuilder:: ~DeclarationBuilder()
{
    if ( ! m_scheduledForDeletion.isEmpty() ) {
        DUChainWriteLocker lock;
        foreach ( DUChainBase* d, m_scheduledForDeletion ) {
            delete d;
        }
        m_scheduledForDeletion.clear();
    }
}

void DeclarationBuilder::setPrebuilding(bool prebuilding)
{
    m_prebuilding = prebuilding;
}

ReferencedTopDUContext DeclarationBuilder::build(const IndexedString& url, Ast* node, ReferencedTopDUContext updateContext)
{
    // The declaration builder needs to run twice, so it can resolve uses of e.g. functions
    // which are called before they are defined (which is easily possible, due to python's dynamic nature).
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
    if ( lastContext() ) {
        DUChainReadLocker lock(DUChain::lock());
        currentDeclaration()->setKind(Declaration::Type);
    }
    
    Q_ASSERT(currentDeclaration()->alwaysForceDirect());

    eventuallyAssignInternalContext();

    DeclarationBuilderBase::closeDeclaration();
}

template<typename T> T* DeclarationBuilder::eventuallyReopenDeclaration(Identifier* name, Ast* range, FitDeclarationType mustFitType)
{
    QList<Declaration*> existingDeclarations = existingDeclarationsForNode(name);
    
    Declaration* dec = 0;
    reopenFittingDeclaration<T>(existingDeclarations, mustFitType, editorFindRange(range, range), &dec);
    bool declarationOpened = (bool) dec;
    if ( ! declarationOpened ) {
        dec = openDeclaration<T>(name, range);
    }
    Q_ASSERT(dynamic_cast<T*>(dec));
    return static_cast<T*>(dec);
}

template<typename T> T* DeclarationBuilder::visitVariableDeclaration(Ast* node, Declaration* previous, AbstractType::Ptr type)
{
    if ( node->astType == Ast::NameAstType ) {
        NameAst* currentVariableDefinition = static_cast<NameAst*>(node);
        // those contexts can invoke a variable declaration
        // this prevents "bar" from being declared in something like "foo = bar"
        // This is just a sanity check, the code should never request creation of a variable
        // in such cases.
        QList<ExpressionAst::Context> declaringContexts;
        declaringContexts << ExpressionAst::Store << ExpressionAst::Parameter << ExpressionAst::AugStore;
        if ( ! declaringContexts.contains(currentVariableDefinition->context) ) {
            return 0;
        }
        Identifier* id = currentVariableDefinition->identifier;
        return visitVariableDeclaration<T>(id, currentVariableDefinition, previous, type);
    }
    else if ( node->astType == Ast::IdentifierAstType ) {
        return visitVariableDeclaration<T>(static_cast<Identifier*>(node), 0, previous, type);
    }
    else {
        kWarning() << "cannot create variable declaration for non-(name|identifier) AST, this is a programming error";
        return static_cast<T*>(0);
    }
}

template<typename T> T* DeclarationBuilder::visitVariableDeclaration(Identifier* node, RangeInRevision range, AbstractType::Ptr type)
{
    Ast* pseudo = new Ast();
    pseudo->startLine = range.start.line; pseudo->startCol = range.start.column;
    pseudo->endLine = range.end.line; pseudo->endCol = range.end.column;
    T* result = visitVariableDeclaration<T>(node, pseudo, 0, type);
    delete pseudo;
    return result;
}

QList< Declaration* > DeclarationBuilder::existingDeclarationsForNode(Identifier* node)
{
    /**DBG**/
    kDebug() << "Current context: " << currentContext()->scopeIdentifier() << currentContext()->range().castToSimpleRange();
    kDebug() << "Looking for node identifier:" << identifierForNode(node) << identifierForNode(node).last();
    /** /DBG **/
    QList<Declaration*> existingDeclarations = currentContext()->findDeclarations(identifierForNode(node).last(),  // <- WARNING first / last?
                                                                CursorInRevision::invalid(), 0,
                                                                (DUContext::SearchFlag) ( DUContext::DontSearchInParent | DUContext::DontResolveAliases) );
    // append arguments context
    if ( m_mostRecentArgumentsContext ) {
        QList<Declaration*> args = m_mostRecentArgumentsContext->findDeclarations(identifierForNode(node).last(),
                                                                                  CursorInRevision::invalid(), 0, DUContext::DontSearchInParent);
        existingDeclarations.append(args);
    }
    return existingDeclarations;
}

DeclarationBuilder::FitDeclarationType DeclarationBuilder::kindForType(AbstractType::Ptr type, bool isAlias)
{
    if ( type ) {
        if ( type->whichType() == AbstractType::TypeFunction ) {
            return FunctionDeclarationType;
        }
    }
    if ( isAlias ) {
        return AliasDeclarationType;
    }
    return InstanceDeclarationType;
}

template<typename T> QList<Declaration*> DeclarationBuilder::reopenFittingDeclaration(QList<Declaration*> declarations, FitDeclarationType mustFitType,
                                                                                      RangeInRevision updateRangeTo, Declaration** ok)
{
    // Search for a declaration from a previous parse pass which should be re-used
    kDebug() << "Found " << declarations.length() << "declarations";
    QList<Declaration*> remainingDeclarations;
    *ok = 0;
    foreach ( Declaration* d, declarations ) {
        Declaration* fitting = dynamic_cast<T*>(d);
        if ( ! fitting ) {
            // Only use a declaration if the type matches
            kDebug() << "skipping" << d->toString() << "which could not be cast to the requested type";
            continue;
        }
        // Do not use declarations which have been encountered previously;
        // this function only handles declarations from previous parser passes which have not
        // been encountered yet in this pass
        bool reallyEncountered = wasEncountered(d) && ! m_scheduledForDeletion.contains(d);
        bool invalidType = false;
        if ( d && d->abstractType() && mustFitType != NoTypeRequired ) {
            invalidType = ( ( d->isFunctionDeclaration() ) != ( mustFitType == FunctionDeclarationType ) );
            if ( ! invalidType ) {
                invalidType = ( ( dynamic_cast<AliasDeclaration*>(d) != 0 ) != ( mustFitType == AliasDeclarationType ) );
            }
        }
        kDebug() << "last one: " << d << d->toString() << fitting << reallyEncountered << invalidType;
        
        if ( fitting && ! reallyEncountered && ! invalidType ) {
            if ( d->topContext() == currentContext()->topContext() ) {
                kDebug() << "Opening previously existing declaration for " << d->toString();
                openDeclarationInternal(d);
                d->setRange(updateRangeTo);
                *ok = d;
                setEncountered(d);
                break;
            }
            else {
                kDebug() << "Not opening previously existing declaration because it's in another top context";
            }
        }
        else if ( fitting && ! invalidType ) {
            remainingDeclarations << d;
        }
    }
    return remainingDeclarations;
}

typedef QPair<Declaration*, int> p;
template<typename T> T* DeclarationBuilder::visitVariableDeclaration(Identifier* node, Ast* originalAst, Declaration* previous, AbstractType::Ptr type)
{
    DUChainWriteLocker lock(DUChain::lock());
    Ast* rangeNode = originalAst ? originalAst : node;
    RangeInRevision range = editorFindRange(rangeNode, rangeNode);
    
    // If no type is known, display "mixed".
    if ( ! type ) {
        type = AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed));
    }
    
    kDebug() << "Parsing variable declaration: " << node->value;
    
    QList<Declaration*> existingDeclarations;
    if ( previous ) {
        existingDeclarations << previous;
    }
    else {
        // declarations declared at an earlier range in this top-context
        existingDeclarations = existingDeclarationsForNode(node);
    }
    
    // declaration existing in a previous version of this top-context
    Declaration* dec = 0;
    existingDeclarations = reopenFittingDeclaration<T>(existingDeclarations, kindForType(type), range, &dec);
    bool declarationOpened = (bool) dec;
    
    kDebug() << "VARIABLE CONTEXT: " << currentContext()->scopeIdentifier() << currentContext()->range().castToSimpleRange() << currentContext()->type() << DUContext::Class;
    
    // tells whether the declaration found for updating is in the same top context
    bool inSameTopContext = true;
    // tells whether there's fitting declarations to update (update is not the same as re-open! one is for
    // code which uses the same variable twice, the other is for multiple passes of the parser)
    bool haveFittingDeclaration = false;
    if ( ! existingDeclarations.isEmpty() and existingDeclarations.last() ) {
        Declaration* d = Helper::resolveAliasDeclaration(existingDeclarations.last());
        if ( d and d->topContext() != topContext() ) {
            inSameTopContext = false;
        }
        if ( dynamic_cast<T*>(existingDeclarations.last()) ) {
            haveFittingDeclaration = true;
        }
    }
    if ( currentContext() && currentContext()->type() == DUContext::Class && ! haveFittingDeclaration ) {
        // If the current context is a class, then this is a class member variable.
        kDebug() << "Creating class member declaration for " << node->value << node->startLine << ":" << node->startCol;
        kDebug() << "Context type: " << currentContext()->scopeIdentifier() << currentContext()->range().castToSimpleRange();
        if ( ! dec ) {
            dec = openDeclaration<ClassMemberDeclaration>(node, originalAst ? originalAst : node);
            Q_ASSERT(! declarationOpened);
            declarationOpened = true;
        }
        if ( declarationOpened ) {
            DeclarationBuilderBase::closeDeclaration();
        }
        dec->setType(AbstractType::Ptr(type));
        dec->setKind(KDevelop::Declaration::Instance);
    } else if ( ! haveFittingDeclaration ) {
        // This name did not previously appear in the user code, so a new variable is declared
        RangeInRevision range = editorFindRange(rangeNode, rangeNode);
        kDebug() << "Creating variable declaration for " << range;
        kDebug() << "which has type" << ( dec && dec->abstractType() ? dec->abstractType()->toString() : "none" );
        // check whether a declaration from a previous parser pass must be updated
        if ( ! dec ) {
            kDebug() << "This declaration is a new one, with range" << range;
            dec = openDeclaration<T>(node, rangeNode);
            Q_ASSERT(! declarationOpened);
            declarationOpened = true;
        }
        else {
            dec->setRange(range);
        }
        if ( declarationOpened ) {
            DeclarationBuilderBase::closeDeclaration();
        }
        // check for argument type hints (those are created when calling functions)
        UnsureType::Ptr hints = Helper::extractTypeHints(dec->abstractType(), topContext());
        kDebug() << "Type Hints: " << hints->toString();
        AbstractType::Ptr newType = Helper::mergeTypes(hints.cast<AbstractType>(), type, topContext());
        kDebug() << "Resulting type: " << newType->toString();
        dec->setType(newType);
        dec->setKind(KDevelop::Declaration::Instance);
    }
    else if ( inSameTopContext ) {
        // The name appeared previously in the user code, so no new variable is declared, but just
        // the type is modified accordingly.
        kDebug() << "Existing declarations are not empty. count: " << existingDeclarations.count();
        dec = existingDeclarations.last();
        AbstractType::Ptr currentType = dec->abstractType();
        AbstractType::Ptr newType = type;
        if ( newType ) {
            if ( currentType && currentType->indexed() != newType->indexed() ) {
                // If the previous and new type are different, use an unsure type
                dec->setType(Helper::mergeTypes(currentType, newType, topContext()));
            }
            else {
                // If no type was set previously, use only the new one.
                kDebug() << "Existing declaration with no type from last declaration.";
                dec->setType(AbstractType::Ptr(type));
            }
        }
        else {
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
    if ( node->name && node->name->astType == Ast::NameAstType ) {
        // Python allows to assign the caught exception to a variable; create that variable if required.
        DUChainReadLocker lock(DUChain::lock());
        ExpressionVisitor v(currentContext(), editor());
        v.visitNode(node->type);
        lock.unlock();
        visitVariableDeclaration<Declaration>(node->name, 0, v.lastType());
    }
    DeclarationBuilderBase::visitExceptionHandler(node);
}

void DeclarationBuilder::visitWith(WithAst* node)
{
    if ( node->optionalVars ) {
        // For statements like "with open(f) as x", a new variable must be created; do this here.
        DUChainReadLocker lock(DUChain::lock());
        ExpressionVisitor v(currentContext(), editor());
        v.visitNode(node->contextExpression);
        lock.unlock();
        visitVariableDeclaration<Declaration>(node->optionalVars, 0, v.lastType());
    }
    Python::ContextBuilder::visitWith(node);
}

void DeclarationBuilder::visitFor(ForAst* node)
{
    DUChainWriteLocker lock(DUChain::lock());
    ExpressionVisitor v(currentContext(), editor());
    v.visitNode(node->iterator);
    lock.unlock();
    VariableLengthContainer::Ptr iteratorList = v.lastType().cast<VariableLengthContainer>();
    if ( node->target->astType == Ast::NameAstType ) {
        // In case the iterator variable is a Name ("for x in range(3)"), just create a declaration for it.
        // The following code tries to figure out the type of "x" from the object that is being iterated over.
        AbstractType::Ptr iteratorType;
        if ( iteratorList && iteratorList->contentType() ) {
            // If the object being iterated over is a simple list or similar, use its content type.
            iteratorType = iteratorList->contentType().abstractType();
        }
        else if ( v.lastType() && v.lastType()->whichType() == AbstractType::TypeUnsure ) {
            // If the object being iterated over *might* be a list, consider all possibilities.
            UnsureType::Ptr u = v.lastType().cast<UnsureType>();
            for ( uint i = 0; i < u->typesSize(); i++ ) {
                if ( VariableLengthContainer::Ptr typeInUnsure = u->types()[i].abstractType().cast<VariableLengthContainer>() ) {
                    if ( ! iteratorType ) {
                        iteratorType = typeInUnsure->contentType().abstractType();
                    }
                    else {
                        iteratorType = Helper::mergeTypes(iteratorType, typeInUnsure->contentType().abstractType());
                    }
                }
            }
        }
        else {
            // No list type whatsoever was available for the iterator list, so just display "mixed".
            iteratorType = AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed));
        }
        // Create the variable declaration for the iterator variable with the type that has been determined.
        visitVariableDeclaration<Declaration>(node->target, 0, iteratorType);
    }
    else if ( node->target->astType == Ast::TupleAstType ) {
        // If the target is a tuple ("for x, y, z in ..."), multiple variables must be declared.
        // For now, types of those variables will only be determined if the iterator list is a dictionary.
        short atElement = 0;
        foreach ( ExpressionAst* tupleMember, static_cast<TupleAst*>(node->target)->elements ) {
            if ( tupleMember->astType == Ast::NameAstType ) {
                AbstractType::Ptr newType;
                if ( atElement == 0 && iteratorList && iteratorList->keyType() ) {
                    newType = iteratorList->keyType().abstractType();
                }
                else if ( atElement == 1 && iteratorList && iteratorList->contentType() ) {
                    newType = iteratorList->contentType().abstractType();
                }
                else {
                    newType = AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed));
                }
                visitVariableDeclaration<Declaration>(tupleMember, 0, newType);
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
    // TODO make this a bit faster, it wastes time
    Declaration* lastAccessedDeclaration = 0;
    int i = 0;
    int identifierCount = dottedNameIdentifier.length();
    foreach ( QString currentIdentifier, dottedNameIdentifier ) {
        Q_ASSERT(currentContext);
        i++;
        QList<Declaration*> declarations = currentContext->findDeclarations(QualifiedIdentifier(currentIdentifier).first(),
                                                                            CursorInRevision::invalid(), 0, DUContext::NoFiltering);
        // break if the list of identifiers is not yet totally worked through and no
        // declaration with an internal context was found
        if ( declarations.isEmpty() or ( not declarations.last()->internalContext() and identifierCount != i ) ) {
            kDebug() << "Declaration not found: " << dottedNameIdentifier << "in top context" << ctx->url().toUrl().path();
            return 0;
        }
        else {
            lastAccessedDeclaration = declarations.last();
            currentContext = lastAccessedDeclaration->internalContext();
        }
    }
    return lastAccessedDeclaration;
}

void DeclarationBuilder::visitImportFrom(ImportFromAst* node)
{
    Python::AstDefaultVisitor::visitImportFrom(node);
    QString moduleName;
    QString declarationName;
    foreach ( AliasAst* name, node->names ) {
        // iterate over all the names that are imported, like "from foo import bar as baz, bang as asdf"
        if ( node->module ) {
            moduleName = node->module->value + "." + name->name->value;
        }
        else {
            moduleName = "." + name->name->value;
        }
        Identifier* declarationIdentifier = 0;
        declarationName = "";
        if ( name->asName ) {
            // use either the alias ("as foo"), or the object name itself if no "as" is given
            declarationIdentifier = name->asName;
            declarationName = name->asName->value;
        }
        else {
            declarationIdentifier = name->name;
            declarationName = name->name->value;
        }
        // This is a bit hackish, it tries to find the specified object twice twice -- once it tries to
        // import the name from a module's __init__.py file, and once from a "real" python file
        // TODO improve this code-wise
        Declaration* success = createModuleImportDeclaration(moduleName, declarationName, declarationIdentifier, 0, DontCreateProblems);
        if ( not success and node->module ) {
            QString modifiedModuleName = node->module->value + ".__init__." + name->name->value;
            createModuleImportDeclaration(modifiedModuleName, declarationName, declarationIdentifier);
        }
    }
}

void DeclarationBuilder::visitComprehension(ComprehensionAst* node)
{
    Python::AstDefaultVisitor::visitComprehension(node);
    kDebug() << "visiting comprehension" << currentContext()->range();
    // make the declaration zero chars long; it must appear at the beginning of the context,
    // because it is actually used *before* its real declaration: [foo for foo in bar]
    // The DUChain doesn't like this, so for now, the declaration is at the opening bracket,
    // and both other occurences are uses of that declaration.
    // TODO add a special case to the usebuilder to display the second occurence as a declaration
    RangeInRevision declarationRange(currentContext()->range().start, currentContext()->range().start);
    declarationRange.end.column -= 1;
    kDebug() << "declaration range: " << declarationRange;
    
    AbstractType::Ptr targetType(new IntegralType(IntegralType::TypeMixed));
    if ( node->iterator ) {
        // try to find the type of the object being iterated over, for guessing the
        // type of the iterator variable
        DUChainReadLocker lock(DUChain::lock());
        ExpressionVisitor v(currentContext());
        v.visitNode(node->iterator);
        lock.unlock();
        if ( VariableLengthContainer* container = dynamic_cast<VariableLengthContainer*>(v.lastType().unsafeData()) ) {
            targetType = container->contentType().abstractType();
        }
    }
    
    // create variable declarations for the iterator variable(s)
    if ( node->target->astType == Ast::NameAstType ) {
        visitVariableDeclaration<Declaration>(static_cast<NameAst*>(node->target)->identifier, declarationRange, targetType);
    }
    if ( node->target->astType == Ast::TupleAstType ) {
        foreach ( ExpressionAst* tupleElt, static_cast<TupleAst*>(node->target)->elements ) {
            if ( tupleElt->astType == Ast::NameAstType ) {
                NameAst* n = static_cast<NameAst*>(tupleElt);
                visitVariableDeclaration<Declaration>(n->identifier, declarationRange);
                // TODO: Fix this as soon as tuple type support is implemented.
//                 DUChainWriteLocker lock(DUChain::lock());
//                 d->setAbstractType(AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed)));
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
        createModuleImportDeclaration(moduleName, declarationIdentifier->value, declarationIdentifier);
    }
}

void DeclarationBuilder::scheduleForDeletion(DUChainBase* d, bool doschedule)
{
    if ( doschedule ) {
        m_scheduledForDeletion.append(d);
    }
    else {
        m_scheduledForDeletion.removeAll(d);
    }
}


Declaration* DeclarationBuilder::createDeclarationTree(const QStringList& nameComponents, Identifier* declarationIdentifier,
                                       const ReferencedTopDUContext& innerCtx, Declaration* aliasDeclaration,
                                       const RangeInRevision& range)
{
    // This actually handles two use cases which are very similar -- thus this check:
    // There might be either one declaration which should be imported from another module,
    // or there might be a whole context. In "import foo.bar", the "bar" might be either
    // a single class/function/whatever, or a whole file to import.
    // NOTE: The former case can't actually happen in python, it's not allowed. However,
    // it is still handled here, because it's very useful for documentation files (pyQt for example
    // makes heavy use of that feature).
    Q_ASSERT( ( innerCtx.data() or aliasDeclaration ) && "exactly one of innerCtx or aliasDeclaration must be provided");
    Q_ASSERT( ( not innerCtx.data() or not aliasDeclaration ) && "exactly one of innerCtx or aliasDeclaration must be provided");
    
    kDebug() << "creating declaration tree for" << nameComponents;
    
    Declaration* lastDeclaration = 0;
    int depth = 0;
    
    // check for already existing trees to update
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
        kDebug() << "remaining identifiers:" << remainingNameComponents;
    }
    else {
        remainingNameComponents = nameComponents;
        extendingPreviousImportCtx = topContext();
    }
    
    // now, proceed in creating the declaration tree with whatever context
    QList<Declaration*> openedDeclarations;
    QList<StructureType::Ptr> openedTypes;
    QList<DUContext*> openedContexts;
    
    RangeInRevision displayRange = RangeInRevision::invalid();
    
    DUChainWriteLocker lock(DUChain::lock());
    for ( int i = 0; i < remainingNameComponents.length(); i++ ) {
        // Iterate over all the names, and create a declaration + sub-context for each of them
        const QString& component = remainingNameComponents.at(i);
        Identifier* temporaryIdentifier = new Identifier(component);
        Declaration* d = 0;
        temporaryIdentifier->copyRange(declarationIdentifier);
        temporaryIdentifier->endCol = temporaryIdentifier->startCol;
        temporaryIdentifier->startCol += 1;
        displayRange = editorFindRange(temporaryIdentifier, temporaryIdentifier); // TODO fixme
        
        bool done = false;
        if ( aliasDeclaration && i == remainingNameComponents.length() - 1 ) {
            // it's the last level, so if we have an alias declaration create it and stop
            if (    aliasDeclaration->isFunctionDeclaration() 
                 || dynamic_cast<ClassDeclaration*>(aliasDeclaration) 
                 || dynamic_cast<AliasDeclaration*>(aliasDeclaration) 
               ) {
                aliasDeclaration = Helper::resolveAliasDeclaration(aliasDeclaration);
                AliasDeclaration* adecl = eventuallyReopenDeclaration<AliasDeclaration>(temporaryIdentifier, temporaryIdentifier, AliasDeclarationType);
                if ( adecl ) {
                    adecl->setAliasedDeclaration(aliasDeclaration);
                }
                d = adecl;
                closeDeclaration();
            }
            else {
                d = visitVariableDeclaration<Declaration>(temporaryIdentifier);
                d->setAbstractType(aliasDeclaration->abstractType());
            }
            openedDeclarations.append(d);
            done = true;
        }
        
        if ( ! done ) {
            // create the next level of the tree hierarchy if not done yet.
            d = visitVariableDeclaration<Declaration>(temporaryIdentifier);
        }
        if ( d ) {
            if ( topContext() != currentContext() ) {
                d->setRange(RangeInRevision(currentContext()->range().start, currentContext()->range().start));
            }
            else {
                d->setRange(displayRange);
            }
            d->setAutoDeclaration(true);
            currentContext()->createUse(d->ownIndex(), displayRange);
            kDebug() << "really encountered:" << d << "; scheduled:" << m_scheduledForDeletion;
            kDebug() << d->toString();
            scheduleForDeletion(d, false);
            kDebug() << "scheduled:" << m_scheduledForDeletion;
        }
        if ( done ) break;
        
        kDebug() << "creating context for " << component;
        // otherwise, create a new "level" entry (a pseudo type + context + declaration which contains all imported items)
        StructureType::Ptr moduleType = StructureType::Ptr(new StructureType());
        openType(moduleType);
        
        openedContexts.append(openContext(declarationIdentifier, KDevelop::DUContext::Other));
        
        foreach ( Declaration* local, currentContext()->localDeclarations() ) {
            // keep all the declarations until the builder finished
            // kdevelop would otherwise delete them as soon as the context is closed
            if ( ! wasEncountered(local) ) {
                setEncountered(local);
                scheduleForDeletion(local, true);
            }
        }
        
        openedDeclarations.append(d);
        openedTypes.append(moduleType);
        if ( i == remainingNameComponents.length() - 1 ) {
            if ( innerCtx ) {
                kDebug() << "adding imported context to inner declaration";
                currentContext()->addImportedParentContext(innerCtx);
            }
            else if ( aliasDeclaration ) {
                kDebug() << "setting alias declaration on inner declaration";
            }
        }
        delete temporaryIdentifier;
    }
    for ( int i = openedContexts.length() - 1; i >= 0; i-- ) {
        // Close all the declarations and contexts opened previosly, and assign the types.
        kDebug() << "closing context";
        closeType();
        closeContext();
        Declaration* d = openedDeclarations.at(i);
        // because no context will be opened for an alias declaration, this will not happen if there's one
        if ( d ) {
            openedTypes[i]->setDeclaration(d);
            d->setType(openedTypes.at(i));
            d->setInternalContext(openedContexts.at(i));
        }
    }
    
    if ( injectingContext ) {
        closeInjectedContext();
    }
    
    if ( ! openedDeclarations.isEmpty() ) {
        // return the lowest-level element in the tree, for the caller to do stuff with
        return openedDeclarations.last();
    }
    else return 0;
}

Declaration* DeclarationBuilder::createModuleImportDeclaration(QString moduleName, QString declarationName,
                                                               Identifier* declarationIdentifier,
                                                               Ast* rangeNode, ProblemPolicy createProblem)
{
    // Search the disk for a python file which contains the requested declaration
    QPair<KUrl, QStringList> moduleInfo = findModulePath(moduleName);
    kDebug() << moduleName;
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
        // The file was not found -- this is either an error in the user's code,
        // a missing module, or a C module (.so) which is unreadable for kdevelop
        // TODO imrpove error handling in case the module exists as a shared object or .pyc file only
        kDebug() << "invalid or non-existent URL:" << moduleInfo;
        if ( createProblem != DontCreateProblems ) {
            KDevelop::Problem *p = new KDevelop::Problem();
            p->setFinalLocation(DocumentRange(currentlyParsedDocument(), range.castToSimpleRange())); // TODO ok?
            p->setSource(KDevelop::ProblemData::SemanticAnalysis);
            p->setSeverity(KDevelop::ProblemData::Warning);
            p->setDescription(i18n("Module \"%1\" not found", moduleName));
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
                                   ->addDocument(moduleInfo.first, TopDUContext::ForceUpdate, m_ownPriority - 1,
                                                 0, ParseJob::FullSequentialProcessing);
        // parseDocuments() must *not* be called from a background thread!
        // KDevelop::ICore::self()->languageController()->backgroundParser()->parseDocuments();
        return 0;
    }
    if ( moduleInfo.second.isEmpty() ) {
        // import the whole module
        kDebug() << "Got module, importing it" << declarationIdentifier->value;
        resultingDeclaration = createDeclarationTree(declarationName.split("."),
                                                     declarationIdentifier, moduleContext, 0, range);
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
                resultingDeclaration = createDeclarationTree(declarationName.split("."), declarationIdentifier,
                                                             ReferencedTopDUContext(0), originalDeclaration,
                                                             editorFindRange(declarationIdentifier, declarationIdentifier));
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
    // Functions containing "yield" statements will return lists in our abstraction.
    // The content type of that list can be guessed from the yield statements.
    AstDefaultVisitor::visitYield(node);
    kDebug() << "visiting yield statement";
    
    // Determine the type of the argument to "yield", like "int" in "yield 3"
    DUChainReadLocker lock(DUChain::lock());
    ExpressionVisitor v(currentContext(), editor());
    v.visitNode(node->value);
    lock.unlock();
    AbstractType::Ptr encountered = v.lastType();
    
    // In some obscure (or wrong) cases, "yield" might appear outside of a function body,
    // so check for that here.
    if ( node->value && hasCurrentType() ) {
        if ( TypePtr<FunctionType> t = currentType<FunctionType>() ) {
            if ( VariableLengthContainer::Ptr previous = t->returnType().cast<VariableLengthContainer>() ) {
                // If the return type of the function already is set to a list, *add* the encountered type
                // to its possible content types.
                previous->addContentType(encountered);
                t->setReturnType(previous.cast<AbstractType>());
            }
            else {
                // Otherwise, create a new container type, and set it as the function's return type.
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

void DeclarationBuilder::visitLambda(LambdaAst* node)
{
    Python::AstDefaultVisitor::visitLambda(node);
    DUChainWriteLocker lock(DUChain::lock());
    // A context must be opened, because the lamdba's arguments are local to the lambda:
    // d = lambda x: x*2; print x # <- gives an error
    openContext(node, editorFindRange(node, node->body), DUContext::Other);
    foreach ( ExpressionAst* argument, node->arguments->arguments ) {
        // Create variable declarations for the lambda's arguments, so they aren't displayed as errors
        if ( argument->astType == Ast::NameAstType ) {
            visitVariableDeclaration<Declaration>(static_cast<NameAst*>(argument));
        }
    }
    closeContext();
}

void DeclarationBuilder::visitCall(CallAst* node)
{
    Python::AstDefaultVisitor::visitCall(node);
    KDEBUG_BLOCK
    kDebug() << "Visiting call";
    
    // Find the function being called; this code also handles cases where non-names
    // are called, for example:
    //     class myclass():
    //         def myfun(self): return 3
    //     l = [myclass()]
    //     x = l[0].myfun() # the called object is actually l[0].myfun
    // In the above example, this call will be evaluated to "myclass.myfun" in the following block.
    DUChainReadLocker lock(DUChain::lock());
    ExpressionVisitor functionVisitor(currentContext(), editor());
    functionVisitor.visitNode(node);
    lock.unlock();
    
    if ( node->function && node->function->astType == Ast::AttributeAstType && functionVisitor.lastDeclaration() ) {
        // Some special functions, like "append", update the content of the object they operate on.
        kDebug() << "Checking for list content updates...";
        // Find the object the function is called on, like for d = [1, 2, 3]; d.append(5), this will give "d"
        lock.lock();
        ExpressionVisitor v(currentContext(), editor());
        v.visitNode(static_cast<AttributeAst*>(node->function)->value);
        lock.unlock();
        
        // Don't do anything if the object the function is being called on is not a container.
        if ( VariableLengthContainer::Ptr container = v.lastType().cast<VariableLengthContainer>() ) {
            // Don't to updates to pre-defined functions.
            if ( v.lastDeclaration() && v.lastDeclaration()->topContext()->url() != IndexedString(Helper::getDocumentationFile()) ) {
                if ( functionVisitor.lastDeclaration()->isFunctionDeclaration() ) {
                    FunctionDeclaration* f = static_cast<FunctionDeclaration*>(functionVisitor.lastDeclaration().data());
                    // Check for the different types of modifiers such a function can have
                    if ( const Decorator* d = Helper::findDecoratorByName<FunctionDeclaration>(f, "addsTypeOfArg") ) {
                        const int offset = d->additionalInformation().str().toInt();
                        if ( node->arguments.length() > offset ) {
                            // Check which type should be added to the list
                            lock.lock();
                            ExpressionVisitor argVisitor(currentContext(), editor());
                            argVisitor.visitNode(node->arguments.at(offset));
                            lock.unlock();
                            // Actually add that type
                            if ( argVisitor.lastType() ) {
                                DUChainWriteLocker wlock(DUChain::lock());
                                kDebug() << "Adding content type: " << argVisitor.lastType()->toString();
                                container->addContentType(argVisitor.lastType());
                                v.lastDeclaration()->setType(container);
                            }
                        }
                    }
                    if ( const Decorator* d = Helper::findDecoratorByName<FunctionDeclaration>(f, "addsTypeOfArgContent") ) {
                        const int offset = d->additionalInformation().str().toInt();
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
    
    // The following code will try to update types of function parameters based on what is passed
    // for those when the function is used.
    // In case of this code:
    //     def foo(arg): print arg
    //     foo(3)
    // the following will change the type of "arg" to be "int" when it processes the second line.
    kDebug() << "--";
    kDebug() << "Trying to update function argument types based on call";
    
    lock.lock();
    QPair<FunctionDeclaration::Ptr, bool> lastFunctionDeclarationP = Helper::functionDeclarationForCalledDeclaration(functionVisitor.lastDeclaration());
    FunctionDeclaration::Ptr lastFunctionDeclaration = lastFunctionDeclarationP.first;
    bool isConstructor = lastFunctionDeclarationP.second;
    
    if ( lastFunctionDeclaration ) {
        if ( lastFunctionDeclaration->topContext()->url() == IndexedString(Helper::getDocumentationFile()) ) {
            return;
        }
        DUContext* args = DUChainUtils::getArgumentContext(lastFunctionDeclaration.data());
        FunctionType::Ptr functiontype = lastFunctionDeclaration->type<FunctionType>();
        if ( args && functiontype ) {
            // The declaration which was found is a function declaration, and has a valid arguments list assigned.
            QVector<Declaration*> parameters = args->localDeclarations();
            // Remove the "self" from the argument list, the type of that should not be updated.
            if ( ( lastFunctionDeclaration->context()->type() == DUContext::Class || isConstructor ) && ! parameters.isEmpty() ) {
                parameters.remove(0);
            }
            int atParam = 0;
            // Check that there's enough known parameters which can be updated
            // TODO handle vararg/kwarg for this, it doesn't work correctly
            uint typeParametersSize = functiontype->arguments().length();
            typeParametersSize += static_cast<FunctionDeclarationPointer>(lastFunctionDeclaration)->defaultParametersSize();
            if ( parameters.size() >= node->arguments.size() && typeParametersSize >= (uint) node->arguments.size() ) {
                lock.unlock();
                DUChainWriteLocker wlock(DUChain::lock());
                foreach ( ExpressionAst* arg, node->arguments ) {
                    // Iterate over all the arguments, trying to guess the type of the object being
                    // passed as an argument, and update the parameter accordingly.
                    if ( atParam >= functiontype->arguments().size() || atParam >= parameters.size() ) {
                        break;
                    }
                    // Get the type of the argument
                    ExpressionVisitor argumentVisitor(currentContext(), editor());
                    argumentVisitor.visitNode(arg);
                    kDebug() << "Got type for function argument: " << argumentVisitor.lastType();
                    if ( argumentVisitor.lastType() && Helper::isUsefulType(argumentVisitor.lastType().cast<AbstractType>()) ) {
                        // Update the parameter type: change both the type of the function argument,
                        // and the type of the declaration which belongs to that argument
                        kDebug() << "last type: " << argumentVisitor.lastType()->toString();
                        HintedType::Ptr addType = HintedType::Ptr(new HintedType());
                        openType(addType);
                        addType->setType(argumentVisitor.lastType());
                        addType->setCreatedBy(topContext(), m_futureModificationRevision);
                        closeType();
                        AbstractType::Ptr newType = Helper::mergeTypes(parameters.at(atParam)->abstractType(), 
                                                                        addType.cast<AbstractType>(), topContext());
                        kDebug() << "new type: " << newType->toString();
                        // TODO this does not correctly update the types in quickopen! Investigate why.
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
    // TODO this urgently needs to be refactored.
    // It has grown crappier and crappier over time.
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
            tupleElementDeclaration = DeclarationPointer(Helper::resolveAliasDeclaration(realDeclarations.at(i).data()));
            currentIsAlias = isAlias.at(i);
        }
        else if ( realTargets.length() == 1 ) {
            DUChainReadLocker lock(DUChain::lock());
            ExpressionVisitor v(currentContext());
            v.visitNode(node->value);
            lock.unlock();
            tupleElementType = v.lastType();
            tupleElementDeclaration = DeclarationPointer(Helper::resolveAliasDeclaration(v.lastDeclaration().data()));
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
        // TODO fix this for x, y = a, b, i.e. if node->value->astType == TupleAstType
        // TODO can't this be handled in a more general way, using the Expression Visitor?
        // Assignments of the form "a = 3"
        if ( target->astType == Ast::NameAstType ) {
            if ( currentIsAlias ) {
                DUChainWriteLocker lock(DUChain::lock());
                kDebug() << "creating alias declaration for " << static_cast<NameAst*>(target)->identifier->value;
                AliasDeclaration* decl = eventuallyReopenDeclaration<AliasDeclaration>(static_cast<NameAst*>(target)->identifier, target, AliasDeclarationType);
                decl->setAliasedDeclaration(tupleElementDeclaration.data());
                closeDeclaration();
            }
            else {
                DUChainWriteLocker lock(DUChain::lock());
                kDebug() << "Creating normal declaration with type" << ( tupleElementType ? tupleElementType->toString() : "<none>" );
                Declaration* dec = visitVariableDeclaration<Declaration>(target, 0, tupleElementType);
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
        // Assignments of the form "a[0] = 3"
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
        // Assignments of the form "a.b = 3"
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
                AbstractType::Ptr type = parentObjectDeclaration->abstractType();
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
                visitVariableDeclaration<ClassMemberDeclaration>(attrib->attribute, target, haveDeclaration, tupleElementType);
                closeAlreadyOpenedContext(internal);
            }
            else {
                injectContext(internal.data());
                
                Declaration* dec = visitVariableDeclaration<ClassMemberDeclaration>(attrib->attribute, target, haveDeclaration, tupleElementType);
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
    
    StructureType::Ptr type(new StructureType());
    
    DUChainWriteLocker lock(DUChain::lock());
    ClassDeclaration* dec = eventuallyReopenDeclaration<ClassDeclaration>(node->name, node->name, NoTypeRequired);
    visitDecorators<ClassDeclaration>(node->decorators, dec);
    eventuallyAssignInternalContext();
    
    dec->setKind(KDevelop::Declaration::Type);
    dec->clearBaseClasses();
    dec->setClassType(ClassDeclarationData::Class);
    
    // check whether this is a type container (list, dict, ...) or just a "normal" class
    const Decorator* d = Helper::findDecoratorByName<ClassDeclaration>(dec, "TypeContainer");
    if ( d ) {
        VariableLengthContainer* container = new VariableLengthContainer();
        if ( Helper::findDecoratorByName<ClassDeclaration>(dec, "hasTypedKeys") ) {
            container->setHasKeyType(true);
        }
        type = StructureType::Ptr(container);
    }
    
    foreach ( ExpressionAst* c, node->baseClasses ) {
        // Iterate over all the base classes, and add them to the duchain.
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
    // every python class inherits from "object".
    // We use this to add all the __str__, __get__, ... methods.
    if ( dec->baseClassesSize() == 0 and node->name->value != "__kdevpythondocumentation_builtin_object" ) {
        ReferencedTopDUContext docContext = Helper::getDocumentationFileContext();
        if ( docContext ) {
            QList<Declaration*> object = docContext->findDeclarations(
                QualifiedIdentifier("__kdevpythondocumentation_builtin_object")
            );
            if ( ! object.isEmpty() && object.first()->abstractType() ) {
                Declaration* objDecl = object.first();
                BaseClassInstance base;
                base.baseClass = objDecl->abstractType()->indexed();
                // this can be queried from autocompletion or elsewhere to hide the items, if required;
                // of course, it's not private strictly speaking
                base.access = KDevelop::Declaration::Private;
                dec->addBaseClass(base);
            }
        }
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
    
    kDebug() << " --- closing CLASS context: " << currentContext()->range().castToSimpleRange();
    lock.lock();
    closeContext();
    closeType();
    closeDeclaration();
    
    dec->setComment(getDocstring(node->body));
}

template<typename T> void DeclarationBuilder::visitDecorators(QList< Python::ExpressionAst* > decorators, T* addTo) {
    foreach ( ExpressionAst* decorator, decorators ) {
        AstDefaultVisitor::visitNode(decorator);
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
    // Search for an eventual containing class declaration;
    // if that exists, then this function is a member function
    DeclarationPointer eventualParentDeclaration(currentDeclaration());
    FunctionType::Ptr type(new FunctionType());
    
    DUChainWriteLocker lock(DUChain::lock());
    kDebug() << identifierForNode(node->name).toString();
    FunctionDeclaration* dec = eventuallyReopenDeclaration<FunctionDeclaration>(node->name, node->name, FunctionDeclarationType);
    
    Q_ASSERT(dec->isFunctionDeclaration());
    
    kDebug() << " <<< open function type";
    openType(type);
    dec->setInSymbolTable(false);
    dec->setType(type);
    
    visitDecorators<FunctionDeclaration>(node->decorators, dec);
    visitFunctionArguments(node);
    
    const bool isStatic = Helper::findDecoratorByName<FunctionDeclaration>(dec, "staticmethod");
    
    // If this is a member function, set the type of the first argument (the "self") to be
    // an instance of the class.
    // this must be done here, because the type of self must be known when parsing the body
    if ( eventualParentDeclaration && currentType<FunctionType>()->arguments().length()
            && m_firstAttributeDeclaration.data() && currentContext()->type() == DUContext::Class
            && ! isStatic )
    {
        DUChainWriteLocker lock(DUChain::lock());
        currentType<FunctionType>()->removeArgument(0);
        m_firstAttributeDeclaration->setAbstractType(eventualParentDeclaration->abstractType());
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
    
    if ( ! isStatic ) {
        DUContext* args = DUChainUtils::getArgumentContext(dec);
        if ( args )  {
            QVector<Declaration*> parameters = args->localDeclarations();
            kDebug() << "checking function with" << parameters.size() << "arguments";
            
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
    }
    else {
        m_firstAttributeDeclaration = DeclarationPointer(0);
        dec->setStatic(true);
    }
    
    // check for documentation
    dec->setComment(getDocstring(node->body));
    dec->setInSymbolTable(true);
}

QString DeclarationBuilder::getDocstring(QList< Ast* > body)
{
    if ( ! body.isEmpty() && body.first()->astType == Ast::ExpressionAstType 
            && static_cast<ExpressionAst*>(body.first())->value->astType == Ast::StringAstType )
    {
        // If the first statement in a function/class body is a string, then that is the docstring.
        StringAst* docstring = static_cast<StringAst*>(static_cast<ExpressionAst*>(body.first())->value);
        kDebug() << "Got docstring for declaration";
        return docstring->value.trimmed();
    }
    return QString();
}

void DeclarationBuilder::visitReturn(ReturnAst* node)
{
    kDebug() << "visiting return statement";
    // Find the type of the object being "return"ed
    DUChainReadLocker lock(DUChain::lock());
    ExpressionVisitor v(currentContext(), editor());
    v.visitNode(node->value);
    lock.unlock();
    
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
        if ( t ) {
            // Update the containing function's return type
            t->setReturnType(Helper::mergeTypes(t->returnType(), encountered));
        }
    }
    DeclarationBuilderBase::visitReturn(node);
}

void DeclarationBuilder::visitArguments( ArgumentsAst* node )
{
    DUChainWriteLocker lock(DUChain::lock());
    kDebug() << "Current context for parameters: " << currentContext() << currentContext()->scopeIdentifier().toString();
    
    if ( currentDeclaration() and currentDeclaration()->isFunctionDeclaration() ) {
        FunctionDeclaration* workingOnDeclaration = static_cast<FunctionDeclaration*>(Helper::resolveAliasDeclaration(currentDeclaration()));
        workingOnDeclaration->clearDefaultParameters();
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
                // Iterate over all the function's arguments, create declarations, and add the arguments
                // to the functions FunctionType.
                currentIndex += 1;
                realParam = dynamic_cast<NameAst*>(expression);
                
                if ( ! realParam || realParam->context != ExpressionAst::Parameter ) {
                    // I'm still not totally sure how non-name parameters might look like,
                    // but better check for it here.
                    continue;
                }
                
                // Create a variable declaration for the parameter, to be used in the function body.
                Declaration* paramDeclaration = visitVariableDeclaration<Declaration>(realParam);
                
                DUChainWriteLocker lock;
                if ( type && paramDeclaration && currentIndex > firstDefaultParameterOffset ) {
                    // Handle arguments with default values, like def foo(bar = 3): pass
                    kDebug() << "Adding default argument: " << realParam->identifier->value << paramDeclaration->abstractType();
                    // Find type of given default value, and assign it to the declaration
                    // TODO does this actually work?
                    ExpressionVisitor v(currentContext());
                    v.visitNode(node->defaultValues.at(currentIndex - firstDefaultParameterOffset - 1));
                    paramDeclaration->setAbstractType(v.lastType());
                    if ( v.lastType() ) {
                        type->addArgument(v.lastType());
                    }
                    else {
                        type->addArgument(AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed)));
                    }
                    // TODO add the real expression from the document here as default value
                    workingOnDeclaration->addDefaultParameter(IndexedString("..."));
                    kDebug() << "Arguments count: " << type->arguments().length();
                }
                else {
                    kDebug() << "Not a default argument: " << realParam->identifier->value;
                    // For now, we cannot know the type, thus we write "mixed".
                    // As soon as a call to the function is encountered, this type might be updated.
                    type->addArgument(AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed)));
                }
                if ( isFirst ) {
                    // Store the first parameter for easy access; if this is a class member declaration,
                    // its type will then be set to be an instance of the containing class.
                    m_firstAttributeDeclaration = DeclarationPointer(paramDeclaration);
                    isFirst = false;
                }
            }
            // Handle *args, **kwargs, and assign them a list / dictionary type.
            kDebug() << "var/kwarg:" <<  node->vararg << node->kwarg;
            if ( node->vararg ) {
                DUChainReadLocker lock(DUChain::lock());
                AbstractType::Ptr listType = ExpressionVisitor::typeObjectForIntegralType("list", currentContext()).cast<AbstractType>();
                lock.unlock();
                type->addArgument(listType);
                node->vararg->startCol = node->vararg_col_offset; node->vararg->endCol = node->vararg_col_offset + node->vararg->value.length() - 1;
                node->vararg->startLine = node->vararg_lineno; node->vararg->endLine = node->vararg_lineno;
                visitVariableDeclaration<Declaration>(node->vararg, 0, listType);
            }
            if ( node->kwarg ) {
                DUChainReadLocker lock(DUChain::lock());
                AbstractType::Ptr dictType = ExpressionVisitor::typeObjectForIntegralType("dict", currentContext()).cast<AbstractType>();
                lock.unlock();
                type->addArgument(dictType);
                node->kwarg->startCol = node->arg_col_offset; node->kwarg->endCol = node->arg_col_offset + node->kwarg->value.length() - 1;
                node->kwarg->startLine = node->arg_lineno; node->kwarg->endLine = node->arg_lineno;
                visitVariableDeclaration<Declaration>(node->kwarg, 0, dictType);
            }
        }
    }
    
    kDebug() << "Got " << currentContext()->localDeclarations().size() << "declarations in arguments.";
    
    DeclarationBuilderBase::visitArguments(node);
}

}


