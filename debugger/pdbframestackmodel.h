/*
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef PDBFRAMESTACKMODEL_H
#define PDBFRAMESTACKMODEL_H

#include <debugger/framestack/framestackmodel.h>

using namespace KDevelop;

namespace Python {

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

    void framesFetched(QByteArray frames);
    void threadsFetched(QByteArray threads);
};

}

#endif // PDBFRAMESTACKMODEL_H
