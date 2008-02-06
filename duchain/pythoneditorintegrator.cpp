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

#include "ast.h"

using namespace KTextEditor;

namespace Python
{

EditorIntegrator::EditorIntegrator( ParseSession* session )
    : m_session(session)
{
}

Cursor EditorIntegrator::findPosition( Ast* node , Edge edge ) const
{
    if( edge == BackEdge )
        return Cursor(node->endLine, node->endCol );
    else
        return Cursor(node->startLine, node->startCol);
}

Range EditorIntegrator::findRange( Ast * node, RangeEdge edge )
{
    kDebug() << "Finding Range ==================";
    Q_UNUSED(edge);
    return Range(findPosition(node, FrontEdge), findPosition(node, BackEdge));
}

Range EditorIntegrator::findRange( Ast* from, Ast* to )
{
    return Range(findPosition(from, FrontEdge), findPosition(to, BackEdge));
}

ParseSession * EditorIntegrator::parseSession() const
{
  return m_session;
}

}
