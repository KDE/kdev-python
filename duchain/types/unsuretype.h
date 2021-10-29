/*
    SPDX-FileCopyrightText: 2011 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

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

    void addType(const IndexedType& type) override;

    const QList<AbstractType::Ptr> typesRecursive() const;

    bool equals(const AbstractType* rhs) const override;

    enum {
// #warning check identity value (63)
        Identity = 63
    };

    typedef KDevelop::UnsureTypeData Data;

protected:
    TYPE_DECLARE_DATA(KDevelop::UnsureType);
};

}

#endif // UNSURETYPE_H
