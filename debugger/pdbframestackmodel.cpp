/*
    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) 2012  <copyright holder> <email>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/


#include "pdbframestackmodel.h"
#include "debugsession.h"
#include <KDebug>
#include <QRegExp>

using namespace KDevelop;

namespace Python {
    
PdbFrameStackModel::PdbFrameStackModel(IDebugSession* session): FrameStackModel(session)
{
    
}

void PdbFrameStackModel::framesFetched(QByteArray framelist)
{
    kDebug() << "frames fetched:" << framelist;
    QList<QByteArray> lines = framelist.split('\n');
    QList<FrameItem> frames;
    bool parsingLocation = false;
    FrameItem* currentFrame = 0;
    int number = 0;
    foreach ( const QString& line, lines ) {
        if ( line.startsWith("-> ") ) {
            parsingLocation = true;
            if ( currentFrame ) {
                frames << *currentFrame;
            }
            currentFrame = new FrameItem();
            currentFrame->nr = number;
            number += 1;
        }
        else if ( parsingLocation ) {
            QRegExp location("\\>?\\s*(.*)\\(([0-9]+)\\)(.*)");
            // version 1 has some *really* weird "greedy" ruleset which makes no sense at all for me
            location.setPatternSyntax(QRegExp::RegExp2);
            if ( location.exactMatch(line) ) {
                kDebug() << location.capturedTexts();
                currentFrame->file = location.capturedTexts().at(1);
                currentFrame->line = location.capturedTexts().at(2).toInt() - 1;
                currentFrame->name = location.capturedTexts().at(3);
            }
            else {
                kDebug() << "regular expression mismatches" << line;
            }
        }
    }
    setFrames(0, frames);
}

void PdbFrameStackModel::threadsFetched(QByteArray threadsData)
{
    kDebug() << "threads fetched" << threadsData;
    QList<ThreadItem> threads;
    ThreadItem testThread;
    testThread.nr = 0;
    testThread.name = "test thread";
    threads << testThread;
    setThreads(threads);
    setCurrentThread(0);
}

void PdbFrameStackModel::fetchFrames(int threadNumber, int from, int to)
{
    kDebug() << "frames requested";
    InternalPdbCommand* cmd = new InternalPdbCommand(this, "framesFetched", "where\n");
    static_cast<DebugSession*>(session())->addCommand(cmd);
}

void PdbFrameStackModel::fetchThreads()
{
    kDebug() << "threads requested";
    // pdb doesn't support threads.
    InternalPdbCommand* cmd = new InternalPdbCommand(this, "threadsFetched", "pass\n");
    static_cast<DebugSession*>(session())->addCommand(cmd);
}

}

#include "pdbframestackmodel.moc"