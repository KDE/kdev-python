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

#include <kdebug.h>
#include <kcomponentdata.h>
#include <kstandarddirs.h>
#include <kpluginfactory.h>
#include <kpluginloader.h>
#include <ktexteditor/smartinterface.h>

#include <interfaces/icore.h>
#include <interfaces/ilanguagecontroller.h>
#include <interfaces/iplugincontroller.h>
#include <interfaces/ilanguage.h>
#include <interfaces/idocument.h>
#include <editor/editorintegrator.h>
#include <language/backgroundparser/backgroundparser.h>
#include <language/duchain/duchain.h>
#include <interfaces/idocumentcontroller.h>

#include "pythonparsejob.h"
#include "pythonhighlighting.h"

using namespace KDevelop;

K_PLUGIN_FACTORY( KDevPythonSupportFactory, registerPlugin<Python::LanguageSupport>(); )
K_EXPORT_PLUGIN( KDevPythonSupportFactory( "kdevpythonsupport" ) )

namespace Python
{

LanguageSupport::LanguageSupport( QObject* parent, const QVariantList& /*args*/ )
        : KDevelop::IPlugin( KDevPythonSupportFactory::componentData(), parent ),
        KDevelop::ILanguageSupport()
{
    KDEV_USE_EXTENSION_INTERFACE( KDevelop::ILanguageSupport )
//     core()->pluginController()->loadPlugin( "kdevduchainview" );
    m_highlighting = new Highlighting( this );
    
    connect( core()->documentController(),
             SIGNAL( documentLoaded( KDevelop::IDocument* ) ),
             this, SLOT( documentLoaded( KDevelop::IDocument* ) ) );
    connect( core()->documentController(),
             SIGNAL( documentClosed( KDevelop::IDocument* ) ),
             this, SLOT( documentClosed( KDevelop::IDocument* ) ) );
    connect( core()->documentController(),
             SIGNAL( documentStateChanged( KDevelop::IDocument* ) ),
             this, SLOT( documentChanged( KDevelop::IDocument* ) ) );
    connect( core()->documentController(),
             SIGNAL( documentContentChanged( KDevelop::IDocument* ) ),
             this, SLOT( documentChanged( KDevelop::IDocument* ) ) );
    connect( core()->documentController(),
             SIGNAL( documentActivated( KDevelop::IDocument* ) ),
             this, SLOT( documentActivated( KDevelop::IDocument* ) ) );
}

void LanguageSupport::documentChanged( KDevelop::IDocument* doc )
{
    core()->languageController()->backgroundParser()->addDocument( doc->url() );
}

LanguageSupport::~LanguageSupport()
{
    core()->languageController()->backgroundParser()->clear( this );
    delete m_highlighting;
    m_highlighting = 0;
}

KDevelop::ParseJob *LanguageSupport::createParseJob( const KUrl &url )
{
    return new ParseJob( url, this );
}

QString LanguageSupport::name() const
{
    return "Python";
}

KDevelop::ILanguage *LanguageSupport::language()
{
    return core()->languageController()->language( name() );
}

KDevelop::ICodeHighlighting* LanguageSupport::codeHighlighting() const
{
    return m_highlighting;
}

void LanguageSupport::documentActivated( KDevelop::IDocument* doc )
{
    Q_UNUSED( doc );
}

void LanguageSupport::documentClosed( KDevelop::IDocument* doc )
{
    Q_UNUSED( doc );
}

void LanguageSupport::documentLoaded( KDevelop::IDocument* doc )
{
    EditorIntegrator editor;
    editor.setCurrentUrl( doc->url().prettyUrl() );
    
    QList<TopDUContext*> chains = DUChain::self()->chainsForDocument( doc->url() );
    foreach( TopDUContext* chain, chains )
    {
        if( codeHighlighting() && editor.smart() )
        {
            QMutexLocker lock( editor.smart()->smartMutex() );
            codeHighlighting()->highlightDUChain( chain );
        }
    }
    if( chains.isEmpty() )
    {
        core()->languageController()->backgroundParser()->addDocument( doc->url() );
    }
}

}

#include "pythonlanguagesupport.moc"
