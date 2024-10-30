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
#include <QStack>
#include <KMessageBox>
#include <KLocalizedString>

#include <QDebug>
#include <QRegularExpression>
#include "variabledebug.h"

namespace Python {

struct CollectionInit
{
    VariableController::UpdateFlags flag;
    KDevelop::TreeItem* collection;
};

VariableController::VariableController(IDebugSession* parent) : IVariableController(parent)
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
    std::array<CollectionInit, 3> collections = {
        CollectionInit{UpdateFlag::Locals, variableCollection()->locals()},
        CollectionInit{UpdateFlag::Watches, variableCollection()->watches()},
        CollectionInit{UpdateFlag::ReturnInfo, variableCollection()->locals(i18n("Return info"))}
    };

    for (auto& item : collections) {
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
        connect(item.collection, &TreeItem::expanded, this, expander);
        connect(item.collection, &TreeItem::collapsed, this, collapser);

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
    IDebugSession* is = ICore::self()->debugController()->currentSession();
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
    return new Variable(model, parent, expression, display);
}

KTextEditor::Range VariableController::expressionRangeUnderCursor(KTextEditor::Document* doc, const KTextEditor::Cursor& cursor)
{
    QString prefix;
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

void VariableController::handleEvent(IDebugSession::event_t event)
{
    if (!variableCollection())
        return;

    // Sync m_isExpanded from autoUpdate() state.
    m_isExpanded.setFlag(UpdateFlag::Locals, autoUpdate() & UpdateType::UpdateLocals);
    m_isExpanded.setFlag(UpdateFlag::Watches, autoUpdate() & UpdateType::UpdateWatches);

    // Note: PdbFrameStackModel queues a "selectframe" command after this method. The call to
    // updateCollections() is deferred here to order any commands we may queue after the "selectframe".

    if (event == IDebugSession::program_state_changed) {
        // The program state has expired and so we must re-fetch *everything* again.
        session()->debugger()->request({QStringLiteral("cleanupobjects")}, [](const ResponseData& d) {
            // This handler is just for logging that cleanupobjects is doing its job.
            const auto obj = responseObject(d, QStringLiteral("released"));
            int purged = obj.value(QStringLiteral("purged")).toInt();
            int pinned = obj.value(QStringLiteral("pinned")).toInt();
            qCDebug(KDEV_PYTHON_VARIABLECONTROLLER) << "purged:" << purged << "pinned:" << pinned;
        });

        // Ensure that all other than Locals collection will be updated.
        m_updateRequested = ~UpdateFlags(Locals);
        m_updateStarted = UpdateFlag::None;
        session()->debugger()->defer([this](const ResponseData&) { updateCollections(); });
        return;
    }

    if (session()->frameStackModel()->currentFrame() == -1 || event != IDebugSession::thread_or_frame_changed)
        return;

    // Invoking IVariableController::handleEvent() doesn't make sense for us:
    // 1. IVariableController::updateIfFrameOrThreadChanged() calls root()->resetChanged() which would throw away
    //    the changed state which has been applied to *all* collections since program_state_changed.
    // 2. updateCollections() already checks all preconditions before doing an update.
    // 3. The collections expanded() and collapsed() signals have been connected to updateCollections().
    if (autoUpdate() & UpdateLocals) {
        m_updateRequested |= UpdateFlag::Locals;
    }

    // FIXME: no way to detect when the variable widget is being shown to set all m_updateRequested bits on.
    //        Result: If the variable widget isn't visible when stepping no update may happen until the next
    //        thread_or_frame_changed event or re-expanding an collection item.

    session()->debugger()->defer([this](const ResponseData&) { updateCollections(); });
}

UpdateGuard::UpdateGuard()
{
    pendingRequests(1);
}

UpdateGuard::UpdateGuard(const UpdateGuard&)
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
            ctrl->pendingRequests(adjust);
            return;
        }
    }
    qCCritical(KDEV_PYTHON_VARIABLECONTROLLER) << "failed to account the number of operations!";
    Q_ASSERT(false);
}

