%{
/*****************************************************************************
 * Copyright (c) 2006 Andreas Pakulat <apaku@gmx.de>                         *
 * Copyright (c) 2007 Piyush Verma <piyush.verma@gmail.com>                  *
 *                                                                           *
 * This program is free software; you can redistribute it and/or             *
 * modify it under the terms of the GNU Library General Public               *
 * License as published by the Free Software Foundation; either              *
 * version 2 of the License, or (at your option) any later version.          *
 *                                                                           *
 * This grammar is distributed in the hope that it will be useful,           *
 * but WITHOUT ANY WARRANTY; without even the implied warranty of            *
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU         *
 * Lesser General Public License for more details.                           *
 *                                                                           *
 * You should have received a copy of the GNU Library General Public License *
 * along with this library; see the file COPYING.LIB.  If not, write to      *
 * the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,      *
 * Boston, MA 02110-1301, USA.                                               *
 *****************************************************************************/
%}


%option c++
%option yyclass="python::Lexer"
%option debug
%option noyywrap

%{

#define DONT_INCLUDE_FLEXLEXER
#include "python_lexer.h"

%}

 /* UTF-8 sequences, generated with the Unicode.hs script from
  * http://lists.gnu.org/archive/html/help-flex/2005-01/msg00043.html */

 /* \u0024, \u0041-\u005a, \u005f, \u0061-\u007a: one byte in UTF-8 */
Letter1         [A-Za-z_$]
 /* \u00c0-\u00d6, \u00d8-\u00f6, \u00f8-\u00ff */
Letter2         [\xC3]([\x80-\x96]|[\x98-\xB6]|[\xB8-\xBF])
 /* \u0100-\u1fff */
Letter3         [\xC4-\xDF][\x80-\xBF]|([\xE0][\xA0-\xBF]|[\xE1][\x80-\xBF])[\x80-\xBF]
 /* \u3040-\u318f */
Letter4         [\xE3]([\x86][\x80-\x8F]|[\x81-\x85][\x80-\xBF])
 /* \u3300-\u337f */
Letter5         [\xE3][\x8C-\x8D][\x80-\xBF]
 /* \u3400-\u3d2d */
Letter6         [\xE3](\xB4[\x80-\xAD]|[\x90-\xB3][\x80-\xBF])
 /* \u4e00-\u9fff */
Letter7         ([\xE4][\xB8-\xBF]|[\xE5-\xE9][\x80-\xBF])[\x80-\xBF]
 /* \uf900-\ufaff */
Letter8         [\xEF][\xA4-\xAB][\x80-\xBF]

Letter          {Letter1}|{Letter2}|{Letter3}|{Letter4}|{Letter5}|{Letter6}|{Letter7}|{Letter8}

 /* \u0030-\u0039: ISO-LATIN-1 digits */
Digit1          [0-9]
 /* \u0660-\u0669, \u06f0-\u06f9: Arabic-Indic and extended Ar.-Indic digits */
Digit2          [\xD9][\xA0-\xA9]|[\xDB][\xB0-\xB9]
 /* \u0966-\u096f, \u09e6-\u09ef: Devanagari digits */
Digit3          [\xE0]([\xA5]|[\xA7])[\xA6-\xAF]
 /* \u0a66-\u0a6f, \u0ae6-\u0aef */
Digit4          [\xE0]([\xA9]|[\xAB])[\xA6-\xAF]
 /* \u0b66-\u0b6f, \u0be7-\u0bef */
Digit5          [\xE0]([\xAD][\xA6-\xAF]|[\xAF][\xA7-\xAF])
 /* \u0c66-\u0c6f, \u0ce6-\u0cef, \u0d66-\u0d6f */
Digit6          [\xE0]([\xB1]|[\xB3]|[\xB5])[\xA6-\xAF]
 /* \u0e50-\u0e59, \u0ed0-\u0ed9 */
Digit7          [\xE0]([\xB9]|[\xBB])[\x90-\x99]
 /* \u1040-\u1049 */
Digit8          [\xE1][\x81][\x80-\x89]
 /* \uff10-\uff19: Fullwidth digits */
Digit9          [\xEF][\xBC][\x90-\x99]

 /* \u0080-\uffff */
