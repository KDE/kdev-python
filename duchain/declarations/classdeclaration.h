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


#ifndef PYTHONCLASSDECLARATION_H
#define PYTHONCLASSDECLARATION_H

#include <language/duchain/classdeclaration.h>
#include <language/duchain/indexedstring.h>

#include "pythonduchainexport.h"
#include "decorator.h"

namespace Python {

DECLARE_LIST_MEMBER_HASH(ClassDeclarationData, m_decorators, Decorator);

class KDEVPYTHONDUCHAIN_EXPORT ClassDeclarationData : public KDevelop::ClassDeclarationData
{
public:
    ClassDeclarationData()
        : KDevelop::ClassDeclarationData()
    {
        initializeAppendedLists();
    }

    ClassDeclarationData(const ClassDeclarationData& rhs)
        : KDevelop::ClassDeclarationData(rhs) 
    {
        initializeAppendedLists();
        copyListsFrom(rhs);
    }
    
    ~ClassDeclarationData() {
        freeAppendedLists();
    }

    START_APPENDED_LISTS_BASE(ClassDeclarationData, KDevelop::ClassDeclarationData);
    APPENDED_LIST_FIRST(ClassDeclarationData, Decorator, m_decorators);
    END_APPENDED_LISTS(ClassDeclarationData, m_decorators);
};
    
class KDEVPYTHONDUCHAIN_EXPORT ClassDeclaration : public KDevelop::ClassDeclaration
{
public:
    ClassDeclaration(const ClassDeclaration& rhs);
    ClassDeclaration(ClassDeclarationData& data);
    ClassDeclaration(const KDevelop::RangeInRevision& range, KDevelop::DUContext* context);
    ClassDeclaration(ClassDeclarationData& data, const KDevelop::RangeInRevision& range, KDevelop::DUContext* context);
    ~ClassDeclaration();
    enum {
        Identity = 125
    };
    
    inline const Decorator* decorators() {
        return d_func()->m_decorators();
    };
    
    inline unsigned int decoratorsSize() {
        return d_func()->m_decoratorsSize();
    };
    
    inline void addDecorator(const Decorator& d) {
        d_func_dynamic()->m_decoratorsList().insert(0, d);
    }
    
    typedef DUChainPointer<ClassDeclaration> Ptr;
    
private:
    DUCHAIN_DECLARE_DATA(ClassDeclaration);
};

} // namespace Python

#endif // PYTHONCLASSDECLARATION_H
