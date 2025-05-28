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

namespace Python {

BreakpointController::BreakpointController(IDebugSession* parent)
    : IBreakpointController(parent)
{
    qCDebug(KDEV_PYTHON_DEBUGGER) << "constructing breakpoint controller";
    connect(debugSession(), SIGNAL(event(IDebugSession::event_t)), this, SLOT(slotEvent(IDebugSession::event_t)));
    connect(session(), &DebugSession::programStopped, this, &BreakpointController::programStopped);
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

void BreakpointController::programStopped(QString filename, int line)
{
    // srclocation must be comparable with locationForBreakpoint()
    const auto srclocation = std::make_pair(filename, line + 1);

    if (m_temporaryBreakpoint && m_temporaryBreakpoint->location == srclocation) {
        qCDebug(KDEV_PYTHON_DEBUGGER) << "temporary breakpoint location" << srclocation << "was reached";
        return;
    }

    for (const auto& brk : m_breakpoints) {
        // Note: the currently inserted PDB breakpoint location is compared,
        //       rather than the model breakpoint, which may have changed since.
        if (!brk->breakpointId || !brk->enabled || !brk->modelBreakpoint || brk->location != srclocation) {
            continue;
        }
        // A breakpoint was hit:
        // Increment hit count. (by-pass IBreakpointController::updateHitCount() which does the same thing.)
        brk->modelBreakpoint->setHitCount(brk->modelBreakpoint->hitCount() + 1);

        // FIXME: BreakpointWidget only guarantees a update of the BreakpointDetails for columns up to ConditionColumn.
        //        Strobe the status column as work-around to force updating of the BreakpointDetails.
        auto state = brk->modelBreakpoint->state();
        brk->modelBreakpoint->setState(Breakpoint::DirtyState);
        brk->modelBreakpoint->setState(state);

        // Notify.
        int row = breakpointModel()->breakpoints().indexOf(brk->modelBreakpoint);
        notifyHit(row, QString());
        return;
    }
}

void BreakpointController::breakpointAdded(int row)
{
    auto* modelBreakpoint = breakpointModel()->breakpoint(row);
    addBreakpoint(modelBreakpoint);
}

void BreakpointController::breakpointModelChanged(int row, BreakpointModel::ColumnFlags columns)
{
    columns &= BreakpointModel::LocationColumnFlag | BreakpointModel::EnableColumnFlag;
    if (!columns) {
        return;
    }

    auto* const modelBreakpoint = breakpointModel()->breakpoint(row);
    updateBreakpoint(modelBreakpoint);

    // TODO: - implement breakpoint ignore hits.
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

std::pair<QString, int> BreakpointController::locationForBreakpoint(Breakpoint* bp)
{
    /*
     * Breakpoint::savedLine() is used for the location since it should match the document's state on disk.
     * This also makes the debugger ignore unsaved modifications of the document, which allows the
     * user to minimally *modify* the document while debugging. (E.g. comment the code)
     */
    return std::make_pair(bp->url().path(), bp->savedLine() + 1);
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
    const auto location = locationForBreakpoint(bp);

    if (!isSupportedBreakpoint(bp)) {
        // updateBreakpoint() inserts the breakpoint once it changes to something valid.
        qCDebug(KDEV_PYTHON_DEBUGGER) << "breakpoint " << bp << "location" << location.first << ':' << location.second
                                      << "rejected";
        bp->setState(Breakpoint::DirtyState);
        return;
    }

    qCDebug(KDEV_PYTHON_DEBUGGER) << "inserting breakpoint" << bp << location.first << ':' << location.second;

    bp->setState(Breakpoint::PendingState);

    // (try) insert the PDB breakpoint.
    brk->breakpointId = m_debuggerBreakpointId++;
    brk->location = location;
    brk->enabled = bp->enabled();
    session()->debugger()->request({CMD_BREAK, location.first, location.second, !brk->enabled},
        [this, brk](const ResponseData& d) {
        addHandler(d, brk);
    });
    session()->flushCommands();
}

void BreakpointController::addHandler(const ResponseData& data, const BreakpointDataPtr& brk)
{
    const auto result = responseValue(data, QStringLiteral("error"));
    if (result.isUndefined()) {
        // Insertion succeeded.
        if (brk->modelBreakpoint) {
            brk->modelBreakpoint->setHitCount(0);
            brk->modelBreakpoint->setState(Breakpoint::CleanState);
        }
        return;
    }

    if (brk->modelBreakpoint) {
        brk->modelBreakpoint->setState(Breakpoint::DirtyState);
    }

    qCDebug(KDEV_PYTHON_DEBUGGER) << "breakpoint insertion failed:" << brk->breakpointId.value() << result.toString();

    // The breakpoint's location was rejected, and therefore the server didn't use the brk->breakpointId.
    --m_debuggerBreakpointId;
    const int invalidId = brk->breakpointId.value();
    // Cancel a possible already queued removeHandler()
    brk->breakpointId.reset();
    brk->location.first.clear();
    brk->location.second = -1;
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
    brk->location.first.clear();
    brk->location.second = -1;
    session()->debugger()->request({CMD_CLEAR, delId});
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
    const auto location = locationForBreakpoint(bp);

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

void BreakpointController::updateHandler(const BreakpointDataPtr& brk, std::pair<QString, int> location)
{
    // Update just the enabled/disabled state if location is up-to-date.
    if (brk->modelBreakpoint && brk->breakpointId && brk->location == location) {
        brk->modelBreakpoint->setState(Breakpoint::CleanState);
        if (brk->modelBreakpoint->enabled() == brk->enabled) {
            // No change to location or enabled state, nothing to do.
            return;
        }
        // Just the enabled state changed.
        brk->enabled = brk->modelBreakpoint->enabled();
        if (brk->enabled) {
            qCDebug(KDEV_PYTHON_DEBUGGER) << "enabling breakpoint" << brk->modelBreakpoint;
            session()->debugger()->request({CMD_ENABLE, brk->breakpointId.value()});
        } else {
            qCDebug(KDEV_PYTHON_DEBUGGER) << "disabling breakpoint" << brk->modelBreakpoint;
            session()->debugger()->request({CMD_DISABLE, brk->breakpointId.value()});
        }
        session()->flushCommands();
        return;
    }

    // Only way to change the location is to create a new PDB breakpoint,
    // so erase the old PDB breakpoint first, if it exist.
    bool flush = removeHandler(brk);
    // Insert only if the model breakpoint has not been deleted yet.
    if (brk->modelBreakpoint) {
        brk->breakpointId = m_debuggerBreakpointId++;
        brk->enabled = brk->modelBreakpoint->enabled();
        session()->debugger()->request({CMD_BREAK, location.first, location.second, !brk->enabled},
        [this, brk](const ResponseData& d) {
            addHandler(d, brk);
        });
        flush = true;
    }
    if (flush) {
        session()->flushCommands();
    }
}

void BreakpointController::runToLocation(const QUrl& fileName, int line, PdbDebuggerInstance::CmdCallback callback,
                                         bool excludeOthers)
{
    // Create a free-standing breakpoint detached from the model.
    auto bp = std::make_unique<KDevelop::Breakpoint>(nullptr, Breakpoint::CodeBreakpoint);
    bp->setLocation(fileName, line);

    const auto location = locationForBreakpoint(bp.get());

    if (!isSupportedBreakpoint(bp.get())) {
        qCDebug(KDEV_PYTHON_DEBUGGER) << "temporary breakpoint location" << location << "ignored";
        return;
    }

    m_temporaryBreakpoint = BreakpointDataPtr::create(bp.release());
    m_temporaryBreakpoint->breakpointId = m_debuggerBreakpointId++;
    m_temporaryBreakpoint->location = location;

    session()->debugger()->request({QStringLiteral("runtolocation"), location.first, location.second, excludeOthers},
    [this, callback](const ResponseData& d) {
        runToLocationHandler(d, callback);
    });
}

void BreakpointController::runToLocationHandler(const ResponseData& data, PdbDebuggerInstance::CmdCallback callback)
{
    Q_ASSERT(m_temporaryBreakpoint);

    // Handle the program stop.
    callback(data);

    // call addHandler() for the temporary breakpoint to possibly
    // fix-up other pending added/updated breakpoint ids if runToLocation() failed.
    addHandler(data, m_temporaryBreakpoint);

    delete m_temporaryBreakpoint->modelBreakpoint;
    m_temporaryBreakpoint->modelBreakpoint = nullptr;
    m_temporaryBreakpoint.reset();
}
}

#include "moc_breakpointcontroller.cpp"
