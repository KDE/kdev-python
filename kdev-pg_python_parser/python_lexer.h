/*****************************************************************************
 * Copyright (c) 2006 Andreas Pakulat <apaku@gmx.de>                         *
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *                                                                                *
 *                                                                           *
 * Permission is hereby granted, free of charge, to any person obtaining     *
 * a copy of this software and associated documentation files (the           *
 * "Software"), to deal in the Software without restriction, including       *
 * without limitation the rights to use, copy, modify, merge, publish,       *
 * distribute, sublicense, and/or sell copies of the Software, and to        *
 * permit persons to whom the Software is furnished to do so, subject to     *
 * the following conditions:                                                 *
 *                                                                           *
 * The above copyright notice and this permission notice shall be            *
 * included in all copies or substantial portions of the Software.           *
 *                                                                           *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,           *
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF        *
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND                     *
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE    *
 * LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION    *
 * OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION     *
 * WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.           *
 *****************************************************************************/

#include <iostream>
#include <stack>
#include <string>
#include "python_parser.h"


#ifndef DONT_INCLUDE_FLEXLEXER
#include <FlexLexer.h>
#endif

// The YY_USER_ACTION macro is called whenever a token is found by Flex
#define YY_USER_ACTION \
m_tokenBegin = m_tokenEnd; \
m_tokenEnd += yyleng;

namespace python
{

class Lexer : public yyFlexLexer
{
public:
    Lexer( python::parser *parser, char *contents  );
    void restart( python::parser *parser, char *contents );
    void indent( int a);
    void indent_tab(int a);
    int dedent();		
    int yylex();
    int indent_level;
    char *contents()         { return m_contents;   }
    std::stack<int> m_indent;	
    std::size_t tokenBegin() { return m_tokenBegin; }
    std::size_t tokenEnd()   { return m_tokenEnd;   }

protected:
    // custom input, replacing the Flex default input stdin
    virtual int LexerInput( char *buf, int max_size );

    // dismisses any lexer output (which should not happen anyways)
    virtual void LexerOutput( const char * /*buf*/, int /*max_size*/ ) { return; }
    virtual void LexerError( const char */*msg*/ ) { return; }

private:
    python::parser* m_parser;
    char *m_contents;
    int  white_count;
    int dedent_level;
    std::size_t m_tokenBegin, m_tokenEnd;
    std::size_t m_currentOffset;
    int m_white_count;	
    kdev_pg_location_table *m_locationTable;
};

} // end of namespace python


