/**
    This file is part of KDevelop
    Copyright (C) 2011  Sven Brauch <svenbrauch@googlemail.com>

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

#include "decorateddeclaration.h"

namespace Python {

Python::PythonClassDeclaration::PythonClassDeclaration(const KDevelop::RangeInRevision& range, KDevelop::DUContext* context)
    : KDevelop::ClassDeclaration(range, context)
{

}

Python::PythonClassDeclaration::PythonClassDeclaration(const KDevelop::ClassDeclaration& rhs)
    : ClassDeclaration(rhs)
{

}

Python::PythonClassDeclaration::PythonClassDeclaration(KDevelop::ClassDeclarationData& data)
    : ClassDeclaration(data)
{

}

Python::PythonClassDeclaration::PythonClassDeclaration(KDevelop::ClassDeclarationData& data, const KDevelop::RangeInRevision& range, KDevelop::DUContext* context)
    : KDevelop::ClassDeclaration(data, range, context)
{

}

Python::PythonFunctionDeclaration::PythonFunctionDeclaration(const KDevelop::RangeInRevision& range, KDevelop::DUContext* context)
    : FunctionDeclaration(range, context)
{

}

Python::PythonFunctionDeclaration::PythonFunctionDeclaration(const KDevelop::FunctionDeclaration& rhs)
    : FunctionDeclaration(rhs)
{

}

Python::PythonFunctionDeclaration::PythonFunctionDeclaration(KDevelop::FunctionDeclarationData& data)
    : FunctionDeclaration(data)
{

}

Python::PythonFunctionDeclaration::PythonFunctionDeclaration(KDevelop::FunctionDeclarationData& data, const KDevelop::RangeInRevision& )
    : FunctionDeclaration(data)
{

}

}

