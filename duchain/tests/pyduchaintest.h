/*
    SPDX-FileCopyrightText: 2010 Miquel Canes Gonzalez <miquelcanes@gmail.com>
    SPDX-FileCopyrightText: 2011-2012 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: MIT
*/

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
        explicit PyDUChainTest(QObject* parent = nullptr);
        void initShell();
        ~PyDUChainTest() override;

        KDevelop::ReferencedTopDUContext parse(const QString& code);
        
        Python::CodeAst::Ptr m_ast;
        
    private Q_SLOTS:
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
