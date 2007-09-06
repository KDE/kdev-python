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

#ifndef SIMPLEASTDEFAULTVISITOR_H
#define SIMPLEASTDEFAULTVISITOR_H

#include "pythonast.h"
#include "simpleastvisitor.h"

namespace Python
{

class SimpleAstDefaultVisitor : public SimpleAstVisitor
{
public:
    virtual void visitStatements( const QList<StatementAst*>& );
    virtual void visitExpression( ExpressionAst* );
    virtual void visitValue( ValueAst* );
    virtual void visitStatement( StatementAst* );
    virtual void visitElseIf( ElseIfAst* );
    virtual void visitIf( IfAst* );
    virtual void visitWhile( WhileAst* );
    virtual void visitFor( ForAst* );
    virtual void visitExcept( ExceptAst* );
    virtual void visitTry( TryAst* );
    virtual void visitClass( ClassAst* );
    virtual void visitDecorator( DecoratorAst* );
    virtual void visitParameter( ParameterAst* );
    virtual void visitFunction( FunctionAst* );
    virtual void visitAssignment( AssignmentAst* );
    virtual void visitAssert( AssertAst* );
    virtual void visitTarget( TargetAst* );
    virtual void visitDelKeyword( DelKeywordAst* );
    virtual void visitPrintKeyword( PrintKeywordAst* );
    virtual void visitReturnKeyword( ReturnKeywordAst* );
    virtual void visitYieldKeyword( YieldKeywordAst* );
    virtual void visitRaiseKeyword( RaiseKeywordAst* );
    virtual void visitImport( ImportAst* );
    virtual void visitImportKeyword( ImportKeywordAst* );
    virtual void visitExecKeyword( ExecKeywordAst* );
    virtual void visitPrimary( PrimaryAst* );
    virtual void visitGlobalKeyword( GlobalKeywordAst* );
    virtual void visitAtom( AtomAst* );
    virtual void visitLiteral( LiteralAst* );
    virtual void visitParenthesizedExpressionList( ParenthesizedExpressionListAst* );
    virtual void visitList( ListAst* );
    virtual void visitGenerator( GeneratorAst* );
    virtual void visitStringConversion( StringConversionAst* );
    virtual void visitAttributeReference( AttributeReferenceAst* );
    virtual void visitDictionary( DictionaryAst* );
    virtual void visitSubscription( SubscriptionAst* );
    virtual void visitLambda( LambdaAst* );
    virtual void visitArgument( ArgumentAst* );
    virtual void visitCall( CallAst* );
    virtual void visitUnaryOperator( UnaryOperatorAst* );
    virtual void visitPower( PowerAst* );
    virtual void visitBinaryOperator( BinaryOperatorAst* );
    virtual void visitShiftOperator( ShiftOperatorAst* );
    virtual void visitBitWiseOperator( BitWiseOperatorAst* );
    virtual void visitComparison( ComparisonAst* );
    virtual void visitBoolean( BooleanAst* );
    virtual void visitSlice( SliceAst* );
    virtual void visitSliceItem( SliceItemAst* );
    virtual void visitIdentifier( IdentifierAst* );
};

}


#endif

//kate: space-indent on; indent-width 4; replace-tabs on; auto-insert-doxygen on; indent-mode cstyle;
