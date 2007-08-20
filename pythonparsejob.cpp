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
#include <QFile>
#include <QByteArray>

#include <ktexteditor/document.h>
#include <ktexteditor/smartinterface.h>

#include <fcntl.h>
#include <sys/stat.h>
#include <sys/mman.h>
#include <klocale.h>
#include "pythonhighlighting.h"
#include "pythoneditorintegrator.h"
#include "Thread.h"
#include "pythonlanguagesupport.h"
#include <parsejob.h>
#include "parsesession.h"
#include "python_parser.h"

#include <duchain.h>
#include <topducontext.h>

#include "contextbuilder.h"
#include "declarationbuilder.h"
using namespace python;
using namespace KDevelop;


PythonParseJob::PythonParseJob( const KUrl &url,PythonLanguageSupport *parent)
            : KDevelop::ParseJob( url, parent )
            , m_session( new ParseSession )
            , m_AST( 0 )
            , m_readFromDisk( false )
            , m_duContext( 0 )
            , m_url(url)
{
}

PythonParseJob::~PythonParseJob()
{}

PythonLanguageSupport *PythonParseJob::python() const
{
    return qobject_cast<PythonLanguageSupport*>(const_cast<QObject*>(parent()));
}


project_ast *PythonParseJob::AST() const
{
    Q_ASSERT(isFinished() && m_AST);
    return m_AST;
}

TopDUContext* PythonParseJob::duChain() const
{
    return m_duContext;
}

bool PythonParseJob::wasReadFromDisk() const
{
    return m_readFromDisk;
}
void PythonParseJob::setDUChain(TopDUContext * duChain)
{
    m_duContext = duChain;
}

void PythonParseJob::setUpdatingContext( const TopDUContextPointer& context ) {
    m_updatingContext = context;
}

TopDUContextPointer PythonParseJob::updatingContext() const {
    return m_updatingContext;
}

void PythonParseJob::run()
{

    m_readFromDisk = !contentsAvailableFromEditor();

    if ( m_readFromDisk )
    {
        QFile file( m_document.path() );
        if ( !file.open( QIODevice::ReadOnly ) )
        {
            m_errorMessage = i18n( "Could not open file '%1'", m_document.path() );
            kWarning() << k_funcinfo << "Could not open file" << m_document
                             << "(path" << m_document.path() << ")";
            return ;
        }

        m_session->setContents( file.readAll() );
        Q_ASSERT ( m_session->size() > 0 );
        file.close();
    }
    else
    {
        m_session->setContents( contentsFromEditor().toAscii() );
    }
    kDebug() << "===-- PARSING --===>"
             << m_document.fileName()
             << "size:" << m_session->size();

    // 0) setup
    //parser python_parser;
    m_session->m_parser->set_token_stream( m_session->token_stream );
    m_session->m_parser->set_memory_pool( m_session->memory_pool );

    // 1) tokenize
    m_session->m_parser->tokenize( (char*) m_session->contents() );

    // 2) parse
    bool matched = m_session->m_parser->parse_project( &m_AST );

    if ( matched )
    {
        kDebug() << m_url;
        DeclarationBuilder declarationBuilder(m_session,m_url);
        m_duContext = declarationBuilder.buildDeclarations(m_AST);
/*        ContextBuilder contextBuilder(m_session,m_url);
        m_duContext = contextBuilder.buildContexts(m_AST);*/
        kDebug() << "----Parsing Succeded---";//TODO: bind declarations to the code model
        if( python() && declarationBuilder.m_editor->smart() )
	{
            QMutexLocker lock(declarationBuilder.m_editor->smart()->smartMutex());
	    python()->codeHighlighting()->highlightDUChain( m_duContext );
	}
    }
    else
    {
        m_session->m_parser->yy_expected_symbol(ast_node::Kind_project, "project");
        kDebug() << "===Failed===";
        return;
    }
}

ParseSession *PythonParseJob::parseSession() const
{
    return m_session;
}
#include "pythonparsejob.moc"
