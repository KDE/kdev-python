/*
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef PDBDEBUGJOB_H
#define PDBDEBUGJOB_H

#include <outputview/outputjob.h>
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

private:
    const StartupInfo m_data;
    DebugSession* m_session;
};

}

#endif // DEBUGJOB_H
