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

#ifndef CORRECTIONHELPER_H
#define CORRECTIONHELPER_H

#include <language/duchain/types/abstracttype.h>
#include <language/duchain/ducontext.h>
#include <language/duchain/topducontext.h>

#include <QStack>

using namespace KDevelop;

namespace Python {

class DeclarationBuilder;

class CorrectionHelper
{
public:
    CorrectionHelper(const IndexedString& url, DeclarationBuilder* builder);
    virtual ~CorrectionHelper();

    /// Keep this object alive as long as you are parsing a class or function.
    /// On destruction, it will automatically leave that class or function.
    struct Recursion {
        Recursion(CorrectionHelper* h) : m_helper(h) { };
        ~Recursion() {
            m_helper->leave();
        };
        CorrectionHelper* m_helper;
    };

    Recursion enterClass(const QString& identifier);
    Recursion enterFunction(const QString& identifier);

    AbstractType::Ptr hintForLocal(const QString& local) const;
    AbstractType::Ptr returnTypeHint() const;

private:
    AbstractType::Ptr hintFor(const KDevelop::Identifier& identifier) const;
    void enter(const Identifier& identifier);
    void leave();

    ReferencedTopDUContext m_hintTopContext;
    QStack<DUContext*> m_contextStack;
};

} // namespace Python

#endif // CORRECTIONHELPER_H
