/*****************************************************************************
 *   Copyright 2012 Sven Brauch <svenbrauch@googlemail.com>                  *
 *                                                                           *
 *   This program is free software: you can redistribute it and/or modify    *
 *   it under the terms of the GNU General Public License as published by    *
 *   the Free Software Foundation, either version 3 of the License, or       *
 *   (at your option) any later version.                                     *
 *                                                                           *
 *   This program is distributed in the hope that it will be useful,         *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of          *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           *
 *   GNU General Public License for more details.                            *
 *                                                                           *
 *   You should have received a copy of the GNU General Public License       *
 *   along with this program.  If not, see <http://www.gnu.org/licenses/>    *
 *****************************************************************************/

#include "pycompletiontest.h"
#include <pythoncodecompletioncontext.h>
#include <language/duchain/declaration.h>
#include <language/codegen/coderepresentation.h>
#include <language/duchain/duchain.h>
#include <tests/testcore.h>
#include <tests/autotestshell.h>
#include <KUrl>
#include <KStandardDirs>

#include <QtTest/QTest>

using namespace KDevelop;

QTEST_MAIN(Python::PyCompletionTest)

static int testId = 0;

namespace Python {
    

QString filenameForTestId(const int id) {
    return "/tmp/__kdevpythoncompletiontest_" + QString::number(id) + ".py";
}

QString nextFilename() {
    testId += 1;
    return filenameForTestId(testId);
}

PyCompletionTest::PyCompletionTest(QObject* parent) : QObject(parent)
{
    initShell();
}

void PyCompletionTest::initShell()
{
    AutoTestShell::init();
    TestCore* core = new TestCore();
    core->initialize(KDevelop::Core::NoUi);
    
    KUrl doc_url = KUrl(KStandardDirs::locate("data", "kdevpythonsupport/documentation_files/builtindocumentation.py"));
    doc_url.cleanPath(KUrl::SimplifyDirSeparators);
    
    DUChain::self()->updateContextForUrl(IndexedString(doc_url), KDevelop::TopDUContext::AllDeclarationsContextsAndUses);
    DUChain::self()->waitForUpdate(IndexedString(doc_url), KDevelop::TopDUContext::AllDeclarationsContextsAndUses);
    
    DUChain::self()->disablePersistentStorage();
    KDevelop::CodeRepresentation::setDiskChangesForbidden(true);
}

QList< CompletionTreeItemPointer > PyCompletionTest::invokeCompletionOn(const QString& initCode, const QString& invokeCode)
{
    QString filename = nextFilename();
    QFile fileptr(filename);
    fileptr.open(QIODevice::WriteOnly);
    fileptr.write(initCode.toAscii().replace("%INVOKE", ""));
    fileptr.close();
    DUChain::self()->updateContextForUrl(IndexedString(filename), KDevelop::TopDUContext::ForceUpdate);
    ReferencedTopDUContext topContext = DUChain::self()->waitForUpdate(IndexedString(filename),
                                                                       KDevelop::TopDUContext::AllDeclarationsAndContexts);
    
    Q_ASSERT(topContext);
    
    Q_ASSERT(initCode.indexOf("%INVOKE") != -1);
    QString copy = initCode;
    QString allCode = copy.replace("%INVOKE", invokeCode);
    QStringList lines = allCode.split('\n');
    CursorInRevision cursorAt = CursorInRevision::invalid();
    for ( int i = 0; i < lines.length(); i++ ) {
        if ( int j = lines.at(i).indexOf("%CURSOR") != -1 ) {
            cursorAt = CursorInRevision(i, j);
            break;
        }
    }
    Q_ASSERT(cursorAt.isValid());
    allCode = allCode.replace("%CURSOR", "");
    
    DUContextPointer contextAtCursor = DUContextPointer(topContext->findContextAt(cursorAt, true));
    Q_ASSERT(contextAtCursor);
    
    PythonCodeCompletionContext codeCompletionContext(contextAtCursor, allCode, cursorAt, 0, 0);
    bool abort = false;
    return codeCompletionContext.completionItems(abort, true);
}

bool PyCompletionTest::containsItemForDeclarationNamed(QList< CompletionTreeItemPointer > items, QString itemName)
{
    foreach ( const CompletionTreeItemPointer ptr, items ) {
        if ( ptr->declaration() ) {
            if ( ptr->declaration()->identifier().toString() == itemName ) {
                return true;
            }
        }
    }
    return false;
}

bool PyCompletionTest::declarationInCompletionList(const QString& initCode, const QString& invokeCode, QString itemName)
{
    return containsItemForDeclarationNamed(invokeCompletionOn(initCode, invokeCode), itemName);
}

bool PyCompletionTest::completionListIsEmpty(const QString& initCode, const QString& invokeCode)
{
    return invokeCompletionOn(initCode, invokeCode).isEmpty();
}

void PyCompletionTest::testIntegralTypesImmediate()
{
    QFETCH(QString, invokeCode);
    QFETCH(QString, completionCode);
    QFETCH(QString, expectedDeclaration);
    
    QVERIFY(declarationInCompletionList(invokeCode, completionCode, expectedDeclaration));
}

void PyCompletionTest::testIntegralTypesImmediate_data()
{
    QTest::addColumn<QString>("invokeCode");
    QTest::addColumn<QString>("completionCode");
    QTest::addColumn<QString>("expectedDeclaration");
    
    QTest::newRow("list_syntax") << "[]%INVOKE" << ".%CURSOR" << "append";
    QTest::newRow("dict_syntax") << "{}%INVOKE" << ".%CURSOR" << "items";
    QTest::newRow("string_syntax") << "\"\"%INVOKE" << ".%CURSOR" << "capitalize";
    QTest::newRow("list_class") << "list()%INVOKE" << ".%CURSOR" << "append";
    QTest::newRow("dict_class") << "dict()%INVOKE" << ".%CURSOR" << "items";
    QTest::newRow("string_class") << "str()%INVOKE" << ".%CURSOR" << "capitalize";
}

void PyCompletionTest::testIntegralExpressionsDifferentContexts()
{
    QFETCH(QString, invokeCode);
    QFETCH(QString, completionCode);
    QFETCH(QString, expectedDeclaration);
    
    QVERIFY(declarationInCompletionList(invokeCode, completionCode, expectedDeclaration));
}

void PyCompletionTest::testIntegralExpressionsDifferentContexts_data()
{
    QTest::addColumn<QString>("invokeCode");
    QTest::addColumn<QString>("completionCode");
    QTest::addColumn<QString>("expectedDeclaration");
    
    QTest::newRow("function_call") << "foo([]%INVOKE)" << ".%CURSOR" << "append";
    QTest::newRow("function_call_multi") << "foo(bar(baz(bang([]%INVOKE))))" << ".%CURSOR" << "append";
    QTest::newRow("empty_list") << "[[]%INVOKE]" << ".%CURSOR" << "append";
    QTest::newRow("list") << "[1, 2, 3, 4, 5, []%INVOKE]" << ".%CURSOR" << "append";
    QTest::newRow("list_with_fancy_string") << "[\"FooFObar\\\", 3)\", []%INVOKE]" << ".%CURSOR" << "append";
    QTest::newRow("empty_dict") << "{[]%INVOKE}" << ".%CURSOR" << "append";
    QTest::newRow("print_stmt") << "print []%INVOKE" << ".%CURSOR" << "append";
}

void PyCompletionTest::testNoCompletionInCommentsOrStrings()
{
    QFETCH(QString, invokeCode);
    QFETCH(QString, completionCode);
    
    QVERIFY(completionListIsEmpty(invokeCode, completionCode));
}

void PyCompletionTest::testNoCompletionInCommentsOrStrings_data()
{
    QTest::addColumn<QString>("invokeCode");
    QTest::addColumn<QString>("completionCode");
    
    QTest::newRow("single_comment") << "# []%INVOKE" << ".%CURSOR";
    QTest::newRow("stringDQ") << "\"[]%INVOKE\"" << ".%CURSOR";
    QTest::newRow("stringSQ") << "\'[]%INVOKE\'" << ".%CURSOR";
    QTest::newRow("multilineDQ") << "\"\"\"[]%INVOKE\"\"\"" << ".%CURSOR";
    QTest::newRow("multilineSQ") << "\'\'\'[]%INVOKE\'\'\'" << ".%CURSOR";
    QTest::newRow("multilineDQ_newlines") << "\"\"\"\n\n[]%INVOKE\n\n\n\"\"\"" << ".%CURSOR";
    QTest::newRow("multilineSQ_newlines") << "\'\'\'\n\n[]%INVOKE\n\n\n\'\'\'" << ".%CURSOR";
}

}


