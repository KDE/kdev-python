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
    checkNode( ast->functionName, expectedast->functionName );
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
        checkNode( ast->keywordName, expectedast->keywordName );
    }
    
    checkNode( ast->argumentExpression, expectedast->argumentExpression );
}

void TestVisitor::visitDefaultParameter( DefaultParameterAst* ast )
{
    DefaultParameterAst* expectedast = pop<DefaultParameterAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkNode( ast->name, expectedast->name );
    checkNode( ast->value, expectedast->value );
}

void TestVisitor::visitIdentifierParameterPart( IdentifierParameterPartAst* ast )
{
    IdentifierParameterPartAst* expectedast = pop<IdentifierParameterPartAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkNode( ast->name, expectedast->name );
}

void TestVisitor::visitListParameterPart( ListParameterPartAst* ast )
{
    ListParameterPartAst* expectedast = pop<ListParameterPartAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkList( ast->parameternames, expectedast->parameternames );
}

void TestVisitor::visitDictionaryParameter( DictionaryParameterAst* ast )
{
    DictionaryParameterAst* expectedast = pop<DictionaryParameterAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkNode( ast->name, expectedast->name );
}

void TestVisitor::visitListParameter( ListParameterAst* ast )
{
    ListParameterAst* expectedast = pop<ListParameterAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkNode( ast->name, expectedast->name );
}

void TestVisitor::visitIf( IfAst* ast )
{
    IfAst* expectedast = pop<IfAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkNode( ast->ifCondition, expectedast->ifCondition );
    checkList( ast->ifBody, expectedast->ifBody );
    checkPairList( ast->elseIfBodies, expectedast->elseIfBodies );
    checkList( ast->elseBody, expectedast->elseBody );
}

void TestVisitor::visitWhile( WhileAst* ast )
{
    WhileAst* expectedast = pop<WhileAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkNode( ast->condition, expectedast->condition );
    checkList( ast->whileBody, expectedast->whileBody );
    checkList( ast->elseBody, expectedast->elseBody );
}

void TestVisitor::visitFor( ForAst* ast )
{
    ForAst* expectedast = pop<ForAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkList( ast->assignedTargets, expectedast->assignedTargets );
    checkList( ast->iterable, expectedast->iterable );
    checkList( ast->forBody, expectedast->forBody );
    checkList( ast->elseBody, expectedast->elseBody );
}

void TestVisitor::visitClassDefinition( ClassDefinitionAst* ast )
{
    ClassDefinitionAst* expectedast = pop<ClassDefinitionAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkNode( ast->className, expectedast->className );
    checkList( ast->inheritance, expectedast->inheritance );
    checkList( ast->classBody, expectedast->classBody );
}

void TestVisitor::visitTry( TryAst* ast )
{
    TryAst* expectedast = pop<TryAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkList( ast->tryBody, expectedast->tryBody );
    checkList( ast->exceptions, expectedast->exceptions );
    checkList( ast->elseBody, expectedast->elseBody );
    checkList( ast->finallyBody, expectedast->finallyBody );
}

void TestVisitor::visitExcept( ExceptAst* ast )
{
    ExceptAst* expectedast = pop<ExceptAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkOptional( ast->exceptionDeclaration, expectedast->exceptionDeclaration );
    checkOptional( ast->exceptionValue, expectedast->exceptionValue );
    checkList( ast->exceptionBody, expectedast->exceptionBody );
}

void TestVisitor::visitWith( WithAst* ast )
{
    WithAst* expectedast = pop<WithAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkNode( ast->context, expectedast->context );
    checkOptional( ast->name, expectedast->name );
    checkList( ast->body, expectedast->body );
}

void TestVisitor::visitExec( ExecAst* ast )
{
    ExecAst* expectedast = pop<ExecAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkNode( ast->executable, expectedast->executable );
    checkOptional( ast->globalsAndLocals, expectedast->globalsAndLocals );
    checkOptional( ast->localsOnly, expectedast->localsOnly );
}

void TestVisitor::visitGlobal( GlobalAst* ast )
{
    GlobalAst* expectedast = pop<GlobalAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkList( ast->identifiers, expectedast->identifiers );
}

void TestVisitor::visitPlainImport( PlainImportAst* ast )
{
    PlainImportAst* expectedast = pop<PlainImportAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkPairList( ast->modulesAsName, expectedast->modulesAsName );
}

void TestVisitor::visitStarImport( StarImportAst* ast )
{
    StarImportAst* expectedast = pop<StarImportAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkList( ast->modulePath, expectedast->modulePath );
}

