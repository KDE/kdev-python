/* KDevelop QMake Support
 *
 * Copyright 2007 Andreas Pakulat <apaku@gmx.de>
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

#include "pythonlexer.h"

#include <QtCore/QString>
#include <QtCore/QStringList>
#include <QtCore/QRegExp>
#include <QtCore/QDebug>
#include "pythonparser.h"
#include <kdev-pg-location-table.h>
#include <kdev-pg-token-stream.h>

#include "kwcheck.h"
#include "numbercheck.h"

namespace PythonParser
{

/*
 * @TODO: COMMENT all the stuff, really needed
 */

Lexer::Lexer( Parser* _parser, const QString& content ):
        m_content( content ), m_parser( _parser ),
        m_curpos( 0 ), m_contentSize( m_content.size() ),
        m_tokenBegin( 0 ), m_tokenEnd( 0 ), m_openParenNum( 0 )
{
    pushState( ErrorState );
    pushState( DefaultState );
    pushState( IndentState );
    pushIndentation( 0 );
}

int Lexer::state() const
{
    return m_state.top();
}

void Lexer::pushState( int state )
{
    m_state.push( state );
}

void Lexer::popState()
{
    m_state.pop();
}

int Lexer::indentation() const
{
    return m_indentation.top();
}

void Lexer::pushIndentation( int indentation )
{
    m_indentation.push( indentation );
}

void Lexer::popIndentation()
{
    m_indentation.pop();
}

