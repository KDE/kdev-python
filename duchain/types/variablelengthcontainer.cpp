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
#include <language/duchain/duchain.h>
#include <language/duchain/duchainlock.h>

using namespace KDevelop;

namespace Python {
    
REGISTER_TYPE(VariableLengthContainer);

VariableLengthContainer::VariableLengthContainer() : KDevelop::StructureType(createData<VariableLengthContainer>())
{

}

VariableLengthContainer::VariableLengthContainer(const VariableLengthContainer& rhs)
    : StructureType(copyData<VariableLengthContainer>(*rhs.d_func()))
{

}

VariableLengthContainer::VariableLengthContainer(StructureTypeData& data): StructureType(data)
{

}
    
void Python::VariableLengthContainer::addContentType(AbstractType::Ptr typeToAdd)
{
    d_func_dynamic()->m_contentType = Helper::mergeTypes(d_func()->m_contentType, typeToAdd);
    DUChainReadLocker lock(DUChain::lock());
    kDebug() << "CONAINER :: new content type: " << d_func()->m_contentType->toString();
}

const AbstractType::Ptr& Python::VariableLengthContainer::contentType() const
{
    return d_func()->m_contentType;
}

void Python::VariableLengthContainer::addKeyType(AbstractType::Ptr typeToAdd)
{
    d_func_dynamic()->m_keyType = Helper::mergeTypes(d_func()->m_keyType, typeToAdd);
    DUChainReadLocker lock(DUChain::lock());
    kDebug() << "CONAINER :: new key type: " << d_func()->m_contentType->toString();
}

const AbstractType::Ptr& Python::VariableLengthContainer::keyType() const
{
    return d_func()->m_keyType;
}

KDevelop::AbstractType* VariableLengthContainer::clone() const
{
    VariableLengthContainer* n = new VariableLengthContainer(*this);
    DUChainReadLocker lock(DUChain::lock());
    kDebug() << "CLONED CONTAINER: " << n->toString() << n->contentType().unsafeData() << contentType().unsafeData();
    return n;
}

bool VariableLengthContainer::equals(const AbstractType* rhs) const
{
    if ( this == rhs ) {
        return true;
    }
    if ( ! KDevelop::StructureType::equals(rhs) ) {
        return false;
    }
    const VariableLengthContainer* c = dynamic_cast<const VariableLengthContainer*>(rhs);
    if ( ! c ) {
        return false;
    }
    kDebug() << c->contentType() << d_func()->m_contentType;
    if ( c->contentType() != d_func()->m_contentType ) {
        return false;
    }
    if ( c->keyType() != d_func()->m_keyType ) {
        return false;
    }
    return true;
}

uint VariableLengthContainer::hash() const
{
    return StructureType::hash() + 
        ( d_func()->m_contentType ? d_func()->m_contentType->hash() : 0 ) + 
        ( d_func()->m_keyType ? d_func()->m_keyType->hash() : 0 );
}

}
