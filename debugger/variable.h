/*
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef VARIABLE_H
#define VARIABLE_H

#include <debugger/variable/variablecollection.h>

namespace Python {

class Variable : public KDevelop::Variable
{
Q_OBJECT
public:
    Variable(KDevelop::TreeModel* model, TreeItem* parent, const QString& expression, const QString& display = QString());
    
    /**
     * @brief Fetch this variable's value, and notify callback::callbackMethod when done.
     *
     * @param callback Object to notify. Skipped if 0. Defaults to 0.
     * @param callbackMethod Method to call. Skipped if 0. Defaults to 0.
     **/
    void attachMaybe(QObject* callback = nullptr, const char* callbackMethod = nullptr) override;
    
    /**
     * @brief Fetches children (list items, object attributes...) for this variable.
     * TODO: Should fetch more children, it currently simply fetches all children which is not so good
     * if there's 20.000 of them
     * This is invoked if the user clicks the "expand" icon in any variable tree view
     **/
    void fetchMoreChildren() override;
    
    QObject* m_notifyCreated;
    const char* m_notifyCreatedMethod;
public Q_SLOTS:
    /**
     * @brief Parse the debugger output and update this variable's value.
     **/
    void dataFetched(QByteArray rawData);
    /**
     * @brief Parse the debugger output and add children to this variable.
     **/
    void moreChildrenFetched(QByteArray rawData);
    /**
     * @brief Set this object's python ID
     **/
    void setId(long unsigned int id);
private:
    /// A unique ID of the python object pointed to by this variable.
    unsigned long int m_pythonPtr;
};

}

#endif // VARIABLE_H
