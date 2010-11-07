/*****************************************************************************
 * Copyright (c) 2007 Andreas Pakulat <apaku@gmx.de>                         *
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 * Copyright 2010 Sven Brauch <svenbrauch@googlemail.com>                    *
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
#include "parsesession.h"
#include <kdebug.h>

#include "pythondriver.h"
#include <language/duchain/indexedstring.h>
#include "astbuilder.h"

using namespace KDevelop;

namespace Python
{

ParseSession::ParseSession()
{
}
ParseSession::~ParseSession()
{
}

void ParseSession::setCurrentDocument(KUrl& filename)
{
    m_currentDocument = KDevelop::IndexedString(filename);
}

IndexedString ParseSession::currentDocument()
{
    return m_currentDocument;
}


QString ParseSession::contents() const
{
    return m_contents;
}

void ParseSession::setContents( const QString& contents )
{
    m_contents = contents;
}

QPair<CodeAst*, bool> ParseSession::parse( Python::CodeAst* ast )
{
    Driver driver;
    driver.setCurrentDocument(m_currentDocument.toUrl());
    driver.setContent(m_contents);
    QPair<CodeAst*, bool> result = driver.parse(ast);
    m_problems = driver.m_problems;
    return result;
}

}
