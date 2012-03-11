/*
    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) 2012  <copyright holder> <email>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/


#ifndef SIMPLEREFACTORING_H
#define SIMPLEREFACTORING_H

#include <QtCore/QObject>
#include <interfaces/contextmenuextension.h>
#include <interfaces/context.h>
#include <language/duchain/indexeddeclaration.h>

namespace Python {

class SimpleRefactoring : public QObject
{
Q_OBJECT
public:
    static SimpleRefactoring& self();
    void doContextMenu(KDevelop::ContextMenuExtension& extension, KDevelop::Context* context);
    void startInteractiveRename(KDevelop::IndexedDeclaration decl);
    KDevelop::IndexedDeclaration declarationUnderCursor(bool allowUse = true);
public slots:
    void executeRenameAction();
};

}

#endif // SIMPLEREFACTORING_H
