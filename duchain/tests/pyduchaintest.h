/*****************************************************************************
 * Copyright 2010 (c) Miquel Canes Gonzalez <miquelcanes@gmail.com>          *
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

#ifndef PYDUCHAINTEST_H
#define PYDUCHAINTEST_H

#include <QObject>
#include "ast.h"

namespace KDevelop {
class TopDUContext;
class ReferencedTopDUContext;
}

class PyDUChainTest : public QObject
{
    Q_OBJECT
    public:
        explicit PyDUChainTest(QObject* parent = 0);
        void initShell();
        
        KDevelop::ReferencedTopDUContext parse(const QString& code);
        
        Python::CodeAst* m_ast;
        
    private slots:
        void testSimple();
        void testSimple_data();
        void testRanges();
        void testRanges_data();
        void testTypes();
        void testTypes_data();
        void testImportDeclarations();
        void testImportDeclarations_data();
        void testFunctionStuff();
        void testFunctionStuff_data();
};

#endif // PYDUCHAINTEST_H
