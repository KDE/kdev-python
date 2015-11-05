/*
    This file is part of kdev-python, the python language plugin for KDevelop
    Copyright (C) 2012  Sven Brauch <svenbrauch@googlemail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 2 of the License, or
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

#include <KLocalizedString>
#include <signal.h>

#include <debugger/framestack/framestackmodel.h>
#include <interfaces/icore.h>
#include <interfaces/idocumentcontroller.h>

#include "debugsession.h"
#include "pdbframestackmodel.h"
#include "variablecontroller.h"
#include "variable.h"
#include "breakpointcontroller.h"

#include <QDebug>
#include <QStandardPaths>
#include "debuggerdebug.h"

using namespace KDevelop;

static QByteArray debuggerPrompt = "__KDEVPYTHON_DEBUGGER_PROMPT";
static QByteArray debuggerOutputBegin = "__KDEVPYTHON_BEGIN_DEBUGGER_OUTPUT>>>";
static QByteArray debuggerOutputEnd = "<<<__KDEVPYTHON_END___DEBUGGER_OUTPUT";

namespace Python {

DebugSession::DebugSession(QStringList program, const QUrl &workingDirectory) :
    IDebugSession()
    , m_breakpointController(nullptr)
    , m_variableController(nullptr)
    , m_frameStackModel(nullptr)
    , m_workingDirectory(workingDirectory)
    , m_nextNotifyMethod(0)
    , m_inDebuggerData(0)
{
    qCDebug(KDEV_PYTHON_DEBUGGER) << "creating debug session";
    m_program = program;
    m_breakpointController = new Python::BreakpointController(this);
    m_variableController = new VariableController(this);
    m_frameStackModel = new PdbFrameStackModel(this);
}

IBreakpointController* DebugSession::breakpointController() const
{
    return m_breakpointController;
}

IVariableController* DebugSession::variableController() const
{
    return m_variableController;
}

IFrameStackModel* DebugSession::frameStackModel() const
{
    return m_frameStackModel;
}

void DebugSession::start()
{
    setState(StartingState);
    m_debuggerProcess = new KProcess(this);
    m_debuggerProcess->setProgram(m_program);
    m_debuggerProcess->setOutputChannelMode(KProcess::SeparateChannels);
    m_debuggerProcess->blockSignals(true);
    m_debuggerProcess->setWorkingDirectory(m_workingDirectory.path());
    connect(m_debuggerProcess, SIGNAL(readyReadStandardOutput()), this, SLOT(dataAvailable()));
    connect(m_debuggerProcess, SIGNAL(finished(int)), this, SLOT(debuggerQuit(int)));
    connect(this, SIGNAL(debuggerReady()), SLOT(checkCommandQueue()));
    connect(this, SIGNAL(commandAdded()), SLOT(checkCommandQueue()));
    m_debuggerProcess->start();
    m_debuggerProcess->waitForStarted();
    auto dir = QStandardPaths::locate(QStandardPaths::GenericDataLocation,
                                      "kdevpythonsupport/debugger/", QStandardPaths::LocateDirectory);
    InternalPdbCommand* path = new InternalPdbCommand(0, 0,
        "import sys; sys.path.append('"+dir+"')\n");
    InternalPdbCommand* cmd = new InternalPdbCommand(0, 0, "import __kdevpython_debugger_utils\n");
    addCommand(path);
    addCommand(cmd);
    updateLocation();
    m_debuggerProcess->blockSignals(false);
}

void DebugSession::debuggerQuit(int )
{
    setState(EndedState);
}

QStringList byteArrayToStringList(const QByteArray& r) {
    QStringList items;
    foreach ( const QByteArray& item, r.split('\n') ) {
        items << item.data();
    }
    if ( r.endsWith('\n') ) {
        items.pop_back();
    }
    return items;
}

void DebugSession::dataAvailable()
{
    QByteArray data = m_debuggerProcess->readAllStandardOutput();
    qCDebug(KDEV_PYTHON_DEBUGGER) << data.length() << "bytes of data available";
    
    // remove pointless state changes
    data.replace(debuggerOutputBegin+debuggerOutputEnd, "");
    data.replace(debuggerOutputEnd+debuggerOutputBegin, "");
    
    bool endsWithPrompt = false;
    if ( data.endsWith(debuggerPrompt) ) {
        endsWithPrompt = true;
        // remove the prompt
        data = data.mid(0, data.length() - debuggerPrompt.length());
    }
    
    // scan the data, and seperate program output from debugger output
    int len = data.length();
    int delimiterSkip = debuggerOutputEnd.length();
    int i = 0;
    QByteArray realData;
    while ( i < len ) {
        int nextChangeAt = data.indexOf(m_inDebuggerData ? debuggerOutputEnd : debuggerOutputBegin, i);
        bool atLastChange = nextChangeAt == -1;
        nextChangeAt = atLastChange ? len : qMin(nextChangeAt, len);

        
        qCDebug(KDEV_PYTHON_DEBUGGER) << data;
        Q_ASSERT(m_inDebuggerData == 0 || m_inDebuggerData == 1);
        
        if ( m_inDebuggerData == 1 ) {
            QString newDebuggerData = data.mid(i, nextChangeAt - i);
            m_buffer.append(newDebuggerData);
            if ( data.indexOf("Uncaught exception. Entering post mortem debugging") != -1 ) {
                emit realDataReceived(QStringList() << "*****"
                                                    << "  " + i18n("The program being debugged raised an uncaught exception.")
                                                    << "  " + i18n("You can now inspect the status of the program after it exited.")
                                                    << "  " + i18n("The debugger will silently stop when the next command is triggered.")
                                                    << "*****");
            }
        }
        else if ( m_inDebuggerData == 0 ) {
            QByteArray d = data.mid(i, nextChangeAt - i);
            if ( d.length() > 0 ) {
                realData.append(d);
            }
        }
        
        i = nextChangeAt + delimiterSkip;
        if ( m_inDebuggerData != 1 ) m_inDebuggerData = 1;
        else m_inDebuggerData = 0;
        
        if ( atLastChange ) {
            break;
        }
    }
    
    while (int index = realData.indexOf(debuggerPrompt) != -1 ) {
        realData.remove(index-1, debuggerPrompt.length());
    }
    if ( ! realData.isEmpty() ) {
        // FIXME this is not very elegant.
        QStringList items = byteArrayToStringList(realData);
        emit realDataReceived(items);
    }
    
    // Although unbuffered, it seems guaranteed that the debugger prompt is written at once.
    // I don't think a python statement like print "FooBar" will ever break the output into two parts.
    // TODO find explicit documentation for this somewhere.
    if ( endsWithPrompt ) {
        if ( state() == StartingState ) {
            setState(PausedState);
            raiseEvent(connected_to_program);
        }
        else {
            notifyNext();
            if ( m_commandQueue.isEmpty() ) {
                qCDebug(KDEV_PYTHON_DEBUGGER) << "Changing state to PausedState";
                setState(PausedState);
            }
        }
        m_processBusy = false;
        emit debuggerReady();
    }
    
    data = m_debuggerProcess->readAllStandardError();
    if ( ! data.isEmpty() ) {
        emit stderrReceived(byteArrayToStringList(data));
    }
}

void DebugSession::setNotifyNext(QPointer<QObject> object, const char* method)
{
    qCDebug(KDEV_PYTHON_DEBUGGER) << "set notify next:" << object << method;
    m_nextNotifyObject = object;
    m_nextNotifyMethod = method;
}

void DebugSession::notifyNext()
{
    qCDebug(KDEV_PYTHON_DEBUGGER) << "notify next:" << m_nextNotifyObject << this;
    if ( m_nextNotifyMethod && m_nextNotifyObject ) {
        QMetaObject::invokeMethod(m_nextNotifyObject.data(), m_nextNotifyMethod,
                                  Qt::DirectConnection, Q_ARG(QByteArray, m_buffer));
    }
    else {
        qCDebug(KDEV_PYTHON_DEBUGGER) << "notify called, but nothing to notify!";
    }
    m_buffer.clear();
    m_nextNotifyMethod = 0;
    m_nextNotifyObject.clear();
}

void DebugSession::processNextCommand()
{
    qCDebug(KDEV_PYTHON_DEBUGGER) << "processing next debugger command in queue";
    if ( m_processBusy || m_state == EndedState ) {
        qCDebug(KDEV_PYTHON_DEBUGGER) << "process is busy or ended, aborting";
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
    qCDebug(KDEV_PYTHON_DEBUGGER) << "command executed, deleting it.";
    delete cmd;
    if ( ! m_commandQueue.isEmpty() ) {
        processNextCommand();
    }
}

void DebugSession::setState(DebuggerState state)
{
    qCDebug(KDEV_PYTHON_DEBUGGER) << "Setting state to" << state;
    
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
    
    qCDebug(KDEV_PYTHON_DEBUGGER) << "debugger state changed to" << m_state;
    raiseEvent(program_state_changed);
    emit stateChanged(m_state);
}

void DebugSession::write(const QByteArray& cmd)
{
    qCDebug(KDEV_PYTHON_DEBUGGER) << " >>> WRITE:" << cmd;
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
            addSimpleUserCommand(QString("jump " + QString::number(cursor.line() + 1)).toUtf8());
        }
    }
}

void DebugSession::runToCursor()
{
    if (KDevelop::IDocument* doc = KDevelop::ICore::self()->documentController()->activeDocument()) {
        KTextEditor::Cursor cursor = doc->cursorPosition();
        if ( cursor.isValid() ) {
            // TODO disable all other breakpoints
            QString temporaryBreakpointLocation = doc->url().path() + ':' + QString::number(cursor.line() + 1);
            InternalPdbCommand* temporaryBreakpointCmd = new InternalPdbCommand(0, 0, "tbreak " + temporaryBreakpointLocation + '\n');
            addCommand(temporaryBreakpointCmd);
            addSimpleInternalCommand("continue");
            updateLocation();
        }
    }
}

void DebugSession::run()
{
    addSimpleUserCommand("continue");
}

void DebugSession::interruptDebugger()
{
    kill(m_debuggerProcess->pid(), SIGINT);
    updateLocation();
    setState(PausedState);
}

void DebugSession::addCommand(PdbCommand* cmd)
{
    if ( m_state == EndedState || m_state == StoppingState ) {
        return;
    }
    qCDebug(KDEV_PYTHON_DEBUGGER) << " +++  adding command to queue:" << cmd;
    m_commandQueue.append(cmd);
    if ( cmd->type() == PdbCommand::UserType ) {
        // this is queued and will run after the command is executed.
        updateLocation();
    }
    emit commandAdded();
}

void DebugSession::checkCommandQueue()
{
    qCDebug(KDEV_PYTHON_DEBUGGER) << "items in queue:" << m_commandQueue.length();
    if ( m_commandQueue.isEmpty() ) {
        return;
    }
    processNextCommand();
}

void DebugSession::clearObjectTable()
{
    addSimpleInternalCommand("__kdevpython_debugger_utils.cleanup()");
}

void DebugSession::addSimpleUserCommand(const QString& cmd)
{
    clearObjectTable();
    UserPdbCommand* cmdObject = new UserPdbCommand(0, 0, cmd + '\n');
    Q_ASSERT(cmdObject->type() == PdbCommand::UserType);
    addCommand(cmdObject);
}

void DebugSession::addSimpleInternalCommand(const QString& cmd)
{
    Q_ASSERT( ! cmd.endsWith('\n') );
    InternalPdbCommand* cmdObject = new InternalPdbCommand(0, 0, cmd + '\n');
    addCommand(cmdObject);
}

void DebugSession::runImmediately(const QString& cmd)
{
    Q_ASSERT(cmd.endsWith('\n'));
    if ( state() == ActiveState ) {
        m_nextNotifyMethod = 0;
        m_nextNotifyObject.clear(); // TODO is this correct?
        qCDebug(KDEV_PYTHON_DEBUGGER) << "interrupting debugger";
        kill(m_debuggerProcess->pid(), SIGINT);
        write(cmd.toUtf8());
        write("continue\n");
        updateLocation();
    }
    else {
        addCommand(new InternalPdbCommand(0, 0, cmd));
    }
}

void DebugSession::addBreakpoint(Breakpoint* bp)
{
    QString location = bp->url().path() + ":" + QString::number(bp->line() + 1);
    qCDebug(KDEV_PYTHON_DEBUGGER) << "adding breakpoint" << location;
    runImmediately("break " + location + '\n');
}

void DebugSession::removeBreakpoint(Breakpoint* bp)
{
    QString location = bp->url().path() + ":" + QString::number(bp->line() + 1);
    qCDebug(KDEV_PYTHON_DEBUGGER) << "deleting breakpoint" << location;
    runImmediately("clear " + location + '\n');
}

void DebugSession::createVariable(Python::Variable* variable, QObject* callback, const char* callbackMethod)
{
    qCDebug(KDEV_PYTHON_DEBUGGER) << "asked to create variable";
    auto text = ("print(__kdevpython_debugger_utils.obj_to_string(" + variable->expression() + "))\n").toUtf8();
    auto cmd = new InternalPdbCommand(variable, "dataFetched", text);
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
    qCDebug(KDEV_PYTHON_DEBUGGER) << "updating location";
    InternalPdbCommand* cmd = new InternalPdbCommand(this, "locationUpdateReady", "where\n");
    addCommand(cmd);
}

void DebugSession::locationUpdateReady(QByteArray data) {
    qCDebug(KDEV_PYTHON_DEBUGGER) << "Got where information: " << data;
    QList<QByteArray> lines = data.split('\n');
    if ( lines.length() >= 3 ) {
        lines.removeLast(); // prompt
        lines.removeLast(); // source line
        QString where = lines.last();
        // > /bar/baz/foo.py(123)<module>()
        QRegExp m("^> (/.*\\.py)\\((\\d*)\\).*$");
        m.setMinimal(true);
        m.exactMatch(where);
        setCurrentPosition(QUrl::fromLocalFile(m.capturedTexts().at(1)), m.capturedTexts().at(2).toInt() - 1 , "<unknown>");
        qCDebug(KDEV_PYTHON_DEBUGGER) << "New position: " << m.capturedTexts().at(1) << m.capturedTexts().at(2).toInt() - 1 << m.capturedTexts() << where;
    }
}

void DebugSession::stopDebugger()
{
    m_commandQueue.clear();
    InternalPdbCommand* cmd = new InternalPdbCommand(0, 0, "quit\nquit\n");
    addCommand(cmd);
    setState(StoppingState);
    if ( ! m_debuggerProcess->waitForFinished(200) ) {
        m_debuggerProcess->kill();
    }
    m_commandQueue.clear();
    m_nextNotifyMethod = 0;
    m_nextNotifyObject.clear();
    qCDebug(KDEV_PYTHON_DEBUGGER) << "killed debugger";
    setState(IDebugSession::EndedState);
}

DebugSession::~DebugSession()
{
    m_debuggerProcess->kill();
}

void DebugSession::restartDebugger()
{
    addSimpleUserCommand("run");
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

