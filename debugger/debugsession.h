/*
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef PDBDEBUGSESSION_H
#define PDBDEBUGSESSION_H

#include <QDebug>
#include "debuggerdebug.h"

#include <debugger/interfaces/idebugsession.h>
#include <debugger/interfaces/ivariablecontroller.h>
#include <debugger/interfaces/ibreakpointcontroller.h>
#include "variable.h"

using namespace KDevelop;

namespace Python {

struct StartupInfo;

class DebugSession : public KDevelop::IDebugSession
{
    Q_OBJECT
public:
    DebugSession();
    ~DebugSession() override;

    IBreakpointController* breakpointController() const override;
    IFrameStackModel* frameStackModel() const override;

    /**
     * @brief Start the debugger.
     **/
    void start(const StartupInfo& info);

    /**
     * @brief Access this session's variable controller
     **/
    IVariableController* variableController() const override;
    
    /// Those functions just execute the basic debugger commands. They're used when the user
    /// clicks the appropriate button.
    void stepOut() override;
    void stepOverInstruction() override;
    void stepInto() override;
    void stepIntoInstruction() override;
    void stepOver() override;
    void jumpToCursor() override;
    void runToCursor() override;
    void run() override;
    void restartDebugger() override;
    
    bool restartAvaliable() const override;
    
    /**
     * @brief Interrupt the running program with SIGINT and set the state to PausedState
     **/
    void interruptDebugger() override;
    
    /**
     * @brief Kill the debugger and program being debugged.
     * This tries to send a "quit" command, and if the debugger doesn't react to that quickly,
     * it'll just kill it.
     **/
    void stopDebugger() override;

    /**
     * @brief Kill the debugger process synchronously
     **/
    void killDebuggerNow() override;
    
    /**
     * @brief Gives the debugger state.
     * The two main states are "ActiveState" and "PausedState"; the former is given
     * if the *user program* is being run by the debugger.
     * 
     * @return :IDebugSession::DebuggerState the current state the debugger is in
     **/
    IDebugSession::DebuggerState state() const override;
    
    /**
     */
    void updateLocation();
    
public Q_SLOTS:
    /**
     * @brief Emitted when new data has been received from the debugger process (via stdout)
     **/
    void stdoutData(QByteArray data);
    void stderrData(QByteArray data);
    
    /**
     * @brief Emitted once when the debugger process has exited.
     * @todo
     */
    void finalizeState();

Q_SIGNALS:
    /// Emitted when real data from the program is received
    void realDataReceived(QStringList);
    void stderrReceived(QStringList);

private:
    IBreakpointController* m_breakpointController;
    IVariableController* m_variableController;
    IFrameStackModel* m_frameStackModel;
    DebuggerState m_state = DebuggerState::NotStartedState;
    
    /**
     * @brief Performs a location update.
     * This is used by updateLocation().
     **/
    void locationUpdateReady(QByteArray data);
};

}

#endif // DEBUGSESSION_H
