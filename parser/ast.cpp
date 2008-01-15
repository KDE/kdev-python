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
    : StatementAst( parent, Ast::FunctionDefinitionAst ), functionName( 0 )
{
}
DecoratorAst::DecoratorAst( Ast* parent )
    : Ast( parent, Ast::DecoratorAst )
{
}
ArgumentAst::ArgumentAst( Ast* parent )
    : Ast( parent, Ast::ArgumentAst ), argumentExpression( 0 ), keywordName( 0 )
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
    : StatementAst( parent, Ast::IfAst ), ifCondition( 0 )
{
}
WhileAst::WhileAst( Ast* parent )
    : StatementAst( parent, Ast::WhileAst ), condition( 0 )
{
}
ForAst::ForAst( Ast* parent )
    : StatementAst( parent, Ast::ForAst )
{
}
ClassDefinitionAst::ClassDefinitionAst( Ast* parent )
    : StatementAst( parent, Ast::ClassDefinitionAst ), className( 0 )
{
}
TryAst::TryAst( Ast* parent )
    : StatementAst( parent, Ast::TryAst )
{
}
ExceptAst::ExceptAst( Ast* parent )
    : Ast( parent, Ast::ExceptAst ), exceptionDeclaration( 0 ), exceptionValue( 0 )
{
}
WithAst::WithAst( Ast* parent )
    : StatementAst( parent, Ast::WithAst ), context( 0 ), name( 0 )
{
}
ExecAst::ExecAst( Ast* parent )
    : StatementAst( parent, Ast::ExecAst ), executable( 0 ), globalsAndLocals( 0 ), localsOnly( 0 )
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
    : StatementAst( parent, Ast::RaiseAst ), exceptionType( 0 ), exceptionValue( 0 ), traceback( 0 )
{
}
PrintAst::PrintAst( Ast* parent )
    : StatementAst( parent, Ast::PrintAst ), outfile( 0 )
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
    : StatementAst( parent, Ast::AssertAst ), assertTest( 0 ), exceptionValue( 0 )
{
}
ExpressionStatementAst::ExpressionStatementAst( Ast* parent )
    : StatementAst( parent, Ast::ExpressionStatementAst )
{
}
AssignmentAst::AssignmentAst( Ast* parent )
    : StatementAst( parent, Ast::AssignmentAst ), yieldValue( 0 )
{
}
TargetAst::TargetAst( Ast* parent, Ast::AstType type )
    : Ast( parent, type )
{
}
AtomAst::AtomAst( Ast* parent )
    : PrimaryAst( parent, Ast::AtomAst ), identifier( 0 ), literal( 0 ), enclosure( 0 )
{
}
EnclosureAst::EnclosureAst( Ast* parent )
    : Ast( parent, Ast::EnclosureAst ), list( 0 ), generator( 0 ), dict( 0 ), yield( 0 )
{
}
ListAst::ListAst( Ast* parent )
    : Ast( parent, Ast::ListAst ), listGenerator( 0 )
{
}
ListForAst::ListForAst( Ast* parent )
    : Ast( parent, Ast::ListForAst ), nextGenerator( 0 ), nextCondition( 0 )
{
}
ListIfAst::ListIfAst( Ast* parent )
    : Ast( parent, Ast::ListIfAst ), condition( 0 ), nextGenerator( 0 ), nextCondition( 0 )
{
}
GeneratorAst::GeneratorAst( Ast* parent )
    : Ast( parent, Ast::GeneratorAst ), generatedValue( 0 ), generator( 0 )
{
}
GeneratorForAst::GeneratorForAst( Ast* parent )
    : Ast( parent, Ast::GeneratorForAst ), iterableObject( 0 ), 
      nextGenerator( 0 ), nextCondition( 0 )
{
}
GeneratorIfAst::GeneratorIfAst( Ast* parent )
    : Ast( parent, Ast::GeneratorIfAst ), condition( 0 ), nextGenerator( 0 ), nextCondition( 0 )
{
}
DictionaryAst::DictionaryAst( Ast* parent )
    : Ast( parent, Ast::DictionaryAst )
{
}
PrimaryAst::PrimaryAst( Ast* parent, Ast::AstType type )
    : ExpressionAst( parent, type )
{
}
AttributeReferenceAst::AttributeReferenceAst( Ast* parent )
    : PrimaryAst( parent, Ast::AttributeReferenceAst ), primary( 0 ), identifier( 0 )
{
}
SubscriptAst::SubscriptAst( Ast* parent )
    : PrimaryAst( parent, Ast::SubscriptAst ), primary( 0 )
{
}
SliceAst::SliceAst( Ast* parent, Ast::AstType type )
    : PrimaryAst( parent, type ), primary( 0 )
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
    : SliceItemAst( parent, Ast::ProperSliceItemAst ), stride( 0 )
{
}
ExpressionSliceItemAst::ExpressionSliceItemAst( Ast* parent )
    : SliceItemAst( parent, Ast::ExpressionSliceItemAst ), sliceExpression( 0 )
{
}
EllipsisSliceItemAst::EllipsisSliceItemAst( Ast* parent )
    : SliceItemAst( parent, Ast::EllipsisSliceItemAst )
{
}
CallAst::CallAst( Ast* parent )
    : PrimaryAst( parent, Ast::CallAst ), callable( 0 ), generator( 0 )
{
}
ArithmeticExpressionAst::ArithmeticExpressionAst( Ast* parent, Ast::AstType type )
    : ExpressionAst( parent, type )
{
}
UnaryExpressionAst::UnaryExpressionAst( Ast* parent )
    : ArithmeticExpressionAst( parent, Ast::UnaryExpressionAst ), operand( 0 )
{
}
BinaryExpressionAst::BinaryExpressionAst( Ast* parent )
    : ArithmeticExpressionAst( parent, Ast::BinaryExpressionAst ), lhs( 0 ), rhs( 0 )
{
}
ComparisonAst::ComparisonAst( Ast* parent )
    : BooleanOperationAst( parent, Ast::ComparisonAst ), firstComparator( 0 )
{
}
BooleanOperationAst::BooleanOperationAst( Ast* parent, Ast::AstType type )
    : ExpressionAst( parent, type )
{
}
ExpressionAst::ExpressionAst( Ast* parent, Ast::AstType type )
    : Ast( parent, type )
{
}
ConditionalExpressionAst::ConditionalExpressionAst( Ast* parent )
    : ExpressionAst( parent, Ast::ConditionalExpressionAst ), 
      mainExpression( 0 ), condition( 0 ), elseExpression( 0 )
{
}
LambdaAst::LambdaAst( Ast* parent )
    : ExpressionAst( parent, Ast::LambdaAst ), expression( 0 )
{
}

