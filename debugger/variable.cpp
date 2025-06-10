/*
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>
    SPDX-FileCopyrightText: 2024 Jarmo Tiitto <jarmo.tiitto@gmail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#include "variable.h"
#include "variablecontroller.h"
#include "debugsession.h"
#include <interfaces/icore.h>

#include <QDebug>
#include "variabledebug.h"

namespace Python {

class VariableRequestHandler
{
    UpdateGuard m_guard;
    QPointer<Variable> m_holder;

public:
    VariableRequestHandler(Variable* var)
        : m_guard(var->collection())
        , m_holder(var)
    {
    }
    virtual ~VariableRequestHandler()
    {
    }

    void operator()(const ResponseData& d)
    {
        auto* const var = m_holder.data();
        if (!var) {
            cleanup(d);
        } else {
            process(*var, d);
        }
    }
    virtual void process(Variable& self, const ResponseData& d) = 0;
    virtual void cleanup(const ResponseData& d)
    {
        qCWarning(KDEV_PYTHON_VARIABLECONTROLLER) << "Variable was deleted before its update completed";
    }
};

Variable::Variable(KDevelop::TreeModel* model, KDevelop::TreeItem* parent, int collection, const QString& expression,
                   const QString& display)
    : KDevelop::Variable(model, parent, expression, display)
    , m_collection(collection)
{
    // Copy the namespace id from the parent if possible.
    if (auto* const var = qobject_cast<Python::Variable*>(parent)) {
        m_nsId = var->m_nsId;
    }
}

Variable::~Variable()
{
    if (!ICore::self() || !ICore::self()->debugController())
        return;
    if (m_is_watch && namespaceId() < -2) {
        session()->debugger()->request({QStringLiteral("dropnamespace"), namespaceId()});
    }
}

DebugSession* Variable::session()
{
    IDebugSession* is = ICore::self()->debugController()->currentSession();
    return qobject_cast<DebugSession*>(is);
}

class EvalHandler : public VariableRequestHandler
{
    QObject* m_context;
    const char* m_callback;

public:
    EvalHandler(Variable* self, QObject* context, const char* callback)
        : VariableRequestHandler(self)
        , m_context(context)
        , m_callback(callback)
    {
    }

    void process(Variable& self, const ResponseData& d) override
    {
        self.attachDone(d, m_context, m_callback);
    }

    void cleanup(const ResponseData& d) override
    {
        // var got deleted...
        qCDebug(KDEV_PYTHON_VARIABLECONTROLLER) << "attachMaybe() was aborted";
        // Release the namespace id if it was assigned.
        const auto result = responseObject(d, QStringLiteral("evaluate"));
        const auto ns_id = result.value(QStringLiteral("namespace")).toInt();
        if (ns_id < -2) {
            Variable::session()->debugger()->request({QStringLiteral("dropnamespace"), ns_id});
        }
    }
};

void Variable::attachMaybe(QObject* context, const char* callback)
{
    if (auto* s = session(); !s || s->state() != DebugSession::PausedState) {
        // KDevelop can call this function even if the inferior is running, so just don't.
        if (context) {
            QMetaObject::invokeMethod(context, callback, Qt::QueuedConnection, Q_ARG(bool, false));
        }
        return;
    }

    qCDebug(KDEV_PYTHON_VARIABLECONTROLLER) << "search for:" << expression();

    // FIXME: expression() can be from an expanded tooltip that contains "foo/[0]"
    //        This does not work since "foo/[0]" is syntactically wrong.

    m_is_watch = true;
    session()->debugger()->request(
        {QStringLiteral("evalexpression"), QStringLiteral("'%1'").arg(expression()), namespaceId()},
        EvalHandler(this, context, callback));
}

void Variable::attachDone(const ResponseData& d, QObject* context, const char* callback)
{
    const auto result = responseObject(d, QStringLiteral("evaluate"));
    const auto ns_id = result.value(QStringLiteral("namespace")).toInt();
    const auto inscope = result.value(QStringLiteral("inscope")).toBool();
    if (!ns_id) {
        qCDebug(KDEV_PYTHON_VARIABLECONTROLLER) << "failed to lookup:" << expression();
        if (context) {
            QMetaObject::invokeMethod(context, callback, Qt::QueuedConnection, Q_ARG(bool, false));
        }
        return;
    }

    setNamespaceId(ns_id);
    setInScope(inscope);

    if (!inscope) {
        // The server accepted the ns_id but there is no value available.
        if (context) {
            QMetaObject::invokeMethod(context, callback, Qt::QueuedConnection, Q_ARG(bool, true));
        }
        return;
    }

    // Process the "enumeratevariables" response.
    const auto var = responseObject(d, QStringLiteral("variable"));
    const PythonId ptr = var.value(QStringLiteral("ptr")).toInt();
    setId(ptr);
    // Process the 'inspect' response.
    valueFetched(d);

    if (context) {
        QMetaObject::invokeMethod(context, callback, Qt::QueuedConnection, Q_ARG(bool, true));
    }
}

class FetchHandler : public VariableRequestHandler
{
public:
    FetchHandler(Variable* self)
        : VariableRequestHandler(self)
    {
    }
    void process(Variable& self, const ResponseData& d) override
    {
        self.valueFetched(d);
    }
};

void Variable::fetchValue()
{
    session()->debugger()->request({QStringLiteral("inspectvalue"), int(m_pythonPtr), m_nsId}, FetchHandler(this));
}

class EnumerateHandler : public VariableRequestHandler
{
public:
    EnumerateHandler(Variable* self)
        : VariableRequestHandler(self)
    {
    }
    void process(Variable& self, const ResponseData& d) override
    {
        const auto fetched = self.variablesEnumerated(d);
        self.enumerateDone(fetched);
    }
};

void Variable::valueFetched(const ResponseData& d)
{
    auto errors = responseValue(d, QStringLiteral("error"));
    if (!errors.isUndefined()) {
        qCWarning(KDEV_PYTHON_VARIABLECONTROLLER) << "inspectvalue failed:" << errors.toString();
        return;
    }

    const auto result = responseObject(d, QStringLiteral("inspect"));
    if (result.empty()) {
        // failed.
        more_ = ellipsis_;
        deleteChildren();
        setValue(QString());
        setType(QString());
        return;
    }

    bool firstInit = m_maxItems == -1;
    m_maxItems = result.value(QStringLiteral("count")).toInt();
    m_expandBy = qMin(result.value(QStringLiteral("expandhint")).toInt(1), m_maxItems);

    QString data;
    if (result.contains(QStringLiteral("data"))) {
        data = result.value(QStringLiteral("data")).toString();
    }
    if (result.contains(QStringLiteral("len"))) {
        const int len = result.value(QStringLiteral("len")).toInt();
        if (data.isEmpty()) {
            data = QStringLiteral("len=%1").arg(len);
        } else {
            data = QStringLiteral("len=%1, %2").arg(len).arg(data);
        }
    }

    bool changed = result.value(QStringLiteral("changed")).toBool();
    bool report = changed != isChanged();
    if (value() != data) {
        itemData[VariableCollection::ValueColumn] = data;
        report = true;
    }

    const auto typeident = result.value(QStringLiteral("type")).toString();
    if (type() != typeident) {
        itemData[VariableCollection::TypeColumn] = typeident;
        report = true;
    }

    if (report) {
        // This assumes setChange() unconditionally calls reportChange().
        // Thus, this updates all of value(), type() and isChanged() in one go.
        setChanged(changed);
    }

    qCDebug(KDEV_PYTHON_VARIABLECONTROLLER) << expression() << "children:" << childItems.size() << "->" << m_maxItems
                                            << "type:" << typeident << "data:" << data << "changed:" << changed;

    if (!m_maxItems) {
        // No children.
        more_ = ellipsis_;
        deleteChildren();
    }

    if (firstInit || childItems.empty()) {
        // How setHasMoreInitial() should be used is beyond me...
        more_ = ellipsis_;
        setHasMore(m_maxItems);
        // No need to update existing children.
        return;
    }

    Q_ASSERT(!m_pendingUpdates);
    ++m_pendingUpdates;
    // Update all existing children.
    const auto count = qMin(m_maxItems, childItems.size());
    session()->debugger()->request({QStringLiteral("enumeratevariables"), int(m_pythonPtr), m_nsId, count},
                                   EnumerateHandler(this));
}

void Variable::enumerateDone(const QList<Variable*>& fetched)
{
    // var->die() modifies childItems...
    const auto list = childItems;
    for (auto* const item : std::as_const(list)) {
        Q_ASSERT(qobject_cast<Variable*>(item));
        auto* var = static_cast<Variable*>(item);

        if (fetched.contains(var)) {
            var->fetchValue();
        } else {
            qCDebug(KDEV_PYTHON_VARIABLECONTROLLER) << "removing:" << var->expression();
            Q_ASSERT(!var->m_pendingUpdates);
            var->die();
        }
    }

    updateHasMore();
}

void Variable::updateHasMore()
{
    more_ = ellipsis_;
    setHasMore(m_maxItems > childItems.size());

    --m_pendingUpdates;
    if (m_pendingUpdates) {
        QMetaObject::invokeMethod(this, &Variable::tryFetchMoreChildren, Qt::QueuedConnection);
    }
}

void Variable::fetchMoreChildren()
{
    if (m_pendingUpdates) {
        // The user attempted this action before the last update had completed...
        ++m_pendingUpdates;
        return;
    }
    ++m_pendingUpdates;
    tryFetchMoreChildren();
}

class FetchMoreHandler : public VariableRequestHandler
{
public:
    FetchMoreHandler(Variable* self)
        : VariableRequestHandler(self)
    {
    }

    void process(Variable& self, const ResponseData& d) override
    {
        // Process the response.
        const auto fetched = self.variablesEnumerated(d);
        // Update any added children.
        for (auto* const var : std::as_const(fetched)) {
            var->fetchValue();
        }

        self.updateHasMore();
    }
};

void Variable::tryFetchMoreChildren()
{
    Q_ASSERT(m_pendingUpdates);
    if (m_maxItems <= 0 || childItems.size() >= m_maxItems) {
        --m_pendingUpdates;
        return;
    }

    qCDebug(KDEV_PYTHON_VARIABLECONTROLLER) << "expand" << expression();

    // Enumerate more of the variable's children.
    // (The server continues the enumeration from the last point, so count is relative)
    const auto count = qMin(m_expandBy, m_maxItems - childItems.size());
    session()->debugger()->request({QStringLiteral("enumeratevariables"), int(m_pythonPtr), m_nsId, count},
                                   FetchMoreHandler(this));
}

std::pair<Variable*, bool> Variable::findOrCreateChild(QString longname, QString expr)
{
    for (auto* const item : std::as_const(childItems)) {
        Q_ASSERT(qobject_cast<Variable*>(item));
        auto* const var = static_cast<Variable*>(item);
        if (var->expression() == longname) {
            return {var, false};
        }
    }
    return {new Variable(model_, this, m_collection, longname, expr), true};
}

QList<Variable*> Variable::variablesEnumerated(const ResponseData& d)
{
    QList<Variable*> fetched;
    auto errors = responseValue(d, QStringLiteral("error"));
    if (!errors.isUndefined()) {
        qCWarning(KDEV_PYTHON_VARIABLECONTROLLER) << "fetching a children failed:" << errors.toString();
        return fetched;
    }

    const auto list = responseValue(d, QStringLiteral("variables")).toArray();
    for (auto& result : std::as_const(list)) {
        if (!result.isObject()) {
            // All children fetched.
            return fetched;
        }
        const auto obj = result.toObject();
        const auto expr = obj.value(QStringLiteral("expression")).toString();
        // longname can contain dots so using '/' enables splitting the longname to its components
        // if a such need arises. This also follows how kdevpdbvariablesupport.py: _enumerateHandle()
        // generates the longnames.
        const QString longname = expression() + QLatin1Char('/') + expr;
        const PythonId ptr = obj.value(QStringLiteral("ptr")).toInt();

        auto [var, isnew] = findOrCreateChild(longname, expr);
        fetched.emplace_back(var);
        var->setId(ptr);
        // the child must originate from the same namespace as this.
        Q_ASSERT(var->namespaceId() == m_nsId);

        if (isnew) {
            insertChild(childItems.size(), var);
        }
    }
    return fetched;
}
}

#include "moc_variable.cpp"
