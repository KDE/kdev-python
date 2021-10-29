/*
    SPDX-FileCopyrightText: 2007 Piyush verma <piyush.verma@gmail.com>
    SPDX-FileCopyrightText: 2011-2012 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
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
    m_indentInformationCache = nullptr;
}

ParseSession* PythonEditorIntegrator::parseSession() const
{
    Q_ASSERT(m_session);
    return m_session;
}

CursorInRevision PythonEditorIntegrator::findPosition(const Ast* node , Edge edge) const
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

RangeInRevision PythonEditorIntegrator::findRange(const Ast * node, RangeEdge edge) const
{
    Q_UNUSED( edge );
    return RangeInRevision( findPosition( node, FrontEdge ), findPosition( node, BackEdge ) );
}

RangeInRevision PythonEditorIntegrator::findRange(const Python::Ast* from, const Python::Ast* to) const
{
    return RangeInRevision( findPosition( from, FrontEdge ), findPosition( to, BackEdge ) );
}

}
