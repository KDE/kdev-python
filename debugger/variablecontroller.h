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


#ifndef VARIABLECONTROLLER_H
#define VARIABLECONTROLLER_H
#include <debugger/interfaces/ivariablecontroller.h>
#include <debugger/interfaces/idebugsession.h>
#include "variable.h"

using namespace KDevelop;

namespace Python {

class VariableController : public KDevelop::IVariableController
{
public:
    VariableController(IDebugSession* parent);
    virtual void addWatch(KDevelop::Variable* variable);
    virtual void addWatchpoint(KDevelop::Variable* variable);
    virtual KDevelop::Variable* createVariable(KDevelop::TreeModel* model, KDevelop::TreeItem* parent, const QString& expression, const QString& display = "");
    virtual QString expressionUnderCursor(KTextEditor::Document* doc, const KTextEditor::Cursor& cursor);
    virtual void update();
private:
    QList<Variable*> m_watchVariables;
};

}

#endif // VARIABLECONTROLLER_H
