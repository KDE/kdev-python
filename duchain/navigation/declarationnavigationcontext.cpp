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

void DeclarationNavigationContext::htmlIdentifiedType(AbstractType::Ptr type, const IdentifiedType* idType)
{
    // TODO this code is duplicate of variablelengthcontainer::toString, resolve that somehow
    if ( VariableLengthContainer::Ptr t = VariableLengthContainer::Ptr::dynamicCast(type) ) {
        makeLink(t->containerToString(), DeclarationPointer(idType->declaration(m_topContext.data())), NavigationAction::NavigateDeclaration );
        modifyHtml() += i18nc("as in \"list of string\", \"set of integer\"", " of ");
        if ( t->hasKeyType() ) {
            if ( AbstractType::Ptr key = t->keyType().abstractType() ) {
                IdentifiedType* identifiedKey = dynamic_cast<IdentifiedType*>(key.unsafeData());
                if ( identifiedKey ) {
                    makeLink(key->toString(), DeclarationPointer(
                        identifiedKey->declaration(m_topContext.data())),
                        NavigationAction::NavigateDeclaration
                    );
                }
                else {
                    modifyHtml() += key->toString();
                }
                modifyHtml() += " : ";
            }
        }
        if ( AbstractType::Ptr contents = t->contentType().abstractType() ) {
            IdentifiedType* identifiedContent = dynamic_cast<IdentifiedType*>(contents.unsafeData());
            if ( identifiedContent ) {
                makeLink(contents->toString(), DeclarationPointer(
                    identifiedContent->declaration(m_topContext.data())),
                    NavigationAction::NavigateDeclaration
                );
            }
            else {
                modifyHtml() += contents->toString();
            }
        }
        else {
            modifyHtml() += i18nc("refers to an unknown type in programming", "unknown");
        }
    }
    else {
        KDevelop::AbstractDeclarationNavigationContext::htmlIdentifiedType(type, idType);
    }
}

QString DeclarationNavigationContext::html(bool shorten)
{
    return KDevelop::AbstractDeclarationNavigationContext::html(shorten).replace("__kdevpythondocumentation_builtin_", "");
}

}
