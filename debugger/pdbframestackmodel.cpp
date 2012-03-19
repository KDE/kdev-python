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

using namespace KDevelop;

namespace Python {
    
PdbFrameStackModel::PdbFrameStackModel(IDebugSession* session): FrameStackModel(session)
{
    
}

void PdbFrameStackModel::fetchFrames(int threadNumber, int from, int to)
{
    QList<FrameItem> frames;
    FrameItem testFrame;
    testFrame.file = "test.py";
    testFrame.line = 3;
    testFrame.name = "foo";
    frames << testFrame;
    setFrames(0, frames);
}

void PdbFrameStackModel::fetchThreads()
{
    QList<ThreadItem> threads;
    ThreadItem testThread;
    testThread.nr = 0;
    testThread.name = "test thread";
    threads << testThread;
    setThreads(threads);
}

}