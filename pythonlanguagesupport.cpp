/*
    SPDX-FileCopyrightText: 2007 Andreas Pakulat <apaku@gmx.de>
    SPDX-FileCopyrightText: 2007 Piyush verma <piyush.verma@gmail.com>
    SPDX-FileCopyrightText: 2012-2016 Sven Brauch <svenbrauch@gmail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#include "pythonlanguagesupport.h"

#include <QMutexLocker>
#include <QReadWriteLock>

#include <KPluginFactory>
//#include <KPlugin>

#include <interfaces/icore.h>
#include <interfaces/ilanguagecontroller.h>
#include <interfaces/iplugincontroller.h>
#include <interfaces/idocument.h>
#include <interfaces/isourceformatter.h>
#include <interfaces/idocumentcontroller.h>
#include <interfaces/context.h>
#include <interfaces/contextmenuextension.h>
#include <interfaces/iprojectcontroller.h>
#include <interfaces/iproject.h>
#include <interfaces/isession.h>
#include <language/assistant/renameassistant.h>
#include <language/assistant/staticassistantsmanager.h>
#include <language/interfaces/editorcontext.h>
#include <language/duchain/duchain.h>
#include <language/duchain/duchainlock.h>
#include <language/codecompletion/codecompletion.h>
#include <language/codecompletion/codecompletionmodel.h>

#include "pythonparsejob.h"
#include "pythonhighlighting.h"
#include "duchain/pythoneditorintegrator.h"
#include "codecompletion/model.h"
#include "codegen/refactoring.h"
#include "codegen/correctionfilegenerator.h"
#include "kdevpythonversion.h"
#include "pep8kcm/kcm_pep8.h"
#include "projectconfig/projectconfigpage.h"
#include "docfilekcm/kcm_docfiles.h"
#include "pythonstylechecking.h"
#include "helpers.h"

#include <QDebug>
#include <QProcess>
#include "pythondebug.h"

using namespace KDevelop;

K_PLUGIN_FACTORY_WITH_JSON( KDevPythonSupportFactory, "kdevpythonsupport.json", registerPlugin<Python::LanguageSupport>(); )

namespace Python
{
LanguageSupport* LanguageSupport::m_self = nullptr;

ContextMenuExtension LanguageSupport::contextMenuExtension(Context* context, QWidget* parent)
{
    ContextMenuExtension cm;
    EditorContext *ec = dynamic_cast<KDevelop::EditorContext *>(context);

    if (ec && ICore::self()->languageController()->languagesForUrl(ec->url()).contains(this)) {
        // It's a Python file, let's add our context menu.
        m_refactoring->fillContextMenu(cm, context, parent);
        TypeCorrection::self().doContextMenu(cm, context);
    }
    return cm;
}

LanguageSupport::LanguageSupport( QObject* parent, const QVariantList& /*args*/ )
    : KDevelop::IPlugin(QStringLiteral("pythonlanguagesupport"), parent )
    , KDevelop::ILanguageSupport()
    , m_highlighting( new Highlighting( this ) )
    , m_refactoring( new Refactoring( this ) )
    , m_styleChecking( new StyleChecking( this ) )
{
    m_self = this;

    PythonCodeCompletionModel* codeCompletion = new PythonCodeCompletionModel(this);
    new KDevelop::CodeCompletion(this, codeCompletion, QStringLiteral("Python"));

    auto assistantsManager = core()->languageController()->staticAssistantsManager();
    assistantsManager->registerAssistant(StaticAssistant::Ptr(new RenameAssistant(this)));

    QObject::connect(ICore::self()->documentController(), &IDocumentController::documentOpened,
                     this, &LanguageSupport::documentOpened);
}

void LanguageSupport::documentOpened(IDocument* doc)
{
    if ( ! ICore::self()->languageController()->languagesForUrl(doc->url()).contains(this) ) {
        // not a python file
        return;
    }

    DUChainReadLocker lock;
    ReferencedTopDUContext top = DUChain::self()->chainForDocument(doc->url());
    lock.unlock();
    updateStyleChecking(top);
}

