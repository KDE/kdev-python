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

#include "indexedcontainer.h"
#include "helpers.h"
#include <language/duchain/duchain.h>
#include <language/duchain/duchainlock.h>
#include <KLocalizedString>

using namespace KDevelop;

namespace Python {

DEFINE_LIST_MEMBER_HASH(IndexedContainerData, m_values, IndexedType)
REGISTER_TYPE(IndexedContainer);

IndexedContainer::IndexedContainer() : KDevelop::StructureType(createData<IndexedContainer>())
{

}

IndexedContainer::IndexedContainer(const IndexedContainer& rhs)
    : StructureType(copyData<IndexedContainer>(*rhs.d_func()))
{

}

IndexedContainer::IndexedContainer(StructureTypeData& data): StructureType(data)
{

}
    

void IndexedContainer::addEntry(AbstractType::Ptr typeToAdd)
{
    d_func_dynamic()->m_valuesList().append(typeToAdd->indexed());
}

const IndexedType& IndexedContainer::typeAt(int index) const
{
    Q_ASSERT((uint) index < d_func()->m_valuesSize());
    return d_func()->m_values()[index];
}

KDevelop::AbstractType* IndexedContainer::clone() const
{
    IndexedContainer* n = new IndexedContainer(*this);
    DUChainReadLocker lock(DUChain::lock());
    return n;
}

QString IndexedContainer::toString() const
{
    QString prefix = KDevelop::StructureType::toString();
    return "(indexed container with " + QString::number(d_func()->m_valuesSize()) + "entries)";
}

QString IndexedContainer::containerToString() const
{
    return KDevelop::StructureType::toString();
}

int IndexedContainer::typesCount() const
{
    return d_func()->m_valuesSize();
}

bool IndexedContainer::equals(const AbstractType* rhs) const
{
    if ( this == rhs ) {
        return true;
    }
    if ( ! KDevelop::StructureType::equals(rhs) ) {
        return false;
    }
    const IndexedContainer* c = dynamic_cast<const IndexedContainer*>(rhs);
    if ( ! c ) {
        return false;
    }
    if ( typesCount() != c->typesCount() ) {
        return false;
    }
    for ( int i = 0; i < typesCount(); i++ ) {
        if ( c->typeAt(i) != typeAt(i) ) {
            return false;
        }
    }
    return true;
}

uint IndexedContainer::hash() const
{
    uint h = StructureType::hash();
    for ( uint i = 0; i < d_func()->m_valuesSize(); i++ ) {
        h += i*d_func()->m_values()[i];
    }
    return h;
}

}
