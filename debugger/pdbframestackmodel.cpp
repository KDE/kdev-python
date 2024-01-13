/*
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#include "pdbframestackmodel.h"
#include "debugsession.h"
#include <QRegularExpression>

#include <QDebug>
#include "debuggerdebug.h"

using namespace KDevelop;

namespace Python {
    
PdbFrameStackModel::PdbFrameStackModel(IDebugSession* session): FrameStackModel(session), m_debuggerAtFrame(0)
{
    
}

int PdbFrameStackModel::debuggerAtFrame() const
{
    return m_debuggerAtFrame;
}

void PdbFrameStackModel::setDebuggerAtFrame(int newFrame)
{
//     Q_ASSERT(newFrame >= 0);
    m_debuggerAtFrame = newFrame;
}

void PdbFrameStackModel::framesFetched(QByteArray framelist)
{
    qCDebug(KDEV_PYTHON_DEBUGGER) << "frames fetched:" << framelist;
    QList<QByteArray> lines = framelist.split('\n');
    QList<FrameItem> frames;
    bool parsingLocation = false;
    FrameItem* currentFrame = nullptr;
    int framesCount = 0;
    for ( const QString& line : lines ) {
        if ( line.startsWith("-> ") ) {
            parsingLocation = true;
            if ( currentFrame ) {
                frames << *currentFrame;
            }
            currentFrame = new FrameItem();
            currentFrame->nr = framesCount;
            framesCount++;
        }
        else if ( parsingLocation ) {
            QRegularExpression location(QStringLiteral("(\\>?)\\s*(.*)\\(([0-9]+)\\)(.*)"));
            // version 1 has some *really* weird "greedy" ruleset which makes no sense at all for me
            location.setPatternSyntax(QRegExp::RegExp2);
            const auto match = location.match(line);
            if ( match.hasMatch() ) {
                if ( ! location.capturedTexts().at(1).isEmpty() ) {
                if ( ! match.captured(1).isEmpty() ) {
                    m_debuggerAtFrame = framesCount;
                }
                currentFrame->file = QUrl::fromLocalFile(match.captured(2));
                currentFrame->line = match.captured(3).toInt() - 1;
                currentFrame->name = match.captured(4);
            }
            else {
                qCDebug(KDEV_PYTHON_DEBUGGER) << "regular expression mismatches" << line;
            }
        }
    }
    m_debuggerAtFrame = framesCount - m_debuggerAtFrame - 1;
    qCDebug(KDEV_PYTHON_DEBUGGER) << "at frame:" << m_debuggerAtFrame;
    QVector<FrameItem> framesReversed;
    framesReversed.reserve(frames.length());
    for ( int i = frames.length() - 1; i >= 0; i-- ) {
        framesReversed.append(frames.at(i));
        framesReversed.last().nr = framesCount - i - 2;
    }
    setFrames(0, framesReversed);
}

void PdbFrameStackModel::threadsFetched(QByteArray threadsData)
{
    qCDebug(KDEV_PYTHON_DEBUGGER) << "threads fetched" << threadsData;
    qCDebug(KDEV_PYTHON_DEBUGGER) << "Implement me: Thread debugging is not supported by pdb.";
    QVector<ThreadItem> threads;
    ThreadItem mainThread;
    mainThread.nr = 0;
    mainThread.name = "main thread";
    threads << mainThread;
    setThreads(threads);
    setCurrentThread(0);
}

void PdbFrameStackModel::fetchFrames(int /*threadNumber*/, int /*from*/, int /*to*/)
{
    qCDebug(KDEV_PYTHON_DEBUGGER) << "frames requested";
    InternalPdbCommand* cmd = new InternalPdbCommand(this, "framesFetched", "where\n");
    static_cast<DebugSession*>(session())->addCommand(cmd);
}

void PdbFrameStackModel::fetchThreads()
{
    qCDebug(KDEV_PYTHON_DEBUGGER) << "threads requested";
    // pdb doesn't support threads.
    InternalPdbCommand* cmd = new InternalPdbCommand(this, "threadsFetched", "pass\n");
    static_cast<DebugSession*>(session())->addCommand(cmd);
}

}

#include "moc_pdbframestackmodel.cpp"
