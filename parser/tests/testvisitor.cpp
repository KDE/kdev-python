/***************************************************************************
 *   This file is part of KDevelop                                         *
 *   Copyright 2008 Andreas Pakulat <apaku@gmx.de>                         *
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

#include "testvisitor.h"

#include <QtTest/QtTest>

#define BASIC_AST_TEST( result, expected ) \
    QCOMPARE( result->start, expected->start ); \
    QCOMPARE( result->startCol, expected->startCol ); \
    QCOMPARE( result->startLine, expected->startLine ); \
    QEXPECT_FAIL("", "This will fail for code ast", Continue); \
    QCOMPARE( result->end, expected->end ); \
    QEXPECT_FAIL("", "This will fail for code ast", Continue); \
    QCOMPARE( result->endCol, expected->endCol ); \
    QEXPECT_FAIL("", "This will fail for code ast", Continue); \
    QCOMPARE( result->endLine, expected->endLine ); \
    QCOMPARE( result->astType, expected->astType )

using namespace Python;



TestVisitor::TestVisitor()
{
}

TestVisitor::~TestVisitor()
{
}

void TestVisitor::setExpected( CodeAst* ast )
{
    expectedStack.push( ast );
}

void TestVisitor::visitCode( CodeAst* ast )
{
    CodeAst* expectedast = pop<CodeAst>();
    BASIC_AST_TEST( ast, expectedast );
    QCOMPARE( ast->statements.count(), expectedast->statements.count() );
    checkList( ast->statements, expectedast->statements );
    Q_ASSERT( expectedStack.isEmpty() );
}

void TestVisitor::visitFunctionDefinition( FunctionDefinitionAst* ast )
{
    FunctionDefinitionAst* expectedast = pop<FunctionDefinitionAst>();
    BASIC_AST_TEST( ast, expectedast );
    QCOMPARE( ast->decorators.count(), expectedast->decorators.count() );
    QCOMPARE( ast->functionBody.count(), expectedast->functionBody.count() );
    QCOMPARE( ast->parameters.count(), expectedast->parameters.count() );
    
    checkList( ast->decorators, expectedast->decorators );
    expectedStack.push( expectedast->functionName );
    visitNode( ast->functionName );
    checkList( ast->parameters, expectedast->parameters );
    checkList( ast->functionBody, expectedast->functionBody );
}

void TestVisitor::visitDecorator( DecoratorAst* ast )
{
    DecoratorAst* expectedast = pop<DecoratorAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkList( ast->dottedName, expectedast->dottedName );
    checkList( ast->arguments, expectedast->arguments );
}

void TestVisitor::visitArgument( ArgumentAst* ast )
{
    ArgumentAst* expectedast = pop<ArgumentAst>();
    BASIC_AST_TEST( ast, expectedast );
    QCOMPARE( ast->argumentType, expectedast->argumentType );
    if( ast->argumentType == ArgumentAst::KeywordArgument )
    {
        expectedStack.push( expectedast->keywordName );
        visitNode( ast->keywordName );
    }
    
    expectedStack.push( expectedast->argumentExpression );
    visitNode( ast->argumentExpression );
}

void TestVisitor::visitDefaultParameter( DefaultParameterAst* ast )
{
    DefaultParameterAst* expectedast = pop<DefaultParameterAst>();
    BASIC_AST_TEST( ast, expectedast );
    expectedStack.push( expectedast->name );
    visitNode( ast->name );
    expectedStack.push( expectedast->value );
    visitNode( ast->value );
}

void TestVisitor::visitIdentifierParameterPart( IdentifierParameterPartAst* )
{
}

void TestVisitor::visitListParameterPart( ListParameterPartAst* )
{
}

void TestVisitor::visitDictionaryParameter( DictionaryParameterAst* )
{
}

void TestVisitor::visitListParameter( ListParameterAst* )
{
}

void TestVisitor::visitIf( IfAst* )
{
}

void TestVisitor::visitWhile( WhileAst* )
{
}

void TestVisitor::visitFor( ForAst* )
{
}

void TestVisitor::visitClassDefinition( ClassDefinitionAst* )
{
}

void TestVisitor::visitTry( TryAst* )
{
}

void TestVisitor::visitExcept( ExceptAst* )
{
}

void TestVisitor::visitWith( WithAst* )
{
}

void TestVisitor::visitExec( ExecAst* )
{
}

void TestVisitor::visitGlobal( GlobalAst* )
{
}

void TestVisitor::visitPlainImport( PlainImportAst* )
{
}

void TestVisitor::visitStarImport( StarImportAst* )
{
}

void TestVisitor::visitFromImport( FromImportAst* )
{
}

void TestVisitor::visitRaise( RaiseAst* )
{
}

void TestVisitor::visitPrint( PrintAst* )
{
}

void TestVisitor::visitReturn( ReturnAst* )
{
}

void TestVisitor::visitYield( YieldAst* )
{
}

void TestVisitor::visitDel( DelAst* )
{
}

void TestVisitor::visitAssert( AssertAst* )
{
}

void TestVisitor::visitExpressionStatement( ExpressionStatementAst* )
{
}

void TestVisitor::visitAssignment( AssignmentAst* )
{
}

void TestVisitor::visitAtom( AtomAst* )
{
}

void TestVisitor::visitEnclosure( EnclosureAst* )
{
}

void TestVisitor::visitList( ListAst* )
{
}

void TestVisitor::visitListFor( ListForAst* )
{
}

void TestVisitor::visitListIf( ListIfAst* )
{
}

void TestVisitor::visitLiteral( LiteralAst* )
{
}

void TestVisitor::visitGenerator( GeneratorAst* )
{
}

void TestVisitor::visitGeneratorFor( GeneratorForAst* )
{
}

void TestVisitor::visitGeneratorIf( GeneratorIfAst* )
{
}

void TestVisitor::visitDictionary( DictionaryAst* )
{
}

void TestVisitor::visitAttributeReference( AttributeReferenceAst* )
{
}

void TestVisitor::visitSubscript( SubscriptAst* )
{
}

void TestVisitor::visitExtendedSlice( ExtendedSliceAst* )
{
}

void TestVisitor::visitSimpleSlice( SimpleSliceAst* )
{
}

void TestVisitor::visitProperSliceItem( ProperSliceItemAst* )
{
}

void TestVisitor::visitExpressionSliceItem( ExpressionSliceItemAst* )
{
}

void TestVisitor::visitEllipsisSliceItem( EllipsisSliceItemAst* )
{
}

void TestVisitor::visitCall( CallAst* )
{
}

void TestVisitor::visitUnaryExpression( UnaryExpressionAst* )
{
}

void TestVisitor::visitBinaryExpression( BinaryExpressionAst* )
{
}

void TestVisitor::visitComparison( ComparisonAst* )
{
}

void TestVisitor::visitBooleanNotOperation( BooleanNotOperationAst* )
{
}

void TestVisitor::visitBooleanAndOperation( BooleanAndOperationAst* )
{
}

void TestVisitor::visitBooleanOrOperation( BooleanOrOperationAst* )
{
}

void TestVisitor::visitConditionalExpression( ConditionalExpressionAst* )
{
}

void TestVisitor::visitLambda( LambdaAst* )
{
}

void TestVisitor::visitBreak( StatementAst* )
{
}

void TestVisitor::visitContinue( StatementAst* )
{
}

void TestVisitor::visitPass( StatementAst* )
{
}

void TestVisitor::visitIdentifier( IdentifierAst* )
{
}

void TestVisitor::visitIdentifierTarget( IdentifierTargetAst* )
{
}

void TestVisitor::visitListTarget( ListTargetAst* )
{
}

void TestVisitor::visitTupleTarget( TupleTargetAst* )
{
}

void TestVisitor::visitAttributeReferenceTarget( AttributeReferenceTargetAst* )
{
}

void TestVisitor::visitSubscriptTarget( SubscriptTargetAst* )
{
}

void TestVisitor::visitSliceTarget( SliceTargetAst* )
{
}

