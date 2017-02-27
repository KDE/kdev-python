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
#include <QTemporaryDir>
#include "ast.h"
#include <serialization/indexedstring.h>
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
        ~PyDUChainTest() override;

        KDevelop::ReferencedTopDUContext parse(const QString& code);
        
        Python::CodeAst::Ptr m_ast;
        
    private slots:
        void init();
        void testSimple();
        void testSimple_data();
        void testRanges();
        void testRanges_data();
        void testTypes();
        void testTypes_data();
        void testImportDeclarations();
        void testImportDeclarations_data();
        void testImportFiles();
        void testCrashes();
        void testCrashes_data();
        void testFlickering();
        void testFlickering_data();
        void testFunctionArgs();
        void testAutocompletionFlickering();
        void testContainerTypes();
        void testContainerTypes_data();
        void testInheritance();
        void testInheritance_data();
        void testClassVariables();
        void testWarnNewNotCls();
        void testWarnNewNotCls_data();
        void testBinaryOperatorsUnsure();
        void testBinaryOperatorsUnsure_data();
        void testClassContextRanges();
        void testVarKWArgs();
        void testMultiFromImport();
        void testMultiFromImport_data();
        void testRelativeImport();
        void testRelativeImport_data();
        void testCannotOverwriteBuiltins();
        void testFunctionHints();
        void testFunctionHints_data();
        void testCannotOverwriteBuiltins_data();
        void testOperators();
        void testOperators_data();
        void testVariableCreation();
        void testVariableCreation_data();
        void testProblemCount();
        void testProblemCount_data();
        void testHintedTypes();
        void testHintedTypes_data();
        void testCleanupMultiplePasses();
        void testComments();
        void testComments_data();
        void testManyDeclarations();


    private:
        QList<KDevelop::TestFile*> createdFiles;
        QTemporaryDir testDirOwner;
        QDir testDir;
        QDir assetsDir;
        QString lastTest;
        
        QList<QString> FindPyFiles(QDir& root);
};

#endif // PYDUCHAINTEST_H
