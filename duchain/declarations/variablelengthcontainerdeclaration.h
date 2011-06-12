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


#ifndef VARIABLELENGTHCONTAINERDECLARATION_H
#define VARIABLELENGTHCONTAINERDECLARATION_H

#include <language/duchain/declaration.h>
#include "pythonduchainexport.h"

using namespace KDevelop;

namespace Python {

/**
* Describes something like a python list which is a list, but has a second type,
* the type of its content (for example "list of integers").
**/
class KDEVPYTHONDUCHAIN_EXPORT VariableLengthContainerDeclaration : public KDevelop::Declaration
{
public:
    AbstractType::Ptr m_contentType;
    AbstractType::Ptr contentType();
    void addContentType(AbstractType::Ptr typeToAdd);
    AbstractType::Ptr m_keyType;
    AbstractType::Ptr keyType();
    void addKeyType(AbstractType::Ptr typeToAdd);
};

}

#endif // VARIABLELENGTHCONTAINERDECLARATION_H
