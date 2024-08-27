/*
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#include "pdbframestackmodel.h"
#include "debugsession.h"

#include <QDebug>
#include "debuggerdebug.h"

using namespace KDevelop;

namespace Python {

PdbFrameStackModel::PdbFrameStackModel(IDebugSession* session)
    : FrameStackModel(session)
{
}

int PdbFrameStackModel::debuggerAtFrame() const
{
    return m_debuggerAtFrame;
}

void PdbFrameStackModel::setDebuggerAtFrame(int newFrame)
{
    // FIXME: actually change the current frame in PDB.
    m_debuggerAtFrame = newFrame;
}

void PdbFrameStackModel::framesFetched(QByteArray framelist)
{
    QList<FrameItem> frames;
    // TODO
    qCDebug(KDEV_PYTHON_DEBUGGER) << "at frame:" << m_debuggerAtFrame;
    setFrames(0, frames);
}

void PdbFrameStackModel::threadsFetched(QByteArray threadsData)
{
    // TODO: Implement me: Thread debugging is not supported by pdb.
    qCDebug(KDEV_PYTHON_DEBUGGER) << "threads fetched";
    QVector<ThreadItem> threads;
    ThreadItem mainThread;
    mainThread.nr = 0;
    mainThread.name = QStringLiteral("main thread");
    threads << mainThread;
    setThreads(threads);
    setCurrentThread(0);
}

void PdbFrameStackModel::fetchFrames(int /*threadNumber*/, int /*from*/, int /*to*/)
{
    qCDebug(KDEV_PYTHON_DEBUGGER) << "frames requested";
    // TODO
}

void PdbFrameStackModel::fetchThreads()
{
    qCDebug(KDEV_PYTHON_DEBUGGER) << "threads requested";
    // TODO
}

}

#include "moc_pdbframestackmodel.cpp"
