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
    QCOMPARE( result->end, expected->end ); \
    QCOMPARE( result->endCol, expected->endCol ); \
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
    checkList( ast->statements, expectedast->statements );
    Q_ASSERT( expectedStack.isEmpty() );
}

void TestVisitor::visitFunctionDefinition( FunctionDefinitionAst* ast )
{
    FunctionDefinitionAst* expectedast = pop<FunctionDefinitionAst>();
    BASIC_AST_TEST( ast, expectedast );
    
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
    checkOptional( ast->value, expectedast->value );
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

void TestVisitor::visitGenerator( GeneratorAst* ast )
{
    GeneratorAst* expectedast = pop<GeneratorAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkNode( ast->generatedValue, expectedast->generatedValue );
    checkNode( ast->generator, expectedast->generator );
}

void TestVisitor::visitGeneratorFor( GeneratorForAst* ast )
{
    GeneratorForAst* expectedast = pop<GeneratorForAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkList( ast->assignedTargets, expectedast->assignedTargets );
    checkNode( ast->iterableObject, expectedast->iterableObject );
    checkOptional( ast->nextCondition, expectedast->nextCondition );
    checkOptional( ast->nextGenerator, expectedast->nextGenerator );
}

void TestVisitor::visitGeneratorIf( GeneratorIfAst* ast )
{
    GeneratorIfAst* expectedast = pop<GeneratorIfAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkNode( ast->condition, expectedast->condition );
    checkOptional( ast->nextCondition, expectedast->nextCondition );
    checkOptional( ast->nextGenerator, expectedast->nextGenerator );
}

void TestVisitor::visitDictionary( DictionaryAst* ast )
{
    DictionaryAst* expectedast = pop<DictionaryAst>();
    BASIC_AST_TEST( ast, expectedast );
    QCOMPARE( ast->dictionary.count(), expectedast->dictionary.count() );
    QMap<ExpressionAst*, ExpressionAst*>::ConstIterator it, end = ast->dictionary.end();
    QMap<ExpressionAst*, ExpressionAst*>::ConstIterator expectedit, expectedend = expectedast->dictionary.end();
    for( it = ast->dictionary.begin(), expectedit = expectedast->dictionary.begin(); it != end, expectedit != expectedend; it++, expectedit++ )
    {
        checkNode( it.key(), expectedit.key() );
        checkNode( it.value(), expectedit.value() );
    }
}

void TestVisitor::visitAttributeReference( AttributeReferenceAst* ast )
{
    AttributeReferenceAst* expectedast = pop<AttributeReferenceAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkNode( ast->primary, expectedast->primary );
    checkNode( ast->identifier, expectedast->identifier );
}

void TestVisitor::visitSubscript( SubscriptAst* ast )
{
    SubscriptAst* expectedast = pop<SubscriptAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkNode( ast->primary, expectedast->primary );
    checkList( ast->subscription, expectedast->subscription );
}

void TestVisitor::visitExtendedSlice( ExtendedSliceAst* ast )
{
    ExtendedSliceAst* expectedast = pop<ExtendedSliceAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkNode( ast->primary, expectedast->primary );
    checkList( ast->extendedSliceList, expectedast->extendedSliceList );
}

void TestVisitor::visitSimpleSlice( SimpleSliceAst* ast )
{
    SimpleSliceAst* expectedast = pop<SimpleSliceAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkNode( ast->primary, expectedast->primary );
    checkNode( ast->simpleSliceBounds.first, expectedast->simpleSliceBounds.first );
    checkNode( ast->simpleSliceBounds.second, expectedast->simpleSliceBounds.second );
}

void TestVisitor::visitProperSliceItem( ProperSliceItemAst* ast )
{
    ProperSliceItemAst* expectedast = pop<ProperSliceItemAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkNode( ast->bounds.first, expectedast->bounds.first );
    checkNode( ast->bounds.second, expectedast->bounds.second );
    checkOptional( ast->stride, expectedast->stride );
}

void TestVisitor::visitExpressionSliceItem( ExpressionSliceItemAst* ast )
{
    ExpressionSliceItemAst* expectedast = pop<ExpressionSliceItemAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkNode( ast->sliceExpression, expectedast->sliceExpression );
}

void TestVisitor::visitEllipsisSliceItem( EllipsisSliceItemAst* ast )
{
    EllipsisSliceItemAst* expectedast = pop<EllipsisSliceItemAst>();
    BASIC_AST_TEST( ast, expectedast );
}

void TestVisitor::visitCall( CallAst* ast )
{
    CallAst* expectedast = pop<CallAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkNode( ast->callable, expectedast->callable );
    checkList( ast->arguments, expectedast->arguments );
    checkOptional( ast->generator, expectedast->generator );
}

void TestVisitor::visitUnaryExpression( UnaryExpressionAst* ast )
{
    UnaryExpressionAst* expectedast = pop<UnaryExpressionAst>();
    BASIC_AST_TEST( ast, expectedast );
    QCOMPARE( ast->opType, expectedast->opType );
    checkNode( ast->operand, expectedast->operand );
}

void TestVisitor::visitBinaryExpression( BinaryExpressionAst* ast )
{
    BinaryExpressionAst* expectedast = pop<BinaryExpressionAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkNode( ast->lhs, expectedast->lhs );
    QCOMPARE( ast->opType, expectedast->opType );
    checkNode( ast->rhs, expectedast->rhs );
}

void TestVisitor::visitComparison( ComparisonAst* ast )
{
    ComparisonAst* expectedast = pop<ComparisonAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkNode( ast->firstComparator, expectedast->firstComparator );
    checkPairList( ast->comparatorList, expectedast->comparatorList );
}

void TestVisitor::visitBooleanNotOperation( BooleanNotOperationAst* ast )
{
    BooleanNotOperationAst* expectedast = pop<BooleanNotOperationAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkNode( ast->op, expectedast->op );
}

void TestVisitor::visitBooleanAndOperation( BooleanAndOperationAst* ast )
{
    BooleanAndOperationAst* expectedast = pop<BooleanAndOperationAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkNode( ast->lhs, expectedast->lhs );
    checkNode( ast->rhs, expectedast->rhs );
}

void TestVisitor::visitBooleanOrOperation( BooleanOrOperationAst* ast )
{
    BooleanOrOperationAst* expectedast = pop<BooleanOrOperationAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkNode( ast->lhs, expectedast->lhs );
    checkNode( ast->rhs, expectedast->rhs );
}

void TestVisitor::visitConditionalExpression( ConditionalExpressionAst* ast )
{
    ConditionalExpressionAst* expectedast = pop<ConditionalExpressionAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkNode( ast->mainExpression, expectedast->mainExpression );
    checkNode( ast->condition, expectedast->condition );
    checkNode( ast->elseExpression, expectedast->elseExpression );
}

void TestVisitor::visitLambda( LambdaAst* ast )
{
    LambdaAst* expectedast = pop<LambdaAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkList( ast->parameters, expectedast->parameters );
    checkNode( ast->expression, expectedast->expression );
}

void TestVisitor::visitBreak( StatementAst* ast )
{
    StatementAst* expectedast = pop<StatementAst>();
    BASIC_AST_TEST( ast, expectedast );
}

void TestVisitor::visitContinue( StatementAst* ast )
{
    StatementAst* expectedast = pop<StatementAst>();
    BASIC_AST_TEST( ast, expectedast );
}

void TestVisitor::visitPass( StatementAst* ast )
{
    StatementAst* expectedast = pop<StatementAst>();
    BASIC_AST_TEST( ast, expectedast );
}

void TestVisitor::visitIdentifier( IdentifierAst* ast )
{
    IdentifierAst* expectedast = pop<IdentifierAst>();
    BASIC_AST_TEST( ast, expectedast );
    QCOMPARE( ast->identifier, expectedast->identifier );
}

void TestVisitor::visitIdentifierTarget( IdentifierTargetAst* ast )
{
    IdentifierTargetAst* expectedast = pop<IdentifierTargetAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkNode( ast->identifier, expectedast->identifier );
}

void TestVisitor::visitListTarget( ListTargetAst* ast )
{
    ListTargetAst* expectedast = pop<ListTargetAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkList( ast->items, expectedast->items );
}

void TestVisitor::visitTupleTarget( TupleTargetAst* ast )
{
    TupleTargetAst* expectedast = pop<TupleTargetAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkList( ast->items, expectedast->items );
}

void TestVisitor::visitAttributeReferenceTarget( AttributeReferenceTargetAst* ast )
{
    AttributeReferenceTargetAst* expectedast = pop<AttributeReferenceTargetAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkNode( ast->attribute, expectedast->attribute );
}

void TestVisitor::visitSubscriptTarget( SubscriptTargetAst* ast )
{
    SubscriptTargetAst* expectedast = pop<SubscriptTargetAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkNode( ast->subscript, expectedast->subscript );
}

void TestVisitor::visitSliceTarget( SliceTargetAst* ast )
{
    SliceTargetAst* expectedast = pop<SliceTargetAst>();
    BASIC_AST_TEST( ast, expectedast );
    checkNode( ast->slice, expectedast->slice );
}

