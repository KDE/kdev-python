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

#include "unsuretype.h"
#include "helpers.h"
#include <language/duchain/duchain.h>
#include <language/duchain/duchainlock.h>
#include <KLocalizedString>
#include <language/duchain/parsingenvironment.h>
#include <language/duchain/types/typesystem.h>
#include <language/duchain/types/typealiastype.h>
#include <language/duchain/types/unsuretype.h>

namespace Python {
    
REGISTER_TYPE(UnsureType);

UnsureType::UnsureType() : KDevelop::UnsureType(createData<UnsureType>())
{
}

UnsureType::UnsureType(const UnsureType& rhs)
    : KDevelop::UnsureType(copyData<UnsureType>(*rhs.d_func()))
{

}

UnsureType::UnsureType(KDevelop::UnsureTypeData& data): KDevelop::UnsureType(data)
{

}

const QList<AbstractType::Ptr> UnsureType::typesRecursive() const
{
    QList<AbstractType::Ptr> results;
    FOREACH_FUNCTION ( const IndexedType& type, d_func()->m_types ) {
        AbstractType::Ptr current = type.abstractType();
        AbstractType::Ptr resolved = Helper::resolveType(current);
        if ( resolved->whichType() == AbstractType::TypeUnsure ) {
            results.append(resolved.cast<UnsureType>()->typesRecursive());
        }
        else
            results.append(current);
    }
    return results;
}

QString UnsureType::toString() const
{
    QString ret = "unsure (";
    bool first = true;
    QList<IndexedType> encountered;
    foreach ( AbstractType::Ptr type, typesRecursive() ) {
        if ( ! type ) {
            kWarning() << "Invalid type: " << type.unsafeData();
            continue;
        }
        
        IndexedType indexed = Helper::resolveType(type)->indexed();
        if ( encountered.contains(indexed) )
            continue;
        encountered << indexed;
        
        if ( ! first )
            ret += ", ";
        first = false;
        
        ret += type->toString();
    }
    ret += ')';

    return ret;
}

KDevelop::AbstractType* UnsureType::clone() const
{
    UnsureType* n = new UnsureType(*this);
    return n;
}

AbstractType::WhichType UnsureType::whichType() const
{
    return AbstractType::TypeUnsure;
}

bool UnsureType::equals(const AbstractType* rhs) const
{
    if ( this == rhs ) {
        return true;
    }
    if ( ! dynamic_cast<const UnsureType*>(rhs) ) {
        return false;
    }
    if ( ! KDevelop::UnsureType::equals(rhs) ) {
        return false;
    }
    return true;
}

uint UnsureType::hash() const
{
    return KDevelop::UnsureType::hash() + 1;
}

}
