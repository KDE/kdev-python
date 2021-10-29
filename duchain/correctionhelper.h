/*
    SPDX-FileCopyrightText: 2013 Sven Brauch <svenbrauch@gmail.com>

    SPDX-License-Identifier: GPL-2.0-only OR GPL-3.0-only OR LicenseRef-KDE-Accepted-GPL
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
