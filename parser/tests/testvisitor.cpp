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
    QCOMPARE( result->astType, expected->astType );

using namespace Python;

TestVisitor::TestVisitor()
{
}

TestVisitor::~TestVisitor()
{
}

void TestVisitor::setExpected( Python::CodeAst* ast )
{
    expectedStack.push( ast );
}

void TestVisitor::visitCode( Python::CodeAst* ast )
{
    Python::CodeAst* expectedast = pop<Python::CodeAst>();
    BASIC_AST_TEST( ast, expectedast )
    QCOMPARE( ast->statements.count(), expectedast->statements.count() );
    QList<StatementAst*>::const_iterator it, end = ast->statements.end();
    QList<StatementAst*>::const_iterator expectedit, expectedend = expectedast->statements.end();
    for( it = ast->statements.begin(), expectedit = expectedast->statements.begin(); it != end, expectedit != expectedend ; it++, expectedit++ )
    {
        expectedStack.push( *expectedit );
        visitNode( *it );
    }
}

void TestVisitor::visitFunctionDefinition( Python::FunctionDefinitionAst* ast )
{
    Python::FunctionDefinitionAst* expectedast = pop<Python::FunctionDefinitionAst>();
    BASIC_AST_TEST( ast, expectedast )
    QCOMPARE( ast->decorators.count(), expectedast->decorators.count() );
    QCOMPARE( ast->functionBody.count(), expectedast->functionBody.count() );
    QCOMPARE( ast->parameters.count(), expectedast->parameters.count() );
    
    {
        QList<DecoratorAst*>::const_iterator it, end = ast->decorators.end();
        QList<DecoratorAst*>::const_iterator expectedit, expectedend = expectedast->decorators.end();
        for( it = ast->decorators.begin(), expectedit = expectedast->decorators.begin();
             it != end, expectedit != end; it++, expectedit++ )
        {
            expectedStack.push( *expectedit );
            visitNode( *it );
        }
    }
    expectedStack.push( expectedast->functionName );
    visitNode( ast->functionName );
    {
        QList<ParameterAst*>::const_iterator it, end = ast->parameters.end();
        QList<ParameterAst*>::const_iterator expectedit, expectedend = expectedast->parameters.end();
        for( it = ast->parameters.begin(), expectedit = expectedast->parameters.begin();
             it != end, expectedit != end; it++, expectedit++ )
        {
            expectedStack.push( *expectedit );
            visitNode( *it );
        }
    }
    {
        QList<StatementAst*>::const_iterator it, end = ast->functionBody.end();
        QList<StatementAst*>::const_iterator expectedit, expectedend = expectedast->functionBody.end();
        for( it = ast->functionBody.begin(), expectedit = expectedast->functionBody.begin();
             it != end, expectedit != end; it++, expectedit++ )
        {
            expectedStack.push( *expectedit );
            visitNode( *it );
        }
    }
}

void TestVisitor::visitDecorator( Python::DecoratorAst* )
{
}

void TestVisitor::visitArgument( Python::ArgumentAst* )
{
}

void TestVisitor::visitDefaultParameter( Python::DefaultParameterAst* )
{
}

void TestVisitor::visitIdentifierParameterPart( Python::IdentifierParameterPartAst* )
{
}

void TestVisitor::visitListParameterPart( Python::ListParameterPartAst* )
{
}

void TestVisitor::visitDictionaryParameter( Python::DictionaryParameterAst* )
{
}

void TestVisitor::visitListParameter( Python::ListParameterAst* )
{
}

void TestVisitor::visitIf( Python::IfAst* )
{
}

void TestVisitor::visitWhile( Python::WhileAst* )
{
}

void TestVisitor::visitFor( Python::ForAst* )
{
}

void TestVisitor::visitClassDefinition( Python::ClassDefinitionAst* )
{
}

void TestVisitor::visitTry( Python::TryAst* )
{
}

void TestVisitor::visitExcept( Python::ExceptAst* )
{
}

void TestVisitor::visitWith( Python::WithAst* )
{
}

void TestVisitor::visitExec( Python::ExecAst* )
{
}

