/***************************************************************************
 *   This file is part of KDevelop                                         *
 *   Copyright 2012-2014 Sven Brauch <svenbrauch@googlemail.com>           *
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
#include "helpers.h"

using namespace KDevelop;

namespace Python {

NavigationWidget::NavigationWidget(KDevelop::DeclarationPointer declaration, KDevelop::TopDUContextPointer topContext,
                                   const QString& /* htmlPrefix */, const QString& /* htmlSuffix */)
{
    m_topContext = topContext;

    initBrowser(400);
    auto realDeclaration = DeclarationPointer(Helper::resolveAliasDeclaration(declaration.data()));
    m_startContext = new DeclarationNavigationContext(realDeclaration, m_topContext);
    setContext(m_startContext);
}

NavigationWidget::NavigationWidget(const IncludeItem &/*includeItem*/, TopDUContextPointer /*topContext*/,
                                   const QString &/*htmlPrefix*/, const QString &/*htmlSuffix*/)
{
    // not supported
}

}
