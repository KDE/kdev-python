/*
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>
    SPDX-FileCopyrightText: 2024 Jarmo Tiitto <jarmo.tiitto@gmail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#include "breakpointcontroller.h"
#include <debugger/breakpoint/breakpointmodel.h>

#include <QDebug>
#include "debuggerdebug.h"

#include <algorithm>

// TODO: BreakpointController is not yet invoking notifyHit() to tell the model a breakpoint was hit...

namespace Python {

BreakpointController::BreakpointController(IDebugSession* parent)
    : IBreakpointController(parent)
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
    const auto breakpoints = breakpointModel()->breakpoints();

    if (evt == IDebugSession::debugger_exited) {
        // Reset breakpoint states.
        for (Breakpoint* const bp : breakpoints) {
            bp->setState(Breakpoint::NotStartedState);
        }
        return;
    }
    if (evt != IDebugSession::connected_to_program) {
        return;
    }

    qCDebug(KDEV_PYTHON_DEBUGGER) << "insert" << breakpoints.size() << "model breakpoints";

    for (Breakpoint* const bp : breakpoints) {
        addBreakpoint(bp);
    }
}

void BreakpointController::breakpointAdded(int row)
{
    auto* modelBreakpoint = breakpointModel()->breakpoint(row);
    addBreakpoint(modelBreakpoint);
}

void BreakpointController::breakpointModelChanged(int row, BreakpointModel::ColumnFlags columns)
{
    columns &= BreakpointModel::LocationColumnFlag;
    if (!columns) {
        return;
    }

    auto* const modelBreakpoint = breakpointModel()->breakpoint(row);
    updateBreakpoint(modelBreakpoint);

    // TODO: - implement breakpoint enable/disable state.
    //       - implement breakpoint hit count. (feedback on breakpoint hit)
    //       - implement breakpoint ignore hits.
    //       - implement breakpoint condition.
}

void BreakpointController::breakpointAboutToBeDeleted(int row)
{
    auto* modelBreakpoint = breakpointModel()->breakpoint(row);
    removeBreakpoint(modelBreakpoint);
}

bool BreakpointController::isSupportedBreakpoint(Breakpoint* bp)
{
    static const QRegularExpression pyfiles(QStringLiteral(".*\\.py.*$"), QRegularExpression::CaseInsensitiveOption);

    if (bp->url().isEmpty() || bp->savedLine() == -1) {
        return false;
    } else if (!pyfiles.match(bp->url().path()).hasMatch()) {
        return false;
    } else if (bp->kind() != KDevelop::Breakpoint::CodeBreakpoint || !bp->expression().isEmpty()) {
        // No support for expressions... of any kind.
        qCDebug(KDEV_PYTHON_DEBUGGER) << "Implement me: kdevpdb has no support for expression breakpoints";
        return false;
    }

    return true;
}

QString BreakpointController::locationForBreakpoint(Breakpoint* bp)
{
    /*
     * Breakpoint::savedLine() is used for the location since it should match the document's state on disk.
     * This also makes the debugger ignore unsaved modifications of the document, which allows the
     * user to minimally *modify* the document while debugging. (E.g. comment the code)
     */
    return bp->url().path() + QLatin1Char(':') + QString::number(bp->savedLine() + 1);
}

std::vector<BreakpointDataPtr>::iterator BreakpointController::lookupBreakpointData(Breakpoint* bp)
{
    return std::find_if(m_breakpoints.begin(), m_breakpoints.end(), [bp](const BreakpointDataPtr& brk) -> bool {
        return brk->modelBreakpoint == bp;
    });
}

void BreakpointController::addBreakpoint(Breakpoint* bp)
{
    // We have not added this breakpoint yet, right?
    if (lookupBreakpointData(bp) != m_breakpoints.end()) {
        qCWarning(KDEV_PYTHON_DEBUGGER) << "model breakpoint" << bp << "already registered";
        return;
    }

    // Add entry for the model breakpoint.
    const auto& brk = m_breakpoints.emplace_back(BreakpointDataPtr::create(bp));
    const QString location = locationForBreakpoint(bp);

    if (!isSupportedBreakpoint(bp)) {
        // updateBreakpoint() inserts the breakpoint once it changes to something valid.
        qCDebug(KDEV_PYTHON_DEBUGGER) << "breakpoint " << bp << "location" << location << "rejected";
        bp->setState(Breakpoint::DirtyState);
        return;
    }

    qCDebug(KDEV_PYTHON_DEBUGGER) << "inserting breakpoint" << bp << location;

    bp->setState(Breakpoint::PendingState);

    // (try) insert the PDB breakpoint.
    brk->breakpointId = m_debuggerBreakpointId++;
    session()->debugger()->request(CMD_BREAK.arg(location), [this, brk](const ResponseData& d) {
        addHandler(d, brk);
    });
    session()->flushCommands();
}