void TestVisitor::visitGlobal( Python::GlobalAst* )
{
}

void TestVisitor::visitPlainImport( Python::PlainImportAst* )
{
}

void TestVisitor::visitStarImport( Python::StarImportAst* )
{
}

void TestVisitor::visitFromImport( Python::FromImportAst* )
{
}

void TestVisitor::visitRaise( Python::RaiseAst* )
{
}

void TestVisitor::visitPrint( Python::PrintAst* )
{
}

void TestVisitor::visitReturn( Python::ReturnAst* )
{
}

void TestVisitor::visitYield( Python::YieldAst* )
{
}

void TestVisitor::visitDel( Python::DelAst* )
{
}

void TestVisitor::visitAssert( Python::AssertAst* )
{
}

void TestVisitor::visitExpressionStatement( Python::ExpressionStatementAst* )
{
}

void TestVisitor::visitAssignment( Python::AssignmentAst* )
{
}

void TestVisitor::visitAtom( Python::AtomAst* )
{
}

void TestVisitor::visitEnclosure( Python::EnclosureAst* )
{
}

void TestVisitor::visitList( Python::ListAst* )
{
}

void TestVisitor::visitListFor( Python::ListForAst* )
{
}

void TestVisitor::visitListIf( Python::ListIfAst* )
{
}

void TestVisitor::visitLiteral( Python::LiteralAst* )
{
}

void TestVisitor::visitGenerator( Python::GeneratorAst* )
{
}

void TestVisitor::visitGeneratorFor( Python::GeneratorForAst* )
{
}

void TestVisitor::visitGeneratorIf( Python::GeneratorIfAst* )
{
}

void TestVisitor::visitDictionary( Python::DictionaryAst* )
{
}

void TestVisitor::visitAttributeReference( Python::AttributeReferenceAst* )
{
}

void TestVisitor::visitSubscript( Python::SubscriptAst* )
{
}

void TestVisitor::visitExtendedSlice( Python::ExtendedSliceAst* )
{
}

void TestVisitor::visitSimpleSlice( Python::SimpleSliceAst* )
{
}

void TestVisitor::visitProperSliceItem( Python::ProperSliceItemAst* )
{
}

void TestVisitor::visitExpressionSliceItem( Python::ExpressionSliceItemAst* )
{
}

void TestVisitor::visitEllipsisSliceItem( Python::EllipsisSliceItemAst* )
{
}

void TestVisitor::visitCall( Python::CallAst* )
{
}

void TestVisitor::visitUnaryExpression( Python::UnaryExpressionAst* )
{
}

void TestVisitor::visitBinaryExpression( Python::BinaryExpressionAst* )
{
}

void TestVisitor::visitComparison( Python::ComparisonAst* )
{
}

void TestVisitor::visitBooleanNotOperation( Python::BooleanNotOperationAst* )
{
}

void TestVisitor::visitBooleanAndOperation( Python::BooleanAndOperationAst* )
{
}

void TestVisitor::visitBooleanOrOperation( Python::BooleanOrOperationAst* )
{
}

void TestVisitor::visitConditionalExpression( Python::ConditionalExpressionAst* )
{
}

void TestVisitor::visitLambda( Python::LambdaAst* )
{
}

void TestVisitor::visitBreak( Python::StatementAst* )
{
}

void TestVisitor::visitContinue( Python::StatementAst* )
{
}

void TestVisitor::visitPass( Python::StatementAst* )
{
}

void TestVisitor::visitIdentifier( Python::IdentifierAst* )
{
}

void TestVisitor::visitIdentifierTarget( Python::IdentifierTargetAst* )
{
}

void TestVisitor::visitListTarget( Python::ListTargetAst* )
{
}

void TestVisitor::visitTupleTarget( Python::TupleTargetAst* )
{
}

void TestVisitor::visitAttributeReferenceTarget( Python::AttributeReferenceTargetAst* )
{
}

void TestVisitor::visitSubscriptTarget( Python::SubscriptTargetAst* )
{
}

void TestVisitor::visitSliceTarget( Python::SliceTargetAst* )
{
}

