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

#include "declarationnavigationcontext.h"

#include <klocalizedstring.h>

#include <language/duchain/functiondefinition.h>
#include <language/duchain/namespacealiasdeclaration.h>
#include <language/duchain/forwarddeclaration.h>
#include <language/duchain/duchainutils.h>
#include <language/duchain/types/typepointer.h>
#include <language/duchain/aliasdeclaration.h>

#include <language/duchain/types/containertypes.h>

#include "helpers.h"
#include <types/indexedcontainer.h>

namespace Python
{
using namespace KDevelop;

DeclarationNavigationContext::DeclarationNavigationContext(DeclarationPointer decl, KDevelop::TopDUContextPointer topContext, AbstractNavigationContext* previousContext)
        : AbstractDeclarationNavigationContext(decl, topContext, previousContext)
{
}

QString DeclarationNavigationContext::getLink(const QString& name, DeclarationPointer declaration, NavigationAction::Type actionType) {
    NavigationAction action( declaration, actionType );
    QString targetId = QString::number((quint64)declaration.data() * actionType);
    return createLink(name, targetId, action);
};

void DeclarationNavigationContext::htmlClass()
{
    StructureType::Ptr klass = m_declaration->abstractType().cast<StructureType>();
    Q_ASSERT(klass);

    modifyHtml() += QStringLiteral("class ");
    eventuallyMakeTypeLinks( klass.cast<AbstractType>() );

    auto classDecl = dynamic_cast<ClassDeclaration*>(klass->declaration(m_topContext.data()));
    if ( classDecl && classDecl->baseClassesSize() ) {
        int count = 0;
        FOREACH_FUNCTION( const BaseClassInstance& base, classDecl->baseClasses ) {
            modifyHtml() += count++ ? QStringLiteral(", ") : QStringLiteral(" (");
            eventuallyMakeTypeLinks(base.baseClass.abstractType());
        }
        modifyHtml() += QStringLiteral(")");
    }
}

QString DeclarationNavigationContext::typeLinkOrString(const AbstractType::Ptr type) {
    if ( type ) {
        if ( auto idType = dynamic_cast<IdentifiedType*>(type.data()) ) {
            return getLink(type->toString(),
                           DeclarationPointer(idType->declaration(m_topContext.data())),
                           NavigationAction::NavigateDeclaration);
        }
        return type->toString().toHtmlEscaped();
    }
    return i18nc("refers to an unknown type in programming", "unknown");
}

void DeclarationNavigationContext::htmlIdentifiedType(AbstractType::Ptr type, const IdentifiedType* idType)
{
    // TODO this code is duplicate of variablelengthcontainer::toString, resolve that somehow
    if ( auto listType = type.cast<ListType>() ) {
        QString contentType;
        const QString containerType = getLink(listType->containerToString(),
                                              DeclarationPointer(idType->declaration(m_topContext.data())),
                                              NavigationAction::NavigateDeclaration );
        if ( auto map = listType.cast<MapType>() ) {
            contentType.append(typeLinkOrString(map->keyType().abstractType()));
            contentType.append(" : ");
        }
        contentType.append(typeLinkOrString(listType->contentType().abstractType()));
        modifyHtml() += i18nc("as in list of int, set of string", "%1 of %2", containerType, contentType);
    }
    else if (auto indexedContainer = type.cast<IndexedContainer>()) {
        const QString containerType = getLink(indexedContainer->containerToString(),
                                              DeclarationPointer(idType->declaration(m_topContext.data())),
                                              NavigationAction::NavigateDeclaration );
        QStringList typesArray;
        for ( int i = 0; i < indexedContainer->typesCount(); i++ ) {
            if ( i >= 5 ) {
                // Don't print more than five types explicitly
                typesArray << "...";
                break;
            }
            typesArray << typeLinkOrString(indexedContainer->typeAt(i).abstractType());
        }
        const QString contentType = QStringLiteral("(") + typesArray.join(", ") + ")";
        modifyHtml() += i18nc("as in list of int, set of string", "%1 of %2", containerType, contentType);
    }
    else {
        KDevelop::AbstractDeclarationNavigationContext::htmlIdentifiedType(type, idType);
    }
}

void DeclarationNavigationContext::eventuallyMakeTypeLinks(AbstractType::Ptr type)
{
    KDevelop::AbstractDeclarationNavigationContext::eventuallyMakeTypeLinks(Helper::resolveAliasType(type));
}

}
