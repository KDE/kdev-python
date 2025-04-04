/*
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#include "debugjob.h"
#include "debugsession.h"

#include <interfaces/idebugcontroller.h>
#include <interfaces/icore.h>
#include <interfaces/iplugincontroller.h>

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
    OutputModel* pyOutputModel = new KDevelop::OutputModel();
    pyOutputModel->setFilteringStrategy(OutputModel::ScriptErrorFilter);
    setModel(pyOutputModel);

    startOutput();
    
    qCDebug(KDEV_PYTHON_DEBUGGER) << "connecting standardOutputReceived";
    connect(m_session, &DebugSession::realDataReceived, this, &DebugJob::standardOutputReceived);
    connect(m_session, &DebugSession::stderrReceived, this, &DebugJob::standardErrorReceived);
    connect(m_session, &KDevelop::IDebugSession::finished, this, &DebugJob::sessionFinished);
    KDevelop::ICore::self()->debugController()->addSession(m_session);
    m_session->start(m_data);
}

void DebugJob::sessionFinished()
{
    emitResult();
}

void DebugJob::standardErrorReceived(QStringList lines)
{
    if ( OutputModel* m = outputModel() ) {
        m->appendLines(lines);
    }
}

void DebugJob::standardOutputReceived(QStringList lines)
{
    qCDebug(KDEV_PYTHON_DEBUGGER) << "standard output received:" << lines << outputModel();
    if ( OutputModel* m = outputModel() ) {
        m->appendLines(lines);
    }
}

OutputModel* DebugJob::outputModel()
{
    return dynamic_cast<OutputModel*>(model());
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
