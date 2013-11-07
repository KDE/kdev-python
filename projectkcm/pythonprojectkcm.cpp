/*
 * <one line to give the library's name and an idea of what it does.>
 * Copyright 2013  Sven Brauch <svenbrauch@gmail.com>
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License as
 * published by the Free Software Foundation; either version 2 of
 * the License or (at your option) version 3 or any later version
 * accepted by the membership of KDE e.V. (or its successor approved
 * by the membership of KDE e.V.), which shall act as a proxy
 * defined in Section 14 of version 3 of the license.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 */

#ifndef PYTHONPROJECTKCM_H
#define PYTHONPROJECTKCM_H

#include "pythonprojectkcm.h"
#include <interfaces/iproject.h>

#include <KPluginFactory>
#include <KLocalizedString>
#include <KConfigGroup>
#include <QFormLayout>

namespace Python {

K_PLUGIN_FACTORY(PythonProjectKCMFactory, registerPlugin<PythonProjectKCM>();)
K_EXPORT_PLUGIN(PythonProjectKCMFactory("kcm_kdevpythonproject"))

PythonProjectKCM::PythonProjectKCM(QWidget* parent, const QVariantList& args)
    : ProjectKCModule<PythonProjectSettings>(PythonProjectKCMFactory::componentData(), parent, args)
{
    QFormLayout* form = new QFormLayout();
    languageVersion = new QComboBox();
    languageVersion->addItem("Python 3");
    languageVersion->addItem("Python 2");
    form->addRow(i18n("Language version for Python files in this project:"), languageVersion);
    setLayout(form);
}

void PythonProjectKCM::load()
{
    KConfigGroup group(project()->projectConfiguration()->group("python"));
    const QString& version = group.readEntry("languageVersion", "Python 3");
    languageVersion->setCurrentIndex(languageVersion->findText(version));
}

void PythonProjectKCM::save()
{
    KConfigGroup group(project()->projectConfiguration()->group("python"));
    group.writeEntry("languageVersion", languageVersion->currentText());
}

void PythonProjectKCM::defaults()
{
    languageVersion->setCurrentIndex(0);
}


} // namespace Python

#endif // PYTHONPROJECTKCM_H
