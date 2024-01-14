/*
    SPDX-FileCopyrightText: 2013 Sven Brauch <svenbrauch@gmail.com>

    SPDX-License-Identifier: GPL-2.0-only OR GPL-3.0-only OR LicenseRef-KDE-Accepted-GPL
*/

#include "missingincludeassistant.h"
#include <docfilekcm/docfilewizard.h>
#include <interfaces/icore.h>
#include <interfaces/idocumentcontroller.h>
#include <interfaces/ilanguagecontroller.h>
#include <language/backgroundparser/backgroundparser.h>

#include <QDebug>
#include <QStandardPaths>
#include <duchaindebug.h>


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
    QString path = QStandardPaths::writableLocation(QStandardPaths::GenericDataLocation) + QStringLiteral("/") + QStringLiteral("kdevpythonsupport/documentation_files/");
    QDir dir(path);
    dir.mkpath(path);
    auto wizard = new DocfileWizard(path);
    wizard->setModuleName(module);
    wizard->setModal(true);
    wizard->setAttribute(Qt::WA_DeleteOnClose);
    wizard->show();
    QObject::connect(wizard, &QDialog::accepted,
        [wizard, this]() {
            if ( ! wizard->wasSavedAs().isNull() ) {
                ICore::self()->documentController()->openDocument(QUrl::fromLocalFile(wizard->wasSavedAs()));
                // force a recursive update of the context, so that all the imports are reparsed too
                // (since they potentially have changed through this action)
                ICore::self()->languageController()->backgroundParser()->addDocument(document, TopDUContext::ForceUpdateRecursive);
            }
        }
    );

    /*emit */executed(this);
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

#include "moc_missingincludeassistant.cpp"
