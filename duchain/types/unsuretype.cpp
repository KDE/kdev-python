/**
    This file is part of KDevelop
    Copyright (C) 2011 Sven Brauch <svenbrauch@googlemail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
**/

#include "unsuretype.h"
#include "helpers.h"
#include "indexedcontainer.h"

#include <QDebug>
#include "../duchaindebug.h"

#include <language/duchain/types/typeregister.h>
#include <language/duchain/types/typesystem.h>
#include <language/duchain/types/typealiastype.h>
#include <language/duchain/types/containertypes.h>
#include <language/duchain/types/unsuretype.h>
#include <language/duchain/parsingenvironment.h>
#include <language/duchain/duchainlock.h>

#include <KLocalizedString>

namespace Python {

REGISTER_TYPE(UnsureType);

UnsureType::UnsureType() : KDevelop::UnsureType(createData<UnsureType>())
{
}

UnsureType::UnsureType(const UnsureType& rhs)
    : KDevelop::UnsureType(copyData<UnsureType>(*rhs.d_func()))
{

}

UnsureType::UnsureType(KDevelop::UnsureTypeData& data)
    : KDevelop::UnsureType(data)
{

}

const QList<AbstractType::Ptr> UnsureType::typesRecursive() const
{
    QList<AbstractType::Ptr> results;
    FOREACH_FUNCTION ( const IndexedType& type, d_func()->m_types ) {
        AbstractType::Ptr current = type.abstractType();
        AbstractType::Ptr resolved = Helper::resolveAliasType(current);
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
    QString typeList;
    QVector<AbstractType::Ptr> types;
    auto is_new_type = [&types](const IndexedType newType) {
        foreach ( const auto& type, types ) {
            if ( type->indexed() == newType ) {
                return false;
            }
        }
        return true;
    };

    foreach ( AbstractType::Ptr type, typesRecursive() ) {
        if ( ! type ) {
            qCWarning(KDEV_PYTHON_DUCHAIN) << "Invalid type: " << type.data();
            continue;
        }

        const auto new_type = Helper::resolveAliasType(type);
        if ( is_new_type(new_type->indexed()) ) {
            types.append(new_type);
        }
    }

    auto count_and_remove = [&types](std::function<bool(AbstractType::Ptr)> match) -> bool {
        auto count = std::count_if(types.begin(), types.end(), match);
        if ( count < 3 ) {
            // nothing worth collapsing
            return false;
        }
        auto end = std::remove_if(types.begin(), types.end(), match);
        types.erase(end, types.end());
        return true;
    };

    QStringList collapsedTypes;
    if ( types.size() > 2 ) {
        // try to collapse the list, if possible
        using T = const AbstractType::Ptr&;
        auto have_callable = count_and_remove([](T t) { return t->whichType() == AbstractType::TypeFunction; });
        if ( have_callable ) {
            // TODO collapse arguments / return type
            collapsedTypes.append(i18nc("some object that can be called, in programming", "<callable>"));
        }
        auto have_iterable = count_and_remove([](T t) { return t.cast<IndexedContainer>() || t.cast<ListType>(); });
        if ( have_iterable ) {
            // TODO collapse element count / types
            collapsedTypes.append(i18nc("a set with some elements", "<iterable>"));
        }
    }

    int count = 0;
    foreach ( const auto& type, types ) {
        if ( count )
            typeList += ", ";
        count += 1;

        typeList += type->toString();
    }
    foreach ( const auto& collapsed, collapsedTypes ) {
        if ( count )
            typeList += ", ";
        count += 1;

        typeList += collapsed;
    }

    if ( count == 0 || count > 7 )
        return i18nc("refers to a type (in program code) which is not known", "mixed");
    if ( count == 1 )
        return typeList;
    return i18nc("refers to a type (in program code) which can have multiple values", "unsure (%1)", typeList);
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

void UnsureType::addType(IndexedType indexed) {
    KDevelop::UnsureType::addType(indexed);
    auto type = indexed.abstractType();
    if ( ! type.cast<HintedType>() ) {
        return;
    }

    auto list = d_func_dynamic()->m_typesList();
    for ( int j = 0; j < list.size(); j++ ) {
        const auto& old = list.at(j).abstractType();
        if ( auto hinted = old.cast<HintedType>() ) {
            if ( ! hinted->isValid() ) {
                list.remove(j);
                j--;
            }
        }
    }
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
