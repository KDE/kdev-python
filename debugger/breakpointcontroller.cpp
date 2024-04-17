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
    if ( evt == IDebugSession::connected_to_program ) {
        const auto breakpoints = breakpointModel()->breakpoints();
        for (Breakpoint* const bp : breakpoints) {
            // TODO
        }
    }
}

void BreakpointController::breakpointAdded(int row)
{
    auto* modelBreakpoint = breakpointModel()->breakpoint(row);

    qCDebug(KDEV_PYTHON_DEBUGGER) << "adding breakpoint: " << modelBreakpoint << "( line:" << modelBreakpoint->line()
                                  << ")";
    // TODO
}

void BreakpointController::breakpointModelChanged(int row, BreakpointModel::ColumnFlags columns)
{
    // TODO
    Q_UNUSED(row);
    Q_UNUSED(columns);
}

void BreakpointController::breakpointAboutToBeDeleted(int row)
{
    auto* modelBreakpoint = breakpointModel()->breakpoint(row);
    qCDebug(KDEV_PYTHON_DEBUGGER) << "removing breakpoint: " << modelBreakpoint << "( line:" << modelBreakpoint->line()
                                  << ")";
    // TODO
}
}

#include "moc_breakpointcontroller.cpp"
