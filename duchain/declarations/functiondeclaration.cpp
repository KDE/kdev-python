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


#include "functiondeclaration.h"
#include <language/duchain/duchainregister.h>

namespace Python {

DEFINE_LIST_MEMBER_HASH(FunctionDeclarationData, m_decorators, Decorator);
REGISTER_DUCHAIN_ITEM(FunctionDeclaration);

FunctionDeclaration::FunctionDeclaration(const FunctionDeclaration& rhs)
        : KDevelop::FunctionDeclaration(*new FunctionDeclarationData(*rhs.d_func()))
{
}

FunctionDeclaration::FunctionDeclaration(const KDevelop::RangeInRevision& range, KDevelop::DUContext* context)
        : KDevelop::FunctionDeclaration(*new FunctionDeclarationData, range)
{
    d_func_dynamic()->setClassId(this);
    if (context) {
        setContext(context);
    }
}

FunctionDeclaration::FunctionDeclaration(FunctionDeclarationData& data)
        : KDevelop::FunctionDeclaration(data)
{
}

FunctionDeclaration::FunctionDeclaration(FunctionDeclarationData& data, const KDevelop::RangeInRevision& range, KDevelop::DUContext* context)
        : KDevelop::FunctionDeclaration(data, range)
{
    if (context) {
        setContext(context);
    }
}

FunctionDeclaration::~FunctionDeclaration()
{
}


DEFINE_LIST_MEMBER_HASH(ClassFunctionDeclarationData, m_decorators, Decorator);
REGISTER_DUCHAIN_ITEM(ClassFunctionDeclaration);

ClassFunctionDeclaration::ClassFunctionDeclaration(const ClassFunctionDeclaration& rhs)
        : KDevelop::ClassFunctionDeclaration(*new ClassFunctionDeclarationData(*rhs.d_func()))
{
}

ClassFunctionDeclaration::ClassFunctionDeclaration(const KDevelop::RangeInRevision& range, KDevelop::DUContext* context)
        : KDevelop::ClassFunctionDeclaration(*new ClassFunctionDeclarationData, range, context)
{
    d_func_dynamic()->setClassId(this);
    if (context) {
        setContext(context);
    }
}

ClassFunctionDeclaration::ClassFunctionDeclaration(ClassFunctionDeclarationData& data)
        : KDevelop::ClassFunctionDeclaration(data)
{
}

ClassFunctionDeclaration::ClassFunctionDeclaration(ClassFunctionDeclarationData& data, const KDevelop::RangeInRevision& range, KDevelop::DUContext* context)
        : KDevelop::ClassFunctionDeclaration(data, range, context)
{
    if (context) {
        setContext(context);
    }
}

ClassFunctionDeclaration::~ClassFunctionDeclaration()
{
}


}