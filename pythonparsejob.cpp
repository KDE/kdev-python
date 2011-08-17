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
#include <language/backgroundparser/urlparselock.h>

#include "pythonhighlighting.h"
#include "pythoneditorintegrator.h"
#include "dumpchain.h"
#include "parsesession.h"
#include "pythonlanguagesupport.h"
// #include "contextbuilder.h"
#include "declarationbuilder.h"
#include "usebuilder.h"
// #include "astprinter.h"
// #include "usebuilder.h"
#include <language/highlighting/codehighlighting.h>
#include <interfaces/icore.h>
#include <interfaces/ilanguagecontroller.h>
#include <language/duchain/indexedstring.h>
#include <language/backgroundparser/backgroundparser.h>

using namespace KDevelop;

namespace Python
{

TopDUContext* ParseJob::m_internalFunctions;

ParseJob::ParseJob(LanguageSupport* parent, const KUrl &url )
        : KDevelop::ParseJob( url )
        , m_session( 0 )
        , m_ast( 0 )
        , m_readFromDisk( false )
        , m_duContext( 0 )
        , m_url( url )
{
    kDebug();
    m_parent = parent;
    ParseJob::m_internalFunctions = 0;
}

ParseJob::~ParseJob()
{
}

LanguageSupport *ParseJob::python() const
{
    return LanguageSupport::self();
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
    qDebug() << " ====> PARSING ====> " << m_url;

    m_session = new ParseSession();    
    LanguageSupport* lang = python();
    ILanguage* ilang = lang->language();
    
    if ( !python() || !python()->language()) {
        kWarning() << "Language support is NULL";
        return abortJob();
    }
    
    if ( abortRequested() ) return abortJob();
    
    QReadLocker parselock(ilang->parseLock());
    UrlParseLock urlLock(document());
    
    readContents();
    
    m_session->setContents( QString::fromUtf8(contents().contents) + "\n" ); // append a newline in case the parser doesnt like it without one
    Q_ASSERT(m_url.isValid());
    m_session->setCurrentDocument(m_url);
    kDebug() << "MODIFICATION: " << contents().modification;
    kDebug() << contents().modification.modificationTime << contents().modification.revision;
    
    if ( abortRequested() )
        return abortJob();
    
    IndexedString filename = KDevelop::IndexedString(m_url.pathOrUrl());
    
    // 2) parse
    QPair<CodeAst*, bool> parserResults = m_session->parse(m_ast);
    m_ast = parserResults.first;
    
    if ( parserResults.second )
    {
        Q_ASSERT(m_url.isValid());
//         AstPrinter printer;
//         printer.visitCode( m_ast );
        if ( abortRequested() )
            return abortJob();
        
        QSharedPointer<PythonEditorIntegrator> editor = QSharedPointer<PythonEditorIntegrator>(new PythonEditorIntegrator());
        editor->setParseSession(m_session);
        DeclarationBuilder builder( editor.data() );
        builder.m_currentlyParsedDocument = filename;
        builder.m_futureModificationRevision = contents().modification;
        
        Q_ASSERT(m_session->currentDocument().toUrl().isValid());
        m_duContext = builder.build(filename, m_ast, m_duContext);
        bool needsReparse = builder.m_hasUnresolvedImports;
        setDuChain(m_duContext);
        
        if ( abortRequested() )
            return abortJob();
        Q_ASSERT(m_session->currentDocument().toUrl().isValid());
        UseBuilder usebuilder( editor.data() );
        usebuilder.m_currentlyParsedDocument = filename;
        usebuilder.buildUses(m_ast);
        
        if ( abortRequested() )
            return abortJob();
        qDebug() << "Document needs update because of unresolved identifiers: " << needsReparse;
        if ( needsReparse ) {
            if ( ! ( minimumFeatures() & Rescheduled ) && KDevelop::ICore::self()->languageController()->backgroundParser()->queuedCount() ) {
                DUChainWriteLocker lock(DUChain::lock());
                m_duContext->setFeatures(minimumFeatures());
                KDevelop::ICore::self()->languageController()->backgroundParser()->addDocument(document().toUrl(), 
                                     static_cast<TopDUContext::Features>(minimumFeatures() | Rescheduled), 10000);
            }
        }
        
        if ( abortRequested() )
            return abortJob();
        {
            DUChainWriteLocker lock(DUChain::lock());
            m_duContext->setFeatures(minimumFeatures());
            ParsingEnvironmentFilePointer parsingEnvironmentFile = m_duContext->parsingEnvironmentFile();
//             parsingEnvironmentFile->clearModificationRevisions();
            parsingEnvironmentFile->setModificationRevision(contents().modification);
            DUChain::self()->updateContextEnvironment(m_duContext, parsingEnvironmentFile.data());
        }
        
        kDebug() << "----Parsing Succeded---***";
        
        if ( abortRequested() )
            return abortJob();
        if ( m_parent && m_parent->codeHighlighting() ) {
            kDebug() << "Starting highlighter...";
            KDevelop::ICodeHighlighting* hl = m_parent->codeHighlighting();
            hl->highlightDUChain(m_duContext);
        }
    }
    else
    {
        kWarning() << "===Failed===";
        if ( abortRequested() )
            return abortJob();
        DUChainWriteLocker lock;
        m_duContext = DUChain::self()->chainForDocument(document());
        if ( m_duContext ) {
            m_duContext->parsingEnvironmentFile()->clearModificationRevisions();
            m_duContext->clearProblems();
        }
        else {
            ParsingEnvironmentFile *file = new ParsingEnvironmentFile(document());
            static const IndexedString langString("python");
            file->setLanguage(langString);
            m_duContext = new TopDUContext(document(), RangeInRevision(0, 0, INT_MAX, INT_MAX), file);
            DUChain::self()->addDocumentChain(m_duContext);
        }
        
        setDuChain(m_duContext);
    }
    
    if ( abortRequested() )
            return abortJob();
    
    DUChainWriteLocker lock(DUChain::lock());
    foreach ( ProblemPointer p, m_session->m_problems ) {
        kDebug() << "Added problem to context";
        m_duContext->addProblem(p);
    }
    
    setDuChain(m_duContext);
    
//     DUChainWriteLocker lock(DUChain::lock());
//     if ( ! DUChain::self()->chainForDocument(document()) && m_duContext ) {
//         DUChain::self()->addDocumentChain(m_duContext);
//     }
    
}

ParseSession *ParseJob::parseSession() const
{
    return m_session;
}

}

#include "pythonparsejob.moc"
// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
