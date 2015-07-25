/************************************************************************
 * KDevelop4 Python Language Support                                    *
 *                                                                      *
 * Copyright 2013 Sven Brauch <svenbrauch@gmail.com>                    *
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

#include <QLabel>
#include <QLayout>
#include <QBoxLayout>
#include <QLineEdit>
#include <QFormLayout>

#include <KLocalizedString>
#include <KConfig>

PEP8KCModule::PEP8KCModule(KDevelop::IPlugin* plugin, QWidget* parent)
    : KDevelop::ConfigPage(plugin, nullptr, parent)
{
    KConfig* config = new KConfig("kdevpythonsupportrc");
    configGroup = config->group("pep8");
    QFormLayout* formlayout = new QFormLayout;
    setLayout(formlayout);

    QLabel* urllabel = new QLabel(i18n("Full path to the PEP8 checker to use:"));
    QLabel* argumentlabel = new QLabel(i18n("PEP8 checker arguments:"));
    QLabel* enablelabel = new QLabel(i18n("Enable PEP8 checking:"));
    pep8url = new QLineEdit;
    pep8arguments = new QLineEdit;
    enableChecking = new QCheckBox;
    reset(); // load the initial values
    formlayout->addRow(urllabel, pep8url);
    formlayout->addRow(argumentlabel, pep8arguments);
    formlayout->addRow(enablelabel, enableChecking);
    formlayout->addItem(new QSpacerItem(0, 0, QSizePolicy::Expanding, QSizePolicy::Expanding));

    connect(pep8url, &QLineEdit::textChanged, this, &PEP8KCModule::changed);
    connect(pep8arguments, &QLineEdit::textChanged, this, &PEP8KCModule::changed);
    connect(enableChecking, &QCheckBox::clicked, this, &PEP8KCModule::changed);
}

void PEP8KCModule::apply()
{
    configGroup.writeEntry("pep8url", pep8url->text());
    configGroup.writeEntry("pep8arguments", pep8arguments->text());
    configGroup.writeEntry("pep8enabled", enableChecking->isChecked());
    configGroup.sync();
}

static QString defaultPep8Path() {
    QString result = QStandardPaths::findExecutable("pep8-python3");
    if (result.isEmpty()) {
        result = QStandardPaths::findExecutable("pep8");
    }
    return result;
}

bool PEP8KCModule::isPep8Enabled(const KConfigGroup& group)
{
    return group.readEntry<bool>("pep8enabled", false);
}

QString PEP8KCModule::pep8Path(const KConfigGroup& group)
{
    static const QString pep8Default = defaultPep8Path();
    return group.readEntry("pep8url", pep8Default);
}

QString PEP8KCModule::pep8Arguments(const KConfigGroup& group)
{
    return group.readEntry("pep8arguments", QString());
}

void PEP8KCModule::reset()
{
    pep8url->setText(pep8Path(configGroup));
    pep8arguments->setText(pep8Arguments(configGroup));
    enableChecking->setChecked(isPep8Enabled(configGroup));
}

void PEP8KCModule::defaults()
{
    pep8url->setText(defaultPep8Path());
    pep8arguments->setText(QString());
    enableChecking->setChecked(false);
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
    return i18n("Python style checking");
}

PEP8KCModule::~PEP8KCModule()
{
    delete configGroup.config();
}

