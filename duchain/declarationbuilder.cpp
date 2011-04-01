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

#include <ktexteditor/smartrange.h>
#include <ktexteditor/smartinterface.h>

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
#include <declarations/importedmoduledeclaration.h>
#include <../kdevplatform/language/duchain/declaration.h>

#include "contextbuilder.h"
#include "declarationbuilder.h"
#include "pythoneditorintegrator.h"
#include "expressionvisitor.h"
#include <interfaces/foregroundlock.h>


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
    Q_ASSERT(currentVariableDefinition);
    if ( currentVariableDefinition->context != ExpressionAst::Store
      && currentVariableDefinition->context != ExpressionAst::Parameter
      && currentVariableDefinition->context != ExpressionAst::AugStore
    ) {
            return 0;
    }
    Identifier* id = currentVariableDefinition->identifier;
    return visitVariableDeclaration<T>(id, currentVariableDefinition, previous);
}

/*
 * WARNING: This will return a nullpointer if another than the expected type of variable was found!
 * */
template<typename T> T* DeclarationBuilder::visitVariableDeclaration(Identifier* node, Ast* originalAst, Declaration* previous)
{
    DUChainWriteLocker lock(DUChain::lock());
    Q_ASSERT(node);
    
    kDebug() << "Parsing variable declaration: " << node->value;
    
    //CursorInRevision until = editorFindRange(node, node).end;
    
    Declaration* dec = 0;
    QList<Declaration*> existingDeclarations;
    if ( ! previous ) {
        existingDeclarations = currentContext()->findDeclarations(identifierForNode(node), editorFindRange(node, node).end);
        if ( existingDeclarations.length() ) {
            kDebug() << "Existing declaration range: " << existingDeclarations.last()->range().castToSimpleRange() << "vs" << editorFindRange(node, node).castToSimpleRange();
        }
        if ( existingDeclarations.length() && existingDeclarations.last()->range() == editorFindRange(node, node) ) {
            if ( dynamic_cast<T*>(existingDeclarations.last()) ) {
                kDebug() << "Opening previously existing declaration for " << existingDeclarations.last()->toString();
                openDeclarationInternal(existingDeclarations.last());
                dec = existingDeclarations.last();
                setEncountered(dec);
                existingDeclarations.removeLast();
            }
        }
    }
    else {
        dec = previous;
        openDeclarationInternal(dec);
        setEncountered(dec);
    }
    
    kDebug() << "VARIABLE CONTEXT: " << currentContext()->scopeIdentifier() << currentContext()->range().castToSimpleRange() << currentContext()->type() << DUContext::Class;
    
    if ( currentContext() && currentContext()->type() == DUContext::Class ) {
        kDebug() << "Creating class member declaration for " << node->value << node->startLine << ":" << node->startCol;
        kDebug() << "Context type: " << currentContext()->scopeIdentifier() << currentContext()->range().castToSimpleRange();
        if ( ! dec ) dec = openDeclaration<ClassMemberDeclaration>(node, originalAst ? originalAst : node);
        DeclarationBuilderBase::closeDeclaration();
        dec->setType(lastType());
        dec->setKind(KDevelop::Declaration::Instance);
    } else if ( existingDeclarations.isEmpty() || existingDeclarations.last()->context() != currentContext() ) {
        kDebug() << "Creating variable declaration for " << node->value << node->startLine << ":" << node->startCol;
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
                    UnsureType::Ptr unsure = UnsureType::Ptr::dynamicCast(currentType);
                    // maybe it's referenced?
                    ReferenceType::Ptr rType = ReferenceType::Ptr::dynamicCast(currentType);
                    if ( !unsure && rType ) {
                        unsure = UnsureType::Ptr::dynamicCast(rType->baseType());
                    }
                    if ( !unsure ) {
                        unsure = UnsureType::Ptr(new UnsureType());
                        if ( rType ) {
                            unsure->addType(rType->baseType()->indexed());
                        } else {
                            unsure->addType(dec->indexedType());
                        }
                    }
                    unsure->addType(newType->indexed());
                    if ( rType ) {
                        rType->setBaseType(AbstractType::Ptr(unsure.unsafeData()));
                        dec->setType(rType);
                    } else {
                        dec->setType(unsure);
                    }
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

void DeclarationBuilder::visitImport(ImportAst* node)
{
    Python::ContextBuilder::visitImport(node);
    DUChainWriteLocker lock(DUChain::lock());
    foreach ( AliasAst* name, node->names ) {
        QString moduleName = name->name->value;
        if ( name->asName && name->asName ) 
            moduleName += "." + name->asName->value;
        
        ReferencedTopDUContext contextptr = contextsForModules.value(name->asName ? name->asName->value : name->name->value);
        kDebug() << "Chain for document: " << contextptr;
        importedModuleDeclaration* dec;
        kDebug() << ( name->asName ? name->asName->value : QString("no asName") ) << ( name->name ? name->name->value : "no name" );
        
        StructureType::Ptr type(new StructureType());
        openType(type);
        setLastType(AbstractType::Ptr(0));
        if ( name->asName ) {
            dec = visitVariableDeclaration<importedModuleDeclaration>(name->asName);
        }
        else {
            dec = visitVariableDeclaration<importedModuleDeclaration>(name->name);
        }
        closeType();
        
        DUContext* newctx = openContext(name, KDevelop::DUContext::Other);
        newctx->setType(KDevelop::DUContext::Other);
        kDebug() << currentContext()->type() << DUContext::Namespace << DUContext::Class;
        
        if ( currentContext() && contextptr.data() ) {
            currentContext()->addImportedParentContext(contextptr.data());
            kDebug() << "Context for " << moduleName << "imported (I)"; 
        }
        else {
            kWarning() << "Context for " << moduleName << " is not available" << currentContext() << contextptr.data();
        }
        
        closeContext();
        
        type->setDeclaration(dec);
        
        if ( dec ) {
            DUChainWriteLocker lock(DUChain::lock());
            dec->m_moduleIdentifier = moduleName;
            dec->setType(type);
            kDebug() << "Context for " << moduleName << "imported (II)"; 
            
            if ( m_builtinFunctionsContext.data() ) {
                kDebug() << "Deleting builtin functions context from imported module...";
                newctx->removeImportedParentContext(m_builtinFunctionsContext.data());
            }
            dec->setInternalContext(newctx);
            kDebug() << "All declarations in the module which has just been imported" << dec->internalContext()
                        ->allDeclarations(CursorInRevision::invalid(), currentContext()->topContext(), false);
        }
        else {
            kWarning() << "Failed to import context for " << moduleName << ", no declaration";
        }
    }
}

void DeclarationBuilder::visitImportFrom(ImportFromAst* node)
{
    Python::AstDefaultVisitor::visitImportFrom(node);
    foreach ( AliasAst* name, node->names ) {
        importedModuleDeclaration* dec = 0;
        openType(AbstractType::Ptr(0));
        setLastType(AbstractType::Ptr(0));
        if ( name->asName ) {
            dec = visitVariableDeclaration<importedModuleDeclaration>(name->asName);
        }
        else {
            dec = visitVariableDeclaration<importedModuleDeclaration>(name->name);
        }
        closeType();
        if ( dec && name->name && node->module ) {
            dec->m_moduleIdentifier = node->module->value + "." + name->name->value;
            kDebug() << "FromImport module name: " << name->name->value;
        }
    }
}

void DeclarationBuilder::visitAssignment(AssignmentAst* node)
{
    ExpressionVisitor v(currentContext(), editor());
    v.visitNode(node->value);
    
    foreach ( ExpressionAst* target, node->targets ) {
        setLastType(v.lastType()); // TODO fix this for x, y = a, b, i.e. if node->value->astType == TupleAstType
        if ( target->astType == Ast::NameAstType ) {
            if ( v.lastType() && v.lastType()->whichType() == AbstractType::TypeFunction) {
                // TODO change this: use AliasDeclaration, I guess
                FunctionDeclaration* d = visitVariableDeclaration<FunctionDeclaration>(target);
                if ( v.lastDeclaration() && d ) {
                    // copy docstring
                    d->setComment(v.lastDeclaration()->comment());
                }
            }
            else {
                visitVariableDeclaration<Declaration>(target);
            }
        }
        if ( target->astType == Ast::AttributeAstType ) {
            AttributeAst* attrib = static_cast<AttributeAst*>(target);
            // check weather the current attribute is undeclared, but the previos ones known
            // like in X.Y.Z = 3 where X and Y are defined, but Z isn't; then declare Z.
            ExpressionVisitor checkForUnknownAttribute(currentContext(), editor());
            checkForUnknownAttribute.visitNode(attrib);
            DeclarationPointer unknown = checkForUnknownAttribute.lastDeclaration();
            
            // declare the attribute.
            // however, if there's an earlier declaration which does not match the current position
            // (so it's really a different declaration) we skip this.
            Declaration* haveDeclaration = 0;
            if ( unknown.data() && unknown->range() != editorFindRange(target, target) && ! unknown->range().isEmpty() ) {
                kWarning() << "Another declaration exists for this attribute, aborting";
                kDebug() << "Other range: " << unknown->range().castToSimpleRange() << "; own range: " << editorFindRange(target, target).castToSimpleRange();
                continue;
            }
            else if ( unknown.data() ) {
                kWarning() << "Declaration is already created";
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
                Declaration* dec = visitVariableDeclaration<ClassMemberDeclaration>(attrib->attribute, target, haveDeclaration);
                closeAlreadyOpenedContext(internal);
            }
            else {
                injectContext(internal.data());
            
                Declaration* dec = visitVariableDeclaration<ClassMemberDeclaration>(attrib->attribute, target, haveDeclaration);
                dec->setRange(RangeInRevision(internal->range().start, internal->range().start));
                dec->setAutoDeclaration(true);
                DUChainWriteLocker lock(DUChain::lock());
                previousContext->createUse(dec->ownIndex(), editorFindRange(attrib, attrib));
                lock.unlock();
                
                closeInjectedContext();
            }
            
//             kDebug() << "Declaration for attribute " << attrib->attribute << "has been created successfully.";
//             DUChainReadLocker lock(DUChain::lock());
//             kDebug() << "declaration context range:" << dec->context()->range().castToSimpleRange() << "declaration range: " << dec->range().castToSimpleRange();
//             kDebug() << dec->identifier().toString();
//             kDebug() << "all matching declarations in context: " << internal.data()->findDeclarations(dec->identifier()) << "dec: " << dec;
        }
    }
}

void DeclarationBuilder::visitClassDefinition( ClassDefinitionAst* node )
{
    kDebug() << "opening class definition";
    
    DUChainWriteLocker lock(DUChain::lock());
    ClassDeclaration* dec = openDeclaration<ClassDeclaration>( node->name, node );
    eventuallyAssignInternalContext();
    dec->setKind(KDevelop::Declaration::Type);
    dec->clearBaseClasses();
    dec->setClassType(ClassDeclarationData::Class);
    StructureType::Ptr type(new StructureType());
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

void DeclarationBuilder::visitFunctionDefinition( FunctionDefinitionAst* node )
{
    kDebug() << "opening function definition" << node->startLine << node->endLine;
    DeclarationPointer eventualParentDeclaration(currentDeclaration()); // an eventual containing class declaration
    FunctionType::Ptr type;
    FunctionDeclaration* dec = 0;
    QList<Declaration*> existing;
//     {
//         DUChainReadLocker lock(DUChain::lock());
//         existing = currentContext()->findDeclarations(identifierForNode(node->name), editorFindRange(node, node).end);
//     }
//     if ( !existing.isEmpty() && existing.last()->range() == editorFindRange(node, node) )
//         dec = dynamic_cast<FunctionDeclaration*>(existing.last());
//     
    if ( ! dec ) 
        dec = openDeclaration<FunctionDeclaration>( node->name, node );
//     else 
//         setEncountered(existing.last());
    
    eventuallyAssignInternalContext();
    type = FunctionType::Ptr(new FunctionType());
    
    {
        DUChainWriteLocker lock;
        dec->setType(type);
    }
    
    openType(type);
    kDebug() << " <<< open function type";
    DUChainWriteLocker lock(DUChain::lock());
    bool hasFirstArgument = false;
    {
        visitNodeList( node->decorators );
        visitFunctionArguments(node);
        
        closeDeclaration();
        
        // this must be done here, because the type of self must be known when parsing the body
        kDebug() << "Checking weather we have to change argument types...";
        kDebug() <<  eventualParentDeclaration.data() << currentType<FunctionType>()->arguments().length() << m_firstAttributeDeclaration.data() << currentContext()->type() << DUContext::Class;
        if ( eventualParentDeclaration.data() && currentType<FunctionType>()->arguments().length() 
             && m_firstAttributeDeclaration.data() && currentContext()->type() == DUContext::Class ) {
            kDebug() << "Changing self argument type";
            kDebug() << "Arguments left: " << currentType<FunctionType>()->arguments().count();
            currentType<FunctionType>()->removeArgument(currentType<FunctionType>()->arguments().at(0));
            kDebug() << "Arguments left: " << currentType<FunctionType>()->arguments().count();
            DUChainWriteLocker lock(DUChain::lock());
            m_firstAttributeDeclaration->setAbstractType(eventualParentDeclaration->abstractType());
            hasFirstArgument = true;
        }
        
        visitFunctionBody(node);
    }
    kDebug() << " >>> close function type";
    closeType();
    
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
        foreach ( ExpressionAst* expression, node->arguments ) {
            currentIndex += 1;
            realParam = dynamic_cast<NameAst*>(expression);
            
            if ( ! realParam || realParam->context != ExpressionAst::Parameter ) continue;
            
            setLastType(AbstractType::Ptr(0));
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
                    type->addArgument(AbstractType::Ptr(new IntegralType(IntegralType::TypeNone)));
                }
                static_cast<FunctionDeclaration*>(currentDeclaration())->addDefaultParameter(paramDeclaration->identifier().identifier());
                kDebug() << "Arguments count: " << type->arguments().length();
            }
            else {
                kDebug() << "Not a default argument: " << realParam->identifier->value;
                type->addArgument(AbstractType::Ptr(new IntegralType(IntegralType::TypeNone)));
            }
            if ( isFirst ) {
                m_firstAttributeDeclaration = DeclarationPointer(paramDeclaration);
                isFirst = false;
            }
        }
    }
    
    DeclarationBuilderBase::visitArguments(node);
}

}


