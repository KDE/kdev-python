/*****************************************************************************
 * Copyright (c) 2007 Andreas Pakulat <apaku@gmx.de>                         *
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 * Copyright (c) 2010-2013 Sven Brauch <svenbrauch@googlemail.com>           *
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
#include "pythonparsejob.h"

#include "pythonhighlighting.h"
#include "pythoneditorintegrator.h"
#include "dumpchain.h"
#include "parsesession.h"
#include "pythonlanguagesupport.h"
#include "declarationbuilder.h"
#include "usebuilder.h"
#include "checks/controlflowgraphbuilder.h"
#include "checks/dataaccessvisitor.h"
#include "kshell.h"

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
#include <language/checks/controlflowgraph.h>
#include <language/checks/dataaccessrepository.h>
#include <interfaces/ilanguage.h>
#include <interfaces/icore.h>
#include <interfaces/ilanguagecontroller.h>
#include <interfaces/idocumentcontroller.h>
#include <util/foregroundlock.h>

#include <ktexteditor/document.h>

#include <QReadLocker>
#include <QFile>
#include <QThread>
#include <QProcess>
#include <QTemporaryFile>
#include <QDebug>
#include <klocale.h>
#include <KConfigGroup>

using namespace KDevelop;

namespace Python
{

ParseJob::ParseJob(const IndexedString &url, ILanguageSupport* languageSupport)
        : KDevelop::ParseJob(url, languageSupport)
        , m_ast(0)
        , m_duContext(0)
{
}

ParseJob::~ParseJob()
{
}

CodeAst *ParseJob::ast() const
{
    Q_ASSERT( isFinished() && m_ast );
    return m_ast.data();
}

void ParseJob::run()
{
    if ( abortRequested() || ICore::self()->shuttingDown() ) {
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
    
    m_currentSession = new ParseSession();
    m_currentSession->setContents(QString::fromUtf8(contents().contents));
    m_currentSession->setCurrentDocument(document());
    
    // call the python API and the AST transformer to populate the syntax tree
    QPair<CodeAst::Ptr, bool> parserResults = m_currentSession->parse();
    m_ast = parserResults.first;

    auto editor = QSharedPointer<PythonEditorIntegrator>(new PythonEditorIntegrator(m_currentSession.data()));
    // if parsing succeeded, continue and do semantic analysis
    if ( parserResults.second )
    {
        // set up the declaration builder, it gets the parsePriority so it can re-schedule imported files with a better priority
        DeclarationBuilder builder(editor.data(), parsePriority());
        builder.setCurrentlyParsedDocument(document());
        builder.setFutureModificationRevision(contents().modification);

        // Run the declaration builder. If necessary, it will run itself again.
        m_duContext = builder.build(document(), m_ast.data(), toUpdate.data());
        if ( abortRequested() ) {
            return abortJob();
        }
        
        setDuChain(m_duContext);
        
        // gather uses of variables and functions on the document
        UseBuilder usebuilder(editor.data());
        usebuilder.setCurrentlyParsedDocument(document());
        usebuilder.buildUses(m_ast.data());
        
        // check whether any unresolved imports were encountered
        bool needsReparse = ! builder.unresolvedImports().isEmpty();
        qDebug() << "Document needs update because of unresolved identifiers: " << needsReparse;
        if ( needsReparse ) {
            // check whether one of the imports is queued for parsing, this is to avoid deadlocks
            // it's also ok if the duchain is now available (and thus has been parsed before already)
            bool dependencyInQueue = false;
            DUChainWriteLocker lock;
            foreach ( const IndexedString& url, builder.unresolvedImports() ) {
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
        
        qDebug() << "---- Parsing Succeeded ----";
        
        if ( abortRequested() ) {
            return abortJob();
        }
        
        // start the code highlighter if parsing was successful.
        highlightDUChain();
    }
    else {
        // No syntax tree was received from the parser, the expected reason for this is a syntax error in the document.
        qWarning() << "---- Parsing FAILED ----";
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
        return abortJob();
    }
    
    // The parser might have given us some syntax errors, which are now added to the document.
    DUChainWriteLocker lock;
    foreach ( const ProblemPointer& p, m_currentSession->m_problems ) {
        m_duContext->addProblem(p);
    }

    // If enabled, and if the document is open, do PEP8 checking.
    eventuallyDoPEP8Checking(document(), m_duContext);
    
    if ( minimumFeatures() & TopDUContext::AST ) {
        DUChainWriteLocker lock;
        m_currentSession->ast = m_ast;
        m_duContext->setAst(KSharedPtr<IAstContainer>::staticCast(m_currentSession));
    }
    
    setDuChain(m_duContext);
}

ControlFlowGraph* ParseJob::controlFlowGraph()
{
    if ( ! m_currentSession ) {
        return nullptr;
    }
    auto graph = new ControlFlowGraph();
    ControlFlowGraphBuilder builder(m_duContext, graph, m_currentSession);
    builder.visitNode(m_ast.data());
    return graph;
}

DataAccessRepository* ParseJob::dataAccessInformation()
{
    if ( ! m_currentSession ) {
        return nullptr;
    }
    auto repo = new DataAccessRepository();
    DataAccessVisitor builder(m_duContext, repo, m_currentSession);
    builder.visitNode(m_ast.data());
    return repo;
}

void ParseJob::eventuallyDoPEP8Checking(const IndexedString document, TopDUContext* topContext)
{
    IDocument* idoc = ICore::self()->documentController()->documentForUrl(document.toUrl());
    if ( ! idoc || ! topContext || ! idoc->textDocument() || topContext->features() & PEP8Checking ) {
        return;
    }

    KConfig config("kdevpythonsupportrc");
    KConfigGroup configGroup = config.group("pep8");
    if ( ! configGroup.readEntry<bool>("pep8enabled", false) ) {
        return;
    }
    {
        DUChainWriteLocker lock;
        topContext->setFeatures((TopDUContext::Features) ( topContext->features() | PEP8Checking ));
    }
    qDebug() << "doing pep8 checking";
    // TODO that's not very elegant, better would be making pep8 read from stdin -- but it doesn't support that atm
    QTemporaryFile tempfile;
    tempfile.open();
    tempfile.write(idoc->textDocument()->text().toUtf8());
    tempfile.close();
    QString url = configGroup.readEntry("pep8url", "/usr/bin/pep8-python2");
    QString arguments = configGroup.readEntry("pap8arguments", "");
    QFileInfo f(url);
    bool error = false;
    if ( ! f.isExecutable() ) {
        error = true;
    }
    // create a string that contains the command to call pep8 with the given arguments
    QStringList commandArgs = (QStringList() << tempfile.fileName() << KShell::splitArgs(arguments));
    QProcess process;
    process.setProcessChannelMode(QProcess::MergedChannels);
    // call the pep8 command
    process.start(url, commandArgs);
    process.waitForFinished(1000);
    if ( process.state() != QProcess::NotRunning || ( process.exitCode() != 0 && process.exitCode() != 1 )  ) {
        process.kill();
        error = true;
    }
    else {
        QByteArray data = process.readAll();
        QList<QByteArray> errors = data.split('\n');
        QRegExp errorFormat("(.*):(\\d*):(\\d*): (.*)", Qt::CaseInsensitive, QRegExp::RegExp2);
        DUChainWriteLocker lock;
        foreach ( const QByteArray& error, errors ) {
            if ( errorFormat.exactMatch(error.data()) ) {
                const QStringList texts = errorFormat.capturedTexts();
                bool lineno_ok = false;
                bool colno_ok = false;
                int lineno = texts.at(2).toInt(&lineno_ok);
                int colno = texts.at(3).toInt(&colno_ok);
                if ( ! lineno_ok || ! colno_ok ) {
                    qDebug() << "invalid line / col number:" << texts;
                    continue;
                }
                QString error = texts.at(4);
                KDevelop::Problem *p = new KDevelop::Problem();
                p->setFinalLocation(DocumentRange(document, SimpleRange(lineno - 1, qMax(colno - 4, 0),
                                                                        lineno - 1, colno + 4)));
                p->setSource(KDevelop::ProblemData::Preprocessor);
                p->setSeverity(KDevelop::ProblemData::Warning);
                p->setDescription(i18n("PEP8 checker error: %1", error));
                ProblemPointer ptr(p);
                topContext->addProblem(ptr);
            }
            else {
                qDebug() << "invalid pep8 error line:" << error;
            }
        }
    }
    if ( error ) {
        DUChainWriteLocker lock;
        KDevelop::Problem *p = new KDevelop::Problem();
        p->setFinalLocation(DocumentRange(document, SimpleRange(0, 0, 0, 0)));
        p->setSource(KDevelop::ProblemData::Preprocessor);
        p->setSeverity(KDevelop::ProblemData::Warning);
        p->setDescription(i18n("The selected PEP8 syntax checker \"%1\" does not seem to work correctly.", url));
        ProblemPointer ptr(p);
        topContext->addProblem(ptr);
    }
}

}

#include "pythonparsejob.moc"
// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
