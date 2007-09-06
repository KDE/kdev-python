/***************************************************************************
 *   This file is part of KDevelop                                         *
 *   Copyright (C) 2007 Andreas Pakulat <apaku@gmx.de>                     *
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

#ifndef SIMPLEASTVISITOR_H
#define SIMPLEASTVISITOR_H

#include "pythonast.h"

namespace Python
{

class SimpleAstVisitor
{
public:
    virtual void visitStatements( const QList<StatementAst*>& )= 0;
    virtual void visitExpression( ExpressionAst* )= 0;
    virtual void visitValue( ValueAst* )= 0;
    virtual void visitStatement( StatementAst* )= 0;
    virtual void visitElseIf( ElseIfAst* )= 0;
    virtual void visitIf( IfAst* )= 0;
    virtual void visitWhile( WhileAst* )= 0;
    virtual void visitFor( ForAst* )= 0;
    virtual void visitExcept( ExceptAst* )= 0;
    virtual void visitTry( TryAst* )= 0;
    virtual void visitClass( ClassAst* )= 0;
    virtual void visitDecorator( DecoratorAst* )= 0;
    virtual void visitParameter( ParameterAst* )= 0;
    virtual void visitFunction( FunctionAst* )= 0;
    virtual void visitAssignment( AssignmentAst* )= 0;
    virtual void visitAssert( AssertAst* )= 0;
    virtual void visitTarget( TargetAst* )= 0;
    virtual void visitDelKeyword( DelKeywordAst* )= 0;
    virtual void visitPrintKeyword( PrintKeywordAst* )= 0;
    virtual void visitReturnKeyword( ReturnKeywordAst* )= 0;
    virtual void visitYieldKeyword( YieldKeywordAst* )= 0;
    virtual void visitRaiseKeyword( RaiseKeywordAst* )= 0;
    virtual void visitImport( ImportAst* )= 0;
    virtual void visitImportKeyword( ImportKeywordAst* )= 0;
    virtual void visitExecKeyword( ExecKeywordAst* )= 0;
    virtual void visitPrimary( PrimaryAst* )= 0;
    virtual void visitGlobalKeyword( GlobalKeywordAst* )= 0;
    virtual void visitAtom( AtomAst* )= 0;
    virtual void visitLiteral( LiteralAst* )= 0;
    virtual void visitParenthesizedExpressionList( ParenthesizedExpressionListAst* )= 0;
    virtual void visitList( ListAst* )= 0;
    virtual void visitGenerator( GeneratorAst* )= 0;
    virtual void visitStringConversion( StringConversionAst* )= 0;
    virtual void visitAttributeReference( AttributeReferenceAst* )= 0;
    virtual void visitDictionary( DictionaryAst* )= 0;
    virtual void visitSubscription( SubscriptionAst* )= 0;
    virtual void visitLambda( LambdaAst* )= 0;
    virtual void visitArgument( ArgumentAst* )= 0;
    virtual void visitCall( CallAst* )= 0;
    virtual void visitUnaryOperator( UnaryOperatorAst* )= 0;
    virtual void visitPower( PowerAst* )= 0;
    virtual void visitBinaryOperator( BinaryOperatorAst* )= 0;
    virtual void visitShiftOperator( ShiftOperatorAst* )= 0;
    virtual void visitBitWiseOperator( BitWiseOperatorAst* )= 0;
    virtual void visitComparison( ComparisonAst* )= 0;
    virtual void visitBoolean( BooleanAst* )= 0;
    virtual void visitSlice( SliceAst* )= 0;
    virtual void visitSliceItem( SliceItemAst* )= 0;
    virtual void visitIdentifier( IdentifierAst* )= 0;
};

}

#endif

//kate: space-indent on; indent-width 4; replace-tabs on; auto-insert-doxygen on; indent-mode cstyle;
