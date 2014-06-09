/*****************************************************************************
 * Copyright (c) 2007 Andreas Pakulat <apaku@gmx.de>                         *
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 * Copyright (c) 2012 Sven Brauch <svenbrauch@gmail.com>                     *
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

#include "pythonlanguagesupport.h"

#include <QMutexLocker>

#include <KDebug>
#include <KComponentData>
#include <KStandardDirs>
#include <KPluginFactory>
#include <KPluginLoader>

#include <interfaces/icore.h>
#include <interfaces/ilanguagecontroller.h>
#include <interfaces/iplugincontroller.h>
#include <interfaces/ilanguage.h>
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

using namespace KDevelop;

K_PLUGIN_FACTORY( KDevPythonSupportFactory, registerPlugin<Python::LanguageSupport>(); )

K_EXPORT_PLUGIN(KDevPythonSupportFactory(
    KAboutData("kdevpythonsupport", "kdevpython", ki18n("Python Support"),
               KDEVPYTHON_VERSION_STR, ki18n("Support for the Python Scripting Language"), KAboutData::License_GPL)
    .addAuthor(ki18n("Sven Brauch"), ki18n("Author"), "svenbrauch@googlemail.com", "")
))

namespace Python
{
LanguageSupport* LanguageSupport::m_self = 0;

KDevelop::ContextMenuExtension LanguageSupport::contextMenuExtension(KDevelop::Context* context)
{
    ContextMenuExtension cm;
    EditorContext *ec = dynamic_cast<KDevelop::EditorContext *>(context);

    if (ec && ICore::self()->languageController()->languagesForUrl(ec->url()).contains(language())) {
        // It's a Python file, let's add our context menu.
        m_refactoring->fillContextMenu(cm, context);
        TypeCorrection::self().doContextMenu(cm, context);
    }
    return cm;
}

LanguageSupport::LanguageSupport( QObject* parent, const QVariantList& /*args*/ )
        : KDevelop::IPlugin( KDevPythonSupportFactory::componentData(), parent )
        , KDevelop::ILanguageSupport()
        , m_highlighting( new Highlighting( this ) )
        , m_refactoring( new Refactoring( this ) )
{
    KDEV_USE_EXTENSION_INTERFACE( KDevelop::ILanguageSupport )

    m_self = this;

    PythonCodeCompletionModel* codeCompletion = new PythonCodeCompletionModel(this);
    new KDevelop::CodeCompletion(this, codeCompletion, "Python");

    auto assistantsManager = core()->languageController()->staticAssistantsManager();
    assistantsManager->registerAssistant(StaticAssistant::Ptr(new RenameAssistant(this)));

    QObject::connect(ICore::self()->documentController(), SIGNAL(documentOpened(KDevelop::IDocument*)),
                     this, SLOT(documentOpened(KDevelop::IDocument*)));
}

void LanguageSupport::documentOpened(IDocument* doc)
{
    if ( ! ICore::self()->languageController()->languagesForUrl(doc->url()).contains(language()) ) {
        // not a python file
        return;
    }

    DUChainReadLocker lock;
    TopDUContextPointer topContext = TopDUContextPointer(DUChain::self()->chainForDocument(doc->url()));
    lock.unlock();
    ParseJob::eventuallyDoPEP8Checking(IndexedString(doc->url()), topContext.data());
}

LanguageSupport::~LanguageSupport()
{
    delete m_highlighting;
    m_highlighting = 0;
}

KDevelop::ParseJob *LanguageSupport::createParseJob( const IndexedString& url )
{
    if ( enabledForFile(url.toUrl()) ) {
        return new ParseJob(url, this);
    }
    else {
        return 0;
    }
}

QString LanguageSupport::name() const
{
    return "Python";
}

LanguageSupport* LanguageSupport::self()
{
    return m_self;
}

bool LanguageSupport::enabledForFile(const KUrl& url)
{
    // This is a bit more general than it would need to be,
    // but that way we can have the same code for both branches.
    QList< ILanguage* > enabledLanguages = ICore::self()->languageController()->languagesForUrl(url);
    const QString& name = LanguageSupport::self()->name();
    static const QString otherName = ( name == "Python3" ? "Python" : "Python3" );
    bool haveBoth = false;
    foreach ( const ILanguage* lang, enabledLanguages ) {
        if ( lang->name() == otherName ) {
            // both py2 and py3 plugins are installed
            haveBoth = true;
        }
    }
    if ( ! haveBoth ) {
        // If only one of the plugins is installed, use that.
        return true;
    }

    // Otherwise, both plugins are installed, so check if there's a choice for this session.
    KDevelop::ISession* activeSession = KDevelop::ICore::self()->activeSession();
    if ( activeSession ) {
        KConfigGroup group(activeSession->config()->group("python"));
        const QString& version = group.readEntry("languageVersion", "Python 3");
        if ( ( version == "Python 3" && name == "Python3" ) || ( version == "Python 2" && name == "Python" ) ) {
            // this plugin is the right one, the other one will disable itself
            return true;
        }
    }
    else {
        // no session, treat this as a py3 file
        return name == "Python3";
    }
    return false;
}

SourceFormatterItemList LanguageSupport::sourceFormatterItems() const
{
    SourceFormatterStyle autopep8("pep8ify");
    autopep8.setCaption("pep8ify");
    autopep8.setDescription(i18n("Format source with the pep8ify formatter."));
    autopep8.setOverrideSample("class klass:\n def method(arg1,arg2):\n  a=3+5\n"
                               "def function(arg,*vararg,**kwargs): return arg+kwarg[0]\nfunction(3, 5, 7)");
    using P = SourceFormatterStyle::MimeHighlightPair;
    autopep8.setMimeTypes(SourceFormatterStyle::MimeList{ P{"text/x-python", "Python"} });
    autopep8.setContent("/usr/bin/pep8ify -w $TMPFILE");

    return SourceFormatterItemList{SourceFormatterStyleItem{"customscript", autopep8}};
}

KDevelop::ILanguage *LanguageSupport::language()
{
    kDebug() << core()->languageController()->language( name() );
    return core()->languageController()->language( name() );
}

KDevelop::ICodeHighlighting* LanguageSupport::codeHighlighting() const
{
    return m_highlighting;
}

BasicRefactoring* LanguageSupport::refactoring() const
{
    return m_refactoring;
}

ILanguageSupport::WhitespaceSensitivity LanguageSupport::whitespaceSensititivy() const
{
    return ILanguageSupport::IndentOnly;
}

}

#include "pythonlanguagesupport.moc"
