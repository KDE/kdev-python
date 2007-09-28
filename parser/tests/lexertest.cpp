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
#include "python_parser.h"

#include <QDebug>

#define MAX_SIZE_T qulonglong(std::numeric_limits<std::size_t>::max())

#define MAKETESTROW(str,token,begin,end) \
    str \
    << static_cast<int>(token) \
    << static_cast<std::size_t>(begin) \
    << static_cast<std::size_t>(end)

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
    QFETCH( std::size_t, expectedbegin );
    QFETCH( std::size_t, expectedend );
    Python::Lexer l(0, project);
    int token = l.nextTokenKind();
    std::size_t begin = qulonglong(l.tokenBegin());
    std::size_t end = qulonglong(l.tokenEnd());
//     qDebug() << project << token << expectedtoken << l.tokenBegin() << qulonglong(l.tokenEnd());
    QVERIFY( token == expectedtoken );
    QVERIFY( begin == expectedbegin );
    QVERIFY( end == expectedend );
}

void LexerTest::lexNumberLiteral_data()
{
    QTest::addColumn<QString>( "project" );
    QTest::addColumn<int>( "expectedtoken" );
    QTest::addColumn<std::size_t>( "expectedbegin" );
    QTest::addColumn<std::size_t>( "expectedend" );
    //First integers
    QTest::newRow( "row1" )
            << MAKETESTROW( "0", Python::parser::Token_INTEGER, 0, 0 );
    QTest::newRow( "row2" )
            << MAKETESTROW( "241412403243", Python::parser::Token_INTEGER, 0, 11 );
    QTest::newRow( "row3" )
            << MAKETESTROW( "240412023243l", Python::parser::Token_INTEGER, 0, 12 );
    QTest::newRow( "row4" )
            << MAKETESTROW( "241410420243L", Python::parser::Token_INTEGER, 0, 12 );
    QTest::newRow( "row5" )
            << MAKETESTROW( "0l", Python::parser::Token_INTEGER, 0, 1 );
    QTest::newRow( "row6" )
            << MAKETESTROW( "0L", Python::parser::Token_INTEGER, 0, 1 );
    QTest::newRow( "row7" )
            << MAKETESTROW( "000", Python::parser::Token_INTEGER, 0, 2 );
    QTest::newRow( "row8" )
            << MAKETESTROW( "065", Python::parser::Token_INTEGER, 0, 2 );
    QTest::newRow( "row9" )
            << MAKETESTROW( "040l", Python::parser::Token_INTEGER, 0, 3 );
    QTest::newRow( "row10" )
            << MAKETESTROW( "065L", Python::parser::Token_INTEGER, 0, 3 );
    QTest::newRow( "row11" )
            << MAKETESTROW( "073", Python::parser::Token_INTEGER, 0, 2 );
    QTest::newRow( "row12" )
            << MAKETESTROW( "089", Python::parser::Token_INVALID, 0, 2 );
    QTest::newRow( "row13" )
            << MAKETESTROW( "0x00", Python::parser::Token_INTEGER, 0, 3 );
    QTest::newRow( "row14" )
            << MAKETESTROW( "0x03", Python::parser::Token_INTEGER, 0, 3 );
    QTest::newRow( "row15" )
            << MAKETESTROW( "0x03Al", Python::parser::Token_INTEGER, 0, 5 );
    QTest::newRow( "row16" )
            << MAKETESTROW( "0x03AL", Python::parser::Token_INTEGER, 0, 5 );
    QTest::newRow( "row17" )
            << MAKETESTROW( "0x03JL", Python::parser::Token_INVALID, 0, 5 );
    // Now floats
    QTest::newRow( "row18" )
            << MAKETESTROW( "03.23", Python::parser::Token_FLOAT, 0, 4 );
    QTest::newRow( "row19" )
            << MAKETESTROW( ".23", Python::parser::Token_FLOAT, 0, 2 );
    QTest::newRow( "row20" )
            << MAKETESTROW( "03.", Python::parser::Token_FLOAT, 0, 2 );
    QTest::newRow( "row21" )
            << MAKETESTROW( "03e34", Python::parser::Token_FLOAT, 0, 4 );
    QTest::newRow( "row22" )
            << MAKETESTROW( "03E34", Python::parser::Token_FLOAT, 0, 4 );
    QTest::newRow( "row23" )
            << MAKETESTROW( "03e+34", Python::parser::Token_FLOAT, 0, 5 );
    QTest::newRow( "row24" )
            << MAKETESTROW( "03e-34", Python::parser::Token_FLOAT, 0, 5 );
    QTest::newRow( "row25" )
            << MAKETESTROW( "03.23e12", Python::parser::Token_FLOAT, 0, 7 );
    QTest::newRow( "row26" )
            << MAKETESTROW( ".23E+5", Python::parser::Token_FLOAT, 0, 5 );
    QTest::newRow( "row27" )
            << MAKETESTROW( "03.e-6", Python::parser::Token_FLOAT, 0, 5 );
    QTest::newRow( "row29" )
            << MAKETESTROW( "23.23.", Python::parser::Token_INVALID, 0, 5 );
    QTest::newRow( "row30" )
            << MAKETESTROW( "23.23F4", Python::parser::Token_INVALID, 0, 6 );
    //Imaginary
    QTest::newRow( "row30" )
            << MAKETESTROW( "23.23e4j", Python::parser::Token_IMAGNUM, 0, 7 );
    QTest::newRow( "row30" )
            << MAKETESTROW( "23.23e4J", Python::parser::Token_IMAGNUM, 0, 7 );
    QTest::newRow( "row30" )
            << MAKETESTROW( "2323J", Python::parser::Token_IMAGNUM, 0, 4 );
    QTest::newRow( "row30" )
            << MAKETESTROW( "0634j", Python::parser::Token_IMAGNUM, 0, 4 );
}

