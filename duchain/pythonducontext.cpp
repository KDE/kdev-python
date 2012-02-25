/*****************************************************************************
 * This file is part of KDevelop                                             *
 * Copyright 2011-2012 Sven Brauch <svenbrauch@googlemail.com>               *
 *                                                                           *
 * Permission is hereby granted, free of charge, to any person obtaining     *
 * a copy of this software and associated documentation files (the           *
 * "Software"), to deal in the Software without restriction, including       *
 * without limitation the rights to use, copy, modify, merge, publish,       *
 * distribute, sublicense, and/or sell copies of the Software, and to        *
 * permit persons to whom the Software is furnished to do so, subject to     *
 * the following conditions:                                                 *
 *                                                                           *
 * The above copyright notice and this permission notice shall be            *
 * included in all copies or substantial portions of the Software.           *
 *                                                                           *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,           *
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF        *
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND                     *
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE    *
 * LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION    *
 * OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION     *
 * WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.           *
 *****************************************************************************/

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