Multibyte1      ([\xC2-\xDF]|[\xE0][\xA0-\xBF]|[\xE1-\xEF][\x80-\xBF])[\x80-\xBF]
 /* \u10000-\u1fffff */
Multibyte2      ([\xF0][\x90-\xBF]|[\xF1-\xF7][\x80-\xBF])[\x80-\xBF][\x80-\xBF]
 /* \u200000-\u3ffffff */
Multibyte3      ([\xF8][\x88-\xBF]|[\xF9-\xFB][\x80-\xBF])[\x80-\xBF][\x80-\xBF][\x80-\xBF]
 /* \u4000000-\u7fffffff */
Multibyte4      ([\xFC][\x84-\xBF]|[\xFD][\x80-\xBF])[\x80-\xBF][\x80-\xBF][\x80-\xBF]
 /* Any multi-byte Unicode character. Single-byte ones are just . in lex. */
Multibyte       {Multibyte1}|{Multibyte2}|{Multibyte3}|{Multibyte4}


 /* non-Unicode stuff */

HexDigit        [0-9a-fA-F]
Digit           {Digit1}|{Digit2}|{Digit3}|{Digit4}|{Digit5}|{Digit6}|{Digit7}|{Digit8}|{Digit9}
OctalDigit      [0-7]
NonZeroDigit    [1-9]

