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

using namespace KDevelop;

namespace Python {

class DebugSession : public KDevelop::IDebugSession
{

protected:
    virtual KDevelop::IFrameStackModel* createFrameStackModel();

public:
    DebugSession(QStringList program);
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
    
    void lockProcess();
    void unlockProcess();
    bool lockWhenReady(int msecs = 2000);
private:
    KProcess* m_debuggerProcess;
    QMutex m_processLocker;
    IDebugSession::DebuggerState m_state;
    void writeWhenReady(const QByteArray& cmd);
};

}

#endif // DEBUGSESSION_H
