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
#include "declarationbuilder.h"

#include <QByteArray>

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

#include "contextbuilder.h"

#include "pythoneditorintegrator.h"
#include "QtGlobal"

#include <declarations/importedmoduledeclaration.h>
#include <../kdevplatform/language/duchain/declaration.h>
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
    
    kDebug() << "VARIABLE CONTEXT: " << currentContext()->scopeIdentifier() << currentContext()->range().castToSimpleRange() << currentContext()->type();
    
    if ( currentContext() && currentContext()->type() == DUContext::Class ) {
        kDebug() << "Creating class member declaration for " << node->value << node->startLine << ":" << node->startCol;
        kDebug() << "Context type: " << currentContext()->scopeIdentifier() << currentContext()->range().castToSimpleRange();
        dec = openDeclaration<ClassMemberDeclaration>(node, originalAst ? originalAst : node, DeclarationIsDefinition);
        closeDeclaration();
        dec->setType(lastType());
        dec->setKind(KDevelop::Declaration::Instance);
    } else if ( existingDeclarations.isEmpty() || existingDeclarations.last()->context() != currentContext() ) {
        kDebug() << "Creating variable declaration for " << node->value << node->startLine << ":" << node->startCol;
        dec = openDeclaration<T>(node, originalAst ? originalAst : node, DeclarationIsDefinition);
        closeDeclaration();
        dec->setType(lastType());
        dec->setKind(KDevelop::Declaration::Instance); // everything is an object in python
    } else {
        qDebug() << "Existing declarations are not empty. count: " << existingDeclarations.count();
        dec = existingDeclarations.last();
        AbstractType::Ptr lasttype = dec->abstractType();
        AbstractType::Ptr type = lastType();
        if(type){
            if ( lasttype && !lasttype->equals(type.unsafeData()) ) {
                IntegralType::Ptr integral = IntegralType::Ptr::dynamicCast(lasttype);
                if ( integral &&  integral->dataType() == IntegralType::TypeMixed ) {
                    dec->setType(type);
                }else{
                    UnsureType::Ptr unsure = UnsureType::Ptr::dynamicCast(lasttype);
                    // maybe it's referenced?
                    ReferenceType::Ptr rType = ReferenceType::Ptr::dynamicCast(lasttype);
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
                    unsure->addType(type->indexed());
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

void DeclarationBuilder::visitExceptionHandler(ExceptionHandlerAst* node)
{
    if ( dynamic_cast<NameAst*>(node->name) ) visitVariableDeclaration<Declaration>(node->name); // except Error as <vardecl>
    DeclarationBuilderBase::visitExceptionHandler(node);
}

void DeclarationBuilder::visitFor(ForAst* node)
{
    if ( node->target->astType == Ast::NameAstType ) visitVariableDeclaration<Declaration>(node->target);
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
    foreach ( AliasAst* name, node->names ) {
        TopDUContextPointer contextptr = contextsForModules.value(name->asName ? name->asName->value : name->name->value);
        kDebug() << "Chain for document: " << contextptr;
        m_importContextsForImportStatement.push(contextptr);
        importedModuleDeclaration* dec;
        kDebug() << ( name->asName ? name->asName->value : QString("no asName") ) << ( name->name ? name->name->value : "no name" );
        if ( name->asName ) {
            dec = visitVariableDeclaration<importedModuleDeclaration>(name->asName);
        }
        else {
            dec = visitVariableDeclaration<importedModuleDeclaration>(name->name);
        }
            
        QString moduleName = name->name->value;
        if ( name->asName && name->asName ) 
            moduleName += "." + name->asName->value;
        kDebug() << "Module name: " << moduleName;
        if ( dec ) {
            DUChainWriteLocker lock(DUChain::lock());
            dec->m_moduleIdentifier = moduleName;
            dec->setType(IntegralType::Ptr(new IntegralType(IntegralType::TypeMixed)));
        }
        m_importContextsForImportStatement.clear();
    }
}

void DeclarationBuilder::visitImportFrom(ImportFromAst* node)
{
    Python::AstDefaultVisitor::visitImportFrom(node);
    foreach ( AliasAst* name, node->names ) {
        importedModuleDeclaration* dec = 0;
        if ( name->asName ) {
            dec = visitVariableDeclaration<importedModuleDeclaration>(name->asName);
        }
        else {
            dec = visitVariableDeclaration<importedModuleDeclaration>(name->name);
        }
        if ( dec && name->name && node->module ) {
            dec->m_moduleIdentifier = node->module->value + "." + name->name->value;
            kDebug() << "FromImport module name: " << name->name->value;
        }
        if ( dec ) {
            dec->setType(IntegralType::Ptr(new IntegralType(IntegralType::TypeMixed)));
        }
    }
}

void DeclarationBuilder::visitAssignment(AssignmentAst* node)
{
    ExpressionVisitor v(currentContext());
    v.visitNode(node->value);
    setLastType(v.lastType());
    
    kDebug() << ( lastType().unsafeData() ? "last type: " + lastType()->toString() : "don't have a type for variable :(" );
    
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
    
    ClassDeclaration* dec = openDeclaration<ClassDeclaration>( node->name, node );
    eventuallyAssignInternalContext();
    dec->setKind(KDevelop::Declaration::Type);
    dec->clearBaseClasses();
    dec->setClassType(ClassDeclarationData::Class);
    StructureType::Ptr type(new StructureType());
    type->setDeclaration(dec);
    dec->setType(type);
    
    DeclarationBuilderBase::visitClassDefinition( node );
    
    closeDeclaration();
}

void DeclarationBuilder::visitFunctionDefinition( FunctionDefinitionAst* node )
{
    kDebug() << "opening function definition";
    FunctionDeclaration* dec = openDeclaration<FunctionDeclaration>( node->name, node );

    FunctionType::Ptr type(new FunctionType);
    
    {
        DUChainWriteLocker lock;
        dec->setType(type);
    }

    openType(type);
    ContextBuilder::visitFunctionDefinition( node );
    closeType();
    
    kDebug() << "Got function return type: " << ( type->returnType().unsafeData() ? type->returnType()->toString() : "<none set>" );
    
    closeDeclaration();
}

void DeclarationBuilder::visitReturn(ReturnAst* node)
{
    ExpressionVisitor v(currentContext());
    v.visitNode(node->value);
    if ( node->value ) {
        TypePtr<FunctionType> t = currentType<FunctionType>();
        if ( ! t.unsafeData() ) {
            KDevelop::Problem *p = new KDevelop::Problem();
            p->setFinalLocation(DocumentRange(document(), SimpleRange(node->startLine, node->startCol, node->endLine, node->endCol)));
            p->setSource(KDevelop::ProblemData::SemanticAnalysis);
            p->setDescription(i18n("Return statement not within function declaration"));
            ProblemPointer ptr(p);
            topContext()->addProblem(ptr);
            return;
        }
        AbstractType::Ptr encountered = v.lastType();
        kDebug() << "Found type: " << encountered->toString();
        t->setReturnType(encountered);
    }
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
    foreach ( ExpressionAst* currentArgument, node->arguments ) {
        NameAst* realArgument = dynamic_cast<NameAst*>(currentArgument);
        if ( realArgument ) {
            visitVariableDeclaration<Declaration>(realArgument); // some_func(<arg1>, <arg2>)
        }
    }
    Python::AstDefaultVisitor::visitCall(node);
}

void DeclarationBuilder::visitArguments( ArgumentsAst* node )
{
    AbstractFunctionDeclaration* function = dynamic_cast<AbstractFunctionDeclaration*>(currentDeclaration());
    kDebug() << "Current context for parameters: " << currentContext();
    if ( function ) {
        NameAst* realParam;
        foreach (ExpressionAst* expression, node->arguments) {
            realParam = dynamic_cast<NameAst*>(expression);
            if ( realParam && realParam->context == ExpressionAst::Parameter ) {
                Declaration* paramDeclaration = visitVariableDeclaration<Declaration>(realParam);
                function->addDefaultParameter(IndexedString(realParam->identifier->value));
                FunctionType::Ptr type = currentType<FunctionType>();
                if ( type && paramDeclaration ) type->addArgument(paramDeclaration->abstractType());
            }
            else {
                DeclarationBuilderBase::visitArguments(node);
            }
        }
    }
}

}

