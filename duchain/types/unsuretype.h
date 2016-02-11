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


#ifndef PYTHON_UNSURETYPE_H
#define PYTHON_UNSURETYPE_H

#include "pythonduchainexport.h"
#include "hintedtype.h"

#include <language/duchain/types/structuretype.h>
#include <language/duchain/types/typesystemdata.h>
#include <language/duchain/use.h>
#include <language/editor/modificationrevision.h>
#include <language/duchain/topducontext.h>
#include <language/duchain/types/typesystem.h>
#include <language/duchain/types/typesystemdata.h>
#include <language/duchain/types/typealiastype.h>
#include <language/duchain/types/unsuretype.h>
#include <language/duchain/types/indexedtype.h>
#include <language/duchain/types/typepointer.h>

namespace Python {

class KDEVPYTHONDUCHAIN_EXPORT UnsureType : public KDevelop::UnsureType
{
public:
    typedef KDevelop::TypePtr<UnsureType> Ptr;

    UnsureType();
    UnsureType(const UnsureType& rhs);
    UnsureType(KDevelop::UnsureTypeData& data);

    WhichType whichType() const override;

    AbstractType* clone() const override;
    uint hash() const override;
    QString toString() const override;

    void addType(IndexedType type);

    const QList<AbstractType::Ptr> typesRecursive() const;

    bool equals(const AbstractType* rhs) const override;

    enum {
// #warning check identity value (63)
        Identity = 63
    };

    typedef KDevelop::UnsureTypeData Data;
    typedef KDevelop::UnsureType BaseType;

protected:
    TYPE_DECLARE_DATA(KDevelop::UnsureType);
};

}

#endif // UNSURETYPE_H
