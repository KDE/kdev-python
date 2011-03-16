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
#include <declarations/importedmoduledeclaration.h>

#include <QTcpSocket>
#include <QProcess>

#include "parser/parserConfig.h"

namespace Python
{
using namespace KDevelop;

DeclarationNavigationContext::DeclarationNavigationContext(DeclarationPointer decl, KDevelop::TopDUContextPointer topContext, AbstractNavigationContext* previousContext)
        : AbstractDeclarationNavigationContext(decl, topContext, previousContext)
{
    kDebug() << "Generating declaration widget";
    importedModuleDeclaration* import_decl = dynamic_cast<importedModuleDeclaration*>(decl.data());
    if ( import_decl ) {
        kDebug() << " >> Module declaration found! Building documentation";
        kDebug() << " >> Identifier: " << import_decl->m_moduleIdentifier;
        m_fullyQualifiedModuleIdentifier = import_decl->m_moduleIdentifier;
    }
    else {
        kDebug() << "Could not find declaration for this module!" << decl->identifier().identifier().str();
    }
}

NavigationContextPointer DeclarationNavigationContext::registerChild(DeclarationPointer declaration)
{
    return AbstractDeclarationNavigationContext::registerChild(new DeclarationNavigationContext(declaration, m_topContext, this));
}

void DeclarationNavigationContext::makeLink(const QString& name, DeclarationPointer declaration, NavigationAction::Type actionType)
{
    QString linktext = name;
    if ( declaration && declaration->url() == IndexedString(DOCFILE_PATH) ) {
        modifyHtml() += linktext.replace("__kdevpythondocumentation_builtin_", "");
        return;
    }
    AbstractDeclarationNavigationContext::makeLink(name, declaration, actionType);
}

QString DeclarationNavigationContext::declarationKind(DeclarationPointer decl)
{
    return AbstractDeclarationNavigationContext::declarationKind(decl);
}

}
