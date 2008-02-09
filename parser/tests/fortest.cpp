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

#include "fortest.h"
#include <QtTest/QtTest>
#include <qtest_kde.h>

#include "datahelper.h"


using namespace Python;

Q_DECLARE_METATYPE(CodeAst*)
QTEST_KDEMAIN_CORE( ForTest )


extern CodeAst* simpleForLoop();

ForTest::ForTest( QObject* parent )
    : QObject( parent )
{
}

ForTest::~ForTest()
{
}

void ForTest::basicLoop_data( )
{
    QTest::addColumn<QString>("project");
    QTest::addColumn<CodeAst*>("expected");
    QTest::newRow( "simple for loop" ) << "for i in list:\n  pass\n" << simpleForLoop();
}

void ForTest::basicLoop( )
{
    QFETCH( QString, project );
    QFETCH( CodeAst*, expected );
    doTest( project, expected );
}

