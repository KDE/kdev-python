/*****************************************************************************
 * Copyright (c) 2007 Andreas Pakulat <apaku@gmx.de>                         *
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 *                                                                           *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
 * 02110-1301, USA.
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
#include <language/backgroundparser/backgroundparser.h>
#include <language/duchain/duchain.h>
#include <interfaces/idocumentcontroller.h>

#include "pythonparsejob.h"
#include "pythonhighlighting.h"
#include "duchain/pythoneditorintegrator.h"

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

    m_highlighting = new Highlighting( this );
}

LanguageSupport::~LanguageSupport()
{
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

const KDevelop::ICodeHighlighting* LanguageSupport::codeHighlighting() const
{
    return m_highlighting;
}

}

#include "pythonlanguagesupport.moc"
