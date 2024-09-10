/*
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef PDBDEBUGJOB_H
#define PDBDEBUGJOB_H

#include <outputview/outputjob.h>
#include <outputview/outputmodel.h>
#include "debugsession.h"

namespace Python {

class DebugJob : public KDevelop::OutputJob
{
Q_OBJECT
public:
    DebugJob();
    ~DebugJob() override;
    
    /**
     * @brief Create a debug session and start it.
     **/
    void start() override;
    bool doKill() override;
    
    QUrl m_scriptUrl;
    QString m_interpreter;
    QStringList m_args;
    QUrl m_workingDirectory;
    QString m_envProfileName;

private Q_SLOTS:
    void standardOutputReceived(QStringList lines);
    void standardErrorReceived(QStringList lines);

private:
    OutputModel* outputModel();
    DebugSession* m_session;
public Q_SLOTS:
    void sessionFinished();
};

}

#endif // DEBUGJOB_H
