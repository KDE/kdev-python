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


#include "variable.h"
#include "debugsession.h"
#include <interfaces/icore.h>

namespace Python {

Variable::Variable(KDevelop::TreeModel* model, KDevelop::TreeItem* parent, const QString& expression, const QString& display):
    KDevelop::Variable(model, parent, expression, display)
{

}

void Variable::attachMaybe(QObject* callback, const char* callbackMethod)
{
    IDebugSession* is = ICore::self()->debugController()->currentSession();
    DebugSession* s = static_cast<DebugSession*>(is);
    s->createVariable(this, callback, callbackMethod);
}

void Variable::fetchMoreChildren()
{

}

}

