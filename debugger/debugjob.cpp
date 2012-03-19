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

#include <KDebug>

#include <interfaces/idebugcontroller.h>
#include <interfaces/icore.h>

#include "debugjob.h"

namespace Python {


void DebugJob::start()
{
    QStringList program;
    program << m_interpreter << "-u" << "-m" << "pdb" << m_scriptUrl.path(KUrl::RemoveTrailingSlash) << m_args;
    m_session = new DebugSession(program);
    KDevelop::ICore::self()->debugController()->addSession(m_session);
    m_session->start();
    kDebug() << "starting program:" << program;
}

bool DebugJob::doKill()
{
    kDebug() << "kill signal received";
    if ( m_session ) {
        m_session->stopDebugger();
    }
    return KJob::doKill();
}

DebugJob::DebugJob()
{

}

DebugJob::~DebugJob()
{

}

}
