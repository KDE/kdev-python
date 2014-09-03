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

#include <KPluginFactory>
#include <KLocalizedString>

K_PLUGIN_FACTORY(PEP8KCModuleFactory, registerPlugin<PEP8KCModule>(); )
K_EXPORT_PLUGIN(PEP8KCModuleFactory("kcm_pep8", "kdevpythonsupport"))

PEP8KCModule::PEP8KCModule(QWidget* parent, const QVariantList& args)
    : KCModule(PEP8KCModuleFactory::componentData(), parent, args)
{
    KConfig* config = new KConfig("kdevpythonsupportrc");
    configGroup = config->group("pep8");
    QWidget* configWidget = new QWidget;
    QFormLayout* formlayout = new QFormLayout;
    configWidget->setLayout(formlayout);
    parent->layout()->addWidget(configWidget);

    QLabel* urllabel = new QLabel(i18n("Full path to the PEP8 checker to use:"));
    QLabel* argumentlabel = new QLabel(i18n("PEP8 checker arguments:"));
    QLabel* enablelabel = new QLabel(i18n("Enable PEP8 checking:"));
    pep8url = new QLineEdit(configGroup.readEntry("pep8url", "/usr/bin/pep8-python2"));
    pep8arguments = new QLineEdit(configGroup.readEntry("pap8arguments", ""));
    enableChecking = new QCheckBox;
    enableChecking->setChecked(configGroup.readEntry<bool>("pep8enabled", false));
    formlayout->addRow(urllabel, pep8url);
    formlayout->addRow(argumentlabel, pep8arguments);
    formlayout->addRow(enablelabel, enableChecking);
    formlayout->addItem(new QSpacerItem(0, 0, QSizePolicy::Expanding, QSizePolicy::Expanding));

    connect(pep8url, SIGNAL(textChanged(QString)), this, SLOT(changed()));
    connect(pep8arguments, SIGNAL(textChanged(QString)), this, SLOT(changed()));
    connect(enableChecking, SIGNAL(clicked(bool)), this, SLOT(changed()));
}

void PEP8KCModule::save()
{
    configGroup.writeEntry("pep8url", pep8url->text());
    configGroup.writeEntry("pap8arguments", pep8arguments->text());
    configGroup.writeEntry("pep8enabled", enableChecking->isChecked());
    KCModule::save();
}

PEP8KCModule::~PEP8KCModule()
{
    delete configGroup.config();
}

