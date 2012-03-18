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


#include "debugsession.h"
#include <debugger/framestack/framestackmodel.h>
#include <QTimer>
#include <QApplication>

using namespace KDevelop;

namespace Python {

KDevelop::IFrameStackModel* DebugSession::createFrameStackModel()
{
    return 0;
}

DebugSession::DebugSession(QStringList program)
{
    lockProcess();
    m_debuggerProcess = new KProcess(this);
    m_debuggerProcess->setProgram(program);
    m_debuggerProcess->start();
    setState(IDebugSession::ActiveState);
    unlockProcess();
}

void DebugSession::setState(IDebugSession::DebuggerState state)
{
    m_state = state;
}

bool DebugSession::lockWhenReady(int msecs)
{
    QTimer t;
    t.setSingleShot(true);
    t.start(msecs);
    while ( t.isActive() and state() != IDebugSession::PausedState ) {
        QApplication::processEvents();
    }
    if ( state() == IDebugSession::PausedState ) {
        lockProcess();
        return true;
    }
    else {
        return false;
    }
}

void DebugSession::lockProcess()
{
    m_processLocker.lock();
}

void DebugSession::unlockProcess()
{
    m_processLocker.unlock();
}

void DebugSession::writeWhenReady(const QByteArray& cmd)
{
    bool canExecute = lockWhenReady();
    if ( canExecute ) {
        m_debuggerProcess->write(cmd);
    }
    unlockProcess();
}

void DebugSession::stepOut()
{

}

void DebugSession::stepOverInstruction()
{

}

void DebugSession::stepInto()
{

}

void DebugSession::stepIntoInstruction()
{

}

void DebugSession::stepOver()
{
    writeWhenReady("next");
    setState(IDebugSession::ActiveState);
}

void DebugSession::jumpToCursor()
{

}

void DebugSession::runToCursor()
{

}

void DebugSession::run()
{

}

void DebugSession::interruptDebugger()
{

}


void DebugSession::stopDebugger()
{

}

void DebugSession::restartDebugger()
{

}

bool DebugSession::restartAvaliable() const
{
    return false;
}

KDevelop::IDebugSession::DebuggerState DebugSession::state() const
{
    return IDebugSession::NotStartedState;
}


}
