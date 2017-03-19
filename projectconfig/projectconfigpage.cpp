/*****************************************************************************
 * Copyright (c) 2016 Sven Brauch <svenbrauch@gmail.com>                     *
 *                                                                           *
 * This program is free software; you can redistribute it and/or             *
 * modify it under the terms of the GNU General Public License as            *
 * published by the Free Software Foundation; either version 2 of            *
 * the License, or (at your option) any later version.                       *
 *                                                                           *
 * This program is distributed in the hope that it will be useful,           *
 * but WITHOUT ANY WARRANTY; without even the implied warranty of            *
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             *
 * GNU General Public License for more details.                              *
 *                                                                           *
 * You should have received a copy of the GNU General Public License         *
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.     *
 *****************************************************************************
 */

#include "projectconfigpage.h"

#include "ui_projectconfig.h"

#include "duchain/helpers.h"

namespace Python {

ProjectConfigPage::ProjectConfigPage(KDevelop::IPlugin* self, const KDevelop::ProjectConfigOptions& options, QWidget* parent)
    : KDevelop::ConfigPage(self, nullptr, parent)
    , m_ui(new Ui_ProjectConfig)
{
    m_configGroup = options.project->projectConfiguration()->group("pythonsupport");
    m_ui->setupUi(this);
    m_project = options.project;
}

void Python::ProjectConfigPage::apply()
{
    m_configGroup.writeEntry("interpreter", m_ui->pythonInterpreter->text());
    // remove cached paths, so they are updated on the next parse job run
    QMutexLocker lock(&Helper::cacheMutex);
    Helper::cachedSearchPaths.remove(m_project);
}

void Python::ProjectConfigPage::defaults()
{
    m_ui->pythonInterpreter->setText(QString());
}

void Python::ProjectConfigPage::reset()
{
    m_ui->pythonInterpreter->setText(m_configGroup.readEntry("interpreter"));
}

QString Python::ProjectConfigPage::name() const
{
    return i18n("Python Settings");
}

}


