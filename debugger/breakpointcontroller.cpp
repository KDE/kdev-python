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
    QString srclocation = filename + QLatin1Char(':') + QString::number(line + 1);

    if (m_temporaryBreakpoint && m_temporaryBreakpoint->location == srclocation) {
        qCDebug(KDEV_PYTHON_DEBUGGER) << "temporary breakpoint location" << srclocation << "was reached";
        // A call to cleanTemporaryBreakpoint() was ordered after this slot by addHandler().
        // The PDB has by now deleted the temporary breakpoint, so cancel the clear command for it.
        m_temporaryBreakpoint->breakpointId.reset();
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

    if (m_temporaryBreakpoint || !isSupportedBreakpoint(bp)) {
        // updateBreakpoint() inserts the breakpoint once it changes to something valid.
        qCDebug(KDEV_PYTHON_DEBUGGER) << "breakpoint " << bp << "location" << location << "rejected";
        bp->setState(Breakpoint::DirtyState);
        return;
    }

    qCDebug(KDEV_PYTHON_DEBUGGER) << "inserting breakpoint" << bp << location;

    bp->setState(Breakpoint::PendingState);

    // (try) insert the PDB breakpoint.
    brk->breakpointId = m_debuggerBreakpointId++;
    brk->location = location;
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
            brk->modelBreakpoint->setHitCount(0);
            brk->modelBreakpoint->setState(Breakpoint::CleanState);

            if (!brk->modelBreakpoint->enabled()) {
                brk->enabled = false;
                session()->debugger()->request(CMD_DISABLE.arg(brk->breakpointId.value()));
                session()->flushCommands();
            }
        }
        if (m_temporaryBreakpoint == brk) {
            // The runToCursor() can proceed.
            session()->resumeAction(DebugSession::RunAction::RunToCursor);
            // Ensure the temporary breakpoint will be cleaned up if it is never hit.
            session()->debugger()->defer([this](const ResponseData&) {
                cleanTemporaryBreakpoint();
            });
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
    brk->location.clear();
    // Subtract one from all PDB ids greater than invalidId to correct them.
    for (const auto& breakpoint : m_breakpoints) {
        if (breakpoint->breakpointId.value_or(-1) < invalidId) {
            continue;
        }
        qCDebug(KDEV_PYTHON_DEBUGGER) << "fix-up pending id:" << breakpoint->breakpointId.value() << "as"
                                      << breakpoint->breakpointId.value() - 1;
        breakpoint->breakpointId.value()--;
    }

    if (m_temporaryBreakpoint == brk) {
        // Failed to create the temporary breakpoint...
        cleanTemporaryBreakpoint();
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
    brk->location.clear();
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

    if (m_temporaryBreakpoint) {
        // Can't update while the temporary breakpoint exist.
        return;
    }

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
            session()->debugger()->request(CMD_ENABLE.arg(brk->breakpointId.value()));
        } else {
            qCDebug(KDEV_PYTHON_DEBUGGER) << "disabling breakpoint" << brk->modelBreakpoint;
            session()->debugger()->request(CMD_DISABLE.arg(brk->breakpointId.value()));
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
        brk->location = location;
        session()->debugger()->request(CMD_BREAK.arg(location), [this, brk](const ResponseData& d) {
            addHandler(d, brk);
        });
        flush = true;
    }
    if (flush) {
        session()->flushCommands();
    }
}

void BreakpointController::runToLocation(const QUrl& fileName, int line)
{
    // Create a free-standing breakpoint detached from the model.
    auto bp = std::make_unique<KDevelop::Breakpoint>(nullptr, Breakpoint::CodeBreakpoint);
    bp->setLocation(fileName, line);

    const QString location = locationForBreakpoint(bp.get());

    if (!isSupportedBreakpoint(bp.get())) {
        qCDebug(KDEV_PYTHON_DEBUGGER) << "temporary breakpoint location" << location << "ignored";
        return;
    }

    m_temporaryBreakpoint = BreakpointDataPtr::create(bp.release());
    m_temporaryBreakpoint->breakpointId = m_debuggerBreakpointId++;
    m_temporaryBreakpoint->location = location;

    session()->debugger()->request(QStringLiteral("tbreak %1").arg(location), [this](const ResponseData& d) {
        // The disable loop uses the BreakpointData state, so it cannot run before this point.
        for (const auto& breakpoint : m_breakpoints) {
            if (breakpoint->breakpointId && breakpoint->enabled) {
                session()->debugger()->request(CMD_DISABLE.arg(breakpoint->breakpointId.value()));
            }
        }
        addHandler(d, m_temporaryBreakpoint);
    });
    // No flushCommands() since this function is only invoked from DebugSession::runToCursor()
}

void BreakpointController::cleanTemporaryBreakpoint()
{
    if (!m_temporaryBreakpoint) {
        return;
    }

    delete m_temporaryBreakpoint->modelBreakpoint;
    m_temporaryBreakpoint->modelBreakpoint = nullptr;
    // Note: we are being invoked from three possible scenarios:
    // - The temporary breakpoint was hit, and thus m_temporaryBreakpoint->breakpointId was reset.
    // - 'tbreak' command failed, and thus m_temporaryBreakpoint->breakpointId was reset.
    // - The m_temporaryBreakpoint->breakpointId is still valid, and thus has to be cleared.
    removeHandler(m_temporaryBreakpoint);
    m_temporaryBreakpoint.reset();

    // Sync-up with the model again.
    // We have ignored all updates since the temporary breakpoint was installed,
    // so some PDB breakpoints can be missing or their enabled state doesn't match the model state.
    for (const auto& breakpoint : m_breakpoints) {
        if (!breakpoint->modelBreakpoint) {
            continue;
        }
        const QString location = locationForBreakpoint(breakpoint->modelBreakpoint);
        if (breakpoint->breakpointId && location == breakpoint->location) {
            // Location is still up-to-date...
            breakpoint->enabled = breakpoint->modelBreakpoint->enabled();
            if (breakpoint->enabled) {
                session()->debugger()->request(CMD_ENABLE.arg(breakpoint->breakpointId.value()));
            }
            continue;
        }
        // Do a full update.
        // This might be an newly created model breakpoint, or one with a rejected location, we don't know.
        updateBreakpoint(breakpoint->modelBreakpoint);
    }
}
}

#include "moc_breakpointcontroller.cpp"
