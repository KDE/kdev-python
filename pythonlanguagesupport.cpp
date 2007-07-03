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

#include <kdebug.h>
#include <kcomponentdata.h>
#include <kstandarddirs.h>
#include <kgenericfactory.h>
#include <icore.h>
#include <QExtensionFactory>
#include <ilanguagecontroller.h>
#include <ilanguage.h>
#include <idocument.h>
#include <backgroundparser.h>
#include <idocumentcontroller.h>
#include <QExtensionFactory>

typedef KGenericFactory<PythonLanguageSupport> KDevPythonSupportFactory;
K_EXPORT_COMPONENT_FACTORY( kdevpythonlanguagesupport, KDevPythonSupportFactory( "kdevpythonsupport" ) )

PythonLanguageSupport::PythonLanguageSupport( QObject* parent, const QStringList& /*args*/ )
        : KDevelop::IPlugin( KDevPythonSupportFactory::componentData(), parent ),
        KDevelop::ILanguageSupport()
{
    KDEV_USE_EXTENSION_INTERFACE( KDevelop::ILanguageSupport )
    connect( core()->documentController(),
             SIGNAL( documentStateChanged( KDevelop::IDocument* ) ),
             this, SLOT( documentChanged( KDevelop::IDocument* ) ) );
    connect( core()->documentController(),
             SIGNAL( documentContentChanged( KDevelop::IDocument* ) ),
             this, SLOT( documentChanged( KDevelop::IDocument* ) ) );
    connect( core()->documentController(),
             SIGNAL( documentActivated( KDevelop::IDocument* ) ),
             this, SLOT( documentChanged( KDevelop::IDocument* ) ) );
}

void PythonLanguageSupport::documentChanged( KDevelop::IDocument* doc )
{
        kDebug() << "-------------Adding document to parser--------------" << endl;
        language()->backgroundParser()->addDocument(doc->url());
}
PythonLanguageSupport::~PythonLanguageSupport()
{
}

KDevelop::ParseJob *PythonLanguageSupport::createParseJob(const KUrl &url)
{
    kDebug() << ">>>>>>>>>Parsing<<<<<<<<<"
             << url
             << endl;
    return 0;
}

QString PythonLanguageSupport::name() const
{
    return "Python";
}

KDevelop::ILanguage *PythonLanguageSupport::language()
{
    return core()->languageController()->language(name());
}
#include "pythonlanguagesupport.moc"
