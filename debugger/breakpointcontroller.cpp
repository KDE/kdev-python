/*
    This file is part of kdev-python, the python language plugin for KDevelop
    Copyright (C) 2012  Sven Brauch <svenbrauch@googlemail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/


#include "breakpointcontroller.h"
#include <debugger/breakpoint/breakpointmodel.h>

#include <QDebug>
#include "debuggerdebug.h"

namespace Python {
    
BreakpointController::BreakpointController(IDebugSession* parent): IBreakpointController(parent)
{
    qCDebug(KDEV_PYTHON_DEBUGGER) << "constructing breakpoint controller";
    connect(debugSession(), SIGNAL(event(IDebugSession::event_t)), this, SLOT(slotEvent(IDebugSession::event_t)));
}

DebugSession* BreakpointController::session()
{
    return static_cast<DebugSession*>(parent());
}

void BreakpointController::slotEvent(IDebugSession::event_t evt)
{
    qCDebug(KDEV_PYTHON_DEBUGGER) << evt;
    if ( evt == IDebugSession::connected_to_program ) {
        foreach ( Breakpoint* bp, breakpointModel()->breakpoints() ) {
            if ( bp->deleted() ) {
                continue;
            }
            session()->addBreakpoint(bp);
        }
    }
}

void BreakpointController::sendMaybe(KDevelop::Breakpoint* breakpoint)
{
    qCDebug(KDEV_PYTHON_DEBUGGER) << "sending breakpoint: " << breakpoint << "( deleted:" << breakpoint->deleted() << ")";
    if ( breakpoint->deleted() ) {
        session()->removeBreakpoint(breakpoint);
    }
    else {
        session()->addBreakpoint(breakpoint);
    }
}

}

