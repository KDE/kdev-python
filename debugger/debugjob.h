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


#ifndef PDBDEBUGJOB_H
#define PDBDEBUGJOB_H

#include <outputview/outputjob.h>
#include "debugsession.h"
#include <KUrl>

namespace Python {

class DebugJob : public KDevelop::OutputJob
{

public:
    DebugJob();
    virtual ~DebugJob();
    
    virtual void start();
    virtual bool doKill();
    
    void lockProcess();
    void unlockProcess();
    
    KUrl m_scriptUrl;
    QString m_interpreter;
    QStringList m_args;

private:
    DebugSession* m_session;
};

}

#endif // DEBUGJOB_H
