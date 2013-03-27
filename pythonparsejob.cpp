/*****************************************************************************
 * Copyright (c) 2007 Andreas Pakulat <apaku@gmx.de>                         *
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 * Copyright (c) 2010-2012 Sven Brauch <svenbrauch@googlemail.com>           *
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

#include "pythonhighlighting.h"
#include "pythoneditorintegrator.h"
#include "dumpchain.h"
#include "parsesession.h"
#include "pythonlanguagesupport.h"
#include "declarationbuilder.h"
#include "usebuilder.h"

#include <language/duchain/duchainlock.h>
#include <language/duchain/duchain.h>
#include <language/duchain/topducontext.h>
#include <language/duchain/dumpdotgraph.h>
#include <language/duchain/indexedstring.h>
#include <language/duchain/duchainutils.h>
#include <language/backgroundparser/urlparselock.h>
#include <language/backgroundparser/backgroundparser.h>
#include <language/highlighting/codehighlighting.h>
#include <language/interfaces/iastcontainer.h>
#include <interfaces/ilanguage.h>
#include <interfaces/foregroundlock.h>
#include <interfaces/icore.h>
#include <interfaces/ilanguagecontroller.h>

#include <ktexteditor/document.h>
#include <ktexteditor/smartinterface.h>

#include <QReadLocker>
#include <QFile>
#include <QThread>
#include <QProcess>
#include <kdebug.h>
#include <klocale.h>
#include <KConfigGroup>

using namespace KDevelop;

namespace Python
{

ParseJob::ParseJob(const IndexedString &url, ILanguageSupport* languageSupport)
        : KDevelop::ParseJob(url, languageSupport)
        , m_ast(0)
        , m_readFromDisk(false)
        , m_duContext(0)
{
}

ParseJob::~ParseJob()
{
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
    ParseSession* currentSession = new ParseSession();
    
    if ( abortRequested() || ICore::self()->shuttingDown() ) {
        delete currentSession;
        return abortJob();
    }
    
    qDebug() << " ====> PARSING ====> parsing file " << document().toUrl() << "; has priority" << parsePriority();
    
    // lock the URL so no other parse job can run on this document
    QReadLocker parselock(languageSupport()->language()->parseLock());
    UrlParseLock urlLock(document());
    
    readContents();
    
    if ( !(minimumFeatures() & TopDUContext::ForceUpdate || minimumFeatures() & Rescheduled) ) {
        DUChainReadLocker lock(DUChain::lock());
        static const IndexedString langString("python");
        foreach(const ParsingEnvironmentFilePointer &file, DUChain::self()->allEnvironmentFiles(document())) {
            if ( file->language() != langString ) {
                continue;
            }
            if ( ! file->needsUpdate() && file->featuresSatisfied(minimumFeatures()) && file->topContext() ) {
                qDebug() << " ====> NOOP    ====> Already up to date:" << document().str();
                setDuChain(file->topContext());
                if ( ICore::self()->languageController()->backgroundParser()->trackerForUrl(document()) ) {
                    lock.unlock();
                    highlightDUChain();
                }
                delete currentSession;
                return;
            }
            break;
        }
    }
    
    ReferencedTopDUContext toUpdate = 0;
    {
        DUChainReadLocker lock;
        toUpdate = DUChainUtils::standardContextForUrl(document().toUrl());
    }
    if ( toUpdate ) {
        translateDUChainToRevision(toUpdate);
        toUpdate->setRange(RangeInRevision(0, 0, INT_MAX, INT_MAX));
    }
    
    currentSession->setContents(QString::fromUtf8(contents().contents));
    currentSession->setCurrentDocument(document());
    
    // call the python API and the AST transformer to populate the syntax tree
    QPair<CodeAst*, bool> parserResults = currentSession->parse(m_ast);
    m_ast = parserResults.first;
    
    if ( abortRequested() ) {
        delete currentSession;
        return abortJob();
    }
    
    QSharedPointer<PythonEditorIntegrator> editor = QSharedPointer<PythonEditorIntegrator>(
        new PythonEditorIntegrator(currentSession)
    );
    // if parsing succeeded, continue and do semantic analysis
    if ( parserResults.second )
    {
        // set up the declaration builder, it gets the parsePriority so it can re-schedule imported files with a better priority
        DeclarationBuilder builder(editor.data());
        builder.m_ownPriority = parsePriority();
        builder.m_currentlyParsedDocument = document();
        builder.m_futureModificationRevision = contents().modification;
        
        // Run the declaration builder. If necessary, it will run itself again.
        m_duContext = builder.build(document(), m_ast, toUpdate.data());
        if ( abortRequested() ) {
            delete currentSession;
            return abortJob();
        }
        
        setDuChain(m_duContext);
        
        // gather uses of variables and functions on the document
        UseBuilder usebuilder(editor.data());
        usebuilder.m_currentlyParsedDocument = document();
        usebuilder.buildUses(m_ast);
        
        // check whether any unresolved imports were encountered
        bool needsReparse = ! builder.m_unresolvedImports.isEmpty();
        kDebug() << "Document needs update because of unresolved identifiers: " << needsReparse;
        if ( needsReparse ) {
            // check whether one of the imports is queued for parsing, this is to avoid deadlocks
            // it's also ok if the duchain is now available (and thus has been parsed before already)
            bool dependencyInQueue = false;
            DUChainWriteLocker lock(DUChain::lock());
            foreach ( const IndexedString& url, builder.m_unresolvedImports ) {
                dependencyInQueue = KDevelop::ICore::self()->languageController()->backgroundParser()->isQueued(url);
                dependencyInQueue = dependencyInQueue || DUChain::self()->chainForDocument(url);
                if ( dependencyInQueue ) {
                    break;
                }
            }
            // we check whether this document already has been re-scheduled once and abort if that is the case
            // this prevents infinite loops in case something goes wrong (optimally, shouldn't reach here if
            // the document was already rescheduled, but there's many cases where this might still happen)
            if ( ! ( minimumFeatures() & Rescheduled ) && dependencyInQueue ) {
                KDevelop::ICore::self()->languageController()->backgroundParser()->addDocument(document(),
                                     static_cast<TopDUContext::Features>(TopDUContext::ForceUpdate | Rescheduled), parsePriority(),
                                     0, ParseJob::FullSequentialProcessing);
            }
        }
        
        // some internal housekeeping work
        {
            DUChainWriteLocker lock(DUChain::lock());
            m_duContext->setFeatures(minimumFeatures());
            ParsingEnvironmentFilePointer parsingEnvironmentFile = m_duContext->parsingEnvironmentFile();
            parsingEnvironmentFile->setModificationRevision(contents().modification);
            DUChain::self()->updateContextEnvironment(m_duContext, parsingEnvironmentFile.data());
        }
        
        kDebug() << "---- Parsing Succeeded ----";
        
        if ( abortRequested() ) {
            delete currentSession;
            return abortJob();
        }
        
        // start the code highlighter if parsing was successful.
        highlightDUChain();
    }
    else {
        // No syntax tree was received from the parser, the expected reason for this is a syntax error in the document.
        kWarning() << "---- Parsing FAILED ----";
        DUChainWriteLocker lock;
        m_duContext = toUpdate.data();
        // if there's already a chain for the document, do some cleanup.
        if ( m_duContext ) {
//             m_duContext->parsingEnvironmentFile()->clearModificationRevisions(); // TODO why?
            ParsingEnvironmentFilePointer parsingEnvironmentFile = m_duContext->parsingEnvironmentFile();
            parsingEnvironmentFile->setModificationRevision(contents().modification);
            m_duContext->clearProblems();
        }
        // otherwise, create a new, empty top context for the file. This serves as a placeholder until
        // the syntax is fixed; for example, it prevents the document from being reparsed again until it is modified.
        else {
            ParsingEnvironmentFile* file = new ParsingEnvironmentFile(document());
            static const IndexedString langString("python");
            file->setLanguage(langString);
            m_duContext = new TopDUContext(document(), RangeInRevision(0, 0, INT_MAX, INT_MAX), file);
            m_duContext->setType(DUContext::Global);
            DUChain::self()->addDocumentChain(m_duContext);
            Q_ASSERT(m_duContext->type() == DUContext::Global);
        }
        
        setDuChain(m_duContext);
    }
    
    if ( abortRequested() ) {
        delete currentSession;
        return abortJob();
    }
    
    // The parser might have given us some syntax errors, which are now added to the document.
    DUChainWriteLocker lock(DUChain::lock());
    foreach ( const ProblemPointer& p, currentSession->m_problems ) {
        m_duContext->addProblem(p);
    }

    // If enabled, do PEP8 checking.
    KConfig config("kdevpythonsupportrc");
    KConfigGroup configGroup = config.group("pep8");
    if ( configGroup.readEntry<bool>("pep8enabled", false) ) {
        kDebug() << "doing pep8 checking";
        QString url = configGroup.readEntry("pep8url", "/usr/bin/pep8-python2");
        QFileInfo f(url);
        bool error = false;
        if ( ! f.isExecutable() ) {
            error = true;
        }
        QProcess process;
        process.setProcessChannelMode(QProcess::MergedChannels);
        process.start(url, QStringList() << document().str());
        process.waitForFinished(1000);
        if ( process.state() != QProcess::NotRunning || ( process.exitCode() != 0 && process.exitCode() != 1 )  ) {
            process.kill();
            error = true;
        }
        else {
            QByteArray data = process.readAll();
            QList<QByteArray> errors = data.split('\n');
            QRegExp errorFormat("(.*):(\\d*):(\\d*): (.*)", Qt::CaseInsensitive, QRegExp::RegExp2);
            foreach ( const QByteArray& error, errors ) {
                if ( errorFormat.exactMatch(error.data()) ) {
                    const QStringList texts = errorFormat.capturedTexts();
                    bool lineno_ok = false;
                    bool colno_ok = false;
                    int lineno = texts.at(2).toInt(&lineno_ok);
                    int colno = texts.at(3).toInt(&colno_ok);
                    if ( ! lineno_ok || ! colno_ok ) {
                        kDebug() << "invalid line / col number:" << texts;
                        continue;
                    }
                    QString error = texts.at(4);
                    KDevelop::Problem *p = new KDevelop::Problem();
                    p->setFinalLocation(DocumentRange(document(), SimpleRange(lineno - 1, qMax(colno - 4, 0),
                                                                              lineno - 1, colno + 4)));
                    p->setSource(KDevelop::ProblemData::Preprocessor);
                    p->setSeverity(KDevelop::ProblemData::Warning);
                    p->setDescription(i18n("PEP8 checker error: %1", error));
                    ProblemPointer ptr(p);
                    m_duContext->addProblem(ptr);
                }
                else {
                    kDebug() << "invalid pep8 error line:" << error;
                }
            }
        }
        if ( error ) {
            KDevelop::Problem *p = new KDevelop::Problem();
            p->setFinalLocation(DocumentRange(document(), SimpleRange(0, 0, 0, 0)));
            p->setSource(KDevelop::ProblemData::Preprocessor);
            p->setSeverity(KDevelop::ProblemData::Warning);
            p->setDescription(i18n("The selected PEP8 syntax checker \"%1\" does not seem to work correctly.", url));
            ProblemPointer ptr(p);
            m_duContext->addProblem(ptr);
        }
    }
    
    if ( minimumFeatures() & TopDUContext::AST ) {
        DUChainWriteLocker lock;
        currentSession->ast = m_ast;
        m_duContext->setAst(KSharedPtr<IAstContainer>(currentSession));
    }
    else {
        delete currentSession;
    }
    
    setDuChain(m_duContext);
}

}

#include "pythonparsejob.moc"
// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
