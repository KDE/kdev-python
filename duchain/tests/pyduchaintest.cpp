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

#include "pyduchaintest.h"

#include <language/duchain/topducontext.h>
#include <language/duchain/dumpchain.h>
#include <language/codegen/coderepresentation.h>
#include <tests/autotestshell.h>
#include <tests/testcore.h>
#include <language/duchain/duchain.h>
#include <QtTest/QtTest>
#include <parsesession.h>
#include <pythoneditorintegrator.h>
#include <declarationbuilder.h>
#include <usebuilder.h>

QTEST_MAIN(PyDUChainTest)

using namespace KDevelop;
using namespace Python;

PyDUChainTest::PyDUChainTest(QObject* parent): QObject(parent)
{
    initShell();
}

void PyDUChainTest::initShell()
{
  AutoTestShell::init();
  TestCore* core = new TestCore();
  core->initialize(KDevelop::Core::NoUi);

  DUChain::self()->disablePersistentStorage();
  KDevelop::CodeRepresentation::setDiskChangesForbidden(true);
}

ReferencedTopDUContext PyDUChainTest::parse(const QByteArray& code)
{
    ParseSession* session = new ParseSession;
    session->setContents( code + "\n" ); // append a newline in case the parser doesnt like it without one
    
    static int mytest=0;
    KUrl filename("/test"+QString::number(mytest++));
    session->setCurrentDocument(filename);
    
    QPair<CodeAst*, bool> parserResults = session->parse(0);
    CodeAst* ast = parserResults.first;
    
    if(!parserResults.second)
        return 0;
    
    PythonEditorIntegrator editor;
    DeclarationBuilder builder( &editor );
    
    editor.setParseSession(session);
    
    ReferencedTopDUContext ret = builder.build(IndexedString(filename), ast);
    
    {
        DUChainWriteLocker lock(DUChain::lock());
//         ParsingEnvironmentFilePointer parsingEnvironmentFile = ret->parsingEnvironmentFile();
//         parsingEnvironmentFile->clearModificationRevisions();
//         parsingEnvironmentFile->setModificationRevision(contents().modification);
//         DUChain::self()->updateContextEnvironment(m_duContext, parsingEnvironmentFile.data());
        ret->clearProblems();
    }
    
    UseBuilder usebuilder( &editor );
    usebuilder.buildUses(ast);
    
    return ret;
}

void PyDUChainTest::testSimple()
{
    QFETCH(QString, code);
    QFETCH(int, decls);
    QFETCH(int, uses);
    
    ReferencedTopDUContext ctx = parse(code.toLatin1());
    QVERIFY(ctx);
    
    DUChainReadLocker lock(DUChain::lock());
    QVector< Declaration* > declarations = ctx->localDeclarations(ctx);
    
    QCOMPARE(declarations.size(), decls);
    
    int usesCount = 0;
    foreach(Declaration* d, declarations) {
        usesCount += d->uses().size();
        
        QVERIFY(!d->abstractType().isNull());
    }
    
    QCOMPARE(usesCount, uses);
}

void PyDUChainTest::testSimple_data()
{
    QTest::addColumn<QString>("code");
    QTest::addColumn<int>("decls");
    QTest::addColumn<int>("uses");
    
    QTest::newRow("assign") << "b = 2;" << 1 << 0;
    QTest::newRow("assign_str") << "b = 'hola';" << 1 << 0;
    QTest::newRow("op") << "a = 3; b = a+2;" << 2 << 1;
}
