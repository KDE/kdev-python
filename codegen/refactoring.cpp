/*
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>
    SPDX-FileCopyrightText: 2014 Miquel Sabaté <mikisabate@gmail.com>

    SPDX-License-Identifier: LGPL-2.0-or-later
*/

#include "refactoring.h"
#include "duchain/helpers.h"

#include <QDebug>
#include "codegendebug.h"

namespace Python {

RefactoringCollector::RefactoringCollector(const IndexedDeclaration &decl)
    : BasicRefactoringCollector(decl)
{
    /* There's nothing to do in here.*/
}

void RefactoringCollector::processUses(KDevelop::ReferencedTopDUContext topContext)
{
    if (topContext != Helper::getDocumentationFileContext())
        RefactoringCollector::processUses(topContext);
}

Refactoring::Refactoring(QObject *parent)
    : BasicRefactoring(parent)
{
    /* There's nothing to do in here.*/
}

bool Refactoring::acceptForContextMenu(const KDevelop::Declaration* decl)
{
    if (decl->topContext() == Helper::getDocumentationFileContext()) {
        qCDebug(KDEV_PYTHON_CODEGEN) << "in doc file, not offering rename action";
        return false;
    }
    return true;
}

}

#include "moc_refactoring.cpp"
