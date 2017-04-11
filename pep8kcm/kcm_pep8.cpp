/************************************************************************
 * KDevelop Python Language Support                                     *
 *                                                                      *
 * Copyright 2013-2016 Sven Brauch <svenbrauch@gmail.com>               *
 *                                                                      *
 * This program is free software; you can redistribute it and/or modify *
 * it under the terms of the GNU General Public License as published by *
 * the Free Software Foundation; either version 2 or version 3 of the   *
 * License, or (at your option) any later version.                      *
 *                                                                      *
 * This program is distributed in the hope that it will be useful, but  *
 * WITHOUT ANY WARRANTY; without even the implied warranty of           *
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU     *
 * General Public License for more details.                             *
 *                                                                      *
 * You should have received a copy of the GNU General Public License    *
 * along with this program; if not, see <http://www.gnu.org/licenses/>. *
 ************************************************************************/

#include "kcm_pep8.h"

#include <KLocalizedString>
#include <KSharedConfig>
#include <QDebug>

namespace {
    QString pep8DefaultIgnoreErrors() {
        return QStringLiteral("E121,E123,E126,E226,E24,E704,W503");
    }
}

PEP8KCModule::PEP8KCModule(KDevelop::IPlugin* plugin, QWidget* parent)
    : KDevelop::ConfigPage(plugin, nullptr, parent)
{
    auto config = KSharedConfig::openConfig("kdevpythonsupportrc");
    configGroup = config->group("pep8");
    m_ui.setupUi(this);

    connect(m_ui.disableErrors, &QLineEdit::textChanged, this, &PEP8KCModule::changed);
    connect(m_ui.enableErrors, &QLineEdit::textChanged, this, &PEP8KCModule::changed);
    connect(m_ui.maxLineLength, static_cast<void (QSpinBox::*)(int)>(&QSpinBox::valueChanged), this, &PEP8KCModule::changed);
    connect(m_ui.enableChecking, &QGroupBox::toggled, this, &PEP8KCModule::changed);
}

void PEP8KCModule::apply()
{
    configGroup.writeEntry("enableErrors", m_ui.enableErrors->text());
    configGroup.writeEntry("disableErrors", m_ui.disableErrors->text());
    configGroup.writeEntry("maxLineLength", m_ui.maxLineLength->text());
    configGroup.writeEntry("pep8enabled", m_ui.enableChecking->isChecked());
    configGroup.sync();
}

bool PEP8KCModule::isPep8Enabled(const KConfigGroup& group)
{
    return group.readEntry<bool>("pep8enabled", false);
}
void PEP8KCModule::reset()
{
    m_ui.enableErrors->setText(configGroup.readEntry("enableErrors", QString()));
    m_ui.disableErrors->setText(configGroup.readEntry("disableErrors", pep8DefaultIgnoreErrors()));
    m_ui.maxLineLength->setValue(configGroup.readEntry("maxLineLength", 79));
    m_ui.enableChecking->setChecked(configGroup.readEntry("pep8enabled", false));
}

void PEP8KCModule::defaults()
{
    m_ui.enableErrors->setText("");
    m_ui.disableErrors->setText(pep8DefaultIgnoreErrors());
    m_ui.maxLineLength->setValue(79);
    m_ui.enableChecking->setChecked(false);
}

QString PEP8KCModule::fullName() const
{
    return i18n("Configure Python style checking");
}

QIcon PEP8KCModule::icon() const
{
    return QIcon::fromTheme(QStringLiteral("text-x-python"));
}

QString PEP8KCModule::name() const
{
    return i18n("Python Style Checking");
}

PEP8KCModule::~PEP8KCModule()
{
}

KDevelop::ConfigPage::ConfigPageType PEP8KCModule::configPageType() const
{
    return KDevelop::ConfigPage::AnalyzerConfigPage;
}
