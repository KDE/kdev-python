/*
    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) 2012  <copyright holder> <email>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/


#ifndef PDBDEBUGSESSION_H
#define PDBDEBUGSESSION_H

#include <KProcess>
#include <QMutexLocker>

#include <debugger/interfaces/idebugsession.h>
#include <debugger/interfaces/ivariablecontroller.h>
#include <debugger/interfaces/ibreakpointcontroller.h>
#include "variable.h"

using namespace KDevelop;

namespace Python {

class PdbCommand;
    
class DebugSession : public KDevelop::IDebugSession
{
Q_OBJECT
protected:
    virtual KDevelop::IFrameStackModel* createFrameStackModel();

public:
    DebugSession(QStringList program);
    DebugSession();
    void start();
    
    void addCommand(PdbCommand* cmd);
    void addSimpleUserCommand(const QString& cmd);
    void addSimpleInternalCommand(const QString& cmd);
    void addBreakpoint(Breakpoint* bp);
    void removeBreakpoint(Breakpoint* bp);
    QByteArray getFrameList();
    
    virtual IVariableController* variableController();
    
    virtual void stepOut();
    virtual void stepOverInstruction();
    virtual void stepInto();
    virtual void stepIntoInstruction();
    virtual void stepOver();
    virtual void jumpToCursor();
    virtual void runToCursor();
    virtual void run();
    virtual void interruptDebugger();
    virtual void stopDebugger();
    virtual void restartDebugger();
    virtual bool restartAvaliable() const;
    virtual IDebugSession::DebuggerState state() const;
    void setState(IDebugSession::DebuggerState state);
    void updateLocation();
    void setLocationChanged();
    
    enum WriteFlag {
        NoFlags = 0,
        KeepLocked = 1,
        ClearBuffer = 2
    };
    Q_DECLARE_FLAGS(WriteFlags, WriteFlag);
    
    void lockProcess();
    void unlockProcess();
    bool lockWhenReady(int msecs = 2000);
    void write(const QByteArray& cmd);

public slots:
    void dataAvailable();
    void createVariable(Python::Variable* variable, QObject* callback, const char* callbackMethod);
    void checkCommandQueue();
    void locationUpdateReady(QByteArray data);

private slots:
    void createVariableInternal(QByteArray data);

signals:
    void debuggerReady();
    void commandAdded();

private:
    KProcess* m_debuggerProcess;
    QMutex m_processLocker;
    IDebugSession::DebuggerState m_state;
    QByteArray m_buffer;
    bool m_locationUpdateRequired;
    QStringList m_program;
    QList<PdbCommand*> m_commandQueue;
    QObject* m_nextNotifyObject;
    QObject* m_nextNotifyVarObject;
    const char* m_nextNotifyMethod;
    const char* m_nextNotifyVarMethod;
    Variable* m_nextUpdateVar;
    bool m_processBusy;
    
    void setNotifyNext(QObject* object, const char* method);
    void notifyNext();
    void processNextCommand();
    void clearOutputBuffer();
    bool waitForState(DebuggerState state_, int msecs = 3000);
};

Q_DECLARE_OPERATORS_FOR_FLAGS(DebugSession::WriteFlags);

struct PdbCommand {
public:
    // notifyMethod must have a QByteArray argument, which is the 
    // output produced by the command.
    PdbCommand(QObject* notifyObject, const char* notifyMethod) :
      m_notifyObject(notifyObject)
    , m_notifyMethod(notifyMethod)
    , m_output(QByteArray()) {};
    
    // process is already locked and ready when this is called.
    // Don't acquire or release the lock here.
    virtual void run(DebugSession* session) = 0;
    virtual ~PdbCommand() {};
    void setOutput(QByteArray output) {
        m_output = output;
    };
    QObject* notifyObject() {
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
    
    inline Type type() {
        return m_type;
    };

protected:
    Type m_type;
    QObject* m_notifyObject;
    const char* m_notifyMethod;
    QByteArray m_output;
};

struct SimplePdbCommand : public PdbCommand {
public:
    SimplePdbCommand(QObject* notifyObject, const char* notifyMethod, const QString& command) :
      PdbCommand(notifyObject, notifyMethod)
    , m_command(command) {
        m_type = InvalidType;
    };
    void run(DebugSession* session) {
        Q_ASSERT(m_command.endsWith('\n'));
        kDebug() << "running command:" << m_command.toAscii() << m_notifyMethod;
        session->write(m_command.toAscii());
    }
private:
    QString m_command;
};

struct InternalPdbCommand : public SimplePdbCommand {
public:
    InternalPdbCommand(QObject* notifyObject, const char* notifyMethod, const QString& command) :
      SimplePdbCommand(notifyObject, notifyMethod, command) {
        m_type = InternalType;
    } ;
};

struct UserPdbCommand : public SimplePdbCommand {
public:
    UserPdbCommand(QObject* notifyObject, const char* notifyMethod, const QString& command) :
      SimplePdbCommand(notifyObject, notifyMethod, command) {
          m_type = UserType;
    } ;
};

}

#endif // DEBUGSESSION_H
