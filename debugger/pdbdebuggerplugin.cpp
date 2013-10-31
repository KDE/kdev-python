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
#include <KLocalizedString>
#include <KAboutData>

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

K_PLUGIN_FACTORY(PdbDebuggerPluginFactory, registerPlugin<PdbDebuggerPlugin>(); )
K_EXPORT_PLUGIN(PdbDebuggerPluginFactory(
    KAboutData("kdevpdbsupport", "kdevpython", ki18n("Python Debugger (pdb) Support"),
               KDEVPYTHON_VERSION_STR, ki18n("Support for the Python Debugger"), KAboutData::License_GPL)
    .addAuthor(ki18n("Sven Brauch"), ki18n("Author"), "svenbrauch@googlemail.com", "")
))

PdbDebuggerPlugin::PdbDebuggerPlugin(QObject* parent, const QVariantList&) 
    : IPlugin(PdbDebuggerPluginFactory::componentData(), parent)
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
