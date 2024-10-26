/*
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#include "variablecontroller.h"
#include "variable.h"
#include "debugsession.h"
#include "pdbframestackmodel.h"
#include <codehelpers.h>
#include <language/duchain/duchainlock.h>
#include <language/duchain/declaration.h>
#include <language/duchain/duchain.h>
#include <interfaces/ilanguagecontroller.h>

#include <debugger/variable/variablecollection.h>
#include <debugger/framestack/framestackmodel.h>
#include <interfaces/icore.h>
#include <QStack>
#include <KMessageBox>
#include <KLocalizedString>

#include <QDebug>
#include <QRegularExpression>
#include "debuggerdebug.h"

using namespace KDevelop;

namespace Python {

VariableController::VariableController(IDebugSession* parent) : IVariableController(parent)
{
    m_updateTimer.setSingleShot(true);
    m_updateTimer.setInterval(100);
    QObject::connect(&m_updateTimer, &QTimer::timeout,
                     this, &VariableController::_update);
}

void VariableController::addWatch(KDevelop::Variable* variable)
{
    variableCollection()->watches()->add(variable->expression());
}

void VariableController::addWatchpoint(KDevelop::Variable* /*variable*/)
{
    qCWarning(KDEV_PYTHON_DEBUGGER) << "addWatchpoint requested (not implemented)";
}

KDevelop::Variable* VariableController::createVariable(KDevelop::TreeModel* model, KDevelop::TreeItem* parent, const QString& expression, const QString& display)
{
    return new Variable(model, parent, expression, display);
}

KTextEditor::Range VariableController::expressionRangeUnderCursor(KTextEditor::Document* doc, const KTextEditor::Cursor& cursor)
{
    QString prefix;
    DUChainReadLocker lock;
    if ( ! doc->isModified() ) {
        if ( TopDUContext* context = DUChain::self()->chainForDocument(doc->url()) ) {
            DUContext* contextAtCursor = context->findContextAt(CursorInRevision(cursor.line(), cursor.column()));
            if ( contextAtCursor && contextAtCursor->type() == DUContext::Class ) {
                if ( contextAtCursor->owner() && ! contextAtCursor->owner()->identifier().isEmpty() ) {
                    prefix = contextAtCursor->owner()->identifier().toString() + QStringLiteral(".");
                }
            }
        }
    }
    else {
        qCDebug(KDEV_PYTHON_DEBUGGER) << "duchain unavailable for document" << doc->url() << "or document out of date";
    }

    TextDocumentLazyLineFetcher linefetcher(doc);
    KTextEditor::Cursor startCursor;
    auto text = QString(prefix + CodeHelpers::expressionUnderCursor(linefetcher, cursor, startCursor));
    return {startCursor, startCursor + KTextEditor::Cursor{0, static_cast<int>(text.length())}};
}

void VariableController::handleEvent(IDebugSession::event_t event)
{
    if (!variableCollection())
        return;

    const auto* const frameModel = qobject_cast<DebugSession*>(QObject::parent())->frameStackModel();
    const int frame = frameModel->currentFrame();

    if (event == IDebugSession::program_state_changed) {
        return;
    }

    if (frame == -1 || event != IDebugSession::thread_or_frame_changed)
        return;

    KDevelop::IVariableController::handleEvent(event);
}

void VariableController::localsUpdateReady(QByteArray rawData)
{
    // TODO
}

void VariableController::update() {
    m_updateTimer.start();
}

void VariableController::_update()
{
    qCDebug(KDEV_PYTHON_DEBUGGER) << " ************************* update requested";
    DebugSession* d = static_cast<DebugSession*>(parent());
    if (autoUpdate() & UpdateWatches) {
        variableCollection()->watches()->reinstall();
    }

   if (autoUpdate() & UpdateLocals) {
       // TODO
   }
}

}

#include "moc_variablecontroller.cpp"
