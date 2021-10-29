/*
    SPDX-FileCopyrightText: 2011 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

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

QString NoneType::toString() const { return QStringLiteral("None"); };

}
