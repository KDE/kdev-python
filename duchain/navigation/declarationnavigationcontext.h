/*
    SPDX-FileCopyrightText: 2007 David Nolden <david.nolden.kdevelop@art-master.de>
    SPDX-FileCopyrightText: 2008 Niko Sams <niko.sams@gmail.com>

    SPDX-License-Identifier: LGPL-2.0-only
*/

#ifndef DECLARATIONNAVIGATIONCONTEXT_H
#define DECLARATIONNAVIGATIONCONTEXT_H

#include <language/duchain/navigation/abstractdeclarationnavigationcontext.h>
#include <language/duchain/navigation/navigationaction.h>
#include <language/duchain/types/abstracttype.h>
#include <language/duchain/duchainpointer.h>

using namespace KDevelop;

namespace Python
{

class DeclarationNavigationContext : public KDevelop::AbstractDeclarationNavigationContext
{
    Q_OBJECT

public:
    DeclarationNavigationContext(KDevelop::DeclarationPointer decl, KDevelop::TopDUContextPointer topContext, KDevelop::AbstractNavigationContext* previousContext = nullptr);

    QString m_fullyQualifiedModuleIdentifier;

protected:
    void htmlClass() override;
    void htmlIdentifiedType(KDevelop::AbstractType::Ptr type, const KDevelop::IdentifiedType* idType) override;
    void eventuallyMakeTypeLinks(AbstractType::Ptr type) override;
    QString getLink(const QString& name, DeclarationPointer declaration, NavigationAction::Type actionType);

private:
    QString typeLinkOrString(const AbstractType::Ptr type);
};

}

#endif
