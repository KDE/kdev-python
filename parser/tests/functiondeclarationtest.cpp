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
#include <qtest_kde.h>

#include "ast.h"
#include "datahelper.h"

using namespace Python;

Q_DECLARE_METATYPE(CodeAst*)
QTEST_KDEMAIN_CORE( FunctionDeclarationTest )

extern CodeAst* simpleFunctionSingleParam();
extern CodeAst* simpleFunctionDefaultParam();
extern CodeAst* simpleFunctionListParam();
extern CodeAst* simpleFunctionNoParams();
extern CodeAst* simpleFunctionDictParam();
extern CodeAst* simpleFunctionTwoParam();
extern CodeAst* simpleFunctionTwoLongParam();
extern CodeAst* simpleFunctionListAndDictParam();
extern CodeAst* simpleFunctionCombinedDictParam();
extern CodeAst* simpleFunctionCombinedListParam();

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
    QTest::newRow( "simple function def" ) << "def foo():\n  pass\n" << simpleFunctionNoParams();
}

void FunctionDeclarationTest::singleArgument()
{
    QFETCH( QString, project );
    QFETCH( CodeAst*, expected );
    doTest( project, expected );
}

void FunctionDeclarationTest::singleArgument_data()
{
    QTest::addColumn<QString>("project");
    QTest::addColumn<CodeAst*>("expected");
    QTest::newRow( "simple func one argument" ) << "def foo( a ):\n  pass\n" << simpleFunctionSingleParam();
    QTest::newRow( "simple func one argument with default" ) << "def foo( a='bar' ):\n  pass\n" << simpleFunctionDefaultParam();
    QTest::newRow( "simple func one list argument" ) << "def foo( *bar ):\n  pass\n" << simpleFunctionListParam();
    QTest::newRow( "simple func one dict argument" ) << "def foo( **bar ):\n  pass\n" << simpleFunctionDictParam();
}


void FunctionDeclarationTest::multiArguments()
{
    QFETCH( QString, project );
    QFETCH( CodeAst*, expected );
    doTest( project, expected );
}

void FunctionDeclarationTest::multiArguments_data()
{
    QTest::addColumn<QString>("project");
    QTest::addColumn<CodeAst*>("expected");
    QTest::newRow( "function with two simple params" ) << "def foo( a, b ):\n  pass\n" << simpleFunctionTwoParam();
    QTest::newRow( "function with two longer params" ) << "def foo( alpha, beta ):\n  pass\n" << simpleFunctionTwoLongParam();
}

void FunctionDeclarationTest::combindedArgumentTypes()
{
    QFETCH( QString, project );
    QFETCH( CodeAst*, expected );
    doTest( project, expected );
}

void FunctionDeclarationTest::combindedArgumentTypes_data()
{
    QTest::addColumn<QString>("project");
    QTest::addColumn<CodeAst*>("expected");
    QTest::newRow( "function with an added dict param" ) << "def foo( a, **b ):\n  pass\n" << simpleFunctionCombinedDictParam();
    QTest::newRow( "function with an added list param" ) << "def foo( a, *b ):\n  pass\n" << simpleFunctionCombinedListParam();
    QTest::newRow( "function with added list and dict param" ) << "def foo( a, *b, **c ):\n  pass\n" << simpleFunctionListAndDictParam();
}


#include "functiondeclarationtest.moc"
