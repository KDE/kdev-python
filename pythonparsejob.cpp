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
// #include <cassert>
#include <QFile>

#include <ktexteditor/document.h>
#include <ktexteditor/smartinterface.h>

#include <klocale.h>
#include "pythonhighlighting.h"
#include <duchainlock.h>
// #include "pythoneditorintegrator.h"
// #include "Thread.h"
#include "pythonlanguagesupport.h"
#include <parsejob.h>
#include "dumpchain.h"
#include "dumpdotgraph.h"
#include "parsesession.h"

#include <duchain.h>
#include <topducontext.h>

#include "contextbuilder.h"
// #include "declarationbuilder.h"

using namespace KDevelop;

namespace Python
{


ParseJob::ParseJob( const KUrl &url,LanguageSupport *parent)
        : KDevelop::ParseJob( url, parent )
        , m_session( new ParseSession )
        , m_ast( 0 )
        , m_readFromDisk( false )
        , m_duContext( 0 )
        , m_url(url)
{
}

ParseJob::~ParseJob()
{
}

LanguageSupport *ParseJob::python() const
{
    return qobject_cast<LanguageSupport*>(const_cast<QObject*>(parent()));
}


CodeAst *ParseJob::ast() const
{
    Q_ASSERT(isFinished() && m_ast);
    return m_ast;
}

TopDUContext* ParseJob::duChain() const
{
    return m_duContext;
}

bool ParseJob::wasReadFromDisk() const
{
    return m_readFromDisk;
}
void ParseJob::setDUChain(TopDUContext * duChain)
{
    m_duContext = duChain;
}

void ParseJob::run()
{

    m_readFromDisk = !contentsAvailableFromEditor();

    if ( m_readFromDisk )
    {
        QFile file( document().str() );
        //TODO: Read the first lines to determine encoding using Python encoding and use that for the text stream
        if ( !file.open( QIODevice::ReadOnly | QIODevice::Text ) )
        {
            m_errorMessage = i18n( "Could not open file '%1'", document().str() );
            kWarning() << "Could not open file" << document().str()
                        << "(path" << document().str() << ")";
            return ;
        }
        QTextStream s(&file);
//         if( codec )
//             s.setCodec( QTextCodec::codecForName(codec) );
        m_session->setContents( s.readAll() );
        Q_ASSERT ( m_session->contents().size() > 0 );
        file.close();
    }
    else
    {
        m_session->setContents( contentsFromEditor().toAscii() );
    }


    // 2) parse
    bool matched = m_session->parse( &m_ast );

    if ( matched )
    {
        kDebug() << m_url;
//         DeclarationBuilder declarationBuilder(m_session,m_url);
        ContextBuilder builder( m_session, m_url );
        m_duContext = builder.buildContexts( m_ast );
//         m_duContext = declarationBuilder.buildDeclarations(m_AST);
        kDebug() << "----Parsing Succeded---***";//TODO: bind declarations to the code model
        
        {
            DUChainReadLocker lock(DUChain::lock());
            DumpChain dump;
            dump.dump(m_duContext);
        }
//         KDevelop::DumpDotGraph dumpGraph;
//         kDebug() << "Dot-Graph:\n" << dumpGraph.dotGraph(m_duContext, true);
//         if( python() && declarationBuilder.m_editor->smart() )
//         {
//             QMutexLocker lock(declarationBuilder.m_editor->smart()->smartMutex());
//             python()->codeHighlighting()->highlightDUChain( m_duContext );
//         }
    }
    else
    {
        kDebug() << "===Failed===";
        return;
    }
}

ParseSession *ParseJob::parseSession() const
{
    return m_session;
}

}

#include "pythonparsejob.moc"
// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
