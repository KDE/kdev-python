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
Ast::~Ast() { }

ArgumentsAst::ArgumentsAst(Ast* parent, Ast::AstType type): Ast(parent, Ast::ArgumentsAstType)
{
    Q_UNUSED(type);
}

AssertionAst::AssertionAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::AssertionAstType)
{
    Q_UNUSED(type);
}

AssignmentAst::AssignmentAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::AssignmentAstType)
{
    Q_UNUSED(type);
}

AttributeAst::AttributeAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::AttributeAstType)
{
    Q_UNUSED(type);
}

AugmentedAssignmentAst::AugmentedAssignmentAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::AugmentedAssignmentAstType)
{
    Q_UNUSED(type);
}

BinaryOperationAst::BinaryOperationAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::BinaryOperationAstType)
{
    Q_UNUSED(type);
}

BooleanOperationAst::BooleanOperationAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::BooleanOperationAstType)
{
    Q_UNUSED(type);
}

BreakAst::BreakAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::BreakAstType)
{
    Q_UNUSED(type);
}

CallAst::CallAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::CallAstType)
{
    Q_UNUSED(type);
}

ClassDefinitionAst::ClassDefinitionAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::ClassDefinitionAstType)
{
    Q_UNUSED(type);
}

CodeAst::CodeAst(Ast* parent, Ast::AstType type): Ast(parent, Ast::CodeAstType)
{
    Q_UNUSED(type);
}

CompareAst::CompareAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::CompareAstType)
{
    Q_UNUSED(type);
}

ComprehensionAst::ComprehensionAst(Ast* parent, Ast::AstType type): Ast(parent, Ast::ComprehensionAstType)
{
    Q_UNUSED(type);
}

ContinueAst::ContinueAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::ContinueAstType)
{
    Q_UNUSED(type);
}

DeleteAst::DeleteAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::DeleteAstType)
{
    Q_UNUSED(type);
}

DictionaryComprehensionAst::DictionaryComprehensionAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::DictionaryComprehensionAstType)
{
    Q_UNUSED(type);
}

EllipsisAst::EllipsisAst(Ast* parent, Ast::AstType type): SliceAstBase(parent, Ast::EllipsisAstType)
{
    Q_UNUSED(type);
}

ExceptionHandlerAst::ExceptionHandlerAst(Ast* parent, Ast::AstType type): Ast(parent, Ast::ExceptionHandlerAstType)
{
    Q_UNUSED(type);
}

ExecAst::ExecAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::ExecAstType)
{
    Q_UNUSED(type);
}

ExpressionAst::ExpressionAst(Ast* parent, Ast::AstType type): Ast(parent, Ast::ExpressionAstType)
{
    Q_UNUSED(type);
}

ExtendedSliceAst::ExtendedSliceAst(Ast* parent, Ast::AstType type): SliceAstBase(parent, Ast::ExtendedSliceAstType)
{
    Q_UNUSED(type);
}

ForAst::ForAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::ForAstType)
{
    Q_UNUSED(type);
}

FunctionDefinitionAst::FunctionDefinitionAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::FunctionDefinitionAstType)
{
    Q_UNUSED(type);
}

GeneratorExpressionAst::GeneratorExpressionAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::GeneratorExpressionAstType)
{
    Q_UNUSED(type);
}

GlobalAst::GlobalAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::GlobalAstType)
{
    Q_UNUSED(type);
}

Identifier::Identifier(QString value) : value(value)
{
    
}

IfAst::IfAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::IfAstType)
{
    Q_UNUSED(type);
}

IfExpressionAst::IfExpressionAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::IfExpressionAstType)
{
    Q_UNUSED(type);
}

ImportAst::ImportAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::ImportAstType)
{
    Q_UNUSED(type);
}

ImportFromAst::ImportFromAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::ImportFromAstType)
{
    Q_UNUSED(type);
}

KeywordAst::KeywordAst(Ast* parent, Ast::AstType type): Ast(parent, Ast::KeywordAstType)
{
    Q_UNUSED(type);
}

LambdaAst::LambdaAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::LambdaAstType)
{
    Q_UNUSED(type);
}

ListAst::ListAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::ListAstType)
{
    Q_UNUSED(type);
}

NameAst::NameAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::NameAstType)
{
    Q_UNUSED(type);
}

NumberAst::NumberAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::NumberAstType)
{
    Q_UNUSED(type);
}

PassAst::PassAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::PassAstType)
{
    Q_UNUSED(type);
}

PrintAst::PrintAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::PrintAstType)
{
    Q_UNUSED(type);
}

RaiseAst::RaiseAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::RaiseAstType)
{
    Q_UNUSED(type);
}

ReprAst::ReprAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::ReprAstType)
{
    Q_UNUSED(type);
}

ReturnAst::ReturnAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::ReturnAstType)
{
    Q_UNUSED(type);
}

SetAst::SetAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::SetAstType)
{
    Q_UNUSED(type);
}

SetComprehensionAst::SetComprehensionAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::SetComprehensionAstType)
{
    Q_UNUSED(type);
}

SliceAstBase::SliceAstBase(Ast* parent, Ast::AstType type): Ast(parent, Ast::SliceAstType)
{
    Q_UNUSED(type);
}

StatementAst::StatementAst(Ast* parent, Ast::AstType type): Ast(parent, Ast::StatementAstType)
{
    Q_UNUSED(type);
}

StringAst::StringAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::StringAstType)
{
    Q_UNUSED(type);
}

SubscriptAst::SubscriptAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::SubscriptAstType)
{
    Q_UNUSED(type);
}

TryExceptAst::TryExceptAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::TryExceptAstType)
{
    Q_UNUSED(type);
}

TryFinallyAst::TryFinallyAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::TryFinallyAstType)
{
    Q_UNUSED(type);
}

TupleAst::TupleAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::TupleAstType)
{
    Q_UNUSED(type);
}

UnaryOperationAst::UnaryOperationAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::UnaryOperationAstType)
{
    Q_UNUSED(type);
}

WhileAst::WhileAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::WhileAstType)
{
    Q_UNUSED(type);
}

WithAst::WithAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::WithAstType)
{
    Q_UNUSED(type);
}

YieldAst::YieldAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::YieldAstType)
{
    Q_UNUSED(type);
}

AliasAst::AliasAst(Ast* parent, Ast::AstType type): Ast(parent, Ast::AliasAstType)
{
    Q_UNUSED(type);
}



}


#include "pythonast.h"