void LexerTest::lexKeywordAndIdentifier()
{
    QFETCH( QString, project );
    QFETCH( int, expectedtoken );
    QFETCH( std::size_t, expectedbegin );
    QFETCH( std::size_t, expectedend );
    Python::Lexer l(0, project);
    int token = l.nextTokenKind();
    std::size_t begin = qulonglong(l.tokenBegin());
    std::size_t end = qulonglong(l.tokenEnd());
//     qDebug() << project << token << expectedtoken << l.tokenBegin() << qulonglong(l.tokenEnd());
    QVERIFY( token == expectedtoken );
    QVERIFY( begin == expectedbegin );
    QVERIFY( end == expectedend );
}

void LexerTest::lexKeywordAndIdentifier_data()
{
    QTest::addColumn<QString>( "project" );
    QTest::addColumn<int>( "expectedtoken" );
    QTest::addColumn<std::size_t>( "expectedbegin" );
    QTest::addColumn<std::size_t>( "expectedend" );
    //first all keywords
    QTest::newRow( "row1" )
            << MAKETESTROW( "and", Python::parser::Token_AND, 0, 2 );
    QTest::newRow( "row2" )
            << MAKETESTROW( "as", Python::parser::Token_AS, 0, 1 );
    QTest::newRow( "row3" )
            << MAKETESTROW( "print", Python::parser::Token_PRINT, 0, 4 );
    QTest::newRow( "row4" )
            << MAKETESTROW( "in", Python::parser::Token_IN, 0, 1 );
    QTest::newRow( "row5" )
            << MAKETESTROW( "finally", Python::parser::Token_FINALLY, 0, 6 );
    QTest::newRow( "row6" )
            << MAKETESTROW( "def", Python::parser::Token_DEF, 0, 2 );
    QTest::newRow( "row7" )
            << MAKETESTROW( "yield", Python::parser::Token_YIELD, 0, 4 );
    QTest::newRow( "row8" )
            << MAKETESTROW( "continue", Python::parser::Token_CONTINUE, 0, 7 );
    QTest::newRow( "row9" )
            << MAKETESTROW( "exec", Python::parser::Token_EXEC, 0, 3 );
    QTest::newRow( "row10" )
            << MAKETESTROW( "import", Python::parser::Token_IMPORT, 0, 5 );
    QTest::newRow( "row11" )
            << MAKETESTROW( "pass", Python::parser::Token_PASS, 0, 3 );
    QTest::newRow( "row12" )
            << MAKETESTROW( "while", Python::parser::Token_WHILE, 0, 4 );
    QTest::newRow( "row13" )
            << MAKETESTROW( "or", Python::parser::Token_OR, 0, 1 );
    QTest::newRow( "row14" )
            << MAKETESTROW( "if", Python::parser::Token_IF, 0, 1 );
    QTest::newRow( "row15" )
            << MAKETESTROW( "except", Python::parser::Token_EXCEPT, 0, 5 );
    QTest::newRow( "row16" )
            << MAKETESTROW( "class", Python::parser::Token_CLASS, 0, 4 );
    QTest::newRow( "row17" )
            << MAKETESTROW( "try", Python::parser::Token_TRY, 0, 2 );
    QTest::newRow( "row18" )
            << MAKETESTROW( "not", Python::parser::Token_NOT, 0, 2 );
    QTest::newRow( "row19" )
            << MAKETESTROW( "del", Python::parser::Token_DEL, 0, 2 );
    QTest::newRow( "row20" )
            << MAKETESTROW( "for", Python::parser::Token_FOR, 0, 2 );
    QTest::newRow( "row21" )
            << MAKETESTROW( "is", Python::parser::Token_IS, 0, 1 );
    QTest::newRow( "row22" )
            << MAKETESTROW( "raise", Python::parser::Token_RAISE, 0, 4 );
    QTest::newRow( "row23" )
            << MAKETESTROW( "assert", Python::parser::Token_ASSERT, 0, 5 );
    QTest::newRow( "row24" )
            << MAKETESTROW( "elif", Python::parser::Token_ELIF, 0, 3 );
    QTest::newRow( "row25" )
            << MAKETESTROW( "from", Python::parser::Token_FROM, 0, 3 );
    QTest::newRow( "row26" )
            << MAKETESTROW( "lambda", Python::parser::Token_LAMBDA, 0, 5 );
    QTest::newRow( "row27" )
            << MAKETESTROW( "return", Python::parser::Token_RETURN, 0, 5 );
    QTest::newRow( "row28" )
            << MAKETESTROW( "break", Python::parser::Token_BREAK, 0, 4 );
    QTest::newRow( "row29" )
            << MAKETESTROW( "else", Python::parser::Token_ELSE, 0, 3 );
    QTest::newRow( "row30" )
            << MAKETESTROW( "global", Python::parser::Token_GLOBAL, 0, 5 );
    //Now check that anything else is an identifier
    QTest::newRow( "row31" )
            << MAKETESTROW( "globally", Python::parser::Token_IDENTIFIER, 0, 7 );
    QTest::newRow( "row32" )
            << MAKETESTROW( "_globall45y", Python::parser::Token_IDENTIFIER, 0, 10 );
}

