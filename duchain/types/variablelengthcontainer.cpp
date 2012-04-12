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

#include "variablelengthcontainer.h"
#include "helpers.h"

#include <language/duchain/types/typeregister.h>
#include <language/duchain/duchain.h>
#include <language/duchain/duchainlock.h>

#include <KLocalizedString>

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
    AbstractType::Ptr newContentType = Helper::mergeTypes(contentType().abstractType(), typeToAdd);
    DUChainReadLocker lock;
    d_func_dynamic()->m_contentType = newContentType->indexed();
    kDebug() << "CONTAINER :: new content type: " << contentType().abstractType()->toString();
}

void VariableLengthContainer::replaceContentType(AbstractType::Ptr newType)
{
    d_func_dynamic()->m_contentType = newType->indexed();
}

void VariableLengthContainer::replaceKeyType(AbstractType::Ptr newType)
{
    d_func_dynamic()->m_keyType = newType->indexed();
}

const IndexedType& Python::VariableLengthContainer::contentType() const
{
    return d_func()->m_contentType;
}

void Python::VariableLengthContainer::addKeyType(AbstractType::Ptr typeToAdd)
{
    d_func_dynamic()->m_keyType = Helper::mergeTypes(keyType().abstractType(), typeToAdd)->indexed();
    DUChainReadLocker lock(DUChain::lock());
    kDebug() << "CONTAINER :: new key type: " << keyType().abstractType()->toString();
    if ( ! hasKeyType() ) {
        kWarning() << "warning: you're adding key types to an object which should not have typed keys";
    }
}

VariableLengthContainer::~VariableLengthContainer()
{
}

const IndexedType& Python::VariableLengthContainer::keyType() const
{
    return d_func()->m_keyType;
}

KDevelop::AbstractType* VariableLengthContainer::clone() const
{
    VariableLengthContainer* n = new VariableLengthContainer(*this);
    return n;
}

void VariableLengthContainer::setHasKeyType(bool hasKeyType)
{
    d_func_dynamic()->m_hasKeyType = hasKeyType;
}

bool VariableLengthContainer::hasKeyType() const
{
    return d_func()->m_hasKeyType;
}

QString VariableLengthContainer::toString() const
{
    QString prefix = KDevelop::StructureType::toString();
    AbstractType::Ptr content = contentType().abstractType();
    AbstractType::Ptr key = keyType().abstractType();
    if ( hasKeyType() && content && key ) {
        return i18n("%1 of %2 : %3", prefix, key->toString(), content->toString());
    }
    if ( content ) {
        return i18n("%1 of %2", prefix, content->toString());
    }
    else
        return prefix;
}

QString VariableLengthContainer::containerToString() const
{
    return KDevelop::StructureType::toString();
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
        ( contentType().abstractType() ? contentType().abstractType()->hash() : 0 ) + 
        ( keyType().abstractType() ? keyType().abstractType()->hash() : 0 );
}

}
