/*
   Copyright 2007 David Nolden <david.nolden.kdevelop@art-master.de>
   Copyright 2008 Niko Sams <niko.sams@gmail.com>

   This library is free software; you can redistribute it and/or
   modify it under the terms of the GNU Library General Public
   License version 2 as published by the Free Software Foundation.

   This library is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
   Library General Public License for more details.

   You should have received a copy of the GNU Library General Public License
   along with this library; see the file COPYING.LIB.  If not, write to
   the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
   Boston, MA 02110-1301, USA.
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
    DeclarationNavigationContext(KDevelop::DeclarationPointer decl, KDevelop::TopDUContextPointer topContext, KDevelop::AbstractNavigationContext* previousContext = 0);

    QString m_fullyQualifiedModuleIdentifier;

protected:
    void htmlIdentifiedType(KDevelop::AbstractType::Ptr type, const KDevelop::IdentifiedType* idType) override;
    void eventuallyMakeTypeLinks(AbstractType::Ptr type) override;
    QString getLink(const QString& name, DeclarationPointer declaration, NavigationAction::Type actionType);

private:
    QString typeLinkOrString(const AbstractType::Ptr type);
};

}

#endif
