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

#include "hintedtype.h"
#include "helpers.h"
#include <language/duchain/duchain.h>
#include <language/duchain/duchainlock.h>
#include <KLocalizedString>
#include <language/duchain/parsingenvironment.h>
#include <language/duchain/types/typesystem.h>

using namespace KDevelop;

namespace Python {
    
REGISTER_TYPE(HintedType);

HintedType::HintedType() : KDevelop::AbstractType(createData<HintedType>())
{
}

HintedType::HintedType(const HintedType& rhs)
    : AbstractType(copyData<HintedType>(*rhs.d_func()))
{

}

HintedType::HintedType(AbstractTypeData& data): AbstractType(data)
{

}

const IndexedType& HintedType::typeHinted() const
{
    return d_func()->m_hintedType;
}
    
KDevelop::AbstractType* HintedType::clone() const
{
    HintedType* n = new HintedType(*this);
    return n;
}

void HintedType::accept0(TypeVisitor* v) const
{
    v->visit(d_func()->m_hintedType.abstractType().unsafeData());
}

bool HintedType::equals(const AbstractType* rhs) const
{
    if ( this == rhs ) {
        return true;
    }
    if ( ! KDevelop::AbstractType::equals(rhs) ) {
        return false;
    }
    const HintedType* c = dynamic_cast<const HintedType*>(rhs);
    if ( ! c ) {
        return false;
    }
    if ( c->typeHinted() != d_func()->m_hintedType ) {
        return false;
    }
    return true;
}

uint HintedType::hash() const
{
    return AbstractType::hash() + 1 + ( typeHinted().abstractType() ? typeHinted().abstractType()->hash() : 0 );
}

}
