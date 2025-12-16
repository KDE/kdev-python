/*
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>
    SPDX-FileCopyrightText: 2024 Jarmo Tiitto <jarmo.tiitto@gmail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#include "variablecontroller.h"
#include "variable.h"
#include "debugsession.h"
#include <codehelpers.h>
#include <language/duchain/duchainlock.h>
#include <language/duchain/declaration.h>
#include <language/duchain/duchain.h>
#include <interfaces/ilanguagecontroller.h>

#include <debugger/variable/variablecollection.h>
#include <debugger/interfaces/iframestackmodel.h>
#include <interfaces/icore.h>
#include <interfaces/idebugcontroller.h>

#include <QStack>
#include <KMessageBox>
#include <KLocalizedString>

#include <QDebug>
#include <QRegularExpression>
#include "variabledebug.h"

namespace Python {

VariableController::VariableController(KDevelop::IDebugSession* parent)
    : IVariableController(parent)
    , m_collections{Collection{UpdateType::UpdateLocals, variableCollection()->locals(),
                               std::bind(&VariableController::doLocalsUpdate, this), {}},
                    Collection{UpdateType::UpdateReturnInfo, variableCollection()->locals(i18n("Return info")),
                               std::bind(&VariableController::doReturnInfoUpdate, this), {}},
                    Collection{UpdateType::UpdateGlobals, variableCollection()->locals(i18n("Globals")),
                               std::bind(&VariableController::doGlobalsUpdate, this), {}},
                    Collection{UpdateType::UpdateWatches, variableCollection()->watches(),
                               std::bind(&VariableController::doWatchesUpdate, this), {}}}
{
    qCDebug(KDEV_PYTHON_VARIABLECONTROLLER) << "constructing VariableController";

    /*
     * TreeItem::isExpanded() is not an public method and this causes quite a headache. Any custom
     * collection(s) also won't get updated (or created) unless we do this ourselves.
     * To partially work-around this:
     * 1. Connect TreeItem::expanded() signal to a lambda, which sets a flag and calls our updateCollections().
     * 2. Connect TreeItem::collapsed() signal to a lambda, which clears a flag.
     * This allows us to at least attempt updating all collections when user expands
     * them, and skip updating while the collection is collapsed.
     * FIXME: The m_isExpanded can get out-of-sync with what the state of isExpanded() is,
     *        since we have no way to query this and the Locals and Watches can live longer than
     *        VariableController. We may also miss an update when the variable widget is shown/hidden.
     *        (can detect only hiding via autoUpdate() which is useless...)
     */
    for (auto& item : m_collections) {
        auto expander = [&, flag = item.flag]() {
            m_updateRequested |= flag;
            m_isExpanded |= flag;
            updateCollections();
        };
        auto collapser = [&, flag = item.flag]() {
            m_isExpanded &= ~flag;
        };
        // The four argument connect() must be used here or else the connections are not cleaned up
        // when VariableController is destroyed.
        Q_ASSERT(item.collection);
        connect(item.collection, &KDevelop::TreeItem::expanded, this, expander);
        connect(item.collection, &KDevelop::TreeItem::collapsed, this, collapser);

        // The user cannot expand collection without this...
        if (auto* collection = qobject_cast<KDevelop::Locals*>(item.collection)) {
            collection->setHasMore(true);
            /**
             * FIXME: enable this code once KDevelop::Locals::isExpanded() becomes public
            if (collection->isExpanded()) {
                m_isExpanded |= item.flag;
            } else {
                m_isExpanded &= ~item.flag;
            }
            */
        }
    }
}

DebugSession* VariableController::session()
{
    KDevelop::IDebugSession* is = KDevelop::ICore::self()->debugController()->currentSession();
    return qobject_cast<DebugSession*>(is);
}

void VariableController::addWatch(KDevelop::Variable* variable)
{
    variableCollection()->watches()->add(variable->expression());
}

