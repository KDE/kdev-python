/*
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>
    SPDX-FileCopyrightText: 2024 Jarmo Tiitto <jarmo.tiitto@gmail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef VARIABLE_H
#define VARIABLE_H

#include <QList>
#include <QPointer>

#include <debugger/variable/variablecollection.h>

#include "pdbdebuggerinstance.h"

namespace Python {

class DebugSession;

/// A unsigned integer large enough to hold a handle.
typedef unsigned int PythonId;

class Variable : public KDevelop::Variable
{
Q_OBJECT
public:
    /**
     * Construct a variable.
     * @note If possible, the namespaceId() is inherited from @p parent.
     */
    Variable(KDevelop::TreeModel* model, TreeItem* parent, int collection, const QString& expression,
             const QString& display = QString());

    ~Variable();

    /**
     * @brief Fetch this variable's value, and notify callback::callbackMethod when done.
     *
     * @param callback Object to notify. Skipped if 0. Defaults to 0.
     * @param callbackMethod Method to call. Skipped if 0. Defaults to 0.
     **/
    void attachMaybe(QObject* callback = nullptr, const char* callbackMethod = nullptr) override;
    
    /**
     * @brief Fetches more children (list items, object attributes...) for this variable.
     * This is invoked if the user clicks the "expand" icon in any variable tree view.
     **/
    void fetchMoreChildren() override;

    static DebugSession* session();

    /**
     * @brief Fetch this variable's value.
     */
    void fetchValue();

    /**
     * @brief Set this object's python ID.
     **/
    void setId(PythonId id)
    {
        m_pythonPtr = id;
    }
    PythonId id() const
    {
        return m_pythonPtr;
    }

    /**
     * @brief Set this object's "namespace id".
     **/
    void setNamespaceId(int nsid)
    {
        m_nsId = nsid;
    }
    int namespaceId() const
    {
        return m_nsId;
    }
    /// Collection index of this variable.
    int collection()
    {
        return m_collection;
    }

private Q_SLOTS:
    /**
     * Try fetch more children.
     * @note m_pendingUpdates must be incremented before calling this.
     */
    void tryFetchMoreChildren();

private:
    /// Which collection this variable is part of? ("Locals", "Globals", "Watches" or "Return info")
    const int m_collection;
    /// A unique ID of the python object associated with this variable.
    PythonId m_pythonPtr = 0;
    /// To what namespace this variable is bound to?
    int m_nsId = -1;
    /// Number of items to expand by
    int m_expandBy = 1;
    /// Count of possible children.
    int m_maxItems = -1;
    /// Account deferred fetchMoreChildren() calls.
    int m_pendingUpdates = 0;
    /// True, if this is a watch root variable.
    bool m_is_watch = false;

    /**
     * Try insert a new child or return an existing child.
     */
    std::pair<Variable*, bool> findOrCreateChild(QString longname, QString expr);

public:
    void valueFetched(const ResponseData& data);
    QList<Variable*> variablesEnumerated(const ResponseData& data);
    void enumerateDone(const QList<Variable*>& fetched);
    void updateHasMore();
    void attachDone(const ResponseData& d, QObject* object, const char* method);
};

}

#endif // VARIABLE_H
