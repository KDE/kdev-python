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

#include "contextbuilder.h"
#include "declarationbuilder.h"
#include "pythoneditorintegrator.h"
#include "expressionvisitor.h"
#include "helpers.h"
#include "types/variablelengthcontainer.h"
#include "declarations/decorateddeclaration.h"

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
    NameAst* currentVariableDefinition = dynamic_cast<NameAst*>(node);
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
    
    kDebug() << "Parsing variable declaration: " << node->value;
    
    Declaration* dec = 0;
    QList<Declaration*> existingDeclarations;
    // specified from outside
    if ( previous ) {
        existingDeclarations << previous;
    }
    // find decls by ourselves
    else {
        /**DBG**/
        kDebug() << "Current context: " << currentContext()->scopeIdentifier() << currentContext()->range().castToSimpleRange();
        kDebug() << "Looking for node identifier:" << identifierForNode(node);
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
    }
    QList<Declaration*> remainingDeclarations;
    foreach ( Declaration* d, existingDeclarations ) {
        Declaration* fitting = dynamic_cast<T*>(d);
        kDebug() << "last one: " << d << d->toString() << dynamic_cast<T*>(d) << wasEncountered(d);
        bool invalidType = d && d->abstractType() && lastType() && lastType()->whichType() != AbstractType::TypeFunction && d->isFunctionDeclaration();
        if ( fitting && ! wasEncountered(d) && ! invalidType ) {
            kDebug() << "Opening previously existing declaration for " << d->toString();
            openDeclarationInternal(d);
            d->setRange(editorFindRange(node, node));
            setEncountered(d);
            dec = d;
        }
        else if ( fitting && ! invalidType ) {
           remainingDeclarations << fitting;
        }
    }
    existingDeclarations = remainingDeclarations;
    
//     if ( dec || ! existingDeclarations.isEmpty() ) {
//         Declaration* d = dec ? dec : existingDeclarations.first();
//         Q_ASSERT(d);
//         d = Helper::resolveAliasDeclaration(d);
//         if ( d && d->abstractType() && lastType() && lastType()->whichType() != AbstractType::TypeFunction && d->isFunctionDeclaration() ) {
//             kWarning() << "Found re-declaration, reporting error";
//             kDebug() << d->abstractType()->toString() << lastType()->toString() << d->abstractType()->whichType() << lastType()->whichType();
//             // assigning e.g. an integral value to something that was a function definition previously
//             // is difficult to handle and most likely not what you want, so we just report an error.
//             KDevelop::Problem *p = new KDevelop::Problem();
//             p->setFinalLocation(DocumentRange(currentlyParsedDocument(), SimpleRange(
//                                 node->startLine, node->startCol, node->startLine, (node->startLine == node->endLine ? node->endCol + 1 : 100))));
//             p->setSource(KDevelop::ProblemData::SemanticAnalysis);
//             p->setSeverity(KDevelop::ProblemData::Error);
//             p->setDescription(i18n("Re-declaration of \"%1\" shadows a previous declaration with different type", node->value));
//             ProblemPointer ptr(p);
//             topContext()->addProblem(ptr);
//             return 0;
//         }
//     }
    
    kDebug() << "VARIABLE CONTEXT: " << currentContext()->scopeIdentifier() << currentContext()->range().castToSimpleRange() << currentContext()->type() << DUContext::Class;
    
    bool noFittingDeclaration = existingDeclarations.isEmpty() || ( ! existingDeclarations.isEmpty() && ! dynamic_cast<T*>(existingDeclarations.last()) );
    if ( currentContext() && currentContext()->type() == DUContext::Class && noFittingDeclaration ) {
        kDebug() << "Creating class member declaration for " << node->value << node->startLine << ":" << node->startCol;
        kDebug() << "Context type: " << currentContext()->scopeIdentifier() << currentContext()->range().castToSimpleRange();
        if ( ! dec ) dec = openDeclaration<ClassMemberDeclaration>(node, originalAst ? originalAst : node);
        DeclarationBuilderBase::closeDeclaration();
        dec->setType(lastType());
        dec->setKind(KDevelop::Declaration::Instance);
    } else if ( noFittingDeclaration ) {
        kDebug() << "Creating variable declaration for " << node->value << node->startLine << ":" << node->startCol << "->" << node->endLine << ":" << node->endCol;
        if ( ! dec ) dec = openDeclaration<T>(node, originalAst ? originalAst : node);
        DeclarationBuilderBase::closeDeclaration();
        dec->setType(lastType());
        dec->setKind(KDevelop::Declaration::Instance); // everything is an object in python
    } else {
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
                    dec->setType(Helper::mergeTypes(currentType, newType));
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
    m_hasUnresolvedImports = false;
    DeclarationBuilderBase::visitCode(node);
}

