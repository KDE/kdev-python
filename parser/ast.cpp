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
    
Ast::Ast( Ast* parent, Ast::AstType type ) : parent(parent), astType( type ), startCol(0), startLine(-5), endCol(0), endLine(0), hasUsefulRangeInformation(false), context(0) { }
Ast::Ast() :  parent(0), startCol(0), startLine(-5), endCol(0), endLine(0), hasUsefulRangeInformation(false), context(0) { }
Ast::~Ast() { }

ArgumentsAst::ArgumentsAst(Ast* parent): Ast(parent, Ast::ArgumentsAstType), arg_lineno(0), arg_col_offset(0), vararg_lineno(0), vararg_col_offset(0)
{
    
}

AssertionAst::AssertionAst(Ast* parent): StatementAst(parent, Ast::AssertionAstType) 
{
    
}

AssignmentAst::AssignmentAst(Ast* parent): StatementAst(parent, Ast::AssignmentAstType), value(0)
{
    
}

AttributeAst::AttributeAst(Ast* parent): ExpressionAst(parent, Ast::AttributeAstType), value(0), depth(0)
{
    
}

AugmentedAssignmentAst::AugmentedAssignmentAst(Ast* parent): StatementAst(parent, Ast::AugmentedAssignmentAstType), value(0)
{
    
}

BinaryOperationAst::BinaryOperationAst(Ast* parent): ExpressionAst(parent, Ast::BinaryOperationAstType), lhs(0), rhs(0)
{
    
}

BooleanOperationAst::BooleanOperationAst(Ast* parent): ExpressionAst(parent, Ast::BooleanOperationAstType)
{
    
}

BreakAst::BreakAst(Ast* parent): StatementAst(parent, Ast::BreakAstType)
{
    
}

CallAst::CallAst(Ast* parent): ExpressionAst(parent, Ast::CallAstType), function(0), keywordArguments(0), starArguments(0)
{
    
}

ClassDefinitionAst::ClassDefinitionAst(Ast* parent): StatementAst(parent, Ast::ClassDefinitionAstType), name(0)
{
    
}

CodeAst::CodeAst() : name(0)
{
    astType = Ast::CodeAstType;
}

CompareAst::CompareAst(Ast* parent): ExpressionAst(parent, Ast::CompareAstType), leftmostElement(0)
{
    
}

ComprehensionAst::ComprehensionAst(Ast* parent): Ast(parent, Ast::ComprehensionAstType), target(0), iterator(0)
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

IndexAst::IndexAst(Ast* parent): SliceAstBase(parent, Ast::IndexAstType), value(0)
{

}

SliceAst::SliceAst(Ast* parent): SliceAstBase(parent, Ast::SliceAstType), lower(0), upper(0), step(0)
{

}

DictionaryComprehensionAst::DictionaryComprehensionAst(Ast* parent): ExpressionAst(parent, Ast::DictionaryComprehensionAstType), key(0), value(0)
{
    
}

EllipsisAst::EllipsisAst(Ast* parent): SliceAstBase(parent, Ast::EllipsisAstType)
{
    
}

ExceptionHandlerAst::ExceptionHandlerAst(Ast* parent): Ast(parent, Ast::ExceptionHandlerAstType), type(0), name(0)
{
    
}

ExecAst::ExecAst(Ast* parent): StatementAst(parent, Ast::ExecAstType), body(0), globals(0), locals(0)
{
    
}

ListComprehensionAst::ListComprehensionAst(Ast* parent): ExpressionAst(parent, Ast::ListComprehensionAstType), element(0)
{

}

ExpressionAst::ExpressionAst(Ast* parent, AstType type): Ast(parent, type), value(0), belongsToCall(0)
{
    
}

ExtendedSliceAst::ExtendedSliceAst(Ast* parent): SliceAstBase(parent, Ast::ExtendedSliceAstType)
{
    
}

