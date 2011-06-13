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

#include <language/duchain/types/typeregister.h>

#include "variablelengthcontainer.h"
#include "helpers.h"

using namespace KDevelop;

namespace Python {
    
REGISTER_TYPE(VariableLengthContainer);
    
VariableLengthContainer::VariableLengthContainer(const StructureType& rhs) : StructureType(rhs), m_contentType(0), m_keyType(0)
{

}

VariableLengthContainer::VariableLengthContainer(const AbstractType::Ptr copyFrom)
{
    VariableLengthContainer(*(copyFrom.cast<StructureType>().unsafeData()));
}
    
void Python::VariableLengthContainer::addContentType(AbstractType::Ptr typeToAdd)
{
    m_contentType = AbstractType::Ptr::staticCast(Helper::mergeTypes(m_contentType, typeToAdd));
}

AbstractType::Ptr Python::VariableLengthContainer::contentType()
{
    return m_contentType;
}

void Python::VariableLengthContainer::addKeyType(AbstractType::Ptr typeToAdd)
{
    m_keyType = AbstractType::Ptr::staticCast(Helper::mergeTypes(m_keyType, typeToAdd));
}

AbstractType::Ptr Python::VariableLengthContainer::keyType()
{
    return m_keyType;
}

KDevelop::AbstractType* VariableLengthContainer::clone() const
{
    return new VariableLengthContainer(*this);
}

uint VariableLengthContainer::hash() const
{
    return StructureType::hash() + ( m_contentType ? m_contentType->hash() : 0 ) + ( m_keyType ?  m_keyType->hash() : 0 );
}

}