void VariableController::addWatchpoint(KDevelop::Variable* /*variable*/)
{
    qCWarning(KDEV_PYTHON_VARIABLECONTROLLER) << "addWatchpoint requested (not implemented)";
}

KDevelop::Variable* VariableController::createVariable(KDevelop::TreeModel* model, KDevelop::TreeItem* parent, const QString& expression, const QString& display)
{
    // Put the variable into one of the collections:
    // This is propagated up in the tree to account the queued request handlers in each collection.
    if (qobject_cast<KDevelop::Watches*>(parent) || qobject_cast<KDevelop::TooltipRoot*>(parent)) {
        // Tooltips and watches are accounted in the Watches collection.
        return new Variable(model, parent, UpdateGuard::WatchesIndex, expression, display);
    }

    // Parent can only be a Locals TreeItem
    Q_ASSERT(qobject_cast<KDevelop::Locals*>(parent));

    const auto itr = std::find_if(m_collections.cbegin(), m_collections.cend(), [parent](const Collection& c) {
        return c.collection == parent;
    });
    Q_ASSERT(itr != m_collections.end());

    const int collectionIndex = std::distance(m_collections.cbegin(), itr);
    Q_ASSERT(collectionIndex >= UpdateGuard::LocalsIndex);
    Q_ASSERT(collectionIndex < UpdateGuard::WatchesIndex);
    return new Variable(model, parent, collectionIndex, expression, display);
}

KTextEditor::Range VariableController::expressionRangeUnderCursor(KTextEditor::Document* doc, const KTextEditor::Cursor& cursor)
{
    QString prefix;
    using namespace KDevelop;
    DUChainReadLocker lock;
    if ( ! doc->isModified() ) {
        if ( TopDUContext* context = DUChain::self()->chainForDocument(doc->url()) ) {
            DUContext* contextAtCursor = context->findContextAt(CursorInRevision(cursor.line(), cursor.column()));
            if ( contextAtCursor && contextAtCursor->type() == DUContext::Class ) {
                if ( contextAtCursor->owner() && ! contextAtCursor->owner()->identifier().isEmpty() ) {
                    prefix = contextAtCursor->owner()->identifier().toString() + QStringLiteral(".");
                }
            }
        }
    }
    else {
        qCDebug(KDEV_PYTHON_VARIABLECONTROLLER)
            << "duchain unavailable for document" << doc->url() << "or document out of date";
    }

    TextDocumentLazyLineFetcher linefetcher(doc);
    KTextEditor::Cursor startCursor;
    auto text = QString(prefix + CodeHelpers::expressionUnderCursor(linefetcher, cursor, startCursor));
    return {startCursor, startCursor + KTextEditor::Cursor{0, static_cast<int>(text.length())}};
}

void VariableController::update()
{
    // This a stub method. Actual update happens via handleEvent() and updateCollections()
}

