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


#ifndef UNSURETYPE_H
#define UNSURETYPE_H

#include "pythonduchainexport.h"

#include <language/duchain/types/structuretype.h>
#include <language/duchain/types/typesystemdata.h>
#include <language/duchain/use.h>
#include <language/editor/modificationrevision.h>
#include <language/duchain/topducontext.h>
#include <language/duchain/types/typesystem.h>
#include <language/duchain/types/typesystemdata.h>
#include <language/duchain/types/typealiastype.h>
#include <language/duchain/types/unsuretype.h>

namespace Python {
    
// class KDEVPYTHONDUCHAIN_EXPORT UnsureTypeData : public KDevelop::UnsureTypeData
// {
// public:
//     /// Constructor
//     UnsureTypeData()
//         : KDevelop::UnsureTypeData()
//     {
//     }
//     /// Copy constructor. \param rhs data to copy
//     UnsureTypeData( const UnsureTypeData& rhs )
//         : KDevelop::UnsureTypeData(rhs)
//     {
//     }
// };


/**
* Describes a type which is a hint, and thus kept between parser passes and only deleted if the context which created it
* goes away or is reparsed (it'll create a new one in case the hint still exists)
**/
class KDEVPYTHONDUCHAIN_EXPORT UnsureType : public KDevelop::UnsureType
{
public:
    typedef TypePtr<UnsureType> Ptr;
    
    UnsureType();
    UnsureType(const UnsureType& rhs);
    UnsureType(KDevelop::UnsureTypeData& data);
    
    virtual AbstractType* clone() const;
    virtual uint hash() const;
    
    virtual bool equals(const AbstractType* rhs) const;
    
    enum {
#warning check identity value (63)
        Identity = 63
    };
    
    typedef KDevelop::UnsureTypeData Data;
    typedef KDevelop::UnsureType BaseType;
    
protected:
    TYPE_DECLARE_DATA(KDevelop::UnsureType);
};

}

#endif // UNSURETYPE_H
