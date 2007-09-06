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

#include "simpleastdefaultvisitor.h"

namespace Python
{

void SimpleAstDefaultVisitor::visitStatements( const QList<StatementAst*>& list )
{
    QList<StatementAst*>::const_iterator end = list.end();
    for( QList<StatementAst*>::const_iterator it = list.begin(); it != end; ++it )
    {
        visitStatement(*it);
    }
}

void SimpleAstDefaultVisitor::visitExpression( ExpressionAst* ast )
{
    if( ast )
    {
        switch(ast->m_type)
        {
            case Ast::Lambda:
                visitLambda( static_cast<LambdaAst*>(ast) );
                break;
            case Ast::BinaryOperator:
                visitBinaryOperator( static_cast<BinaryOperatorAst*>(ast) );
                break;
            case Ast::BitWiseOperator:
                visitBitWiseOperator( static_cast<BitWiseOperatorAst*>(ast) );
                break;
            case Ast::Boolean:
                visitBoolean( static_cast<BooleanAst*>(ast) );
                break;
            case Ast::ShiftOperator:
                visitShiftOperator( static_cast<ShiftOperatorAst*>(ast) );
                break;
            case Ast::Comparison:
                visitComparison( static_cast<ComparisonAst*>(ast) );
                break;
            case Ast::UnaryOperator:
                visitUnaryOperator( static_cast<UnaryOperatorAst*>(ast) );
                break;
            case Ast::Power:
                visitPower( static_cast<PowerAst*>(ast) );
                break;
            default:
                break;
        }
    }
}

void SimpleAstDefaultVisitor::visitValue( ValueAst* )
{
}

void SimpleAstDefaultVisitor::visitStatement( StatementAst* ast )
{
    if( ast )
    {
        switch(ast->m_type)
        {
            case Ast::Assert:
                visitAssert( static_cast<AssertAst*>(ast) );
                break;
            case Ast::Assignment:
                visitAssignment( static_cast<AssignmentAst*>(ast) );
                break;
            case Ast::Class:
                visitClass( static_cast<ClassAst*>(ast) );
                break;
            case Ast::Del:
                visitDelKeyword( static_cast<DelKeywordAst*>(ast) );
                break;
            case Ast::ElseIf:
                visitElseIf( static_cast<ElseIfAst*>(ast) );
                break;
            case Ast::Exec:
                visitExecKeyword( static_cast<ExecKeywordAst*>(ast) );
                break;
            case Ast::For:
                visitFor( static_cast<ForAst*>(ast) );
                break;
            case Ast::Function:
                visitFunction( static_cast<FunctionAst*>(ast) );
                break;
            case Ast::Global:
                visitGlobalKeyword( static_cast<GlobalKeywordAst*>(ast) );
                break;
            case Ast::If:
                visitIf( static_cast<IfAst*>(ast) );
                break;
            case Ast::Import:
                visitImportKeyword( static_cast<ImportKeywordAst*>(ast) );
                break;
            case Ast::Print:
                visitPrintKeyword( static_cast<PrintKeywordAst*>(ast) );
                break;
            case Ast::Raise:
                visitRaiseKeyword( static_cast<RaiseKeywordAst*>(ast) );
                break;
            case Ast::Return:
                visitReturnKeyword( static_cast<ReturnKeywordAst*>(ast) );
                break;
            case Ast::Try:
                visitTry( static_cast<TryAst*>(ast) );
                break;
            case Ast::While:
                visitWhile( static_cast<WhileAst*>(ast) );
                break;
            case Ast::Yield:
                visitYieldKeyword( static_cast<YieldKeywordAst*>(ast) );
                break;
            default:
                break;
        }
    }
}

void SimpleAstDefaultVisitor::visitElseIf( ElseIfAst* ast )
{
    if( ast )
    {
        visitExpression( ast->m_expression );
        visitStatements( ast->m_statements );
    }
}

void SimpleAstDefaultVisitor::visitIf( IfAst* ast )
{
    if( ast )
    {
        visitExpression( ast->m_ifExpression );
        visitStatements( ast->m_ifStatements );
        foreach( ElseIfAst* elif, ast->m_elseIfList )
        {
            visitElseIf( elif );
        }
        visitStatements( ast->m_elseStatements );
    }
}

void SimpleAstDefaultVisitor::visitWhile( WhileAst* ast )
{
    if( ast )
    {
        visitExpression( ast->m_whileExpression );
        visitStatements( ast->m_whileStatements );
        visitStatements( ast->m_elseStatements );
    }
}

void SimpleAstDefaultVisitor::visitFor( ForAst* ast )
{
    if( ast )
    {
        foreach( TargetAst* target, ast->m_forTargets )
        {
            visitTarget( target );
        }
        foreach( ExpressionAst* exp, ast->m_forExpressions )
        {
            visitExpression( exp );
        }
        visitStatements( ast->m_forStatements );
        visitStatements( ast->m_elseStatements );
    }
}

void SimpleAstDefaultVisitor::visitExcept( ExceptAst* ast )
{
    if( ast )
    {
        visitExpression( ast->m_exception );
        visitTarget( ast->m_target );
        visitStatements( ast->m_statements );
    }
}

void SimpleAstDefaultVisitor::visitTry( TryAst* ast )
{
    if( ast )
    {
        visitStatements( ast->m_tryStatements );
        if( !ast->m_finallyStatements.isEmpty() )
        {
            visitStatements( ast->m_finallyStatements );
        }else
        {
            foreach( ExceptAst* exception, ast->m_exceptions )
            {
                visitExcept( exception );
            }
            visitStatements( ast->m_elseStatements );
        }
    }
}

void SimpleAstDefaultVisitor::visitClass( ClassAst* ast )
{
    if( ast )
    {
        visitIdentifier( ast->m_identifier );
        foreach( ExpressionAst* exp, ast->m_inheritance )
        {
            visitExpression( exp );
        }
        visitStatements( ast->m_statements );
    }
}

void SimpleAstDefaultVisitor::visitDecorator( DecoratorAst* ast )
{
    if( ast )
    {
        foreach( IdentifierAst* id,  ast->m_name )
        {
            visitIdentifier( id );
        }
        foreach( ArgumentAst* arg, ast->m_arguments )
        {
            visitArgument( arg );
        }
    }
}

void SimpleAstDefaultVisitor::visitParameter( ParameterAst* ast )
{
    if( ast )
    {
        switch( ast->m_parameterType )
        {
            case ParameterAst::DefaultParameter:
                if( ast->m_identifier )
                {
                    visitIdentifier( ast->m_identifier );
                }else
                {
                    foreach( ParameterAst* p, ast->m_sublist )
                    {
                        visitParameter( p );
                    }
                }
                visitExpression( ast->m_expression );
                break;
            case ParameterAst::PositionalParameter:
                if( ast->m_identifier )
                {
                    visitIdentifier( ast->m_identifier );
                }else
                {
                    foreach( ParameterAst* p, ast->m_sublist )
                    {
                        visitParameter( p );
                    }
                }
                break;
            case ParameterAst::KeywordParameter:
                visitIdentifier( ast->m_identifier );
                break;
        }
    }
}

void SimpleAstDefaultVisitor::visitFunction( FunctionAst* ast )
{
    if( ast )
    {
        foreach( DecoratorAst* dec, ast->m_decorators )
        {
            visitDecorator( dec );
        }
        visitIdentifier( ast->m_identifier );
        foreach( ParameterAst* p, ast->m_parameters )
        {
            visitParameter( p );
        }
        visitStatements( ast->m_statements );
    }
}

void SimpleAstDefaultVisitor::visitAssignment( AssignmentAst* ast )
{
    if( ast )
    {
    }
}

void SimpleAstDefaultVisitor::visitAssert( AssertAst* ast )
{
    if( ast )
    {
    }
}

void SimpleAstDefaultVisitor::visitTarget( TargetAst* ast )
{
    if( ast )
    {
    }
}

void SimpleAstDefaultVisitor::visitDelKeyword( DelKeywordAst* ast )
{
    if( ast )
    {
    }
}

void SimpleAstDefaultVisitor::visitPrintKeyword( PrintKeywordAst* ast )
{
    if( ast )
    {
    }
}

void SimpleAstDefaultVisitor::visitReturnKeyword( ReturnKeywordAst* ast )
{
    if( ast )
    {
    }
}

void SimpleAstDefaultVisitor::visitYieldKeyword( YieldKeywordAst* ast )
{
    if( ast )
    {
    }
}

void SimpleAstDefaultVisitor::visitRaiseKeyword( RaiseKeywordAst* ast )
{
    if( ast )
    {
    }
}

void SimpleAstDefaultVisitor::visitImport( ImportAst* ast )
{
    if( ast )
    {
    }
}

void SimpleAstDefaultVisitor::visitImportKeyword( ImportKeywordAst* ast )
{
    if( ast )
    {
    }
}

void SimpleAstDefaultVisitor::visitExecKeyword( ExecKeywordAst* ast )
{
    if( ast )
    {
    }
}

void SimpleAstDefaultVisitor::visitPrimary( PrimaryAst* ast )
{
    if( ast )
    {
    }
}

void SimpleAstDefaultVisitor::visitGlobalKeyword( GlobalKeywordAst* ast )
{
    if( ast )
    {
    }
}

void SimpleAstDefaultVisitor::visitAtom( AtomAst* ast )
{
    if( ast )
    {
    }
}

void SimpleAstDefaultVisitor::visitLiteral( LiteralAst* ast )
{
    if( ast )
    {
    }
}

void SimpleAstDefaultVisitor::visitParenthesizedExpressionList( ParenthesizedExpressionListAst* ast )
{
    if( ast )
    {
    }
}

void SimpleAstDefaultVisitor::visitList( ListAst* ast )
{
    if( ast )
    {
    }
}

void SimpleAstDefaultVisitor::visitGenerator( GeneratorAst* ast )
{
    if( ast )
    {
    }
}

void SimpleAstDefaultVisitor::visitStringConversion( StringConversionAst* ast )
{
    if( ast )
    {
    }
}

void SimpleAstDefaultVisitor::visitAttributeReference( AttributeReferenceAst* ast )
{
    if( ast )
    {
    }
}

void SimpleAstDefaultVisitor::visitDictionary( DictionaryAst* ast )
{
    if( ast )
    {
    }
}

void SimpleAstDefaultVisitor::visitSubscription( SubscriptionAst* ast )
{
    if( ast )
    {
    }
}

void SimpleAstDefaultVisitor::visitLambda( LambdaAst* ast )
{
    if( ast )
    {
    }
}

void SimpleAstDefaultVisitor::visitArgument( ArgumentAst* ast )
{
    if( ast )
    {
    }
}

void SimpleAstDefaultVisitor::visitCall( CallAst* ast )
{
    if( ast )
    {
    }
}

void SimpleAstDefaultVisitor::visitUnaryOperator( UnaryOperatorAst* ast )
{
    if( ast )
    {
    }
}

void SimpleAstDefaultVisitor::visitPower( PowerAst* ast )
{
    if( ast )
    {
    }
}

void SimpleAstDefaultVisitor::visitBinaryOperator( BinaryOperatorAst* ast )
{
    if( ast )
    {
    }
}

void SimpleAstDefaultVisitor::visitShiftOperator( ShiftOperatorAst* ast )
{
    if( ast )
    {
    }
}

void SimpleAstDefaultVisitor::visitBitWiseOperator( BitWiseOperatorAst* ast )
{
    if( ast )
    {
    }
}

void SimpleAstDefaultVisitor::visitComparison( ComparisonAst* ast )
{
    if( ast )
    {
    }
}

void SimpleAstDefaultVisitor::visitBoolean( BooleanAst* ast )
{
    if( ast )
    {
    }
}

void SimpleAstDefaultVisitor::visitSlice( SliceAst* ast )
{
    if( ast )
    {
    }
}

void SimpleAstDefaultVisitor::visitSliceItem( SliceItemAst* ast )
{
    if( ast )
    {
    }
}

void SimpleAstDefaultVisitor::visitIdentifier( IdentifierAst* ast )
{
    if( ast )
    {
    }
}

}

//kate: space-indent on; indent-width 4; replace-tabs on; auto-insert-doxygen on; indent-mode cstyle;
