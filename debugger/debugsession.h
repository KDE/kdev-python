/*
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef PDBDEBUGSESSION_H
#define PDBDEBUGSESSION_H

#include <KProcess>
#include <QMutexLocker>
#include <QPointer>

#include <QDebug>
#include "debuggerdebug.h"

#include <debugger/interfaces/idebugsession.h>
#include <debugger/interfaces/ivariablecontroller.h>
#include <debugger/interfaces/ibreakpointcontroller.h>
#include "variable.h"

using namespace KDevelop;

namespace Python {

struct PdbCommand;
    
class DebugSession : public KDevelop::IDebugSession
{
    Q_OBJECT
public:
    DebugSession(QStringList program, const QUrl& workingDirectory,
                 const QString& envProfileName);
    ~DebugSession() override;

    IBreakpointController* breakpointController() const override;
    IFrameStackModel* frameStackModel() const override;

    /**
     * @brief Start the debugger.
     **/
    void start();
    
    /**
     * @brief Adds a command to the queue.
     * Commands are processed in the same order they're added.
     * If the type of the command added is UserType, automatic updates
     * (of local variables, location, ...) will be triggered.
     *
     * @param cmd The command to enqeue.
     **/
    void addCommand(PdbCommand* cmd);
    
    /**
     * @brief Convenience function, constructs a new UserPdbCommand and enqueues it.
     * Use this to enqueue simple commands invoked by user clicks ("next" etc.)
     *
     * @param cmd What you would type at the debugger command line.
     **/
    void addSimpleUserCommand(const QString& cmd);
    
    /**
     * @brief Convencience function, constructs a new InternalPdbCommand and enqueues it.
     * Use this to enqueue simple commands which are needed internally ("where", ...)
     *
     * @param cmd What you would type at the debugger command line.
     **/
    void addSimpleInternalCommand(const QString& cmd);
    
    /**
     * @brief Interrupt the running program with SIGINT and immediately run the specified command.
     * This will also trigger a location update. Program execution will continue immediately after
     * the given command has been run!
     *
     * @param cmd What you would type at the debugger command line, terminated by \n.
     **/
    void runImmediately(const QString& cmd);
    
    /**
     * @brief Constructs commands to add the given breakpoint to the debugger.
     *
     * @param bp The breakpoint to add
     **/
    void addBreakpoint(Breakpoint* bp);
    
    /**
     * @brief Constructs commands to remove the given breakpoint from the debugger.
     *
     * @param bp The breakpoint to remove
     **/
    void removeBreakpoint(Breakpoint* bp);
    
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
     * @brief Change the debugger state, and trigger various events depending on the previous and new state.
     * WARNING: Do *not* switch to ActiveState for running internal commands: If
     * the location is being updated by "where", no state switching should occur.
     * Otherwise, various endless loops might occur because kdevplatform tries auto-
     * update various things (like the location, ...)
     * State changes should only occur when starting up, shutting down, or on explicit user interaction.
     * 
     * @param state The state to change to.
     **/
    void setState(IDebugSession::DebuggerState state);
    
    /**
     * @brief Enqueue a command which updates the location.
     * Run this whenever you enqueue a command which might change the location in the source code
     * (like "next" or similar). This is queued, so you can do addSimpleUserCommand("next"); updateLocation();
     * without problems.
     **/
    void updateLocation();
    
    /**
     * @brief Clears the table of object IDs stored in the debugger script
     **/
    void clearObjectTable();
    
    /**
     * @brief Write raw data to the debugger process' stdin.
     * Remember that you have to terminate your input by "\n" for the debugger to process it.
     * 
     * @param cmd data to write to stdin
     **/
    void write(const QByteArray& cmd);

public Q_SLOTS:
    /**
     * @brief Emitted when new data has been received from the debugger process (via stdout)
     **/
    void dataAvailable();
    /**
     * @brief Fetch the given variable's value and assign it, and when done call the given callback method.
     *
     * @param variable Variable object to fetch data for
     * @param callback object to call callbackMethod on
     * @param callbackMethod method to call when done
     **/
    void createVariable(Python::Variable* variable, QObject* callback, const char* callbackMethod);
    
    /**
     * @brief Check the command queue, and run the next command if it's not empty.
     **/
    void checkCommandQueue();
    
    /**
     * @brief Performs a location update.
     * This is used by updateLocation().
     **/
    void locationUpdateReady(QByteArray data);
    void debuggerQuit(int);

