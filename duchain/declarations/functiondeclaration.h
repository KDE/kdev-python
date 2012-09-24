/**
    This file is part of KDevelop
    Copyright (C) 2011 Sven Brauch <svenbrauch@googlemail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
**/


#ifndef PYTHONFUNCTIONDECLARATION_H
#define PYTHONFUNCTIONDECLARATION_H

#include <language/duchain/functiondeclaration.h>
#include <language/duchain/indexedstring.h>

#include "pythonduchainexport.h"
#include "decorator.h"

namespace Python {

KDEVPYTHONDUCHAIN_EXPORT DECLARE_LIST_MEMBER_HASH(FunctionDeclarationData, m_decorators, Decorator);

class KDEVPYTHONDUCHAIN_EXPORT FunctionDeclarationData : public KDevelop::FunctionDeclarationData
{
public:
    FunctionDeclarationData()
        : KDevelop::FunctionDeclarationData(), m_isStatic(false), m_hasKwarg(false), m_hasVararg(false)
    {
        initializeAppendedLists();
    }

    FunctionDeclarationData(const FunctionDeclarationData& rhs)
        : KDevelop::FunctionDeclarationData(rhs), m_isStatic(rhs.m_isStatic), m_hasVararg(rhs.m_hasVararg), m_hasKwarg(rhs.m_hasKwarg)
    {
        initializeAppendedLists();
        copyListsFrom(rhs);
    }
    
    ~FunctionDeclarationData() {
        freeAppendedLists();
    }
    
    bool m_isStatic: 1;
    bool m_hasVararg: 1;
    bool m_hasKwarg: 1;

    START_APPENDED_LISTS_BASE(FunctionDeclarationData, KDevelop::FunctionDeclarationData);
    APPENDED_LIST_FIRST(FunctionDeclarationData, Decorator, m_decorators);
    END_APPENDED_LISTS(FunctionDeclarationData, m_decorators);
};
    
class KDEVPYTHONDUCHAIN_EXPORT FunctionDeclaration : public KDevelop::FunctionDeclaration
{
public:
    FunctionDeclaration(const FunctionDeclaration &rhs);
    FunctionDeclaration(const KDevelop::RangeInRevision &range, KDevelop::DUContext *context);
    FunctionDeclaration(FunctionDeclarationData &data);
    FunctionDeclaration(FunctionDeclarationData &data, const KDevelop::RangeInRevision &range, KDevelop::DUContext *context);
    ~FunctionDeclaration();
    
    enum {
        Identity = 126
    };
    
    inline void setHasVararg(bool hasVararg) {
        d_func_dynamic()->m_hasVararg = hasVararg;
    }
    
    inline bool hasVararg() const {
        return d_func()->m_hasVararg;
    }
    
    inline void setHasKwarg(bool hasKwarg) {
        d_func_dynamic()->m_hasKwarg = hasKwarg;
    }
    
    inline bool hasKwarg() const {
        return d_func()->m_hasKwarg;
    }
    
    inline bool isStatic() const {
        return d_func()->m_isStatic;
    }
    
    inline void setStatic(bool isStatic) {
        d_func_dynamic()->m_isStatic = isStatic;
    }
    
    inline const Decorator* decorators() const {
        return d_func()->m_decorators();
    };
    
    inline unsigned int decoratorsSize() const {
        return d_func()->m_decoratorsSize();
    };
    
    inline void addDecorator(const Decorator& d) {
        d_func_dynamic()->m_decoratorsList().insert(0, d);
    }
    
    typedef DUChainPointer<FunctionDeclaration> Ptr;
    
private:
    DUCHAIN_DECLARE_DATA(FunctionDeclaration);
};

} // namespace Python

#endif // PYTHONFUNCTIONDECLARATION_H
