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
#include <interfaces/icore.h>
#include <interfaces/idocumentcontroller.h>

#include "debugsession.h"
#include "pdbframestackmodel.h"
#include "variablecontroller.h"
#include "variable.h"
#include "breakpointcontroller.h"

using namespace KDevelop;

static QByteArray debuggerPrompt = "(Pdb) ";

namespace Python {

KDevelop::IFrameStackModel* DebugSession::createFrameStackModel()
{
    return new PdbFrameStackModel(this);
}

DebugSession::DebugSession() :
      m_nextNotifyObject(0)
    , m_nextNotifyMethod(0)
{
    m_variableController = new Python::VariableController(this);
    m_breakpointController = new Python::BreakpointController(this);
}

DebugSession::DebugSession(QStringList program) :
    IDebugSession()
    , m_nextNotifyObject(0)
    , m_nextNotifyMethod(0)
{
    kDebug() << "creating debug session";
    m_variableController = new Python::VariableController(this);
    m_breakpointController = new Python::BreakpointController(this);
    m_program = program;
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
    m_debuggerProcess = new KProcess(this);
    m_debuggerProcess->setProgram(m_program);
    m_debuggerProcess->setOutputChannelMode(KProcess::SeparateChannels);
    m_debuggerProcess->blockSignals(true);
    connect(m_debuggerProcess, SIGNAL(readyReadStandardOutput()), this, SLOT(dataAvailable()));
    connect(this, SIGNAL(debuggerReady()), SLOT(checkCommandQueue()));
    connect(this, SIGNAL(commandAdded()), SLOT(checkCommandQueue()));
    m_debuggerProcess->start();
    m_debuggerProcess->waitForStarted();
    m_debuggerProcess->blockSignals(false);
    updateLocation();
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
        if ( state() == StartingState ) {
            setState(PausedState);
            raiseEvent(connected_to_program);
        }
        else {
            notifyNext();
            if ( m_commandQueue.isEmpty() ) {
                kDebug() << "Changing state to PausedState";
                setState(PausedState);
            }
        }
        m_processBusy = false;
        emit debuggerReady();
    }
}

void DebugSession::setNotifyNext(QObject* object, const char* method)
{
    m_nextNotifyObject = object;
    m_nextNotifyMethod = method;
}

void DebugSession::notifyNext()
{
    if ( m_nextNotifyMethod and m_nextNotifyObject ) {
        kDebug() << "Calling:" << m_nextNotifyMethod << m_nextNotifyObject;
        QMetaObject::invokeMethod(m_nextNotifyObject, m_nextNotifyMethod, Qt::DirectConnection, Q_ARG(QByteArray, m_buffer));
    }
    else {
        kWarning() << "notify called, but nothing to notify!";
    }
    m_buffer.clear();
    m_nextNotifyMethod = 0;
    m_nextNotifyObject = 0;
}

void DebugSession::processNextCommand()
{
    kDebug() << "processing next debugger command in queue";
    if ( m_processBusy or m_state == EndedState ) {
        kDebug() << "process is busy or ended, aborting";
        return;
    }
    m_processBusy = true;
    PdbCommand* cmd = m_commandQueue.first();
    Q_ASSERT(cmd->type() != PdbCommand::InvalidType);
    if ( cmd->type() == PdbCommand::UserType ) {
        setState(ActiveState);
    }
    m_commandQueue.removeFirst();
    setNotifyNext(cmd->notifyObject(), cmd->notifyMethod());
    cmd->run(this);
    kDebug() << "command executed, deleting it.";
    delete cmd;
    if ( ! m_commandQueue.isEmpty() ) {
        processNextCommand();
    }
}

void DebugSession::setState(DebuggerState state)
{
    kDebug() << "Setting state to" << state;
    
    if ( state == m_state ) {
        return;
    }
    m_state = state;
    if ( m_state == EndedState ) {
        raiseEvent(debugger_exited);
        emit finished();
    }
    else if ( m_state == ActiveState || m_state == StartingState || m_state == StoppingState ) {
        raiseEvent(debugger_busy);
    }
    else if ( m_state == PausedState ) {
        raiseEvent(debugger_ready);
        if ( currentUrl().isValid() ) {
            emit showStepInSource(currentUrl(), currentLine(), currentAddr());
        }
    }
    
    kDebug() << "debugger state changed to" << m_state;
    raiseEvent(program_state_changed);
    emit stateChanged(m_state);
}

bool DebugSession::waitForState(IDebugSession::DebuggerState state_, int msecs)
{
    QTimer t;
    t.setSingleShot(true);
    t.start(msecs);
    while ( t.isActive() and state() != state_ ) {
        QApplication::processEvents();
    }
    kDebug() << "state" << state_ << "reached:" << ( state_ == state() );
    return state() == state_;
}

bool DebugSession::lockWhenReady(int msecs)
{
    bool result = waitForState(PausedState, msecs);
    if ( result ) {
        setState(ActiveState);
    }
    return result;
}

void DebugSession::write(const QByteArray& cmd)
{
    kDebug() << " >>> WRITE:" << cmd;
    m_debuggerProcess->write(cmd);
}

void DebugSession::stepOut()
{
    // TODO this only steps out of functions; use temporary breakpoints for loops maybe?
    addSimpleUserCommand("return");
}

void DebugSession::stepOverInstruction()
{
    addSimpleUserCommand("next");
}

void DebugSession::stepInto()
{
    addSimpleUserCommand("step");
}

