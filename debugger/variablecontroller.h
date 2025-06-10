/*
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>
    SPDX-FileCopyrightText: 2024 Jarmo Tiitto <jarmo.tiitto@gmail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef VARIABLECONTROLLER_H
#define VARIABLECONTROLLER_H

#include <QHash>
#include <QList>
#include <QSharedPointer>

#include <debugger/interfaces/idebugsession.h>
#include <debugger/interfaces/ivariablecontroller.h>
#include <util/scopedincrementor.h>

#include "pdbdebuggerinstance.h"

#include <array>

namespace Python {

class DebugSession;
class Variable;
typedef unsigned int PythonId;

class UpdateGuard
{
public:
    UpdateGuard(int collection);
    UpdateGuard(const UpdateGuard&);
    ~UpdateGuard();

private:
    const int m_collection;
    void pendingRequests(int adjust);
};

class VariableController : public KDevelop::IVariableController
{
Q_OBJECT
public:
    VariableController(KDevelop::IDebugSession* parent);
    void addWatch(KDevelop::Variable* variable) override;
    void addWatchpoint(KDevelop::Variable* variable) override;
    
    /**
     * @brief This just calls the Variable constructor and returns a new, empty \a Variable object.
     **/
    KDevelop::Variable* createVariable(KDevelop::TreeModel* model, KDevelop::TreeItem* parent,
                                               const QString& expression, const QString& display = QString()) override;
    
    /**
     * @brief Mini-parser which gives the expression under the cursor.
     * Example: _I_ = cursor
     * self.fo_I_obar(something) # should return "self.foobar"
     * self.foobar(some_I_thing) # should return "something"
     * The expressions returned by this are "print"ed by the debugger, and then displayed in the tooltip.
     * @param doc The document to operate on
     * @param cursor the cursor position
     * @return The expression to print. Should be an (at least syntactically) valid python expression
     **/
    KTextEditor::Range expressionRangeUnderCursor(KTextEditor::Document* doc, const KTextEditor::Cursor& cursor) override;

    /**
     * @brief Update locals and/or watches, as indicated by autoUpdate().
     **/
    void update() override;

    static DebugSession* session();

    enum UpdateFlag { None = 0x0, Locals = 0x1, Watches = 0x2, ReturnInfo = 0x4, Globals = 0x8 };
    Q_DECLARE_FLAGS(UpdateFlags, UpdateFlag)

    /**
     * @brief Before a debugger request is made with an response handler that might modify an
     *        variable, pendingRequests(1) must be called to keep track of the number of such
     *        queued requests. Before the response handler returns, the
     *        pendingRequests(-1) must be called to signal the handler has completed.
     * @param adjust Increment (1) or decrement (-1) the count of queued requests.
     */
    void pendingRequests(int adjust, UpdateFlag collection);

protected:
    void handleEvent(KDevelop::IDebugSession::event_t event) override;

private:
    QList<Variable*> m_watchVariables;

    struct Item
    {
        PythonId ptr = 0;
        bool remove = false;
    };
    using ItemPtr = QSharedPointer<Item>;
    struct Namespace
    {
        QString name;
        QHash<QString, ItemPtr> items;
    };
    QHash<int, QSharedPointer<Namespace>> m_namespaces;

    /// Which collections are expanded? (to best of knowing)
    UpdateFlags m_isExpanded;
    /// Which updates have been requested?
    UpdateFlags m_updateRequested;
    /// Which updates have been started?
    UpdateFlags m_updateStarted;
    /// Which updates have been deferred?
    UpdateFlags m_updateDeferred;

    struct Collection
    {
        const VariableController::UpdateFlags flag;
        KDevelop::TreeItem* collection;
        std::function<void()> fn;
        /// Count of in-flight queued requests on Python::Variable(s)
        KDevelop::NonNegative<> pending;
    };
    // Array of Collections.
    std::array<Collection, 4> m_collections;

    /// Update any variable collections which have m_updateRequested flag set.
    void updateCollections();

    void fetchFrameLocals(const ResponseData& data);
    void fetchReturnInfo(const ResponseData& data);
    void fetchGlobals(const ResponseData& data);
    void enumerateNamespace(int nsid, int count, PythonId handle, UpdateFlag collection, QString name = QString());
    void variablesEnumerated(const ResponseData& data, int nsid);

    void doLocalsUpdate();
    void doReturnInfoUpdate();
    void doGlobalsUpdate();
    void doWatchesUpdate();
};

Q_DECLARE_OPERATORS_FOR_FLAGS(VariableController::UpdateFlags)
}

#endif // VARIABLECONTROLLER_H