int Lexer::nextTokenKind()
{
    int token = Parser::Token_INVALID;
    if ( m_curpos >= m_contentSize )
    {
        m_tokenBegin = -1;
        m_tokenEnd = -1;
        if( indentation() > 0 )
        {
            popIndentation();
            return Parser::Token_DEDENT;
        }
        return 0;
    }
    QChar* it = m_content.data();
    it += m_curpos;
    if( state() == IndentState )
    {
        // Check wether we need to indent or dedent, this is quite complicated.
        // Especially because it contains 3 exit points and one point that resets
        // the current position and it and then lets the rest of the code run
        if( !it->isSpace() && it->unicode() != '#' && indentation() > 0 )
        {
            // No whitespace at the start of the line, so we need to create
            // as many DEDENT tokens as we have indenations in the stack
            token = Parser::Token_DEDENT;
            m_tokenBegin = -1;
            m_tokenEnd = -1;
            popIndentation();
            return token;
        }else if( it->isSpace() )
        {
            // We've got indentation, lets see how much
            m_tokenBegin = m_curpos;
            int spacecount = 0;
            do
            {
                if( it->unicode() == '\t' )
                {
                    spacecount += 8-( spacecount % 8 );
                } else if( it->unicode() != '\f' && it->unicode() != '\n' )
                {
                    spacecount++;
                }else if( it->unicode() == '#' )
                {
                    // find the next newline position and return a linebreak token for it
                    do
                    {
                        it++;
                        m_curpos++;
                    }while( it->unicode() != '\n' && m_curpos < m_contentSize );
                    m_tokenBegin = m_curpos;
                    m_tokenEnd = m_curpos;
                    createNewline( m_curpos );
                    m_curpos++;
                    return Parser::Token_LINEBREAK;
                }
                it++;
                m_curpos++;
            }while( it->isSpace() && it->unicode() != '\n' && m_curpos < m_contentSize );
            if( it->unicode() == '#' )
            {
                // Ooops, whitespace and then a #, this is a plain comment line, only create
                // a newline token for this
                do
                {
                    it++;
                    m_curpos++;
                }while( it->unicode() != '\n' && m_curpos < m_contentSize );
                m_tokenBegin = m_curpos;
                m_tokenEnd = m_curpos;
                createNewline( m_curpos );
                m_curpos++;
                return Parser::Token_LINEBREAK;
            }else if( it->unicode() == '\n' )
            {
                m_tokenBegin = m_curpos;
                m_tokenEnd = m_curpos;
                createNewline( m_curpos );
                m_curpos++;
                return Parser::Token_LINEBREAK;
            }
            it--;
            m_tokenEnd = m_curpos-1;

            if( spacecount > indentation() )
            {
                // We have more indentation, so we need to create an INDENT token
                pushIndentation( spacecount );
                popState();
                token = Parser::Token_INDENT;
                return token;
            }else if( spacecount == indentation() )
            {
                // Don't do anything, same indentation level so we ignore the whitespace and move on with lexing the forthcoming text
                popState();
                m_curpos = m_tokenBegin;
                it = m_content.data() + m_curpos;
            }else
            {
                // We've got a dedentation, so create a DEDENT token
                // If the next indentation level is still larger than what we've
                // counted we'll do another try on the next call, else we'll go into
                // usual parsing next time we enter this function
                popIndentation();
                token = Parser::Token_DEDENT;
                if( spacecount < indentation() )
                {
                    m_curpos = m_tokenBegin;
                }else
                {
                    popState();
                }
                return token;
            }
        }else
        {
            // Either we have a comment, which will be ignored in the next part
            // or we have a non-whitespace character and no more indentation
            // level to create a DEDENT token for. Thus get out of IndentState
            // and do normal parsing
            popState();
        }
    }
    switch ( state() )
    {
        case DefaultState:
            it = ignoreWhitespaceAndComments( it );
            if( it->unicode() == '\\' && (it+1)->unicode() == '\n' )
            {
                createNewline(m_curpos+1);
                m_curpos += 2;
                it += 2;
            }
            m_tokenBegin = m_curpos;
            if( isStringStart( it ) )
            {
                if( it->toLower().unicode() == 'u' )
                {
                    it++;
                    m_curpos++;
                }
                if( it->toLower().unicode() == 'r' )
                {
                    it++;
                    m_curpos++;
                }
                QChar* quotestart = it++;
                m_curpos++;
                if( it->unicode() == quotestart->unicode() && (it+1)->unicode() == quotestart->unicode() )
                {
                    it += 2;
                    m_curpos += 2;
                    // read everything until we find 3 consecutive chars that are
                    // equal to quotestart
                    while( m_curpos < m_contentSize - 3 && !( it->unicode() == quotestart->unicode()
                            && (it+1)->unicode() == quotestart->unicode()
                            && (it+2)->unicode() == quotestart->unicode()) )
                    {
                        if( it->unicode() == '\\' )
                        {
                            it += 2;
                            m_curpos += 2;
                        }else
                        {
                            it++;
                            m_curpos++;
                        }
                    }
                    // We checked these 2 characters and they're either the last 2 chars
                    // or they're the closing '' or "" and thus we always consume them too
                    it += 2;
                    m_curpos += 2;
                    token = Parser::Token_STRINGLITERAL;
                }else
                {
                    // single quote so read until the end of line or closing quote
                    // if eol is found return invalid token
                    while( it->unicode() != quotestart->unicode() && it->unicode() != '\n' && m_curpos < m_contentSize )
                    {
                        if( it->unicode() == '\\' )
                        {
                            it += 2;
                            m_curpos += 2;
                        }else
                        {
                            it++;
                            m_curpos++;
                        }
                    }
                    if( it->unicode() == '\n' )
                    {
                        // We've read to the newline, now return to the last string character
                        m_curpos--;
                    }
                    token = Parser::Token_STRINGLITERAL;
                }
                //Go to the next character, it still points to the end of the literal
                it++;
                if( it->isSpace() )
                {
                    // read more space until we find a non-space character
                    // if the non-space char is a quote again set the current position
                    // to the char before this non-space character, so next time
                    // we lex the next string. This allows for string concatenation
                    QChar* space = it;
                    int count = 0;
                    while( space->isSpace() && (m_curpos+count) < m_contentSize )
                    {
                        space++;
                        count++;
                    }
                    // Now check wether this is a string begin, if so we immediately
                    // return the token and set its endPos, we also set the parsing
                    // position to the next quote and ignore the newline that might exist
                    // between the strings
                    if( space->unicode() == '\'' || space->unicode() == '"' )
                    {
                        m_tokenEnd = m_curpos;
                        m_curpos += count;
                        return token;
                    }
                }
            }else if( it->isLetter() || it->unicode() == '_' )
            {
                QChar* start = it;
                do{
                    it++;
                    m_curpos++;
                }while( m_curpos < m_contentSize
                        && ( it->isLetterOrNumber() || it->unicode() == '_' ) );
                //Adjust current position to the last character that belongs to the identifier/keyword
                m_curpos--;
                token = checkForKeyword( start, m_curpos-m_tokenBegin+1 );
            }else if( it->isNumber() || ( it->unicode() == '.' && (it+1)->isNumber() ) )
            {
                // all numeric literals start with a number or a . followed by a number
                do{
                    it++;
                    m_curpos++;
                }while( m_curpos < m_contentSize
                        && ( it->isNumber() || it->unicode() == 'e'
                            || it->unicode() == 'E' || it->unicode() == 'j'
                            || it->unicode() == 'J' || it->unicode() == '+'
                            || it->unicode() == '-' || it->unicode() == '.'
                            || it->unicode() == 'A' || it->unicode() == 'B'
                            || it->unicode() == 'C' || it->unicode() == 'D'
                            || it->unicode() == 'F' || it->unicode() == 'a'
                            || it->unicode() == 'b' || it->unicode() == 'c'
                            || it->unicode() == 'd' || it->unicode() == 'f'
                            || it->unicode() == 'l' || it->unicode() == 'L'
                            || it->unicode() == 'X' || it->unicode() == 'x' ) );
                //Adjust position to last character that belongs to the number
                m_curpos--;
                token = getTokenForNumberString( m_content.mid( m_tokenBegin, m_curpos-m_tokenBegin+1 ) );
            }else
            {
                QChar* ch2 = m_curpos < m_contentSize ? it + 1 : 0;
                QChar* ch3 = m_curpos < m_contentSize ? it + 2 : 0;
                switch ( it->unicode() )
                {
                    case '\n':
                        pushState( IndentState );
                        createNewline( m_curpos );
                        token = Parser::Token_LINEBREAK;
                        break;
                    case '(':
                        m_openParenNum++;
                        token = Parser::Token_LPAREN;
                        break;
                    case ')':
                        m_openParenNum--;
                        token = Parser::Token_RPAREN;
                        break;
                    case '{':
                        m_openParenNum++;
                        token = Parser::Token_LBRACE;
                        break;
                    case '}':
                        m_openParenNum--;
                        token = Parser::Token_RBRACE;
                        break;
                    case '[':
                        m_openParenNum++;
                        token = Parser::Token_LBRACKET;
                        break;
                    case ']':
                        m_openParenNum--;
                        token = Parser::Token_RBRACKET;
                        break;
                    case ',':
                        token = Parser::Token_COMMA;
                        break;
                    case ';':
                        token = Parser::Token_SEMICOLON;
                        break;
                    case ':':
                        token = Parser::Token_COLON;
                        break;
                    case '.':
                        if( ch2 && ch3 && ch2->unicode() == '.' && ch3->unicode() == '.' )
                        {
                            m_curpos += 2;
                            token = Parser::Token_ELLIPSIS;
                        }else
                        {
                            token = Parser::Token_DOT;
                        }
                        break;
                    case '`':
                        token = Parser::Token_BACKTICK;
                        break;
                    case '@':
                        token = Parser::Token_AT;
                        break;
                    case '*':
                        if( ch2 && ch3 && ch2->unicode() == '*' && ch3->unicode() == '=')
                        {
                            m_curpos += 2;
                            token = Parser::Token_DOUBLESTAREQ;
                        }else if( ch2 && ch2->unicode() == '*' )
                        {
                            m_curpos++;
                            token = Parser::Token_DOUBLESTAR;
                        }else if( ch2 && ch2->unicode() == '=')
                        {
                            m_curpos++;
                            token = Parser::Token_STAREQ;
                        }else
                        {
                            token = Parser::Token_STAR;
                        }
                        break;
                    case '=':
                        if( ch2 && ch2->unicode() == '=' )
                        {
                            m_curpos++;
                            token = Parser::Token_ISEQUAL;
                        }else
                        {
                            token = Parser::Token_EQUAL;
                        }
                        break;
                    case '+':
                        if( ch2 && ch2->unicode() == '=' )
                        {
                            m_curpos++;
                            token = Parser::Token_PLUSEQ;
                        }else
                        {
                            token = Parser::Token_PLUS;
                        }
                        break;
                    case '-':
                        if( ch2 && ch2->unicode() == '=' )
                        {
                            m_curpos++;
                            token = Parser::Token_MINUSEQ;
                        }else
                        {
                            token = Parser::Token_MINUS;
                        }
                        break;
                    case '~':
                        if( ch2 && ch2->unicode() == '=' )
                        {
                            m_curpos++;
                            token = Parser::Token_TILDEEQ;
                        }else
                        {
                            token = Parser::Token_TILDE;
                        }
                        break;
                    case '/':
                        if( ch2 && ch2->unicode() == '=' )
                        {
                            m_curpos++;
                            token = Parser::Token_SLASHEQ;
                        }else if( ch2 && ch3 && ch2->unicode() == '/' && ch3->unicode() == '=' )
                        {
                            m_curpos += 2;
                            token = Parser::Token_DOUBLESLASHEQ;
                        }else if( ch2 && ch2->unicode() == '/' )
                        {
                            m_curpos++;
                            token = Parser::Token_DOUBLESLASH;
                        }else
                        {
                            token = Parser::Token_SLASH;
                        }
                        break;
                    case '%':
                        if( ch2 && ch2->unicode() == '=' )
                        {
                            m_curpos++;
                            token = Parser::Token_MODULOEQ;
                        }else
                        {
                            token = Parser::Token_MODULO;
                        }
                        break;
                    case '&':
                        if( ch2 && ch2->unicode() == '=' )
                        {
                            m_curpos++;
                            token = Parser::Token_ANDEQ;
                        }else
                        {
                            token = Parser::Token_ANDD;
                        }
                        break;
                    case '<':
                        if( ch2 && ch2->unicode() == '=' )
                        {
                            m_curpos++;
                            token = Parser::Token_LESSEQ;
                        }else if( ch2 && ch3 && ch2->unicode() == '<' && ch3->unicode() == '=' )
                        {
                            m_curpos += 2;
                            token = Parser::Token_LSHIFTEQ;
                        }else if( ch2 && ch2->unicode() == '<' )
                        {
                            m_curpos++;
                            token = Parser::Token_LSHIFT;
                        }else if( ch2 && ch2->unicode() == '>' )
                        {
                            m_curpos++;
                            token = Parser::Token_UNEQUAL;
                        }else
                        {
                            token = Parser::Token_LESS;
                        }
                        break;
                    case '>':
                        if( ch2 && ch2->unicode() == '=' )
                        {
                            m_curpos++;
                            token = Parser::Token_GREATEREQ;
                        }else if( ch2 && ch3 && ch2->unicode() == '>' && ch3->unicode() == '=' )
                        {
                            m_curpos += 2;
                            token = Parser::Token_RSHIFTEQ;
                        }else if( ch2 && ch2->unicode() == '>' )
                        {
                            m_curpos++;
                            token = Parser::Token_RSHIFT;
                        }else
                        {
                            token = Parser::Token_GREATER;
                        }
                        break;
                    case '|':
                        if( ch2 && ch2->unicode() == '=' )
                        {
                            m_curpos++;
                            token = Parser::Token_OREQ;
                        }else
                        {
                            token = Parser::Token_ORR;
                        };
                        break;
                    case '^':
                        token = Parser::Token_HAT;
                        break;
                    case '!':
                        if( ch2 && ch2->unicode() == '=' )
                        {
                            m_curpos++;
                            token = Parser::Token_UNEQUAL;
                        }
                        break;
                    default:
                        break;
                }
            }
            break;
        default:
            token = Parser::Token_INVALID;
            break;
    }
    if ( m_curpos >= m_contentSize )
    {
        m_tokenBegin = -1;
        m_tokenEnd = -1;
        if( indentation() > 0 )
        {
            popIndentation();
            return Parser::Token_DEDENT;
        }
        return 0;
    }
    m_tokenEnd = m_curpos;
    m_curpos++;
    return token;
}

