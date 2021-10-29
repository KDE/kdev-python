/*
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>
    SPDX-FileCopyrightText: 2014 Miquel Sabaté <mikisabate@gmail.com>

    SPDX-License-Identifier: LGPL-2.0-or-later
*/

#ifndef REFACTORING_H_
#define REFACTORING_H_


#include <interfaces/context.h>
#include <language/codegen/basicrefactoring.h>

namespace KDevelop {
    class Declaration;
}


namespace Python {

class RefactoringCollector : public KDevelop::BasicRefactoringCollector
{
    Q_OBJECT

public:
    RefactoringCollector(const KDevelop::IndexedDeclaration &decl);

protected:
    void processUses(KDevelop::ReferencedTopDUContext topContext) override;
};

class Refactoring : public KDevelop::BasicRefactoring
{
    Q_OBJECT

public:
    explicit Refactoring(QObject *parent = nullptr);

protected:
    bool acceptForContextMenu(const KDevelop::Declaration *decl) override;
};

}

#endif // REFACTORING_H_
