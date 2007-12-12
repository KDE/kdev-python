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

Ast::Ast( Ast* parent, Ast::AstType type )
    : parent(parent), astType( type )
{
}

Ast::~Ast()
{
}

CodeAst::CodeAst()
    : Ast( 0, Ast::CodeAst )
{
}
FunctionDefinitionAst::FunctionDefinitionAst( Ast* parent )
    : StatementAst( parent, Ast::FunctionDefinitionAst )
{
}
DecoratorAst::DecoratorAst( Ast* parent )
    : Ast( parent, Ast::DecoratorAst )
{
}
ArgumentAst::ArgumentAst( Ast* parent )
    : Ast( parent, Ast::ArgumentAst )
{
}
ParameterAst::ParameterAst( Ast* parent, Ast::AstType type )
    : Ast( parent, type )
{
}
StatementAst::StatementAst( Ast* parent, Ast::AstType type )
    : Ast( parent, type )
{
}
IfAst::IfAst( Ast* parent )
    : StatementAst( parent, Ast::IfAst )
{
}
WhileAst::WhileAst( Ast* parent )
    : StatementAst( parent, Ast::WhileAst )
{
}
ForAst::ForAst( Ast* parent )
    : StatementAst( parent, Ast::ForAst )
{
}
ClassDefinitionAst::ClassDefinitionAst( Ast* parent )
    : StatementAst( parent, Ast::ClassDefinitionAst )
{
}
TryAst::TryAst( Ast* parent )
    : StatementAst( parent, Ast::TryAst )
{
}
ExceptAst::ExceptAst( Ast* parent )
    : Ast( parent, Ast::ExceptAst )
{
}
WithAst::WithAst( Ast* parent )
    : StatementAst( parent, Ast::WithAst )
{
}
ExecAst::ExecAst( Ast* parent )
    : StatementAst( parent, Ast::ExecAst )
{
}
GlobalAst::GlobalAst( Ast* parent )
    : StatementAst( parent, Ast::GlobalAst )
{
}
ImportAst::ImportAst( Ast* parent, Ast::AstType type )
    : StatementAst( parent, type )
{
}
PlainImportAst::PlainImportAst( Ast* parent )
    : ImportAst( parent, Ast::PlainImportAst )
{
}
StarImportAst::StarImportAst( Ast* parent )
    : ImportAst( parent, Ast::StarImportAst )
{
}
FromImportAst::FromImportAst( Ast* parent )
    : ImportAst( parent, Ast::FromImportAst )
{
}
RaiseAst::RaiseAst( Ast* parent )
    : StatementAst( parent, Ast::RaiseAst )
{
}
PrintAst::PrintAst( Ast* parent )
    : StatementAst( parent, Ast::PrintAst )
{
}

