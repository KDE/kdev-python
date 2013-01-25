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

#include <QtGui/QTextDocument>

#include <klocale.h>
#include <klocalizedstring.h>

#include <language/duchain/functiondefinition.h>
#include <language/duchain/namespacealiasdeclaration.h>
#include <language/duchain/forwarddeclaration.h>
#include <language/duchain/duchainutils.h>
#include <types/variablelengthcontainer.h>
#include <language/duchain/types/typepointer.h>
#include <language/duchain/aliasdeclaration.h>

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

void DeclarationNavigationContext::htmlIdentifiedType(AbstractType::Ptr type, const IdentifiedType* idType)
{
    // TODO this code is duplicate of variablelengthcontainer::toString, resolve that somehow
    if ( VariableLengthContainer::Ptr t = VariableLengthContainer::Ptr::dynamicCast(type) ) {
        const QString containerType = getLink(t->containerToString(), DeclarationPointer(idType->declaration(m_topContext.data())), NavigationAction::NavigateDeclaration );
        QString contentType;
        if ( t->hasKeyType() ) {
            if ( AbstractType::Ptr key = t->keyType().abstractType() ) {
                IdentifiedType* identifiedKey = dynamic_cast<IdentifiedType*>(key.unsafeData());
                if ( identifiedKey ) {
                    contentType.append(getLink(key->toString(), DeclarationPointer(
                        identifiedKey->declaration(m_topContext.data())),
                        NavigationAction::NavigateDeclaration
                    ));
                }
                else {
                    contentType.append(key->toString());
                }
                contentType.append(" : ");
            }
        }
        if ( AbstractType::Ptr contents = t->contentType().abstractType() ) {
            IdentifiedType* identifiedContent = dynamic_cast<IdentifiedType*>(contents.unsafeData());
            if ( identifiedContent ) {
                contentType.append(getLink(contents->toString(), DeclarationPointer(
                    identifiedContent->declaration(m_topContext.data())),
                    NavigationAction::NavigateDeclaration
                ));
            }
            else {
                contentType.append(contents->toString());
            }
        }
        else {
            modifyHtml() += i18nc("refers to an unknown type in programming", "unknown");
        }
        modifyHtml() += i18nc("as in list of int, set of string", "%1 of %2", containerType, contentType);
    }
    else {
        KDevelop::AbstractDeclarationNavigationContext::htmlIdentifiedType(type, idType);
    }
}

QString DeclarationNavigationContext::html(bool shorten)
{
    return KDevelop::AbstractDeclarationNavigationContext::html(shorten);
}

}
