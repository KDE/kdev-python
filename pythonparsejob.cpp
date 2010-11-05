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

using namespace KDevelop;

namespace Python
{

TopDUContext* ParseJob::m_internalFunctions;

ParseJob::ParseJob(LanguageSupport* parent, const KUrl &url )
        : KDevelop::ParseJob( url )
        , m_session( new ParseSession )
        , m_ast( 0 )
        , m_readFromDisk( false )
        , m_duContext( 0 )
        , m_url( url )
{
    kDebug();
    m_parent = parent;
    ParseJob::internalFunctionsFile =  new KUrl("/home/sven/projects/kde4/python/documentation/test.py");
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

void ParseJob::checkInternalFunctionsParsed()
{
    if ( ! ParseJob::m_internalFunctions ) {
        DUChain::self()->updateContextForUrl(IndexedString(*internalFunctionsFile), minimumFeatures());
    }
}

void ParseJob::run()
{
    kDebug();
    
    LanguageSupport* lang = python();
    ILanguage* ilang = lang->language();
    QReadLocker parselock(ilang->parseLock());
    UrlParseLock urlLock(document());
    
    if ( m_url != *internalFunctionsFile ) checkInternalFunctionsParsed();

    if (abortRequested() || !python() || !python()->language()) {
        kWarning() << "Language support is NULL";
        return abortJob();
    }

    readContents();
    m_session->setContents( QString::fromUtf8(contents().contents) + "\n" );
    m_session->setCurrentDocument(m_url);
    
    if ( abortRequested() )
        return abortJob();
    
    IndexedString filename = KDevelop::IndexedString(m_url.pathOrUrl());
    
//     {
//         DUChainWriteLocker lock(DUChain::lock());
//         
//         m_duContext = DUChain::self()->chainForDocument(document());
//         if ( ! m_duContext ) {
//             IndexedString langstring("python");
//             ParsingEnvironmentFile* file = new ParsingEnvironmentFile(document());
//             m_duContext = new TopDUContext(document(), RangeInRevision(0, 0, INT_MAX, INT_MAX), file);
//             m_duContext->setType(KDevelop::DUContext::Global);
//             DUChain::self()->addDocumentChain(m_duContext);
//         }
//         m_duContext->clearProblems();
//         
//         ParsingEnvironmentFilePointer file = m_duContext->parsingEnvironmentFile();
//         file.data()->setModificationRevision(contents().modification);
//     }
    
    // 2) parse
    QPair<CodeAst*, bool> parserResults = m_session->parse(m_ast);
    m_ast = parserResults.first;
    
    if ( parserResults.second )
    {
        kDebug() << m_url;
//         AstPrinter printer;
//         printer.visitCode( m_ast );
        if ( abortRequested() )
            return abortJob();

        PythonEditorIntegrator editor;
        DeclarationBuilder builder( &editor );
        
        editor.setParseSession(m_session);
        
        m_duContext = builder.build(filename, m_ast);
        setDuChain(m_duContext);
        
        UseBuilder usebuilder( &editor );
        usebuilder.buildUses(m_ast);
        
        kDebug() << "----Parsing Succeded---***";
        
        if ( m_parent && m_parent->codeHighlighting() ) {
            kDebug() << m_duContext.data();
            DUChainReadLocker lock(DUChain::lock());
            KDevelop::ICodeHighlighting* hl = m_parent->codeHighlighting();
            hl->highlightDUChain(m_duContext);
        }
        
        DUChainWriteLocker lock(DUChain::lock());
        ParsingEnvironmentFilePointer parsingEnvironmentFile = m_duContext->parsingEnvironmentFile();
        parsingEnvironmentFile->setModificationRevision(contents().modification);
        DUChain::self()->updateContextEnvironment(m_duContext, parsingEnvironmentFile.data());
    }
    else
    {
        kWarning() << "===Failed===";
        {
            DUChainReadLocker lock(DUChain::lock());
            m_duContext = DUChain::self()->chainForDocument(document());
        }
        if ( m_duContext ) {
            DUChainWriteLocker lock(DUChain::lock());
            m_duContext->clearProblems();
            m_duContext->parsingEnvironmentFile()->clearModificationRevisions();
        }
        else {
            DUChainWriteLocker lock(DUChain::lock());
            ParsingEnvironmentFile *file = new ParsingEnvironmentFile(document());
            static const IndexedString langString("python");
            file->setModificationRevision(contents().modification);
            file->setLanguage(langString);
            m_duContext = new TopDUContext(document(), RangeInRevision(0, 0, INT_MAX, INT_MAX), file);
            DUChain::self()->addDocumentChain(m_duContext);
        }
        DUChainWriteLocker lock(DUChain::lock());
        foreach ( ProblemPointer p, m_session->m_problems ) {
            kDebug() << "Added problem to context";
            m_duContext->addProblem(p);
        }
        setDuChain(m_duContext);
    }
}

ParseSession *ParseJob::parseSession() const
{
    return m_session;
}

}

#include "pythonparsejob.moc"
// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
