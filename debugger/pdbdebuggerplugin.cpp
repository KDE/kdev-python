/*
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

//#include <kexportplugin.h>
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
    : IPlugin(QStringLiteral("kdevpdbsupport"), parent)
{
    IExecuteScriptPlugin* iface = KDevelop::ICore::self()->pluginController()
                            ->pluginForExtension(QStringLiteral("org.kdevelop.IExecuteScriptPlugin"))->extension<IExecuteScriptPlugin>();
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

#include "moc_pdbdebuggerplugin.cpp"
