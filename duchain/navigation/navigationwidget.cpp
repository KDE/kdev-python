/*
    SPDX-FileCopyrightText: 2012-2014 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: LGPL-2.0-or-later
*/

#include "navigationwidget.h"
#include "declarationnavigationcontext.h"
#include "helpers.h"

using namespace KDevelop;

namespace Python {

NavigationWidget::NavigationWidget(KDevelop::DeclarationPointer declaration, KDevelop::TopDUContextPointer topContext,
                                   KDevelop::AbstractNavigationWidget::DisplayHints hints)
    : KDevelop::AbstractNavigationWidget()
{
    setDisplayHints(hints);

    initBrowser(400);
    auto realDeclaration = DeclarationPointer(Helper::resolveAliasDeclaration(declaration.data()));
    auto context = new DeclarationNavigationContext(realDeclaration, topContext);
    setContext(NavigationContextPointer(context));
}

NavigationWidget::NavigationWidget(const IncludeItem &/*includeItem*/, TopDUContextPointer /*topContext*/,
                                   KDevelop::AbstractNavigationWidget::DisplayHints hints)
    : KDevelop::AbstractNavigationWidget()
{
    setDisplayHints(hints);
    // not supported
}

}