void VariableController::handleEvent(KDevelop::IDebugSession::event_t event)
{
    if (!variableCollection())
        return;

    // Sync m_isExpanded from autoUpdate() state.
    m_isExpanded.setFlag(UpdateType::UpdateLocals, autoUpdate() & UpdateType::UpdateLocals);
    m_isExpanded.setFlag(UpdateType::UpdateWatches, autoUpdate() & UpdateType::UpdateWatches);

    // Note: PdbFrameStackModel queues a "selectframe" command after this method. The call to
    // updateCollections() is deferred here to order any commands we may queue after the "selectframe".

    if (event == KDevelop::IDebugSession::program_state_changed) {
        // The program state has expired and so we must re-fetch *everything* again.
        session()->debugger()->request({QStringLiteral("cleanupobjects")}, [](const ResponseData& d) {
            // This handler is just for logging that cleanupobjects is doing its job.
            const auto obj = responseObject(d, QStringLiteral("released"));
            int purged = obj.value(QStringLiteral("purged")).toInt();
            int pinned = obj.value(QStringLiteral("pinned")).toInt();
            qCDebug(KDEV_PYTHON_VARIABLECONTROLLER) << "purged:" << purged << "pinned:" << pinned;
        });

        // Ensure that all other than Locals collection will be updated.
        m_updateRequested = ~UpdateTypes(UpdateLocals);
        m_updateStarted = UpdateType::UpdateNone;
        session()->debugger()->defer([this](const ResponseData&) { updateCollections(); });
        return;
    }

    if (session()->frameStackModel()->currentFrame() == -1 || event != KDevelop::IDebugSession::thread_or_frame_changed)
        return;

    // Invoking IVariableController::handleEvent() doesn't make sense for us:
    // 1. IVariableController::updateIfFrameOrThreadChanged() calls root()->resetChanged() which would throw away
    //    the changed state which has been applied to *all* collections since program_state_changed.
    // 2. updateCollections() already checks all preconditions before doing an update.
    // 3. The collections expanded() and collapsed() signals have been connected to updateCollections().
    if (autoUpdate() & UpdateLocals) {
        m_updateRequested |= UpdateType::UpdateLocals;
    }

    // FIXME: no way to detect when the variable widget is being shown to set all m_updateRequested bits on.
    //        Result: If the variable widget isn't visible when stepping no update may happen until the next
    //        thread_or_frame_changed event or re-expanding an collection item.

    session()->debugger()->defer([this](const ResponseData&) { updateCollections(); });
}

UpdateGuard::UpdateGuard(int index)
    : m_collection(index)
{
    Q_ASSERT(index >= UpdateGuard::LocalsIndex);
    Q_ASSERT(index <= UpdateGuard::WatchesIndex);
    pendingRequests(1);
}

UpdateGuard::UpdateGuard(const UpdateGuard& copy)
    : m_collection(copy.m_collection)
{
    pendingRequests(1);
}

UpdateGuard::~UpdateGuard()
{
    pendingRequests(-1);
}

void UpdateGuard::pendingRequests(int adjust)
{
    if (auto* s = VariableController::session()) {
        if (auto* ctrl = qobject_cast<Python::VariableController*>(s->variableController())) {
            ctrl->pendingRequests(adjust, m_collection);
            return;
        }
    }
    // The debug session is likely exiting due to a bug.
    qCCritical(KDEV_PYTHON_VARIABLECONTROLLER) << "failed to account the number of operations!";
}

void VariableController::pendingRequests(int adjust, int index)
{
    auto& collection = m_collections[index];
    if (adjust > 0) {
        ++collection.pending;
    } else {
        --collection.pending;
    }

    if (collection.pending)
        return;

    // Clear flag on m_updateStarted since it's now safe to update this collection.
    m_updateStarted &= ~collection.flag;

    if (m_updateDeferred & collection.flag) {
        m_updateDeferred &= ~collection.flag;
        m_updateRequested |= collection.flag;
        QMetaObject::invokeMethod(this, &VariableController::updateCollections, Qt::QueuedConnection);
    }
}

