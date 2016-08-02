/***************************************************************************
 *   This file is part of KDevelop                                         *
 *   Copyright 2013 Sven Brauch <svenbrauch@googlemail.com>                *
 *                                                                           *
 * This program is free software; you can redistribute it and/or             *
 * modify it under the terms of the GNU General Public License as            *
 * published by the Free Software Foundation; either version 2 of            *
 * the License, or (at your option) any later version.                       *
 *                                                                           *
 * This program is distributed in the hope that it will be useful,           *
 * but WITHOUT ANY WARRANTY; without even the implied warranty of            *
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             *
 * GNU General Public License for more details.                              *
 *                                                                           *
 * You should have received a copy of the GNU General Public License         *
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.     *
 *****************************************************************************
 */

#ifndef PYTHONDUCONTEXT_H
#define PYTHONDUCONTEXT_H

#include <QString>
#include <language/duchain/ducontext.h>
#include <language/editor/modificationrevision.h>

class QWidget;

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
    
    virtual QWidget* createNavigationWidget(KDevelop::Declaration* decl, KDevelop::TopDUContext* topContext, 
                                            const QString& htmlPrefix, const QString& htmlSuffix,
                                            KDevelop::AbstractNavigationWidget::DisplayHints hints) const;
    
    enum {
        Identity = IdentityT
    };
};

typedef PythonDUContext<KDevelop::TopDUContext, 100> PythonTopDUContext;
typedef PythonDUContext<KDevelop::DUContext, 101> PythonNormalDUContext;

}


#endif // PYTHONDUCONTEXT_H
