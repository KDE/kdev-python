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


#ifndef PDBFRAMESTACKMODEL_H
#define PDBFRAMESTACKMODEL_H

#include <debugger/framestack/framestackmodel.h>

using namespace KDevelop;

namespace Python {

class PdbFrameStackModel : public KDevelop::FrameStackModel
{
Q_OBJECT
public:
    PdbFrameStackModel(IDebugSession* session);
    virtual void fetchFrames(int threadNumber, int from, int to);
    virtual void fetchThreads();
public slots:
    void framesFetched(QByteArray frames);
    void threadsFetched(QByteArray threads);
};

}

#endif // PDBFRAMESTACKMODEL_H
