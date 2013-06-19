/*****************************************************************************
 * This file is part of KDevelop                                             *
 * Copyright 2011-2013 Sven Brauch <svenbrauch@googlemail.com>               *
 *                                                                           *
 * This program is free software; you can redistribute it and/or             *
 * modify it under the terms of the GNU General Public License as            *
 * published by the Free Software Foundation; either version 2 of            *
 * the License, or (at your option) any later version.                       *
 *                                                                           *
 * This program is distributed in the hope that it will be useful,           *
 * but WITHOUT ANY WARRANTY; without even the implied warranty of            *
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             *
 * GNU General Public License for more details.                              *
 *                                                                           *
 * You should have received a copy of the GNU General Public License         *
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.     *
 *****************************************************************************
 */

#include "pythonducontext.h"

#include <language/duchain/topducontext.h>
#include <language/duchain/topducontextdata.h>
#include <language/duchain/duchainregister.h>
#include <language/duchain/duchainpointer.h>

#include "navigation/navigationwidget.h"

using namespace KDevelop;

namespace Python {

REGISTER_DUCHAIN_ITEM_WITH_DATA(PythonTopDUContext, TopDUContextData);

REGISTER_DUCHAIN_ITEM_WITH_DATA(PythonNormalDUContext, DUContextData);

template<>
QWidget* PythonTopDUContext::createNavigationWidget(Declaration* decl, TopDUContext* topContext, const QString& htmlPrefix, const QString& htmlSuffix) const {
    if ( ! decl ) {
        kDebug() << "no declaration, not returning navigationwidget";
        return 0;
    }
    return new NavigationWidget(DeclarationPointer(decl), TopDUContextPointer(topContext), htmlPrefix, htmlSuffix);
}

template<>
QWidget* PythonNormalDUContext::createNavigationWidget(Declaration* decl, TopDUContext* topContext, const QString& htmlPrefix, const QString& htmlSuffix) const {
    if ( ! decl ) {
        kDebug() << "no declaration, not returning navigationwidget";
        return 0;
    }
    return new NavigationWidget(DeclarationPointer(decl), TopDUContextPointer(topContext), htmlPrefix, htmlSuffix);
}

}
