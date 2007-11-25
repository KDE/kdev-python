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

Ast::Ast( Ast* parent )
    : parent(parent)
{
}

Ast::~Ast()
{
}

CodeAst::CodeAst()
    : Ast( 0 )
{
}
FunctionDefinitionAst::FunctionDefinitionAst( Ast* parent )
    : StatementAst( parent )
{
}
DecoratorAst::DecoratorAst( Ast* parent )
    : Ast( parent )
{
}
ArgumentAst::ArgumentAst( Ast* parent )
    : Ast( parent )
{
}
ParameterAst::ParameterAst( Ast* parent )
    : Ast( parent )
{
}
StatementAst::StatementAst( Ast* parent )
    : Ast( parent )
{
}
IfAst::IfAst( Ast* parent )
    : StatementAst( parent )
{
}
WhileAst::WhileAst( Ast* parent )
    : StatementAst( parent )
{
}
ForAst::ForAst( Ast* parent )
    : StatementAst( parent )
{
}
ClassDefinitionAst::ClassDefinitionAst( Ast* parent )
    : StatementAst( parent )
{
}
TryAst::TryAst( Ast* parent )
    : StatementAst( parent )
{
}
ExceptAst::ExceptAst( Ast* parent )
    : Ast( parent )
{
}
WithAst::WithAst( Ast* parent )
    : StatementAst( parent )
{
}
ExecAst::ExecAst( Ast* parent )
    : StatementAst( parent )
{
}
GlobalAst::GlobalAst( Ast* parent )
    : StatementAst( parent )
{
}
ImportAst::ImportAst( Ast* parent )
    : StatementAst( parent )
{
}
PlainImportAst::PlainImportAst( Ast* parent )
    : ImportAst( parent )
{
}
StarImportAst::StarImportAst( Ast* parent )
    : ImportAst( parent )
{
}
FromImportAst::FromImportAst( Ast* parent )
    : ImportAst( parent )
{
}
RaiseAst::RaiseAst( Ast* parent )
    : StatementAst( parent )
{
}
PrintAst::PrintAst( Ast* parent )
    : StatementAst( parent )
{
}
ReturnAst::ReturnAst( Ast* parent )
    : StatementAst( parent )
{
}
YieldAst::YieldAst( Ast* parent )
    : StatementAst( parent )
{
}
DelAst::DelAst( Ast* parent )
    : StatementAst( parent )
{
}
AssertAst::AssertAst( Ast* parent )
    : StatementAst( parent )
{
}
ExpressionStatementAst::ExpressionStatementAst( Ast* parent )
    : StatementAst( parent )
{
}
AssignmentAst::AssignmentAst( Ast* parent )
    : StatementAst( parent )
{
}
TargetAst::TargetAst( Ast* parent )
    : Ast( parent )
{
}
AtomAst::AtomAst( Ast* parent )
    : PrimaryAst( parent )
{
}
EnclosureAst::EnclosureAst( Ast* parent )
    : Ast( parent )
{
}
ListAst::ListAst( Ast* parent )
    : Ast( parent )
{
}
ListForAst::ListForAst( Ast* parent )
    : Ast( parent )
{
}
ListIfAst::ListIfAst( Ast* parent )
    : Ast( parent )
{
}
GeneratorAst::GeneratorAst( Ast* parent )
    : Ast( parent )
{
}
GeneratorForAst::GeneratorForAst( Ast* parent )
    : Ast( parent )
{
}
GeneratorIfAst::GeneratorIfAst( Ast* parent )
    : Ast( parent )
{
}
DictionaryAst::DictionaryAst( Ast* parent )
    : Ast( parent )
{
}
PrimaryAst::PrimaryAst( Ast* parent )
    : Ast( parent )
{
}
AttributeReferenceAst::AttributeReferenceAst( Ast* parent )
    : PrimaryAst( parent )
{
}
SubscriptAst::SubscriptAst( Ast* parent )
    : PrimaryAst( parent )
{
}
SliceAst::SliceAst( Ast* parent )
    : PrimaryAst( parent )
{
}
ExtendedSliceAst::ExtendedSliceAst( Ast* parent )
    : SliceAst( parent )
{
}
SimpleSliceAst::SimpleSliceAst( Ast* parent )
    : SliceAst( parent )
{
}
SliceItemAst::SliceItemAst( Ast* parent )
    : Ast( parent )
{
}
ProperSliceItemAst::ProperSliceItemAst( Ast* parent )
    : SliceItemAst( parent )
{
}
ExpressionSliceAst::ExpressionSliceAst( Ast* parent )
    : SliceItemAst( parent )
{
}
EllipsisSliceAst::EllipsisSliceAst( Ast* parent )
    : SliceItemAst( parent )
{
}
CallAst::CallAst( Ast* parent )
    : PrimaryAst( parent )
{
}
ArithmeticExpressionAst::ArithmeticExpressionAst( Ast* parent )
    : Ast( parent )
{
}
UnaryExpressionAst::UnaryExpressionAst( Ast* parent )
    : ArithmeticExpressionAst( parent )
{
}
BinaryExpressionAst::BinaryExpressionAst( Ast* parent )
    : ArithmeticExpressionAst( parent )
{
}
ComparisonAst::ComparisonAst( Ast* parent )
    : Ast( parent )
{
}
BooleanOperationAst::BooleanOperationAst( Ast* parent )
    : Ast( parent )
{
}
ExpressionAst::ExpressionAst( Ast* parent )
    : Ast( parent )
{
}
BooleanExpressionAst::BooleanExpressionAst( Ast* parent )
    : ExpressionAst( parent )
{
}
LambdaAst::LambdaAst( Ast* parent )
    : ExpressionAst( parent )
{
}

DefaultParameterAst::DefaultParameterAst( Ast * parent )
    : ParameterAst( parent )
{
}

ParameterPartAst::ParameterPartAst( Ast * parent )
    : Ast( parent )
{
}

IdentifierParameterPartAst::IdentifierParameterPartAst( Ast * parent )
    : ParameterPartAst( parent )
{
}

ListParameterPartAst::ListParameterPartAst( Ast * parent )
    : ParameterPartAst( parent )
{
}

DictionaryParameterAst::DictionaryParameterAst( Ast * parent )
    : ParameterAst( parent )
{
}

ListParameterAst::ListParameterAst( Ast * parent )
    : ParameterAst( parent )
{
}

}

#include "pythonast.h"
