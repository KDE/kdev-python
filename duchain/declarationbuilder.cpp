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

    eventuallyAssignInternalContext();

    DeclarationBuilderBase::closeDeclaration();
}

template<typename T> T* DeclarationBuilder::visitVariableDeclaration(Ast* node)
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
    return visitVariableDeclaration<T>(id, currentVariableDefinition);
}

/*
 * WARNING: This will return a nullpointer if another than the expected type of variable was found!
 * */
template<typename T> T* DeclarationBuilder::visitVariableDeclaration(Identifier* node, Ast* originalAst)
{
    DUChainWriteLocker lock(DUChain::lock());
    Q_ASSERT(node);
    
    //CursorInRevision until = editorFindRange(node, node).end;
    
    QList<Declaration*> existingDeclarations = currentContext()->findDeclarations(identifierForNode(node), startPos(node));
    
    Declaration* dec = 0;
    
    kDebug() << "VARIABLE CONTEXT: " << currentContext()->scopeIdentifier() << currentContext()->range().castToSimpleRange() << currentContext()->type() << DUContext::Class;
    
    if ( currentContext() && currentContext()->type() == DUContext::Class ) {
        kDebug() << "Creating class member declaration for " << node->value << node->startLine << ":" << node->startCol;
        kDebug() << "Context type: " << currentContext()->scopeIdentifier() << currentContext()->range().castToSimpleRange();
        dec = openDeclaration<ClassMemberDeclaration>(node, originalAst ? originalAst : node);
        DeclarationBuilderBase::closeDeclaration();
        dec->setType(lastType());
        dec->setKind(KDevelop::Declaration::Instance);
    } else if ( existingDeclarations.isEmpty() || existingDeclarations.last()->context() != currentContext() ) {
        kDebug() << "Creating variable declaration for " << node->value << node->startLine << ":" << node->startCol;
        dec = openDeclaration<T>(node, originalAst ? originalAst : node);
        DeclarationBuilderBase::closeDeclaration();
        dec->setType(lastType());
        dec->setKind(KDevelop::Declaration::Instance); // everything is an object in python
    } else {
        qDebug() << "Existing declarations are not empty. count: " << existingDeclarations.count();
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
                qDebug() << "Existing declaration with no type from last declaration.";
                dec->setType(lastType());
            }
        } else {
            qDebug() << "Existing declaration with no type.";
        }
    }
    
    T* result = dynamic_cast<T*>(dec);
    if ( ! result ) kError() << "variable declaration does not have the expected type";
    return result;
}

void DeclarationBuilder::visitCode(CodeAst* node)
{
    Python::ContextBuilder::visitCode(node);
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
        
        TopDUContextPointer contextptr = contextsForModules.value(name->asName ? name->asName : name->name);
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
            kWarning() << "Context for " << moduleName << " is not available";
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
    setLastType(v.lastType());
    
//     kDebug() << ( lastType().unsafeData() ? "last type: " + lastType()->toString() : "don't have a type for variable :(" );
    
    foreach ( ExpressionAst* target, node->targets ) {
        if ( target->astType == Ast::NameAstType ) {
            visitVariableDeclaration<Declaration>(target);
        }
    }
}

void DeclarationBuilder::visitClassDefinition( ClassDefinitionAst* node )
{
    kDebug() << "opening class definition";
//     ClassDeclaration* classDec = new ClassDeclaration(editorFindRange(node->body.first(), node->body.last()), currentContext());
    
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
    DeclarationBuilderBase::visitClassDefinition( node );
    closeType();
    
    closeDeclaration();
}

