/*****************************************************************************
 * Copyright (c) 2007 Andreas Pakulat <apaku@gmx.de>                         *
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 * Copyright 2010-2014 Sven Brauch <svenbrauch@googlemail.com>               *
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
#include "parsesession.h"

#include <KDebug>

#include "astbuilder.h"

using namespace KDevelop;

namespace Python
{

ParseSession::ParseSession()
    : ast(0)
    , m_currentDocument(KDevelop::IndexedString("<invalid>"))
    , m_futureModificationRevision()
{
}
ParseSession::~ParseSession()
{
    ast.clear();
}

void ParseSession::setCurrentDocument(const IndexedString& url)
{
    m_currentDocument = url;
}

IndexedString ParseSession::currentDocument()
{
    return m_currentDocument;
}

const ModificationRevision& ParseSession::futureModificationRevision() const
{
    return m_futureModificationRevision;
}

void ParseSession::setFutureModificationRevision(const ModificationRevision& revision)
{
    m_futureModificationRevision = revision;
}

QString ParseSession::contents() const
{
    return m_contents;
}

void ParseSession::setContents( const QString& contents )
{
    m_contents = contents;
}

QPair<CodeAst::Ptr, bool> ParseSession::parse()
{
    AstBuilder pythonparser;
    QPair<CodeAst::Ptr, bool> matched;
    matched.first = pythonparser.parse(m_currentDocument.toUrl(), m_contents);
    matched.second = matched.first ? true : false; // check whether an AST was returned and react accordingly
    
    m_problems = pythonparser.m_problems;
    
    if( matched.second )
    {
        kDebug() << "Sucessfully parsed";
    }else
    {
        matched.first.clear();
        kDebug() << "Couldn't parse content";
    }
    return matched;
}

}
