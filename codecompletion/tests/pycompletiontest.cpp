/*
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#include "pycompletiontest.h"

#include <language/backgroundparser/backgroundparser.h>
#include <language/codecompletion/codecompletiontesthelper.h>
#include <language/duchain/declaration.h>
#include <language/codegen/coderepresentation.h>
#include <language/duchain/duchain.h>
#include <interfaces/ilanguagecontroller.h>

#include <tests/testcore.h>
#include <tests/autotestshell.h>

#include <ktexteditor_version.h>
#include <KTextEditor/Editor>
#include <KService>

#include "codecompletion/context.h"
#include "codecompletion/helpers.h"
#include "codecompletiondebug.h"

#include <QDebug>
#include <QStandardPaths>
#include <QTest>

using namespace KDevelop;

QTEST_MAIN(Python::PyCompletionTest)

Q_DECLARE_METATYPE(QList<Python::RangeInString>)

static int testId = 0;
static QString basepath = QStringLiteral("/tmp/__kdevpythoncompletiontest.dir/");

namespace Python {

QStandardItemModel& fakeModel() {
  static QStandardItemModel model;
  model.setColumnCount(10);
  model.setRowCount(10);
  return model;
}

QString filenameForTestId(const int id) {
    return basepath + QStringLiteral("test_") + QString::number(id) + QStringLiteral(".py");
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
    fileptr.write(contents.toUtf8());
    fileptr.close();
    auto url = QUrl::fromLocalFile(QDir::cleanPath(basepath + filename));
    qCDebug(KDEV_PYTHON_CODECOMPLETION) <<  "updating duchain for " << url.url() << basepath;
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
    QDir d;
    d.mkpath(basepath);

    auto doc_url = QDir::cleanPath(QStandardPaths::locate(QStandardPaths::GenericDataLocation,
                                                          QStringLiteral("kdevpythonsupport/documentation_files/builtindocumentation.py")));

    DUChain::self()->updateContextForUrl(IndexedString(doc_url), KDevelop::TopDUContext::AllDeclarationsContextsAndUses);
    ICore::self()->languageController()->backgroundParser()->parseDocuments();
    DUChain::self()->waitForUpdate(IndexedString(doc_url), KDevelop::TopDUContext::AllDeclarationsContextsAndUses);

    DUChain::self()->disablePersistentStorage();
    KDevelop::CodeRepresentation::setDiskChangesForbidden(true);

    // now, create a nice little completion hierarchy
    d.mkpath(basepath + QStringLiteral("submoduledir"));
    d.mkpath(basepath + QStringLiteral("submoduledir/anothersubdir"));
    makefile(QStringLiteral("toplevelmodule.py"), QStringLiteral("some_var = 3\ndef some_function(): pass\nclass some_class():\n def method(): pass"));
    makefile(QStringLiteral("submoduledir/__init__.py"), QStringLiteral("var_in_sub_init = 5"));
    makefile(QStringLiteral("submoduledir/subfile.py"), QStringLiteral("var_in_subfile = 5\nclass some_subfile_class():\n def method2(): pass"));
    makefile(QStringLiteral("submoduledir/anothersubdir/__init__.py"), QStringLiteral("var_in_subsub_init = 5"));
    makefile(QStringLiteral("submoduledir/anothersubdir/subsubfile.py"), QStringLiteral("var_in_subsubfile = 5\nclass another_subfile_class():"
                                                      "\n def method3(): pass"));
}

void PyCompletionTest::testIdentifierMatching()
{
    QCOMPARE(camelCaseToUnderscore(QStringLiteral("FooBarBaz")).toUtf8().data(), "foo_bar_baz");
    QCOMPARE(camelCaseToUnderscore(QStringLiteral("fooBarbaz")).toUtf8().data(),  "foo_barbaz");

    QCOMPARE(identifierMatchQuality(QStringLiteral("foobar"), QStringLiteral("foobar")),  3);
    QCOMPARE(identifierMatchQuality(QStringLiteral("foobar"), QStringLiteral("bar")),  2);
    QCOMPARE(identifierMatchQuality(QStringLiteral("bar"), QStringLiteral("foobar")),  2);
    QCOMPARE(identifierMatchQuality(QStringLiteral("foobarbaz"), QStringLiteral("bar")),  2);
    QCOMPARE(identifierMatchQuality(QStringLiteral("bar"), QStringLiteral("foobarbaz")),  2);
    QCOMPARE(identifierMatchQuality(QStringLiteral("FoobarBaz"), QStringLiteral("FoobarBang")), 1);
    QCOMPARE(identifierMatchQuality(QStringLiteral("Foobar_Baz"), QStringLiteral("Foobar_Bang")), 1);
    QCOMPARE(identifierMatchQuality(QStringLiteral("xydsf"), QStringLiteral("qkigfb")), 0);
    QCOMPARE(identifierMatchQuality(QStringLiteral("ac_ac"), QStringLiteral("ac_ae")), 0);
    QCOMPARE(identifierMatchQuality(QStringLiteral("AcAb"), QStringLiteral("AbDe")), 0);
}

void PyCompletionTest::testExpressionParserMisc()
{
    // in completion, strings are filtered out and never contain " or ' chars.
    ExpressionParser p(QStringLiteral("foobar(3, \"some_string\", func(), funcfunc(3, 5), \t"));
    bool ok;
    int expressionsSkipped = 0;
    p.skipUntilStatus(ExpressionParser::EventualCallFound, &ok, &expressionsSkipped);
    QVERIFY(ok);
    QCOMPARE(expressionsSkipped, 4); // number of params
    QCOMPARE(p.getRemainingCode(), QString(QStringLiteral("foobar")));
    ExpressionParser::Status s;
    QString calledFunction = p.popExpression(&s);
    QVERIFY(s == ExpressionParser::ExpressionFound);
    QCOMPARE(calledFunction, QString(QStringLiteral("foobar")));

    ExpressionParser q(QStringLiteral("hello(world, foo.bar[3].foobar(3, \"some_string\", func(), funcfunc(3, 5), \t"));
    q.skipUntilStatus(ExpressionParser::EventualCallFound, &ok, &expressionsSkipped);
    QVERIFY(ok);
    QCOMPARE(expressionsSkipped, 4);
    QCOMPARE(q.getRemainingCode(), QString(QStringLiteral("hello(world, foo.bar[3].foobar")));
    calledFunction = q.popExpression(&s);
    QCOMPARE(s, ExpressionParser::ExpressionFound);
    QCOMPARE(calledFunction, QString(QStringLiteral("foo.bar[3].foobar")));
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
    CompletionParameters data = prepareCompletion(initCode, invokeCode);
    return runCompletion(data);
}

const CompletionParameters PyCompletionTest::prepareCompletion(const QString& initCode, const QString& invokeCode)
{
    CompletionParameters completion_data;

    QString filename = nextFilename();
    QFile fileptr(filename);
    fileptr.open(QIODevice::WriteOnly);
    fileptr.write(initCode.toUtf8().replace("%INVOKE", ""));
    fileptr.close();

    DUChain::self()->updateContextForUrl(IndexedString(filename), KDevelop::TopDUContext::ForceUpdate);
    ICore::self()->languageController()->backgroundParser()->parseDocuments();
    ReferencedTopDUContext topContext = DUChain::self()->waitForUpdate(IndexedString(filename),
                                                                       KDevelop::TopDUContext::AllDeclarationsAndContexts);

    Q_ASSERT(topContext);

    Q_ASSERT(initCode.indexOf(QStringLiteral("%INVOKE")) != -1);
    QString copy = initCode;
    QString allCode = copy.replace(QStringLiteral("%INVOKE"), invokeCode);

    QStringList lines = allCode.split(QLatin1Char('\n'));
    completion_data.cursorAt = CursorInRevision::invalid();
    for ( int i = 0; i < lines.length(); i++ ) {
        int j = lines.at(i).indexOf(QStringLiteral("%CURSOR"));
        if ( j != -1 ) {
            completion_data.cursorAt = CursorInRevision(i, j);
            break;
        }
    }
    Q_ASSERT(completion_data.cursorAt.isValid());
    // codeCompletionContext only gets passed the text until the place where completion is invoked
    completion_data.snip = allCode.mid(0, allCode.indexOf(QStringLiteral("%CURSOR")));
    completion_data.remaining = allCode.mid(allCode.indexOf(QStringLiteral("%CURSOR")) + 7);

    DUChainReadLocker lock;
    completion_data.contextAtCursor = DUContextPointer(topContext->findContextAt(completion_data.cursorAt, true));
    Q_ASSERT(completion_data.contextAtCursor);

    return completion_data;
}

const QList<CompletionTreeItem*> PyCompletionTest::runCompletion(const CompletionParameters parameters)
{
    PythonCodeCompletionContext* context = new PythonCodeCompletionContext(parameters.contextAtCursor, parameters.snip, parameters.remaining, parameters.cursorAt, 0, nullptr);
    bool abort = false;
    QList<CompletionTreeItem*> items;
    for ( CompletionTreeItemPointer ptr : context->completionItems(abort, true) ) {
        items << ptr.data();
        // those are leaked, but it's only a few kb while the tests are running. who cares.
        m_ptrs << ptr;
    }
    return items;
}

bool PyCompletionTest::containsItemForDeclarationNamed(const QList<CompletionTreeItem*> items, QString itemName)
{
    for ( const CompletionTreeItem* ptr : items ) {
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
    for ( const CompletionTreeItem* ptr : items ) {
        if ( ptr->data(idx, Qt::DisplayRole, nullptr).toString().startsWith(itemName) ) {
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

    if ( expectedItem == QStringLiteral("EMPTY") ) {
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
    invokeCode = QStringLiteral("testvar = 3\n") + invokeCode;
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
    QVERIFY(! itemInCompletionList(QStringLiteral("class my(): pass\nd = my()\n%INVOKE"), QStringLiteral("d.%CURSOR"), QStringLiteral("__get__")) );
    QEXPECT_FAIL("", "Sorting needs to be fixed first before magic function completion can be re-enabled", Continue);
    bool result = itemInCompletionList(QStringLiteral("class my():\n def __get__(self): pass\nd = my()\n%INVOKE"), QStringLiteral("d.%CURSOR"), QStringLiteral("__get__"));
    QVERIFY(result);
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
    QVERIFY( ! completionListIsEmpty(QStringLiteral("'#'%INVOKE"), QStringLiteral(".%CURSOR")) );
    QVERIFY( ! completionListIsEmpty(QStringLiteral("def addEntry(self,array):\n"
                                     "  \"\"\"\"some comment\"\"\"\n  %INVOKE"), QStringLiteral("%CURSOR")) );
}

void PyCompletionTest::testNoCompletionInCommentsOrStrings()
{
    QFETCH(QString, invokeCode);
    QFETCH(QString, completionCode);

    QVERIFY(! declarationInCompletionList(invokeCode, completionCode, QStringLiteral("append")));
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
    QVERIFY(itemInCompletionList(invokeCode, completionCode, QStringLiteral("__init__")));
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
    QList< CompletionTreeItem* > items = invokeCompletionOn(QStringLiteral("class Foo:\n @property\n def myprop(self): pass\n"
                                                            "a=Foo()\n%INVOKE"), QStringLiteral("a.%CURSOR"));
    QVERIFY(containsItemForDeclarationNamed(items, QStringLiteral("myprop")));
    CompletionTreeItem* item = nullptr;
    for ( CompletionTreeItem* ptr : items ) {
        if ( ptr->declaration() ) {
            if ( ptr->declaration()->identifier().toString() == QStringLiteral("myprop") ) {
                item = ptr;
                break;
            }
        }
    }
    QVERIFY(item);
    // get access to the global editor singleton
    auto editor = KTextEditor::Editor::instance();
    auto document = editor->createDocument(this);

    // create a widget to display the document
    auto view = document->createView(nullptr);
    QVERIFY(document);
    item->execute(view, KTextEditor::Range(0, 0, 0, 0));
    QCOMPARE(document->text(), QLatin1String("myprop"));
}

void PyCompletionTest::testExceptionCompletion()
{
    QList< CompletionTreeItem* > items = invokeCompletionOn(QStringLiteral("localvar = 3\nraise %INVOKE"), QStringLiteral("%CURSOR"));
    QVERIFY(containsItemForDeclarationNamed(items, QStringLiteral("Exception")));
    QVERIFY(! containsItemForDeclarationNamed(items, QStringLiteral("localvar")));

    items = invokeCompletionOn(QStringLiteral("localvar = 3\n%INVOKE"), QStringLiteral("try: pass\nexcept %CURSOR"));
    QVERIFY(containsItemForDeclarationNamed(items, QStringLiteral("Exception")));
    QVERIFY(! containsItemForDeclarationNamed(items, QStringLiteral("localvar")));
}

void PyCompletionTest::testGeneratorCompletion()
{
    QVERIFY(itemInCompletionList(QStringLiteral("%INVOKE"), QStringLiteral("foobar = [item for %CURSOR"), QStringLiteral("item in")));
    QVERIFY(itemInCompletionList(QStringLiteral("%INVOKE"), QStringLiteral("foobar = [key, value for %CURSOR"), QStringLiteral("key, value in")));
    QVERIFY(itemInCompletionList(QStringLiteral("%INVOKE"), QStringLiteral("foobar = [str(key + value) for %CURSOR"), QStringLiteral("key, value in")));
    QVERIFY(itemInCompletionList(QStringLiteral("%INVOKE\ndec_l8r=3"), QStringLiteral("foobar = [dec_l8r for %CURSOR"), QStringLiteral("dec_l8r in")));
}

void PyCompletionTest::testInheritanceCompletion()
{
    QList< CompletionTreeItem* > items = invokeCompletionOn(QStringLiteral("class parentClass: pass\n%INVOKE"), QStringLiteral("class childClass(%CURSOR"));
    QVERIFY(containsItemForDeclarationNamed(items, QStringLiteral("parentClass")));
    items = invokeCompletionOn(QStringLiteral("class parentClass: pass\nclass childClass(%INVOKE): pass"), QStringLiteral("%CURSOR"));
    QVERIFY(containsItemForDeclarationNamed(items, QStringLiteral("parentClass")));
    items = invokeCompletionOn(QStringLiteral("class parentClass:\n class blubb: pass\nclass childClass(%INVOKE): pass"), QStringLiteral("parentClass.%CURSOR"));
    QVERIFY(! containsItemForDeclarationNamed(items, QStringLiteral("parentClass")));
    QVERIFY(containsItemForDeclarationNamed(items, QStringLiteral("blubb")));
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

void PyCompletionTest::testFunctionDeclarationCompletion()
{
    QFETCH(QString, completionCode);
    QFETCH(QString, invokeCode);
    QFETCH(KTextEditor::Range, executeRange);
    QFETCH(QString, expectedReplacement);

    QString documentCode = completionCode;
    documentCode.replace(QStringLiteral("%INVOKE"), invokeCode).replace(QStringLiteral("%CURSOR"), QString());

    QString expectedCode = completionCode;
    expectedCode.replace(QStringLiteral("%INVOKE"), expectedReplacement);

    const QList<CompletionTreeItem *> completionItems = invokeCompletionOn(completionCode, invokeCode);

    QVERIFY( ! completionItems.isEmpty() );

    // KService::Ptr documentService = KService::serviceByDesktopPath(QStringLiteral("katepart.desktop"));
    // QVERIFY(documentService);
    // KTextEditor::Document* document = documentService->createInstance<KTextEditor::Document>(this);
    // QVERIFY(document);
    // document->setText(documentCode);
    //
    // auto view = document->createView(nullptr);
    //
    // completionItems.first()->execute(view, executeRange);
    // QCOMPARE(document->text(), expectedCode);
}

void PyCompletionTest::testFunctionDeclarationCompletion_data()
{
    QTest::addColumn<QString>("completionCode");
    QTest::addColumn<QString>("invokeCode");
    QTest::addColumn<KTextEditor::Range>("executeRange");
    QTest::addColumn<QString>("expectedReplacement");

    QTest::newRow("func_decl_no_parens") << "def foo():\n  pass\n%INVOKE" << "foo%CURSOR" << KTextEditor::Range(2, 0, 2, 3)
                                         << "foo()";

    QTest::newRow("func_decl_existing_parens") << "def foo():\n  return 0\nbar = %INVOKE" << "foo%CURSOR()" << KTextEditor::Range(2, 6, 2, 9)
                                           << "foo()";

    QTest::newRow("decorator_no_parens") << "def mydecorator():\n  pass\nclass Foo:\n  %INVOKE\n  def bar():\n    pass" << "@mydecorator%CURSOR" << KTextEditor::Range(3, 3, 3, 15)
                                         << "@mydecorator";

    QTest::newRow("class_name_no_constructor_parens") << "class Foo:\n  pass\nbar = %INVOKE" << "Foo%CURSOR" << KTextEditor::Range(2, 6, 2, 9)
                                                      << "Foo()";

    QTest::newRow("class_name_explicit_constructor_parens") << "class Foo:\n  def __init__(self):\n    pass\nbar = %INVOKE" << "Fo%CURSOR"
                                                        << KTextEditor::Range(3, 6, 3, 9)
                                                        << "Foo()";
}

void PyCompletionTest::testCompletionScopes()
{
    QFETCH(QString, invokeCode);
    QFETCH(QString, completionCode);
    QFETCH(QString, expectedDeclaration);
    QVERIFY(declarationInCompletionList(invokeCode, completionCode, expectedDeclaration));
}

void PyCompletionTest::testCompletionScopes_data()
{
    QTest::addColumn<QString>("invokeCode");
    QTest::addColumn<QString>("completionCode");
    QTest::addColumn<QString>("expectedDeclaration");
    QTest::newRow("class_scope_end_inside") << "class A:\n test1=1\nclass B:\n test2=1\nf = A()\nclass T:\n f = B()\n f%INVOKE" << ".%CURSOR" << "test2";
    QTest::newRow("class_scope_end_outside") << "class A:\n test1=1\nclass B:\n test2=1\nf = A()\nclass T:\n f = B()\nf%INVOKE" << ".%CURSOR" << "test1";
}

void PyCompletionTest::testStringFormattingCompletion()
{
    QFETCH(QString, completionCode);
    QFETCH(QString, invokeCode);
    QFETCH(QString, expectedItem);
    QFETCH(bool, expectedPresent);

    QCOMPARE(itemInCompletionList(completionCode, invokeCode, expectedItem), expectedPresent);
}

void PyCompletionTest::testStringFormattingCompletion_data()
{
    QTest::addColumn<QString>("completionCode");
    QTest::addColumn<QString>("invokeCode");
    QTest::addColumn<QString>("expectedItem");
    QTest::addColumn<bool>("expectedPresent");

    QTest::newRow("sq_string") << "'foo %INVOKE'" << "%CURSOR" << "{0}" << true;
    QTest::newRow("dq_string") << "\"foo %INVOKE bar\"" << "%CURSOR" << "{0}" << true;
    QTest::newRow("sq_ml_string") << "'''foo\n\n%INVOKE\nbar'''" << "%CURSOR" << "{0}" << true;
    QTest::newRow("dq_ml_string") << "\"\"\"foo\nbar %INVOKE baz\"\"\"" << "%CURSOR" << "{0}" << true;
    QTest::newRow("auto_id") << "\"foo {0} bar {1} baz %INVOKE\"" << "%CURSOR" << "{2}" << true;

    QTest::newRow("format_suggestions_conversion") << "\"foo {0} bar %INVOKE\"" << "{1}%CURSOR" << "{1!r}" << true;
    QTest::newRow("format_suggestions_spec") << "\"foo {0} bar {1}%INVOKE baz\"" << "{2}%CURSOR" << "{2:%}" << true;

    QTest::newRow("incompatible_suggestions_conversion") << "\"foo %INVOKE bar\"" << "{0:%}%CURSOR" << "{0!s:%}" << false;
    QTest::newRow("incompatible_suggestions_spec") << "\"foo %INVOKE bar\"" << "{0!s}%CURSOR" << "{0!s:%}" << false;

    QTest::newRow("alignment_for_strings") << "\"foo %INVOKE bar\"" << "{0!s}%CURSOR" << "{0!s:^${width}}" << true;
    QTest::newRow("conversion_for_aliged_strings") << "\"foo %INVOKE bar\"" << "{0!s}%CURSOR" << "{0!s:^${width}}" << true;

}

void PyCompletionTest::testStringFormatter()
{
    QFETCH(QString, string);
    QFETCH(int, expectedId);
    QFETCH(QList<RangeInString>, expectedVariablePositions);

    StringFormatter f(string);

    int id = f.nextIdentifierId();
    QCOMPARE(id, expectedId);

    for (int i = 0; i < string.size(); i++) {
        bool expectedInsideVariable = false;
        for (RangeInString range : expectedVariablePositions) {
            if (i >= range.beginIndex && i <= range.endIndex) {
                expectedInsideVariable = true;
                break;
            }
        }
        QCOMPARE(f.isInsideReplacementVariable(i), expectedInsideVariable);
    }
}

void PyCompletionTest::testStringFormatter_data()
{
    QTest::addColumn<QString>("string");
    QTest::addColumn<int>("expectedId");
    QTest::addColumn<QList<RangeInString> >("expectedVariablePositions");

    QTest::newRow("sl_string") << "\"foo {0} bar {1}\"" << 2
                               << (QList<RangeInString>() << RangeInString(5, 8) << RangeInString(13, 16));

    QTest::newRow("ml_string") << "\"\"\"foo {0} \n\nbar {1} \n{foo} {2}\nbaz\"\"\"" << 3
                               << (QList<RangeInString>() << RangeInString(7, 10) << RangeInString(17, 20)
                                   << RangeInString(22, 27) << RangeInString(28, 31));

    QTest::newRow("containing_quotes") << "'''foo {0}\nbar\n{1}{0} \\' \\\" \\\" {2} {foo} \n\\'\n {3}baz'''" << 4
                                       << (QList<RangeInString>() << RangeInString(7, 10) << RangeInString(15, 18)
                                           << RangeInString(18, 21) << RangeInString(31, 34) << RangeInString(35, 40)
                                           << RangeInString(46, 49));
}

QString repeat_distinct(const QString& code, int count) {
    QString result;
    QString line;
    for ( int i = 0; i < count; i++ ) {
        line = code;
        result.append(line.replace(QStringLiteral("%X"), QString::number(i)));
    }
    return result;
}

void PyCompletionTest::completionBenchTest()
{
    QFETCH(QString, completionCode);
    QFETCH(QString, invokeCode);

    CompletionParameters data = prepareCompletion(completionCode, invokeCode);
    QBENCHMARK {
        runCompletion(data);
    }
}

void PyCompletionTest::completionBenchTest_data()
{
    QTest::addColumn<QString>("completionCode");
    QTest::addColumn<QString>("invokeCode");

    QTest::newRow("variable_completion") << "a0 = 2\n%INVOKE" << "b = a%CURSOR";
    QTest::newRow("no_items") << "%INVOKE" << "def func(%CURSOR";
    QTest::newRow("function") << "%INVOKE" << "foo(%CURSOR";
    QTest::newRow("deep_function") << "foo(bar(baz(bang([]%INVOKE))))" << ".%CURSOR";
    QTest::newRow("class_completion") << "class my(): pass\nd = my()\n%INVOKE" << "d.%CURSOR";

    QString many_globals = repeat_distinct(QStringLiteral("a%X=%X\n"), 1000);

    QTest::newRow("function_many_globals") << many_globals + QStringLiteral("%INVOKE") << "foo(%CURSOR";
    QTest::newRow("variable_completion_many_globals") << many_globals + QStringLiteral("%INVOKE") << "b = a%CURSOR";
}

}

#include "moc_pycompletiontest.cpp"
