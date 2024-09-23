/*
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef PDBDEBUGSESSION_H
#define PDBDEBUGSESSION_H

#include <QTimer>
#include <QDebug>
#include "debuggerdebug.h"

#include <debugger/interfaces/idebugsession.h>
#include <debugger/interfaces/ivariablecontroller.h>
#include <debugger/interfaces/ibreakpointcontroller.h>
#include "pdbdebuggerinstance.h"
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
     * @brief Get the PdbDebuggerInstance i.e. the debugger.
     */
    PdbDebuggerInstance* debugger() const;

    /**
     * flushCommands() interrupts the debugger, so any requests queued up to this point can be processed
     * immediately, after which the interrupted user action is re-issued.
     */
    void flushCommands();

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
     * @brief Kill the debugger process synchronously.
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

    enum class RunAction {
        None,
        Unspecified,
        StepOut,
        StepOverInstruction,
        StepInto,
        StepIntoInstruction,
        StepOver,
        JumpToCursor,
        RunToCursor,
        Run
    };
    /**
     * Resume execution of the inferior's code.
     */
    void resumeAction(RunAction action);

public Q_SLOTS:
    void debuggerInit();

    /**
     * @brief Emitted when new data has been received from the debugger process (via stdout)
     **/
    void stdoutData(QByteArray data);
    void stderrData(QByteArray data);

    /**
     * @brief Emitted once each time the debugger has started running commands.
     */
    void debuggerBusy();

    /**
     * @brief Emitted once each time when the debugger has run out of commands to process.
     */
    void inferiorSuspended();

    /**
     * @brief Called once when the debugger process has exited.
     */
    void finalizeState();

    /**
     * Straight up kill the debugger process.
     */
    void killDebugger();

Q_SIGNALS:
    /// Emitted when real data from the program is received
    void realDataReceived(QStringList);
    void stderrReceived(QStringList);

    /// Emitted when the program has stopped. (for any reason)
    void programStopped(QString filename, int line);

private:
    IBreakpointController* m_breakpointController;
    IVariableController* m_variableController;
    IFrameStackModel* m_frameStackModel;
    DebuggerState m_state = DebuggerState::NotStartedState;
    PdbDebuggerInstance* m_debugger = nullptr;
    QTimer m_killTimer;
    bool m_sessionStarted = false;
    const PdbDebuggerInstance::CmdCallback m_resumingFinished;
    /// Must be set before running a command that would resume running the inferior's code.
    RunAction m_resumingRequest = RunAction::None;
    bool m_flushInProgress = false;
    int m_flushSeqNro = -1;
    QUrl m_runToUrl;
    int m_runToLine = -1;

    /**
     * @brief Handler for debugger requests, which continued to execute inferior's code.
     **/
    void resumingFinished(const ResponseData& data);
};

}

#endif // DEBUGSESSION_H