void DeclarationBuilder::visitExceptionHandler(ExceptionHandlerAst* node)
{
    if ( dynamic_cast<NameAst*>(node->name) ) {
        openType(AbstractType::Ptr(0)); // TODO set exception type
        setLastType(AbstractType::Ptr(0));
        visitVariableDeclaration<Declaration>(node->name); // except Error as <vardecl>
        closeType();
    }
    DeclarationBuilderBase::visitExceptionHandler(node);
}

void DeclarationBuilder::visitFor(ForAst* node)
{
    if ( node->target->astType == Ast::NameAstType ) {
        openType(AbstractType::Ptr(0)); // TODO check for what is iterated over
        setLastType(AbstractType::Ptr(0));
        visitVariableDeclaration<Declaration>(node->target);
        closeType();
    }
    else if ( node->target->astType == Ast::TupleAstType ) {
        foreach ( ExpressionAst* tupleMember, dynamic_cast<TupleAst*>(node->target)->elements ) {
            if ( tupleMember->astType == Ast::NameAstType ) visitVariableDeclaration<Declaration>(tupleMember);
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
            kWarning() << "Declaration not found: " << dottedNameIdentifier << "in top context" << ctx->url().toUrl().path();
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
            moduleName = name->name->value;
        }
        Identifier* declarationIdentifier = name->asName ? name->asName : name->name;
        createModuleImportDeclaration(moduleName, declarationIdentifier);
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

Declaration* DeclarationBuilder::createModuleImportDeclaration(QString dottedName, Identifier* declarationIdentifier, Ast* rangeNode)
{
    QPair<KUrl, QStringList> moduleInfo = findModulePath(dottedName);
    RangeInRevision range(RangeInRevision::invalid());
    if ( rangeNode ) {
        range = rangeForNode(rangeNode, false);
    }
    else {
        range = rangeForNode(declarationIdentifier, true);
    }
    Q_ASSERT(range.isValid());
    
    kDebug() << "Found module path [path/path in file]: " << moduleInfo;
    DUChainWriteLocker lock(DUChain::lock());
    ReferencedTopDUContext moduleContext = DUChain::self()->chainForDocument(IndexedString(moduleInfo.first));
    lock.unlock();
    Declaration* resultingDeclaration = 0;
    if ( ! moduleInfo.first.isValid() ) {
        kWarning() << "invalid or non-existent URL:" << moduleInfo;
        return 0;
    }
    if ( ! moduleContext ) {
        // schedule the include file for parsing, and schedule the current one for reparsing after that is done
        qDebug() << "No module context, recompiling";
        m_hasUnresolvedImports = true;
        DUChain::self()->updateContextForUrl(IndexedString(moduleInfo.first), TopDUContext::AllDeclarationsContextsAndUses, 0, -20);
        return 0;
    }
    if ( moduleInfo.second.isEmpty() ) {
        // import the whole module
        kDebug() << "Got module, importing it";
        StructureType::Ptr moduleType(new StructureType());
        openType(moduleType);
        DUChainWriteLocker lock(DUChain::lock());
        setLastType(AbstractType::Ptr(0));
        resultingDeclaration = visitVariableDeclaration<Declaration>(declarationIdentifier, range);
        Q_ASSERT(resultingDeclaration);
        closeType();
        // create a wrapper context, import the context for the file into that context, and add it using a declaration
        DUContext* wrapperContext = openContext(declarationIdentifier, KDevelop::DUContext::Other);
        closeContext();
        wrapperContext->addImportedParentContext(moduleContext);
        moduleType->setDeclaration(resultingDeclaration);
        resultingDeclaration->setType(moduleType);
        if ( m_builtinFunctionsContext )
            wrapperContext->removeImportedParentContext(m_builtinFunctionsContext.data());
        resultingDeclaration->setInternalContext(wrapperContext);
    }
    else {
        // import a specific declaration from the given file
        lock.lock();
        kDebug() << "Got module, importing declaration: " << moduleInfo.second;
        Declaration* originalDeclaration = findDeclarationInContext(moduleInfo.second, moduleContext);
        kDebug() << "Result: " << originalDeclaration;
        if ( originalDeclaration ) {
            DUChainWriteLocker lock(DUChain::lock());
            resultingDeclaration = visitVariableDeclaration<AliasDeclaration>(declarationIdentifier, range);
            if ( dynamic_cast<AliasDeclaration*>(resultingDeclaration) ) {
                static_cast<AliasDeclaration*>(resultingDeclaration)->setAliasedDeclaration(originalDeclaration);
                kDebug() << "Resulting alias: " << resultingDeclaration->toString();
                moduleContext->addDirectImporter(topContext());
            }
            else
                kWarning() << "import declaration is being overwritten!";
        }
        // TODO report error
    }
    return resultingDeclaration;
}

void DeclarationBuilder::visitCall(CallAst* node)
{
    Python::AstDefaultVisitor::visitCall(node);
}

void DeclarationBuilder::visitAssignment(AssignmentAst* node)
{
    QList<ExpressionAst*> realTargets;
    QList<AbstractType::Ptr> realValues;
    QList<DeclarationPointer> realDeclarations;
    
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
        foreach ( ExpressionAst* value, static_cast<TupleAst*>(node->value)->elements ) {
            ExpressionVisitor v(currentContext(), editor());
            v.visitNode(value);
            realValues << v.lastType();
            realDeclarations << v.lastDeclaration();
        }
    }
    else {
        ExpressionVisitor v(currentContext(), editor());
        v.visitNode(node->value);
        realValues << v.lastType();
        realDeclarations << v.lastDeclaration();
        DUChainReadLocker lock(DUChain::lock());
        kDebug() << ( v.lastType() ? v.lastType()->toString() : "< no last type >" ) << ( v.lastDeclaration() ? v.lastDeclaration()->toString() : "< no last declaration >" );
    }
    
    AbstractType::Ptr tupleElementType(0);
    DeclarationPointer tupleElementDeclaration(0);
    bool canUnpack = realTargets.length() == realValues.length();
    int i = 0;
    foreach ( ExpressionAst* target, realTargets ) {
        if ( canUnpack ) {
            tupleElementType = realValues.at(i);
            tupleElementDeclaration = realDeclarations.at(i);
        } else if (realTargets.length() == 1) {
            ExpressionVisitor v(currentContext(), editor());
            v.visitNode(node->value);
            tupleElementType =  v.lastType();
        } else {
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
        i += 1;
        setLastType(tupleElementType); // TODO fix this for x, y = a, b, i.e. if node->value->astType == TupleAstType
        if ( target->astType == Ast::NameAstType ) {
            if ( tupleElementType && tupleElementType->whichType() == AbstractType::TypeFunction ) {
                if ( tupleElementDeclaration ) {
                    DUChainWriteLocker lock(DUChain::lock());
                    AliasDeclaration* decl = openDeclaration<AliasDeclaration>(static_cast<NameAst*>(target)->identifier, target);
                    decl->setAliasedDeclaration(tupleElementDeclaration.data());
                }
            }
            else {
                DUChainWriteLocker lock(DUChain::lock());
                Declaration* dec = visitVariableDeclaration<Declaration>(target);
                /** DEBUG **/
                if ( tupleElementType && dec ) {
                    VariableLengthContainer* type = dynamic_cast<VariableLengthContainer*>(dec->abstractType().unsafeData());
                    kDebug() << "type is: " << dec->abstractType().unsafeData() << type << dynamic_cast<VariableLengthContainer*>(tupleElementType.unsafeData());
                    kDebug() << "indexed: " << tupleElementType->indexed().hash() << "<>" << dec->indexedType().hash();
                    kDebug() << "Container: " << dynamic_cast<VariableLengthContainer*>(dec->abstractType().unsafeData());
                    Q_ASSERT(dec->abstractType());
                }
                /** END DEBUG **/
            }
        }
        if ( target->astType == Ast::AttributeAstType ) {
            AttributeAst* attrib = static_cast<AttributeAst*>(target);
            kDebug() << "Visiting attribute: " << attrib->attribute->value;
            // check whether the current attribute is undeclared, but the previos ones known
            // like in X.Y.Z = 3 where X and Y are defined, but Z isn't; then declare Z.
            ExpressionVisitor checkForUnknownAttribute(currentContext(), editor());
            checkForUnknownAttribute.visitNode(attrib);
            DeclarationPointer unknown = checkForUnknownAttribute.lastDeclaration();
            
            // declare the attribute.
            // however, if there's an earlier declaration which does not match the current position
            // (so it's really a different declaration) we skip this.
            Declaration* haveDeclaration = 0;
            if ( unknown.data() ) {
                kDebug() << "Declaration is already created";
                haveDeclaration = unknown.data();
            }
            
            ExpressionVisitor checkPreviousAttributes(currentContext(), editor());
            checkPreviousAttributes.visitNode(attrib->value); // go "down one level", so only visit "X.Y"
            
            DUContextPointer internal(0);
            DeclarationPointer parentObjectDeclaration = checkPreviousAttributes.lastDeclaration();
            AbstractType::Ptr type = checkPreviousAttributes.lastType();
        
            if ( ! parentObjectDeclaration ) {
                kWarning() << "No declaration for attribute base, aborting creation of attribute";
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
                if ( ! structure.unsafeData() || ! structure->declaration(topContext()) ) continue;
                parentObjectDeclaration = structure->declaration(topContext());
                internal = parentObjectDeclaration->internalContext();
                kDebug() << "... ok!";
            }
            if ( ! internal.data() ) {
                kWarning() << "No internal context for structure type, aborting creation of attribute declaration";
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
    }
}

void DeclarationBuilder::visitClassDefinition( ClassDefinitionAst* node )
{
    kDebug() << "opening class definition";
    
    DUChainWriteLocker lock(DUChain::lock());
    ClassDeclaration* dec = openDeclaration<ClassDeclaration>( node->name, node );
    visitDecorators(node->decorators, dec);
    eventuallyAssignInternalContext();
    
    dec->setKind(KDevelop::Declaration::Type);
    dec->clearBaseClasses();
    dec->setClassType(ClassDeclarationData::Class);
    
    foreach ( ExpressionAst* c, node->baseClasses ) {
        ExpressionVisitor v(currentContext(), editor());
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
    foreach ( const Decorator& d, dec->decorators ) {
        kDebug() << "Decorator for class: " << d.name;
        if ( d.name == "TypeContainer" ) {
            type = StructureType::Ptr(new VariableLengthContainer());
        }
    }
    if ( ! type ) {
        type = StructureType::Ptr(new StructureType());
    }
    type->setDeclaration(dec);
    dec->setType(type);
    lock.unlock();
    
    openType(type);
    
    // needs to be done here, so the assignment of the internal context happens before visiting the body
    
    openContextForClassDefinition(node);
    lock.lock();
    dec->setInternalContext(currentContext());
    lock.unlock();
    // yes, we do not call the context builder here, because contexts are already open
    AstDefaultVisitor::visitClassDefinition( node );
    lock.lock();
    kDebug() << " --- closing CLASS context: " << currentContext()->range().castToSimpleRange();
    closeContext();
    lock.unlock();
    
    closeType();
    
    closeDeclaration();
    
    dec->setComment(getDocstring(node->body));
}

void DeclarationBuilder::visitDecorators(QList< ExpressionAst* > decorators, DecoratedDeclaration* addTo) {
    foreach ( ExpressionAst* decorator, decorators ) {
        kDebug() << "decorator type: " << decorator->astType << "(name: " << Ast::NameAstType << ", call: " << Ast::CallAstType << ")";
        if ( decorator->astType == Ast::CallAstType ) {
            CallAst* call = static_cast<CallAst*>(decorator);
            Decorator d;
            if ( call->function->astType != Ast::NameAstType ) continue;
            d.name = *static_cast<NameAst*>(call->function)->identifier;
            foreach ( ExpressionAst* arg, call->arguments ) {
                if ( arg->astType == Ast::NumberAstType ) {
                    d.args << static_cast<NumberAst*>(arg)->value;
                }
                else if ( arg->astType == Ast::StringAstType ) {
                    d.args << static_cast<StringAst*>(arg)->value;
                }
            }
            kDebug() << "call decorator identifier: " << d.name << *static_cast<NameAst*>(call->function)->identifier;
            addTo->decorators.append(d);
        }
        else if ( decorator->astType == Ast::NameAstType ) {
            NameAst* name = static_cast<NameAst*>(decorator);
            Decorator d;
            d.name = *(name->identifier);
            kDebug() << "name decorator identifier: " << d.name << *(name->identifier);
            addTo->decorators.append(d);
        }
    }
}

void DeclarationBuilder::visitFunctionDefinition( FunctionDefinitionAst* node )
{
    kDebug() << "opening function definition" << node->startLine << node->endLine;
    DeclarationPointer eventualParentDeclaration(currentDeclaration()); // an eventual containing class declaration
    FunctionType::Ptr type;
    QList<Declaration*> existing;
    
    FunctionDeclaration* dec = openDeclaration<FunctionDeclaration>( node->name, node );
    Q_ASSERT(dec->isFunctionDeclaration());
    
    type = FunctionType::Ptr(new FunctionType());
    type->setReturnType(AbstractType::Ptr(new IntegralType(IntegralType::TypeVoid)));
    {
        DUChainWriteLocker lock;
        dec->setType(type);
    }
    
    openType(type);
    kDebug() << " <<< open function type";
    DUChainWriteLocker lock(DUChain::lock());
    bool hasFirstArgument = false;
    
    visitDecorators(node->decorators, dec);
    visitFunctionArguments(node);
    
    // this must be done here, because the type of self must be known when parsing the body
    kDebug() << "Checking weather we have to change argument types...";
    kDebug() <<  eventualParentDeclaration.data() << currentType<FunctionType>()->arguments().length() << m_firstAttributeDeclaration.data() << currentContext()->type() << DUContext::Class;
    if ( eventualParentDeclaration.data() && currentType<FunctionType>()->arguments().length() 
            && m_firstAttributeDeclaration.data() && currentContext()->type() == DUContext::Class ) {
        kDebug() << "Changing self argument type";
        kDebug() << "Arguments left: " << currentType<FunctionType>()->arguments().count();
        currentType<FunctionType>()->removeArgument(0);
        kDebug() << "Arguments left: " << currentType<FunctionType>()->arguments().count();
        DUChainWriteLocker lock(DUChain::lock());
        m_firstAttributeDeclaration->setAbstractType(eventualParentDeclaration->abstractType());
        hasFirstArgument = true;
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
        dec->setType(type);
    }

    if ( eventualParentDeclaration.data() && currentContext()->type() == DUContext::Class && m_firstAttributeDeclaration.data()
          && ( type->arguments().length() || hasFirstArgument ) ) {
        if ( m_firstAttributeDeclaration->identifier().identifier() != IndexedString("self") ) {
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
    else if ( currentContext()->type() == DUContext::Class ) {
        DUChainWriteLocker lock(DUChain::lock());
        KDevelop::Problem *p = new KDevelop::Problem();
        p->setFinalLocation(DocumentRange(currentlyParsedDocument(), SimpleRange(node->startLine, node->startCol, node->startLine, 10000))); // only mark first line
        p->setSource(KDevelop::ProblemData::SemanticAnalysis);
        p->setSeverity(KDevelop::ProblemData::Warning);
        p->setDescription(i18n("Non-static class method without arguments, must have at least one (self)"));
        ProblemPointer ptr(p);
        topContext()->addProblem(ptr);
    }
    
    // check for documentation
    dec->setComment(getDocstring(node->body));
}

QString DeclarationBuilder::getDocstring(QList< Ast* > body)
{
    if ( body.length() && body.first()->astType == Ast::ExpressionAstType 
            && static_cast<ExpressionAst*>(body.first())->value->astType == Ast::StringAstType ) {
        StringAst* docstring = static_cast<StringAst*>(static_cast<ExpressionAst*>(body.first())->value);
        kDebug() << "Got docstring for declaration: " << docstring->value;
        return docstring->value;
    }
    return QString("");
}

void DeclarationBuilder::visitReturn(ReturnAst* node)
{
    ExpressionVisitor v(currentContext(), editor());
    v.visitNode(node->value);
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
        t->setReturnType(encountered);
    }
    setLastType(AbstractType::Ptr(0));
}

void DeclarationBuilder::visitArguments( ArgumentsAst* node )
{
    DUChainWriteLocker lock(DUChain::lock());
    AbstractFunctionDeclaration* function = dynamic_cast<AbstractFunctionDeclaration*>(currentDeclaration());
    kDebug() << "Current context for parameters: " << currentContext();
    kDebug() << currentContext()->scopeIdentifier().toString();
    if ( currentDeclaration() ) kDebug() << currentDeclaration()->identifier().toString();
    
    
    if ( function ) {
        static_cast<FunctionDeclaration*>(currentDeclaration())->clearDefaultParameters();
        FunctionType::Ptr type = currentType<FunctionType>();
        NameAst* realParam;
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
            AbstractType::Ptr listType = ExpressionVisitor::typeObjectForIntegralType<AbstractType>("list", currentContext());
            type->addArgument(listType);
            node->vararg->startCol = node->vararg_col_offset; node->vararg->endCol = node->vararg_col_offset + node->vararg->value.length() - 1;
            node->vararg->startLine = node->vararg_lineno - 1; node->vararg->endLine = node->vararg_lineno - 1;
            Declaration* d = visitVariableDeclaration<Declaration>(node->vararg);
            Q_ASSERT(d);
            d->setAbstractType(listType);
        }
        if ( node->kwarg ) {
            AbstractType::Ptr dictType = ExpressionVisitor::typeObjectForIntegralType<AbstractType>("dict", currentContext());
            type->addArgument(dictType);
            node->kwarg->startCol = node->arg_col_offset; node->kwarg->endCol = node->arg_col_offset + node->kwarg->value.length() - 1;
            node->kwarg->startLine = node->arg_lineno - 1; node->kwarg->endLine = node->arg_lineno - 1;
            Declaration* d = visitVariableDeclaration<Declaration>(node->kwarg);
            Q_ASSERT(d);
            d->setAbstractType(dictType);
        }
    }
    
    DeclarationBuilderBase::visitArguments(node);
}

}


