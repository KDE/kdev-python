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
#include <language/duchain/types/typealiastype.h>

using namespace KDevelop;

namespace Python {

REGISTER_TYPE(HintedType);

HintedType::HintedType() : KDevelop::TypeAliasType(createData<HintedType>())
{

}

HintedType::HintedType(const HintedType& rhs)
    : TypeAliasType(copyData<HintedType>(*rhs.d_func()))
{

}

HintedType::HintedType(TypeAliasTypeData& data): TypeAliasType(data)
{

}

bool HintedType::isValid(TopDUContext* /*current*/)
{
    TopDUContext* creator = d_func()->m_createdByContext.data();
    if ( ! creator ) {
        return false;
    }
    KDEBUG_BLOCK
    ModificationRevision rev(creator->parsingEnvironmentFile()->modificationRevision());
    kDebug() << "current: " << rev.revision << "; created:" << d_func()->m_modificationRevision.revision;
    kDebug() << "current: " << rev.modificationTime << "; created:" << d_func()->m_modificationRevision.modificationTime;
    if ( d_func()->m_modificationRevision < rev ) {
        kDebug() << "modification revision mismatch, invalidating";
        return false;
    }
    /// This should not be needed any more since 193f52027fb7
//     if ( creator == current && d_func()->m_modificationRevision == rev && rev.revision != 0 ) {
//         kDebug() << "modification revision exact match, but same context, invalidating";
//         return false;
//     }
    return true;
}

void HintedType::setCreatedBy(TopDUContext* context, const ModificationRevision& revision)
{
    d_func_dynamic()->m_createdByContext = context->indexed();
    d_func_dynamic()->m_modificationRevision = revision;
    kDebug() << "new HintedType with modification time: " << d_func()->m_modificationRevision.modificationTime 
             << "; " << d_func()->m_modificationRevision.revision;
}

KDevelop::AbstractType* HintedType::clone() const
{
    HintedType* n = new HintedType(*this);
    return n;
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
    if ( c->type()->indexed() != d_func()->m_type ) {
        return false;
    }
    if ( c->d_func()->m_modificationRevision != d_func()->m_modificationRevision ) {
        return false;
    }
    if ( c->d_func()->m_createdByContext != d_func()->m_createdByContext ) {
        return false;
    }
    return true;
}

uint HintedType::hash() const
{
    return AbstractType::hash() + 1 + ( type() ? type()->hash() : 0 ) + d_func()->m_createdByContext.index()
                                + d_func()->m_modificationRevision.modificationTime % 17 + (d_func()->m_modificationRevision.revision * 19) % 13;
}

}
