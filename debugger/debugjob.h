/*
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef PDBDEBUGJOB_H
#define PDBDEBUGJOB_H

#include <outputview/outputjob.h>
#include <outputview/outputmodel.h>
#include "startupinfo.h"

namespace Python {

class DebugSession;

class DebugJob : public KDevelop::OutputJob
{
Q_OBJECT
public:
    explicit DebugJob(const StartupInfo& info);
    ~DebugJob() override;
    
    /**
     * @brief Create a debug session and start it.
     **/
    void start() override;
    bool doKill() override;

private Q_SLOTS:
    void standardOutputReceived(QStringList lines);
    void standardErrorReceived(QStringList lines);

private:
    KDevelop::OutputModel* outputModel();
    const StartupInfo m_data;
    DebugSession* m_session;
public Q_SLOTS:
    void sessionFinished();
};

}

#endif // DEBUGJOB_H
