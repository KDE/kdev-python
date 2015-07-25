/*
 * This file is part of kdev-python, the Python language support plugin for KDevelop
 * Copyright 2013 Sven Brauch <svenbrauch@gmail.com>
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

#include "missingincludeassistant.h"
#include <docfilekcm/docfilewizard.h>
#include <interfaces/icore.h>
#include <interfaces/idocumentcontroller.h>
#include <interfaces/ilanguagecontroller.h>
#include <language/backgroundparser/backgroundparser.h>

#include <iostream>

#include <QDebug>
#include <QStandardPaths>
#include "../duchaindebug.h"


#include <KAction>
#include <KLocalizedString>

using namespace KDevelop;

namespace Python {

MissingIncludeProblem::MissingIncludeProblem(const QString &moduleName, IndexedString currentDocument)
    : Problem()
    , m_moduleName(moduleName)
    , m_currentDocument(currentDocument)
{

}

QExplicitlySharedDataPointer<IAssistant> MissingIncludeProblem::solutionAssistant() const
{
    return QExplicitlySharedDataPointer<IAssistant>(new MissingIncludeAssistant(m_moduleName, m_currentDocument));
}

DocumentationGeneratorAction::DocumentationGeneratorAction(const QString& module, const IndexedString& document)
    : IAssistantAction()
    , module(module)
    , document(document)
{

}

QString DocumentationGeneratorAction::description() const
{
    return i18n("Generate documentation for module \"%1\"...", module);
}

void DocumentationGeneratorAction::execute()
{
    // yes, it's duplicate from the doc file widget, but it's too painful to share it
    QDir dir(QStandardPaths::GenericDataLocation + "kdevpythonsupport/documentation_files/");
    dir.mkpath(QStandardPaths::GenericDataLocation + "kdevpythonsupport/documentation_files/");
    QString path = QStandardPaths::writableLocation(QStandardPaths::GenericDataLocation) + "/" + "kdevpythonsupport/documentation_files/";
    DocfileWizard wizard(path);
    wizard.setModuleName(module);
    wizard.exec();
    if ( ! wizard.wasSavedAs().isNull() ) {
        ICore::self()->documentController()->openDocument(QUrl::fromLocalFile(wizard.wasSavedAs()));
        // force a recursive update of the context, so that all the imports are reparsed too
        // (since they potentially have changed through this action)
        ICore::self()->languageController()->backgroundParser()->addDocument(document, TopDUContext::ForceUpdateRecursive);
    }
    emit executed(this);
}

void MissingIncludeAssistant::createActions()
{
    QExplicitlySharedDataPointer<IAssistantAction> action(new DocumentationGeneratorAction(module, document));
    addAction(action);
}

MissingIncludeAssistant::MissingIncludeAssistant(const QString& module, const IndexedString& document)
    : IAssistant()
    , module(module)
    , document(document)
{
}

}