ReturnAst::ReturnAst( Ast* parent )
    : StatementAst( parent, Ast::ReturnAst )
{
}
YieldAst::YieldAst( Ast* parent )
    : StatementAst( parent, Ast::YieldAst )
{
}
DelAst::DelAst( Ast* parent )
    : StatementAst( parent, Ast::DelAst )
{
}
AssertAst::AssertAst( Ast* parent )
    : StatementAst( parent, Ast::AssertAst )
{
}
ExpressionStatementAst::ExpressionStatementAst( Ast* parent )
    : StatementAst( parent, Ast::ExpressionStatementAst )
{
}
AssignmentAst::AssignmentAst( Ast* parent )
    : StatementAst( parent, Ast::AssignmentAst )
{
}
TargetAst::TargetAst( Ast* parent )
    : Ast( parent, Ast::TargetAst )
{
}
AtomAst::AtomAst( Ast* parent )
    : PrimaryAst( parent, Ast::AtomAst )
{
}
EnclosureAst::EnclosureAst( Ast* parent )
    : Ast( parent, Ast::EnclosureAst )
{
}
ListAst::ListAst( Ast* parent )
    : Ast( parent, Ast::ListAst )
{
}
ListForAst::ListForAst( Ast* parent )
    : Ast( parent, Ast::ListForAst )
{
}
ListIfAst::ListIfAst( Ast* parent )
    : Ast( parent, Ast::ListIfAst )
{
}
GeneratorAst::GeneratorAst( Ast* parent )
    : Ast( parent, Ast::GeneratorAst )
{
}
GeneratorForAst::GeneratorForAst( Ast* parent )
    : Ast( parent, Ast::GeneratorForAst )
{
}
GeneratorIfAst::GeneratorIfAst( Ast* parent )
    : Ast( parent, Ast::GeneratorIfAst )
{
}
DictionaryAst::DictionaryAst( Ast* parent )
    : Ast( parent, Ast::DictionaryAst )
{
}
PrimaryAst::PrimaryAst( Ast* parent, Ast::AstType type )
    : Ast( parent, type )
{
}
AttributeReferenceAst::AttributeReferenceAst( Ast* parent )
    : PrimaryAst( parent, Ast::AttributeReferenceAst )
{
}
SubscriptAst::SubscriptAst( Ast* parent )
    : PrimaryAst( parent, Ast::SubscriptAst )
{
}
SliceAst::SliceAst( Ast* parent, Ast::AstType type )
    : PrimaryAst( parent, type )
{
}
ExtendedSliceAst::ExtendedSliceAst( Ast* parent )
    : SliceAst( parent, Ast::ExtendedSliceAst )
{
}
SimpleSliceAst::SimpleSliceAst( Ast* parent )
    : SliceAst( parent, Ast::SimpleSliceAst )
{
}
SliceItemAst::SliceItemAst( Ast* parent, Ast::AstType type )
    : Ast( parent, type )
{
}
ProperSliceItemAst::ProperSliceItemAst( Ast* parent )
    : SliceItemAst( parent, Ast::ProperSliceItemAst )
{
}
ExpressionSliceAst::ExpressionSliceAst( Ast* parent )
    : SliceItemAst( parent, Ast::ExpressionSliceAst )
{
}
EllipsisSliceAst::EllipsisSliceAst( Ast* parent )
    : SliceItemAst( parent, Ast::EllipsisSliceAst )
{
}
CallAst::CallAst( Ast* parent )
    : PrimaryAst( parent, Ast::CallAst )
{
}
ArithmeticExpressionAst::ArithmeticExpressionAst( Ast* parent, Ast::AstType type )
    : ExpressionAst( parent, type )
{
}
UnaryExpressionAst::UnaryExpressionAst( Ast* parent )
    : ArithmeticExpressionAst( parent, Ast::UnaryExpressionAst )
{
}
BinaryExpressionAst::BinaryExpressionAst( Ast* parent )
    : ArithmeticExpressionAst( parent, Ast::BinaryExpressionAst )
{
}
ComparisonAst::ComparisonAst( Ast* parent )
    : BooleanOperationAst( parent, Ast::ComparisonAst )
{
}
BooleanOperationAst::BooleanOperationAst( Ast* parent, Ast::AstType type )
    : Ast( parent, type )
{
}
ExpressionAst::ExpressionAst( Ast* parent, Ast::AstType type )
    : Ast( parent, type )
{
}
ConditionalExpressionAst::ConditionalExpressionAst( Ast* parent )
    : ExpressionAst( parent, Ast::ConditionalExpressionAst )
{
}
LambdaAst::LambdaAst( Ast* parent )
    : ExpressionAst( parent, Ast::LambdaAst )
{
}

DefaultParameterAst::DefaultParameterAst( Ast * parent )
    : ParameterAst( parent, Ast::DefaultParameterAst )
{
}

ParameterPartAst::ParameterPartAst( Ast * parent, Ast::AstType type )
    : Ast( parent, type )
{
}

IdentifierParameterPartAst::IdentifierParameterPartAst( Ast * parent )
    : ParameterPartAst( parent, Ast::IdentifierParameterPartAst )
{
}

ListParameterPartAst::ListParameterPartAst( Ast * parent )
    : ParameterPartAst( parent, Ast::ListParameterPartAst )
{
}

DictionaryParameterAst::DictionaryParameterAst( Ast * parent )
    : ParameterAst( parent, Ast::DictionaryParameterAst )
{
}

ListParameterAst::ListParameterAst( Ast * parent )
    : ParameterAst( parent, Ast::ListParameterAst )
{
}

BooleanNotOperationAst::BooleanNotOperationAst( Ast * parent )
    : BooleanOperationAst( parent, Ast::BooleanNotOperationAst )
{
}

BooleanOrOperationAst::BooleanOrOperationAst( Ast * parent )
    : BooleanOperationAst( parent, Ast::BooleanOrOperationAst )
{
}

BooleanAndOperationAst::BooleanAndOperationAst( Ast * parent )
    : BooleanOperationAst( parent, Ast::BooleanAndOperationAst )
{
}

IdentifierAst::IdentifierAst( Ast * parent )
    : ExpressionAst( parent, Ast::IdentifierAst )
{
}


}


#include "pythonast.h"
