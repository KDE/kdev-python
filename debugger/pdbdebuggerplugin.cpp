/*
    This file is part of kdev-python, the python language plugin for KDevelop
    Copyright (C) 2012  Sven Brauch <svenbrauch@googlemail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

#include <kexportplugin.h>
#include <kpluginfactory.h>
#include <KAboutData>
#include <KLocalizedString>

#include "pdbdebuggerplugin.h"
#include "pdblauncher.h"
#include <executescript/iexecutescriptplugin.h>
#include <execute/iexecuteplugin.h>
#include <interfaces/launchconfigurationtype.h>
#include <interfaces/icore.h>
#include <interfaces/iplugincontroller.h>
#include <interfaces/iruncontroller.h>

#include "kdevpythonversion.h"

namespace Python {

K_PLUGIN_FACTORY_WITH_JSON(PdbDebuggerPluginFactory, "kdevpdb.json", registerPlugin<PdbDebuggerPlugin>(); )

PdbDebuggerPlugin::PdbDebuggerPlugin(QObject* parent, const QVariantList&) 
    : IPlugin("kdevpdbsupport", parent)
{
    IExecuteScriptPlugin* iface = KDevelop::ICore::self()->pluginController()
                            ->pluginForExtension("org.kdevelop.IExecuteScriptPlugin")->extension<IExecuteScriptPlugin>();
    Q_ASSERT(iface);
    KDevelop::LaunchConfigurationType* type = core()->runController()
                                              ->launchConfigurationTypeForId(iface->scriptAppConfigTypeId());
    Q_ASSERT(type);
    type->addLauncher(new PdbLauncher());
}

PdbDebuggerPlugin::~PdbDebuggerPlugin()
{

}

}

#include "pdbdebuggerplugin.moc"
