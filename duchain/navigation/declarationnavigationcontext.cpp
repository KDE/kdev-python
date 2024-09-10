/*
    SPDX-FileCopyrightText: 2007 David Nolden <david.nolden.kdevelop@art-master.de>
    SPDX-FileCopyrightText: 2008 Niko Sams <niko.sams@gmail.com>

    SPDX-License-Identifier: LGPL-2.0-only
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
    Q_ASSERT(declaration()->abstractType());
    auto klass = declaration()->abstractType().staticCast<StructureType>();

    modifyHtml() += QStringLiteral("class ");
    eventuallyMakeTypeLinks( klass );

    auto classDecl = dynamic_cast<ClassDeclaration*>(klass->declaration(topContext().data()));
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
                           DeclarationPointer(idType->declaration(topContext().data())),
                           NavigationAction::NavigateDeclaration);
        }
        return type->toString().toHtmlEscaped();
    }
    return i18nc("refers to an unknown type in programming", "unknown");
}

void DeclarationNavigationContext::htmlIdentifiedType(AbstractType::Ptr type, const IdentifiedType* idType)
{
    // TODO this code is duplicate of variablelengthcontainer::toString, resolve that somehow
    if ( auto listType = type.dynamicCast<ListType>() ) {
        QString contentType;
        const QString containerType = getLink(listType->containerToString(),
                                              DeclarationPointer(idType->declaration(topContext().data())),
                                              NavigationAction::NavigateDeclaration );
        if ( auto map = listType.dynamicCast<MapType>() ) {
            contentType.append(typeLinkOrString(map->keyType().abstractType()));
            contentType.append(QStringLiteral(" : "));
        }
        contentType.append(typeLinkOrString(listType->contentType().abstractType()));
        modifyHtml() += i18nc("as in list of int, set of string", "%1 of %2", containerType, contentType);
    }
    else if (auto indexedContainer = type.dynamicCast<IndexedContainer>()) {
        const QString containerType = getLink(indexedContainer->containerToString(),
                                              DeclarationPointer(idType->declaration(topContext().data())),
                                              NavigationAction::NavigateDeclaration );
        QStringList typesArray;
        for ( int i = 0; i < indexedContainer->typesCount(); i++ ) {
            if ( i >= 5 ) {
                // Don't print more than five types explicitly
                typesArray << QStringLiteral("...");
                break;
            }
            typesArray << typeLinkOrString(indexedContainer->typeAt(i).abstractType());
        }
        const QString contentType = QStringLiteral("(") + typesArray.join(QStringLiteral(", ")) + QStringLiteral(")");
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

#include "moc_declarationnavigationcontext.cpp"