Q_SIGNALS:
    /// Emitted when the debugger becomes ready to process a new command, i.e. shows its prompt
    void debuggerReady();
    /// Emitted when a new command is added to the queue
    void commandAdded();
    /// Emitted when real data from the program is received (needs improvement)
    void realDataReceived(QStringList);
    void stderrReceived(QStringList);

private:
    IBreakpointController* m_breakpointController;
    IVariableController* m_variableController;
    IFrameStackModel* m_frameStackModel;
    KProcess* m_debuggerProcess;
    IDebugSession::DebuggerState m_state;
    QByteArray m_buffer;
    QStringList m_program;
    QList<PdbCommand*> m_commandQueue;
    const QUrl& m_workingDirectory;
    const QString m_envProfileName;
private:
    /// objects to notify next
    QPointer<QObject> m_nextNotifyObject;
    const char* m_nextNotifyMethod;
    /// whether the process is busy processing an internal command
    bool m_processBusy;
    
    /**
     * @brief Set the object to notify when the next command is done processing
     **/
    void setNotifyNext(QPointer<QObject> object, const char* method);
    
    /**
     * @brief Invoke the method given by setNotifyNext, and clear it
     **/
    void notifyNext();
    
    /**
     * @brief Process the next command in the queue.
     * WARNING: The queue must be non-empty when this is called.
     * If the process is busy doing something else, returns and does nothing.
     **/
    void processNextCommand();
    
    /**
     * @brief Clear the data accumulated in m_buffer.
     **/
    void clearOutputBuffer();

    /**
     * @brief Clean up and switch to EndedState after stopping/killing the debugger
     **/
    void finalizeState();
    
    /// stores whether the data currently received comes from the debugger
    /// or the debuggee.
    int m_inDebuggerData;
};

/**
 * @brief Base class for all Pdb command objects. Those are enqueued in the debug session.
 **/
struct PdbCommand {
public:
    /// notifyMethod must have a QByteArray argument, which is the 
    /// output produced by the command.
    PdbCommand(QObject* notifyObject, const char* notifyMethod) :
      m_notifyObject(notifyObject)
    , m_notifyMethod(notifyMethod)
    , m_output(QByteArray()) {};
    
    /**
     * @brief Implement this method in your sub-class to execute the command in the given session.
     * WARNING: The process is already locked and ready when this is called.
     * Don't acquire or release any locks or do fancy checking here, just do your business (write data
     * to the process, ...). Everything else is handled from outside.
     * @param session the debug session to run the command in
     **/
    virtual void run(DebugSession* session) = 0;
    virtual ~PdbCommand() {};
    void setOutput(QByteArray output) {
        m_output = output;
    };
    QPointer<QObject> notifyObject() {
        return m_notifyObject;
    };
    const char* notifyMethod() {
        return m_notifyMethod;
    };
    
    enum Type {
        InvalidType,
        InternalType,
        UserType
    };
    
    inline Type type() const {
        return m_type;
    };

protected:
    Type m_type;
    QPointer<QObject> m_notifyObject;
    const char* m_notifyMethod;
    QByteArray m_output;
};

/**
 * @brief Base-class for commands which just write a simple piece of text to the debugger command line and read its output.
 **/
struct SimplePdbCommand : public PdbCommand {
public:
    SimplePdbCommand(QObject* notifyObject, const char* notifyMethod, const QString& command) :
      PdbCommand(notifyObject, notifyMethod)
    , m_command(command) {
        m_type = InvalidType;
    };
    void run(DebugSession* session) override {
        Q_ASSERT(m_command.endsWith(QLatin1Char('\n')) && "command must end with a newline");
        qCDebug(KDEV_PYTHON_DEBUGGER) << "running command:" << m_command<< m_notifyMethod;
        session->write(m_command.toUtf8());
    }
private:
    QString m_command;
};

/**
 * @brief Represents a command which is invoked by kdevelop to obtain information to display in the UI.
 **/
struct InternalPdbCommand : public SimplePdbCommand {
public:
    InternalPdbCommand(QObject* notifyObject, const char* notifyMethod, const QString& command) :
      SimplePdbCommand(notifyObject, notifyMethod, command) {
        m_type = InternalType;
    } ;
};

/**
 * @brief Represents a command which is invoked by the user by clicking a button.
 **/
struct UserPdbCommand : public SimplePdbCommand {
public:
    UserPdbCommand(QObject* notifyObject, const char* notifyMethod, const QString& command) :
      SimplePdbCommand(notifyObject, notifyMethod, command) {
          m_type = UserType;
    } ;
};

}

#endif // DEBUGSESSION_H
