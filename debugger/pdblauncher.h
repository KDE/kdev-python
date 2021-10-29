/*
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
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
