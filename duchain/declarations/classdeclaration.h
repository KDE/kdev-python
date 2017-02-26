/**
    This file is part of KDevelop
    Copyright (C) 2011 Sven Brauch <svenbrauch@googlemail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 2 of the License, or
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
#include <serialization/indexedstring.h>

#include "pythonduchainexport.h"

namespace Python {

class KDEVPYTHONDUCHAIN_EXPORT ClassDeclarationData : public KDevelop::ClassDeclarationData
{
public:
    ClassDeclarationData()
        : KDevelop::ClassDeclarationData() {}

    ClassDeclarationData(const ClassDeclarationData& rhs)
        : KDevelop::ClassDeclarationData(rhs) {}

    ~ClassDeclarationData() {}
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
    typedef KDevelop::DUChainPointer<ClassDeclaration> Ptr;
    
private:
    DUCHAIN_DECLARE_DATA(ClassDeclaration);
};

} // namespace Python

#endif // PYTHONCLASSDECLARATION_H
