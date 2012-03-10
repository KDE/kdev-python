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

#include <interfaces/launchconfigurationpage.h>
#include <KLocalizedString>

#include <KDebug>

QList< KDevelop::LaunchConfigurationPageFactory* > PdbLauncher::configPages() const
{
    return QList<KDevelop::LaunchConfigurationPageFactory*>();
}

QString PdbLauncher::description() const
{
    return i18n("A plugin to debug python applications with pdb.");
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
}

QStringList PdbLauncher::supportedModes() const
{
    return QStringList() << "debug";
}


