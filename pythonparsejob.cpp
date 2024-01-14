/*
    SPDX-FileCopyrightText: 2007 Andreas Pakulat <apaku@gmx.de>
    SPDX-FileCopyrightText: 2007 Piyush verma <piyush.verma@gmail.com>
    SPDX-FileCopyrightText: 2010-2013 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#include "pythonparsejob.h"

#include "pythondebug.h"
#include "pythonhighlighting.h"
#include "pythoneditorintegrator.h"
#include "dumpchain.h"
#include "parsesession.h"
#include "pythonlanguagesupport.h"
#include "declarationbuilder.h"
#include "usebuilder.h"
#include "kshell.h"
#include "duchain/helpers.h"
#include "pep8kcm/kcm_pep8.h"

#include <language/duchain/duchainlock.h>
#include <language/duchain/duchain.h>
#include <language/duchain/topducontext.h>
#include <language/duchain/dumpdotgraph.h>
#include <serialization/indexedstring.h>
#include <language/duchain/duchainutils.h>
#include <language/backgroundparser/urlparselock.h>
#include <language/backgroundparser/backgroundparser.h>
#include <language/highlighting/codehighlighting.h>
#include <language/interfaces/iastcontainer.h>
#include <language/checks/controlflowgraph.h>
#include <language/checks/dataaccessrepository.h>
#include <interfaces/icore.h>
#include <interfaces/iprojectcontroller.h>
#include <interfaces/ilanguagecontroller.h>
#include <interfaces/idocumentcontroller.h>
#include <util/foregroundlock.h>
#include <project/projectmodel.h>
#include <util/path.h>

#include <ktexteditor/document.h>

#include <QReadLocker>
#include <QThread>
#include <QCoreApplication>
#include <QProcess>
#include <QTemporaryFile>
#include <QDebug>
#include <KConfigGroup>

#include <custom-definesandincludes/idefinesandincludesmanager.h>

using namespace KDevelop;

namespace Python
{

ParseJob::ParseJob(const IndexedString &url, ILanguageSupport* languageSupport)
        : KDevelop::ParseJob(url, languageSupport)
        , m_ast(nullptr)
        , m_duContext(nullptr)
{
    IDefinesAndIncludesManager* iface = IDefinesAndIncludesManager::manager();
    auto project = ICore::self()->projectController()->findProjectForUrl(url.toUrl());
    if ( project ) {
        for (Path path : iface->includes(project->projectItem(), IDefinesAndIncludesManager::UserDefined)) {
            m_cachedCustomIncludes.append(path.toUrl());
        }
        QMutexLocker lock(&Helper::cacheMutex);
        Helper::cachedCustomIncludes[project] = m_cachedCustomIncludes;
    }
}

ParseJob::~ParseJob()
{
}

CodeAst *ParseJob::ast() const
{
    Q_ASSERT( isFinished() && m_ast );
    return m_ast.data();
}


void ParseJob::run(ThreadWeaver::JobPointer /*self*/, ThreadWeaver::Thread* /*thread*/)
{
    if ( abortRequested() || ICore::self()->shuttingDown() ) {
        return abortJob();
    }
    
    qCDebug(KDEV_PYTHON) << " ====> PARSING ====> parsing file " << document().toUrl() << "; has priority" << parsePriority();

    {
        QMutexLocker l(&Helper::projectPathLock);
        Helper::projectSearchPaths.clear();
        for (IProject* project : ICore::self()->projectController()->projects() ) {
            Helper::projectSearchPaths.append(QUrl::fromLocalFile(project->path().path()));
        }
    }
    
    // lock the URL so no other parse job can run on this document
    QReadLocker parselock(languageSupport()->parseLock());
    UrlParseLock urlLock(document());

    readContents();
    
    if ( !(minimumFeatures() & TopDUContext::ForceUpdate || minimumFeatures() & Rescheduled) ) {
        DUChainReadLocker lock(DUChain::lock());
        static const IndexedString langString("python");
        for (const ParsingEnvironmentFilePointer &file : DUChain::self()->allEnvironmentFiles(document())) {
            if ( file->language() != langString ) {
                continue;
            }
            if ( ! file->needsUpdate() && file->featuresSatisfied(minimumFeatures()) && file->topContext() ) {
                qCDebug(KDEV_PYTHON) << " ====> NOOP    ====> Already up to date:" << document().str();
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
    
    ReferencedTopDUContext toUpdate = nullptr;
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
        UseBuilder usebuilder(editor.data(), builder.missingModules());
        usebuilder.setCurrentlyParsedDocument(document());
        usebuilder.buildUses(m_ast.data());
        
        // check whether any unresolved imports were encountered
        bool needsReparse = ! builder.unresolvedImports().isEmpty();
        qCDebug(KDEV_PYTHON) << "Document needs update because of unresolved identifiers: " << needsReparse;
        if ( needsReparse ) {
            // check whether one of the imports is queued for parsing, this is to avoid deadlocks
            // it's also ok if the duchain is now available (and thus has been parsed before already)
            bool dependencyInQueue = false;
            DUChainWriteLocker lock;
            for ( const IndexedString& url : builder.unresolvedImports() ) {
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
                constexpr TopDUContext::Features features{TopDUContext::ForceUpdate};
                KDevelop::ICore::self()->languageController()->backgroundParser()->addDocument(document(),
                                     static_cast<TopDUContext::Features>(features | Rescheduled), parsePriority(),
                                     nullptr, ParseJob::FullSequentialProcessing);
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
        
        qCDebug(KDEV_PYTHON) << "---- Parsing Succeeded ----";
        
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
    for ( const ProblemPointer& p : m_currentSession->m_problems ) {
        m_duContext->addProblem(p);
    }

    // If enabled, and if the document is open, do PEP8 checking.
    eventuallyDoPEP8Checking(m_duContext);

    if ( minimumFeatures() & TopDUContext::AST ) {
        DUChainWriteLocker lock;
        m_currentSession->ast = m_ast;
        m_duContext->setAst(QExplicitlySharedDataPointer<IAstContainer>(m_currentSession.data()));
    }
    
    setDuChain(m_duContext);
    DUChain::self()->emitUpdateReady(document(), duChain());
}

ControlFlowGraph* ParseJob::controlFlowGraph()
{
    return nullptr;
}

DataAccessRepository* ParseJob::dataAccessInformation()
{
    return nullptr;
}

void ParseJob::eventuallyDoPEP8Checking(TopDUContext* topContext)
{
    KConfig config(QStringLiteral("kdevpythonsupportrc"));
    KConfigGroup configGroup = config.group(QStringLiteral("pep8"));
    if ( !PEP8KCModule::isPep8Enabled(configGroup) ) {
        return;
    }
    auto ls = static_cast<Python::LanguageSupport*>(languageSupport());
    QMetaObject::invokeMethod(ls, "updateStyleChecking", Q_ARG(KDevelop::ReferencedTopDUContext, topContext));
}

}

#include "moc_pythonparsejob.cpp"

// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
