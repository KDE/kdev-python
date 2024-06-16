/*
    SPDX-FileCopyrightText: 2011 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef HINTEDTYPE_H
#define HINTEDTYPE_H

#include "pythonduchainexport.h"

#include <language/duchain/types/structuretype.h>
#include <language/duchain/types/typesystem.h>
#include <language/duchain/types/typesystemdata.h>
#include <language/duchain/types/typealiastype.h>
#include <language/duchain/use.h>
#include <language/duchain/topducontext.h>
#include <language/editor/modificationrevision.h>

using namespace KDevelop;

namespace Python {

class KDEVPYTHONDUCHAIN_EXPORT HintedTypeData : public KDevelop::TypeAliasTypeData
{
public:
    /// Constructor
    HintedTypeData()
        : KDevelop::TypeAliasTypeData(), m_createdByContext((TopDUContext*) nullptr), m_modificationRevision()
    {
    }
    /// Copy constructor. \param rhs data to copy
    HintedTypeData( const HintedTypeData& rhs )
        : KDevelop::TypeAliasTypeData(rhs), m_createdByContext(rhs.m_createdByContext)
        , m_modificationRevision(rhs.m_modificationRevision)
    {
    }
    
    HintedTypeData(const TypeAliasTypeData& rhs)
        : KDevelop::TypeAliasTypeData(rhs), m_createdByContext((TopDUContext*) nullptr), m_modificationRevision()
    {
    };
    
    IndexedTopDUContext m_createdByContext;
    ModificationRevision m_modificationRevision;
};


/**
* Describes a type which is a hint, and thus kept between parser passes and only deleted if the context which created it
* goes away or is reparsed (it'll create a new one in case the hint still exists)
**/
class KDEVPYTHONDUCHAIN_EXPORT HintedType : public KDevelop::TypeAliasType
{
public:
    typedef TypePtr<HintedType> Ptr;

    HintedType();
    HintedType(const HintedType& rhs);
    HintedType(TypeAliasTypeData& data);

    /**
     * @brief Sets the creating topDUContext for this type hint.
     * Also uses that contexts current modification revision as creation time.
     *
     * @param context the topDUContext to use
     **/
    void setCreatedBy(TopDUContext* context, const ModificationRevision& revision);
    /** @return the creating TopDUContext for this type hint. */
    IndexedTopDUContext createdBy() const;
    AbstractType* clone() const override;
    size_t hash() const override;

    /**
     * @brief Checks whether this hint is still valid, and returns false if it is not
     * @warning The DUChain must be at least read-locked for this
     *
     * @return bool true if valid, false otherwise
     **/
    bool isValid();

    bool equals(const AbstractType* rhs) const override;
    enum {
        Identity = 62
    };

    typedef HintedTypeData Data;

protected:
    TYPE_DECLARE_DATA(HintedType);
};

}

#endif // VARIABLELENGTHCONTAINER_H
