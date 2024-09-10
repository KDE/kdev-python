/*
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef VARIABLECONTROLLER_H
#define VARIABLECONTROLLER_H
#include <debugger/interfaces/ivariablecontroller.h>
#include <debugger/interfaces/idebugsession.h>
#include "variable.h"

#include <QTimer>

using namespace KDevelop;

namespace Python {

class VariableController : public KDevelop::IVariableController
{
Q_OBJECT
public:
    VariableController(IDebugSession* parent);
    void addWatch(KDevelop::Variable* variable) override;
    void addWatchpoint(KDevelop::Variable* variable) override;
    
    /**
     * @brief This just calls the Variable constructor and returns a new, empty \a Variable object.
     **/
    KDevelop::Variable* createVariable(KDevelop::TreeModel* model, KDevelop::TreeItem* parent,
                                               const QString& expression, const QString& display = QString()) override;
    
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
    KTextEditor::Range expressionRangeUnderCursor(KTextEditor::Document* doc, const KTextEditor::Cursor& cursor) override;

    /**
     * @brief Update locals and/or watches, as indicated by autoUpdate().
     **/
    void update() override;
protected:
    /**
     * @brief Overridden to handle frame change events (when the user clicks the frame list).
     * This then enqueues many "up" or "down" commands to react to the frame change.
     **/
    void handleEvent(IDebugSession::event_t event) override;

private:
    QTimer m_updateTimer;
    QList<Variable*> m_watchVariables;

private Q_SLOTS:
    /**
     * @brief Parse the debugger output, and perform an update of the local variables.
     **/
    void localsUpdateReady(QByteArray rawData);

    void _update();
};

}

#endif // VARIABLECONTROLLER_H
