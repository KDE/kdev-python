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

#include "astdefaultvisitor.h"

namespace Python
{

AstDefaultVisitor::AstDefaultVisitor()
    : AstVisitor()
{
}

AstDefaultVisitor::~AstDefaultVisitor()
{
}

void AstDefaultVisitor::visitCode( CodeAst* code )
{
    foreach( StatementAst* stmt, code->statements )
    {
        visitNode( stmt );
    }
}

void AstDefaultVisitor::visitFunctionDefinition( FunctionDefinitionAst* node )
{
    foreach( DecoratorAst* ast, node->decorators )
    {
        visitNode( ast );
    }
    
    foreach( ParameterAst* ast, node->parameters )
    {
        visitNode( ast );
    }
    
    foreach( StatementAst* ast, node->functionBody )
    {
        visitNode( ast );
    }
}

void AstDefaultVisitor::visitTarget( TargetAst* node )
{
    switch( node->targetType )
    {
        case TargetAst::TupleTarget:
        case TargetAst::ListTarget:
            foreach( TargetAst* t, node->listItems )
            {
                visitNode( t );
            }
            break;
        case TargetAst::AttributeReferenceTarget:
            visitNode( node->attributeReference );
            break;
        case TargetAst::SubscriptTarget:
            visitNode( node->subscript );
            break;
        case TargetAst::SliceTarget:
            visitNode( node->slice );
            break;
    }
}

void AstDefaultVisitor::visitDecorator( DecoratorAst* node )
{
    foreach( ArgumentAst* a, node->arguments )
    {
        visitNode( a );
    }
}

void AstDefaultVisitor::visitArgument( ArgumentAst* node )
{
    visitNode( node->argumentExpression );
}

void AstDefaultVisitor::visitDefaultParameter( DefaultParameterAst* node )
{
    visitNode( node->name );
    visitNode( node->value );
}

void AstDefaultVisitor::visitIdentifierParameterPart( IdentifierParameterPartAst* )
{
}

void AstDefaultVisitor::visitListParameterPart( ListParameterPartAst* node )
{
    foreach( ParameterPartAst* a, node->parameternames )
    {
        visitNode( a );
    }
}

void AstDefaultVisitor::visitDictionaryParameter( DictionaryParameterAst* )
{
}

void AstDefaultVisitor::visitListParameter( ListParameterAst* )
{
}

void AstDefaultVisitor::visitIf( IfAst* node )
{
    visitNode( node->ifCondition );
    foreach( StatementAst* a, node->ifBody )
    {
        visitNode( a );
    }
    QList<QPair<ExpressionAst*, QList<StatementAst*> > >::const_iterator it = 
            node->elseIfBodies.begin();
    QList<QPair<ExpressionAst*, QList<StatementAst*> > >::const_iterator end = 
            node->elseIfBodies.end();
    for( ; it != end; ++it )
    {
        QPair<ExpressionAst*, QList<StatementAst*> > p = *it;
        visitNode( p.first );
        foreach( StatementAst* a, p.second )
        {
            visitNode( a );
        }
    }
    foreach( StatementAst* a, node->elseBody )
    {
        visitNode( a );
    }
}

void AstDefaultVisitor::visitWhile( WhileAst* node )
{
    visitNode( node->condition );
    
    foreach( StatementAst* a, node->whileBody )
    {
        visitNode( a );
    }
    
    foreach( StatementAst* a, node->elseBody )
    {
        visitNode( a );
    }
}

void AstDefaultVisitor::visitFor( ForAst* node )
{
    
    foreach( TargetAst* a, node->assignedTargets )
    {
        visitNode( a );
    }
    
    foreach( ExpressionAst* a, node->iterable )
    {
        visitNode( a );
    }
    
    foreach( StatementAst* a, node->forBody )
    {
        visitNode( a );
    }
    
    
    foreach( StatementAst* a, node->elseBody )
    {
        visitNode( a );
    }
}

void AstDefaultVisitor::visitClassDefinition( ClassDefinitionAst* node )
{
    foreach( ExpressionAst* a, node->inheritance )
    {
        visitNode( a );
    }
    foreach( StatementAst* a, node->classBody )
    {
        visitNode( a );
    }
}

void AstDefaultVisitor::visitTry( TryAst* node )
{
    
    foreach( StatementAst* a, node->tryBody )
    {
        visitNode( a );
    }
    foreach( ExceptAst* a, node->exceptions )
    {
        visitNode( a );
    }
    
    foreach( StatementAst* a, node->elseBody )
    {
        visitNode( a );
    }
    foreach( StatementAst* a, node->finallyBody )
    {
        visitNode( a );
    }
}

void AstDefaultVisitor::visitExcept( ExceptAst* node )
{
    visitNode( node->exceptionDeclaration );
    visitNode( node->exceptionValue );
    foreach( StatementAst* a, node->exceptionBody )
    {
        visitNode( a );
    }
}

void AstDefaultVisitor::visitWith( WithAst* node )
{
    visitNode( node->context );
    visitNode( node->name );
    foreach( StatementAst* a, node->body )
    {
        visitNode( a );
    }
}

void AstDefaultVisitor::visitExec( ExecAst* node )
{
    visitNode( node->executable );
    visitNode( node->globalsAndLocals );
    visitNode( node->localsOnly );
}

void AstDefaultVisitor::visitGlobal( GlobalAst* )
{
}

void AstDefaultVisitor::visitPlainImport( PlainImportAst* )
{
}

void AstDefaultVisitor::visitStarImport( StarImportAst* )
{
}

void AstDefaultVisitor::visitFromImport( FromImportAst* )
{
}

void AstDefaultVisitor::visitRaise( RaiseAst* node )
{
    visitNode( node->exceptionType );
    visitNode( node->exceptionValue );
    visitNode( node->traceback );
}

void AstDefaultVisitor::visitPrint( PrintAst* node )
{
    visitNode( node->outfile );
    foreach( ExpressionAst* a, node->printables )
    {
        visitNode( a );
    }
}

void AstDefaultVisitor::visitReturn( ReturnAst* node )
{
    foreach( ExpressionAst* e, node->returnValues )
    {
        visitNode( e );
    }
}

void AstDefaultVisitor::visitYield( YieldAst* node )
{
    foreach( ExpressionAst* e, node->yieldValue )
    {
        visitNode( e );
    }
}

void AstDefaultVisitor::visitDel( DelAst* node )
{
    foreach( TargetAst* t, node->deleteObjects )
    {
        visitNode( t );
    }
}

void AstDefaultVisitor::visitAssert( AssertAst* node )
{
    visitNode( node->assertTest );
    visitNode( node->exceptionValue );
}

void AstDefaultVisitor::visitExpressionStatement( ExpressionStatementAst* node )
{
    foreach( ExpressionAst* e, node->expressions )
    {
        visitNode( e );
    }
}

void AstDefaultVisitor::visitAssignment( AssignmentAst* node )
{
    foreach( QList<TargetAst*> tl,  node->targets )
    {
        foreach( TargetAst* t,  tl )
        {
            visitNode( t );
        }
    }
    foreach( ExpressionAst* e, node->value )
    {
        visitNode( e );
    }
    visitNode( node->yieldValue );
}

void AstDefaultVisitor::visitAtom( AtomAst* node )
{
    visitNode( node->enclosure );
}

void AstDefaultVisitor::visitEnclosure( EnclosureAst* node )
{
    switch( node->encType )
    {
        case EnclosureAst::Dictionary:
            visitNode( node->dict );
            break;
        case EnclosureAst::Generator:
            visitNode( node->generator );
            break;
        case EnclosureAst::List:
            visitNode( node->list );
            break;
        case EnclosureAst::Yield:
            visitNode( node->yield );
            break;
        case EnclosureAst::ParenthesizedForm:
            foreach( ExpressionAst* a, node->parenthesizedform )
            {
                visitNode( a );
            }
            break;
        case EnclosureAst::StringConversion:
            foreach( ExpressionAst* a, node->stringConversion )
            {
                visitNode( a );
            }
            break;
    }
}

void AstDefaultVisitor::visitList( ListAst* node )
{
    foreach( ExpressionAst* a, node->plainList )
    {
        visitNode( a );
    }
    visitNode( node->listGenerator );
}

void AstDefaultVisitor::visitListFor( ListForAst* node )
{
    foreach( TargetAst* t, node->assignedTargets )
    {
        visitNode( t );
    }
    foreach( ExpressionAst* e, node->iterableObject )
    {
        visitNode( e );
    }
    visitNode( node->nextGenerator );
    visitNode( node->nextCondition );
}

void AstDefaultVisitor::visitListIf( ListIfAst* node )
{
    visitNode( node->condition );
    visitNode( node->nextGenerator );
    visitNode( node->nextCondition );
}

void AstDefaultVisitor::visitGenerator( GeneratorAst* node )
{
    visitNode( node->generatedValue );
    visitNode( node->generator );
}

void AstDefaultVisitor::visitGeneratorFor( GeneratorForAst* node )
{
    foreach( TargetAst* t, node->assignedTargets )
    {
        visitNode( t );
    }
    visitNode( node->iterableObject );
    visitNode( node->nextGenerator );
    visitNode( node->nextCondition );
}

void AstDefaultVisitor::visitGeneratorIf( GeneratorIfAst* node )
{
    visitNode( node->condition );
    visitNode( node->nextGenerator );
    visitNode( node->nextCondition );
}

void AstDefaultVisitor::visitDictionary( DictionaryAst* node )
{
    foreach( ExpressionAst* key, node->dictionary.keys() )
    {
        visitNode( key );
        visitNode( node->dictionary[key] );
    }
}

void AstDefaultVisitor::visitAttributeReference( AttributeReferenceAst* node )
{
    visitNode( node->primary );
}

void AstDefaultVisitor::visitSubscript( SubscriptAst* node )
{
    visitNode( node->primary );
    foreach( ExpressionAst* e, node->subscription )
    {
        visitNode( e );
    }
}

void AstDefaultVisitor::visitExtendedSlice( ExtendedSliceAst* node )
{
    visitNode( node->primary );
    foreach( SliceItemAst* s, node->extendedSliceList )
    {
        visitNode( s );
    }
}

void AstDefaultVisitor::visitSimpleSlice( SimpleSliceAst* node )
{
    visitNode( node->primary );
    visitNode( node->simpleSliceBounds.first );
    visitNode( node->simpleSliceBounds.second );
}

void AstDefaultVisitor::visitProperSliceItem( ProperSliceItemAst* node )
{
    visitNode( node->bounds.first );
    visitNode( node->bounds.second );
    visitNode( node->stride );
}

void AstDefaultVisitor::visitExpressionSlice( ExpressionSliceAst* node )
{
    visitNode( node->sliceExpression );
}

void AstDefaultVisitor::visitEllipsisSlice( EllipsisSliceAst* )
{
}

void AstDefaultVisitor::visitCall( CallAst* node )
{
    visitNode( node->callable );
    foreach( ArgumentAst* a, node->arguments )
    {
        visitNode( a );
    }
    visitNode( node->callValue );
    visitNode( node->callGenerator );
}

void AstDefaultVisitor::visitUnaryExpression( UnaryExpressionAst* node )
{
    visitNode( node->primary );
    visitNode( node->operand );
}

void AstDefaultVisitor::visitBinaryExpression( BinaryExpressionAst* node )
{
    visitNode( node->lhs );
    visitNode( node->rhs );
}

void AstDefaultVisitor::visitComparison( ComparisonAst* node )
{
    visitNode( node->firstComparator );
    foreach( BinaryExpressionAst* b, node->comparatorList.values() )
    {
        visitNode( b );
    }
}

void AstDefaultVisitor::visitBooleanNotOperation( BooleanNotOperationAst* node )
{
    visitNode( node->op );
}

void AstDefaultVisitor::visitBooleanOrOperation( BooleanOrOperationAst* node )
{
    visitNode( node->lhs );
    visitNode( node->rhs );
}

void AstDefaultVisitor::visitBooleanAndOperation( BooleanAndOperationAst* node )
{
    visitNode( node->lhs );
    visitNode( node->rhs );
}

void AstDefaultVisitor::visitConditionalExpression( ConditionalExpressionAst* node )
{
    visitNode( node->mainExpression );
    visitNode( node->condition );
    visitNode( node->elseExpression );
}

void AstDefaultVisitor::visitLambda( LambdaAst* node )
{
    foreach( ParameterAst* p, node->parameters )
    {
        visitNode( p );
    }
    visitNode( node->expression );
}

void AstDefaultVisitor::visitPass( StatementAst* )
{
}

void AstDefaultVisitor::visitContinue( StatementAst* )
{
}

void AstDefaultVisitor::visitBreak( StatementAst* )
{
}

}
