/***************************************************************************
 *   This file is part of KDevelop                                         *
 *   Copyright 2012 Sven Brauch <svenbrauch@googlemail.com>                *
 *   Copyright 2014 Miquel Sabaté <mikisabate@gmail.com>                   *
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU Library General Public License as       *
 *   published by the Free Software Foundation; either version 2 of the    *
 *   License, or (at your option) any later version.                       *
 *                                                                         *
 *   This program is distributed in the hope that it will be useful,       *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
 *   GNU General Public License for more details.                          *
 *                                                                         *
 *   You should have received a copy of the GNU Library General Public     *
 *   License along with this program; if not, write to the                 *
 *   Free Software Foundation, Inc.,                                       *
 *   51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.         *
 ***************************************************************************/

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
    explicit Refactoring(QObject *parent = 0);

protected:
    bool acceptForContextMenu(const KDevelop::Declaration *decl) override;
};

}

#endif // REFACTORING_H_
