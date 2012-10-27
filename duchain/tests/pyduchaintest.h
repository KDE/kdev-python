/*****************************************************************************
 * Copyright 2010 (c) Miquel Canes Gonzalez <miquelcanes@gmail.com>          *
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

#ifndef PYDUCHAINTEST_H
#define PYDUCHAINTEST_H

#include <QObject>
#include <kdev-pg-memory-pool.h>
#include "ast.h"
#include <language/duchain/indexedstring.h>
#include <language/duchain/topducontext.h>
#include <tests/testfile.h>

namespace KDevelop {
class TopDUContext;
class ReferencedTopDUContext;
}

using namespace KDevelop;

class PyDUChainTest : public QObject
{
    Q_OBJECT
    public:
        explicit PyDUChainTest(QObject* parent = 0);
        void initShell();
        
        KDevelop::ReferencedTopDUContext parse(const QString& code);
        
        Python::CodeAst* m_ast;
        KDevPG::MemoryPool m_pool;
        
    private slots:
        void testSimple();
        void testSimple_data();
        void testRanges();
        void testRanges_data();
        void testTypes();
        void testTypes_data();
        void testImportDeclarations();
        void testImportDeclarations_data();
        void testCrashes();
        void testCrashes_data();
        void testFlickering();
        void testFlickering_data();
        void testFunctionArgs();
        void testAutocompletionFlickering();
        void testContainerTypes();
        void testContainerTypes_data();
        void testDecorators();
        void testDecorators_data();
        void testInheritance();
        void testInheritance_data();
        void testClassVariables();
        void testClassContextRanges();
        void testVarKWArgs();
        void testMultiFromImport();
        void testCannotOverwriteBuiltins();
        void testFunctionHints();
        void testFunctionHints_data();
};

#endif // PYDUCHAINTEST_H
