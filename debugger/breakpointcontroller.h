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
     * @brief Notify the debugger about a breakpoint update.
     * This is triggered if the user clicks the breakpoint bar.
     * Deleting breakpoints is also handled here.
     * 
     * @param breakpoint The breakpoint to update.
     **/
    void sendMaybe(KDevelop::Breakpoint* breakpoint) override;
    DebugSession* session();
};

}

#endif // BREAKPOINTCONTROLLER_H
