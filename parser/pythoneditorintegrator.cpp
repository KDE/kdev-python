/*****************************************************************************
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
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
#include "pythoneditorintegrator.h"
#include "parsesession.h"
#include <ktexteditor/document.h>
#include <ktexteditor/smartrange.h>
#include <ktexteditor/smartinterface.h>

#include <documentrange.h>
#include <documentrangeobject.h>

#include "python_ast.h"
#include "python_parser.h"
using namespace KTextEditor;
using namespace python;

PythonEditorIntegrator::PythonEditorIntegrator( ParseSession* session )
    : m_session(session)
{
}

Cursor PythonEditorIntegrator::findPosition( std::size_t token, Edge edge ) const
{
    parser::token_type const & t = m_session->token_stream->token(token);
    return findPosition(t, edge);
}

Cursor PythonEditorIntegrator::findPosition( parser::token_type const & token, Edge edge ) const
{
    std::size_t line, column;
    size_t index = m_session->token_stream->index();

    m_session->positionAt((edge == BackEdge) ? token.end : token.begin, &line, &column);
    return Cursor(line, column);
}

Range PythonEditorIntegrator::findRange( ast_node * node, RangeEdge edge )
{
    kDebug() << "Finding Range";
    Q_UNUSED(edge);
    kDebug() << tokenToString(node->start_token) ;
    kDebug() << tokenToString(node->end_token) ;
    return Range(findPosition(node->start_token, FrontEdge), findPosition(node->end_token, BackEdge));
}

Range PythonEditorIntegrator::findRange(ast_node* from, ast_node* to)
{
    return Range(findPosition(from->start_token, FrontEdge), findPosition(to->end_token, BackEdge));
}

Range PythonEditorIntegrator::findRange( parser::token_type const & token )
{
    return Range(findPosition(token, FrontEdge), findPosition(token, BackEdge));
}

QString PythonEditorIntegrator::tokenToString(std::size_t token) const
{
    parser::token_type const & t = m_session->token_stream->token(token);
    size_t tokenLength = t.end - t.begin;
    char *tokenValue = new char[tokenLength+1];
    strncpy(tokenValue, m_session->m_parser->tokenText(t.begin), tokenLength);
    tokenValue[tokenLength] = 0;
    return tokenValue;
}


ParseSession * PythonEditorIntegrator::parseSession() const
{
  return m_session;
}
