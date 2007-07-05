/*****************************************************************************
 * Copyright (c) 2007 Andreas Pakulat <apaku@gmx.de>                         *
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
#include "pythonparsejob.h"
#include <kdebug.h>
#include <cassert>
#include "Thread.h"
#include "pythonlanguagesupport.h"
#include <parsejob.h>
#include "parsesession.h"
#include <python_parser.h>

PythonParseJob::PythonParseJob( const KUrl &url,PythonLanguageSupport *parent)
            : KDevelop::ParseJob( url, parent )
            , m_session( new ParseSession )
            , m_AST( 0 )
{
}

PythonParseJob::~PythonParseJob()
{}

PythonLanguageSupport *PythonParseJob::python() const
{
    return qobject_cast<PythonLanguageSupport*>(const_cast<QObject*>(parent()));
}

ParseSession *PythonParseJob::parseSession() const
{
    return m_session;
}

void PythonParseJob::run()
{
    kDebug() << "===-- PARSING --===> "
             << endl;
}

#include "pythonparsejob.moc"
