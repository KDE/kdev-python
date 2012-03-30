/*
    This file is part of kdev-python, the python language plugin for KDevelop
    Copyright (C) 2012  Sven Brauch <svenbrauch@googlemail.com>

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

#include <KDebug>
#include <KStandardDirs>

#include <interfaces/idebugcontroller.h>
#include <interfaces/icore.h>

#include "debugjob.h"
#include <sublime/view.h>
#include <util/processlinemaker.h>

namespace Python {


void DebugJob::start()
{
    QStringList program;
    QString debuggerUrl = KStandardDirs::locate("data", "kdevpythonsupport/debugger/") + "/kdevpdb.py";
    program << m_interpreter << "-u" << debuggerUrl << m_scriptUrl.path(KUrl::RemoveTrailingSlash) << m_args;
    m_session = new DebugSession(program);
    
    setStandardToolView(KDevelop::IOutputView::DebugView);
    setBehaviours(KDevelop::IOutputView::Behaviours(KDevelop::IOutputView::AllowUserClose) | KDevelop::IOutputView::AutoScroll);
    setModel(new KDevelop::OutputModel(), KDevelop::IOutputView::TakeOwnership);
    setTitle(m_interpreter + m_scriptUrl.path());
    
    startOutput();
    
    kDebug() << "connecting standardOutputReceived";
    connect(m_session, SIGNAL(realDataReceived(QStringList)), this, SLOT(standardOutputReceived(QStringList)));
    connect(m_session, SIGNAL(stderrReceived(QStringList)), this, SLOT(standardErrorReceived(QStringList)));
    connect(m_session, SIGNAL(finished()), this, SLOT(sessionFinished()));
    KDevelop::ICore::self()->debugController()->addSession(m_session);
    m_session->start();
    kDebug() << "starting program:" << program;
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
    kDebug() << "standard output received:" << lines << outputModel();
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
    kDebug() << "kill signal received";
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