DefaultParameterAst::DefaultParameterAst( Ast * parent )
    : ParameterAst( parent, Ast::DefaultParameterAst ), name( 0 ), value( 0 )
{
}

ParameterPartAst::ParameterPartAst( Ast * parent, Ast::AstType type )
    : Ast( parent, type )
{
}

IdentifierParameterPartAst::IdentifierParameterPartAst( Ast * parent )
    : ParameterPartAst( parent, Ast::IdentifierParameterPartAst ), name( 0 )
{
}

ListParameterPartAst::ListParameterPartAst( Ast * parent )
    : ParameterPartAst( parent, Ast::ListParameterPartAst )
{
}

DictionaryParameterAst::DictionaryParameterAst( Ast * parent )
    : ParameterAst( parent, Ast::DictionaryParameterAst ), name( 0 )
{
}

ListParameterAst::ListParameterAst( Ast * parent )
    : ParameterAst( parent, Ast::ListParameterAst ), name( 0 )
{
}

BooleanNotOperationAst::BooleanNotOperationAst( Ast * parent )
    : BooleanOperationAst( parent, Ast::BooleanNotOperationAst ), op( 0 )
{
}

BooleanOrOperationAst::BooleanOrOperationAst( Ast * parent )
    : BooleanOperationAst( parent, Ast::BooleanOrOperationAst ), lhs( 0 ), rhs( 0 )
{
}

BooleanAndOperationAst::BooleanAndOperationAst( Ast * parent )
    : BooleanOperationAst( parent, Ast::BooleanAndOperationAst ), lhs( 0 ), rhs( 0 )
{
}

IdentifierAst::IdentifierAst( Ast * parent )
    : ExpressionAst( parent, Ast::IdentifierAst )
{
}

LiteralAst::LiteralAst( Ast* parent )
    : Ast( parent, Ast::LiteralAst )
{
}

IdentifierTargetAst::IdentifierTargetAst( Ast * parent )
    : TargetAst( parent, Ast::IdentifierTargetAst ), identifier( 0 )
{
}

TupleTargetAst::TupleTargetAst( Ast * parent )
    : TargetAst( parent, Ast::TupleTargetAst )
{
}

ListTargetAst::ListTargetAst( Ast * parent )
    : TargetAst( parent, Ast::ListTargetAst )
{
}

AttributeReferenceTargetAst::AttributeReferenceTargetAst( Ast * parent )
    : TargetAst( parent, Ast::AttributeReferenceTargetAst ), attribute( 0 )
{
}

SubscriptTargetAst::SubscriptTargetAst( Ast * parent )
    : TargetAst( parent, Ast::SubscriptTargetAst ), subscript( 0 )
{
}

SliceTargetAst::SliceTargetAst( Ast * parent )
    : TargetAst( parent, Ast::SliceTargetAst ), slice( 0 )
{
}


}


#include "pythonast.h"
