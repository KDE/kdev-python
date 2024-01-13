/*
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
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
        for ( Breakpoint* bp : breakpointModel()->breakpoints() ) {
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

#include "moc_breakpointcontroller.cpp"
