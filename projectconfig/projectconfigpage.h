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

#pragma once

#include <project/projectconfigpage.h>

#include <KConfigGroup>

class Ui_ProjectConfig;

namespace Python {

class ProjectConfigPage : public KDevelop::ConfigPage {
public:
    ProjectConfigPage(KDevelop::IPlugin* self, const KDevelop::ProjectConfigOptions& options, QWidget* parent);
    QString name() const override;

public Q_SLOTS:
    void apply() override;
    void defaults() override;
    void reset() override;

private:
    KConfigGroup m_configGroup;
    Ui_ProjectConfig* m_ui;
    KDevelop::IProject* m_project;
};

}
