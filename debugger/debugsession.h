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

class DebugSession : public KDevelop::IDebugSession
{
Q_OBJECT
protected:
    virtual KDevelop::IFrameStackModel* createFrameStackModel();

public:
    DebugSession(QStringList program);
    DebugSession();
    void start();
    
    void runDefaultCommand(const QString& cmd);
    void addBreakpoint(Breakpoint* bp);
    void removeBreakpoint(Breakpoint* bp);
    
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
    
    void lockProcess();
    void unlockProcess();
    bool lockWhenReady(int msecs = 2000);
    
    enum WriteFlag {
        NoFlags = 0,
        KeepLocked = 1,
        ClearBuffer = 2
    };
    Q_DECLARE_FLAGS(WriteFlags, WriteFlag);

public slots:
    void dataAvailable();
    void createVariable(Python::Variable* variable, QObject* callback, const char* callbackMethod);

private:
    KProcess* m_debuggerProcess;
    QMutex m_processLocker;
    IDebugSession::DebuggerState m_state;
    QByteArray m_buffer;
    bool m_locationUpdateRequired;
    QStringList m_program;
    
    void writeWhenReady(const QByteArray& cmd, WriteFlags flags = NoFlags);
    void clearOutputBuffer();
    bool waitForState(DebuggerState state_, int msecs = 3000);
};

Q_DECLARE_OPERATORS_FOR_FLAGS(DebugSession::WriteFlags);

}

#endif // DEBUGSESSION_H