void DeclarationBuilder::visitFunctionDefinition( FunctionDefinitionAst* node )
{
    kDebug() << "opening function definition" << node->startLine << node->endLine;
    FunctionDeclaration* dec = openDeclaration<FunctionDeclaration>( node->name, node );
    eventuallyAssignInternalContext();
    FunctionType::Ptr type(new FunctionType);
    
    {
        DUChainWriteLocker lock;
        dec->setType(type);
    }

    openType(type);
    kDebug() << " <<< open function type";
    DeclarationBuilderBase::visitFunctionDefinition( node );
    kDebug() << " >>> close function type";
    closeType();
    
//     kDebug() << "Got function return type: " << ( type->returnType().unsafeData() ? type->returnType()->toString() : "<none set>" );
//     kDebug() << type->toString();
    {
        DUChainWriteLocker lock(DUChain::lock());
        dec->setType(type);
    }
    
//     kDebug() << dec->toString();
    
    FunctionType::Ptr funcdecl = dec->type<FunctionType>();
    kDebug() << funcdecl->arguments().toSet();
    
    closeDeclaration();
    
    kDebug() << "parent context: " << currentContext()->parentContext();
    if ( currentContext()->parentContext() ) {
        kDebug() << currentContext()->parentContext()->type() << currentContext()->type() << DUContext::Class;
    }
    
    if ( funcdecl->arguments().length() && currentContext()->type() == DUContext::Class ) {
        kDebug() << "Changing self argument type";
        funcdecl->arguments().removeFirst();
        Q_ASSERT(m_firstAttributeDeclaration.data());
        DUChainWriteLocker lock(DUChain::lock());
        m_firstAttributeDeclaration->setAbstractType(currentDeclaration()->abstractType());
        if ( m_firstAttributeDeclaration->identifier().identifier() != IndexedString("self") ) {
            KDevelop::Problem *p = new KDevelop::Problem();
            p->setFinalLocation(DocumentRange(document(), SimpleRange(node->startLine, node->startCol, node->startLine, 10000)));
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
        p->setFinalLocation(DocumentRange(document(), SimpleRange(node->startLine, node->startCol, node->startLine, 10000))); // only mark first line
        p->setSource(KDevelop::ProblemData::SemanticAnalysis);
        p->setSeverity(KDevelop::ProblemData::Warning);
        p->setDescription(i18n("Non-static class method without arguments, must have at least one (self)"));
        ProblemPointer ptr(p);
        topContext()->addProblem(ptr);
    }
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
            p->setFinalLocation(DocumentRange(document(), SimpleRange(node->startLine, node->startCol, node->endLine, node->endCol))); // only mark first line
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

void DeclarationBuilder::visitLambda( LambdaAst* node )
{
    kDebug() << "opening lambda def";
//     openDeclaration<FunctionDeclaration>( QualifiedIdentifier( "lambda" ), node ) );
    ContextBuilder::visitLambda( node );
//     closeDeclaration();
}

void DeclarationBuilder::visitCall(CallAst* node)
{
//     foreach ( ExpressionAst* currentArgument, node->arguments ) {
//         NameAst* realArgument = dynamic_cast<NameAst*>(currentArgument);
//         if ( realArgument ) {
//             visitVariableDeclaration<Declaration>(realArgument); // some_func(<arg1>, <arg2>)
//         }
//     }
    Python::AstDefaultVisitor::visitCall(node);
}

void DeclarationBuilder::visitArguments( ArgumentsAst* node )
{
    AbstractFunctionDeclaration* function = dynamic_cast<AbstractFunctionDeclaration*>(currentDeclaration());
    kDebug() << "Current context for parameters: " << currentContext();
    kDebug() << currentContext()->scopeIdentifier().toString();
    kDebug() << currentDeclaration()->identifier().toString();
    
    if ( function ) {
        NameAst* realParam;
        bool isFirst = true;
        foreach (ExpressionAst* expression, node->arguments) {
            realParam = dynamic_cast<NameAst*>(expression);
            
            if ( realParam && realParam->context == ExpressionAst::Parameter ) {
                ExpressionVisitor t(currentContext(), editor());
                t.visitExpression(expression);
                
                setLastType(t.lastType());
                Declaration* paramDeclaration = visitVariableDeclaration<Declaration>(realParam);
                setLastType(AbstractType::Ptr(0));
                
                FunctionType::Ptr type = currentType<FunctionType>();
                if ( type && paramDeclaration ) {
                    kDebug() << "Adding argument: " << realParam->identifier->value << paramDeclaration->abstractType();
                    AbstractType::Ptr p = paramDeclaration->abstractType();
                    if ( ! p ) {
                        kDebug() << "No type set for argument, using null type";
                        p = AbstractType::Ptr(new IntegralType(IntegralType::TypeUnsure));
                    }
                    type->addArgument(p);
                }
                if ( isFirst ) {
                    m_firstAttributeDeclaration = paramDeclaration;
                    isFirst = false;
                }
            }
        }
    }
}

}


