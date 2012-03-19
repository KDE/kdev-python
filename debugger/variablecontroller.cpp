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


#include "variablecontroller.h"
#include "variable.h"

#include <debugger/variable/variablecollection.h>

using namespace KDevelop;

namespace Python {

VariableController::VariableController(IDebugSession* parent) : IVariableController(parent)
{

}

void VariableController::addWatch(KDevelop::Variable* variable)
{
    kDebug() << "addWatch requested (not implemented)";
}

void VariableController::addWatchpoint(KDevelop::Variable* variable)
{
    kDebug() << "addWatchpoint requested (not implemented)";
}

KDevelop::Variable* VariableController::createVariable(KDevelop::TreeModel* model, KDevelop::TreeItem* parent, const QString& expression, const QString& display)
{
    return new Variable(model, parent, expression, display);
}

QString VariableController::expressionUnderCursor(KTextEditor::Document* doc, const KTextEditor::Cursor& cursor)
{
    kDebug() << "expressionUnderCursor requested (not implemented)";
    return "not implemented: expressionUnderCursor";
}

void VariableController::update()
{
    kDebug() << "update requested (not implemented)";
}

}