void VariableController::fetchFrameLocals(const ResponseData& d)
{
    const auto data = responseObject(d, QStringLiteral("locals"));
    if (data.empty()) {
        qCWarning(KDEV_PYTHON_VARIABLECONTROLLER) << "failed to enumerate stack-frame!";
    }
    // The debugger provides a "namespace id" that must be assigned to all created variables
    // and propagated into all children variables.
    // For frame objects, nsid is the index of the PDB frame object between zero and max frames - 1.
    // (nsid therefore isn't same as kdevframe but is related to it.)
    int nsid = data.value(QStringLiteral("namespace")).toInt();
    int count = data.value(QStringLiteral("count")).toInt();
    PythonId handle = data.value(QStringLiteral("ptr")).toInt();

    qCDebug(KDEV_PYTHON_VARIABLECONTROLLER).noquote() << "enumerating stack-frame:"
        << QStringLiteral("ns_id=%1, count=%2, ptr=%3").arg(nsid).arg(count).arg(handle);

    /**
     * TODO: KDevelop's Locals or Variable classes provide no way to swap out/in a set of children
     * from it such that we could more quickly update it. Perhaps mockingly, Variable::removeSelf() can
     * detach a variable from Locals but there is *no way to insert* a variable back into Locals.
     *
     * Therefore, a better API such as making Locals::insertChild() public or perhaps: QList<
     * TreeItem*> TreeItem::exchangeItems(QList< TreeItem*> newSet) which would replace all of the
     * children in one-go and simply return the previous set of items without deleting any of them.
     * (leaving the possible deletion of items to the caller.) Thus, until such support arrives in
     * KDevelop, the penalty of updating Locals remains rather high:
     *
     * All of the local variables' children are destroyed when the user changes the selected
     * stack-frame to different one, or when more stack-frames become available. The API limitation not
     * only causes us lose how the variables were expanded, but we are forced rebuild the "Locals"
     * collection from scratch each time a switch happens.
     */
    enumerateNamespace(nsid, count, handle, UpdateGuard::LocalsIndex);
}

void VariableController::fetchReturnInfo(const ResponseData& d)
{
    const auto data = responseObject(d, QStringLiteral("returninfo"));
    if (data.empty()) {
        qCWarning(KDEV_PYTHON_VARIABLECONTROLLER) << "failed to get return info!";
    }

    int nsid = data.value(QStringLiteral("namespace")).toInt();
    int count = data.value(QStringLiteral("count")).toInt();
    PythonId handle = data.value(QStringLiteral("ptr")).toInt();

    qCDebug(KDEV_PYTHON_VARIABLECONTROLLER).noquote()
        << "enumerating return info:" << QStringLiteral("ns_id=%1, count=%2, ptr=%3").arg(nsid).arg(count).arg(handle);

    enumerateNamespace(nsid, count, handle, UpdateGuard::ReturnInfoIndex);
}

void VariableController::fetchGlobals(const ResponseData& d)
{
    const auto data = responseObject(d, QStringLiteral("globals"));
    if (data.empty()) {
        qCWarning(KDEV_PYTHON_VARIABLECONTROLLER) << "failed to enumerate globals";
    }
    int nsid = data.value(QStringLiteral("namespace")).toInt();
    int count = data.value(QStringLiteral("count")).toInt();
    PythonId handle = data.value(QStringLiteral("ptr")).toInt();

    qCDebug(KDEV_PYTHON_VARIABLECONTROLLER).noquote()
        << "enumerating globals:" << QStringLiteral("ns_id=%1, count=%2, ptr=%3").arg(nsid).arg(count).arg(handle);

    enumerateNamespace(nsid, count, handle, UpdateGuard::GlobalsIndex);
}

void VariableController::enumerateNamespace(int nsid, int count, PythonId handle, int collection)
{
    auto itr = m_namespaces.find(nsid);
    if (itr == m_namespaces.end()) {
        // Can only be a Locals instance
        Q_ASSERT(qobject_cast<KDevelop::Locals*>(m_collections[collection].collection));
        itr = m_namespaces.emplace(
            nsid,
            QSharedPointer<Namespace>::create(static_cast<KDevelop::Locals*>(m_collections[collection].collection)));
    }
    auto ns = *itr;
    // Reset which variables can be kept.
    for (auto& item : ns->items) {
        item->remove = true;
    }

    // The last argument count + 1 ensures the server will release the enumeration handle.
    session()->debugger()->request({QStringLiteral("enumeratevariables"), int(handle), nsid, count + 1},
        [this, nsid, guard = UpdateGuard(collection)](const ResponseData& d) {
            variablesEnumerated(d, nsid);
    });
}