void DebugSession::stepIntoInstruction()
{
    addSimpleUserCommand("step");
}

void DebugSession::stepOver()
{
    addSimpleUserCommand("next");
}

void DebugSession::jumpToCursor()
{
    if (KDevelop::IDocument* doc = KDevelop::ICore::self()->documentController()->activeDocument()) {
        KTextEditor::Cursor cursor = doc->cursorPosition();
        if ( cursor.isValid() ) {
            // TODO disable all other breakpoints
            addSimpleUserCommand(QString("jump " + QString::number(cursor.line() + 1)).toAscii());
        }
    }
}

void DebugSession::runToCursor()
{
    if (KDevelop::IDocument* doc = KDevelop::ICore::self()->documentController()->activeDocument()) {
        KTextEditor::Cursor cursor = doc->cursorPosition();
        if ( cursor.isValid() ) {
            // TODO disable all other breakpoints
            QString temporaryBreakpointLocation = doc->url().path() + QString(":") + QString::number(cursor.line() + 1);
            InternalPdbCommand* temporaryBreakpointCmd = new InternalPdbCommand(0, 0, "tbreak " + temporaryBreakpointLocation + "\n");
            addCommand(temporaryBreakpointCmd);
            addSimpleInternalCommand("continue");
        }
    }
}

void DebugSession::run()
{
    addSimpleUserCommand("continue");
}

void DebugSession::interruptDebugger()
{
    addSimpleInternalCommand("quit");
    setState(IDebugSession::EndedState);
}

void DebugSession::addCommand(PdbCommand* cmd)
{
    if ( m_state == EndedState || m_state == StoppingState ) {
        return;
    }
    kDebug() << " +++  adding command to queue:" << cmd;
    if ( cmd->type() == PdbCommand::UserType ) {
        // this is queued and will run after the command is executed.
        updateLocation();
    }
    m_commandQueue.append(cmd);
    emit commandAdded();
}

void DebugSession::checkCommandQueue()
{
    kDebug() << "items in queue:" << m_commandQueue.length();
    if ( m_commandQueue.isEmpty() ) {
        return;
    }
    processNextCommand();
}

void DebugSession::addSimpleUserCommand(const QString& cmd)
{
    UserPdbCommand* cmdObject = new UserPdbCommand(0, 0, cmd + "\n");
    Q_ASSERT(cmdObject->type() == PdbCommand::UserType);
    addCommand(cmdObject);
}

void DebugSession::addSimpleInternalCommand(const QString& cmd)
{
    Q_ASSERT( ! cmd.endsWith('\n') );
    InternalPdbCommand* cmdObject = new InternalPdbCommand(0, 0, cmd + "\n");
    Q_ASSERT(cmdObject->type() == PdbCommand::InternalType);
    addCommand(cmdObject);
}

void DebugSession::addBreakpoint(Breakpoint* bp)
{
    QString location = bp->url().path() + ":" + QString::number(bp->line() + 1);
    kDebug() << "adding breakpoint" << location;
    addSimpleInternalCommand("break " + location);
}

void DebugSession::removeBreakpoint(Breakpoint* bp)
{
    QString location = bp->url().path() + ":" + QString::number(bp->line() + 1);
    kDebug() << "deleting breakpoint" << location;
    addSimpleInternalCommand("clear " + location);
}

void DebugSession::createVariable(Python::Variable* variable, QObject* callback, const char* callbackMethod)
{
    kDebug() << "asked to create variable";
    InternalPdbCommand* cmd = new InternalPdbCommand(variable, "dataFetched", ("print " + variable->expression() + "\n").toAscii());
    variable->m_notifyCreated = callback;
    variable->m_notifyCreatedMethod = callbackMethod;
    addCommand(cmd);
}

void DebugSession::clearOutputBuffer()
{
    m_buffer.clear();
}

void DebugSession::updateLocation()
{
    kDebug() << "updating location";
    InternalPdbCommand* cmd = new InternalPdbCommand(this, "locationUpdateReady", "where\n");
    addCommand(cmd);
}

void DebugSession::locationUpdateReady(QByteArray data) {
    kDebug() << "Got where information: " << data;
    QList<QByteArray> lines = data.split('\n');
    if ( lines.length() >= 3 ) {
        lines.removeLast(); // prompt
        lines.removeLast(); // source line
        QString where = lines.last();
        // > /bar/baz/foo.py(123)<module>()
        QRegExp m("^> (/.*\\.py)\\((\\d*)\\).*$");
        m.setMinimal(true);
        m.exactMatch(where);
        setCurrentPosition(KUrl(m.capturedTexts().at(1)), m.capturedTexts().at(2).toInt() - 1 , "<unknown>");
        kDebug() << "New position: " << m.capturedTexts().at(1) << m.capturedTexts().at(2).toInt() - 1 << m.capturedTexts() << where;
    }
}

void DebugSession::stopDebugger()
{
    m_commandQueue.clear();
    InternalPdbCommand* cmd = new InternalPdbCommand(0, 0, "quit\n");
    addCommand(cmd);
    setState(StoppingState);
    if ( ! m_debuggerProcess->waitForFinished(200) ) {
        m_debuggerProcess->kill();
    }
    m_commandQueue.clear();
    m_nextNotifyMethod = 0;
    m_nextNotifyObject = 0;
    kDebug() << "killed debugger";
    setState(IDebugSession::EndedState);
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
