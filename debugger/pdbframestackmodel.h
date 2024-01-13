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
    
    /// pdb does not support "select-frame n", so we have to use "up" and "down" repeatedly
    /// to select frames. Those two functions tell at which frame the debugger is internally.
    int debuggerAtFrame() const;
    void setDebuggerAtFrame(int newFrame);
public Q_SLOTS:
    void framesFetched(QByteArray frames);
    void threadsFetched(QByteArray threads);
private:
    int m_debuggerAtFrame;
};

}

#endif // PDBFRAMESTACKMODEL_H
