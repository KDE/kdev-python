/*
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>
    SPDX-FileCopyrightText: 2024 Jarmo Tiitto <jarmo.tiitto@gmail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef BREAKPOINTCONTROLLER_H
#define BREAKPOINTCONTROLLER_H

#include <QSharedPointer>
#include <QString>

#include <debugger/interfaces/ibreakpointcontroller.h>
#include "debugsession.h"
#include "pdbdebuggerinstance.h"

#include <optional>
#include <utility>
#include <vector>

using namespace KDevelop;

namespace Python {

struct BreakpointData
{
    /// PDB breakpoint id. No value, if no breakpoint is inserted in PDB.
    std::optional<int> breakpointId;
    /// The model breakpoint associated with the PDB breakpoint.
    KDevelop::Breakpoint* modelBreakpoint = nullptr;
    std::pair<QString, int> location;
    bool enabled = true;

    Q_DISABLE_COPY_MOVE(BreakpointData)

    BreakpointData(KDevelop::Breakpoint* bp)
        : modelBreakpoint(bp)
    {
    }
};

using BreakpointDataPtr = QSharedPointer<BreakpointData>;

class BreakpointController : public KDevelop::IBreakpointController
{
Q_OBJECT
public:
    BreakpointController(IDebugSession* parent);

    void breakpointAdded(int row) override;

    void breakpointModelChanged(int row, BreakpointModel::ColumnFlags columns) override;

    void breakpointAboutToBeDeleted(int row) override;

    /**
     * Note: this method exists to ease the API transition; it should be removed at once
     *       when this method is no longer called by KDevelop. We don't want KDevelop's
     *       debuggerStateChanged() default implementation to override the breakpoint states that
     *       we have setup.
     **/
    void debuggerStateChanged(IDebugSession::DebuggerState state) override
    {
        Q_UNUSED(state);
    }

    /**
     * Create a temporary breakpoint, disable all other breakpoints if @p excludeOthers is true and run
     * the program if the breakpoint creation succeeded. The temporary breakpoint is automatically
     * cleaned up.
     */
    void runToLocation(const QUrl& fileName, int line, PdbDebuggerInstance::CmdCallback callback, bool excludeOthers);

public Q_SLOTS:
    /**
     * @brief Handles events in the debug session.
     * It is used here to send breakpoints to the debugger which were created by the user
     * before the program was started.
     * 
     * @param evt passed by kdevplatform, specifies the type of the event.
     **/
    void slotEvent(IDebugSession::event_t evt);

    /**
     * Report a location at where the program has stopped.
     */
    void programStopped(const Python::ResponseData& data);

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

private:
    /// Registered model breakpoints, unordered.
    std::vector<BreakpointDataPtr> m_breakpoints;
    /*
     * What PDB breakpoint Id would be created next. PDB breakpoint ids start from 1 and are never
     * reused in the same session. Must be incremented *before* queuing a CMD_BREAK.
     */
    int m_debuggerBreakpointId = 1;

    BreakpointDataPtr m_temporaryBreakpoint;

    static inline const auto CMD_BREAK = QStringLiteral("break");
    static inline const auto CMD_CLEAR = QStringLiteral("clear");
    static inline const auto CMD_ENABLE = QStringLiteral("enable");
    static inline const auto CMD_DISABLE = QStringLiteral("disable");

    static bool isSupportedBreakpoint(Breakpoint* bp);
    static std::pair<QString, int> locationForBreakpoint(Breakpoint* bp);

    /**
     * Find the BreakpointData for a model breakpoint.
     */
    std::vector<BreakpointDataPtr>::iterator lookupBreakpointData(Breakpoint* bp);

    /**
     * Add a given model breakpoint to the debugger.
     * @param bp The breakpoint to add
     **/
    void addBreakpoint(Breakpoint* bp);
    void addHandler(const ResponseData& data, const BreakpointDataPtr& brk);

    /**
     * Queue commands to remove a given model breakpoint from the debugger.
     * @param bp The breakpoint to remove
     **/
    void removeBreakpoint(Breakpoint* bp);

    /**
     * Queue a PDB clear command if possible.
     * @return true if flushCommands() is required afterwards.
     */
    bool removeHandler(const BreakpointDataPtr& brk);

    /**
     * Queue commands to update a given model breakpoint in the debugger.
     * @param bp The breakpoint to update
     **/
    void updateBreakpoint(Breakpoint* bp);
    void updateHandler(const BreakpointDataPtr& brk, std::pair<QString, int> location);

    void runToLocationHandler(const ResponseData& data, PdbDebuggerInstance::CmdCallback callback);
};

}

#endif // BREAKPOINTCONTROLLER_H