void VariableController::variablesEnumerated(const ResponseData& d, int nsid)
{
    auto errors = responseValue(d, QStringLiteral("error"));
    if (!errors.isUndefined()) {
        qCWarning(KDEV_PYTHON_VARIABLECONTROLLER) << "enumeratevariables failed:" << errors.toString();
    }

    Q_ASSERT(m_namespaces.contains(nsid));
    auto ns = m_namespaces.find(nsid).value();

    const auto list = responseValue(d, QStringLiteral("variables")).toArray();
    for (auto result : list) {
        if (!result.isObject()) {
            continue;
        }

        const auto obj = result.toObject();
        const auto expression = obj.value(QStringLiteral("expression")).toString();
        auto itr = ns->items.find(expression);
        if (itr == ns->items.end()) {
            itr = ns->items.emplace(expression, ItemPtr::create());
        }

        auto& item = *itr.value();
        item.remove = false;
        item.ptr = obj.value(QStringLiteral("ptr")).toInteger();
    }

    // Drop removed items from ns->names
    for (auto itr = ns->items.begin(); itr != ns->items.end();) {
        if (itr.value()->remove) {
            itr = ns->items.erase(itr);
        } else {
            ++itr;
        }
    }

    qCDebug(KDEV_PYTHON_VARIABLECONTROLLER)
        << "enumeration of ns_id" << nsid << "completed, updating section variables.";

    const auto variables = ns->section->updateLocals(ns->items.keys());

    for (auto* const itr : std::as_const(variables)) {
        Q_ASSERT(qobject_cast<Variable*>(itr));
        auto* const var = static_cast<Variable*>(itr);
        const auto& item = *ns->items[var->expression()];

        if (var->namespaceId() != nsid) {
            // TODO: Can't keep any of the existing variable's children...
            var->deleteChildren();
        }

        var->setId(item.ptr);
        var->setNamespaceId(nsid);
        var->fetchValue();
    }
}

void VariableController::updateCollections()
{
    if (session()->state() != DebugSession::PausedState) {
        // Can't update unless we are in PausedState.
        return;
    }

    // What actually needs to be updated?
    auto updateMask = m_updateRequested & m_isExpanded;

    for (auto& updater : m_collections) {
        if (!(updateMask & updater.flag))
            continue;
        if (updater.pending || (m_updateStarted & updater.flag)) {
            // Defer the update. pendingRequests(-1)
            // will call us again once the pending request count reaches zero.
            m_updateDeferred |= updater.flag;
        } else {
            m_updateStarted |= updater.flag;
            m_updateRequested &= ~updater.flag;
            updater.fn();
        }
    }
}

void VariableController::doLocalsUpdate()
{
    qCDebug(KDEV_PYTHON_VARIABLECONTROLLER) << "starting Locals update";
    session()->debugger()->request({QStringLiteral("framelocals")},
        [this, guard = UpdateGuard(UpdateGuard::LocalsIndex)](const ResponseData& d) {
            fetchFrameLocals(d);
    });
}

void VariableController::doReturnInfoUpdate()
{
    qCDebug(KDEV_PYTHON_VARIABLECONTROLLER) << "starting Return info update";
    session()->debugger()->request({QStringLiteral("getreturninfo")},
        [this, guard = UpdateGuard(UpdateGuard::ReturnInfoIndex)](const ResponseData& d) {
            fetchReturnInfo(d);
    });
}

void VariableController::doGlobalsUpdate()
{
    qCDebug(KDEV_PYTHON_VARIABLECONTROLLER) << "starting Globals update";
    session()->debugger()->request({QStringLiteral("globalobjects")},
        [this, guard = UpdateGuard(UpdateGuard::GlobalsIndex)](const ResponseData& d) {
            fetchGlobals(d);
    });
}

void VariableController::doWatchesUpdate()
{
    qCDebug(KDEV_PYTHON_VARIABLECONTROLLER) << "starting Watches update";
    variableCollection()->watches()->reinstall();
}
}

#include "moc_variablecontroller.cpp"
