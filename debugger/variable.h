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


#ifndef VARIABLE_H
#define VARIABLE_H

#include <debugger/variable/variablecollection.h>

namespace Python {

class Variable : public KDevelop::Variable
{
Q_OBJECT
public:
    Variable(KDevelop::TreeModel* model, TreeItem* parent, const QString& expression, const QString& display = "");
    
    /**
     * @brief Fetch this variable's value, and notify callback::callbackMethod when done.
     *
     * @param callback Object to notify. Skipped if 0. Defaults to 0.
     * @param callbackMethod Method to call. Skipped if 0. Defaults to 0.
     **/
    virtual void attachMaybe(QObject* callback = 0, const char* callbackMethod = 0);
    
    /**
     * @brief Fetches children (list items, object attributes...) for this variable.
     * TODO: Should fetch more children, it currently simply fetches all children which is not so good
     * if there's 20.000 of them
     * This is invoked if the user clicks the "expand" icon in any variable tree view
     **/
    virtual void fetchMoreChildren();
    
    QObject* m_notifyCreated;
    const char* m_notifyCreatedMethod;
public slots:
    /**
     * @brief Parse the debugger output and update this variable's value.
     **/
    void dataFetched(QByteArray rawData);
    /**
     * @brief Parse the debugger output and add children to this variable.
     **/
    void moreChildrenFetched(QByteArray rawData);
};

}

#endif // VARIABLE_H
