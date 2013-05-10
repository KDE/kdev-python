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
#include <interfaces/idocumentcontroller.h>
#include <interfaces/context.h>
#include <interfaces/contextmenuextension.h>
#include <language/duchain/duchain.h>
#include <language/duchain/duchainlock.h>
#include <language/codecompletion/codecompletion.h>
#include <language/codecompletion/codecompletionmodel.h>

#include "pythonparsejob.h"
#include "pythonhighlighting.h"
#include "duchain/pythoneditorintegrator.h"
#include "codecompletion/model.h"
#include "codegen/simplerefactoring.h"
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
    SimpleRefactoring::self().doContextMenu(cm, context);
    return cm;
}

LanguageSupport::LanguageSupport( QObject* parent, const QVariantList& /*args*/ )
        : KDevelop::IPlugin( KDevPythonSupportFactory::componentData(), parent ),
        KDevelop::ILanguageSupport()
{
    KDEV_USE_EXTENSION_INTERFACE( KDevelop::ILanguageSupport )

    m_self = this;

    m_highlighting = new Highlighting( this );
    PythonCodeCompletionModel* codeCompletion = new PythonCodeCompletionModel(this);
    new KDevelop::CodeCompletion(this, codeCompletion, "Python");

    QObject::connect(ICore::self()->documentController(), SIGNAL(documentOpened(KDevelop::IDocument*)),
                     this, SLOT(documentOpened(KDevelop::IDocument*)));
}

void LanguageSupport::documentOpened(IDocument* doc)
{
    if ( ICore::self()->languageController()->languagesForUrl(doc->url()).contains(language()) ) {
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
    return new ParseJob(url, this);
}

QString LanguageSupport::name() const
{
    return "Python";
}

LanguageSupport* LanguageSupport::self()
{
    return m_self;
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

ILanguageSupport::WhitespaceSensitivity LanguageSupport::whitespaceSensititivy() const
{
    return ILanguageSupport::IndentOnly;
}

}

#include "pythonlanguagesupport.moc"
