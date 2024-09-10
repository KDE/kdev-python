/*
    SPDX-FileCopyrightText: 2016 Sven Brauch <svenbrauch@gmail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#include "projectconfigpage.h"

#include "ui_projectconfig.h"

#include "duchain/helpers.h"
#include <QLineEdit>

namespace Python {

ProjectConfigPage::ProjectConfigPage(KDevelop::IPlugin* self, const KDevelop::ProjectConfigOptions& options, QWidget* parent)
    : KDevelop::ConfigPage(self, nullptr, parent)
    , m_ui(new Ui_ProjectConfig)
{
    m_configGroup = options.project->projectConfiguration()->group(QStringLiteral("pythonsupport"));
    m_ui->setupUi(this);
    m_project = options.project;
    // So apply button activates
    connect(m_ui->pythonInterpreter, &QLineEdit::textChanged, this, &ProjectConfigPage::changed);
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


