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

using namespace KTextEditor;

PythonEditorIntegrator::PythonEditorIntegrator( ParseSession* session )
    : m_session(session)
{
}

Cursor PythonEditorIntegrator::findPosition( std::size_t token, Edge edge ) const
{
    kdev_pg_token_stream::token_type const & t = m_session->tokenStream()->token(token);
    return findPosition(t, edge);
}

Cursor PythonEditorIntegrator::findPosition( kdev_pg_token_stream::token_type const & token, Edge edge ) const
{
    std::size_t line, column;

    //kDebug() << "Finding position for offset:" << offset  << m_session->contents()[offset];
    m_session->positionAt((edge == BackEdge) ? token.end : token.begin, &line, &column);
    //kDebug() << "Found position:" << line << column;
    return Cursor(line, column);
}

Range PythonEditorIntegrator::findRange( Python::ast_node * node, RangeEdge edge )
{
    //kDebug() << "Finding Range";
    Q_UNUSED(edge);
    return Range(findPosition(node->start_token, FrontEdge), findPosition(node->end_token -1, BackEdge));
}

Range PythonEditorIntegrator::findRange( Python::ast_node* from, Python::ast_node* to )
{
    return Range(findPosition(from->start_token, FrontEdge), findPosition(to->end_token - 1, BackEdge));
}

Range PythonEditorIntegrator::findRange( kdev_pg_token_stream::token_type const & token )
{
    return Range(findPosition(token, FrontEdge), findPosition(token, BackEdge));
}

QString PythonEditorIntegrator::tokenToString( std::size_t token ) const
{
    kdev_pg_token_stream::token_type const & t = m_session->tokenStream()->token(token);
    return m_session->tokenText(t.begin, t.end);
}


ParseSession * PythonEditorIntegrator::parseSession() const
{
  return m_session;
}
// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
