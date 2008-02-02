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

#ifndef TESTVISITOR_H
#define TESTVISITOR_H

#include "astdefaultvisitor.h"
#include "ast.h"
#include <QStack>
#include <QList>
#include <QtTest/QtTest>

class TestVisitor : public Python::AstDefaultVisitor
{
public:
    TestVisitor();
    ~TestVisitor();
    
    void setExpected( Python::CodeAst* );
    
    virtual void visitCode( Python::CodeAst* );
    virtual void visitFunctionDefinition( Python::FunctionDefinitionAst* );
    virtual void visitDecorator( Python::DecoratorAst* );
    virtual void visitArgument( Python::ArgumentAst* );
    virtual void visitDefaultParameter( Python::DefaultParameterAst* );
    virtual void visitIdentifierParameterPart( Python::IdentifierParameterPartAst* );
    virtual void visitListParameterPart( Python::ListParameterPartAst* );
    virtual void visitDictionaryParameter( Python::DictionaryParameterAst* );
    virtual void visitListParameter( Python::ListParameterAst* );
    virtual void visitIf( Python::IfAst* );
    virtual void visitWhile( Python::WhileAst* );
    virtual void visitFor( Python::ForAst* );
    virtual void visitClassDefinition( Python::ClassDefinitionAst* );
    virtual void visitTry( Python::TryAst* );
    virtual void visitExcept( Python::ExceptAst* );
    virtual void visitWith( Python::WithAst* );
    virtual void visitExec( Python::ExecAst* );
    virtual void visitGlobal( Python::GlobalAst* );
    virtual void visitPlainImport( Python::PlainImportAst* );
    virtual void visitStarImport( Python::StarImportAst* );
    virtual void visitFromImport( Python::FromImportAst* );
    virtual void visitRaise( Python::RaiseAst* );
    virtual void visitPrint( Python::PrintAst* );
    virtual void visitReturn( Python::ReturnAst* );
    virtual void visitYield( Python::YieldAst* );
    virtual void visitDel( Python::DelAst* );
    virtual void visitAssert( Python::AssertAst* );
    virtual void visitExpressionStatement( Python::ExpressionStatementAst* );
    virtual void visitAssignment( Python::AssignmentAst* );
    virtual void visitAtom( Python::AtomAst* );
    virtual void visitEnclosure( Python::EnclosureAst* );
    virtual void visitList( Python::ListAst* );
    virtual void visitListFor( Python::ListForAst* );
    virtual void visitListIf( Python::ListIfAst* );
    virtual void visitLiteral( Python::LiteralAst* );
    virtual void visitGenerator( Python::GeneratorAst* );
    virtual void visitGeneratorFor( Python::GeneratorForAst* );
    virtual void visitGeneratorIf( Python::GeneratorIfAst* );
    virtual void visitDictionary( Python::DictionaryAst* );
    virtual void visitAttributeReference( Python::AttributeReferenceAst* );
    virtual void visitSubscript( Python::SubscriptAst* );
    virtual void visitExtendedSlice( Python::ExtendedSliceAst* );
    virtual void visitSimpleSlice( Python::SimpleSliceAst* );
    virtual void visitProperSliceItem( Python::ProperSliceItemAst* );
    virtual void visitExpressionSliceItem( Python::ExpressionSliceItemAst* );
    virtual void visitEllipsisSliceItem( Python::EllipsisSliceItemAst* );
    virtual void visitCall( Python::CallAst* );
    virtual void visitUnaryExpression( Python::UnaryExpressionAst* );
    virtual void visitBinaryExpression( Python::BinaryExpressionAst* );
    virtual void visitComparison( Python::ComparisonAst* );
    virtual void visitBooleanNotOperation( Python::BooleanNotOperationAst* );
    virtual void visitBooleanAndOperation( Python::BooleanAndOperationAst* );
    virtual void visitBooleanOrOperation( Python::BooleanOrOperationAst* );
    virtual void visitConditionalExpression( Python::ConditionalExpressionAst* );
    virtual void visitLambda( Python::LambdaAst* );
    virtual void visitBreak( Python::StatementAst* );
    virtual void visitContinue( Python::StatementAst* );
    virtual void visitPass( Python::StatementAst* );
    virtual void visitIdentifier( Python::IdentifierAst* );
    virtual void visitIdentifierTarget( Python::IdentifierTargetAst* );
    virtual void visitListTarget( Python::ListTargetAst* );
    virtual void visitTupleTarget( Python::TupleTargetAst* );
    virtual void visitAttributeReferenceTarget( Python::AttributeReferenceTargetAst* );
    virtual void visitSubscriptTarget( Python::SubscriptTargetAst* );
    virtual void visitSliceTarget( Python::SliceTargetAst* );

private:
    template <typename T> T* pop() 
    {
        T* ast = dynamic_cast<T*>( expectedStack.pop() );
        Q_ASSERT(ast);
        return ast;
    }
    template <typename T> void checkList( const QList<T*>& l, const QList<T*>& expected )
    {
        QCOMPARE( l.count(), expected.count() );
        typename QList<T*>::ConstIterator it, end = l.end();
        typename QList<T*>::ConstIterator expectedit, expectedend = expected.end();
        for( it = l.begin(), expectedit = expected.begin(); it != end, expectedit != expectedend; it++, expectedit++ )
        {
            expectedStack.push( *expectedit );
            visitNode( *it );
        }
    }

