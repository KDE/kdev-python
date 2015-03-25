/************************************************************************
 * KDevelop4 Python Language Support                                    *
 * Copyright 2013 Sven Brauch <svenbrauch@gmail.com>                    *
 *                                                                      *
 *                                                                      *
 * This program is free software; you can redistribute it and/or modify *
 * it under the terms of the GNU General Public License as published by *
 * the Free Software Foundation; either version 2 or version 3 of the License, or    *
 * (at your option) any later version.                                  *
 *                                                                      *
 * This program is distributed in the hope that it will be useful, but  *
 * WITHOUT ANY WARRANTY; without even the implied warranty of           *
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU     *
 * General Public License for more details.                             *
 *                                                                      *
 * You should have received a copy of the GNU General Public License    *
 * along with this program; if not, see <http://www.gnu.org/licenses/>. *
 ************************************************************************/

#include "kcm_docfiles.h"

#include <QVBoxLayout>

#include "docfilemanagerwidget.h"

DocfilesKCModule::DocfilesKCModule(KDevelop::IPlugin* plugin, QWidget* parent)
    : KDevelop::ConfigPage(plugin, nullptr, parent)
{
    managerWidget = new DocfileManagerWidget(this);

    QVBoxLayout* layout = new QVBoxLayout;
    layout->addWidget(managerWidget);
    setLayout(layout);
}

DocfilesKCModule::~DocfilesKCModule()
{
}

void DocfilesKCModule::apply()
{
    // nothing to do, but must override since we do not use KCoreConfigSkeleton
}
void DocfilesKCModule::reset()
{
    // nothing to do, but must override since we do not use KCoreConfigSkeleton
}
void DocfilesKCModule::defaults()
{
    // nothing to do, but must override since we do not use KCoreConfigSkeleton
}

QString DocfilesKCModule::fullName() const
{
    return i18n("Manage documentation files used by the Python plugin");
}

QIcon DocfilesKCModule::icon() const
{
    return QIcon::fromTheme(QStringLiteral("text-x-python"));
}

QString DocfilesKCModule::name() const
{
    return i18n("Python documentation");
}


#include "kcm_docfiles.moc"