UnicodeEscape   [\\][u]+{HexDigit}{HexDigit}{HexDigit}{HexDigit}
OctalEscape     [\\]{OctalDigit}({Digit}({Digit})?)?
SimpleEscape    [\\]([']|["]|[\\]|[rnbft])
Escape          {SimpleEscape}|{UnicodeEscape}|{OctalEscape}
AsciiEscape     [\\].

IntSuffix       [Ll]
DecimalNum      ([0]|{NonZeroDigit}{Digit}*){IntSuffix}?
OctalNum        [0]{OctalDigit}+{IntSuffix}?
HexNum          [0][xX]{HexDigit}+{IntSuffix}?
IntegerLiteral  {DecimalNum}|{OctalNum}|{HexNum}

Sign            [+-]
SignedInt       {Sign}?{Digit}+
DecimalExponent [eE]{SignedInt}?
Float1          {Digit}+[\.]{Digit}*{DecimalExponent}?
Float2          {Digit}*[\.]{Digit}+{DecimalExponent}?
Float3          {Digit}+{DecimalExponent}
FloatingPoint   {Float1}|{Float2}|{Float3}

ImagNumber      ({FloatingPoint}|{Digit}+)[fF]

Whitespace      [ \v\f]
Tab	            [\t]
LineBreak       [\n]

Identifier      [a-zA-Z_][a-zA-Z0-9_]*

StringPrefix    "r"|"u"|"U"|"R"|"ur"|"UR"|"Ur"|"uR"

ShortString1    "'"([^\n\\']|{AsciiEscape})*"'"
ShortString2    "\""([^\n\\"]|{AsciiEscape})*"\""
ShortString     {ShortString1}|{ShortString2}
LongString1     "'''"([^\\]|{AsciiEscape})"'''"
LongString2     "\"\"\""
LongString      {LongString1}
Comment         ("#"[^\n]*)|(^[\n][\t\v\f]*"\"")
StringLiteral   {StringPrefix}?({ShortString}|{LongString})


%%%%

 /* whitespace, comments, linebreak */
{LongString2}(.)*{LongString2} return parser::Token_STRINGLITERAL;
{LineBreak}	{
    if( !m_paren )
    {
        int d = m_currentOffset;
        if( m_contents[ d ] != ' ' && m_contents[ d]  != '\t' && m_contents[ d ]  != '\v' && m_contents[ d ] != '\f' )
        {
            if( m_indent.back() > 0 )
            {
                while( m_indent.back() != 0)
                {
                    dedent_level++;
                    m_indent.pop_back();
                }
                return parser::Token_DEDENT;
            }
            else
            {
                return parser::Token_LINEBREAK;
            }
        }
    }
}
[\\]    {
        m_currentOffset++;
    }
{LineBreak}{Tab} {
    if( !m_paren )
    {
        white_count = 8;
        space_count = 0;
        indent();
        if( white_count > (m_indent.back()) )
        {
            m_indent.push_back(white_count);
            return parser::Token_INDENT;
        }
        else if( white_count < (m_indent.back()) )
        {
            element = find( m_indent.begin(),m_indent.end(),white_count);
            if( * element )
            {
                while( m_indent.back() != white_count)
                {
                    dedent_level++;
                    m_indent.pop_back();
                }
                return parser::Token_DEDENT;
            }
            else
            {
                if ( ! blank_line)
                std::cerr<<"Inconsistent Spacing";
            }
        }
        else
        {
            if(white_count>0)
            {
                return parser::Token_LINEBREAK;
            }
        }
    }
}
{Tab}*
{LineBreak}{Whitespace} {
    if( !m_paren)
    {
        white_count = 0;
        space_count = 1;
        indent();
        if( white_count > (m_indent.back()) )
        {
            m_indent.push_back(white_count);
            return  parser::Token_INDENT;
        }
        else if( white_count < (m_indent.back()) )
        {
            element = find( m_indent.begin(),m_indent.end(),white_count);
            if( * element )
            {
                while( m_indent.back() != white_count)
                {
                    dedent_level++;
                    m_indent.pop_back();
                }
                return parser::Token_DEDENT;
            }
            else
            {
                if( ! blank_line )
                std::cerr<<"Inconsistent Spacing";
            }
        }
        else
        {
            if(white_count>0)
            {
                return parser::Token_LINEBREAK;
            }
        }
    }
}
{Comment}       /*skip*/
{Whitespace}*   /* skip */

 /* reserved keywords */
"and"            return parser::Token_AND;
"del"            return parser::Token_DEL;
"for"            return parser::Token_FOR;
"is"             return parser::Token_IS;
"raise"          return parser::Token_RAISE;
"assert"         return parser::Token_ASSERT;
"elif"           return parser::Token_ELIF;
"from"           return parser::Token_FROM;
"lambda"         return parser::Token_LAMBDA;
"return"         return parser::Token_RETURN;
"break"          return parser::Token_BREAK;
"else"           return parser::Token_ELSE;
"global"         return parser::Token_GLOBAL;
"not"            return parser::Token_NOT;
"try"            return parser::Token_TRY;
"class"          return parser::Token_CLASS;
"except"         return parser::Token_EXCEPT;
"if"             return parser::Token_IF;
"or"             return parser::Token_OR;
"while"          return parser::Token_WHILE;
"continue"       return parser::Token_CONTINUE;
"exec"           return parser::Token_EXEC;
"import"         return parser::Token_IMPORT;
"pass"           return parser::Token_PASS;
"yield"          return parser::Token_YIELD;
"def"            return parser::Token_DEF;
"finally"        return parser::Token_FINALLY;
"in"             return parser::Token_IN;
"print"          return parser::Token_PRINT;

 /* String literals */

{StringLiteral}  return parser::Token_STRINGLITERAL;

 /* Identifiers and Numbers */
{Identifier}     return parser::Token_IDENTIFIER;
{IntegerLiteral} return parser::Token_INTEGER;
{FloatingPoint}  return parser::Token_FLOAT;
{ImagNumber}     return parser::Token_IMAGNUM;

 /* Separators */
"("              return parser::Token_LPAREN;
")"              return parser::Token_RPAREN;
"{"             {
    m_paren = m_paren + 1;
    return parser::Token_LBRACE;
    }
"}"             {
    m_paren = m_paren - 1;
    return parser::Token_RBRACE;
    }
"["              return parser::Token_LBRACKET;
"]"              return parser::Token_RBRACKET;
","              return parser::Token_COMMA;
";"              return parser::Token_SEMICOLON;
":"              return parser::Token_COLON;
"."              return parser::Token_DOT;
"`"              return parser::Token_BACKTICK;
"@"              return parser::Token_AT;

 /* operators */
"..."            return parser::Token_ELLIPSIS;
"*"              return parser::Token_STAR;
"**"             return parser::Token_DOUBLESTAR;
"="              return parser::Token_EQUAL;
"+"              return parser::Token_PLUS;
"-"              return parser::Token_MINUS;
"~"              return parser::Token_TILDE;
"/"              return parser::Token_SLASH;
"//"             return parser::Token_DOUBLESLASH;
"%"              return parser::Token_MODULO;
"&"              return parser::Token_AND;
"<<"             return parser::Token_LSHIFT;
">>"             return parser::Token_RSHIFT;
"+="             return parser::Token_PLUSEQ;
"-="             return parser::Token_MINUSEQ;
"/="             return parser::Token_SLASHEQ;
"//="            return parser::Token_DOUBLESLASHEQ;
"%="             return parser::Token_MODULOEQ;
"&="             return parser::Token_ANDEQ;
"*="             return parser::Token_STAREQ;
"~="             return parser::Token_TILDEEQ;
"|="             return parser::Token_OREQ;
"**="            return parser::Token_DOUBLESTAREQ;
"<<="            return parser::Token_LSHIFTEQ;
">>="            return parser::Token_RSHIFTEQ;

 /* comparison */

"<"              return parser::Token_LESS;
">"              return parser::Token_GREATER;
">="             return parser::Token_GREATEREQ;
"<="             return parser::Token_LESSEQ;
"<>"             return parser::Token_UNEQUAL;
"!="             return parser::Token_UNEQUAL;
"|"              return parser::Token_OR;
"^"              return parser::Token_HAT;
"=="             return parser::Token_ISEQUAL;

 /* End of file */
<<EOF>> {
    if( m_indent.back() > 0 )
    {
        while( m_indent.back() != 0)
        {
            m_indent.pop_back();
        }
        return parser::Token_DEDENT;
    }
    return parser::Token_EOF;
}


 /* Everything that is not handled up to now is not part of the language. */
.                return parser::Token_INVALID;

%%%%


namespace python
{

Lexer::Lexer( parser* parser, char* contents)
{
    restart( parser, contents );
}

void Lexer::restart( parser *parser, char *contents  )
{
    m_parser = parser;
    m_locationTable = parser->token_stream->location_table();
    m_contents = contents;
    m_tokenBegin = m_tokenEnd = 0;
    m_currentOffset = 0;
    m_paren = 0;
    m_indent.push_back(0);
    indent_level = dedent_level = 0;
    // check for and ignore the UTF-8 byte order mark
    unsigned char *ucontents = (unsigned char *) m_contents;
    if ( ucontents[0] == 0xEF && ucontents[1] == 0xBB && ucontents[2] == 0xBF )
    {
        m_tokenBegin = m_tokenEnd = 3;
        m_currentOffset = 3;
    }

    yyrestart(NULL);
    BEGIN(INITIAL); // is not set automatically by yyrestart()
}

void Lexer::indent()
{
    int d = m_currentOffset;
    for(;;)
    {
        if( m_contents[ d ] == '\t')
        {
            white_count=white_count+8;
            space_count = 0;
            d++;
        }
        else if( m_contents[ d ] == ' ')
        {
            space_count = space_count + 1;
            d++;
        }
        else if( m_contents[ d ] == '#')
        {
            std::cerr<<"Comment"<<std::endl;
            white_count = 0;
            break;
        }
        else if( m_contents[ d ] == '\n' )
        {
            std::cerr<<"Blank Line"<<std::endl;
            white_count = 0;
            blank_line = 1;
            break;
        }
        else
        {
            white_count = white_count + space_count;
            break;
        }
    }
}


// reads a character, and returns 1 as the number of characters read
// (or 0 when the end of the string is reached)
int Lexer::LexerInput( char *buf, int /*max_size*/ )
{
    int c = m_contents[ m_currentOffset++ ];

    switch(c)
    {
    case '\r':
        c = '\n'; // only have one single line break character: '\n'
        if ( m_contents[m_currentOffset + 1] == '\n' )
        {
            m_currentOffset++;
            m_tokenEnd++;
        }

        // fall through
    case '\n':

        m_locationTable->newline( m_currentOffset );
        break;

    default:
        break;
    }

    return (c == 0) ? 0 : (buf[0] = c, 1);
}

} // end  of namespace python

// kate: space-indent on; indent-width 4; tab-width: 4; replace-tabs on; auto-insert-doxygen on