void LanguageSupport::updateStyleChecking(KDevelop::ReferencedTopDUContext top)
{
    m_styleChecking->updateStyleChecking(top);
}

LanguageSupport::~LanguageSupport()
{
    parseLock()->lockForWrite();
    // By locking the parse-mutexes, we make sure that parse jobs get a chance to finish in a good state
    parseLock()->unlock();

    delete m_highlighting;
    m_highlighting = nullptr;
}

KDevelop::ParseJob *LanguageSupport::createParseJob( const IndexedString& url )
{
    return new ParseJob(url, this);
}

QString LanguageSupport::name() const
{
    return QStringLiteral("Python");
}

LanguageSupport* LanguageSupport::self()
{
    return m_self;
}

SourceFormatterItemList LanguageSupport::sourceFormatterItems() const
{
    SourceFormatterStyle autopep8(QStringLiteral("autopep8"));
    autopep8.setCaption(QStringLiteral("autopep8"));
    autopep8.setDescription(i18n("Format source with the autopep8 formatter."));
    autopep8.setOverrideSample(QStringLiteral("class klass:\n def method(arg1,arg2):\n  a=3+5\n"
                               "def function(arg,*vararg,**kwargs): return arg+kwarg[0]\nfunction(3, 5, 7)"));
    using P = SourceFormatterStyle::MimeHighlightPair;
    autopep8.setMimeTypes(SourceFormatterStyle::MimeList{ P{QStringLiteral("text/x-python"), QStringLiteral("Python")},
                                                          P{QStringLiteral("text/x-python3"), QStringLiteral("Python 3")} });
    QString autopep8path = QStandardPaths::findExecutable(QStringLiteral("autopep8"));
    if (autopep8path.isEmpty()) {
        // TODO: proper error handling/user notification
        qCDebug(KDEV_PYTHON) << "Could not find the autopep8 executable";
        autopep8path = QStringLiteral("/usr/bin/autopep8");
    }
    autopep8.setContent(autopep8path + QStringLiteral(" -i $TMPFILE"));

    return SourceFormatterItemList{SourceFormatterStyleItem{QStringLiteral("customscript"), autopep8}};
}

KDevelop::ICodeHighlighting* LanguageSupport::codeHighlighting() const
{
    return m_highlighting;
}

BasicRefactoring* LanguageSupport::refactoring() const
{
    return m_refactoring;
}

int LanguageSupport::suggestedReparseDelayForChange(KTextEditor::Document* doc, const KTextEditor::Range& changedRange,
                                                    const QString& changedText, bool /*removal*/) const
{
    if ( changedRange.start().line() != changedRange.end().line() ) {
        // instant update
        return 0;
    }
    if ( std::all_of(changedText.begin(), changedText.end(), [](const QChar& c) { return c.isSpace(); }) ) {
        qCDebug(KDEV_PYTHON) << changedText << changedRange.end().column() << doc->lineLength(changedRange.end().line());
        if ( changedRange.end().column()-1 == doc->lineLength(changedRange.end().line()) ) {
            return ILanguageSupport::NoUpdateRequired;
        }
    }
    return ILanguageSupport::DefaultDelay;
}


QList<ILanguageCheck*> LanguageSupport::providedChecks()
{
    return {};
}

int LanguageSupport::configPages() const
{
    return 2;
}

KDevelop::ConfigPage* LanguageSupport::configPage(int number, QWidget* parent)
{
    if (number == 0) {
        return new PEP8KCModule(this, parent);
    } else if (number == 1) {
        return new DocfilesKCModule(this, parent);
    }
    return nullptr;
}

int LanguageSupport::perProjectConfigPages() const
{
    return 1;
}

KDevelop::ConfigPage* LanguageSupport::perProjectConfigPage(int number, const KDevelop::ProjectConfigOptions& options, QWidget* parent)
{
    if ( number == 0 ) {
        return new Python::ProjectConfigPage(this, options, parent);
    }
    return nullptr;
}

}

#include "pythonlanguagesupport.moc"

#include "moc_pythonlanguagesupport.cpp"
