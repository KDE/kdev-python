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

#include "debugjob.h"



#include <interfaces/idebugcontroller.h>
#include <interfaces/icore.h>
#include <interfaces/iplugincontroller.h>

#include <sublime/view.h>
#include <util/processlinemaker.h>

#include <QDebug>
#include <QStandardPaths>
#include "debuggerdebug.h"

namespace Python {


void DebugJob::start()
{
    QStringList program;
    QString debuggerUrl = QStandardPaths::locate(QStandardPaths::GenericDataLocation, "kdevpythonsupport/debugger", QStandardPaths::LocateDirectory) + "/kdevpdb.py";
    program << m_interpreter << "-u" << debuggerUrl << m_scriptUrl.toLocalFile() << m_args;
    // Inject environment
    m_session = new DebugSession(program, m_workingDirectory, m_envProfileName);
    
    setStandardToolView(KDevelop::IOutputView::DebugView);
    setBehaviours(KDevelop::IOutputView::Behaviours(KDevelop::IOutputView::AllowUserClose) | KDevelop::IOutputView::AutoScroll);
    OutputModel* pyOutputModel = new KDevelop::OutputModel();
    pyOutputModel->setFilteringStrategy(OutputModel::ScriptErrorFilter);
    setModel(pyOutputModel);
    setTitle(m_interpreter + m_scriptUrl.toLocalFile());

    setModel(new KDevelop::OutputModel(nullptr));

    startOutput();
    
    qCDebug(KDEV_PYTHON_DEBUGGER) << "connecting standardOutputReceived";
    connect(m_session, &DebugSession::realDataReceived, this, &DebugJob::standardOutputReceived);
    connect(m_session, &DebugSession::stderrReceived, this, &DebugJob::standardErrorReceived);
    connect(m_session, &KDevelop::IDebugSession::finished, this, &DebugJob::sessionFinished);
    KDevelop::ICore::self()->debugController()->addSession(m_session);
    m_session->start();
    qCDebug(KDEV_PYTHON_DEBUGGER) << "starting program:" << program;
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

DebugJob::DebugJob()
{

}

DebugJob::~DebugJob()
{

}

}
