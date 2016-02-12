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
    auto type = indexed.abstractType();
    auto hinted = type.cast<HintedType>(); // XXX: do we need a read locker here?
    if ( ! hinted ) {
        // if we aren't adding a HintedType the default implementation works
        KDevelop::UnsureType::addType(indexed);
        return;
    }
    auto& list = d_func_dynamic()->m_typesList();
    DUChainReadLocker lock;
    if (!hinted->isValid()) { // needs a read lock (as does most of the rest of the function)
        // can happen if the user saves the currently open document again before parsing has finished
        return;
    }
    // If there is already a HintedType in the list referring to the underlying type
    // we only add it if the context it was created in is the same.
    // Additionally, we also remove all HintedType instances that are no longer valid
    // to make sure the list doesn't grow infinitely large
    const auto newHintedTargetIndex = hinted->type()->indexed().index();
    bool alreadyExists = false;
    for ( int j = 0; j < list.size(); j++ ) {
        const IndexedType oldIndexed = list.at(j);
        if (oldIndexed == indexed) {
            alreadyExists = true;
        }
        const auto& old = oldIndexed.abstractType();
        if ( auto oldHinted = old.cast<HintedType>() ) {
            if ( !alreadyExists ) {
                // only do these checks if we haven't already determined that it is a duplicate
                auto oldHintedTargetIndex = oldHinted->type()->indexed().index();
                if ( oldHintedTargetIndex == newHintedTargetIndex ) {
                    if ( hinted->createdBy() == oldHinted->createdBy()) {
                        alreadyExists = true;
                    }
                }
            }
            if ( ! oldHinted->isValid() ) {
                // std::remove_if + erase() would be faster than remove() but this list won't have many entries
                // and the memcpy() cost is probably massively offset by the IndexedType -> AbstractType
                // lookup that we would have to duplicated if we had a separate check for duplicates loop
                list.remove(j);
                j--;
                continue;
            }
        }
    }
    if ( !alreadyExists ) {
        list.append(indexed);
    }
// #define CHECK_DUPLICATES
#ifdef CHECK_DUPLICATES
    if (list.size() > 1) {
        QString types;
        bool foundDuplicates = false;
        QStringList checkDuplicates;
        FOREACH_FUNCTION(const IndexedType& type2, d_func()->m_types) {
            auto t = type2.abstractType();
            auto str = t->toString();
            types += "\n    " + QString::number(type2.index());
            auto hinted = t.cast<HintedType>();
            while (hinted) {
                auto target = hinted->type();
                types += " (aka " + QString::number(target->indexed().index()) + ": " + target->toString()
                        +  " and context " + QString::number(hinted->createdBy().index()) + ")";
                hinted = target.cast<HintedType>();
            }
            types += " - " + t->toString() + " of type "  + typeid(*t).name();
            if (!foundDuplicates) {
                if (checkDuplicates.contains(str)) {
                    foundDuplicates = true;
                } else {
                    checkDuplicates.append(str);
                }
            }
        }
        if (foundDuplicates) {
            qWarning().nospace().noquote() << "found potential duplicates when adding " << typeid(*type).name()
                << " " << type->toString()
                << "(index = " << indexed.index() << ") ->" << types;
        }
    }
#endif
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
