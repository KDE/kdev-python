/*
    SPDX-FileCopyrightText: 2013 Sven Brauch <svenbrauch@gmail.com>

    SPDX-License-Identifier: GPL-2.0-only OR GPL-3.0-only OR LicenseRef-KDE-Accepted-GPL
*/

#include "correctionhelper.h"
#include "helpers.h"
#include "declarationbuilder.h"

#include <language/duchain/duchain.h>
#include <language/duchain/duchainlock.h>
#include <language/duchain/declaration.h>

#include <QDebug>
#include "duchaindebug.h"


#include <QFile>

using namespace KDevelop;

namespace Python {

CorrectionHelper::CorrectionHelper(const IndexedString& _url, DeclarationBuilder* builder)
{
    m_contextStack.push(nullptr);
    auto absolutePath = Helper::getCorrectionFile(_url.toUrl());

    if ( !absolutePath.isValid() || absolutePath.isEmpty() || ! QFile::exists(absolutePath.path()) ) {
        return;
    }
    qCDebug(KDEV_PYTHON_DUCHAIN) << "Found correction file for " << _url.str() << ": " << absolutePath.path();

    const IndexedString indexedPath(absolutePath);
    DUChainReadLocker lock;
    m_hintTopContext = DUChain::self()->chainForDocument(indexedPath);
    qCDebug(KDEV_PYTHON_DUCHAIN) << "got top context for" << absolutePath << m_hintTopContext;
    m_contextStack.top() = m_hintTopContext.data();
    if ( ! m_hintTopContext ) {
        // The file exists, but was not parsed yet. Schedule it, and re-schedule the current one too.
        Helper::scheduleDependency(indexedPath, builder->jobPriority());
        builder->addUnresolvedImport(indexedPath);
    }
}

CorrectionHelper::~CorrectionHelper()
{
    Q_ASSERT(m_contextStack.size() == 1);
    Q_ASSERT(m_contextStack.top() == m_hintTopContext.data());
}

void CorrectionHelper::enter(const KDevelop::Identifier& identifier)
{
    DUContext* current = m_contextStack.top();
    if ( ! current ) {
        // no hints for the parent object, so no hints for its children either
        m_contextStack.push(nullptr);
        return;
    }

    DUChainReadLocker lock;
    const QList<Declaration*> decls = current->findDeclarations(identifier);
    if ( decls.isEmpty() ) {
        // no hints for the current object
        m_contextStack.push(nullptr);
        return;
    }

    qCDebug(KDEV_PYTHON_DUCHAIN) << "Looking in " << identifier.toString();
    // there's a hint declaration for this object, put it on the stack
    DUContext* internal = decls.first()->internalContext();
    m_contextStack.push(internal);
    return;
}

AbstractType::Ptr CorrectionHelper::hintForLocal(const QString &local) const
{
    return hintFor(KDevelop::Identifier(QLatin1String("l_") + local));
}

AbstractType::Ptr CorrectionHelper::returnTypeHint() const
{
    return hintFor(KDevelop::Identifier(QLatin1String("returns")));
}

AbstractType::Ptr CorrectionHelper::hintFor(const KDevelop::Identifier &identifier) const
{
    DUContext* current = m_contextStack.top();
    AbstractType::Ptr hint;
    if ( ! current ) {
        return hint;
    }
    const QList<Declaration*> decls = current->findDeclarations(identifier);
    if ( decls.isEmpty() ) {
        return hint;
    }

    qCDebug(KDEV_PYTHON_DUCHAIN) << "Found specified correct type for " << identifier.toString() << decls.first()->abstractType()->toString();
    return decls.first()->abstractType();
}


CorrectionHelper::Recursion CorrectionHelper::enterClass(const QString& identifier)
{
    enter(KDevelop::Identifier(QLatin1String("class_") + identifier));
    return CorrectionHelper::Recursion(this);
}

CorrectionHelper::Recursion CorrectionHelper::enterFunction(const QString &identifier)
{
    enter(KDevelop::Identifier(QLatin1String("function_") + identifier));
    return CorrectionHelper::Recursion(this);
}

void CorrectionHelper::leave()
{
    m_contextStack.pop();
}

}
