/*
    This file is part of kdev-python, the python language plugin for KDevelop
    Copyright (C) 2012  Sven Brauch <svenbrauch@googlemail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/


#include "pdblauncher.h"
#include "debugjob.h"

#include <util/executecompositejob.h>
#include <executescript/iexecutescriptplugin.h>
#include <interfaces/launchconfigurationpage.h>
#include <interfaces/ilaunchconfiguration.h>
#include <interfaces/iplugincontroller.h>
#include <interfaces/icore.h>
#include <interfaces/iuicontroller.h>

#include <KLocalizedString>
#include <KMessageBox>
#include <KParts/MainWindow>
#include <KDebug>
#include <KConfigGroup>


namespace Python {
    
PdbLauncher::PdbLauncher()
{

}

QList< KDevelop::LaunchConfigurationPageFactory* > PdbLauncher::configPages() const
{
    return QList<KDevelop::LaunchConfigurationPageFactory*>();
}

QString PdbLauncher::description() const
{
    return i18n("A plugin to debug Python applications with pdb.");
}

QString PdbLauncher::id()
{
    return "pdbdebugger";
}

QString PdbLauncher::name() const
{
    return "pdbdebugger";
}

KJob* PdbLauncher::start(const QString& launchMode, KDevelop::ILaunchConfiguration* cfg)
{
    kDebug() << "start of debugger process requested";
    if ( launchMode == "debug" ) {
        IExecuteScriptPlugin* iface = KDevelop::ICore::self()->pluginController()
                                      ->pluginForExtension("org.kdevelop.IExecuteScriptPlugin")->extension<IExecuteScriptPlugin>();
        Q_ASSERT(iface);
        QString err;
        QString interpreter = iface->interpreter(cfg, err);
        
        // check the interpreter
        QProcess p;
        p.start(interpreter, QStringList() << "--version");
        p.waitForFinished(500);
        QByteArray version = p.readAllStandardError();
        kDebug() << "interpreter version:" << version;
        if ( ! version.startsWith("Python 3.") ) {
            KMessageBox::error(ICore::self()->uiController()->activeMainWindow(),
                            i18n("Sorry, debugging is only supported for Python 3.x applications."),
                            i18n("Unsupported interpreter"));
            return 0;
        }
        
        DebugJob* job = new DebugJob();
        
        job->m_scriptUrl = iface->script(cfg, err);
        job->m_interpreter = interpreter;
        job->m_args = iface->arguments(cfg, err);
        QList<KJob*> l;
        l << job;
        return new KDevelop::ExecuteCompositeJob( KDevelop::ICore::self()->runController(), l );
    }
    kDebug() << "unknown launch mode";
    return 0;
}

QStringList PdbLauncher::supportedModes() const
{
    return QStringList() << "debug";
}

}
