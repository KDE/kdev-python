/*****************************************************************************
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 * Copyright 2011-2012 Sven Brauch <svenbrauch@googlemail.com>               *
 *                                                                           *
 * This program is free software; you can redistribute it and/or             *
 * modify it under the terms of the GNU General Public License as            *
 * published by the Free Software Foundation; either version 2 of            *
 * the License, or (at your option) any later version.                       *
 *                                                                           *
 * This program is distributed in the hope that it will be useful,           *
 * but WITHOUT ANY WARRANTY; without even the implied warranty of            *
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             *
 * GNU General Public License for more details.                              *
 *                                                                           *
 * You should have received a copy of the GNU General Public License         *
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.     *
 *****************************************************************************
 */
#include "pythoneditorintegrator.h"
#include <ktexteditor/document.h>

#include <language/editor/documentrange.h>

#include "ast.h"

using namespace KTextEditor;

namespace Python
{

PythonEditorIntegrator::PythonEditorIntegrator(ParseSession* session) :
    m_session(session), m_indentInformationCache(new FileIndentInformation(session->contents()))
{
    
}

PythonEditorIntegrator::~PythonEditorIntegrator() 
{
    delete m_indentInformationCache;
    m_indentInformationCache = 0;
}

ParseSession* PythonEditorIntegrator::parseSession() const
{
    Q_ASSERT(m_session);
    return m_session;
}

CursorInRevision PythonEditorIntegrator::findPosition( Ast* node , Edge edge ) const
{
    Q_ASSERT(node);
    if ( edge == BackEdge )
    {
        // Apparently KTE expects a range to go until _after_ the last character that should be included
        // however the parser calculates endCol as the index _before_ the last included character, so adjust here
        return CursorInRevision( node->endLine, node->endCol+1 );
    }else
    {
        return CursorInRevision( node->startLine, node->startCol );
    }
}

RangeInRevision PythonEditorIntegrator::findRange( Ast * node, RangeEdge edge ) const
{
    Q_UNUSED( edge );
    return RangeInRevision( findPosition( node, FrontEdge ), findPosition( node, BackEdge ) );
}

RangeInRevision PythonEditorIntegrator::findRange( Ast* from, Ast* to ) const
{
    return RangeInRevision( findPosition( from, FrontEdge ), findPosition( to, BackEdge ) );
}

}
