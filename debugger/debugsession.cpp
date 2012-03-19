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
#include "pdbframestackmodel.h"
#include "variablecontroller.h"

using namespace KDevelop;

static QByteArray debuggerPrompt = "(Pdb) ";

namespace Python {

KDevelop::IFrameStackModel* DebugSession::createFrameStackModel()
{
    return new PdbFrameStackModel(this);
}

DebugSession::DebugSession(QStringList program) :
    IDebugSession(),
    m_locationUpdateRequired(true)
{
    m_program = program;
    m_variableController = new VariableController(this);
}

IVariableController* DebugSession::variableController()
{
    return m_variableController;
}

void DebugSession::start()
{
    setState(StartingState);
    lockProcess();
    m_debuggerProcess = new KProcess(this);
    m_debuggerProcess->setProgram(m_program);
    m_debuggerProcess->setOutputChannelMode(KProcess::SeparateChannels);
    m_debuggerProcess->blockSignals(true);
    connect(m_debuggerProcess, SIGNAL(readyReadStandardOutput()), this, SLOT(dataAvailable()));
    m_debuggerProcess->start();
    m_debuggerProcess->waitForStarted();
    setState(ActiveState);
    m_debuggerProcess->blockSignals(false);
    unlockProcess();
}

void DebugSession::dataAvailable()
{
    kDebug() << "data available";
    QByteArray data = m_debuggerProcess->readAllStandardOutput();
    kDebug() << "data arrived:" << data;
    m_buffer.append(data);
    // Although unbuffered, it seems guaranteed that the debugger prompt is written at once.
    // I don't think a python statement like print "FooBar" will ever break the output into two parts.
    // TODO find explicit documentation for this somewhere.
    if ( data.endsWith(debuggerPrompt) ) {
        setState(PausedState);
    }
}

void DebugSession::setState(DebuggerState state)
{
    m_state = state;
    emit stateChanged(m_state);
    raiseEvent(program_state_changed);
    if ( m_state == EndedState ) {
        raiseEvent(debugger_exited);
        emit finished();
    }
    else if ( m_state == ActiveState || m_state == StartingState || m_state == StoppingState ) {
        raiseEvent(debugger_busy);
    }
    else if ( m_state == PausedState ) {
        if ( m_locationUpdateRequired ) {
            m_locationUpdateRequired = false;
            updateLocation();
        }
        raiseEvent(debugger_ready);
    }
    kDebug() << "debugger state changed to" << m_state;
}

bool DebugSession::waitForState(IDebugSession::DebuggerState state_, int msecs)
{
    QTimer t;
    t.setSingleShot(true);
    t.start(msecs);
    while ( t.isActive() and state() != state_ ) {
        QApplication::processEvents();
    }
    if ( state() == state_ ) {
        return true;
    }
    else {
        return false;
    }
}

bool DebugSession::lockWhenReady(int msecs)
{
    bool result = waitForState(PausedState, msecs);
    if ( result ) {
        lockProcess();
    }
    return result;
}

void DebugSession::lockProcess()
{
    m_processLocker.lock();
}

void DebugSession::unlockProcess()
{
    m_processLocker.unlock();
}

void DebugSession::writeWhenReady(const QByteArray& cmd, Python::DebugSession::WriteFlags flags)
{
    bool canExecute = lockWhenReady();
    if ( flags & ClearBuffer ) {
        m_buffer.clear();
    }
    if ( canExecute ) {
        m_debuggerProcess->write(cmd);
    }
    if ( ! flags & KeepLocked ) {
        unlockProcess();
    }
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
    writeWhenReady("next\n", KeepLocked);
    setState(IDebugSession::ActiveState);
    m_locationUpdateRequired = true;
    unlockProcess();
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

void DebugSession::clearOutputBuffer()
{
    m_buffer.clear();
}

void DebugSession::updateLocation()
{
    kDebug() << "updating location";
    writeWhenReady("where\n", KeepLocked | ClearBuffer);
    setState(ActiveState);
    waitForState(PausedState, 1000);
    kDebug() << "Got where information: " << m_buffer;
    QList<QByteArray> lines = m_buffer.split('\n');
    if ( lines.length() >= 3 ) {
        lines.removeLast(); // prompt
        lines.removeLast(); // source line
        QString where = lines.last();
        // > /bar/baz/foo.py(123)<module>()
        QRegExp m("^> (/.*\\.py)\\((\\d*)\\).*$");
        m.setMinimal(true);
        m.exactMatch(where);
        setCurrentPosition(KUrl(m.capturedTexts().at(1)), m.capturedTexts().at(2).toInt(), "<unknown>");
        kDebug() << "New position: " << m.capturedTexts().at(1) << m.capturedTexts().at(2).toInt() << m.capturedTexts() << where;
    }
    unlockProcess();
}

void DebugSession::stopDebugger()
{
    writeWhenReady("quit\n");
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
