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
#include "testvisitor.h"

using namespace Python;

Q_DECLARE_METATYPE(CodeAst*)
QTEST_MAIN( FunctionDeclarationTest )

extern CodeAst* simpleFunctionSingleParam();
extern CodeAst* simpleFunctionDefaultParam();
extern CodeAst* simpleFunctionListParam();
extern CodeAst* simpleFunctionNoParams();
extern CodeAst* simpleFunctionDictParam();

static void doTest( const QString& project, CodeAst* expected )
{
    Driver d;
    CodeAst* result;
    d.setContent( project );
    d.parse( &result );
    TestVisitor tv;
    tv.setExpected( expected );
    tv.visitCode( result );
}

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
    QFETCH( CodeAst*, expected );
    doTest( project, expected );
}

void FunctionDeclarationTest::noArguments_data( )
{
    QTest::addColumn<QString>("project");
    QTest::addColumn<CodeAst*>("expected");
    QTest::newRow( "simple name" ) << "def foo():\n  pass\n" << simpleFunctionNoParams();
}

void FunctionDeclarationTest::singleArgument()
{
    {
        QFETCH( QString, project );
        QFETCH( CodeAst*, expected );
        doTest( project, expected );
    }
    
    {
        QFETCH( QString, project );
        QFETCH( CodeAst*, expected );
        doTest( project, expected );
        
    }
}

void FunctionDeclarationTest::singleArgument_data()
{
    QTest::addColumn<QString>("project");
    QTest::addColumn<CodeAst*>("expected");
    QTest::newRow( "simple name" ) << "def foo( a ):\n  pass\n" << simpleFunctionSingleParam();
    QTest::newRow( "simple name" ) << "def foo( a='bar' ):\n  pass\n" << simpleFunctionDefaultParam();
    QTest::newRow( "simple name" ) << "def foo( *bar ):\n  pass\n" << simpleFunctionListParam();
    QTest::newRow( "simple name" ) << "def foo( **bar ):\n  pass\n" << simpleFunctionDictParam();
}

#include "functiondeclarationtest.moc"
