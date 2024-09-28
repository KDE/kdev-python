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

Variable::Variable(KDevelop::TreeModel* model, KDevelop::TreeItem* parent, const QString& expression,
                   const QString& display)
    : KDevelop::Variable(model, parent, expression, display)
    , m_pythonPtr(0)
{
    // Copy the namespace id from the parent if possible.
    if (auto* const var = qobject_cast<Python::Variable*>(parent)) {
        m_nsId = var->m_nsId;
    }
}

DebugSession* Variable::session()
{
    IDebugSession* is = ICore::self()->debugController()->currentSession();
    return qobject_cast<DebugSession*>(is);
}

void Variable::attachMaybe(QObject* callback, const char* callbackMethod)
{
    qCDebug(KDEV_PYTHON_VARIABLECONTROLLER) << "Variable::attachMaybe() invoked for" << expression();
    if (callback) {
        // TODO: Needs server support... so for now just reject the request.
        QMetaObject::invokeMethod(callback, callbackMethod, Qt::QueuedConnection, Q_ARG(bool, false));
    }
}

void Variable::fetchValue()
{
    session()->debugger()->request(
        {QStringLiteral("inspectvalue"), int(m_pythonPtr), m_nsId},
        [this, guard = UpdateGuard()](const ResponseData& d) {
            valueFetched(d);
        });
}

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
        [this, guard = UpdateGuard()](const ResponseData& d) {

        const auto fetched = variablesEnumerated(d);
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

        more_ = ellipsis_;
        setHasMore(m_maxItems > childItems.size());

        --m_pendingUpdates;
        if (m_pendingUpdates) {
            QMetaObject::invokeMethod(this, &Variable::tryFetchMoreChildren, Qt::QueuedConnection);
        }
    });
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
        [this, guard = UpdateGuard()](const ResponseData& d) {
        // Process the response.
        const auto fetched = variablesEnumerated(d);
        // Update any added children.
        for (auto* const var : std::as_const(fetched)) {
            var->fetchValue();
        }

        more_ = ellipsis_;
        setHasMore(m_maxItems > childItems.size());

        --m_pendingUpdates;
        if (m_pendingUpdates) {
            QMetaObject::invokeMethod(this, &Variable::tryFetchMoreChildren, Qt::QueuedConnection);
        }
    });
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
    return {new Variable(model_, this, longname, expr), true};
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
