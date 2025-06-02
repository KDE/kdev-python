/*
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>
    SPDX-FileCopyrightText: 2024 Jarmo Tiitto <jarmo.tiitto@gmail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#include <QTimer>
#include <QApplication>

#include <KLocalizedString>

#include <debugger/framestack/framestackmodel.h>
#include <interfaces/icore.h>
#include <interfaces/idocumentcontroller.h>

#include "debugsession.h"
#include "breakpointcontroller.h"
#include "pdbframestackmodel.h"
#include "variablecontroller.h"
#include "variable.h"
#include "pdbprocess.h"

#include <QDebug>
#include <QRegularExpression>

#include "debuggerdebug.h"

using namespace KDevelop;

namespace Python {

DebugSession::DebugSession()
    : IDebugSession()
    , m_breakpointController(nullptr)
    , m_variableController(nullptr)
    , m_frameStackModel(nullptr)
    , m_resumingFinished([this](const ResponseData& d) {
        resumingFinished(d);
    })
{
    qCDebug(KDEV_PYTHON_DEBUGGER) << "creating debug session";
    auto* const breakpointController = new Python::BreakpointController(this);
    m_breakpointController = breakpointController;
    m_frameStackModel = new PdbFrameStackModel(this);
    m_variableController = new VariableController(this);
    m_debugger = new PdbDebuggerInstance(this);

    connect(&m_killTimer, &QTimer::timeout, this, &DebugSession::killDebuggerNow);
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

PdbDebuggerInstance* DebugSession::debugger() const
{
    // start() must have been invoked once before this method!
    Q_ASSERT(m_debugger);
    Q_ASSERT(m_debugger->instance());
    Q_ASSERT(m_debugger->instance()->process());
    return m_debugger;
}

void DebugSession::start(const StartupInfo& info)
{
    m_state = StartingState;
    // Disable UI controls, so the user cannot try e.g. run() until we are ready.
    raiseEvent(debugger_busy);
    Q_EMIT stateChanged(m_state);

    // Connect lower-level PdbProcess signals to our slots:
    auto* const debugger = m_debugger->instance();
    connect(debugger, &PdbProcess::ready, this, &DebugSession::debuggerInit);
    connect(debugger, &PdbProcess::running, this, &DebugSession::debuggerBusy);
    connect(debugger, &PdbProcess::suspended, this, &DebugSession::inferiorSuspended);
    connect(debugger, &PdbProcess::finished, this, &DebugSession::finalizeState);
    connect(debugger, &PdbProcess::stdoutAvailable, this, &DebugSession::stdoutData, Qt::QueuedConnection);
    connect(debugger, &PdbProcess::stderrAvailable, this, &DebugSession::stderrData, Qt::QueuedConnection);

    // The debugger sends a "frames" response when it has initialized.
    m_debugger->setMethod(m_debugger->currentSeqnro(), m_resumingFinished);

    // Launch the process.
    debugger->start(info);
}

void DebugSession::debuggerInit()
{
    // Successfully connected to the debugger.
    // debuggerBusy() slot was skipped since we haven't actually sent any commands
    // yet. Thus, set up the states such that inferiorSuspended() brings us into
    // PausedState, once the initial response is processed after this slot.
    m_resumingRequest = RunAction::Unspecified;
    m_state = ActiveState;
    Q_EMIT stateChanged(m_state);
}

QStringList byteArrayToStringList(const QByteArray& r) {
    QStringList items;
    const auto list = r.split('\n');
    for ( const QByteArray& item : list ) {
        items << QString::fromLatin1(item);
    }
    if ( r.endsWith('\n') ) {
        items.pop_back();
    }
    return items;
}

void DebugSession::stdoutData(QByteArray data)
{
    // Forward the data.
    Q_EMIT realDataReceived(byteArrayToStringList(data));
}

void DebugSession::stderrData(QByteArray data)
{
    // Forward the data.
    Q_EMIT stderrReceived(byteArrayToStringList(data));
}

void DebugSession::debuggerBusy()
{
    // Switch to active state if we are running user commands. Such commands are those
    // that would resume running the inferior's code. Other commands shouldn't switch
    // between the PausedState or ActiveState.
    if (m_resumingRequest == RunAction::None || m_state != PausedState) {
        return;
    }
    m_state = ActiveState;
    qCDebug(KDEV_PYTHON_DEBUGGER) << PausedState << "==>" << m_state;

    if (!m_flushInProgress) {
        raiseEvent(debugger_busy);
        raiseEvent(program_running);
    }
    Q_EMIT stateChanged(m_state);
}

void DebugSession::inferiorSuspended()
{
    if (m_resumingRequest == RunAction::None || m_state != ActiveState) {
        return;
    }
    qCDebug(KDEV_PYTHON_DEBUGGER) << m_state << "==>" << PausedState;

    if (!m_sessionStarted) {
        m_sessionStarted = true;
        qCDebug(KDEV_PYTHON_DEBUGGER) << "debugger initialized successfully!";
        // run() cannot be invoked from this method as this would interfere
        // with the PausedState <==> ActiveState switching.
        QMetaObject::invokeMethod(this, &DebugSession::runOnStart, Qt::QueuedConnection);

        raiseEvent(connected_to_program);
    }

    m_state = PausedState;
    Q_EMIT stateChanged(m_state);

    // Don't raise debugger_ready nor program_state_changed, or reset m_resumingRequest
    // if flushCommands() is in progress.
    if (!m_flushInProgress) {
        m_resumingRequest = RunAction::None;
        raiseEvent(debugger_ready);
        // Program state has changed.
        raiseEvent(program_state_changed);
    }
}

void DebugSession::runOnStart()
{
    if (debugger()->instance()->isBusy()) {
        qCDebug(KDEV_PYTHON_DEBUGGER) << "DebugSession is not idle yet";

        // Retry to after all currently queued commands.
        debugger()->defer([this](const ResponseData&) {
            QMetaObject::invokeMethod(this, &DebugSession::runOnStart, Qt::QueuedConnection);
        });
        return;
    }

    qCDebug(KDEV_PYTHON_DEBUGGER) << "DebugSession::run()";
    run();
}

void DebugSession::stepOut()
{
    m_resumingRequest = RunAction::StepOut;
    m_debugger->request({QStringLiteral("stepout")}, m_resumingFinished);
}

void DebugSession::stepOverInstruction()
{
    m_resumingRequest = RunAction::StepOverInstruction;
    m_debugger->request({QStringLiteral("steppast")}, m_resumingFinished);
}

void DebugSession::stepInto()
{
    m_resumingRequest = RunAction::StepInto;
    m_debugger->request({QStringLiteral("step")}, m_resumingFinished);
}

void DebugSession::stepIntoInstruction()
{
    m_resumingRequest = RunAction::StepIntoInstruction;
    m_debugger->request({QStringLiteral("step")}, m_resumingFinished);
}

void DebugSession::stepOver()
{
    m_resumingRequest = RunAction::StepOver;
    m_debugger->request({QStringLiteral("next")}, m_resumingFinished);
}

void DebugSession::jumpToCursor()
{
    m_resumingRequest = RunAction::JumpToCursor;
    if (KDevelop::IDocument* doc = KDevelop::ICore::self()->documentController()->activeDocument()) {
        KTextEditor::Cursor cursor = doc->cursorPosition();
        if ( cursor.isValid() ) {
            // TODO: consider a specialized handler, since "jump" can refuse to do anything.
            m_debugger->request({QStringLiteral("jump"), cursor.line() + 1}, m_resumingFinished);
        }
    }
}

void DebugSession::runToCursor()
{
    m_resumingRequest = RunAction::RunToCursor;
    if (KDevelop::IDocument* doc = KDevelop::ICore::self()->documentController()->activeDocument()) {
        KTextEditor::Cursor cursor = doc->cursorPosition();
        if ( cursor.isValid() ) {
            m_runToUrl = doc->url();
            m_runToLine = cursor.line();
            qobject_cast<Python::BreakpointController*>(m_breakpointController)
                ->runToLocation(m_runToUrl, m_runToLine, m_resumingFinished, true);
        }
    }
}

void DebugSession::run()
{
    // The m_resumingRequest is set here (and this applies to other such stepping commands also)
    // to trigger entering into ActiveState. debuggerBusy() then disables the debugger UI controls,
    // and thus prevents the user from trying again until we reach PausedState.
    m_resumingRequest = RunAction::Run;
    m_debugger->request({QStringLiteral("continue")}, m_resumingFinished);
}

void DebugSession::interruptDebugger()
{
    m_debugger->instance()->tryInterrupt();
}

void DebugSession::flushCommands()
{
    if (m_resumingRequest == RunAction::None) {
        return;
    }

    if (m_flushInProgress) {
        // A flush is already in progress.
        // Cancel our handler from the last time flushCommands() was issued.
        m_debugger->setMethod(m_flushSeqNro, {});
    } else {
        // Switch silently to PausedState, if we actually do interrupt the debugger.
        m_flushInProgress = true;
        if (!m_debugger->instance()->tryInterrupt()) {
            m_flushInProgress = false;
            return;
        }
        qCDebug(KDEV_PYTHON_DEBUGGER) << "starting immediate flushing of commands";
    }

    // Queue a no-op with a handler that resumes the interrupted operation.
    auto action = m_resumingRequest;
    m_flushSeqNro = m_debugger->currentSeqnro();
    m_debugger->defer([this, action](const ResponseData&) {
        qCDebug(KDEV_PYTHON_DEBUGGER) << "immediate flushing completed, resuming last action";
        m_flushInProgress = false;
        m_flushSeqNro = -1;
        // Re-issue the interrupted action's command.
        resumeAction(action);
    });
}

void DebugSession::resumeAction(RunAction action)
{
    switch (action) {
    case RunAction::Run:
        run();
        break;
    case RunAction::StepInto:
    case RunAction::StepIntoInstruction:
        stepInto();
        break;
    case RunAction::StepOver:
        stepOver();
        break;
    case RunAction::StepOverInstruction:
        stepOverInstruction();
        break;
    case RunAction::StepOut:
        stepOut();
        break;
    case RunAction::RunToCursor:
        qobject_cast<Python::BreakpointController*>(m_breakpointController)
            ->runToLocation(m_runToUrl, m_runToLine, m_resumingFinished, false);
        break;
    default:
        break;
    }
}

void DebugSession::resumingFinished(const ResponseData& data)
{
    // Update execution location.
    // This handler is invoked by any of the resuming actions, and
    // the "frames" field contains just the most recent frame. (this response is guaranteed)

    if (m_flushInProgress) {
        qCDebug(KDEV_PYTHON_DEBUGGER) << "not updating position due to flushCommands() in progress";
        return;
    }

    const auto frame = responseArray(data, QStringLiteral("frames")).at(0).toObject();
    const auto file = frame.value(QStringLiteral("filename")).toString();
    const int line = frame.value(QStringLiteral("line")).toInt();
    const int addr = frame.value(QStringLiteral("address")).toInt();

    setCurrentPosition(QUrl::fromLocalFile(file), line - 1, QString::number(addr));
    qCDebug(KDEV_PYTHON_DEBUGGER) << "New position: " << file << line - 1;

    Q_EMIT programStopped(data);
}

void DebugSession::stopDebugger()
{
    if (m_state >= StoppingState || m_state == NotStartedState) {
        return;
    }
    qCDebug(KDEV_PYTHON_DEBUGGER) << "stopping debugger";
    m_state = StoppingState;
    Q_EMIT stateChanged(m_state);

    if (!m_debugger || !m_debugger->instance()) {
        return;
    }
    // Tell the server to quit eventually.
    m_debugger->instance()->sendControlCommand(PdbProcess::ControlCommand::Terminate);
    m_debugger->instance()->tryInterrupt();

    // Ensure we won't wait forever for the process to die.
    m_killTimer.setSingleShot(true);
    m_killTimer.setInterval(5000);
    m_killTimer.start();
}

void DebugSession::killDebuggerNow()
{
    killDebugger();
}

void DebugSession::finalizeState()
{
    // Disarm the kill timer, the process exited.
    m_killTimer.stop();

    if (m_state == EndedState) {
        // finalizeState() already invoked.
        return;
    } else if (m_state < StoppingState) {
        // Normal exit of the inferior. (we skipped the StoppingState.)
        raiseEvent(program_exited);
    }

    m_state = EndedState;
    raiseEvent(debugger_exited);
    Q_EMIT stateChanged(m_state);
}

void DebugSession::killDebugger()
{
    if (m_state == EndedState || m_state == NotStartedState) {
        return;
    }
    // Kill timer expired or must stop in a hurry.
    qCDebug(KDEV_PYTHON_DEBUGGER) << "killing debugger now";
    if (m_state < StoppingState) {
        m_state = StoppingState;
        Q_EMIT stateChanged(m_state);
    }

    if (m_debugger && m_debugger->instance()) {
        // Disarm the kill timer to not repeatedly invoke us.
        m_killTimer.stop();
        // Be gone!
        m_debugger->instance()->killNow();
    }

    finalizeState();
}

DebugSession::~DebugSession()
{
    killDebugger();
}

void DebugSession::restartDebugger()
{
    // Not implemented. There seems to be no user action for this in KDevelop?
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

#include "moc_debugsession.cpp"
