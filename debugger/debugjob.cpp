/*
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>
    SPDX-FileCopyrightText: 2025 Jarmo Tiitto <jarmo.tiitto@gmail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#include "debugjob.h"
#include "debugsession.h"

#include <interfaces/idebugcontroller.h>
#include <interfaces/icore.h>
#include <interfaces/iplugincontroller.h>
#include <outputview/outputmodel.h>

#include <sublime/view.h>
#include <util/processlinemaker.h>

#include <QDebug>
#include "debuggerdebug.h"

namespace Python {


void DebugJob::start()
{
    // Inject environment
    m_session = new DebugSession();

    setStandardToolView(KDevelop::IOutputView::DebugView);
    setBehaviours(KDevelop::IOutputView::Behaviours(KDevelop::IOutputView::AllowUserClose) | KDevelop::IOutputView::AutoScroll);
    KDevelop::OutputModel* pyOutputModel = new KDevelop::OutputModel();
    pyOutputModel->setFilteringStrategy(KDevelop::OutputModel::ScriptErrorFilter);
    setModel(pyOutputModel);

    startOutput();

    qCDebug(KDEV_PYTHON_DEBUGGER) << "connecting DebugSession to OutputModel";
    connect(m_session, &DebugSession::realDataReceived, pyOutputModel, &KDevelop::OutputModel::appendLines);
    connect(m_session, &DebugSession::stderrReceived, pyOutputModel, &KDevelop::OutputModel::appendLines);
    connect(m_session, &DebugSession::stateChanged, this, [this](KDevelop::IDebugSession::DebuggerState state) {
        if (state == KDevelop::IDebugSession::EndedState) {
            emitResult();
        }
    });
    KDevelop::ICore::self()->debugController()->addSession(m_session);
    m_session->start(m_data);
}

bool DebugJob::doKill()
{
    qCDebug(KDEV_PYTHON_DEBUGGER) << "kill signal received";
    m_session->stopDebugger();
    return true;
}

DebugJob::DebugJob(const StartupInfo& info)
    : m_data(info)
{
    setCapabilities(Killable);
}

DebugJob::~DebugJob()
{

}

}

#include "moc_debugjob.cpp"
