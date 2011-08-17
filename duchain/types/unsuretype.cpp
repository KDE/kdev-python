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

QString UnsureType::toString() const
{
    QString ret = "py_unsure (";
    bool first = true;
    QList<IndexedType> encountered;
    FOREACH_FUNCTION(const IndexedType& type, d_func()->m_types) {
        if ( ! first )
            ret += ", ";
        first = false;
        
        if ( encountered.contains(type) )
            continue;
        encountered << type;
        
        AbstractType::Ptr t = type.abstractType();
        if ( t )
            ret += t->toString();
        else
            ret += "none";
    }
    ret += ')';

    return ret;
}

KDevelop::AbstractType* UnsureType::clone() const
{
    UnsureType* n = new UnsureType(*this);
    return n;
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
