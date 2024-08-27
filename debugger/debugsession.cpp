/*
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>

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
#include "startupinfo.h"
#include "variablecontroller.h"
#include "variable.h"

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
{
    qCDebug(KDEV_PYTHON_DEBUGGER) << "creating debug session";
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

void DebugSession::start(const StartupInfo& info)
{
    // TODO
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

#if 0 // temporally keep this code as place holder for git.
        raiseEvent(debugger_ready);
        if ( currentUrl().isValid() ) {
            Q_EMIT showStepInSource(currentUrl(), currentLine(), currentAddr());
        }
#endif

void DebugSession::stepOut()
{
    // TODO this only steps out of functions; use temporary breakpoints for loops maybe?
    // TODO
}

void DebugSession::stepOverInstruction()
{
    // TODO
}

void DebugSession::stepInto()
{
    // TODO
}

void DebugSession::stepIntoInstruction()
{
    // TODO
}

void DebugSession::stepOver()
{
    // TODO
}

void DebugSession::jumpToCursor()
{
    if (KDevelop::IDocument* doc = KDevelop::ICore::self()->documentController()->activeDocument()) {
        KTextEditor::Cursor cursor = doc->cursorPosition();
        if ( cursor.isValid() ) {
            // TODO disable all other breakpoints
            // WIP
        }
    }
}

void DebugSession::runToCursor()
{
    if (KDevelop::IDocument* doc = KDevelop::ICore::self()->documentController()->activeDocument()) {
        KTextEditor::Cursor cursor = doc->cursorPosition();
        if ( cursor.isValid() ) {
            // TODO disable all other breakpoints
            QString temporaryBreakpointLocation = doc->url().path() + QLatin1Char(':') + QString::number(cursor.line() + 1);
            // TODO
        }
    }
}

void DebugSession::run()
{
    // TODO
}

void DebugSession::interruptDebugger()
{
    // TODO
}

void DebugSession::updateLocation()
{
    qCDebug(KDEV_PYTHON_DEBUGGER) << "updating location";
    // TODO
}

void DebugSession::locationUpdateReady(QByteArray data) {
    // TODO
}

void DebugSession::stopDebugger()
{
    // TODO
}

void DebugSession::killDebuggerNow()
{
    // TODO
}

void DebugSession::finalizeState()
{
    // TODO
}

DebugSession::~DebugSession()
{
    // TODO
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

#include "moc_debugsession.cpp"
