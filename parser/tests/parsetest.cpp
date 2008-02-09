/* Python Parser Test
 *
 * Copyright 2007 Andreas Pakulat <apaku@gmx.de>
 *
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
 * 02110-1301, USA.
 */

#include "parsetest.h"
#include "pythondriver.h"

#include <qtest_kde.h>

#include <kdebug.h>

QTEST_KDEMAIN_CORE( ParseTest )

ParseTest::ParseTest( QObject* parent )
    : QObject( parent )
{}

ParseTest::~ParseTest()
{}

void ParseTest::successSimpleSource()
{
    QFETCH( QString, project );
    Python::Driver d;
    d.setContent( project );
    Python::CodeAst* ast = 0;
    bool ret = d.parse( &ast );
    QVERIFY( ret );
}

void ParseTest::successSimpleSource_data()
{
    QTest::addColumn<QString>( "project" );
    QTest::newRow( "row1" ) << "class b:\n  pass\n";
}

void ParseTest::simpleStmtAtEndOfFile()
{
    // @TODO: Fails currently, needs fixing in the grammar, but not easy
    QFETCH( QString, project );
    Python::Driver d;
    d.setContent( project );
    Python::CodeAst* ast = 0;
    bool ret = d.parse( &ast );
    QVERIFY( ret );
}

void ParseTest::simpleStmtAtEndOfFile_data()
{
    QTest::addColumn<QString>( "project" );
    QTest::newRow( "row1" ) << "class b:\n  pass";
}


void ParseTest::successSimpleSourceIndent()
{
    QFETCH( QString, project );
    Python::Driver d;
    d.setContent( project );
    Python::CodeAst* ast = 0;
    bool ret = d.parse( &ast );
    QVERIFY( ret );
}

void ParseTest::successSimpleSourceIndent_data()
{
    QTest::addColumn<QString>( "project" );
    QTest::newRow( "row1" ) << "class b:\n\t  pass\nclass c:\n  \tpass\n";
}

void ParseTest::init()
{
}

void ParseTest::cleanup()
{
}


#include "parsetest.moc"

// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
