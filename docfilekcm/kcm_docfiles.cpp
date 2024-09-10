/*
    SPDX-FileCopyrightText: 2013 Sven Brauch <svenbrauch@gmail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#include "kcm_docfiles.h"

#include <QVBoxLayout>

#include "docfilemanagerwidget.h"

DocfilesKCModule::DocfilesKCModule(KDevelop::IPlugin* plugin, QWidget* parent)
    : KDevelop::ConfigPage(plugin, nullptr, parent)
{
    managerWidget = new DocfileManagerWidget(this);

    QVBoxLayout* layout = new QVBoxLayout;
    layout->setContentsMargins(0, 0, 0, 0);
    layout->addWidget(managerWidget);
    setLayout(layout);
}

DocfilesKCModule::~DocfilesKCModule()
{
}

KDevelop::ConfigPage::ConfigPageType DocfilesKCModule::configPageType() const
{
    return KDevelop::ConfigPage::LanguageConfigPage;
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
    return i18n("Manage Documentation Files Used by the Python Plugin");
}

QIcon DocfilesKCModule::icon() const
{
    return QIcon::fromTheme(QStringLiteral("text-x-python"));
}

QString DocfilesKCModule::name() const
{
    return i18n("Python Documentation");
}

#include "moc_kcm_docfiles.cpp"
