/*
    SPDX-FileCopyrightText: 2017 Francis Herne <mail@flherne.uk>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef PYTHON_NONETYPE_H
#define PYTHON_NONETYPE_H

#include <language/duchain/types/integraltype.h>
#include "pythonduchainexport.h"

using namespace KDevelop;

namespace Python {

typedef IntegralTypeData NoneTypeData;

/**
 * The only purpose of this class is to override IntegralType::toString().
 * TODO: improve kdevplatform API to allow custom strings sanely.
 */
class KDEVPYTHONDUCHAIN_EXPORT NoneType: public IntegralType
{
public:
    /// Default constructor
    explicit NoneType();
    /// Copy constructor. \param rhs type to copy
    NoneType(const NoneType& rhs);
    /// Constructor using raw data. \param data internal data.
    explicit NoneType(IntegralTypeData& data);

    AbstractType* clone() const override;

    enum { Identity = 64 };

    QString toString() const override;
};

}

#endif // PYTHON_NONETYPE_H
