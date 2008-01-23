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

#include "functiondeclarationtest.h"

#include <QtTest/QtTest>

#include "ast.h"
#include "pythondriver.h"

Q_DECLARE_METATYPE(Python::CodeAst*)
QTEST_MAIN( FunctionDeclarationTest )

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

FunctionDeclarationTest::FunctionDeclarationTest( QObject* parent )
    : QObject( parent )
{
}

FunctionDeclarationTest::~FunctionDeclarationTest()
{
}

void FunctionDeclarationTest::noArguments( )
{
    QFETCH( QString, project );
    QFETCH( Python::CodeAst*, expected );
    
    Python::Driver d;
    Python::CodeAst* result;
    d.setContent( project );
    d.parse( &result );
    BASIC_AST_TEST( result, expected )
    QCOMPARE( result->statements.count(), expected->statements.count() );
    
}

void FunctionDeclarationTest::noArguments_data( )
{
    QTest::addColumn<QString>("project");
    QTest::addColumn<Python::CodeAst*>("expected");
    Python::CodeAst* ast = new Python::CodeAst();
    ast->start = 0;
    ast->startLine = 0;
    ast->startCol = 0;
    ast->end = 16;
    ast->endLine = 1;
    ast->endCol = 6;
    Python::FunctionDefinitionAst* funast = new Python::FunctionDefinitionAst( ast );
    funast->startLine = 0;
    funast->endLine = 1;
    funast->start = 0;
    funast->startCol = 0;
    funast->endCol = 6;
    funast->end = 16;
    Python::IdentifierAst* idast = new Python::IdentifierAst( funast );
    idast->startLine = 0;
    idast->startCol = 4;
    idast->start = 4;
    idast->endLine = 0;
    idast->endCol = 6;
    idast->end = 6;
    idast->identifier = "foo";
    funast->functionName = idast;
    Python::StatementAst* pass = new Python::StatementAst( funast, Python::Ast::PassAst );
    pass->startLine = 1;
    pass->startCol = 2;
    pass->start = 13;
    pass->end = 16;
    pass->endLine = 1;
    pass->endCol = 5;
    funast->functionBody << pass;
    ast->statements << funast;
    QTest::newRow( "simple name" ) << "def foo():\n  pass\n" << ast;
}

#include "functiondeclarationtest.moc"