qint64 Lexer::tokenBegin() const
{
    return m_tokenBegin;
}

qint64 Lexer::tokenEnd() const
{
    return m_tokenEnd;
}

QChar* Lexer::ignoreWhitespaceAndComments( QChar* it )
{
    // Ignore whitespace and comments, but preserve the newline if we're not inside a parenthesis
    bool isComment = false;
    while ( m_curpos < m_contentSize
            && ( it->isSpace() || isComment || it->unicode() == '#' ||
                    ( it->unicode() == '\\' && m_openParenNum && (it+1)->unicode() == '\n' )
               )
            && ( it->unicode() != '\n' || m_openParenNum > 0 ) )
    {
        if( it->unicode() == '#' )
        {
            isComment = true;
        }else if( it->unicode() == '\n' && m_openParenNum > 0 )
        {
            isComment = false;
            createNewline( m_curpos );
        }
        ++it;
        ++m_curpos;
    }
    return it;
}

void Lexer::createNewline( int curpos )
{
    if( m_parser )
        m_parser->tokenStream->locationTable()->newline( curpos );
}

bool Lexer::isStringStart( QChar* it )
{
    if( it->unicode() == '\'' || it->unicode() == '"' )
    {
        return true;
    }
    if( it->toLower().unicode() == 'u' && m_curpos < m_contentSize - 1 )
    {
        if( (it+1)->unicode() == '\'' || (it+1)->unicode() == '"' )
        {
            return true;
        }else if( (it+1)->toLower().unicode() == 'r' && m_curpos < m_contentSize - 2 )
        {
            if( (it+2)->unicode() == '\'' || (it+2)->unicode() == '"' )
            {
                return true;
            }
        }
    }
    if( it->toLower().unicode() == 'r' && m_curpos < m_contentSize - 1 )
    {
        if( (it+1)->unicode() == '\'' || (it+1)->unicode() == '"' )
        {
            return true;
        }
    }
    return false;
}

}
