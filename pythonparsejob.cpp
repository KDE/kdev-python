/*****************************************************************************
 * Copyright (c) 2007 Andreas Pakulat <apaku@gmx.de>                         *
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 *                                                                           *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
 * 02110-1301, USA.
 *****************************************************************************/
#include "pythonparsejob.h"
#include <QFile>
#include <QThread>
#include <QReadLocker>

#include <ktexteditor/document.h>
#include <ktexteditor/smartinterface.h>

#include <kdebug.h>
#include <klocale.h>

#include <language/duchain/duchainlock.h>
#include <language/duchain/duchain.h>
#include <language/duchain/topducontext.h>
#include <language/duchain/dumpdotgraph.h>
#include <interfaces/ilanguage.h>

#include "pythonhighlighting.h"
#include "pythoneditorintegrator.h"
#include "dumpchain.h"
#include "parsesession.h"
#include "pythonlanguagesupport.h"
// #include "contextbuilder.h"
#include "declarationbuilder.h"
#include "astprinter.h"

using namespace KDevelop;

namespace Python
{


ParseJob::ParseJob( const KUrl &url, LanguageSupport *parent )
        : KDevelop::ParseJob( url, parent )
        , m_session( new ParseSession )
        , m_ast( 0 )
        , m_readFromDisk( false )
        , m_duContext( 0 )
        , m_url( url )
{
    kDebug();
}

ParseJob::~ParseJob()
{
}

LanguageSupport *ParseJob::python() const
{
    return qobject_cast<LanguageSupport*>( const_cast<QObject*>( parent() ) );
}


CodeAst *ParseJob::ast() const
{
    Q_ASSERT( isFinished() && m_ast );
    return m_ast;
}

bool ParseJob::wasReadFromDisk() const
{
    return m_readFromDisk;
}

void ParseJob::run()
{
    kDebug();

    if ( abortRequested() )
        return abortJob();

    QReadLocker lock(python()->language()->parseLock());
    m_readFromDisk = !contentsAvailableFromEditor();

    if ( m_readFromDisk )
    {
        QFile file( document().str() );
        //TODO: Read the first lines to determine encoding using Python encoding and use that for the text stream

        if ( !file.open( QIODevice::ReadOnly | QIODevice::Text ) )
        {
            KDevelop::ProblemPointer p(new KDevelop::Problem());
            p->setSource(KDevelop::ProblemData::Disk);
            p->setDescription( i18n( "Could not open file '%1'", document().str() ) );
            switch (file.error()) {
                case QFile::ReadError:
                    p->setExplanation(i18n("File could not be read from."));
                    break;
                case QFile::OpenError:
                    p->setExplanation(i18n("File could not be opened."));
                    break;
                case QFile::PermissionsError:
                    p->setExplanation(i18n("File permissions prevent opening for read.")); 
                    break;
                default:
                    break;
            }
            p->setFinalLocation(KDevelop::DocumentRange(document().str(), KTextEditor::Cursor(0,0), KTextEditor::Cursor(0,0)));
            // TODO addProblem(p);
            kWarning( 9007 ) << "Could not open file " << document().str()
                             << " (path " << document().str() << ")" << endl;
            return ;

        }

        QTextStream s( &file );

//         if( codec )
//             s.setCodec( QTextCodec::codecForName(codec) );
        m_session->setContents( s.readAll() );
        Q_ASSERT( m_session->contents().size() > 0 );
        file.close();
    }
    else
    {
        m_session->setContents( contentsFromEditor().toAscii() );
    }

    if ( abortRequested() )
        return abortJob();

    // 2) parse
    bool matched = m_session->parse( &m_ast );

    if ( matched )
    {
        kDebug() << m_url;
        AstPrinter printer;
        printer.visitCode( m_ast );
        {

            if ( abortRequested() )
                return abortJob();

            EditorIntegrator editor;
            DeclarationBuilder builder( &editor );
            m_duContext = builder.build( KDevelop::IndexedString(m_url.pathOrUrl()), m_ast );

            kDebug() << "----Parsing Succeded---***";

            {
                DUChainReadLocker lock( DUChain::lock() );
                DumpChain dump;
                dump.dump( m_duContext );
            }
        }
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
