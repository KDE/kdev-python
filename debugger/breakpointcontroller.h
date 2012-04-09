/*
    This file is part of kdev-python, the python language plugin for KDevelop
    Copyright (C) 2012  Sven Brauch <svenbrauch@googlemail.com>

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
public slots:
    /**
     * @brief Handles events in the debug session.
     * It is used here to send breakpoints to the debugger which were created by the user
     * before the program was started.
     * 
     * @param evt passed by kdevplatform, specifies the type of the event.
     * @return void
     **/
    void slotEvent(IDebugSession::event_t evt);
protected:
    /**
     * @brief Notify the debugger about a breakpoint update.
     * This is triggered if the user clicks the breakpoint bar.
     * Deleting breakpoints is also handled here.
     * 
     * @param breakpoint The breakpoint to update.
     * @return void
     **/
    virtual void sendMaybe(KDevelop::Breakpoint* breakpoint);
    DebugSession* session();
};

}

#endif // BREAKPOINTCONTROLLER_H
