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

}

AssertionAst::AssertionAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::AssertionAstType)
{

}

AssignmentAst::AssignmentAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::AssignmentAstType)
{

}

AttributeAst::AttributeAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::AttributeAstType)
{

}

AugmentedAssignmentAst::AugmentedAssignmentAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::AugmentedAssignmentAstType)
{

}

BinaryOperationAst::BinaryOperationAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::BinaryOperationAstType)
{

}

BooleanOperationAst::BooleanOperationAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::BooleanOperationAstType)
{

}

BreakAst::BreakAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::BreakAstType)
{

}

CallAst::CallAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::CallAstType)
{

}

ClassDefinitionAst::ClassDefinitionAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::ClassDefinitionAstType)
{

}

CodeAst::CodeAst(Ast* parent, Ast::AstType type): Ast(parent, Ast::CodeAstType)
{

}

CompareAst::CompareAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::CompareAstType)
{

}

ComprehensionAst::ComprehensionAst(Ast* parent, Ast::AstType type): Ast(parent, Ast::ComprehensionAstType)
{

}

ContinueAst::ContinueAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::ContinueAstType)
{

}

DeleteAst::DeleteAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::DeleteAstType)
{

}

DictionaryComprehensionAst::DictionaryComprehensionAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::DictionaryComprehensionAstType)
{

}

EllipsisAst::EllipsisAst(Ast* parent, Ast::AstType type): SliceAstBase(parent, Ast::EllipsisAstType)
{

}

ExceptionHandlerAst::ExceptionHandlerAst(Ast* parent, Ast::AstType type): Ast(parent, Ast::ExceptionHandlerAstType)
{

}

ExecAst::ExecAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::ExecAstType)
{

}

ExpressionAst::ExpressionAst(Ast* parent, Ast::AstType type): Ast(parent, Ast::ExpressionAstType)
{

}

ExtendedSliceAst::ExtendedSliceAst(Ast* parent, Ast::AstType type): SliceAstBase(parent, Ast::ExtendedSliceAstType)
{

}

ForAst::ForAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::ForAstType)
{

}

FunctionDefinitionAst::FunctionDefinitionAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::FunctionDefinitionAstType)
{

}

GeneratorExpressionAst::GeneratorExpressionAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::GeneratorExpressionAstType)
{

}

GlobalAst::GlobalAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::GlobalAstType)
{

}

Identifier::Identifier(QString value) : value(value)
{

}

IfAst::IfAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::IfAstType)
{

}

IfExpressionAst::IfExpressionAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::IfExpressionAstType)
{

}

ImportAst::ImportAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::ImportAstType)
{

}

ImportFromAst::ImportFromAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::ImportFromAstType)
{

}

KeywordAst::KeywordAst(Ast* parent, Ast::AstType type): Ast(parent, Ast::KeywordAstType)
{

}

LambdaAst::LambdaAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::LambdaAstType)
{

}

ListAst::ListAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::ListAstType)
{

}

NameAst::NameAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::NameAstType)
{

}

NumberAst::NumberAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::NumberAstType)
{

}

PassAst::PassAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::PassAstType)
{

}

PrintAst::PrintAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::PrintAstType)
{

}

RaiseAst::RaiseAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::RaiseAstType)
{

}

ReprAst::ReprAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::ReprAstType)
{

}

ReturnAst::ReturnAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::ReturnAstType)
{

}

SetAst::SetAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::SetAstType)
{

}

SetComprehensionAst::SetComprehensionAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::SetComprehensionAstType)
{

}

SliceAstBase::SliceAstBase(Ast* parent, Ast::AstType type): Ast(parent, Ast::SliceAstType)
{

}

StatementAst::StatementAst(Ast* parent, Ast::AstType type): Ast(parent, Ast::StatementAstType)
{

}

StringAst::StringAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::StringAstType)
{

}

SubscriptAst::SubscriptAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::SubscriptAstType)
{

}

TryExceptAst::TryExceptAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::TryExceptAstType)
{

}

TryFinallyAst::TryFinallyAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::TryFinallyAstType)
{

}

TupleAst::TupleAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::TupleAstType)
{

}

UnaryOperationAst::UnaryOperationAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::UnaryOperationAstType)
{

}

WhileAst::WhileAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::WhileAstType)
{

}

WithAst::WithAst(Ast* parent, Ast::AstType type): StatementAst(parent, Ast::WithAstType)
{

}

YieldAst::YieldAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, Ast::YieldAstType)
{

}

AliasAst::AliasAst(Ast* parent, Ast::AstType type): Ast(parent, Ast::AliasAstType)
{

}



}


#include "pythonast.h"
