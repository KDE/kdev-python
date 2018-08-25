/*****************************************************************************
 * Copyright 2014 Benjamin Kaiser <benjaminjkaiser@gmail.com>                *
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

#include <QDebug>
#include "duchaindebug.h"

#include "duchainbench.h"

#include <language/duchain/topducontext.h>
#include <language/codegen/coderepresentation.h>
#include <tests/autotestshell.h>
#include <tests/testcore.h>
#include <language/duchain/duchain.h>
#include <QtTest>
#include <language/backgroundparser/backgroundparser.h>
#include <interfaces/ilanguagecontroller.h>
#include <QStandardPaths>

#include "parsesession.h"

QTEST_MAIN(DUChainBench)

using namespace KDevelop;
using namespace Python;


DUChainBench::DUChainBench(QObject* parent): QObject(parent)
{
    testDir = QDir(testDirOwner.path());

    initShell();
}


void DUChainBench::initShell()
{
    AutoTestShell::init();
    TestCore* core = new TestCore();
    core->initialize(KDevelop::Core::NoUi);

    auto doc_url = QDir::cleanPath(QStandardPaths::locate(QStandardPaths::GenericDataLocation,
                                                          "kdevpythonsupport/documentation_files/builtindocumentation.py"));

    DUChain::self()->updateContextForUrl(IndexedString(doc_url), KDevelop::TopDUContext::AllDeclarationsContextsAndUses);
    ICore::self()->languageController()->backgroundParser()->parseDocuments();
    DUChain::self()->waitForUpdate(IndexedString(doc_url), KDevelop::TopDUContext::AllDeclarationsContextsAndUses);

    DUChain::self()->disablePersistentStorage();
    KDevelop::CodeRepresentation::setDiskChangesForbidden(true);
}

ReferencedTopDUContext DUChainBench::parse(const QString& code)
{
    TestFile* testfile = new TestFile(code + "\n", "py", nullptr, testDir.absolutePath().append("/"));
    createdFiles << testfile;
    testfile->parse((TopDUContext::Features) (TopDUContext::ForceUpdate | TopDUContext::AST) );
    testfile->waitForParsed(2000);

    if ( testfile->isReady() ) {
        m_ast = static_cast<Python::ParseSession*>(testfile->topContext()->ast().data())->ast;
        return testfile->topContext();
    }
    else Q_ASSERT(false && "Timed out waiting for parser results, aborting all tests");
    return nullptr;
}

DUChainBench::~DUChainBench()
{
    foreach ( TestFile* f, createdFiles ) {
        delete f;
    }
    testDir.rmdir(testDir.absolutePath());
}

QString repeat_distinct(const QString& code, int count) {
    QString result;
    QString line;
    for ( int i = 0; i < count; i++ ) {
        line = code;
        result.append(line.replace(QString("%X"), QString::number(i)));
    }
    return result;
}

void DUChainBench::benchSimpleStatements_data()
{
    QTest::addColumn<QString>("code");

    // test assignment
    QTest::newRow("test_nondistinct_assignment_repeated") << QString("a=3\n").repeated(200);
    QTest::newRow("test_nondistinct_assignment_looped") << repeat_distinct(QString("a=%X\n"), 200);
    QTest::newRow("test_distinct_assignment_repeated") << repeat_distinct(QString("a%X=3\n"), 200);
    QTest::newRow("test_distinct_assignment_looped") << repeat_distinct(QString("a%X=%X\n"), 200);
    // test function
    QTest::newRow("test_bare_function") << repeat_distinct(QString("def main%X():\n    pass\n"), 100);
    QTest::newRow("test_return_function") << repeat_distinct(QString("def main%X():\n    return %X\n"), 100);
    QTest::newRow("test_arg_function_return_var") << repeat_distinct(QString("def func%X(arg):\n    return arg\na%X = func%X(3)\n"), 200);
    QTest::newRow("test_arg_function_return_fixed") << repeat_distinct(QString("def func%X(arg):\n    return 3\na%X = func%X()\n"), 200);
    // test if statements
    QTest::newRow("test_if_statement") << repeat_distinct(QString("if(True):\n    pass\n"), 200);
    QTest::newRow("test_if_else_statement") << repeat_distinct(QString("if(True):\n    pass\nelse:\n    pass\n"), 200);
    // test for loops
    QTest::newRow("test_for_loop") << repeat_distinct(QString("for i in range(20):\n    pass\n"), 100);
    QTest::newRow("test_for_loop_enum") << repeat_distinct(QString("for key, value in enumerate({1:2, 7:3}):\n    pass\n"), 200);
    QTest::newRow("test_for_loop_list") << repeat_distinct(QString("for key, value in [(3, 5), (7, 9)]:\n    pass\n"), 200);
}

void DUChainBench::benchSimpleStatements()
{
    QFETCH(QString, code);
    QBENCHMARK {
        parse(code);
    }
}
