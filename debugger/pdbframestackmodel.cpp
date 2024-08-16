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
    // Stack-frame selection needs a round trip to the server to be reliable.
    auto* const debugger = static_cast<DebugSession*>(QObject::parent())->debugger();
    qCDebug(KDEV_PYTHON_DEBUGGER) << "selecting stack-frame" << newFrame;
    debugger->request(QStringLiteral("selectframe %1").arg(newFrame), [this](const ResponseData& d) {
        frameSelected(d);
    });
}

void PdbFrameStackModel::frameSelected(const ResponseData& data)
{
    m_debuggerAtFrame = responseValue(data, QStringLiteral("activeframe")).toInt();
    qCDebug(KDEV_PYTHON_DEBUGGER) << "active stack-frame:" << m_debuggerAtFrame;
}

void PdbFrameStackModel::framesFetched(const ResponseData& data)
{
    const auto framelist = responseArray(data, QStringLiteral("frames"));

    QList<FrameItem> frames;

    // The most recent frame is first, but it's not necessarily the current one.
    for (const auto& obj : framelist) {
        const auto frame = obj.toObject();
        if (frame.value(QStringLiteral("current")).toBool()) {
            m_debuggerAtFrame = frames.size();
        }

        const auto file = frame.value(QStringLiteral("filename")).toString();
        if (file == QStringLiteral("<string>")) {
            // End of frames. (server sends us extra frames which we must ignore.
            // "<string>" is magic from depths of Bdb)
            break;
        }

        auto& item = frames.emplace_back();
        item.nr = frames.size() - 1;
        item.file = QUrl::fromLocalFile(file);
        item.line = frame.value(QStringLiteral("line")).toInt() - 1;
        // Extract the function/name part between the first ')' and subsequent '\n' char.
        const QString location = frame.value(QStringLiteral("location")).toString();
        const auto k = location.indexOf(QLatin1Char(')'));
        auto j = location.indexOf(QLatin1Char('\n'), k);
        j = j < k ? location.size() : j; // Some frames don't have a '\n' appended.
        item.name = location.sliced(k + 1, j - (k + 1));
    }

    qCDebug(KDEV_PYTHON_DEBUGGER) << "at frame:" << m_debuggerAtFrame;
    setFrames(0, frames);
}

void PdbFrameStackModel::threadsFetched()
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
    auto* const debugger = static_cast<DebugSession*>(QObject::parent())->debugger();
    debugger->request(QStringLiteral("where"), [this](const ResponseData& d) {
        framesFetched(d);
    });
}

void PdbFrameStackModel::fetchThreads()
{
    qCDebug(KDEV_PYTHON_DEBUGGER) << "threads requested";
    // TODO: pdb doesn't support threads, so no point doing a round-trip to the server yet.
    threadsFetched();
}

}

#include "moc_pdbframestackmodel.cpp"
