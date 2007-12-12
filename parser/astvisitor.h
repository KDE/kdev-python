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

#ifndef PYTHONASTVISITOR_H
#define PYTHONASTVISITOR_H

#include "ast.h"

namespace Python
{

class AstVisitor
{
public:
    virtual ~AstVisitor() {}

    typedef void (AstVisitor::*visitFunc)(Ast *);

    void visitNode( Ast* );

    virtual void visitCode( CodeAst* ) = 0;
    virtual void visitFunctionDefinition( FunctionDefinitionAst* ) = 0;
    virtual void visitTarget( TargetAst* ) = 0;
    virtual void visitDecorator( DecoratorAst* ) = 0;
    virtual void visitArgument( ArgumentAst* ) = 0;
    virtual void visitDefaultParameter( DefaultParameterAst* ) = 0;
    virtual void visitIdentifierParameterPart( IdentifierParameterPartAst* ) = 0;
    virtual void visitListParameterPart( ListParameterPartAst* ) = 0;
    virtual void visitDictionaryParameter( DictionaryParameterAst* ) = 0;
    virtual void visitListParameter( ListParameterAst* ) = 0;
    virtual void visitIf( IfAst* ) = 0;
    virtual void visitWhile( WhileAst* ) = 0;
    virtual void visitFor( ForAst* ) = 0;
    virtual void visitClassDefinition( ClassDefinitionAst* ) = 0;
    virtual void visitTry( TryAst* ) = 0;
    virtual void visitExcept( ExceptAst* ) = 0;
    virtual void visitWith( WithAst* ) = 0;
    virtual void visitExec( ExecAst* ) = 0;
    virtual void visitGlobal( GlobalAst* ) = 0;
    virtual void visitPlainImport( PlainImportAst* ) = 0;
    virtual void visitStarImport( StarImportAst* ) = 0;
    virtual void visitFromImport( FromImportAst* ) = 0;
    virtual void visitRaise( RaiseAst* ) = 0;
    virtual void visitPrint( PrintAst* ) = 0;
    virtual void visitReturn( ReturnAst* ) = 0;
    virtual void visitYield( YieldAst* ) = 0;
    virtual void visitDel( DelAst* ) = 0;
    virtual void visitAssert( AssertAst* ) = 0;
    virtual void visitExpressionStatement( ExpressionStatementAst* ) = 0;
    virtual void visitAssignment( AssignmentAst* ) = 0;
    virtual void visitAtom( AtomAst* ) = 0;
    virtual void visitEnclosure( EnclosureAst* ) = 0;
    virtual void visitList( ListAst* ) = 0;
    virtual void visitListFor( ListForAst* ) = 0;
    virtual void visitListIf( ListIfAst* ) = 0;
    virtual void visitGenerator( GeneratorAst* ) = 0;
    virtual void visitGeneratorFor( GeneratorForAst* ) = 0;
    virtual void visitGeneratorIf( GeneratorIfAst* ) = 0;
    virtual void visitDictionary( DictionaryAst* ) = 0;
    virtual void visitAttributeReference( AttributeReferenceAst* ) = 0;
    virtual void visitSubscript( SubscriptAst* ) = 0;
    virtual void visitExtendedSlice( ExtendedSliceAst* ) = 0;
    virtual void visitSimpleSlice( SimpleSliceAst* ) = 0;
    virtual void visitProperSliceItem( ProperSliceItemAst* ) = 0;
    virtual void visitExpressionSlice( ExpressionSliceAst* ) = 0;
    virtual void visitEllipsisSlice( EllipsisSliceAst* ) = 0;
    virtual void visitCall( CallAst* ) = 0;
    virtual void visitUnaryExpression( UnaryExpressionAst* ) = 0;
    virtual void visitBinaryExpression( BinaryExpressionAst* ) = 0;
    virtual void visitComparison( ComparisonAst* ) = 0;
    virtual void visitBooleanNotOperation( BooleanNotOperationAst* ) = 0;
    virtual void visitBooleanAndOperation( BooleanAndOperationAst* ) = 0;
    virtual void visitBooleanOrOperation( BooleanOrOperationAst* ) = 0;
    virtual void visitConditionalExpression( ConditionalExpressionAst* ) = 0;
    virtual void visitLambda( LambdaAst* ) = 0;
    virtual void visitBreak( StatementAst* ) = 0;
    virtual void visitContinue( StatementAst* ) = 0;
    virtual void visitPass( StatementAst* ) = 0;
    virtual void visitIdentifier( IdentifierAst* ) = 0;
};
}

#endif
