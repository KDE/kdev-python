/*
    SPDX-FileCopyrightText: 2013 Sven Brauch <svenbrauch@gmail.com>

    SPDX-License-Identifier: GPL-2.0-only OR GPL-3.0-only OR LicenseRef-KDE-Accepted-GPL
*/

#ifndef PYTHON_MISSINGINCLUDEASSISTANT_H
#define PYTHON_MISSINGINCLUDEASSISTANT_H

#include <interfaces/iassistant.h>
#include <serialization/indexedstring.h>
#include <language/duchain/problem.h>

#include <QObject>
#include <QExplicitlySharedDataPointer>

namespace Python {

// TODO: add data class with own identity so it gets restored correctly
class MissingIncludeProblem : public KDevelop::Problem {
public:
    MissingIncludeProblem(const QString& moduleName, KDevelop::IndexedString currentDocument);
    QExplicitlySharedDataPointer<KDevelop::IAssistant> solutionAssistant() const override;

private:
    QString m_moduleName;
    KDevelop::IndexedString m_currentDocument;
};

class DocumentationGeneratorAction : public KDevelop::IAssistantAction
{
Q_OBJECT
public:
    DocumentationGeneratorAction(const QString& module, const KDevelop::IndexedString& document);
    QString description() const override;

public Q_SLOTS:
    void execute() override;

private:
    const QString module;
    const KDevelop::IndexedString document;
};

class MissingIncludeAssistant : public KDevelop::IAssistant
{
Q_OBJECT
public:
    MissingIncludeAssistant(const QString& module, const KDevelop::IndexedString& document);
    void createActions() override;
private:
    const QString module;
    const KDevelop::IndexedString document;
};

}

#endif // PYTHON_MISSINGINCLUDEASSISTANT_H
