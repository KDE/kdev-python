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

#include "nonetype.h"
#include <language/duchain/types/typesystemdata.h>

#include <language/duchain/types/typeregister.h>

using namespace KDevelop;

namespace Python {

REGISTER_TYPE(NoneType);

NoneType::NoneType() : IntegralType(createData<NoneType>())
{
    d_func_dynamic()->setTypeClassId<NoneType>();
    setDataType(TypeVoid);
}

NoneType::NoneType(const NoneType& rhs) : IntegralType(copyData<NoneType>(*rhs.d_func())) {}

NoneType::NoneType(IntegralTypeData& data) : IntegralType(data) {}

AbstractType* NoneType::clone() const {
    return new NoneType(*this);
}

QString NoneType::toString() const { return QStringLiteral("NoneType"); };

}
