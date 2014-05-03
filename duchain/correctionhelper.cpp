/*
 * This file is part of kdev-python, the Python language support plugin for KDevelop
 * Copyright 2013  Sven Brauch <svenbrauch@gmail.com>
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License as
 * published by the Free Software Foundation; either version 2 of
 * the License or (at your option) version 3 or any later version
 * accepted by the membership of KDE e.V. (or its successor approved
 * by the membership of KDE e.V.), which shall act as a proxy
 * defined in Section 14 of version 3 of the license.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 */

#include "correctionhelper.h"
#include "helpers.h"
#include "declarationbuilder.h"

#include <language/duchain/duchain.h>
#include <language/duchain/duchainlock.h>
#include <language/duchain/declaration.h>

#include <KStandardDirs>
#include <QFile>

using namespace KDevelop;

namespace Python {

CorrectionHelper::CorrectionHelper(const IndexedString& _url, DeclarationBuilder* builder)
{
    m_contextStack.push(0);
    KUrl absolutePath = Helper::getCorrectionFile(_url.toUrl());

    if ( !absolutePath.isValid() || absolutePath.isEmpty() || ! QFile::exists(absolutePath.path()) ) {
        return;
    }
    kDebug() << "Found correction file for " << _url.str() << ": " << absolutePath.path();

    const IndexedString indexedPath(absolutePath);
    DUChainReadLocker lock;
    m_hintTopContext = DUChain::self()->chainForDocument(indexedPath);
    kDebug() << "got top context for" << absolutePath << m_hintTopContext;
    m_contextStack.top() = m_hintTopContext.data();
    if ( ! m_hintTopContext ) {
        // The file exists, but was not parsed yet. Schedule it, and re-schedule the current one too.
        Helper::scheduleDependency(indexedPath, builder->m_ownPriority);
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
        m_contextStack.push(0);
        return;
    }

    DUChainReadLocker lock;
    const QList<Declaration*> decls = current->findDeclarations(identifier);
    if ( decls.isEmpty() ) {
        // no hints for the current object
        m_contextStack.push(0);
        return;
    }

    kDebug() << "Looking in " << identifier.toString();
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

    kDebug() << "Found specified correct type for " << identifier.toString() << decls.first()->abstractType()->toString();
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
