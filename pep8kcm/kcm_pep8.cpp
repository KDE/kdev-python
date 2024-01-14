/*
    SPDX-FileCopyrightText: 2013-2016 Sven Brauch <svenbrauch@gmail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

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
    auto config = KSharedConfig::openConfig(QStringLiteral("kdevpythonsupportrc"));
    configGroup = config->group(QStringLiteral("pep8"));
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
    m_ui.enableErrors->setText(QString());
    m_ui.disableErrors->setText(pep8DefaultIgnoreErrors());
    m_ui.maxLineLength->setValue(79);
    m_ui.enableChecking->setChecked(false);
}

QString PEP8KCModule::fullName() const
{
    return i18n("Configure Python Style Checking");
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

#include "moc_kcm_pep8.cpp"
