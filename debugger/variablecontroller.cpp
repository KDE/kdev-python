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

void VariableController::handleEvent(IDebugSession::event_t event)
{
    if ( event == IDebugSession::thread_or_frame_changed ) {
        DebugSession* s = static_cast<DebugSession*>(session());
        PdbFrameStackModel* model = static_cast<PdbFrameStackModel*>(s->frameStackModel());
        int delta = model->currentFrame() - model->debuggerAtFrame();
        model->setDebuggerAtFrame(model->currentFrame());
        bool positive = delta > 0;
        qCDebug(KDEV_PYTHON_DEBUGGER) << "changing frame by" << delta;
        for ( int i = delta; i != 0; i += ( positive ? -1 : 1 ) ) {
            qCDebug(KDEV_PYTHON_DEBUGGER) << ( positive ? "up" : "down" ) << model->currentFrame() << model->debuggerAtFrame();
            s->addSimpleInternalCommand(positive ? QStringLiteral("up") : QStringLiteral("down"));
        }
    }
    KDevelop::IVariableController::handleEvent(event);
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

void VariableController::localsUpdateReady(QByteArray rawData)
{
    QRegularExpression formatExtract( QRegularExpression::anchoredPattern(QStringLiteral("([a-zA-Z0-9_]+) \\=\\> (.*)")));
    QList<QByteArray> data = rawData.split('\n');
    data.removeAll({});
    qCDebug(KDEV_PYTHON_DEBUGGER) << "locals update:" << data;

    int i = 0;
    QStringList vars;
    QMap<QString, QString> values;
    while ( i < data.length() ) {
        QByteArray d = data.at(i);
        auto match = formatExtract.match(QString::fromLatin1(d));
        if ( match.hasMatch() ) {
            QString key = match.captured(1);
            vars << key;
            values[key] = match.captured(2);
        }
        else qCWarning(KDEV_PYTHON_DEBUGGER) << "mismatch:" << d;
        i++;
    }

    QList<KDevelop::Variable*> variableObjects = KDevelop::ICore::self()->debugController()->variableCollection()
                                                 ->locals()->updateLocals(vars);
    for ( int i = 0; i < variableObjects.length(); i++ ) {
        KDevelop::Variable* v = variableObjects[i];

        auto model = v->model();
        auto parent = model->indexForItem(v, 0);
        auto childCount = v->model()->rowCount(parent);
        qCDebug(KDEV_PYTHON_DEBUGGER) << "updating:" << v->expression() << "active children:" << childCount;
        for ( int j = 0; j < childCount; j++ ) {
            auto index = model->index(j, 0, parent);
            auto child = static_cast<KDevelop::TreeItem*>(index.internalPointer());
            if ( auto childVariable = qobject_cast<Variable*>(child) ) {
                qCDebug(KDEV_PYTHON_DEBUGGER) << "   got child var:" << childVariable->expression();
                v->fetchMoreChildren();
                break;
            }
        }

        v->setValue(values[v->expression()]);
        v->setHasMoreInitial(true);
    }
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
        // TODO find a more elegant solution for this import!
        InternalPdbCommand* import = new InternalPdbCommand(nullptr, nullptr, QStringLiteral("import __kdevpython_debugger_utils\n"));
        InternalPdbCommand* cmd = new InternalPdbCommand(this, "localsUpdateReady",
                                  QStringLiteral("__kdevpython_debugger_utils.format_locals(__kdevpython_debugger_utils.__kdevpython_builtin_locals())\n"));
        d->addCommand(import);
        d->addCommand(cmd);
   }
}

}

#include "moc_variablecontroller.cpp"