void VariableController::pendingRequests(int adjust)
{
    if (adjust > 0) {
        ++m_pendingRequests;
    } else {
        --m_pendingRequests;
    }

    if (m_pendingRequests)
        return;

    // Clear UpdateFlag::Locals on m_updateStarted since it's now safe to update this collection.
    m_updateStarted.setFlag(Locals, false);

    if (m_localsUpdateDeferred) {
        // Deferred update of "Locals" requested.
        m_localsUpdateDeferred = false;
        m_updateRequested.setFlag(Locals);
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
    enumerateNamespace(nsid, count, handle, i18n("Locals"));
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

    enumerateNamespace(nsid, count, handle, i18n("Return info"));
}

void VariableController::enumerateNamespace(int nsid, int count, PythonId handle, QString name)
{
    auto itr = m_namespaces.find(nsid);
    if (itr == m_namespaces.end()) {
        itr = m_namespaces.emplace(nsid, QSharedPointer<Namespace>::create());
    }
    auto ns = *itr;
    ns->name = name;
    // Reset which variables can be kept.
    for (auto& item : ns->items) {
        item->remove = true;
    }

    // The last argument count + 1 ensures the server will release the enumeration handle.
    session()->debugger()->request({QStringLiteral("enumeratevariables"), int(handle), nsid, count + 1},
        [this, nsid, guard = UpdateGuard()](const ResponseData& d) {
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
        << "enumeration of ns_id" << nsid << "completed, updating" << ns->name << "variables.";

    auto* collection = variableCollection()->locals(ns->name);
    const auto variables = collection->updateLocals(ns->items.keys());

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

    /*
     * Update "Locals" collection. For this case, we must prevent starting the update
     * until the previous update on "Locals" has completed. (The user can switch the selected
     * stack-frame before the last update as fully completed.)
     */
    if (updateMask & UpdateFlag::Locals) {
        if (m_pendingRequests || (m_updateStarted & UpdateFlag::Locals)) {
            // Can't update yet...
            // TODO: Unfortunately the "Locals" update can get arbitrarily delayed more that I
            // would want to, since all other collection updates also increment
            // m_pendingRequests. The UpdateGuard should perhaps be improved such that each
            // collection has its own VariableController::m_pendingRequests counter. Which
            // collection a variable is part of would need to be propagated up in the tree.
            qCDebug(KDEV_PYTHON_VARIABLECONTROLLER) << "deferring Locals update...";
            m_localsUpdateDeferred = true;
        } else {
            // m_updateStarted|UpdateFlag::Locals is cleared by pendingRequests(-1) when
            // m_pendingRequests reaches zero.
            m_updateStarted |= UpdateFlag::Locals;
            m_updateRequested.setFlag(UpdateFlag::Locals, false);
            qCDebug(KDEV_PYTHON_VARIABLECONTROLLER) << "starting Locals update";

            session()->debugger()->request({QStringLiteral("framelocals")},
                [this, guard = UpdateGuard()](const ResponseData& d) {
                    fetchFrameLocals(d);
            });
        }
    }

    // Update "Fixed" collections.
    // These collections are updated at most once per program_state_changed event.

    // Update our return info.
    if ((updateMask & UpdateFlag::ReturnInfo) && !(m_updateStarted & UpdateFlag::ReturnInfo)) {
        m_updateStarted |= UpdateFlag::ReturnInfo;
        m_updateRequested.setFlag(UpdateFlag::ReturnInfo, false);
        qCDebug(KDEV_PYTHON_VARIABLECONTROLLER) << "starting Return info update";

        session()->debugger()->request({QStringLiteral("getreturninfo")},
            [this, guard = UpdateGuard()](const ResponseData& d) {
                fetchReturnInfo(d);
        });
    }

    // Update watches.
    if ((updateMask & UpdateFlag::Watches) && !(m_updateStarted & UpdateFlag::Watches)) {
        m_updateStarted |= UpdateFlag::Watches;
        m_updateRequested.setFlag(UpdateFlag::Watches, false);
        qCDebug(KDEV_PYTHON_VARIABLECONTROLLER) << "starting Watches update";

        variableCollection()->watches()->reinstall();
    }
}
}

#include "moc_variablecontroller.cpp"
