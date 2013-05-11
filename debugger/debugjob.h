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


#ifndef PDBDEBUGJOB_H
#define PDBDEBUGJOB_H

#include <outputview/outputjob.h>
#include <outputview/outputmodel.h>
#include "debugsession.h"
#include <KUrl>

namespace Python {

class DebugJob : public KDevelop::OutputJob
{
Q_OBJECT
public:
    DebugJob();
    virtual ~DebugJob();
    
    /**
     * @brief Create a debug session and start it.
     *
     * @return void
     **/
    virtual void start();
    virtual bool doKill();
    
    KUrl m_scriptUrl;
    QString m_interpreter;
    QStringList m_args;

private slots:
    void standardOutputReceived(QStringList lines);
    void standardErrorReceived(QStringList lines);

private:
    OutputModel* outputModel();
    DebugSession* m_session;
public slots:
    void sessionFinished();
};

}

#endif // DEBUGJOB_H
