/*
    SPDX-FileCopyrightText: 2013 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef PYTHONDUCONTEXT_H
#define PYTHONDUCONTEXT_H

#include <QString>
#include <language/duchain/ducontext.h>
#include <language/editor/modificationrevision.h>

namespace KDevelop
{
    class Declaration;
    class TopDUContext;
}

namespace Python
{

template<class BaseContext, int IdentityT>
class PythonDUContext : public BaseContext
{
public:
    template<class Data>
    PythonDUContext(Data& data) : BaseContext(data) {
    }

    ///Parameters will be reached to the base-class
    template<class Param1, class Param2>
    PythonDUContext(const Param1& p1, const Param2& p2, bool isInstantiationContext) : BaseContext(p1, p2, isInstantiationContext) {
        static_cast<KDevelop::DUChainBase*>(this)->d_func_dynamic()->setClassId(this);
    }

    ///Both parameters will be reached to the base-class. This fits TopDUContext.
    template<class Param1, class Param2, class Param3>
    PythonDUContext(const Param1& p1, const Param2& p2, const Param3& p3) : BaseContext(p1, p2, p3) {
        static_cast<KDevelop::DUChainBase*>(this)->d_func_dynamic()->setClassId(this);
    }
    template<class Param1, class Param2>
    PythonDUContext(const Param1& p1, const Param2& p2) : BaseContext(p1, p2) {
        static_cast<KDevelop::DUChainBase*>(this)->d_func_dynamic()->setClassId(this);
    }

    KDevelop::AbstractNavigationWidget* createNavigationWidget(KDevelop::Declaration* decl, KDevelop::TopDUContext* topContext,
                                            KDevelop::AbstractNavigationWidget::DisplayHints hints) const override;

    enum {
        Identity = IdentityT
    };
};

typedef PythonDUContext<KDevelop::TopDUContext, 100> PythonTopDUContext;
typedef PythonDUContext<KDevelop::DUContext, 101> PythonNormalDUContext;

}


#endif // PYTHONDUCONTEXT_H