ForAst::ForAst(Ast* parent): StatementAst(parent, Ast::ForAstType), target(0), iterator(0)
{
    
}

FunctionDefinitionAst::FunctionDefinitionAst(Ast* parent): StatementAst(parent, Ast::FunctionDefinitionAstType), name(0), arguments(0)
{
    
}

GeneratorExpressionAst::GeneratorExpressionAst(Ast* parent): ExpressionAst(parent, Ast::GeneratorExpressionAstType), element(0)
{
    
}

GlobalAst::GlobalAst(Ast* parent): StatementAst(parent, Ast::GlobalAstType)
{
    
}

Identifier::Identifier(QString value) : value(value)
{
    
}

IfAst::IfAst(Ast* parent): StatementAst(parent, Ast::IfAstType), condition(0)
{
    
}

IfExpressionAst::IfExpressionAst(Ast* parent): ExpressionAst(parent, Ast::IfExpressionAstType), condition(0)
{
    
}

ImportAst::ImportAst(Ast* parent): StatementAst(parent, Ast::ImportAstType)
{
    
}

ImportFromAst::ImportFromAst(Ast* parent): StatementAst(parent, Ast::ImportFromAstType), module(0), level(0)
{
    
}

KeywordAst::KeywordAst(Ast* parent): Ast(parent, Ast::KeywordAstType), argumentName(0), value(0)
{
    
}

LambdaAst::LambdaAst(Ast* parent): ExpressionAst(parent, Ast::LambdaAstType), arguments(0)
{
    
}

ListAst::ListAst(Ast* parent): ExpressionAst(parent, Ast::ListAstType)
{
    
}

NameAst::NameAst(Ast* parent): ExpressionAst(parent, Ast::NameAstType), identifier(0)
{
    
}

NumberAst::NumberAst(Ast* parent): ExpressionAst(parent, Ast::NumberAstType), value("0")
{
    
}

PassAst::PassAst(Ast* parent): StatementAst(parent, Ast::PassAstType)
{
    
}

PrintAst::PrintAst(Ast* parent): StatementAst(parent, Ast::PrintAstType), destination(0), newline(0)
{
    
}

RaiseAst::RaiseAst(Ast* parent): StatementAst(parent, Ast::RaiseAstType), type(0)
{
    
}

ReprAst::ReprAst(Ast* parent): ExpressionAst(parent, Ast::ReprAstType), value(0)
{
    
}

ReturnAst::ReturnAst(Ast* parent): StatementAst(parent, Ast::ReturnAstType), value(0)
{
    
}

SetAst::SetAst(Ast* parent): ExpressionAst(parent, Ast::SetAstType)
{
    
}

SetComprehensionAst::SetComprehensionAst(Ast* parent): ExpressionAst(parent, Ast::SetComprehensionAstType), element(0)
{
    
}

SliceAstBase::SliceAstBase(Ast* parent, AstType type): Ast(parent, type)
{
    
}

StatementAst::StatementAst(Ast* parent, AstType type): Ast(parent, type)
{
    
}

StringAst::StringAst(Ast* parent): ExpressionAst(parent, Ast::StringAstType), value("")
{
    
}

SubscriptAst::SubscriptAst(Ast* parent): ExpressionAst(parent, Ast::SubscriptAstType), value(0), slice(0)
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

UnaryOperationAst::UnaryOperationAst(Ast* parent): ExpressionAst(parent, Ast::UnaryOperationAstType), operand(0)
{
    
}

WhileAst::WhileAst(Ast* parent): StatementAst(parent, Ast::WhileAstType), condition(0)
{
    
}

WithAst::WithAst(Ast* parent): StatementAst(parent, Ast::WithAstType), contextExpression(0)
{
    
}

YieldAst::YieldAst(Ast* parent): ExpressionAst(parent, Ast::YieldAstType), value(0)
{
    
}

AliasAst::AliasAst(Ast* parent): Ast(parent, Ast::AliasAstType), name(0), asName(0)
{
    
}



}
