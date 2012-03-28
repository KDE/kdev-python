/*
    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) 2012  <copyright holder> <email>

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
#include <interfaces/icore.h>
#include <interfaces/iplugincontroller.h>
#include <KLocalizedString>

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
        DebugJob* job = new DebugJob();
        IExecuteScriptPlugin* iface = KDevelop::ICore::self()->pluginController()
                                      ->pluginForExtension("org.kdevelop.IExecuteScriptPlugin")->extension<IExecuteScriptPlugin>();
        Q_ASSERT(iface);
        QString err;
        job->m_scriptUrl = iface->script(cfg, err);
        job->m_interpreter = iface->interpreter(cfg, err);
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
