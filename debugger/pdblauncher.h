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


#ifndef PDBLAUNCHER_H
#define PDBLAUNCHER_H

#include <interfaces/ilauncher.h>

namespace Python {

class PdbLauncher : public KDevelop::ILauncher
{
public:
    PdbLauncher();
    QList< KDevelop::LaunchConfigurationPageFactory* > configPages() const override;
    QString description() const override;
    QString id() override;
    QString name() const override;
    KJob* start(const QString& launchMode, KDevelop::ILaunchConfiguration* cfg) override;
    QStringList supportedModes() const override;
};

}

#endif // PDBLAUNCHER_H
