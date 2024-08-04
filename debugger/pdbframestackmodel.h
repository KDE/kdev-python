/*
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef PDBFRAMESTACKMODEL_H
#define PDBFRAMESTACKMODEL_H

#include <debugger/framestack/framestackmodel.h>

#include "pdbdebuggerinstance.h"

using namespace KDevelop;

namespace Python {

class DebugSession;

/**
* @brief The Frame Stack Model, which contains and controls the frame stack ("backtrace").
**/
class PdbFrameStackModel : public KDevelop::FrameStackModel
{
Q_OBJECT
public:
    PdbFrameStackModel(IDebugSession* session);
    void fetchFrames(int threadNumber, int from, int to) override;
    void fetchThreads() override;

    int debuggerAtFrame() const;
    void setDebuggerAtFrame(int newFrame);

private:
    int m_debuggerAtFrame = 0;

    void framesFetched(const ResponseData& frames);
    void threadsFetched();
};

}

#endif // PDBFRAMESTACKMODEL_H
