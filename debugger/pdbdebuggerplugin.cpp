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

#include <kexportplugin.h>
#include <kpluginfactory.h>
#include <KLocalizedString>
#include <KAboutData>

#include "pdbdebuggerplugin.h"

namespace Python {

K_PLUGIN_FACTORY(PdbDebuggerPluginFactory, registerPlugin<PdbDebuggerPlugin>(); )
K_EXPORT_PLUGIN(PdbDebuggerPluginFactory(KAboutData("kdevpdb", "kdevpdb", ki18n("PDB Support"), "0.1", ki18n("Support for running apps in PDB"), KAboutData::License_GPL)))

PdbDebuggerPlugin::PdbDebuggerPlugin(QObject* parent, const QVariantList&) 
    : IPlugin(PdbDebuggerPluginFactory::componentData(), parent)
{

}

PdbDebuggerPlugin::~PdbDebuggerPlugin()
{

}

}

#include "pdbdebuggerplugin.moc"