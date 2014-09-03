/*
 * This file is part of kdev-python
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

#ifndef PYTHON_MISSINGINCLUDEASSISTANT_H
#define PYTHON_MISSINGINCLUDEASSISTANT_H

#include <interfaces/iassistant.h>
#include <language/duchain/indexedstring.h>
#include <language/duchain/problem.h>

#include <QObject>

namespace Python {

// TODO: add data class with own identity so it gets restored correctly
class MissingIncludeProblem : public KDevelop::Problem {
public:
    MissingIncludeProblem(const QString& moduleName, KDevelop::IndexedString currentDocument);
    virtual KSharedPtr< KDevelop::IAssistant > solutionAssistant() const;

private:
    QString m_moduleName;
    KDevelop::IndexedString m_currentDocument;
};

class DocumentationGeneratorAction : public KDevelop::IAssistantAction
{
Q_OBJECT
public:
    DocumentationGeneratorAction(const QString& module, const KDevelop::IndexedString& document);
    virtual QString description() const;

public slots:
    virtual void execute();

private:
    const QString module;
    const KDevelop::IndexedString document;
};

class MissingIncludeAssistant : public KDevelop::IAssistant
{
Q_OBJECT
public:
    MissingIncludeAssistant(const QString& module, const KDevelop::IndexedString& document);
    virtual void createActions();
private:
    const QString module;
    const KDevelop::IndexedString document;
};

}

#endif // PYTHON_MISSINGINCLUDEASSISTANT_H
