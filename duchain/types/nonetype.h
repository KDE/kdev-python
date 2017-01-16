/**
    This file is part of KDevelop
    Copyright (C) 2017 Francis Herne <mail@flherne.uk>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received az copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
**/

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
