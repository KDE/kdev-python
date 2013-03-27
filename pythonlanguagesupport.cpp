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


#include "pythonlanguagesupport.h"

#include <QMutexLocker>

#include <KDebug>
#include <KComponentData>
#include <KStandardDirs>
#include <KPluginFactory>
#include <KPluginLoader>

#include <QPushButton>
#include <QLabel>
#include <QHBoxLayout>

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

// QWidget* LanguageSupport::specialLanguageObjectNavigationWidget(const KUrl& url, const KDevelop::SimpleCursor& position)
// {
//     kDebug() << "Navigation widget requested *** ";
//     QFrame* frame = new QFrame();
//     QLabel* label = new QLabel();
//     QHBoxLayout *layout = new QHBoxLayout();
//     label->setText("Foo");
//     frame->setLayout(layout);
//     layout->addWidget(label);
//     return frame;
// }


}

#include "pythonlanguagesupport.moc"
