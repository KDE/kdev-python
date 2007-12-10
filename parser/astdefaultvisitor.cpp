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
        visitStatement( stmt );
    }
}

void AstDefaultVisitor::visitFunctionDefinition( FunctionDefinitionAst* )
{
}

void AstDefaultVisitor::visitTarget( TargetAst* )
{
}

void AstDefaultVisitor::visitDecorator( DecoratorAst* )
{
}

void AstDefaultVisitor::visitArgument( ArgumentAst* )
{
}

void AstDefaultVisitor::visitDefaultParameter( DefaultParameterAst* )
{
}

void AstDefaultVisitor::visitIdentifierParameterPart( IdentifierParameterPartAst* )
{
}

void AstDefaultVisitor::visitListParameterPart( ListParameterPartAst* )
{
}

void AstDefaultVisitor::visitDictionaryParameter( DictionaryParameterAst* )
{
}

void AstDefaultVisitor::visitListParameter( ListParameterAst* )
{
}

void AstDefaultVisitor::visitIf( IfAst* )
{
}

void AstDefaultVisitor::visitWhile( WhileAst* )
{
}

void AstDefaultVisitor::visitFor( ForAst* )
{
}

void AstDefaultVisitor::visitClassDefinition( ClassDefinitionAst* )
{
}

void AstDefaultVisitor::visitTry( TryAst* )
{
}

void AstDefaultVisitor::visitExcept( ExceptAst* )
{
}

void AstDefaultVisitor::visitWith( WithAst* )
{
}

void AstDefaultVisitor::visitExec( ExecAst* )
{
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

void AstDefaultVisitor::visitRaise( RaiseAst* )
{
}

void AstDefaultVisitor::visitPrint( PrintAst* )
{
}

void AstDefaultVisitor::visitReturn( ReturnAst* )
{
}

void AstDefaultVisitor::visitYield( YieldAst* )
{
}

void AstDefaultVisitor::visitDel( DelAst* )
{
}

void AstDefaultVisitor::visitAssert( AssertAst* )
{
}

void AstDefaultVisitor::visitExpressionStatement( ExpressionStatementAst* )
{
}

void AstDefaultVisitor::visitAssignment( AssignmentAst* )
{
}

void AstDefaultVisitor::visitAtom( AtomAst* )
{
}

void AstDefaultVisitor::visitEnclosure( EnclosureAst* )
{
}

void AstDefaultVisitor::visitList( ListAst* )
{
}

void AstDefaultVisitor::visitListFor( ListForAst* )
{
}

void AstDefaultVisitor::visitListIf( ListIfAst* )
{
}

void AstDefaultVisitor::visitGenerator( GeneratorAst* )
{
}

void AstDefaultVisitor::visitGeneratorFor( GeneratorForAst* )
{
}

void AstDefaultVisitor::visitGeneratorIf( GeneratorIfAst* )
{
}

void AstDefaultVisitor::visitDictionary( DictionaryAst* )
{
}

void AstDefaultVisitor::visitAttributeReference( AttributeReferenceAst* )
{
}

void AstDefaultVisitor::visitSubscript( SubscriptAst* )
{
}

void AstDefaultVisitor::visitExtendedSlice( ExtendedSliceAst* )
{
}

void AstDefaultVisitor::visitSimpleSlice( SimpleSliceAst* )
{
}

void AstDefaultVisitor::visitProperSliceItem( ProperSliceItemAst* )
{
}

void AstDefaultVisitor::visitExpressionSlice( ExpressionSliceAst* )
{
}

void AstDefaultVisitor::visitEllipsisSlice( EllipsisSliceAst* )
{
}

void AstDefaultVisitor::visitCall( CallAst* )
{
}

void AstDefaultVisitor::visitUnaryExpression( UnaryExpressionAst* )
{
}

void AstDefaultVisitor::visitBinaryExpression( BinaryExpressionAst* )
{
}

void AstDefaultVisitor::visitComparison( ComparisonAst* )
{
}

void AstDefaultVisitor::visitBooleanNotOperation( BooleanNotOperationAst* )
{
}

void AstDefaultVisitor::visitBooleanOrOperation( BooleanOrOperationAst* )
{
}

void AstDefaultVisitor::visitBooleanAndOperation( BooleanAndOperationAst* )
{
}

void AstDefaultVisitor::visitConditionalExpression( ConditionalExpressionAst* )
{
}

void AstDefaultVisitor::visitLambda( LambdaAst* )
{
}

void AstDefaultVisitor::visitPass( PassAst * )
{
}

void AstDefaultVisitor::visitContinue( ContinueAst * )
{
}

void AstDefaultVisitor::visitBreak( BreakAst * )
{
}

}
