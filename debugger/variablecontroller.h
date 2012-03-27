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
Q_OBJECT
public:
    VariableController(IDebugSession* parent);
    virtual void addWatch(KDevelop::Variable* variable);
    virtual void addWatchpoint(KDevelop::Variable* variable);
    
    /**
     * @brief This just calls the Variable constructor and returns a new, empty \a Variable object.
     **/
    virtual KDevelop::Variable* createVariable(KDevelop::TreeModel* model, KDevelop::TreeItem* parent, const QString& expression, const QString& display = "");
    
    /**
     * @brief Mini-parser which gives the expression under the cursor.
     * Example: _I_ = cursor
     * self.fo_I_obar(something) # should return "self.foobar"
     * self.foobar(some_I_thing) # should return "something"
     * The expressions returned by this are "print"ed by the debugger, and then displayed in the tooltip.
     * @param doc The document to operate on
     * @param cursor the cursor position
     * @return The expression to print. Should be an (at least syntactically) valid python expression
     **/
    virtual QString expressionUnderCursor(KTextEditor::Document* doc, const KTextEditor::Cursor& cursor);
    
    /**
     * @brief Update locals and/or watches, as indicated by autoUpdate().
     **/
    virtual void update();
protected:
    /**
     * @brief Overriden to handle frame change events (when the user clicks the frame list).
     * This then enqueues many "up" or "down" commands to react to the frame change.
     **/
    virtual void handleEvent(IDebugSession::event_t event);
private:
    QList<Variable*> m_watchVariables;
private slots:
    /**
     * @brief Parse the debugger output, and perform an update of the local variables.
     **/
    void localsUpdateReady(QByteArray rawData);
};

}

#endif // VARIABLECONTROLLER_H
