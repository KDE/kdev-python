/***************************************************************************
 *   This file is part of KDevelop                                         *
 *   Copyright 2007 Andreas Pakulat <apaku@gmx.de>                         *
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU Library General Public License as       *
 *   published by the Free Software Foundation; either version 2 of the    *
 *   License, or (at your option) any later version.                       *
 *                                                                         *
 *   This program is distributed in the hope that it will be useful,       *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
 *   GNU General Public License for more details.                          *
 *                                                                         *
 *   You should have received a copy of the GNU Library General Public     *
 *   License along with this program; if not, write to the                 *
 *   Free Software Foundation, Inc.,                                       *
 *   51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.         *
 ***************************************************************************/

#include "ast.h"

namespace Python
{

// We never need actual constructors for AST nodes, but it seems to be required, at least for some platforms
// so we provide pseudo implementations
// there's nothing happening here, don't bother reading the code
    
Ast::Ast( Ast* parent, Ast::AstType type ) : parent(parent), astType( type ) { }
Ast::Ast() { }
Ast::~Ast() { }

ArgumentsAst::ArgumentsAst(Ast* parent): Ast(parent, Ast::ArgumentsAstType)
{
    
}

AssertionAst::AssertionAst(Ast* parent): StatementAst(parent, Ast::AssertionAstType)
{
    
}

AssignmentAst::AssignmentAst(Ast* parent): StatementAst(parent, Ast::AssignmentAstType)
{
    
}

AttributeAst::AttributeAst(Ast* parent): ExpressionAst(parent, Ast::AttributeAstType)
{
    
}

AugmentedAssignmentAst::AugmentedAssignmentAst(Ast* parent): StatementAst(parent, Ast::AugmentedAssignmentAstType)
{
    
}

BinaryOperationAst::BinaryOperationAst(Ast* parent): ExpressionAst(parent, Ast::BinaryOperationAstType)
{
    
}

BooleanOperationAst::BooleanOperationAst(Ast* parent): ExpressionAst(parent, Ast::BooleanOperationAstType)
{
    
}

BreakAst::BreakAst(Ast* parent): StatementAst(parent, Ast::BreakAstType)
{
    
}

CallAst::CallAst(Ast* parent): ExpressionAst(parent, Ast::CallAstType)
{
    
}

ClassDefinitionAst::ClassDefinitionAst(Ast* parent): StatementAst(parent, Ast::ClassDefinitionAstType)
{
    
}

CodeAst::CodeAst()
{
    astType = Ast::CodeAstType;
}

CompareAst::CompareAst(Ast* parent): ExpressionAst(parent, Ast::CompareAstType)
{
    
}

ComprehensionAst::ComprehensionAst(Ast* parent): Ast(parent, Ast::ComprehensionAstType)
{
    
}

ContinueAst::ContinueAst(Ast* parent): StatementAst(parent, Ast::ContinueAstType)
{
    
}

DeleteAst::DeleteAst(Ast* parent): StatementAst(parent, Ast::DeleteAstType)
{
    
}

DictAst::DictAst(Ast* parent): ExpressionAst(parent, Ast::DictAstType)
{

}

IndexAst::IndexAst(Ast* parent): SliceAstBase(parent, Ast::IndexAstType)
{

}

SliceAst::SliceAst(Ast* parent): SliceAstBase(parent, Ast::SliceAstType)
{

}

DictionaryComprehensionAst::DictionaryComprehensionAst(Ast* parent): ExpressionAst(parent, Ast::DictionaryComprehensionAstType)
{
    
}

EllipsisAst::EllipsisAst(Ast* parent): SliceAstBase(parent, Ast::EllipsisAstType)
{
    
}

ExceptionHandlerAst::ExceptionHandlerAst(Ast* parent): Ast(parent, Ast::ExceptionHandlerAstType)
{
    
}

ExecAst::ExecAst(Ast* parent): StatementAst(parent, Ast::ExecAstType)
{
    
}

ListComprehensionAst::ListComprehensionAst(Ast* parent): ExpressionAst(parent, Ast::ListComprehensionAstType)
{

}

ExpressionAst::ExpressionAst(Ast* parent, AstType type): Ast(parent, type)
{
    
}

ExtendedSliceAst::ExtendedSliceAst(Ast* parent): SliceAstBase(parent, Ast::ExtendedSliceAstType)
{
    
}

ForAst::ForAst(Ast* parent): StatementAst(parent, Ast::ForAstType)
{
    
}

FunctionDefinitionAst::FunctionDefinitionAst(Ast* parent): StatementAst(parent, Ast::FunctionDefinitionAstType)
{
    
}

GeneratorExpressionAst::GeneratorExpressionAst(Ast* parent): ExpressionAst(parent, Ast::GeneratorExpressionAstType)
{
    
}

GlobalAst::GlobalAst(Ast* parent): StatementAst(parent, Ast::GlobalAstType)
{
    
}

Identifier::Identifier(QString value) : value(value)
{
    
}

IfAst::IfAst(Ast* parent): StatementAst(parent, Ast::IfAstType)
{
    
}

IfExpressionAst::IfExpressionAst(Ast* parent): ExpressionAst(parent, Ast::IfExpressionAstType)
{
    
}

ImportAst::ImportAst(Ast* parent): StatementAst(parent, Ast::ImportAstType)
{
    
}

ImportFromAst::ImportFromAst(Ast* parent): StatementAst(parent, Ast::ImportFromAstType)
{
    
}

KeywordAst::KeywordAst(Ast* parent): Ast(parent, Ast::KeywordAstType)
{
    
}

LambdaAst::LambdaAst(Ast* parent): ExpressionAst(parent, Ast::LambdaAstType)
{
    
}

ListAst::ListAst(Ast* parent): ExpressionAst(parent, Ast::ListAstType)
{
    
}

NameAst::NameAst(Ast* parent): ExpressionAst(parent, Ast::NameAstType)
{
    
}

NumberAst::NumberAst(Ast* parent): ExpressionAst(parent, Ast::NumberAstType)
{
    
}

PassAst::PassAst(Ast* parent): StatementAst(parent, Ast::PassAstType)
{
    
}

PrintAst::PrintAst(Ast* parent): StatementAst(parent, Ast::PrintAstType)
{
    
}

RaiseAst::RaiseAst(Ast* parent): StatementAst(parent, Ast::RaiseAstType)
{
    
}

ReprAst::ReprAst(Ast* parent): ExpressionAst(parent, Ast::ReprAstType)
{
    
}

ReturnAst::ReturnAst(Ast* parent): StatementAst(parent, Ast::ReturnAstType)
{
    
}

SetAst::SetAst(Ast* parent): ExpressionAst(parent, Ast::SetAstType)
{
    
}

SetComprehensionAst::SetComprehensionAst(Ast* parent): ExpressionAst(parent, Ast::SetComprehensionAstType)
{
    
}

SliceAstBase::SliceAstBase(Ast* parent, AstType type): Ast(parent, type)
{
    
}

StatementAst::StatementAst(Ast* parent, AstType type): Ast(parent, type)
{
    
}

StringAst::StringAst(Ast* parent): ExpressionAst(parent, Ast::StringAstType)
{
    
}

SubscriptAst::SubscriptAst(Ast* parent): ExpressionAst(parent, Ast::SubscriptAstType)
{
    
}

TryExceptAst::TryExceptAst(Ast* parent): StatementAst(parent, Ast::TryExceptAstType)
{
    
}

TryFinallyAst::TryFinallyAst(Ast* parent): StatementAst(parent, Ast::TryFinallyAstType)
{
    
}

TupleAst::TupleAst(Ast* parent): ExpressionAst(parent, Ast::TupleAstType)
{
    
}

UnaryOperationAst::UnaryOperationAst(Ast* parent): ExpressionAst(parent, Ast::UnaryOperationAstType)
{
    
}

WhileAst::WhileAst(Ast* parent): StatementAst(parent, Ast::WhileAstType)
{
    
}

WithAst::WithAst(Ast* parent): StatementAst(parent, Ast::WithAstType)
{
    
}

YieldAst::YieldAst(Ast* parent): ExpressionAst(parent, Ast::YieldAstType)
{
    
}

AliasAst::AliasAst(Ast* parent): Ast(parent, Ast::AliasAstType)
{
    
}



}


#include "pythonast.h"