void TestVisitor::visitFromImport( FromImportAst* ast )
{
    FromImportAst* expectedast = pop<FromImportAst>();
    BASIC_AST_TEST( ast, expectedast );
    QCOMPARE( ast->numLeadingDots, expectedast->numLeadingDots );
    checkList( ast->modulePath, expectedast->modulePath );
    checkPairList( ast->identifierAsName, expectedast->identifierAsName );
}

void TestVisitor::visitRaise( RaiseAst* ast )
{
    RaiseAst* expectedast = pop<RaiseAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkOptional( ast->exceptionType, expectedast->exceptionType );
    checkOptional( ast->exceptionValue, expectedast->exceptionValue );
    checkOptional( ast->traceback, expectedast->traceback );
}

void TestVisitor::visitPrint( PrintAst* ast )
{
    PrintAst* expectedast = pop<PrintAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkOptional( ast->outfile, expectedast->outfile );
    checkList( ast->printables, expectedast->printables );
}

void TestVisitor::visitReturn( ReturnAst* ast )
{
    ReturnAst* expectedast = pop<ReturnAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkList( ast->returnValues, expectedast->returnValues );
}

void TestVisitor::visitYield( YieldAst* ast )
{
    YieldAst* expectedast = pop<YieldAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkList( ast->yieldValue, expectedast->yieldValue );
}

void TestVisitor::visitDel( DelAst* ast )
{
    DelAst* expectedast = pop<DelAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkList( ast->deleteObjects, expectedast->deleteObjects );
}

void TestVisitor::visitAssert( AssertAst* ast )
{
    AssertAst* expectedast = pop<AssertAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkNode( ast->assertTest, expectedast->assertTest );
    checkOptional( ast->exceptionValue, expectedast->exceptionValue );
}

void TestVisitor::visitExpressionStatement( ExpressionStatementAst* ast )
{
    ExpressionStatementAst* expectedast = pop<ExpressionStatementAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkList( ast->expressions, expectedast->expressions );
}

void TestVisitor::visitAssignment( AssignmentAst* ast )
{
    AssignmentAst* expectedast = pop<AssignmentAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkPairList( ast->targets, expectedast->targets );
    checkOptional( ast->yieldValue, expectedast->yieldValue );
    checkList( ast->value, expectedast->value );
}

void TestVisitor::visitAtom( AtomAst* ast )
{
    AtomAst* expectedast = pop<AtomAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkOptional( ast->enclosure, expectedast->enclosure );
    checkOptional( ast->identifier, expectedast->identifier );
    checkOptional( ast->literal, expectedast->literal );
}

void TestVisitor::visitEnclosure( EnclosureAst* ast )
{
    EnclosureAst* expectedast = pop<EnclosureAst>();
    BASIC_AST_TEST( ast, expectedast );
    QCOMPARE( ast->encType, expectedast->encType );
    switch( ast->encType )
    {
        case EnclosureAst::Dictionary:
            checkNode( ast->dict, expectedast->dict );
            break;
        case EnclosureAst::Generator:
            checkNode( ast->generator, expectedast->generator );
            break;
        case EnclosureAst::ParenthesizedForm:
            checkList( ast->parenthesizedform, expectedast->parenthesizedform );
            break;
        case EnclosureAst::StringConversion:
            checkList( ast->stringConversion, expectedast->stringConversion );
            break;
        case EnclosureAst::List:
            checkNode( ast->list, expectedast->list );
            break;
        case EnclosureAst::Yield:
            checkNode( ast->yield, expectedast->yield );
            break;
    }
}

void TestVisitor::visitList( ListAst* ast )
{
    ListAst* expectedast = pop<ListAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkList( ast->plainList, expectedast->plainList );
    checkOptional( ast->listGenerator, expectedast->listGenerator );
}

void TestVisitor::visitListFor( ListForAst* ast )
{
    ListForAst* expectedast = pop<ListForAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkList( ast->assignedTargets, expectedast->assignedTargets );
    checkList( ast->iterableObject, expectedast->iterableObject );
    checkOptional( ast->nextCondition, expectedast->nextCondition );
    checkOptional( ast->nextGenerator, expectedast->nextGenerator );
}

void TestVisitor::visitListIf( ListIfAst* ast )
{
    ListIfAst* expectedast = pop<ListIfAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkNode( ast->condition, expectedast->condition );
    checkOptional( ast->nextCondition, expectedast->nextCondition );
    checkOptional( ast->nextGenerator, expectedast->nextGenerator );
}

void TestVisitor::visitLiteral( LiteralAst* ast )
{
    LiteralAst* expectedast = pop<LiteralAst>();
    BASIC_AST_TEST( ast, expectedast );
    QCOMPARE( ast->literalType, expectedast->literalType );
    QCOMPARE( ast->value, expectedast->value );
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

