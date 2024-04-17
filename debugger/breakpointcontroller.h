/*
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef BREAKPOINTCONTROLLER_H
#define BREAKPOINTCONTROLLER_H

#include <debugger/interfaces/ibreakpointcontroller.h>
#include "debugsession.h"

using namespace KDevelop;

namespace Python {

class BreakpointController : public KDevelop::IBreakpointController
{
Q_OBJECT
public:
    BreakpointController(IDebugSession* parent);

    void breakpointAdded(int row) override;

    void breakpointModelChanged(int row, BreakpointModel::ColumnFlags columns) override;

    void breakpointAboutToBeDeleted(int row) override;

public Q_SLOTS:
    /**
     * @brief Handles events in the debug session.
     * It is used here to send breakpoints to the debugger which were created by the user
     * before the program was started.
     * 
     * @param evt passed by kdevplatform, specifies the type of the event.
     **/
    void slotEvent(IDebugSession::event_t evt);
protected:
    /**
     * Note: this method exists solely to full fill KDevelop::IBreakpointController
     *       interface to ease the API transition; it should be removed at once
     *       when KDevelop::IBreakpointController no longer requires the override.
     **/
    void sendMaybe(KDevelop::Breakpoint* breakpoint) override
    {
        Q_UNUSED(breakpoint);
    }
    DebugSession* session();
};

}

#endif // BREAKPOINTCONTROLLER_H
