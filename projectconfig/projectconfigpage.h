/*
    SPDX-FileCopyrightText: 2016 Sven Brauch <svenbrauch@gmail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
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
