/*
    This file is part of kdev-python, the python language plugin for KDevelop
    Copyright (C) 2012  Sven Brauch <svenbrauch@googlemail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
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
public slots:
    void framesFetched(QByteArray frames);
    void threadsFetched(QByteArray threads);
private:
    int m_debuggerAtFrame;
};

}

#endif // PDBFRAMESTACKMODEL_H
