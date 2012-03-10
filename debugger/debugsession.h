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


#ifndef PDBDEBUGSESSION_H
#define PDBDEBUGSESSION_H

#include </home/sven/install/include/kdevplatform/debugger/interfaces/idebugsession.h>


class DebugSession : public KDevelop::IDebugSession
{

protected:
    virtual KDevelop::IFrameStackModel* createFrameStackModel();

public:
    virtual void stepOut();
    virtual void stepOverInstruction();
    virtual void stepInto();
    virtual void stepIntoInstruction();
    virtual void stepOver();
    virtual void jumpToCursor();
    virtual void runToCursor();
    virtual void run();
    virtual void interruptDebugger();
    virtual void stopDebugger();
    virtual void restartDebugger();
    virtual bool restartAvaliable() const;
    virtual KDevelop::IDebugSession::DebuggerState state() const;
};

#endif // DEBUGSESSION_H