    template <typename T1, typename T2> void checkPairList( const QList<QPair<T1*, QList<T2*> > >& l, const QList<QPair<T1*, QList<T2*> > >& expected )
    {
        QCOMPARE( l.count(), expected.count() );
        typename QList<QPair<T1*, QList<T2*> > >::ConstIterator it, end = l.end();
        typename QList<QPair<T1*, QList<T2*> > >::ConstIterator expectedit, expectedend = expected.end();
        for( it = l.begin(), expectedit = expected.begin(); it != end, expectedit != expectedend; it++, expectedit++ )
        {
            expectedStack.push( (*expectedit).first );
            visitNode( (*it).first );
            checkList( (*it).second, (*expectedit).second );
        }
    }
    template <typename T1, typename T2> void checkPairList( const QList<QPair<QList<T1*>, T2*> >& l, const QList<QPair<QList<T1*>, T2* > >& expected )
    {
        QCOMPARE( l.count(), expected.count() );
        typename QList<QPair<QList<T1*>, T2*> >::ConstIterator it, end = l.end();
        typename QList<QPair<QList<T1*>, T2*> >::ConstIterator expectedit, expectedend = expected.end();
        for( it = l.begin(), expectedit = expected.begin(); it != end, expectedit != expectedend; it++, expectedit++ )
        {
            checkList( (*it).first, (*expectedit).first );
            expectedStack.push( (*expectedit).second );
            visitNode( (*it).second );
        }
    }
    template <typename T1> void checkPairList( const QList<QPair<QList<T1*>, Python::AssignmentAst::OpType> >& l, const QList<QPair<QList<T1*>, Python::AssignmentAst::OpType> >& expected )
    {
        QCOMPARE( l.count(), expected.count() );
        typename QList<QPair<QList<T1*>, Python::AssignmentAst::OpType> >::ConstIterator it, end = l.end();
        typename QList<QPair<QList<T1*>, Python::AssignmentAst::OpType> >::ConstIterator expectedit, expectedend = expected.end();
        for( it = l.begin(), expectedit = expected.begin(); it != end, expectedit != expectedend; it++, expectedit++ )
        {
            checkList( (*it).first, (*expectedit).first );
            QCOMPARE( (*it).second, (*expectedit).second );
        }
    }
    template <typename T1, typename T2> void checkPairList( const QList<QPair<T1*, T2*> >& l, const QList<QPair<T1*, T2* > >& expected )
    {
        QCOMPARE( l.count(), expected.count() );
        typename QList<QPair<T1*, T2*> >::ConstIterator it, end = l.end();
        typename QList<QPair<T1*, T2*> >::ConstIterator expectedit, expectedend = expected.end();
        for( it = l.begin(), expectedit = expected.begin(); it != end, expectedit != expectedend; it++, expectedit++ )
        {
            expectedStack.push( (*expectedit).first );
            visitNode( (*it).first );
            expectedStack.push( (*expectedit).second );
            visitNode( (*it).second );
        }
    }
    template <typename T> void checkPairList( const QList<QPair<Python::ComparisonAst::ComparisonOperator, T*> >& l,
                                              const QList<QPair<Python::ComparisonAst::ComparisonOperator, T* > >& expected )
    {
        QCOMPARE( l.count(), expected.count() );
        typename QList<QPair<Python::ComparisonAst::ComparisonOperator, T*> >::ConstIterator it, end = l.end();
        typename QList<QPair<Python::ComparisonAst::ComparisonOperator, T*> >::ConstIterator expectedit, expectedend = expected.end();
        for( it = l.begin(), expectedit = expected.begin(); it != end, expectedit != expectedend; it++, expectedit++ )
        {
            QCOMPARE( (*it).first, (*expectedit).first );
            expectedStack.push( (*expectedit).second );
            visitNode( (*it).second );
        }
    }
    template <typename T> void checkNode( T* org, T* expect )
    {
        expectedStack.push( expect );
        visitNode( org );
    }
    template <typename T> void checkOptional( T* org, T* expect )
    {
        if( org && expect )
        {
            checkNode( org, expect );
        }else
        {
            QCOMPARE( org, expect );
        }
    }
    QStack<Python::Ast*> expectedStack;
};

#endif
