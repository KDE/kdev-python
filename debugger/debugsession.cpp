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


#include <QTimer>
#include <QApplication>
#include <KDebug>

#include <debugger/framestack/framestackmodel.h>

#include "debugsession.h"

using namespace KDevelop;

static QByteArray debuggerPrompt = "\n(Pdb) ";

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
    m_debuggerProcess->setOutputChannelMode(KProcess::SeparateChannels);
    connect(m_debuggerProcess, SIGNAL(readyReadStandardOutput()), this, SLOT(dataAvailable()));
    m_debuggerProcess->start();
    m_debuggerProcess->waitForStarted();
    setState(IDebugSession::ActiveState);
    unlockProcess();
}

void DebugSession::dataAvailable()
{
    kDebug() << "data available";
    lockProcess();
    QByteArray data = m_debuggerProcess->readAllStandardOutput();
    kDebug() << "data arrived:" << data;
    if ( data.endsWith(debuggerPrompt) ) {
        setState(IDebugSession::PausedState);
    }
    unlockProcess();
}

void DebugSession::setState(IDebugSession::DebuggerState state)
{
    m_state = state;
    kDebug() << "debugger state changed to" << state;
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
    writeWhenReady("quit");
    lockProcess();
    if ( ! m_debuggerProcess->waitForFinished(200) ) {
        m_debuggerProcess->kill();
    }
    kDebug() << "killed debugger";
    setState(IDebugSession::EndedState);
    unlockProcess();
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
    return m_state;
}


}

#include "debugsession.moc"
