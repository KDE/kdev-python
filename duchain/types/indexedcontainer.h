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


#ifndef INDEXEDCONTAINER_H
#define INDEXEDCONTAINER_H

#include <language/duchain/types/structuretype.h>
#include <language/duchain/types/typesystemdata.h>

#include "types/unsuretype.h"
#include "pythonduchainexport.h"

using namespace KDevelop;

namespace Python {

KDEVPYTHONDUCHAIN_EXPORT DECLARE_LIST_MEMBER_HASH(IndexedContainerData, m_values, IndexedType)

class KDEVPYTHONDUCHAIN_EXPORT IndexedContainerData : public KDevelop::StructureTypeData
{
public:
    /// Constructor
    IndexedContainerData()
        : KDevelop::StructureTypeData()
    {
        initializeAppendedLists();
    }
    /// Copy constructor. \param rhs data to copy
    IndexedContainerData( const IndexedContainerData& rhs )
        : KDevelop::StructureTypeData(rhs)
    {
        initializeAppendedLists();
        copyListsFrom(rhs);
    }
    
    IndexedContainerData(const StructureTypeData& rhs)
        : KDevelop::StructureTypeData(rhs)
    {
//         initializeAppendedLists();
//         copyListsFrom(rhs);
    };
    
    ~IndexedContainerData() {
        freeAppendedLists();
    };
    
    START_APPENDED_LISTS_BASE(IndexedContainerData, StructureTypeData)
    APPENDED_LIST_FIRST(IndexedContainerData, IndexedType, m_values)
    END_APPENDED_LISTS(IndexedContainerData, m_values)
};


class KDEVPYTHONDUCHAIN_EXPORT IndexedContainer : public KDevelop::StructureType
{
public:
    typedef TypePtr<IndexedContainer> Ptr;
    
    IndexedContainer();
    IndexedContainer(const IndexedContainer& rhs);
    IndexedContainer(StructureTypeData& data);
    void addEntry(AbstractType::Ptr typeToAdd);
    virtual AbstractType* clone() const;
    virtual uint hash() const;
    int typesCount() const;
    const IndexedType& typeAt(int index) const;
    AbstractType::Ptr asUnsureType() const;
    virtual QString toString() const;
    // "toString"s only the container type, not the content; used in declarationnavigationcontext to create
    // seperate links for the content and container type
    // by keeping toString seperate, it is possible to have a pretty type in unsure types etc. without additional
    // efforts being necessary
    QString containerToString() const;
    
    virtual bool equals(const AbstractType* rhs) const;
    
    enum {
// #warning check identity value (59)
        Identity = 59
    };
    
    typedef IndexedContainerData Data;
    typedef KDevelop::StructureType BaseType;
    
protected:
    TYPE_DECLARE_DATA(IndexedContainer);
};

}

#endif // INDEXEDCONTAINER_H
