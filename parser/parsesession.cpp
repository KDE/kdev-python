/*
    SPDX-FileCopyrightText: 2007 Andreas Pakulat <apaku@gmx.de>
    SPDX-FileCopyrightText: 2007 Piyush verma <piyush.verma@gmail.com>
    SPDX-FileCopyrightText: 2010-2014 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#include "parsesession.h"
#include "astbuilder.h"

#include <QDebug>
#include "parserdebug.h"

using namespace KDevelop;

namespace Python
{

ParseSession::ParseSession()
    : ast(nullptr)
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
        qCDebug(KDEV_PYTHON_PARSER) << "Successfully parsed";
    }else
    {
        matched.first.clear();
        qCDebug(KDEV_PYTHON_PARSER) << "Couldn't parse content";
    }
    return matched;
}

}