void LexerTest::lexSeparatorsAndOperators()
{
    QFETCH( QString, project );
    QFETCH( int, expectedtoken );
    QFETCH( std::size_t, expectedbegin );
    QFETCH( std::size_t, expectedend );
    Python::Lexer l(0, project);
    int token = l.nextTokenKind();
    std::size_t begin = qulonglong(l.tokenBegin());
    std::size_t end = qulonglong(l.tokenEnd());
//     qDebug() << project << token << expectedtoken << l.tokenBegin() << qulonglong(l.tokenEnd());
    QVERIFY( token == expectedtoken );
    QVERIFY( begin == expectedbegin );
    QVERIFY( end == expectedend );
}

void LexerTest::lexSeparatorsAndOperators_data()
{
    QTest::addColumn<QString>( "project" );
    QTest::addColumn<int>( "expectedtoken" );
    QTest::addColumn<std::size_t>( "expectedbegin" );
    QTest::addColumn<std::size_t>( "expectedend" );
    QTest::newRow( "row1" )
            << MAKETESTROW( "(", Python::parser::Token_LPAREN, 0, 0 );
    QTest::newRow( "row2" )
            << MAKETESTROW( "(as", Python::parser::Token_LPAREN, 0, 0 );
    QTest::newRow( "row3" )
            << MAKETESTROW( ")", Python::parser::Token_RPAREN, 0, 0 );
    QTest::newRow( "row4" )
            << MAKETESTROW( "{", Python::parser::Token_LBRACE, 0, 0 );
    QTest::newRow( "row5" )
            << MAKETESTROW( "}", Python::parser::Token_RBRACE, 0, 0 );
    QTest::newRow( "row6" )
            << MAKETESTROW( "[", Python::parser::Token_LBRACKET, 0, 0 );
    QTest::newRow( "row7" )
            << MAKETESTROW( "]", Python::parser::Token_RBRACKET, 0, 0 );
    QTest::newRow( "row8" )
            << MAKETESTROW( ",", Python::parser::Token_COMMA, 0, 0 );
    QTest::newRow( "row9" )
            << MAKETESTROW( ";", Python::parser::Token_SEMICOLON, 0, 0 );
    QTest::newRow( "row10" )
            << MAKETESTROW( ":", Python::parser::Token_COLON, 0, 0 );
    QTest::newRow( "row11" )
            << MAKETESTROW( ".", Python::parser::Token_DOT, 0, 0 );
    QTest::newRow( "row12" )
            << MAKETESTROW( "`", Python::parser::Token_BACKTICK, 0, 0 );
    QTest::newRow( "row13" )
            << MAKETESTROW( "@", Python::parser::Token_AT, 0, 0 );
    QTest::newRow( "row14" )
            << MAKETESTROW( "...", Python::parser::Token_ELLIPSIS, 0, 2 );
    QTest::newRow( "row15" )
            << MAKETESTROW( "*", Python::parser::Token_STAR, 0, 0 );
    QTest::newRow( "row16" )
            << MAKETESTROW( "**", Python::parser::Token_DOUBLESTAR, 0, 1 );
    QTest::newRow( "row17" )
            << MAKETESTROW( "=", Python::parser::Token_EQUAL, 0, 0 );
    QTest::newRow( "row18" )
            << MAKETESTROW( "+", Python::parser::Token_PLUS, 0, 0 );
    QTest::newRow( "row19" )
            << MAKETESTROW( "-", Python::parser::Token_MINUS, 0, 0 );
    QTest::newRow( "row20" )
            << MAKETESTROW( "~", Python::parser::Token_TILDE, 0, 0 );
    QTest::newRow( "row21" )
            << MAKETESTROW( "/", Python::parser::Token_SLASH, 0, 0 );
    QTest::newRow( "row22" )
            << MAKETESTROW( "//", Python::parser::Token_DOUBLESLASH, 0, 1 );
    QTest::newRow( "row23" )
            << MAKETESTROW( "%", Python::parser::Token_MODULO, 0, 0 );
    QTest::newRow( "row24" )
            << MAKETESTROW( "&", Python::parser::Token_ANDD, 0, 0 );
    QTest::newRow( "row25" )
            << MAKETESTROW( "<<", Python::parser::Token_LSHIFT, 0, 1 );
    QTest::newRow( "row26" )
            << MAKETESTROW( ">>", Python::parser::Token_RSHIFT, 0, 1 );
    QTest::newRow( "row27" )
            << MAKETESTROW( "+=", Python::parser::Token_PLUSEQ, 0, 1 );
    QTest::newRow( "row28" )
            << MAKETESTROW( "-=", Python::parser::Token_MINUSEQ, 0, 1 );
    QTest::newRow( "row29" )
            << MAKETESTROW( "/=", Python::parser::Token_SLASHEQ, 0, 1 );
    QTest::newRow( "row30" )
            << MAKETESTROW( "//=", Python::parser::Token_DOUBLESLASHEQ, 0, 2 );
    QTest::newRow( "row31" )
            << MAKETESTROW( "%=", Python::parser::Token_MODULOEQ, 0, 1 );
    QTest::newRow( "row32" )
            << MAKETESTROW( "&=", Python::parser::Token_ANDEQ, 0, 1 );
    QTest::newRow( "row33" )
            << MAKETESTROW( "*=", Python::parser::Token_STAREQ, 0, 1 );
    QTest::newRow( "row34" )
            << MAKETESTROW( "~=", Python::parser::Token_TILDEEQ, 0, 1 );
    QTest::newRow( "row35" )
            << MAKETESTROW( "|=", Python::parser::Token_OREQ, 0, 1 );
    QTest::newRow( "row36" )
            << MAKETESTROW( "**=", Python::parser::Token_DOUBLESTAREQ, 0, 2 );
    QTest::newRow( "row37" )
            << MAKETESTROW( "<<=", Python::parser::Token_LSHIFTEQ, 0, 2 );
    QTest::newRow( "row38" )
            << MAKETESTROW( ">>=", Python::parser::Token_RSHIFTEQ, 0, 2 );
    QTest::newRow( "row39" )
            << MAKETESTROW( "<", Python::parser::Token_LESS, 0, 0 );
    QTest::newRow( "row40" )
            << MAKETESTROW( ">", Python::parser::Token_GREATER, 0, 0 );
    QTest::newRow( "row41" )
            << MAKETESTROW( "<=", Python::parser::Token_LESSEQ, 0, 1 );
    QTest::newRow( "row42" )
            << MAKETESTROW( ">=", Python::parser::Token_GREATEREQ, 0, 1 );
    QTest::newRow( "row43" )
            << MAKETESTROW( "<>", Python::parser::Token_UNEQUAL, 0, 1 );
    QTest::newRow( "row44" )
            << MAKETESTROW( "!=", Python::parser::Token_UNEQUAL, 0, 1 );
    QTest::newRow( "row45" )
            << MAKETESTROW( "|", Python::parser::Token_ORR, 0, 0 );
    QTest::newRow( "row46" )
            << MAKETESTROW( "^", Python::parser::Token_HAT, 0, 0 );
    QTest::newRow( "row47" )
            << MAKETESTROW( "==", Python::parser::Token_ISEQUAL, 0, 1 );
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
    expectedtokens << Python::parser::Token_INDENT;
    expectedtokens << Python::parser::Token_IDENTIFIER;
    expectedtokens << Python::parser::Token_LINEBREAK;
    expectedtokens << Python::parser::Token_INDENT;
    expectedtokens << Python::parser::Token_IDENTIFIER;
    expectedtokens << Python::parser::Token_LINEBREAK;
    expectedtokens << Python::parser::Token_DEDENT;
    expectedtokens << Python::parser::Token_IDENTIFIER;
    expectedtokens << Python::parser::Token_DEDENT;
    QList<QVariant> expectedbegins;
    QList<QVariant> expectedends;
    expectedbegins << qulonglong(0) << qulonglong(2) << qulonglong(5) << qulonglong(6) << qulonglong(10) << qulonglong(13) << qulonglong(14) << qulonglong(16) << MAX_SIZE_T;
    expectedends << qulonglong(1) << qulonglong(4) << qulonglong(5) << qulonglong(9) << qulonglong(12) << qulonglong(13) << qulonglong(15) << qulonglong(18) << MAX_SIZE_T;
    QTest::newRow( "row1" )
            << "  foo\n    bar\n  baz" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::parser::Token_INDENT;
    expectedtokens << Python::parser::Token_IDENTIFIER;
    expectedtokens << Python::parser::Token_LINEBREAK;
    expectedtokens << Python::parser::Token_LINEBREAK;
    expectedtokens << Python::parser::Token_IDENTIFIER;
    expectedtokens << Python::parser::Token_DEDENT;
    expectedbegins << qulonglong(0) << qulonglong(2) << qulonglong(5) << qulonglong(14) << qulonglong(17) << MAX_SIZE_T;
    expectedends << qulonglong(1) << qulonglong(4) << qulonglong(5) << qulonglong(14) << qulonglong(19) << MAX_SIZE_T;
    QTest::newRow( "row2" )
            << "  foo\n#    bar\n  baz" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::parser::Token_INDENT;
    expectedtokens << Python::parser::Token_IDENTIFIER;
    expectedtokens << Python::parser::Token_LINEBREAK;
    expectedtokens << Python::parser::Token_INDENT;
    expectedtokens << Python::parser::Token_IDENTIFIER;
    expectedtokens << Python::parser::Token_LINEBREAK;
    expectedtokens << Python::parser::Token_DEDENT;
    expectedtokens << Python::parser::Token_DEDENT;
    expectedtokens << Python::parser::Token_IDENTIFIER;
    expectedbegins << qulonglong(0) << qulonglong(2) << qulonglong(5) << qulonglong(6) << qulonglong(10) << qulonglong(13) << MAX_SIZE_T << MAX_SIZE_T << qulonglong(14);
    expectedends << qulonglong(1) << qulonglong(4) << qulonglong(5) << qulonglong(9) << qulonglong(12) << qulonglong(13) << MAX_SIZE_T << MAX_SIZE_T << qulonglong(16);
    QTest::newRow( "row3" )
            << "  foo\n    bar\nbaz" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::parser::Token_INDENT;
    expectedtokens << Python::parser::Token_IDENTIFIER;
    expectedtokens << Python::parser::Token_LINEBREAK;
    expectedtokens << Python::parser::Token_LINEBREAK;
    expectedtokens << Python::parser::Token_DEDENT;
    expectedtokens << Python::parser::Token_IDENTIFIER;
    expectedbegins << qulonglong(0) << qulonglong(2) << qulonglong(5) << qulonglong(14) << MAX_SIZE_T << qulonglong(15);
    expectedends << qulonglong(1) << qulonglong(4) << qulonglong(5) << qulonglong(14) << MAX_SIZE_T << qulonglong(17);
    QTest::newRow( "row4" )
            << "  foo\n    #bar\nbaz" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::parser::Token_IDENTIFIER;
    expectedtokens << Python::parser::Token_LINEBREAK;
    expectedtokens << Python::parser::Token_INDENT;
    expectedtokens << Python::parser::Token_IDENTIFIER;
    expectedtokens << Python::parser::Token_LINEBREAK;
    expectedtokens << Python::parser::Token_DEDENT;
    expectedtokens << Python::parser::Token_IDENTIFIER;
    expectedbegins << qulonglong(0) << qulonglong(3) << qulonglong(4) << qulonglong(8) << qulonglong(11) << qulonglong(12) << qulonglong(14);
    expectedends << qulonglong(2) << qulonglong(3) << qulonglong(7) << qulonglong(10) << qulonglong(11) << qulonglong(13) << qulonglong(16);
    QTest::newRow( "row5" )
            << "foo\n    bar\n  baz" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::parser::Token_IDENTIFIER;
    expectedtokens << Python::parser::Token_LINEBREAK;
    expectedtokens << Python::parser::Token_INDENT;
    expectedtokens << Python::parser::Token_IDENTIFIER;
    expectedtokens << Python::parser::Token_LINEBREAK;
    expectedtokens << Python::parser::Token_INDENT;
    expectedtokens << Python::parser::Token_IDENTIFIER;
    expectedtokens << Python::parser::Token_LINEBREAK;
    expectedtokens << Python::parser::Token_INDENT;
    expectedtokens << Python::parser::Token_IDENTIFIER;
    expectedtokens << Python::parser::Token_LINEBREAK;
    expectedtokens << Python::parser::Token_DEDENT;
    expectedtokens << Python::parser::Token_DEDENT;
    expectedtokens << Python::parser::Token_DEDENT;
    expectedtokens << Python::parser::Token_IDENTIFIER;
    expectedbegins << qulonglong(0) << qulonglong(3) << qulonglong(4) << qulonglong(8) << qulonglong(11) << qulonglong(12) << qulonglong(18) << qulonglong(21) << qulonglong(22) << qulonglong(30) << qulonglong(33) << MAX_SIZE_T << MAX_SIZE_T << MAX_SIZE_T << qulonglong(34);
    expectedends << qulonglong(2) << qulonglong(3) << qulonglong(7) << qulonglong(10) << qulonglong(11) << qulonglong(17) << qulonglong(20) << qulonglong(21) << qulonglong(29) << qulonglong(32) << qulonglong(33) << MAX_SIZE_T << MAX_SIZE_T << MAX_SIZE_T << qulonglong(36);
    QTest::newRow( "row6" )
            << "foo\n    bar\n      baz\n        bak\nbor" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::parser::Token_INDENT;
    expectedtokens << Python::parser::Token_IDENTIFIER;
    expectedtokens << Python::parser::Token_EQUAL;
    expectedtokens << Python::parser::Token_LBRACKET;
    expectedtokens << Python::parser::Token_RBRACKET;
    expectedtokens << Python::parser::Token_LINEBREAK;
    expectedtokens << Python::parser::Token_DEDENT;
    expectedtokens << Python::parser::Token_IDENTIFIER;
    expectedbegins << qulonglong(0) << qulonglong(2) << qulonglong(5) << qulonglong(6) << qulonglong(17) << qulonglong(18) << MAX_SIZE_T << qulonglong(19);
    expectedends << qulonglong(1) << qulonglong(4) << qulonglong(5) << qulonglong(6) << qulonglong(17) << qulonglong(18) << MAX_SIZE_T << qulonglong(21);
    QTest::newRow( "row7" )
            << "  foo=[\n    #bar\n]\nbaz" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::parser::Token_INDENT;
    expectedtokens << Python::parser::Token_IDENTIFIER;
    expectedtokens << Python::parser::Token_EQUAL;
    expectedtokens << Python::parser::Token_LBRACKET;
    expectedtokens << Python::parser::Token_LBRACE;
    expectedtokens << Python::parser::Token_RBRACE;
    expectedtokens << Python::parser::Token_RBRACKET;
    expectedtokens << Python::parser::Token_LINEBREAK;
    expectedtokens << Python::parser::Token_DEDENT;
    expectedtokens << Python::parser::Token_IDENTIFIER;
    expectedbegins << qulonglong(0) << qulonglong(2) << qulonglong(5) << qulonglong(6) << qulonglong(9) << qulonglong(12) << qulonglong(21) << qulonglong(22) << MAX_SIZE_T << qulonglong(23);
    expectedends << qulonglong(1) << qulonglong(4) << qulonglong(5) << qulonglong(6) << qulonglong(9) << qulonglong(12) << qulonglong(21) << qulonglong(22) << MAX_SIZE_T << qulonglong(25);
    QTest::newRow( "row8" )
            << "  foo=[\n {  }   #bar\n]\nbaz" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::parser::Token_INDENT;
    expectedtokens << Python::parser::Token_IDENTIFIER;
    expectedtokens << Python::parser::Token_LINEBREAK;
    expectedtokens << Python::parser::Token_LINEBREAK;
    expectedtokens << Python::parser::Token_IDENTIFIER;
    expectedtokens << Python::parser::Token_DEDENT;
    expectedbegins << qulonglong(0) << qulonglong(2) << qulonglong(5) << qulonglong(10) << qulonglong(13) << MAX_SIZE_T;
    expectedends << qulonglong(1) << qulonglong(4) << qulonglong(5) << qulonglong(10) << qulonglong(15) << MAX_SIZE_T;
    QTest::newRow( "row9" )
            << "  foo\n    \n  baz" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::parser::Token_INDENT;
    expectedtokens << Python::parser::Token_IDENTIFIER;
    expectedtokens << Python::parser::Token_LINEBREAK;
    expectedtokens << Python::parser::Token_IDENTIFIER;
    expectedtokens << Python::parser::Token_LINEBREAK;
    expectedtokens << Python::parser::Token_IDENTIFIER;
    expectedtokens << Python::parser::Token_DEDENT;
    expectedbegins << qulonglong(0) << qulonglong(3) << qulonglong(6) << qulonglong(15) << qulonglong(18) << qulonglong(26) << MAX_SIZE_T;
    expectedends << qulonglong(2) << qulonglong(5) << qulonglong(6) << qulonglong(17) << qulonglong(18) << qulonglong(28) << MAX_SIZE_T;
    QTest::newRow( "row10" )
            << "  \tfoo\n        boo\n      \tbaz" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::parser::Token_INDENT;
    expectedtokens << Python::parser::Token_IDENTIFIER;
    expectedtokens << Python::parser::Token_LINEBREAK;
    expectedtokens << Python::parser::Token_INDENT;
    expectedtokens << Python::parser::Token_IDENTIFIER;
    expectedtokens << Python::parser::Token_LINEBREAK;
    expectedtokens << Python::parser::Token_DEDENT;
    expectedtokens << Python::parser::Token_IDENTIFIER;
    expectedtokens << Python::parser::Token_DEDENT;
    expectedbegins << qulonglong(0) << qulonglong(3) << qulonglong(6) << qulonglong(7) << qulonglong(16) << qulonglong(19) << qulonglong(20) << qulonglong(23) << MAX_SIZE_T;
    expectedends << qulonglong(2) << qulonglong(5) << qulonglong(6) << qulonglong(15) << qulonglong(18) << qulonglong(19) << qulonglong(22) << qulonglong(25) << MAX_SIZE_T;
    QTest::newRow( "row11" )
            << "  \tfoo\n        \tboo\n  \tbaz" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::parser::Token_INDENT;
    expectedtokens << Python::parser::Token_IDENTIFIER;
    expectedtokens << Python::parser::Token_EQUAL;
    expectedtokens << Python::parser::Token_LBRACKET;
    expectedtokens << Python::parser::Token_IDENTIFIER;
    expectedtokens << Python::parser::Token_RBRACKET;
    expectedtokens << Python::parser::Token_DEDENT;
    expectedbegins << qulonglong(0) << qulonglong(2) << qulonglong(5) << qulonglong(6) << qulonglong(14) << qulonglong(18) << MAX_SIZE_T;
    expectedends << qulonglong(1) << qulonglong(4) << qulonglong(5) << qulonglong(6) << qulonglong(16) << qulonglong(18) << MAX_SIZE_T;
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
    expectedtokens << Python::parser::Token_STRINGLITERAL;
    QList<QVariant> expectedbegins;
    QList<QVariant> expectedends;
    expectedbegins << qulonglong(0);
    expectedends << qulonglong(22);
    QTest::newRow( "row1" )
            << "'''foo\n    bar\n  baz'''" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::parser::Token_STRINGLITERAL;
    expectedbegins << qulonglong(0);
    expectedends << qulonglong(23);
    QTest::newRow( "row2" )
            << "\"\"\"foo\n#    bar\n  baz\"\"\"" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::parser::Token_STRINGLITERAL;
    expectedbegins << qulonglong(0);
    expectedends << qulonglong(27);
    QTest::newRow( "row3" )
            << "\"\"\"foo\n#  ''''  bar\n  baz\"\"\"" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::parser::Token_STRINGLITERAL;
    expectedbegins << qulonglong(0);
    expectedends << qulonglong(27);
    QTest::newRow( "row4" )
            << "'''foo\n# \"\"\"\"   bar\n  baz'''" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::parser::Token_STRINGLITERAL;
    expectedbegins << qulonglong(0);
    expectedends << qulonglong(20);
    QTest::newRow( "row5" )
            << "\"\"\"foo\n#    bar\n  baz" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::parser::Token_STRINGLITERAL;
    expectedbegins << qulonglong(0);
    expectedends << qulonglong(27);
    QTest::newRow( "row6" )
            << "\"\"\"foo\n#   \\\"\"\" bar\n  baz\"\"\"" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::parser::Token_STRINGLITERAL;
    expectedtokens << Python::parser::Token_STRINGLITERAL;
    expectedbegins << qulonglong(0) << qulonglong(17);
    expectedends << qulonglong(13) << qulonglong(25);
    QTest::newRow( "row7" )
            << "\"\"\"foo\n#   \"\"\"\n  \"\"\"baz\"\"\"" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::parser::Token_STRINGLITERAL;
    expectedbegins << qulonglong(0);
    expectedends << qulonglong(18);
    QTest::newRow( "row8" )
            << "\"foo#    bar6  baz\"" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::parser::Token_STRINGLITERAL;
    expectedbegins << qulonglong(0);
    expectedends << qulonglong(17);
    QTest::newRow( "row9" )
            << "'foo#    bar  baz'" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::parser::Token_STRINGLITERAL;
    expectedtokens << Python::parser::Token_LINEBREAK;
    expectedbegins << qulonglong(0) << qulonglong(4);
    expectedends << qulonglong(3) << qulonglong(4);
    QTest::newRow( "row10" )
            << "'foo\n" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::parser::Token_STRINGLITERAL;
    expectedtokens << Python::parser::Token_STRINGLITERAL;
    expectedbegins << qulonglong(0) << qulonglong(10);
    expectedends << qulonglong(4) << qulonglong(14);
    QTest::newRow( "row11" )
            << "'foo'\n    'bar'" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::parser::Token_STRINGLITERAL;
    expectedtokens << Python::parser::Token_STRINGLITERAL;
    expectedbegins << qulonglong(0) << qulonglong(17);
    expectedends << qulonglong(13) << qulonglong(21);
    QTest::newRow( "row12" )
            << "\"\"\"foo\n#   \"\"\"\n  'baz'" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::parser::Token_STRINGLITERAL;
    expectedbegins << qulonglong(0);
    expectedends << qulonglong(5);
    QTest::newRow( "row13" )
            << "u'foo'" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::parser::Token_STRINGLITERAL;
    expectedbegins << qulonglong(0);
    expectedends << qulonglong(5);
    QTest::newRow( "row14" )
            << "r'foo'" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::parser::Token_STRINGLITERAL;
    expectedbegins << qulonglong(0);
    expectedends << qulonglong(5);
    QTest::newRow( "row15" )
            << "R'foo'" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::parser::Token_STRINGLITERAL;
    expectedbegins << qulonglong(0);
    expectedends << qulonglong(6);
    QTest::newRow( "row16" )
            << "uR'foo'" << expectedtokens << expectedbegins << expectedends;
    expectedtokens.clear();
    expectedbegins.clear();
    expectedends.clear();
    expectedtokens << Python::parser::Token_STRINGLITERAL;
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
