/* Python Lexer Test
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

#include "lexertest.h"
#include "pythonlexer.h"
#include "pythonparser.h"

#include <QDebug>

#define MAKETESTROW(str,token,begin,end) \
    str \
    << static_cast<int>(token) \
    << static_cast<qint64>(begin) \
    << static_cast<qint64>(end)

QTEST_MAIN( LexerTest )

LexerTest::LexerTest( QObject* parent )
    : QObject( parent )
{}

LexerTest::~LexerTest()
{}

void LexerTest::lexNumberLiteral()
{
    QFETCH( QString, project );
    QFETCH( int, expectedtoken );
    QFETCH( qint64, expectedbegin );
    QFETCH( qint64, expectedend );
    Python::Lexer l(0, project);
    int token = l.nextTokenKind();
    qint64 begin = qulonglong(l.tokenBegin());
    qint64 end = qulonglong(l.tokenEnd());
//     qDebug() << project << token << expectedtoken << l.tokenBegin() << qulonglong(l.tokenEnd());
    QVERIFY( token == expectedtoken );
    QVERIFY( begin == expectedbegin );
    QVERIFY( end == expectedend );
}

void LexerTest::lexNumberLiteral_data()
{
    QTest::addColumn<QString>( "project" );
    QTest::addColumn<int>( "expectedtoken" );
    QTest::addColumn<qint64>( "expectedbegin" );
    QTest::addColumn<qint64>( "expectedend" );
    //First integers
    QTest::newRow( "row1" )
            << MAKETESTROW( "0", Python::Parser::Token_INTEGER, 0, 0 );
    QTest::newRow( "row2" )
            << MAKETESTROW( "241412403243", Python::Parser::Token_INTEGER, 0, 11 );
    QTest::newRow( "row3" )
            << MAKETESTROW( "240412023243l", Python::Parser::Token_INTEGER, 0, 12 );
    QTest::newRow( "row4" )
            << MAKETESTROW( "241410420243L", Python::Parser::Token_INTEGER, 0, 12 );
    QTest::newRow( "row5" )
            << MAKETESTROW( "0l", Python::Parser::Token_INTEGER, 0, 1 );
    QTest::newRow( "row6" )
            << MAKETESTROW( "0L", Python::Parser::Token_INTEGER, 0, 1 );
    QTest::newRow( "row7" )
            << MAKETESTROW( "000", Python::Parser::Token_INTEGER, 0, 2 );
    QTest::newRow( "row8" )
            << MAKETESTROW( "065", Python::Parser::Token_INTEGER, 0, 2 );
    QTest::newRow( "row9" )
            << MAKETESTROW( "040l", Python::Parser::Token_INTEGER, 0, 3 );
    QTest::newRow( "row10" )
            << MAKETESTROW( "065L", Python::Parser::Token_INTEGER, 0, 3 );
    QTest::newRow( "row11" )
            << MAKETESTROW( "073", Python::Parser::Token_INTEGER, 0, 2 );
    QTest::newRow( "row12" )
            << MAKETESTROW( "089", Python::Parser::Token_INVALID, 0, 2 );
    QTest::newRow( "row13" )
            << MAKETESTROW( "0x00", Python::Parser::Token_INTEGER, 0, 3 );
    QTest::newRow( "row14" )
            << MAKETESTROW( "0x03", Python::Parser::Token_INTEGER, 0, 3 );
    QTest::newRow( "row15" )
            << MAKETESTROW( "0x03Al", Python::Parser::Token_INTEGER, 0, 5 );
    QTest::newRow( "row16" )
            << MAKETESTROW( "0x03AL", Python::Parser::Token_INTEGER, 0, 5 );
    QTest::newRow( "row17" )
            << MAKETESTROW( "0x03JL", Python::Parser::Token_INVALID, 0, 5 );
    // Now floats
    QTest::newRow( "row18" )
            << MAKETESTROW( "03.23", Python::Parser::Token_FLOAT, 0, 4 );
    QTest::newRow( "row19" )
            << MAKETESTROW( ".23", Python::Parser::Token_FLOAT, 0, 2 );
    QTest::newRow( "row20" )
            << MAKETESTROW( "03.", Python::Parser::Token_FLOAT, 0, 2 );
    QTest::newRow( "row21" )
            << MAKETESTROW( "03e34", Python::Parser::Token_FLOAT, 0, 4 );
    QTest::newRow( "row22" )
            << MAKETESTROW( "03E34", Python::Parser::Token_FLOAT, 0, 4 );
    QTest::newRow( "row23" )
            << MAKETESTROW( "03e+34", Python::Parser::Token_FLOAT, 0, 5 );
    QTest::newRow( "row24" )
            << MAKETESTROW( "03e-34", Python::Parser::Token_FLOAT, 0, 5 );
    QTest::newRow( "row25" )
            << MAKETESTROW( "03.23e12", Python::Parser::Token_FLOAT, 0, 7 );
    QTest::newRow( "row26" )
            << MAKETESTROW( ".23E+5", Python::Parser::Token_FLOAT, 0, 5 );
    QTest::newRow( "row27" )
            << MAKETESTROW( "03.e-6", Python::Parser::Token_FLOAT, 0, 5 );
    QTest::newRow( "row29" )
            << MAKETESTROW( "23.23.", Python::Parser::Token_INVALID, 0, 5 );
    QTest::newRow( "row30" )
            << MAKETESTROW( "23.23F4", Python::Parser::Token_INVALID, 0, 6 );
    //Imaginary
    QTest::newRow( "row30" )
            << MAKETESTROW( "23.23e4j", Python::Parser::Token_IMAGNUM, 0, 7 );
    QTest::newRow( "row30" )
            << MAKETESTROW( "23.23e4J", Python::Parser::Token_IMAGNUM, 0, 7 );
    QTest::newRow( "row30" )
            << MAKETESTROW( "2323J", Python::Parser::Token_IMAGNUM, 0, 4 );
    QTest::newRow( "row30" )
            << MAKETESTROW( "0634j", Python::Parser::Token_IMAGNUM, 0, 4 );
}

void LexerTest::lexKeywordAndIdentifier()
{
    QFETCH( QString, project );
    QFETCH( int, expectedtoken );
    QFETCH( qint64, expectedbegin );
    QFETCH( qint64, expectedend );
    Python::Lexer l(0, project);
    int token = l.nextTokenKind();
    qint64 begin = qulonglong(l.tokenBegin());
    qint64 end = qulonglong(l.tokenEnd());
//     qDebug() << project << token << expectedtoken << l.tokenBegin() << qulonglong(l.tokenEnd());
    QVERIFY( token == expectedtoken );
    QVERIFY( begin == expectedbegin );
    QVERIFY( end == expectedend );
}

void LexerTest::lexKeywordAndIdentifier_data()
{
    QTest::addColumn<QString>( "project" );
    QTest::addColumn<int>( "expectedtoken" );
    QTest::addColumn<qint64>( "expectedbegin" );
    QTest::addColumn<qint64>( "expectedend" );
    //first all keywords
    QTest::newRow( "row1" )
            << MAKETESTROW( "and", Python::Parser::Token_AND, 0, 2 );
    QTest::newRow( "row2" )
            << MAKETESTROW( "as", Python::Parser::Token_AS, 0, 1 );
    QTest::newRow( "row3" )
            << MAKETESTROW( "print", Python::Parser::Token_PRINT, 0, 4 );
    QTest::newRow( "row4" )
            << MAKETESTROW( "in", Python::Parser::Token_IN, 0, 1 );
    QTest::newRow( "row5" )
            << MAKETESTROW( "finally", Python::Parser::Token_FINALLY, 0, 6 );
    QTest::newRow( "row6" )
            << MAKETESTROW( "def", Python::Parser::Token_DEF, 0, 2 );
    QTest::newRow( "row7" )
            << MAKETESTROW( "yield", Python::Parser::Token_YIELD, 0, 4 );
    QTest::newRow( "row8" )
            << MAKETESTROW( "continue", Python::Parser::Token_CONTINUE, 0, 7 );
    QTest::newRow( "row9" )
            << MAKETESTROW( "exec", Python::Parser::Token_EXEC, 0, 3 );
    QTest::newRow( "row10" )
            << MAKETESTROW( "import", Python::Parser::Token_IMPORT, 0, 5 );
    QTest::newRow( "row11" )
            << MAKETESTROW( "pass", Python::Parser::Token_PASS, 0, 3 );
    QTest::newRow( "row12" )
            << MAKETESTROW( "while", Python::Parser::Token_WHILE, 0, 4 );
    QTest::newRow( "row13" )
            << MAKETESTROW( "or", Python::Parser::Token_OR, 0, 1 );
    QTest::newRow( "row14" )
            << MAKETESTROW( "if", Python::Parser::Token_IF, 0, 1 );
    QTest::newRow( "row15" )
            << MAKETESTROW( "except", Python::Parser::Token_EXCEPT, 0, 5 );
    QTest::newRow( "row16" )
            << MAKETESTROW( "class", Python::Parser::Token_CLASS, 0, 4 );
    QTest::newRow( "row17" )
            << MAKETESTROW( "try", Python::Parser::Token_TRY, 0, 2 );
    QTest::newRow( "row18" )
            << MAKETESTROW( "not", Python::Parser::Token_NOT, 0, 2 );
    QTest::newRow( "row19" )
            << MAKETESTROW( "del", Python::Parser::Token_DEL, 0, 2 );
    QTest::newRow( "row20" )
            << MAKETESTROW( "for", Python::Parser::Token_FOR, 0, 2 );
    QTest::newRow( "row21" )
            << MAKETESTROW( "is", Python::Parser::Token_IS, 0, 1 );
    QTest::newRow( "row22" )
            << MAKETESTROW( "raise", Python::Parser::Token_RAISE, 0, 4 );
    QTest::newRow( "row23" )
            << MAKETESTROW( "assert", Python::Parser::Token_ASSERT, 0, 5 );
    QTest::newRow( "row24" )
            << MAKETESTROW( "elif", Python::Parser::Token_ELIF, 0, 3 );
    QTest::newRow( "row25" )
            << MAKETESTROW( "from", Python::Parser::Token_FROM, 0, 3 );
    QTest::newRow( "row26" )
            << MAKETESTROW( "lambda", Python::Parser::Token_LAMBDA, 0, 5 );
    QTest::newRow( "row27" )
            << MAKETESTROW( "return", Python::Parser::Token_RETURN, 0, 5 );
    QTest::newRow( "row28" )
            << MAKETESTROW( "break", Python::Parser::Token_BREAK, 0, 4 );
    QTest::newRow( "row29" )
            << MAKETESTROW( "else", Python::Parser::Token_ELSE, 0, 3 );
    QTest::newRow( "row30" )
            << MAKETESTROW( "global", Python::Parser::Token_GLOBAL, 0, 5 );
    //Now check that anything else is an identifier
    QTest::newRow( "row31" )
            << MAKETESTROW( "globally", Python::Parser::Token_IDENTIFIER, 0, 7 );
    QTest::newRow( "row32" )
            << MAKETESTROW( "_globall45y", Python::Parser::Token_IDENTIFIER, 0, 10 );
}

void LexerTest::lexSeparatorsAndOperators()
{
    QFETCH( QString, project );
    QFETCH( int, expectedtoken );
    QFETCH( qint64, expectedbegin );
    QFETCH( qint64, expectedend );
    Python::Lexer l(0, project);
    int token = l.nextTokenKind();
    qint64 begin = qulonglong(l.tokenBegin());
    qint64 end = qulonglong(l.tokenEnd());
//     qDebug() << project << token << expectedtoken << l.tokenBegin() << qulonglong(l.tokenEnd());
    QVERIFY( token == expectedtoken );
    QVERIFY( begin == expectedbegin );
    QVERIFY( end == expectedend );
}

void LexerTest::lexSeparatorsAndOperators_data()
{
    QTest::addColumn<QString>( "project" );
    QTest::addColumn<int>( "expectedtoken" );
    QTest::addColumn<qint64>( "expectedbegin" );
    QTest::addColumn<qint64>( "expectedend" );
    QTest::newRow( "row1" )
            << MAKETESTROW( "(", Python::Parser::Token_LPAREN, 0, 0 );
    QTest::newRow( "row2" )
            << MAKETESTROW( "(as", Python::Parser::Token_LPAREN, 0, 0 );
    QTest::newRow( "row3" )
            << MAKETESTROW( ")", Python::Parser::Token_RPAREN, 0, 0 );
    QTest::newRow( "row4" )
            << MAKETESTROW( "{", Python::Parser::Token_LBRACE, 0, 0 );
    QTest::newRow( "row5" )
            << MAKETESTROW( "}", Python::Parser::Token_RBRACE, 0, 0 );
    QTest::newRow( "row6" )
            << MAKETESTROW( "[", Python::Parser::Token_LBRACKET, 0, 0 );
    QTest::newRow( "row7" )
            << MAKETESTROW( "]", Python::Parser::Token_RBRACKET, 0, 0 );
    QTest::newRow( "row8" )
            << MAKETESTROW( ",", Python::Parser::Token_COMMA, 0, 0 );
    QTest::newRow( "row9" )
            << MAKETESTROW( ";", Python::Parser::Token_SEMICOLON, 0, 0 );
    QTest::newRow( "row10" )
            << MAKETESTROW( ":", Python::Parser::Token_COLON, 0, 0 );
    QTest::newRow( "row11" )
            << MAKETESTROW( ".", Python::Parser::Token_DOT, 0, 0 );
    QTest::newRow( "row12" )
            << MAKETESTROW( "`", Python::Parser::Token_BACKTICK, 0, 0 );
    QTest::newRow( "row13" )
            << MAKETESTROW( "@", Python::Parser::Token_AT, 0, 0 );
    QTest::newRow( "row14" )
            << MAKETESTROW( "...", Python::Parser::Token_ELLIPSIS, 0, 2 );
    QTest::newRow( "row15" )
            << MAKETESTROW( "*", Python::Parser::Token_STAR, 0, 0 );
    QTest::newRow( "row16" )
            << MAKETESTROW( "**", Python::Parser::Token_DOUBLESTAR, 0, 1 );
    QTest::newRow( "row17" )
            << MAKETESTROW( "=", Python::Parser::Token_EQUAL, 0, 0 );
    QTest::newRow( "row18" )
            << MAKETESTROW( "+", Python::Parser::Token_PLUS, 0, 0 );
    QTest::newRow( "row19" )
            << MAKETESTROW( "-", Python::Parser::Token_MINUS, 0, 0 );
    QTest::newRow( "row20" )
            << MAKETESTROW( "~", Python::Parser::Token_TILDE, 0, 0 );
    QTest::newRow( "row21" )
            << MAKETESTROW( "/", Python::Parser::Token_SLASH, 0, 0 );
    QTest::newRow( "row22" )
            << MAKETESTROW( "//", Python::Parser::Token_DOUBLESLASH, 0, 1 );
    QTest::newRow( "row23" )
            << MAKETESTROW( "%", Python::Parser::Token_MODULO, 0, 0 );
    QTest::newRow( "row24" )
            << MAKETESTROW( "&", Python::Parser::Token_ANDD, 0, 0 );
    QTest::newRow( "row25" )
            << MAKETESTROW( "<<", Python::Parser::Token_LSHIFT, 0, 1 );
    QTest::newRow( "row26" )
            << MAKETESTROW( ">>", Python::Parser::Token_RSHIFT, 0, 1 );
    QTest::newRow( "row27" )
            << MAKETESTROW( "+=", Python::Parser::Token_PLUSEQ, 0, 1 );
    QTest::newRow( "row28" )
            << MAKETESTROW( "-=", Python::Parser::Token_MINUSEQ, 0, 1 );
    QTest::newRow( "row29" )
            << MAKETESTROW( "/=", Python::Parser::Token_SLASHEQ, 0, 1 );
    QTest::newRow( "row30" )
            << MAKETESTROW( "//=", Python::Parser::Token_DOUBLESLASHEQ, 0, 2 );
    QTest::newRow( "row31" )
            << MAKETESTROW( "%=", Python::Parser::Token_MODULOEQ, 0, 1 );
    QTest::newRow( "row32" )
            << MAKETESTROW( "&=", Python::Parser::Token_ANDEQ, 0, 1 );
    QTest::newRow( "row33" )
            << MAKETESTROW( "*=", Python::Parser::Token_STAREQ, 0, 1 );
    QTest::newRow( "row34" )
            << MAKETESTROW( "~=", Python::Parser::Token_TILDEEQ, 0, 1 );
    QTest::newRow( "row35" )
            << MAKETESTROW( "|=", Python::Parser::Token_OREQ, 0, 1 );
    QTest::newRow( "row36" )
            << MAKETESTROW( "**=", Python::Parser::Token_DOUBLESTAREQ, 0, 2 );
    QTest::newRow( "row37" )
            << MAKETESTROW( "<<=", Python::Parser::Token_LSHIFTEQ, 0, 2 );
    QTest::newRow( "row38" )
            << MAKETESTROW( ">>=", Python::Parser::Token_RSHIFTEQ, 0, 2 );
    QTest::newRow( "row39" )
            << MAKETESTROW( "<", Python::Parser::Token_LESS, 0, 0 );
    QTest::newRow( "row40" )
            << MAKETESTROW( ">", Python::Parser::Token_GREATER, 0, 0 );
    QTest::newRow( "row41" )
            << MAKETESTROW( "<=", Python::Parser::Token_LESSEQ, 0, 1 );
    QTest::newRow( "row42" )
            << MAKETESTROW( ">=", Python::Parser::Token_GREATEREQ, 0, 1 );
    QTest::newRow( "row43" )
            << MAKETESTROW( "<>", Python::Parser::Token_UNEQUAL, 0, 1 );
    QTest::newRow( "row44" )
            << MAKETESTROW( "!=", Python::Parser::Token_UNEQUAL, 0, 1 );
    QTest::newRow( "row45" )
            << MAKETESTROW( "|", Python::Parser::Token_ORR, 0, 0 );
    QTest::newRow( "row46" )
            << MAKETESTROW( "^", Python::Parser::Token_HAT, 0, 0 );
    QTest::newRow( "row47" )
            << MAKETESTROW( "==", Python::Parser::Token_ISEQUAL, 0, 1 );
}

void LexerTest::lexIndentation()
{
    QFETCH( QString, project );
    QFETCH( QList<QVariant>, expectedtokens );
    QFETCH( QList<QVariant>, expectedbegins );
    QFETCH( QList<QVariant>, expectedends );
    Python::Lexer l(0, project);
    QList<QVariant> tokens;
    QList<QVariant> begins;
    QList<QVariant> ends;
    int token = 0;
    do
    {
        token = l.nextTokenKind();
        tokens << token;
        begins << qulonglong(l.tokenBegin());
        ends << qulonglong(l.tokenEnd());
    }while( token != 0 );
    tokens.removeLast();
    begins.removeLast();
    ends.removeLast();

//     qDebug() << project;
//     qDebug() << tokens << expectedtokens;
//     qDebug() << begins << expectedbegins;
//     qDebug() << ends << expectedends;
    QVERIFY( tokens == expectedtokens );
    QVERIFY( begins == expectedbegins );
    QVERIFY( ends == expectedends );
}

void LexerTest::lexIndentation_data()
{
    QTest::addColumn<QString>( "project" );
    QTest::addColumn< QList<QVariant> >( "expectedtokens" );
    QTest::addColumn< QList<QVariant> >( "expectedbegins" );
    QTest::addColumn< QList<QVariant> >( "expectedends" );
    QList<QVariant> expectedtokens;
    expectedtokens << Python::Parser::Token_INDENT;
    expectedtokens << Python::Parser::Token_IDENTIFIER;
    expectedtokens << Python::Parser::Token_LINEBREAK;
    expectedtokens << Python::Parser::Token_INDENT;
    expectedtokens << Python::Parser::Token_IDENTIFIER;
    expectedtokens << Python::Parser::Token_LINEBREAK;
    expectedtokens << Python::Parser::Token_DEDENT;
    expectedtokens << Python::Parser::Token_IDENTIFIER;
    expectedtokens << Python::Parser::Token_DEDENT;
    QList<QVariant> expectedbegins;
    QList<QVariant> expectedends;
    expectedbegins << qulonglong(0) << qulonglong(2) << qulonglong(5) << qulonglong(6) << qulonglong(10) << qulonglong(13) << qulonglong(14) << qulonglong(16) << -1;
    expectedends << qulonglong(1) << qulonglong(4) << qulonglong(5) << qulonglong(9) << qulonglong(12) << qulonglong(13) << qulonglong(15) << qulonglong(18) << -1;
    QTest::newRow( "row1" )
            << "  foo\n    bar\n  baz" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::Parser::Token_INDENT;
    expectedtokens << Python::Parser::Token_IDENTIFIER;
    expectedtokens << Python::Parser::Token_LINEBREAK;
    expectedtokens << Python::Parser::Token_LINEBREAK;
    expectedtokens << Python::Parser::Token_IDENTIFIER;
    expectedtokens << Python::Parser::Token_DEDENT;
    expectedbegins << qulonglong(0) << qulonglong(2) << qulonglong(5) << qulonglong(14) << qulonglong(17) << -1;
    expectedends << qulonglong(1) << qulonglong(4) << qulonglong(5) << qulonglong(14) << qulonglong(19) << -1;
    QTest::newRow( "row2" )
            << "  foo\n#    bar\n  baz" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::Parser::Token_INDENT;
    expectedtokens << Python::Parser::Token_IDENTIFIER;
    expectedtokens << Python::Parser::Token_LINEBREAK;
    expectedtokens << Python::Parser::Token_INDENT;
    expectedtokens << Python::Parser::Token_IDENTIFIER;
    expectedtokens << Python::Parser::Token_LINEBREAK;
    expectedtokens << Python::Parser::Token_DEDENT;
    expectedtokens << Python::Parser::Token_DEDENT;
    expectedtokens << Python::Parser::Token_IDENTIFIER;
    expectedbegins << qulonglong(0) << qulonglong(2) << qulonglong(5) << qulonglong(6) << qulonglong(10) << qulonglong(13) << -1 << -1 << qulonglong(14);
    expectedends << qulonglong(1) << qulonglong(4) << qulonglong(5) << qulonglong(9) << qulonglong(12) << qulonglong(13) << -1 << -1 << qulonglong(16);
    QTest::newRow( "row3" )
            << "  foo\n    bar\nbaz" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::Parser::Token_INDENT;
    expectedtokens << Python::Parser::Token_IDENTIFIER;
    expectedtokens << Python::Parser::Token_LINEBREAK;
    expectedtokens << Python::Parser::Token_LINEBREAK;
    expectedtokens << Python::Parser::Token_DEDENT;
    expectedtokens << Python::Parser::Token_IDENTIFIER;
    expectedbegins << qulonglong(0) << qulonglong(2) << qulonglong(5) << qulonglong(14) << -1 << qulonglong(15);
    expectedends << qulonglong(1) << qulonglong(4) << qulonglong(5) << qulonglong(14) << -1 << qulonglong(17);
    QTest::newRow( "row4" )
            << "  foo\n    #bar\nbaz" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::Parser::Token_IDENTIFIER;
    expectedtokens << Python::Parser::Token_LINEBREAK;
    expectedtokens << Python::Parser::Token_INDENT;
    expectedtokens << Python::Parser::Token_IDENTIFIER;
    expectedtokens << Python::Parser::Token_LINEBREAK;
    expectedtokens << Python::Parser::Token_DEDENT;
    expectedtokens << Python::Parser::Token_IDENTIFIER;
    expectedbegins << qulonglong(0) << qulonglong(3) << qulonglong(4) << qulonglong(8) << qulonglong(11) << qulonglong(12) << qulonglong(14);
    expectedends << qulonglong(2) << qulonglong(3) << qulonglong(7) << qulonglong(10) << qulonglong(11) << qulonglong(13) << qulonglong(16);
    QTest::newRow( "row5" )
            << "foo\n    bar\n  baz" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::Parser::Token_IDENTIFIER;
    expectedtokens << Python::Parser::Token_LINEBREAK;
    expectedtokens << Python::Parser::Token_INDENT;
    expectedtokens << Python::Parser::Token_IDENTIFIER;
    expectedtokens << Python::Parser::Token_LINEBREAK;
    expectedtokens << Python::Parser::Token_INDENT;
    expectedtokens << Python::Parser::Token_IDENTIFIER;
    expectedtokens << Python::Parser::Token_LINEBREAK;
    expectedtokens << Python::Parser::Token_INDENT;
    expectedtokens << Python::Parser::Token_IDENTIFIER;
    expectedtokens << Python::Parser::Token_LINEBREAK;
    expectedtokens << Python::Parser::Token_DEDENT;
    expectedtokens << Python::Parser::Token_DEDENT;
    expectedtokens << Python::Parser::Token_DEDENT;
    expectedtokens << Python::Parser::Token_IDENTIFIER;
    expectedbegins << qulonglong(0) << qulonglong(3) << qulonglong(4) << qulonglong(8) << qulonglong(11) << qulonglong(12) << qulonglong(18) << qulonglong(21) << qulonglong(22) << qulonglong(30) << qulonglong(33) << -1 << -1 << -1 << qulonglong(34);
    expectedends << qulonglong(2) << qulonglong(3) << qulonglong(7) << qulonglong(10) << qulonglong(11) << qulonglong(17) << qulonglong(20) << qulonglong(21) << qulonglong(29) << qulonglong(32) << qulonglong(33) << -1 << -1 << -1 << qulonglong(36);
    QTest::newRow( "row6" )
            << "foo\n    bar\n      baz\n        bak\nbor" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::Parser::Token_INDENT;
    expectedtokens << Python::Parser::Token_IDENTIFIER;
    expectedtokens << Python::Parser::Token_EQUAL;
    expectedtokens << Python::Parser::Token_LBRACKET;
    expectedtokens << Python::Parser::Token_RBRACKET;
    expectedtokens << Python::Parser::Token_LINEBREAK;
    expectedtokens << Python::Parser::Token_DEDENT;
    expectedtokens << Python::Parser::Token_IDENTIFIER;
    expectedbegins << qulonglong(0) << qulonglong(2) << qulonglong(5) << qulonglong(6) << qulonglong(17) << qulonglong(18) << -1 << qulonglong(19);
    expectedends << qulonglong(1) << qulonglong(4) << qulonglong(5) << qulonglong(6) << qulonglong(17) << qulonglong(18) << -1 << qulonglong(21);
    QTest::newRow( "row7" )
            << "  foo=[\n    #bar\n]\nbaz" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::Parser::Token_INDENT;
    expectedtokens << Python::Parser::Token_IDENTIFIER;
    expectedtokens << Python::Parser::Token_EQUAL;
    expectedtokens << Python::Parser::Token_LBRACKET;
    expectedtokens << Python::Parser::Token_LBRACE;
    expectedtokens << Python::Parser::Token_RBRACE;
    expectedtokens << Python::Parser::Token_RBRACKET;
    expectedtokens << Python::Parser::Token_LINEBREAK;
    expectedtokens << Python::Parser::Token_DEDENT;
    expectedtokens << Python::Parser::Token_IDENTIFIER;
    expectedbegins << qulonglong(0) << qulonglong(2) << qulonglong(5) << qulonglong(6) << qulonglong(9) << qulonglong(12) << qulonglong(21) << qulonglong(22) << -1 << qulonglong(23);
    expectedends << qulonglong(1) << qulonglong(4) << qulonglong(5) << qulonglong(6) << qulonglong(9) << qulonglong(12) << qulonglong(21) << qulonglong(22) << -1 << qulonglong(25);
    QTest::newRow( "row8" )
            << "  foo=[\n {  }   #bar\n]\nbaz" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::Parser::Token_INDENT;
    expectedtokens << Python::Parser::Token_IDENTIFIER;
    expectedtokens << Python::Parser::Token_LINEBREAK;
    expectedtokens << Python::Parser::Token_LINEBREAK;
    expectedtokens << Python::Parser::Token_IDENTIFIER;
    expectedtokens << Python::Parser::Token_DEDENT;
    expectedbegins << qulonglong(0) << qulonglong(2) << qulonglong(5) << qulonglong(10) << qulonglong(13) << -1;
    expectedends << qulonglong(1) << qulonglong(4) << qulonglong(5) << qulonglong(10) << qulonglong(15) << -1;
    QTest::newRow( "row9" )
            << "  foo\n    \n  baz" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::Parser::Token_INDENT;
    expectedtokens << Python::Parser::Token_IDENTIFIER;
    expectedtokens << Python::Parser::Token_LINEBREAK;
    expectedtokens << Python::Parser::Token_IDENTIFIER;
    expectedtokens << Python::Parser::Token_LINEBREAK;
    expectedtokens << Python::Parser::Token_IDENTIFIER;
    expectedtokens << Python::Parser::Token_DEDENT;
    expectedbegins << qulonglong(0) << qulonglong(3) << qulonglong(6) << qulonglong(15) << qulonglong(18) << qulonglong(26) << -1;
    expectedends << qulonglong(2) << qulonglong(5) << qulonglong(6) << qulonglong(17) << qulonglong(18) << qulonglong(28) << -1;
    QTest::newRow( "row10" )
            << "  \tfoo\n        boo\n      \tbaz" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::Parser::Token_INDENT;
    expectedtokens << Python::Parser::Token_IDENTIFIER;
    expectedtokens << Python::Parser::Token_LINEBREAK;
    expectedtokens << Python::Parser::Token_INDENT;
    expectedtokens << Python::Parser::Token_IDENTIFIER;
    expectedtokens << Python::Parser::Token_LINEBREAK;
    expectedtokens << Python::Parser::Token_DEDENT;
    expectedtokens << Python::Parser::Token_IDENTIFIER;
    expectedtokens << Python::Parser::Token_DEDENT;
    expectedbegins << qulonglong(0) << qulonglong(3) << qulonglong(6) << qulonglong(7) << qulonglong(16) << qulonglong(19) << qulonglong(20) << qulonglong(23) << -1;
    expectedends << qulonglong(2) << qulonglong(5) << qulonglong(6) << qulonglong(15) << qulonglong(18) << qulonglong(19) << qulonglong(22) << qulonglong(25) << -1;
    QTest::newRow( "row11" )
            << "  \tfoo\n        \tboo\n  \tbaz" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::Parser::Token_INDENT;
    expectedtokens << Python::Parser::Token_IDENTIFIER;
    expectedtokens << Python::Parser::Token_EQUAL;
    expectedtokens << Python::Parser::Token_LBRACKET;
    expectedtokens << Python::Parser::Token_IDENTIFIER;
    expectedtokens << Python::Parser::Token_RBRACKET;
    expectedtokens << Python::Parser::Token_DEDENT;
    expectedbegins << qulonglong(0) << qulonglong(2) << qulonglong(5) << qulonglong(6) << qulonglong(14) << qulonglong(18) << -1;
    expectedends << qulonglong(1) << qulonglong(4) << qulonglong(5) << qulonglong(6) << qulonglong(16) << qulonglong(18) << -1;
    QTest::newRow( "row7" )
            << "  foo=[\n  \\\n  bar\n]" << expectedtokens << expectedbegins << expectedends;
}

void LexerTest::lexStringLiteral()
{
    QFETCH( QString, project );
    QFETCH( QList<QVariant>, expectedtokens );
    QFETCH( QList<QVariant>, expectedbegins );
    QFETCH( QList<QVariant>, expectedends );
    Python::Lexer l(0, project);
    QList<QVariant> tokens;
    QList<QVariant> begins;
    QList<QVariant> ends;
    int token = 0;
    do
    {
        token = l.nextTokenKind();
        tokens << token;
        begins << qulonglong(l.tokenBegin());
        ends << qulonglong(l.tokenEnd());
    }while( token != 0 );
    tokens.removeLast();
    begins.removeLast();
    ends.removeLast();

//     qDebug() << project;
//     qDebug() << tokens << expectedtokens;
//     qDebug() << begins << expectedbegins;
//     qDebug() << ends << expectedends;
    QVERIFY( tokens == expectedtokens );
    QVERIFY( begins == expectedbegins );
    QVERIFY( ends == expectedends );
}

void LexerTest::lexStringLiteral_data()
{
    QTest::addColumn<QString>( "project" );
    QTest::addColumn< QList<QVariant> >( "expectedtokens" );
    QTest::addColumn< QList<QVariant> >( "expectedbegins" );
    QTest::addColumn< QList<QVariant> >( "expectedends" );
    QList<QVariant> expectedtokens;
    expectedtokens << Python::Parser::Token_STRINGLITERAL;
    QList<QVariant> expectedbegins;
    QList<QVariant> expectedends;
    expectedbegins << qulonglong(0);
    expectedends << qulonglong(22);
    QTest::newRow( "row1" )
            << "'''foo\n    bar\n  baz'''" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::Parser::Token_STRINGLITERAL;
    expectedbegins << qulonglong(0);
    expectedends << qulonglong(23);
    QTest::newRow( "row2" )
            << "\"\"\"foo\n#    bar\n  baz\"\"\"" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::Parser::Token_STRINGLITERAL;
    expectedbegins << qulonglong(0);
    expectedends << qulonglong(27);
    QTest::newRow( "row3" )
            << "\"\"\"foo\n#  ''''  bar\n  baz\"\"\"" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::Parser::Token_STRINGLITERAL;
    expectedbegins << qulonglong(0);
    expectedends << qulonglong(27);
    QTest::newRow( "row4" )
            << "'''foo\n# \"\"\"\"   bar\n  baz'''" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::Parser::Token_STRINGLITERAL;
    expectedbegins << qulonglong(0);
    expectedends << qulonglong(20);
    QTest::newRow( "row5" )
            << "\"\"\"foo\n#    bar\n  baz" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::Parser::Token_STRINGLITERAL;
    expectedbegins << qulonglong(0);
    expectedends << qulonglong(27);
    QTest::newRow( "row6" )
            << "\"\"\"foo\n#   \\\"\"\" bar\n  baz\"\"\"" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::Parser::Token_STRINGLITERAL;
    expectedtokens << Python::Parser::Token_STRINGLITERAL;
    expectedbegins << qulonglong(0) << qulonglong(17);
    expectedends << qulonglong(13) << qulonglong(25);
    QTest::newRow( "row7" )
            << "\"\"\"foo\n#   \"\"\"\n  \"\"\"baz\"\"\"" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::Parser::Token_STRINGLITERAL;
    expectedbegins << qulonglong(0);
    expectedends << qulonglong(18);
    QTest::newRow( "row8" )
            << "\"foo#    bar6  baz\"" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::Parser::Token_STRINGLITERAL;
    expectedbegins << qulonglong(0);
    expectedends << qulonglong(17);
    QTest::newRow( "row9" )
            << "'foo#    bar  baz'" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::Parser::Token_STRINGLITERAL;
    expectedtokens << Python::Parser::Token_LINEBREAK;
    expectedbegins << qulonglong(0) << qulonglong(4);
    expectedends << qulonglong(3) << qulonglong(4);
    QTest::newRow( "row10" )
            << "'foo\n" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::Parser::Token_STRINGLITERAL;
    expectedtokens << Python::Parser::Token_STRINGLITERAL;
    expectedbegins << qulonglong(0) << qulonglong(10);
    expectedends << qulonglong(4) << qulonglong(14);
    QTest::newRow( "row11" )
            << "'foo'\n    'bar'" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::Parser::Token_STRINGLITERAL;
    expectedtokens << Python::Parser::Token_STRINGLITERAL;
    expectedbegins << qulonglong(0) << qulonglong(17);
    expectedends << qulonglong(13) << qulonglong(21);
    QTest::newRow( "row12" )
            << "\"\"\"foo\n#   \"\"\"\n  'baz'" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::Parser::Token_STRINGLITERAL;
    expectedbegins << qulonglong(0);
    expectedends << qulonglong(5);
    QTest::newRow( "row13" )
            << "u'foo'" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::Parser::Token_STRINGLITERAL;
    expectedbegins << qulonglong(0);
    expectedends << qulonglong(5);
    QTest::newRow( "row14" )
            << "r'foo'" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::Parser::Token_STRINGLITERAL;
    expectedbegins << qulonglong(0);
    expectedends << qulonglong(5);
    QTest::newRow( "row15" )
            << "R'foo'" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::Parser::Token_STRINGLITERAL;
    expectedbegins << qulonglong(0);
    expectedends << qulonglong(6);
    QTest::newRow( "row16" )
            << "uR'foo'" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::Parser::Token_STRINGLITERAL;
    expectedbegins << qulonglong(0);
    expectedends << qulonglong(1);
    QTest::newRow( "row17" )
            << "''" << expectedtokens << expectedbegins << expectedends;
}

void LexerTest::init()
{
}

void LexerTest::cleanup()
{
}


#include "lexertest.moc"

// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
