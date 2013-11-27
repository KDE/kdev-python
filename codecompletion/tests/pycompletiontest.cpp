/*****************************************************************************
 *   Copyright 2012 Sven Brauch <svenbrauch@googlemail.com>                  *
 *                                                                           *
 *   This program is free software: you can redistribute it and/or modify    *
 *   it under the terms of the GNU General Public License as published by    *
 *   the Free Software Foundation, either version 2 of the License, or       *
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

#include <language/backgroundparser/backgroundparser.h>
#include <language/codecompletion/codecompletiontesthelper.h>
#include <language/duchain/declaration.h>
#include <language/codegen/coderepresentation.h>
#include <language/duchain/duchain.h>
#include <interfaces/ilanguagecontroller.h>

#include <tests/testcore.h>
#include <tests/autotestshell.h>

#include <QtTest/QTest>
#include <KUrl>
#include <KStandardDirs>
#include <KTextEditor/Editor>
#include <KService>

#include "codecompletion/context.h"
#include "codecompletion/helpers.h"

using namespace KDevelop;

QTEST_MAIN(Python::PyCompletionTest)

static int testId = 0;
static QString basepath = "/tmp/__kdevpythoncompletiontest.dir/";
static QFSFileEngine fileEngine;

namespace Python {

QStandardItemModel& fakeModel() {
  static QStandardItemModel model;
  model.setColumnCount(10);
  model.setRowCount(10);
  return model;
}

QString filenameForTestId(const int id) {
    return basepath + "test_" + QString::number(id) + ".py";
}

QString nextFilename() {
    testId += 1;
    return filenameForTestId(testId);
}

PyCompletionTest::PyCompletionTest(QObject* parent) : QObject(parent)
{
    initShell();
}

void makefile(QString filename, QString contents) {
    QFile fileptr;
    fileptr.setFileName(basepath + filename);
    fileptr.open(QIODevice::WriteOnly);
    fileptr.write(contents.toAscii());
    fileptr.close();
    KUrl url = KUrl(basepath + filename);
    url.cleanPath();
    kDebug() <<  "updating duchain for " << url.url() << basepath;
    const IndexedString urlstring(url);
    DUChain::self()->updateContextForUrl(urlstring, KDevelop::TopDUContext::ForceUpdate);
    ICore::self()->languageController()->backgroundParser()->parseDocuments();
    DUChain::self()->waitForUpdate(urlstring, KDevelop::TopDUContext::AllDeclarationsContextsAndUses);
}

void PyCompletionTest::initShell()
{
    AutoTestShell::init();
    TestCore* core = new TestCore();
    core->initialize(KDevelop::Core::NoUi);
    fileEngine.mkdir(basepath, false);
    
    KUrl doc_url = KUrl(KStandardDirs::locate("data", "kdevpythonsupport/documentation_files/builtindocumentation.py"));
    doc_url.cleanPath(KUrl::SimplifyDirSeparators);
    
    DUChain::self()->updateContextForUrl(IndexedString(doc_url), KDevelop::TopDUContext::AllDeclarationsContextsAndUses);
    ICore::self()->languageController()->backgroundParser()->parseDocuments();
    DUChain::self()->waitForUpdate(IndexedString(doc_url), KDevelop::TopDUContext::AllDeclarationsContextsAndUses);
    
    DUChain::self()->disablePersistentStorage();
    KDevelop::CodeRepresentation::setDiskChangesForbidden(true);
    
    // now, create a nice little completion hierarchy
    fileEngine.mkdir(basepath + "submoduledir", false);
    fileEngine.mkdir(basepath + "submoduledir/anothersubdir", false);
    makefile("toplevelmodule.py", "some_var = 3\ndef some_function(): pass\nclass some_class():\n def method(): pass");
    makefile("submoduledir/__init__.py", "var_in_sub_init = 5");
    makefile("submoduledir/subfile.py", "var_in_subfile = 5\nclass some_subfile_class():\n def method2(): pass");
    makefile("submoduledir/anothersubdir/__init__.py", "var_in_subsub_init = 5");
    makefile("submoduledir/anothersubdir/subsubfile.py", "var_in_subsubfile = 5\nclass another_subfile_class():"
                                                      "\n def method3(): pass");
}

void PyCompletionTest::testIdentifierMatching()
{
    QCOMPARE(camelCaseToUnderscore("FooBarBaz").toAscii().data(), "foo_bar_baz");
    QCOMPARE(camelCaseToUnderscore("fooBarbaz").toAscii().data(),  "foo_barbaz");

    QCOMPARE(identifierMatchQuality("foobar", "foobar"),  3);
    QCOMPARE(identifierMatchQuality("foobar", "bar"),  2);
    QCOMPARE(identifierMatchQuality("bar", "foobar"),  2);
    QCOMPARE(identifierMatchQuality("foobarbaz", "bar"),  2);
    QCOMPARE(identifierMatchQuality("bar", "foobarbaz"),  2);
    QCOMPARE(identifierMatchQuality("FoobarBaz", "FoobarBang"), 1);
    QCOMPARE(identifierMatchQuality("Foobar_Baz", "Foobar_Bang"), 1);
    QCOMPARE(identifierMatchQuality("xydsf", "qkigfb"), 0);
    QCOMPARE(identifierMatchQuality("ac_ac", "ac_ae"), 0);
    QCOMPARE(identifierMatchQuality("AcAb", "AbDe"), 0);
}

void PyCompletionTest::testExpressionParserMisc()
{
    // in completion, strings are filtered out and never contain " or ' chars.
    ExpressionParser p("foobar(3, \"some_string\", func(), funcfunc(3, 5), \t");
    bool ok;
    int expressionsSkipped = 0;
    p.skipUntilStatus(ExpressionParser::EventualCallFound, &ok, &expressionsSkipped);
    QVERIFY(ok);
    QCOMPARE(expressionsSkipped, 4); // number of params
    QCOMPARE(p.getRemainingCode(), QString("foobar"));
    ExpressionParser::Status s;
    QString calledFunction = p.popExpression(&s);
    QVERIFY(s == ExpressionParser::ExpressionFound);
    QCOMPARE(calledFunction, QString("foobar"));
    
    ExpressionParser q("hello(world, foo.bar[3].foobar(3, \"some_string\", func(), funcfunc(3, 5), \t");
    q.skipUntilStatus(ExpressionParser::EventualCallFound, &ok, &expressionsSkipped);
    QVERIFY(ok);
    QCOMPARE(expressionsSkipped, 4);
    QCOMPARE(q.getRemainingCode(), QString("hello(world, foo.bar[3].foobar"));
    calledFunction = q.popExpression(&s);
    QCOMPARE(s, ExpressionParser::ExpressionFound);
    QCOMPARE(calledFunction, QString("foo.bar[3].foobar"));
}

void PyCompletionTest::testExpressionParser()
{
    QFETCH(QString, data);
    QFETCH(int, expectedStatus);
    QFETCH(QString, expectedExpression);
    
    ExpressionParser p(data);
    ExpressionParser::Status status;
    QString result = p.popExpression(&status);
    QCOMPARE((int) status, expectedStatus);
    QCOMPARE(result, expectedExpression);
}

void PyCompletionTest::testExpressionParser_data()
{
    QTest::addColumn<QString>("data");
    QTest::addColumn<int>("expectedStatus");
    QTest::addColumn<QString>("expectedExpression");
    
    QTest::newRow("attrExpression") << "foo.bar.baz" << (int) ExpressionParser::ExpressionFound << "foo.bar.baz";
    QTest::newRow("attrExpressionAccess") << "foo.bar.baz." << (int) ExpressionParser::MemberAccessFound << "";
    QTest::newRow("attrExpressionCall") << "foo.bar(3, 5, 7, hell0(3)).baz" << (int) ExpressionParser::ExpressionFound << "foo.bar(3, 5, 7, hell0(3)).baz";
    QTest::newRow("nextArg") << "foo(3, 5, \t" << (int) ExpressionParser::CommaFound << "";
    QTest::newRow("call") << "fo0barR( \t  " << (int) ExpressionParser::EventualCallFound << "";
    QTest::newRow("initializer") << "my_list = [" << (int) ExpressionParser::InitializerFound << "";
    QTest::newRow("fancy_initializer") << "my_list = [1, 2, 3, 4, []" << (int) ExpressionParser::ExpressionFound << "[]";
    QTest::newRow("def") << "def " << (int) ExpressionParser::DefFound << "";
}

const QList<CompletionTreeItem*> PyCompletionTest::invokeCompletionOn(const QString& initCode, const QString& invokeCode)
{
    QString filename = nextFilename();
    QFile fileptr(filename);
    fileptr.open(QIODevice::WriteOnly);
    fileptr.write(initCode.toAscii().replace("%INVOKE", ""));
    fileptr.close();
    
    DUChain::self()->updateContextForUrl(IndexedString(filename), KDevelop::TopDUContext::ForceUpdate);
    ICore::self()->languageController()->backgroundParser()->parseDocuments();
    ReferencedTopDUContext topContext = DUChain::self()->waitForUpdate(IndexedString(filename),
                                                                       KDevelop::TopDUContext::AllDeclarationsAndContexts);
    
    Q_ASSERT(topContext);
    
    Q_ASSERT(initCode.indexOf("%INVOKE") != -1);
    QString copy = initCode;
    QString allCode = copy.replace("%INVOKE", invokeCode);
    
    QStringList lines = allCode.split('\n');
    CursorInRevision cursorAt = CursorInRevision::invalid();
    for ( int i = 0; i < lines.length(); i++ ) {
        int j = lines.at(i).indexOf("%CURSOR");
        if ( j != -1 ) {
            cursorAt = CursorInRevision(i, j);
            break;
        }
    }
    Q_ASSERT(cursorAt.isValid());
    // codeCompletionContext only gets passed the text until the place where completion is invoked
    QString snip = allCode.mid(0, allCode.indexOf("%CURSOR"));
    QString remaining = allCode.mid(allCode.indexOf("%CURSOR"));
    
    DUChainReadLocker lock;
    DUContextPointer contextAtCursor = DUContextPointer(topContext->findContextAt(cursorAt, true));
    Q_ASSERT(contextAtCursor);
    
    PythonCodeCompletionContext* context = new PythonCodeCompletionContext(contextAtCursor, snip, remaining, cursorAt, 0, 0);
    bool abort = false;
    QList<CompletionTreeItem*> items;
    lock.unlock();
    foreach ( CompletionTreeItemPointer ptr, context->completionItems(abort, true) ) {
        items << ptr.data();
        // those are leaked, but it's only a few kb while the tests are running. who cares.
        m_ptrs << ptr;
    }
    return items;
}

bool PyCompletionTest::containsItemForDeclarationNamed(const QList<CompletionTreeItem*> items, QString itemName)
{
    foreach ( const CompletionTreeItem* ptr, items ) {
        if ( ptr->declaration() ) {
            if ( ptr->declaration()->identifier().toString() == itemName ) {
                return true;
            }
        }
    }
    return false;
}

bool PyCompletionTest::containsItemStartingWith(const QList<CompletionTreeItem*> items, const QString& itemName)
{
    QModelIndex idx = fakeModel().index(0, KDevelop::CodeCompletionModel::Name);
    foreach ( const CompletionTreeItem* ptr, items ) {
        if ( ptr->data(idx, Qt::DisplayRole, 0).toString().startsWith(itemName) ) {
            return true;
        }
    }
    return false;
}

bool PyCompletionTest::itemInCompletionList(const QString& initCode, const QString& invokeCode, QString itemName)
{
    QList< CompletionTreeItem* > items = invokeCompletionOn(initCode, invokeCode);
    return containsItemStartingWith(items, itemName);
}

bool PyCompletionTest::declarationInCompletionList(const QString& initCode, const QString& invokeCode, QString itemName)
{
    QList< CompletionTreeItem* > items = invokeCompletionOn(initCode, invokeCode);
    return containsItemForDeclarationNamed(items, itemName);
}

bool PyCompletionTest::completionListIsEmpty(const QString& initCode, const QString& invokeCode)
{
    return invokeCompletionOn(initCode, invokeCode).isEmpty();
}

void PyCompletionTest::testImportCompletion()
{
    QFETCH(QString, invokeCode);
    QFETCH(QString, completionCode);
    QFETCH(QString, expectedItem);

    if ( expectedItem == "EMPTY" ) {
        QVERIFY(completionListIsEmpty(invokeCode, completionCode));
    }
    else {
        QVERIFY(itemInCompletionList(invokeCode, completionCode, expectedItem));
    }
}

void PyCompletionTest::testImportCompletion_data()
{
    QTest::addColumn<QString>("invokeCode");
    QTest::addColumn<QString>("completionCode");
    QTest::addColumn<QString>("expectedItem");
    
    QTest::newRow("same_directory") << "%INVOKE" << "import %CURSOR" << "toplevelmodule";
//     QTest::newRow("same_directory_beginText") << "%INVOKE" << "import toplevelmo%CURSOR" << "toplevelmodule";
    QTest::newRow("nocompletion") << "%INVOKE" << "from toplevelmodule %CURSOR" << "EMPTY";
    QTest::newRow("subdirectory_full") << "%INVOKE" << "import %CURSOR" << "submoduledir";
    QTest::newRow("subdirectory_file") << "%INVOKE" << "import submoduledir.%CURSOR" << "subfile";
    QTest::newRow("subsubdirectory_file") << "%INVOKE" << "import submoduledir.anothersubdir.%CURSOR" << "subsubfile";
    QTest::newRow("subdirectory_from") << "%INVOKE" << "from submoduledir import %CURSOR" << "subfile";
    QTest::newRow("subdirectory_declfromfile") << "%INVOKE" << "from submoduledir.subfile import %CURSOR" << "var_in_subfile";
    QTest::newRow("declaration_from_init_subdir") << "%INVOKE" << "from submoduledir import %CURSOR" << "var_in_sub_init";
    QTest::newRow("class_from_file") << "%INVOKE" << "from toplevelmodule import %CURSOR" << "some_class";
    // TODO implement this or not? It breaks the possibility to easily document modules like PyQT.
    // maybe enable this behaviour only for doc files?
//     QTest::newRow("class_property_not") << "%INVOKE" << "import toplevelmodule.some_class.%CURSOR" << "EMPTY";
    QTest::newRow("class_from_file_in_subdir") << "%INVOKE" << "from submoduledir.subfile import %CURSOR" << "some_subfile_class";
}

void PyCompletionTest::testCompletionAfterQuotes()
{
    QFETCH(QString, invokeCode);
    QFETCH(QString, completionCode);
    invokeCode = "testvar = 3\n" + invokeCode;
    QVERIFY( ! completionListIsEmpty(invokeCode, completionCode) );
}


void PyCompletionTest::testCompletionAfterQuotes_data()
{
    QTest::addColumn<QString>("invokeCode");
    QTest::addColumn<QString>("completionCode");
    
    QTest::newRow("nothing") << "\n%INVOKE" << "%CURSOR";
    QTest::newRow("sq_in_string") << "\"foo'bar\"\n%INVOKE" << "%CURSOR";
    QTest::newRow("sq_in_sl_comment") << "#foo'bar\n%INVOKE" << "%CURSOR";
    QTest::newRow("sq_in_ml_string") << "\"\"\"foo'bar\n\n' \n'\"\"\"\n%INVOKE" << "%CURSOR";
    QTest::newRow("dq_in_string") << "'foo\"bar'\n%INVOKE" << "%CURSOR";
    QTest::newRow("dq_in_comment") << "# \" foo\n%INVOKE" << "%CURSOR";
    QTest::newRow("dq_in_ml_string") << "\'\'\'foo \n\"\n\n \'\'\'\n%INVOKE" << "%CURSOR";
}

void PyCompletionTest::testNoImplicitMagicFunctions()
{
    QVERIFY(! itemInCompletionList("class my(): pass\nd = my()\n%INVOKE", "d.%CURSOR", "__get__") );
    QEXPECT_FAIL("", "Sorting needs to be fixed first before magic function completion can be re-enabled", Continue);
    QVERIFY(itemInCompletionList("class my():\n def __get__(self): pass\nd = my()\n%INVOKE", "d.%CURSOR", "__get__") );
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
    QTest::newRow("print_stmt") << "%INVOKE" << "print([].%CURSOR" << "append";
}

void PyCompletionTest::testIgnoreCommentSignsInStringLiterals()
{
    QVERIFY( ! completionListIsEmpty("'#'%INVOKE", ".%CURSOR") );
    QVERIFY( ! completionListIsEmpty("def addEntry(self,array):\n"
                                     "  \"\"\"\"some comment\"\"\"\n  %INVOKE", "%CURSOR") );
}

void PyCompletionTest::testNoCompletionInCommentsOrStrings()
{
    QFETCH(QString, invokeCode);
    QFETCH(QString, completionCode);
    
    QVERIFY(! declarationInCompletionList(invokeCode, completionCode, "append"));
}

void PyCompletionTest::testNoCompletionInCommentsOrStrings_data()
{
    QTest::addColumn<QString>("invokeCode");
    QTest::addColumn<QString>("completionCode");
    
    QTest::newRow("single_comment") << "# []%INVOKE" << ".%CURSOR";
    QTest::newRow("single_comment_local") << "local=3\n# %INVOKE" << "%CURSOR";
    QTest::newRow("stringDQ") << "\"[]%INVOKE\"" << ".%CURSOR";
    QTest::newRow("stringSQ") << "\'[]%INVOKE\'" << ".%CURSOR";
    QTest::newRow("multilineDQ") << "\"\"\"[]%INVOKE\"\"\"" << ".%CURSOR";
    QTest::newRow("multilineSQ") << "\'\'\'[]%INVOKE\'\'\'" << ".%CURSOR";
    QTest::newRow("multilineDQ_newlines") << "\"\"\"\n\n[]%INVOKE\n\n\n\"\"\"" << ".%CURSOR";
    QTest::newRow("multilineSQ_newlines") << "\'\'\'\n\n[]%INVOKE\n\n\n\'\'\'" << ".%CURSOR";
}

void PyCompletionTest::testImplementMethodCompletion()
{
    QFETCH(QString, invokeCode);
    QFETCH(QString, completionCode);
    QVERIFY(itemInCompletionList(invokeCode, completionCode, "__init__"));
}

void PyCompletionTest::testImplementMethodCompletion_data()
{
    QTest::addColumn<QString>("invokeCode");
    QTest::addColumn<QString>("completionCode");
    
    QTest::newRow("simple_begin") << "class myclass():\n %INVOKE\n pass" << "def %CURSOR";
    QTest::newRow("another_method_before") << "class myclass():\n def some_method(param):pass\n %INVOKE" << "def %CURSOR";
    QTest::newRow("another_method_before_multiline") << "class myclass():\n def some_method(param):\n  pass\n  pass \n  pass"
                                                        "\n %INVOKE" << "def %CURSOR";
    QTest::newRow("contextskip") << "class myclass():\n def some_method(param):\n  pass\n \n \n \n %INVOKE" << "def %CURSOR";
    QTest::newRow("contextskip2") << "class myclass():\n def some_method(param): pass\n"
                                     " def some_method2(param):\n  pass\n  pass\n %INVOKE" << "\n \n \n def %CURSOR";
}

void PyCompletionTest::testAutoBrackets()
{
    QList< CompletionTreeItem* > items = invokeCompletionOn("class Foo:\n @property\n def myprop(self): pass\n"
                                                            "a=Foo()\n%INVOKE", "a.%CURSOR");
    QVERIFY(containsItemForDeclarationNamed(items, "myprop"));
    CompletionTreeItem* item = 0;
    foreach ( CompletionTreeItem* ptr, items ) {
        if ( ptr->declaration() ) {
            if ( ptr->declaration()->identifier().toString() == "myprop" ) {
                item = ptr;
                break;
            }
        }
    }
    QVERIFY(item);
    KService::Ptr documentService = KService::serviceByDesktopPath("katepart.desktop");
    QVERIFY(documentService);
    KTextEditor::Document* document = documentService->createInstance<KTextEditor::Document>(this);
    QVERIFY(document);
    item->execute(document, KTextEditor::Range(0, 0, 0, 0));
    QCOMPARE(document->text(), QLatin1String("myprop"));
}

void PyCompletionTest::testExceptionCompletion()
{
    QList< CompletionTreeItem* > items = invokeCompletionOn("localvar = 3\nraise %INVOKE", "%CURSOR");
    QVERIFY(containsItemForDeclarationNamed(items, "Exception"));
    QVERIFY(! containsItemForDeclarationNamed(items, "localvar"));
    
    items = invokeCompletionOn("localvar = 3\n%INVOKE", "try: pass\nexcept %CURSOR");
    QVERIFY(containsItemForDeclarationNamed(items, "Exception"));
    QVERIFY(! containsItemForDeclarationNamed(items, "localvar"));
}

void PyCompletionTest::testGeneratorCompletion()
{
    QVERIFY(itemInCompletionList("%INVOKE", "foobar = [item for %CURSOR", "item in"));
    QVERIFY(itemInCompletionList("%INVOKE\ndec_l8r=3", "foobar = [dec_l8r for %CURSOR", "dec_l8r in"));
}

void PyCompletionTest::testInheritanceCompletion()
{
    QList< CompletionTreeItem* > items = invokeCompletionOn("class parentClass: pass\n%INVOKE", "class childClass(%CURSOR");
    QVERIFY(containsItemForDeclarationNamed(items, "parentClass"));
    items = invokeCompletionOn("class parentClass: pass\nclass childClass(%INVOKE): pass", "%CURSOR");
    QVERIFY(containsItemForDeclarationNamed(items, "parentClass"));
    items = invokeCompletionOn("class parentClass:\n class blubb: pass\nclass childClass(%INVOKE): pass", "parentClass.%CURSOR");
    QVERIFY(! containsItemForDeclarationNamed(items, "parentClass"));
    QVERIFY(containsItemForDeclarationNamed(items, "blubb"));
}

void PyCompletionTest::testAddImportCompletion()
{
    QFETCH(QString, completionCode);
    QFETCH(QString, invokeCode);
    QFETCH(int, expectedItems);

    QCOMPARE(invokeCompletionOn(completionCode, invokeCode).size(), expectedItems);
}

void PyCompletionTest::testAddImportCompletion_data()
{
    QTest::addColumn<QString>("completionCode");
    QTest::addColumn<QString>("invokeCode");
    QTest::addColumn<int>("expectedItems");

    QTest::newRow("has_entry_when_necessary") << "toplevelmodule%INVOKE" << ".%CURSOR" << 1;
    QTest::newRow("has_no_when_not_necessary") << "toplevelmodule = 3;\ntoplevelmodule%INVOKE" << ".%CURSOR" << 0;
}

void PyCompletionTest::testStringFormattingCompletion()
{
    QFETCH(QString, completionCode);
    QFETCH(QString, invokeCode);

    QVERIFY(itemInCompletionList(completionCode, invokeCode, "{0}"));
}

void PyCompletionTest::testStringFormattingCompletion_data()
{
    QTest::addColumn<QString>("completionCode");
    QTest::addColumn<QString>("invokeCode");

    QTest::newRow("sq_string") << "\"foo %INVOKE\"" << "%CURSOR";
    QTest::newRow("dq_string") << "'foo %INVOKE bar'" << "%CURSOR";

}



}


