/***************************************************************************
 *   This file is part of KDevelop                                         *
 *   Copyright 2012 Sven Brauch <svenbrauch@googlemail.com>                *
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU Library General Public License as       *
 *   published by the Free Software Foundation; either version 2 of the    *
 *   License, or (at your option) any later version.                       *
 *                                                                         *
 *   This program is distributed in the hope that it will be useful,       *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
 *   GNU General Public License for more details.                          *
 *                                                                         *
 *   You should have received a copy of the GNU Library General Public     *
 *   License along with this program; if not, write to the                 *
 *   Free Software Foundation, Inc.,                                       *
 *   51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.         *
 ***************************************************************************/

#include "navigationwidget.h"
#include "declarationnavigationcontext.h"

#include <QUrl>
#include <QObject>

#include <language/duchain/aliasdeclaration.h>

using namespace KDevelop;

namespace Python {

NavigationWidget::NavigationWidget(KDevelop::DeclarationPointer declaration, KDevelop::TopDUContextPointer topContext, const QString& /* htmlPrefix */, const QString& /* htmlSuffix */)
{
    kDebug() << "Navigation widget for Declaration requested";
    
    AliasDeclaration* alias = dynamic_cast<AliasDeclaration*>(declaration.data());
    DeclarationPointer realDeclaration;
    if ( alias ) {
        kDebug() << "is alias declaration";
        DUChainReadLocker lock(DUChain::lock());
        realDeclaration = DeclarationPointer(alias->aliasedDeclaration().declaration());
    }
    else {
        realDeclaration = declaration;
    }
    
    m_topContext = topContext;
    
    initBrowser(400);
    
    DeclarationNavigationContext* context = new DeclarationNavigationContext(realDeclaration, m_topContext);
    m_startContext = context;
    setContext(m_startContext);
}

void NavigationWidget::addDocumentationData(bool /*finished*/)
{
}

NavigationWidget::NavigationWidget(const KDevelop::IncludeItem& /* includeItem */, KDevelop::TopDUContextPointer /*topContext*/, const QString& /*htmlPrefix*/, const QString& /*htmlSuffix*/)
{

}

}

#include "navigationwidget.moc"