void BreakpointController::addHandler(const ResponseData& data, const BreakpointDataPtr& brk)
{
    if (responseValue(data, QStringLiteral("error")).isUndefined()) {
        // Insertion succeeded.
        if (brk->modelBreakpoint) {
            brk->modelBreakpoint->setState(Breakpoint::CleanState);
        }
        return;
    }

    if (brk->modelBreakpoint) {
        brk->modelBreakpoint->setState(Breakpoint::DirtyState);
    }

    qCDebug(KDEV_PYTHON_DEBUGGER) << "breakpoint insertion failed:" << brk->breakpointId.value();

    // Pdb rejected the breakpoint's location, and therefore the server didn't use the brk->breakpointId.
    --m_debuggerBreakpointId;
    const int invalidId = brk->breakpointId.value();
    // Cancel a possible already queued removeHandler()
    brk->breakpointId.reset();
    // Subtract one from all PDB ids greater than invalidId to correct them.
    for (const auto& breakpoint : m_breakpoints) {
        if (breakpoint->breakpointId.value_or(-1) < invalidId) {
            continue;
        }
        qCDebug(KDEV_PYTHON_DEBUGGER) << "fix-up pending id:" << breakpoint->breakpointId.value() << "as"
                                      << breakpoint->breakpointId.value() - 1;
        breakpoint->breakpointId.value()--;
    }
}

void BreakpointController::removeBreakpoint(Breakpoint* bp)
{
    auto itr = lookupBreakpointData(bp);
    if (itr == m_breakpoints.end()) {
        // No breakpoint inserted for bp currently?
        qCWarning(KDEV_PYTHON_DEBUGGER) << "no BreakpointData found for" << bp;
        return;
    }

    // Erase from m_breakpoints. (swap-and-pop-back)
    BreakpointDataPtr brk(std::move(*itr));
    itr->swap(m_breakpoints.back());
    m_breakpoints.pop_back();
    // Cancel all on-going insertions of this model breakpoint by updateHandler().
    brk->modelBreakpoint = nullptr;

    session()->debugger()->defer([this, brk](const ResponseData&) {
        if (removeHandler(brk)) {
            session()->flushCommands();
        }
    });
    session()->flushCommands();
}

bool BreakpointController::removeHandler(const BreakpointDataPtr& brk)
{
    if (!brk->breakpointId) {
        // No PDB breakpoint available to clear.
        return false;
    }
    int delId = brk->breakpointId.value();
    brk->breakpointId.reset();
    session()->debugger()->request(CMD_CLEAR.arg(delId));
    return true;
}

void BreakpointController::updateBreakpoint(Breakpoint* bp)
{
    auto itr = lookupBreakpointData(bp);
    if (itr == m_breakpoints.end()) {
        // No breakpoint inserted for bp currently?
        qCWarning(KDEV_PYTHON_DEBUGGER) << "no BreakpointData found for" << bp;
        return;
    }

    BreakpointDataPtr brk = *itr;
    const QString location = locationForBreakpoint(bp);

    if (!isSupportedBreakpoint(bp)) {
        // Rejected.
        qCDebug(KDEV_PYTHON_DEBUGGER) << "updated breakpoint " << bp << "location" << location << "rejected";
        bp->setState(Breakpoint::DirtyState);

        session()->debugger()->defer([this, brk](const ResponseData&) {
            if (removeHandler(brk)) {
                session()->flushCommands();
            }
        });
        session()->flushCommands();
        return;
    }

    qCDebug(KDEV_PYTHON_DEBUGGER) << "updated breakpoint " << bp << "location" << location << "accepted";

    bp->setState(Breakpoint::PendingState);

    // Queue a update of the breakpoint.
    session()->debugger()->defer([this, brk, location](const ResponseData&) {
        updateHandler(brk, location);
    });
    session()->flushCommands();
}

void BreakpointController::updateHandler(const BreakpointDataPtr& brk, QString location)
{
    // TODO: Apply breakpoint enable/disabled state, and don't do re-insert if the location didn't change.

    // Only way to change the location is to create a new PDB breakpoint,
    // so erase the old PDB breakpoint first, if it exist.
    bool flush = removeHandler(brk);
    // Insert only if the model breakpoint has not been deleted yet.
    if (brk->modelBreakpoint) {
        brk->breakpointId = m_debuggerBreakpointId++;
        session()->debugger()->request(CMD_BREAK.arg(location), [this, brk](const ResponseData& d) {
            addHandler(d, brk);
        });
        flush = true;
    }
    if (flush) {
        session()->flushCommands();
    }
}
}

#include "moc_breakpointcontroller.cpp"
