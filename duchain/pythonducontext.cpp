/*
    SPDX-FileCopyrightText: 2011-2013 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#include "pythonducontext.h"

#include <language/duchain/topducontext.h>
#include <language/duchain/topducontextdata.h>
#include <language/duchain/duchainregister.h>
#include <language/duchain/duchainpointer.h>

#include "navigation/navigationwidget.h"

#include <QDebug>
#include "duchaindebug.h"

using namespace KDevelop;

namespace Python {

REGISTER_DUCHAIN_ITEM_WITH_DATA(PythonTopDUContext, TopDUContextData);

REGISTER_DUCHAIN_ITEM_WITH_DATA(PythonNormalDUContext, DUContextData);

template<>
KDevelop::AbstractNavigationWidget* PythonTopDUContext::createNavigationWidget(Declaration* decl, TopDUContext* topContext,
                                                    KDevelop::AbstractNavigationWidget::DisplayHints hints) const {
    if ( ! decl ) {
        qCDebug(KDEV_PYTHON_DUCHAIN) << "no declaration, not returning navigationwidget";
        return nullptr;
    }
    return new NavigationWidget(DeclarationPointer(decl), TopDUContextPointer(topContext), hints);
}

template<>
KDevelop::AbstractNavigationWidget* PythonNormalDUContext::createNavigationWidget(Declaration* decl, TopDUContext* topContext,
                                                       KDevelop::AbstractNavigationWidget::DisplayHints hints) const {
    if ( ! decl ) {
        qCDebug(KDEV_PYTHON_DUCHAIN) << "no declaration, not returning navigationwidget";
        return nullptr;
    }
    return new NavigationWidget(DeclarationPointer(decl), TopDUContextPointer(topContext), hints);
}

}
