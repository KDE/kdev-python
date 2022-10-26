/*
    SPDX-FileCopyrightText: 2010 Miquel Canes Gonzalez <miquelcanes@gmail.com>
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: MIT
*/

#include <QDebug>
#include "duchaindebug.h"

#include "pyduchaintest.h"

#include <stdlib.h>

#include <language/duchain/topducontext.h>
#include <language/codegen/coderepresentation.h>
#include <tests/autotestshell.h>
#include <tests/testcore.h>
#include <language/duchain/duchain.h>
#include <QtTest>
#include <QApplication>
#include <language/duchain/types/functiontype.h>
#include <language/duchain/types/containertypes.h>
#include <language/duchain/aliasdeclaration.h>
#include <language/backgroundparser/backgroundparser.h>
#include <language/interfaces/iastcontainer.h>
#include <interfaces/ilanguagecontroller.h>
#include <tests/testfile.h>

#include <KTextEditor/Range>

#include "parsesession.h"
#include "pythoneditorintegrator.h"
#include "declarationbuilder.h"
#include "usebuilder.h"
#include "astdefaultvisitor.h"
#include "expressionvisitor.h"
#include "contextbuilder.h"
#include "astbuilder.h"

#include "duchain/helpers.h"

#include "kdevpythonversion.h"

QTEST_MAIN(PyDUChainTest)

using namespace KDevelop;
using namespace Python;


PyDUChainTest::PyDUChainTest(QObject* parent): QObject(parent)
{
    assetsDir = QDir(DUCHAIN_PY_DATA_DIR);
    if (!assetsDir.cd("data")) {
        qFatal("Failed find data directory for test files. Aborting");
    }

    testDir = QDir(testDirOwner.path());

    qputenv("PYTHONPATH", assetsDir.absolutePath().toUtf8());

    initShell();
}

QList<QString> PyDUChainTest::FindPyFiles(QDir& rootDir)
{
    QList<QString> foundfiles;
    rootDir.setFilter(QDir::Files | QDir::Dirs | QDir::NoDot | QDir::NoDotDot);
    rootDir.setNameFilters(QStringList() << "*.py"); // We only want .py files
    
    QDirIterator it(rootDir, QDirIterator::Subdirectories);
    while(it.hasNext()) {
        foundfiles.append(it.next());
    }
    return foundfiles;
}

void PyDUChainTest::init()
{
    QString currentTest = QString(QTest::currentTestFunction());
    if (lastTest == currentTest) {
        qCDebug(KDEV_PYTHON_DUCHAIN) << "Already prepared assets for " << currentTest << ", skipping";
        return;
    } else {
        lastTest = currentTest;
    }
    qCDebug(KDEV_PYTHON_DUCHAIN) << "Preparing assets for test " << currentTest;
    
    QDir assetModuleDir = QDir(assetsDir.absolutePath());
    
    if (!assetModuleDir.cd(currentTest)) {
        qCDebug(KDEV_PYTHON_DUCHAIN) << "Asset directory " << currentTest
                 <<  " does not exist under " << assetModuleDir.absolutePath() << ". Skipping it.";
        return;
    }
    
    qCDebug(KDEV_PYTHON_DUCHAIN) << "Searching for python files in " << assetModuleDir.absolutePath();
    
    QList<QString> foundfiles = FindPyFiles(assetModuleDir);

    QString correctionFileDir = QStandardPaths::locate(QStandardPaths::GenericDataLocation, "kdevpythonsupport/correction_files", QStandardPaths::LocateDirectory);
    auto correctionFileUrl = QUrl(QDir::cleanPath(correctionFileDir + "/testCorrectionFiles/example.py"));
    foundfiles.prepend(correctionFileUrl.path());

    for ( int i = 0; i < 2; i++ ) {
        // Parse each file twice, to ensure no parsing-order related bugs appear.
        // Such bugs will need separate unit tests and should not influence these.
        foreach(const QString filename, foundfiles) {
            qCDebug(KDEV_PYTHON_DUCHAIN) << "Parsing asset: " << filename;
            DUChain::self()->updateContextForUrl(IndexedString(filename), KDevelop::TopDUContext::AllDeclarationsContextsAndUses);
            ICore::self()->languageController()->backgroundParser()->parseDocuments();
        }
        foreach(const QString filename, foundfiles) {
            DUChain::self()->waitForUpdate(IndexedString(filename), KDevelop::TopDUContext::AllDeclarationsContextsAndUses);
        }
        while ( ICore::self()->languageController()->backgroundParser()->queuedCount() > 0 ) {
            // make sure to wait for all parsejobs to finish
            QTest::qWait(10);
        }
    }
}
    

void PyDUChainTest::initShell()
{
    AutoTestShell::init();
    TestCore* core = new TestCore();
    core->initialize(KDevelop::Core::NoUi);
    
    auto doc_url = QStandardPaths::locate(QStandardPaths::GenericDataLocation,
                                          "kdevpythonsupport/documentation_files/builtindocumentation.py");
    
    qCDebug(KDEV_PYTHON_DUCHAIN) << doc_url;

    DUChain::self()->updateContextForUrl(IndexedString(doc_url), KDevelop::TopDUContext::AllDeclarationsContextsAndUses);
    ICore::self()->languageController()->backgroundParser()->parseDocuments();
    DUChain::self()->waitForUpdate(IndexedString(doc_url), KDevelop::TopDUContext::AllDeclarationsContextsAndUses);
    
    DUChain::self()->disablePersistentStorage();
    KDevelop::CodeRepresentation::setDiskChangesForbidden(true);
}

ReferencedTopDUContext PyDUChainTest::parse(const QString& code)
{
    TestFile* testfile = new TestFile(code + "\n", "py", nullptr, testDir.absolutePath().append("/"));
    createdFiles << testfile;

    testfile->parse(TopDUContext::ForceUpdate | TopDUContext::AST);
    testfile->waitForParsed(2000);
    
    if ( testfile->isReady() ) {
        Q_ASSERT(testfile->topContext());
        m_ast = static_cast<Python::ParseSession*>(testfile->topContext()->ast().data())->ast;
        return testfile->topContext();
    }
    else Q_ASSERT(false && "Timed out waiting for parser results, aborting all tests");
    return nullptr;
}

PyDUChainTest::~PyDUChainTest()
{
    foreach ( TestFile* f, createdFiles ) {
        delete f;
    }
    testDir.rmdir(testDir.absolutePath());
}

void PyDUChainTest::testMultiFromImport()
{
    QFETCH(QString, code);
    ReferencedTopDUContext ctx = parse(code);
    QVERIFY(ctx);
    DUChainReadLocker lock;
    QList<Declaration*> a = ctx->findDeclarations(QualifiedIdentifier("a"));
    QList<Declaration*> b = ctx->findDeclarations(QualifiedIdentifier("b"));
    QVERIFY(! a.isEmpty());
    QVERIFY(! b.isEmpty());
    QVERIFY(a.first()->abstractType()->toString().endsWith("int"));
    QVERIFY(b.first()->abstractType()->toString().endsWith("int"));
}

void PyDUChainTest::testMultiFromImport_data() {
    QTest::addColumn<QString>("code");
    QTest::newRow("multiimport") << "import testMultiFromImport.i.localvar1\n"
                                    "import testMultiFromImport.i.localvar2\n"
                                    "a = testMultiFromImport.i.localvar1\n"
                                    "b = testMultiFromImport.i.localvar2\n";
}

void PyDUChainTest::testRelativeImport()
{
    QFETCH(QString, code);
    QFETCH(QString, token);
    QFETCH(QString, type);
    ReferencedTopDUContext ctx = parse(code);
    QVERIFY(ctx);
    DUChainReadLocker lock;
    QList<Declaration*> t = ctx->findDeclarations(QualifiedIdentifier(token));
    QVERIFY(! t.isEmpty());
    QVERIFY(t.first()->abstractType()->toString().endsWith(type));
}

void PyDUChainTest::testRelativeImport_data() {
    QTest::addColumn<QString>("code");
    QTest::addColumn<QString>("token");
    QTest::addColumn<QString>("type");
    QTest::newRow(".local") << "from testRelativeImport.m.sm1.go import i1" << "i1" << "int";
    QTest::newRow(".init") << "from testRelativeImport.m.sm1.go import i2" << "i2" << "int";
    QTest::newRow("..local") << "from testRelativeImport.m.sm1.go import i3" << "i3" << "int";
    QTest::newRow("..init") << "from testRelativeImport.m.sm1.go import i4" << "i4" << "int";
    QTest::newRow("..sub.local") << "from testRelativeImport.m.sm1.go import i5" << "i5" << "int";
    QTest::newRow("..sub.init") << "from testRelativeImport.m.sm1.go import i6" << "i6" << "int";
}

void PyDUChainTest::testImportFiles() {
    QString code = "import testImportFiles\nk = testImportFiles.fromInit()\np = testImportFiles.other.fromOther()";
    ReferencedTopDUContext ctx = parse(code.toUtf8());
    DUChainReadLocker lock;
    QVERIFY(ctx);

    auto k = ctx->findDeclarations(QualifiedIdentifier("k"));
    auto p = ctx->findDeclarations(QualifiedIdentifier("p"));
    QCOMPARE(k.size(), 1);
    QCOMPARE(p.size(), 1);
    QVERIFY(k.first()->abstractType());
    QCOMPARE(k.first()->abstractType()->toString(), QString("fromInit"));
    QCOMPARE(p.first()->abstractType()->toString(), QString("fromOther"));
}

void PyDUChainTest::testCrashes() {
    QFETCH(QString, code);
    ReferencedTopDUContext ctx = parse(code);
    QVERIFY(ctx);
    QVERIFY(m_ast);
    QVERIFY(! m_ast->body.isEmpty());
}

void PyDUChainTest::testCrashes_data() {
    QTest::addColumn<QString>("code");
    
    QTest::newRow("composite_slice") << "A = M[1:3, 3]";
    QTest::newRow("unicode_char") << "a = \"í\"";
    QTest::newRow("unicode escape char") << "print(\"\\xe9\")";
    QTest::newRow("augassign") << "a = 3\na += 5";
    QTest::newRow("delete") << "a = 3\ndel a";
    QTest::newRow("double_comprehension") << "q = [[x for x in a] + [x for x in a] for y in b]";
    QTest::newRow("for_else") << "for i in range(3): pass\nelse: pass";
    QTest::newRow("for_while") << "while i < 4: pass\nelse: pass";
    QTest::newRow("ellipsis") << "a[...]";
    QTest::newRow("tuple_assign_unknown") << "foo = (unknown, unknown, unknown)";
    QTest::newRow("for_assign_unknown") << "for foo, bar, baz in unknown: pass";
    QTest::newRow("negative slice index") << "t = (1, 2, 3)\nd = t[-1]";
    QTest::newRow("decorator_with_args") << "@foo('bar', 'baz')\ndef myfunc(): pass";
    QTest::newRow("non_name_decorator") << "@foo.crazy_decorators\ndef myfunc(): pass";
    QTest::newRow("static_method") << "class c:\n @staticmethod\n def method(): pass";
    QTest::newRow("vararg_in_middle") << "def func(a, *b, c): pass\nfunc(1, 2, 3, 4, 5)";
    QTest::newRow("whatever") << "for attr in updated:\n    "
                                 "    getattr.update";
    QTest::newRow("return_outside_function") << "return 3";
    QTest::newRow("return_context_outside_function") << "return [x for x in range(3)]";
    QTest::newRow("paren_attrib_access") << "a = (xxx or yyy).zzz";
    QTest::newRow("func_call") << "a = xxx.func(yyy.zzz)";
    QTest::newRow("comprehension_attrib") << "a = [foo for foo in bar].baz";
    QTest::newRow("comprehension_attrib2") << "a = [foo.bar for foo in bar]";
    QTest::newRow("lambda_cmpr_defarg") << "a = lambda foo=[b for b in (1, 2, 3)]: foo";
    QTest::newRow("attrib") << "(sep or ' ').join(xxxx.capitalize() for xxxx in ssss.split(sep))";
    QTest::newRow("attrib2") << "(sep or ' ').join(x.capitalize() for x in s.split(sep))";
    QTest::newRow("attrib3") << "known_threads = {line.strip()}";
    QTest::newRow("attrib4") << "known_threads = {line.strip() for line  in [\"foo\"] if line.strip()}";
    QTest::newRow("stacked_lambdas") << "l4 = lambda x = lambda y = lambda z=1 : z : y() : x()";
    QTest::newRow("newline_attrib2") << "raise TypeError(\"argument should be a bound method, not {}\"\n"
                                        ".format(type(meth))) from None";
    QTest::newRow("newline_attrib") << "some_instance \\\n"
                ".   attr1 \\\n"
                ".funcfunc(argarg, arg2arg) \\\n"
                ".foo";
    QTest::newRow("fancy generator context range") << "c1_list = sorted(letter for (letter, meanings) \\\n"
               "in ambiguous_nucleotide_values.iteritems() \\\n"
               "if set([codon[0] for codon in codons]).issuperset(set(meanings)))";
    QTest::newRow("fancy class range") << "class SchemeLexer(RegexLexer):\n"
                                          "  valid_name = r'[a-zA-Z0-9!$%&*+,/:<=>?@^_~|-]+'\n"
                                          "\n"
                                          "  tokens = {\n"
                                          "      'root' : [\n"
                                          "          # the comments - always starting with semicolon\n"
                                          "          # and going to the end of the line\n"
                                          "          (r';.*$', Comment.Single),\n"
                                          "\n"
                                          "          # whitespaces - usually not relevant\n"
                                          "          (r'\\s+', Text),\n"
                                          "\n"
                                          "          # numbers\n"
                                          "          (r'-?\\d+\\.\\d+', Number.Float),\n"
                                          "          (r'-?\\d+', Number.Integer)\n"
                                          "      ],\n"
                                          "  }\n";
    QTest::newRow("another fancy range") << "setup_args['data_files'] = [\n"
                                          "     (os.path.dirname(os.path.join(install_base_dir, pattern)),\n"
                                          "     [ f for f in glob.glob(pattern) ])\n"
                                          "        for pattern in patterns\n"
                                          "]\n";
    QTest::newRow("kwarg_empty_crash") << "def myfun(): return\ncheckme = myfun(kw=something)";
    QTest::newRow("stacked_tuple_hang") << "tree = (1,(2,(3,(4,(5,'Foo')))))";
    QTest::newRow("stacked_tuple_hang2") << "tree = (257,"
         "(264,"
          "(285,"
           "(259,"
            "(272,"
              "(275,"
               "(1, 'return')))))))";
    QTest::newRow("very_large_tuple_hang") << "tree = "
        "(257,"
         "(264,"
          "(285,"
           "(259,"
            "(1, 'def'),"
            "(1, 'f'),"
            "(260, (7, '('), (8, ')')),"
            "(11, ':'),"
            "(291,"
             "(4, ''),"
             "(5, ''),"
             "(264,"
              "(265,"
               "(266,"
                "(272,"
                 "(275,"
                  "(1, 'return'),"
                  "(313,"
                   "(292,"
                    "(293,"
                     "(294,"
                      "(295,"
                       "(297,"
                        "(298,"
                         "(299,"
                          "(300,"
                           "(301,"
                            "(302, (303, (304, (305, (2, '1')))))))))))))))))),"
               "(264,"
                "(265,"
                 "(266,"
                  "(272,"
                   "(276,"
                   "(1, 'yield'),"
                    "(313,"
                     "(292,"
                      "(293,"
                       "(294,"
                        "(295,"
                         "(297,"
                          "(298,"
                           "(299,"
                            "(300,"
                             "(301,"
                              "(302,"
                               "(303, (304, (305, (2, '1')))))))))))))))))),"
                 "(4, ''))),"
               "(6, ''))))),"
           "(4, ''),"
           "(0, ''))))";
    QTest::newRow("attribute_hang") << "s = \"123\"\n"
            "s = s.replace(u'ł', 'l').\\\n"
            "replace(u'ó', 'o').\\\n"
            "replace(u'ą', 'a').\\\n"
            "replace(u'ę', 'e').\\\n"
            "replace(u'ś', 's').\\\n"
            "replace(u'ż', 'z').\\\n"
            "replace(u'ź', 'z').\\\n"
            "replace(u'ć', 'c').\\\n"
            "replace(u'ń', 'n').\\\n"
            "replace(u'б', 'b').\\\n"
            "replace(u'в', 'v').\\\n"
            "replace(u'г', 'g').\\\n"
            "replace(u'д', 'd').\\\n"
            "replace(u'ё', 'yo').\\\n"
            "replace(u'ć', 'c').\\\n"
            "replace(u'ń', 'n').\\\n"
            "replace(u'б', 'b').\\\n"
            "replace(u'в', 'v').\\\n"
            "replace(u'г', 'g').\\\n"
            "replace(u'д', 'd').\\\n"
            "replace(u'ё', 'yo').\\\n"
            "replace(u'ć', 'c').\\\n"
            "replace(u'ń', 'n').\\\n"
            "replace(u'б', 'b').\\\n"
            "replace(u'в', 'v').\\\n"
            "replace(u'г', 'g').\\\n"
            "replace(u'д', 'd').\\\n"
            "replace(u'ё', 'yo')\n";
    QTest::newRow("function context range crash") << "def myfunc(arg):\n foo = 3 + \\\n[x for x in range(20)]";
    QTest::newRow("decorator comprehension crash") << "@implementer_only(interfaces.ISSLTransport,\n"
                 "                   *[i for i in implementedBy(tcp.Client)\n"
                 "                     if i != interfaces.ITLSTransport])\n"
                 "class Client(tcp.Client):\n"
                 "  pass\n";
    QTest::newRow("comprehension_as_default_crash") << "def foo(bar = [item for (_, item) in items()]):\n return";
    QTest::newRow("try_except") << "try: pass\nexcept: pass";
    QTest::newRow("try_except_type") << "try: pass\nexcept FooException: pass";
    QTest::newRow("try_except_type_as") << "try: pass\nexcept FooException as bar: pass";
    QTest::newRow("import_missing") << "from this_does_not_exist import nor_does_this";

    QTest::newRow("list_append_missing") << "foo = []\nfoo.append(missing)";
    QTest::newRow("list_append_missing_arg") << "foo = []\nfoo.append()";

    QTest::newRow("list_extend_missing") << "foo = []\nfoo.extend(missing)";
    QTest::newRow("list_extend_missing_arg") << "foo = []\nfoo.extend()";
    QTest::newRow("method_of_call_with_list_arg") <<
        "class MyClass:\n"
        "    def bar(self): pass\n"
        "def foo(x):\n"
        "    return MyClass()\n"
        "foo([0]).bar()";
    QTest::newRow("unpacked_dict_kwarg") << "def foo(arg): pass\nfoo(**{'arg': 2})";
    QTest::newRow("negative_container_hints") <<
        "class Evil:\n"
        "   def aa(self, arg):\n"
        "      \"\"\"! addsTypeOfArgContent ! -1\"\"\"\n"
        "   def bb(self, arg):\n"
        "      \"\"\"! addsTypeOfArg ! -2\"\"\"\n"
        "   def cc(self, arg):\n"
        "      \"\"\"! returnContentEqualsContentOf ! -3\"\"\"\n"
        "e = Evil()\n"
        "z = [e.aa(1), e.bb(2), e.cc(3)]";
    QTest::newRow("comprehension_in_lambda") << "lambda foo: [bar for bar in foo]";
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 6, 0)
    QTest::newRow("comprehension_in_fstring") <<
        "def crash(): return f'expr={ {x: y for x, y in [(1, 2), ]}}'";
    QTest::newRow("comprehension_in_annassign_1") << "foo: int = [x for x in (42,)][0]";
    QTest::newRow("comprehension_in_annassign_2") << "foo: [t for t in (int,)][0] = 42";
    QTest::newRow("lambda_in_annassign_1") << "foo: int = (lambda: 42)()";
    QTest::newRow("lambda_in_annassign_2") << "foo: (lambda: int)() = 42";
#endif
    QTest::newRow("definition_in_baseclass_1") << "class Foo(lambda x: 1): pass";
    QTest::newRow("definition_in_baseclass_2") << "class Foo([x for x in (1, 2)]): pass";
}

void PyDUChainTest::testClassVariables()
{
    ReferencedTopDUContext ctx = parse("class c():\n myvar = 3;\n def meth(self):\n  print(myvar)");
    QVERIFY(ctx.data());
    DUChainWriteLocker lock(DUChain::lock());
    CursorInRevision relevantPosition(3, 10);
    DUContext* c = ctx->findContextAt(relevantPosition);
    QVERIFY(c);
    int useIndex = c->findUseAt(relevantPosition);
    if ( useIndex != -1 ) {
        QVERIFY(useIndex < c->usesCount());
        const Use* u = &(c->uses()[useIndex]);
        QVERIFY(!u->usedDeclaration(c->topContext()));
    }
}

void PyDUChainTest::testWarnNewNotCls()
{
    QFETCH(QString, code);
    QFETCH(int, probs);

    ReferencedTopDUContext ctx = parse(code);
    DUChainReadLocker lock;
    QCOMPARE(ctx->problems().count(), probs);
}

void PyDUChainTest::testWarnNewNotCls_data()
{
    QTest::addColumn<QString>("code");
    QTest::addColumn<int>("probs");

    QTest::newRow("check_for_new_first_arg_cls") << "class c():\n def __new__(clf, other):\n  pass" << 1;
    QTest::newRow("check_for_new_first_arg_cls_0") << "class c():\n def __new__(cls, other):\n  pass" << 0;
    QTest::newRow("check_first_arg_class_self") << "class c():\n def test(seff, masik):\n  pass" << 1;
    QTest::newRow("check_first_arg_class_self_0") << "class c():\n def test(self, masik):\n  pass" << 0;
}

// this is actually for both binary and boolean operators
void PyDUChainTest::testBinaryOperatorsUnsure()
{
    QFETCH(QString, code);
    QFETCH(QString, type);

    ReferencedTopDUContext ctx = parse(code);
    DUChainWriteLocker lock;
    QList<Declaration*> ds = ctx->findDeclarations(QualifiedIdentifier("checkme"));
    QVERIFY(!ds.isEmpty());
    Declaration* d = ds.first();
    QVERIFY(d);
    QVERIFY(d->abstractType());
    QCOMPARE(d->abstractType()->toString(), type);
}

void PyDUChainTest::testBinaryOperatorsUnsure_data()
{
    QTest::addColumn<QString>("code");
    QTest::addColumn<QString>("type");

    QTest::newRow("check_unsure_type_0") << "class c():\n def __mul__(self, other):\n  return int();\nx = c();\nx = 3.5;\ny = 3;\ncheckme = x * y;" << "unsure (float, int)";
    QTest::newRow("check_unsure_type_1") << "class c():\n def __mul__(self, other):\n  return int();\nx = c();\nx = 3;\ny = 3;\ncheckme = x * y;" << "int";
    QTest::newRow("check_unsure_type_2") << "class c():\n pass;\nx = c();\nx = 3;\ny = 3;\ncheckme = x * y;" << "int";
    QTest::newRow("check_unsure_type_3") << "class c():\n pass;\nclass d():\n pass;\nx = c();\nx = d();\ny = 3;\ncheckme = x * y;" << "int";

    QTest::newRow("check_unsure_type_4") << "checkme = True or False" << "bool";
    QTest::newRow("check_unsure_type_5") << "a = 'foo'; checkme = a or 'bar';" << "str";
    QTest::newRow("check_unsure_type_6") << "class A(): pass\nclass B(): pass;\ncheckme = A() or B() or 42;" << "unsure (A, B, int)";

}


void PyDUChainTest::testFlickering()
{
    QFETCH(QStringList, code);
    QFETCH(int, before);
    QFETCH(int, after);
    
    TestFile f(code[0], "py");
    f.parse(TopDUContext::ForceUpdate);
    f.waitForParsed(500);
    
    ReferencedTopDUContext ctx = f.topContext();
    QVERIFY(ctx);
    
    DUChainWriteLocker lock(DUChain::lock());
    int count = ctx->localDeclarations().size();
    qDebug() << "Declaration count before: " << count;
    QVERIFY(count == before);
    lock.unlock();
    
    f.setFileContents(code[1]);
    f.parse(TopDUContext::ForceUpdate);
    f.waitForParsed(500);
    ctx = f.topContext();
    QVERIFY(ctx);
    
    lock.lock();
    count = ctx->localDeclarations().size();
    qDebug() << "Declaration count afterwards: " << count;
    QVERIFY(count == after);
    
    foreach(Declaration* dec, ctx->localDeclarations()) {
        qDebug() << dec->toString() << dec->range();
        qDebug() << dec->uses().size();
    }
}

void PyDUChainTest::testFlickering_data()
{
    QTest::addColumn<QStringList>("code");
    QTest::addColumn<int>("before");
    QTest::addColumn<int>("after");
    
    QTest::newRow("declaration_flicker") << ( QStringList() << "a=2\n" << "b=3\na=2\n" ) << 1 << 2;
}

void PyDUChainTest::testCannotOverwriteBuiltins()
{
    QFETCH(QString, code);
    QFETCH(QString, expectedType);

    ReferencedTopDUContext ctx = parse(code);
    DUChainWriteLocker lock;
    QList<Declaration*> ds = ctx->findDeclarations(QualifiedIdentifier("checkme"));
    QVERIFY(!ds.isEmpty());
    Declaration* d = ds.first();
    QVERIFY(d);
    QVERIFY(d->abstractType());
    QCOMPARE(d->abstractType()->toString(), expectedType);
}

void PyDUChainTest::testCannotOverwriteBuiltins_data()
{
    QTest::addColumn<QString>("code");
    QTest::addColumn<QString>("expectedType");

    QTest::newRow("list_assign") << "class list(): pass\ncheckme = []\ncheckme.append(3)" << "list of int";
    QTest::newRow("str_assign") << "str = 5; checkme = 'Foo'" << "str";
    QTest::newRow("str_assign2") << "class Foo: pass\nstr = Foo; checkme = 'Foo'" << "str";
    QTest::newRow("str_assign3") << "from testCannotOverwriteBuiltins.i import Foo as str\ncheckme = 'Foo'" << "str";
    QTest::newRow("for") << "for str in [1, 2, 3]: pass\ncheckme = 'Foo'" << "str";
    QTest::newRow("assert") << "assert isinstance(str, int)\ncheckme = 'Foo'" << "str";
    QTest::newRow("assert2") << "assert isinstance(str, int)\ncheckme = 3" << "int";
    QTest::newRow("can_have_custom") << "from testCannotOverwriteBuiltins import mod\ncheckme = mod.open()" << "int";
    QTest::newRow("can_have_custom2") << "from testCannotOverwriteBuiltins import mod\ncheckme = open().read()" << "str";
    QTest::newRow("can_have_custom3") << "from testCannotOverwriteBuiltins import mod\ncheckme = mod.open().read()" << "mixed";
}

void PyDUChainTest::testVarKWArgs()
{
    ReferencedTopDUContext ctx = parse("def myfun(arg, *vararg, **kwarg):\n pass\n pass");
    DUChainWriteLocker lock;
    QVERIFY(ctx);
    DUContext* func = ctx->findContextAt(CursorInRevision(1, 0));
    QVERIFY(func);
    QVERIFY(! func->findDeclarations(QualifiedIdentifier("arg")).isEmpty());
    QVERIFY(! func->findDeclarations(QualifiedIdentifier("vararg")).isEmpty());
    QVERIFY(! func->findDeclarations(QualifiedIdentifier("kwarg")).isEmpty());
    QVERIFY(func->findDeclarations(QualifiedIdentifier("vararg")).first()->abstractType()->toString().startsWith("tuple"));
    QCOMPARE(func->findDeclarations(QualifiedIdentifier("kwarg")).first()->abstractType()->toString(),
             QString("dict of str : unknown"));
}

void PyDUChainTest::testSimple()
{
    QFETCH(QString, code);
    QFETCH(int, decls);
    QFETCH(int, uses);
    
    ReferencedTopDUContext ctx = parse(code);
    DUChainWriteLocker lock(DUChain::lock());
    QVERIFY(ctx);
    
    QVector< Declaration* > declarations = ctx->localDeclarations();
    
    QCOMPARE(declarations.size(), decls);
    
    int usesCount = 0;
    foreach(Declaration* d, declarations) {
        usesCount += d->uses().size();
        
        QVERIFY(d->abstractType());
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
    QTest::newRow("bool") << "a = True" << 1 << 0;
    QTest::newRow("op") << "a = True and True;" << 1 << 0;
}

class AttributeRangeTestVisitor : public AstDefaultVisitor {
public:
    bool found;
    KTextEditor::Range searchingForRange;
    QString searchingForIdentifier;
    void visitAttribute(AttributeAst* node) override {
        auto r = KTextEditor::Range(0, node->startCol, 0, node->endCol);
        qDebug() << "Found attr: " << r << node->attribute->value << ", looking for: " << searchingForRange << searchingForIdentifier;
        if ( r == searchingForRange && node->attribute->value == searchingForIdentifier ) {
            found = true;
            return;
        }
        AstDefaultVisitor::visitAttribute(node);
    }
    void visitFunctionDefinition(FunctionDefinitionAst* node) override {
        auto r = KTextEditor::Range(0, node->name->startCol, 0, node->name->endCol);
        qDebug() << "Found func: " << r << node->name->value << ", looking for: " << searchingForRange << searchingForIdentifier;
        qDebug() << node->arguments->vararg << node->arguments->kwarg;
        if ( r == searchingForRange && node->name->value == searchingForIdentifier ) {
            found = true;
            return;
        }
        if ( node->arguments->vararg ) {
            auto r = KTextEditor::Range(0, node->arguments->vararg->startCol, 0, node->arguments->vararg->startCol+node->arguments->vararg->argumentName->value.length());
            qDebug() << "Found vararg: " << node->arguments->vararg->argumentName->value << r;
            if ( r == searchingForRange && node->arguments->vararg->argumentName->value == searchingForIdentifier ) {
                found = true;
                return;
            }
        }
        if ( node->arguments->kwarg ) {
            auto r = KTextEditor::Range(0, node->arguments->kwarg->startCol, 0, node->arguments->kwarg->startCol+node->arguments->kwarg->argumentName->value.length());
            qDebug() << "Found kwarg: " << node->arguments->kwarg->argumentName->value << r;
            if ( r == searchingForRange && node->arguments->kwarg->argumentName->value == searchingForIdentifier ) {
                found = true;
                return;
            }
        }
        AstDefaultVisitor::visitFunctionDefinition(node);
    }
    void visitClassDefinition(ClassDefinitionAst* node) override {
        auto r = KTextEditor::Range(0, node->name->startCol, 0, node->name->endCol);
        qDebug() << "Found cls: " << r << node->name->value << ", looking for: " << searchingForRange << searchingForIdentifier;
        if ( r == searchingForRange && node->name->value == searchingForIdentifier ) {
            found = true;
            return;
        }
        AstDefaultVisitor::visitClassDefinition(node);
    }
    void visitImport(ImportAst* node) override {
        foreach ( const AliasAst* name, node->names ) {
            if ( name->name ) {
                qDebug() << "found import" << name->name->value << name->name->range();
            }
            if ( name->name && name->name->value == searchingForIdentifier && name->name->range() == searchingForRange ) {
                found = true;
                return;
            }
            if ( name->asName ) {
                qDebug() << "found import" << name->asName->value << name->asName->range();
            }
            if ( name->asName && name->asName->value == searchingForIdentifier && name->asName->range() == searchingForRange ) {
                found = true;
                return;
            }
        }
    }
};

void PyDUChainTest::testRanges()
{
    QFETCH(QString, code);
    QFETCH(int, expected_amount_of_variables); Q_UNUSED(expected_amount_of_variables);
    QFETCH(QStringList, column_ranges);


    ReferencedTopDUContext ctx = parse(code);
    QVERIFY(ctx);

    QVERIFY(m_ast);

    for ( int i = 0; i < column_ranges.length(); i++ ) {
        int scol = column_ranges.at(i).split(",")[0].toInt();
        int ecol = column_ranges.at(i).split(",")[1].toInt();
        QString identifier = column_ranges.at(i).split(",")[2];
        auto r = KTextEditor::Range(0, scol, 0, ecol);

        AttributeRangeTestVisitor* visitor = new AttributeRangeTestVisitor();
        visitor->searchingForRange = r;
        visitor->searchingForIdentifier = identifier;
        visitor->visitCode(m_ast.data());
        QEXPECT_FAIL("attr_dot_name_hash", "Insufficiently magic hack", Continue);
        QCOMPARE(visitor->found, true);
        delete visitor;
    }
}

void PyDUChainTest::testRanges_data()
{
    QTest::addColumn<QString>("code");
    QTest::addColumn<int>("expected_amount_of_variables");
    QTest::addColumn<QStringList>("column_ranges");

    QTest::newRow("attr_two_attributes") << "base.attr" << 2 << ( QStringList() << "5,8,attr" );
    QTest::newRow("attr_binary") << "base.attr + base.attr" << 4 << ( QStringList() << "5,8,attr" << "17,20,attr" );
    QTest::newRow("attr_same") << "aaa.aaa.aaa + aaa.aaa.aaa" << 6 << ( QStringList() << "4,6,aaa" << "8,10,aaa" << "18,20,aaa" << "22,24,aaa" );
    QTest::newRow("attr_three_attributes") << "base.attr.subattr" << 3 << ( QStringList() << "5,8,attr" << "10,16,subattr" );
    QTest::newRow("attr_functionCall") << "base.attr().subattr" << 3 << ( QStringList() << "5,8,attr" << "12,18,subattr" );
    QTest::newRow("attr_stringSubscript") << "base.attr[\"a.b.c..de\"].subattr" << 3 << ( QStringList() << "5,8,attr" << "23,29,subattr" );
    QTest::newRow("attr_functionCallWithArguments") << "base.attr(arg1, arg2).subattr" << 5 << ( QStringList() << "5,8,attr" << "22,28,subattr" );
    QTest::newRow("attr_functionCallWithArgument_withInner") << "base.attr(arg1.parg2).subattr" << 5 << ( QStringList() << "5,8,attr" << "22,28,subattr" << "15,19,parg2" );
    QTest::newRow("attr_complicated") << "base.attr(arg1.arg2(arg4.arg5, [func(a.b)]).arg3(arg6.arg7)).subattr" << 5 << ( QStringList() << "5,8,attr" << "15,18,arg2" <<
                                                            "25,28,arg5" << "39,39,b" << "44,47,arg3" << "54,57,arg7" << "61,67,subattr");
    QTest::newRow("attr_two_in_call") << "func(inst.aaa, inst.bbbb)" << 2 << ( QStringList() << "10,12,aaa" << "20,23,bbbb" );
    QTest::newRow("attr_two_in_call_same") << "func(inst.aaa, inst.aaaa)" << 2 << ( QStringList() << "10,12,aaa" << "20,23,aaaa" );
    QTest::newRow("attr_two_in_call_same2") << "func(inst.aaa, inst.aaa)" << 2 << ( QStringList() << "10,12,aaa" << "20,22,aaa" );
    QTest::newRow("attr_of_string_slash") << "'/'.join(a)" << 1 << ( QStringList() << "4,7,join" );
    QTest::newRow("attr_of_string_in_list") << "[\"*{0}*\".format(foo)]" << 1 << ( QStringList() << "9,14,format" );
    QTest::newRow("attr_of_call_in_list") << "[foo().format(foo)]" << 1 << ( QStringList() << "7,12,format" );
    QTest::newRow("attr_parentheses") << "(\"foo\" + \"foo\").capitalize()" << 1 << ( QStringList() << "16,25,capitalize" );
    QTest::newRow("attr_commented_name") << "base.attr # attr" << 2 << ( QStringList() << "5,8,attr" );
    QTest::newRow("attr_name_in_strings") << "'attr' + base['attr'].attr # attr" << 4 << ( QStringList() << "22,25,attr" );
    QTest::newRow("attr_dot_hash_in_strings") << "'.foo#' + base['.#'].attr # attr" << 4 << ( QStringList() << "21,24,attr" );
    QTest::newRow("attr_dot_name_hash") << "base['.attr#'].attr" << 4 << ( QStringList() << "15,18,attr" );

    QTest::newRow("string_parentheses") << "(\"asdf\".join())" << 1 << ( QStringList() << "8,11,join" );
    QTest::newRow("string_parentheses2") << "(\"asdf\").join()" << 1 << ( QStringList() << "9,12,join" );
    QTest::newRow("string_parentheses3") << "(\"asdf\".join()).join()" << 2 << ( QStringList() << "8,11,join" << "16,19,join" );
    QTest::newRow("string_parentheses4") << "(\"asdf\".join()+2).join()" << 2 << ( QStringList() << "8,11,join" << "18,21,join" );
    QTest::newRow("string_parentheses_call") << "f(\"asdf\".join())" << 1 << ( QStringList() << "9,12,join" );

    QTest::newRow("funcrange_def") << "def func(): pass" << 1 << ( QStringList() << "4,7,func" );
    QTest::newRow("funcrange_spaces_def") << "def    func(): pass" << 1 << ( QStringList() << "7,10,func" );
    QTest::newRow("classdef_range") << "class cls(): pass" << 1 << ( QStringList() << "6,8,cls" );
    QTest::newRow("classdef_range_inheritance") << "class cls(parent1, parent2): pass" << 1 << ( QStringList() << "6,8,cls" );
    QTest::newRow("classdef_range_inheritance_spaces") << "class       cls(  parent1,    parent2     ):pass" << 1 << ( QStringList() << "12,14,cls" );
    QTest::newRow("vararg_kwarg") << "def func(*vararg, **kwargs): pass" << 2 << ( QStringList() << "10,16,vararg" << "20,26,kwargs" );

    QTest::newRow("import") << "import sys" << 1 << ( QStringList() << "7,10,sys" );
    QTest::newRow("import2") << "import i.localvar1" << 1 << ( QStringList() << "7,18,i.localvar1" );
    QTest::newRow("import3") << "import sys as a" << 1 << ( QStringList() << "13,14,a" );
}

class TypeTestVisitor : public AstDefaultVisitor {
public:
    QString searchingForType;
    TopDUContextPointer ctx;
    bool found;
    void visitName(NameAst* node) override {
        if ( node->identifier->value != "checkme" ) return;
        QList<Declaration*> decls = ctx->findDeclarations(QualifiedIdentifier(node->identifier->value));
        if ( ! decls.length() ) {
            qCDebug(KDEV_PYTHON_DUCHAIN) << "No declaration found for " << node->identifier->value;
            return;
        }
        Declaration* d = decls.last();
        QVERIFY(d->abstractType());
        qCDebug(KDEV_PYTHON_DUCHAIN) << "found: " << node->identifier->value << "is" << d->abstractType()->toString() << "should be" << searchingForType;
        if ( d->abstractType()->toString().replace("__kdevpythondocumentation_builtin_", "").startsWith(searchingForType) ) {
            found = true;
            return;
        }
    };
};

void PyDUChainTest::testTypes()
{
    
    QFETCH(QString, code);
    QFETCH(QString, expectedType);

    ReferencedTopDUContext ctx = parse(code.toUtf8());
    QVERIFY(ctx);
    QVERIFY(m_ast);

    DUChainReadLocker lock(DUChain::lock());
    TypeTestVisitor* visitor = new TypeTestVisitor();
    visitor->ctx = TopDUContextPointer(ctx.data());
    visitor->searchingForType = expectedType;
    visitor->visitCode(m_ast.data());
    QEXPECT_FAIL("tuple_func", "no suitable docstring hint", Continue);
    QEXPECT_FAIL("tuple_add", "not implemented", Continue);
    QEXPECT_FAIL("tuple_mul", "not implemented", Continue);
    QEXPECT_FAIL("return_builtin_iterator", "fake builtin iter()", Continue);
    QEXPECT_FAIL("parent_constructor_arg_type", "Not enough passes?", Continue);
    QEXPECT_FAIL("init_class_no_decl", "aliasing info lost", Continue);
    QEXPECT_FAIL("property_wrong", "visitCall uses declaration if no type", Continue);
    QEXPECT_FAIL("property_setter", "very basic property support", Continue);
    QEXPECT_FAIL("assignment_expr_context", "not implemented", Continue);
    if (!visitor->found)
        qDebug() << m_ast->dump();
    QCOMPARE(visitor->found, true);
}

void PyDUChainTest::testTypes_data()
{
    QTest::addColumn<QString>("code");
    QTest::addColumn<QString>("expectedType");

#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 6, 0)
    QTest::newRow("annotate_decl") << "checkme: int" << "int";
    QTest::newRow("annotate_assign") << "checkme: int = 3.5" << "unsure (float, int)";
#endif
    QTest::newRow("listtype") << "checkme = []" << "list";
    QTest::newRow("listtype_func") << "checkme = list()" << "list";
    QTest::newRow("listtype_with_contents") << "checkme = [1, 2, 3, 4, 5]" << "list of int";
    QTest::newRow("listtype_extended") << "some_misc_var = []; checkme = some_misc_var" << "list";
    QTest::newRow("dicttype") << "checkme = {}" << "dict";
    QTest::newRow("dicttype_get") << "d = {0.4:5}; checkme = d.get(0)" << "int";
    QTest::newRow("dicttype_func") << "checkme = dict()" << "dict";
    QTest::newRow("dicttype_extended") << "some_misc_var = {}; checkme = some_misc_var" << "dict";
    QTest::newRow("tuple") << "checkme = ()" << "tuple of ()";
    QTest::newRow("tuple_func") << "checkme = tuple((1, 2.3))" << "tuple of (int, float)";
    QTest::newRow("tuple_with_contents") << "checkme = 1, 2.3" << "tuple of (int, float)";
    QTest::newRow("tuple_extended") << "some_misc_var = (); checkme = some_misc_var" << "tuple of ()";
    QTest::newRow("tuple_max_display") << "checkme = 1,2,3,4,5,6" << "tuple of (int, int, int, int, int, ...)";
    QTest::newRow("bool") << "checkme = True" << "bool";
    QTest::newRow("float") << "checkme = 3.7" << "float";
    QTest::newRow("int") << "checkme = 3" << "int";
    QTest::newRow("str") << "checkme = \"foo\"" << "str";
    QTest::newRow("bytes") << "checkme = b\"foo\"" << "bytes";

    QTest::newRow("function_arg_scope") <<  "class Foo:\n"
                                            "    a = 3\n"
                                            "    def func(self, x=a):\n"
                                            "        return x\n"
                                            "f = Foo()\n"
                                            "checkme = f.func()" << "int";

    QTest::newRow("with") << "with open('foo') as f: checkme = f.read()" << "str";
    QTest::newRow("with_list_target") << "bar = [1, 2, 3]\n"
                                         "with open('foo') as bar[1]: checkme = bar[1].read()" << "str";
    QTest::newRow("with_attr_target") << "bar = object()\n"
                                         "with open('foo') as bar.zep: checkme = bar.zep.read()" << "str";
    QTest::newRow("with_nonself_enter") <<  // From https://bugs.kde.org/show_bug.cgi?id=399534
        "class Mgr:\n"
        "    def __enter__(self): return 42\n"
        "    def __exit__(self, *args): pass\n"
        "with Mgr() as asd:\n"
        "    checkme = asd" << "int";
    QTest::newRow("with_tuple_target") <<
        "class Mgr:\n"
        "    def __enter__(self): return (42, 3.4)\n"
        "    def __exit__(self, *args): pass\n"
        "with Mgr() as (aa, bb):\n"
        "    checkme = bb" << "float";

    QTest::newRow("arg_after_vararg") << "def func(x, y, *, z:int): return z\ncheckme = func()" << "int";
    QTest::newRow("arg_after_vararg_with_default") << "def func(x=5, y=3, *, z:int): return z\ncheckme = func()" << "int";
    QTest::newRow("arg_default") << "def func(x=5, z='foo'): return z\ncheckme = func()" << "str";
    QTest::newRow("arg_kw_no_default") << "def func(x=5, *, a, z='foo'): return a\ncheckme = func()" << "mixed";
    QTest::newRow("arg_kw_default_after_no_default") << "def func(x=5, *, a, z='foo'): return z\ncheckme = func()" << "str";
    QTest::newRow("arg_kw_default") << "def func(x=5, *, z='foo'): return z\ncheckme = func()" << "str";
    QTest::newRow("arg_kw_default_after_default") << "def func(x=5, *, y='foo', z=True): return z\ncheckme = func()" << "bool";

    QTest::newRow("class_scope_end_inside") << "a = str()\nclass M:\n"
                                               "  a = 2\n  foo = a\n"
                                               "checkme = M().foo" << "int";
    QTest::newRow("class_scope_end_outside") << "a = str()\nclass M:\n  a = 2\ncheckme = a" << "str";

    QTest::newRow("list_access_right_open_slice") << "some_list = []; checkme = some_list[2:]" << "list";
    QTest::newRow("list_access_left_open_slice") << "some_list = []; checkme = some_list[:2]" << "list";
    QTest::newRow("list_access_closed_slice") << "some_list = []; checkme = some_list[2:17]" << "list";
    QTest::newRow("list_access_step") << "some_list = []; checkme = some_list[::2]" << "list";
    QTest::newRow("list_access_singleItem") << "some_list = []; checkme = some_list[42]" << "mixed";

    QTest::newRow("funccall_number") << "def foo(): return 3; \ncheckme = foo();" << "int";
    QTest::newRow("funccall_string") << "def foo(): return 'a'; \ncheckme = foo();" << "str";
    QTest::newRow("funccall_list") << "def foo(): return []; \ncheckme = foo();" << "list";
    QTest::newRow("funccall_dict") << "def foo(): return {}; \ncheckme = foo();" << "dict";
    QTest::newRow("funccall_no_return") << "def foo(): pass\ncheckme = foo()" << "None";
    QTest::newRow("funccall_def_return") << "def foo(): return\ncheckme = foo()" << "None";
    QTest::newRow("funccall_maybe_def_return") << "def foo():\n if False: return\n return 7\ncheckme = foo()" << "unsure (None, int)";

    QTest::newRow("tuple1") << "checkme, foo = 3, \"str\"" << "int";
    QTest::newRow("tuple2") << "foo, checkme = 3, \"str\"" << "str";
    QTest::newRow("tuple2_negative_index") << "foo = (1, 2, 'foo')\ncheckme = foo[-1]" << "str";
    QTest::newRow("tuple_type") << "checkme = 1, 2" << "tuple";
    QTest::newRow("tuple_rhs_unpack") << "foo = 1, 2.5\nbar = 1, *foo, 2\ncheckme = bar[2]" << "float";

    QTest::newRow("dict_iteritems") << "d = {1:2, 3:4}\nfor checkme, k in d.iteritems(): pass" << "int";
    QTest::newRow("enumerate_key") << "d = [str(), str()]\nfor checkme, value in enumerate(d): pass" << "int";
    QTest::newRow("enumerate_value") << "d = [str(), str()]\nfor key, checkme in enumerate(d): pass" << "str";
    QTest::newRow("dict_enumerate") << "d = {1:2, 3:4}\nfor key, checkme in enumerate(d.values()): pass" << "int";

    QTest::newRow("dict_assign_twice") << "d = dict(); d[''] = 0; d = dict(); d[''] = 0; checkme = d"
                                       << "unsure (dict of str : int, dict)";

    QTest::newRow("class_method_import") << "class c:\n attr = \"foo\"\n def m():\n  return attr;\n  return 3;\ni=c()\ncheckme=i.m()" << "int";
    QTest::newRow("getsListDocstring") << "foo = [1, 2, 3]\ncheckme = foo.reverse()" << "list of int";

    QTest::newRow("str_iter") << "checkme = [char for char in 'Hello, world!']" << "list of str";
    QTest::newRow("str_subscript") << "checkme = 'Hello, world!'[0]" << "str";
    QTest::newRow("bytes_iter") << "checkme = [byte for byte in b'Hello, world!']" << "list of int";
    QTest::newRow("bytes_subscript") << "checkme = b'Hello, world!'[0]" << "int";

    QTest::newRow("fromAssertIsinstance") << "class c(): pass\ncheckme = mixed()\nassert isinstance(checkme, c)\n" << "c";
    QTest::newRow("fromAssertIsinstanceInvalid") << "class c(): pass\ncheckme = mixed()\nassert isinstance(c, checkme)\n" << "mixed";
    QTest::newRow("fromAssertIsinstanceInvalid2") << "class c(): pass\ncheckme = mixed()\nassert isinstance(D, c)\n" << "mixed";
    QTest::newRow("fromAssertIsinstanceInvalid3") << "checkme = int()\nassert isinstance(checkme, X)\n" << "int";
    QTest::newRow("fromAssertIsinstanceInvalid4") << "checkme = int()\nassert isinstance(checkme)\n" << "int";
    QTest::newRow("fromAssertType") << "class c(): pass\ncheckme = mixed()\nassert type(checkme) == c\n" << "c";
    QTest::newRow("fromIfType") << "class c(): pass\ncheckme = mixed()\nif type(checkme) == c: pass\n" << "c";
    QTest::newRow("fromIfIsinstance") << "class c(): pass\ncheckme = mixed()\nif isinstance(checkme, c): pass\n" << "c";
    
    QTest::newRow("diff_local_classattr") << "class c(): attr = 1\ninst=c()\ncheckme = c.attr" << "int";
    QTest::newRow("diff_local_classattr2") << "local=3\nclass c(): attr = 1\ninst=c()\ncheckme = c.local" << "mixed";
    QTest::newRow("diff_local_classattr3") << "attr=3.5\nclass c(): attr = 1\ninst=c()\ncheckme = c.attr" << "int";
//     QTest::newRow("class_method_self") << "class c:\n def func(checkme, arg, arg2):\n  pass\n" << "c";
//    QTest::newRow("funccall_dict") << "def foo(): return foo; checkme = foo();" << (uint) IntegralType::TypeFunction;

#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 6, 0)
    // With only one subbed value we get a FormattedValue node
    QTest::newRow("fstring_formattedvalue") << "name = 'Jim'; checkme = f'{name}'" << "str";
    // Otherwise a JoinedString, with FormattedValues as children.
    QTest::newRow("fstring_joinedstring") << "name = 'Jim'; checkme = f'Hello, {name}! Your name is {name}.'" << "str";
#endif

    QTest::newRow("tuple_simple") << "mytuple = 3, 5.5\ncheckme, foobar = mytuple" << "int";
    QTest::newRow("tuple_simple2") << "mytuple = 3, 5.5\nfoobar, checkme = mytuple" << "float";
    QTest::newRow("tuple_simple3") << "mytuple = 3, 5.5, \"str\", 3, \"str\"\na, b, c, d, checkme = mytuple" << "str";

    QTest::newRow("tuple_single") << "checkme = 4," << "tuple";
    QTest::newRow("tuple_single2") << "checkme, = 4," << "int";
    QTest::newRow("tuple_single3") << "mytuple = 4,\ncheckme, = mytuple" << "int";

    QTest::newRow("tuple_ext_unpack") << "mytuple = 3, 5.5\nfoobar, *starred, checkme = mytuple" << "float";
    QTest::newRow("tuple_ext_unpack2") << "mytuple = 3, 5.5\nfoobar, *checkme, another = mytuple" << "list";
    QTest::newRow("tuple_ext_unpack3") << "mytuple = 3, 5.5\nfoobar, *checkme = mytuple" << "list of float";
    QTest::newRow("tuple_ext_unpack4") << "mytuple = 3, 5.5\n*checkme, = mytuple" << "list of unsure (int, float)";

    QTest::newRow("tuple_nested") << "mytuple = 3, ('foo', 5.5)\ncheckme, foobar = mytuple" << "int";
    QTest::newRow("tuple_nested2") << "mytuple = 3, ('foo', 5.5)\nfoobar, (checkme, other) = mytuple" << "str";
    QTest::newRow("tuple_nested3") << "mytuple = ((7, 'foo'), 5.5), 3\n((baz, checkme), other), foo = mytuple" << "str";

    QTest::newRow("tuple_nested_ext") << "mytuple = (2, ('foo', 'bar', 6), 7)\na, (b, *checkme, c), *d = mytuple" << "list of str";

    QTest::newRow("tuple_multi_assign") << "mytuple = 2, 'foo'\ncheckme = a = mytuple" << "tuple";
    QTest::newRow("tuple_multi_assign2") << "mytuple = 2, 'foo'\ncheckme, a = b = mytuple" << "int";

    QTest::newRow("list_unpack") << "mylist = [1, 2, 3]\ncheckme, b, c = mylist" << "int";
    QTest::newRow("list_unpack2") << "mylist = [1, 'x', 3]\ncheckme, b, c = mylist" << "unsure (int, str)";

    QTest::newRow("list_ext_unpack") << "mylist = [1, 2, 3]\n*checkme, foo = mylist" << "list of int";
    QTest::newRow("list_ext_unpack2") << "mylist = [1, 'x', 3]\n*checkme, foo = mylist" << "list of unsure (int, str)";

    QTest::newRow("if_expr_sure") << "checkme = 3 if 7 > 9 else 5" << "int";

    QTest::newRow("unary_op") << "checkme = -42" << "int";
    
    QTest::newRow("tuple_funcret") << "def myfun(): return 3, 5\ncheckme, a = myfun()" << "int";
    QTest::newRow("tuple_funcret2") << "def myfun():\n t = 3, 5\n return t\ncheckme, a = myfun()" << "int";
    
    QTest::newRow("yield") << "def myfun():\n yield 3\ncheckme = myfun()" << "list of int";
    QTest::newRow("yield_twice") << "def myfun():\n yield 3\n yield 'foo'\ncheckme = myfun()" << "list of unsure (int, str)";
    // this is mostly a check that it doesn't crash
    QTest::newRow("yield_return") << "def myfun():\n return 3\n yield 'foo'\ncheckme = myfun()" << "unsure (int, list of str)";

    QTest::newRow("lambda") << "x = lambda t: 3\ncheckme = x()" << "int";
    QTest::newRow("lambda_failure") << "x = lambda t: 3\ncheckme = t" << "mixed";

    QTest::newRow("function_arg_tuple") << "def func(*arg):\n foo, bar = arg\n return bar\ncheckme = func(3, 5)" << "int";
    QTest::newRow("function_arg_tuple2") << "def func(*arg):\n return arg[-1]\ncheckme = func(3, \"Foo\")" << "str";

    QTest::newRow("tuple_indexaccess") << "t = 3, 5.5\ncheckme = t[0]" << "int";
    QTest::newRow("tuple_indexaccess2") << "t = 3, 5.5\ncheckme = t[1]" << "float";
    QTest::newRow("tuple_indexaccess3") << "t = 3, 4\ncheckme = t[1]" << "int";
    QTest::newRow("tuple_indexaccess4") << "t = 3, 4.5\ncheckme = t[2]" << "unsure (int, float)";

    QTest::newRow("tuple_indexaccess_neg") << "t = 3, 4.5; checkme = t[-1]" << "float";
    QTest::newRow("tuple_indexaccess_neg2") << "t = 3, 4.5; checkme = t[-2]" << "int";
    QTest::newRow("tuple_indexaccess_neg3") << "t = 3, 4.5; checkme = t[-3]" << "unsure (int, float)";

    QTest::newRow("tuple_slice") << "t = 3, 'q', 4.5; checkme = t[-3: 2]" << "tuple of (int, str)";
    QTest::newRow("tuple_slice_normal")   << "t = 1, 2.3, 'a', {}; checkme = t[1:3]"    << "tuple of (float, str)";
    QTest::newRow("tuple_slice_defstart") << "t = 1, 2.3, 'a', {}; checkme = t[:3]"     << "tuple of (int, float, str)";
    QTest::newRow("tuple_slice_defstop")  << "t = 1, 2.3, 'a', {}; checkme = t[1:]"     << "tuple of (float, str, dict)";
    QTest::newRow("tuple_slice_defboth")  << "t = 1, 2.3, 'a', {}; checkme = t[:]"      << "tuple of (int, float, str, dict)";
    QTest::newRow("tuple_slice_step")     << "t = 1, 2.3, 'a', {}; checkme = t[0:3:2]"  << "tuple of (int, str)";
    QTest::newRow("tuple_slice_reverse")  << "t = 1, 2.3, 'a', {}; checkme = t[3:1:-1]" << "tuple of (dict, str)";
    QTest::newRow("tuple_slice_revstart") << "t = 1, 2.3, 'a', {}; checkme = t[:1:-1]"  << "tuple of (dict, str)";
    QTest::newRow("tuple_slice_revstop")  << "t = 1, 2.3, 'a', {}; checkme = t[2::-1]"  << "tuple of (str, float, int)";
    QTest::newRow("tuple_slice_revstop")  << "t = 1, 2.3, 'a', {}; checkme = t[::-1]"   << "tuple of (dict, str, float, int)";
    QTest::newRow("tuple_slice_no_elems") << "t = 1, 2.3, 'a', {}; checkme = t[1:1]"    << "tuple of ()";
    // TODO unsure-tuples.
    QTest::newRow("tuple_slice_not_literal") << "n = 2; t = 1, 2.3, 'a', {}; checkme = t[0:n]" << "tuple of ()";
    // These are allowed, for whatever reason.
    QTest::newRow("tuple_slice_past_range") << "t = 1, 2.3; checkme = t[-999999999:8888888888]" << "tuple of (int, float)";
    QTest::newRow("tuple_slice_wrong_direction") << "t = 1, 2.3, 'a'; checkme = t[0:3:-1]" << "tuple of ()";
    // This isn't.
    QTest::newRow("tuple_slice_zero_step") << "t = 1, 2.3; checkme = t[::0]" << "tuple of ()";

    QTest::newRow("tuple_add") << "t, u = (3,), ('q', 4.5); checkme = t + u" << "tuple of (int, str, float)";
    QTest::newRow("tuple_mul") << "t = 3, 4.5; checkme = t * 2" << "tuple of (int, float, int, float)";

    QTest::newRow("dict_unsure") << "t = dict(); t = {3: str()}\ncheckme = t[1].capitalize()" << "str";
    QTest::newRow("unsure_attr_access") << "d = str(); d = 3; checkme = d.capitalize()" << "str";

    QTest::newRow("class_create_var") << "class c: pass\nd = c()\nd.foo = 3\ncheckme = d.foo" << "int";
    
    QTest::newRow("tuple_loop") << "t = [(1, \"str\")]\nfor checkme, a in t: pass" << "int";
    
    QTest::newRow("no_hints_type") << "def myfun(arg): arg = 3; return arg\ncheckme = myfun(3)" << "int";
    QTest::newRow("hints_type") << "def myfun(arg): return arg\ncheckme = myfun(3)" << "int";
    QTest::newRow("args_type") << "def myfun(*args): return args[0]\ncheckme = myfun(3)" << "int";
    QTest::newRow("kwarg_type") << "def myfun(**kwargs): return kwargs['a']\ncheckme = myfun(a=3)" << "int";
    QTest::newRow("dict_kwarg_type") << "def foo(**kwargs): return kwargs['']\ncheckme = foo(**{'a': 12})" << "int";
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 5, 0)
    QTest::newRow("dict_norm_kwarg_type") << "def foo(**kwargs): return kwargs['']\n"
                                             "checkme = foo(**{'a': 12}, b=1.2)" << "unsure (int, float)";
    QTest::newRow("multi_dict_kwarg_type") << "def foo(**kwargs): return kwargs['']\n"
                                              "checkme = foo(**{'a': 12}, b=1.2, **{'c': ''})" << "unsure (int, float, str)";
#endif
    QTest::newRow("named_arg_type") << "def myfun(arg): return arg\ncheckme = myfun(arg=3)" << "int";

    QTest::newRow("arg_args_type") << "def myfun(arg, *args): return args[0]\n"
                                      "checkme = myfun(3, str())" << "str";
    QTest::newRow("arg_kwargs_type") << "def myfun(arg, **kwargs): return kwargs['a']\n"
                                         "checkme = myfun(12, a=str())" << "str";
    QTest::newRow("named_kwargs_type_1") << "def myfun(arg, **kwargs): return arg\n"
                                            "checkme = myfun(arg=12, a=str())" << "int";
    QTest::newRow("named_kwargs_type_2") << "def myfun(arg, **kwargs): return kwargs['a']\n"
                                            "checkme = myfun(arg=12, a=str())" << "str";
    QTest::newRow("kwargs_named_type") << "def myfun(arg, **kwargs): return kwargs['a']\n"
                                          "checkme = myfun(a=str(), arg=12)" << "str";
    QTest::newRow("varied_args_type_1") << "def myfun(arg, *args, **kwargs): return arg\n"
                                           "checkme = myfun(1, 1.5, a=str())" << "int";
    QTest::newRow("varied_args_type_2") << "def myfun(arg, *args, **kwargs): return args[0]\n"
                                           "checkme = myfun(1, 1.5, a=str())" << "float";
    QTest::newRow("varied_args_type_3") << "def myfun(arg, *args, **kwargs): return kwargs['a']\n"
                                           "checkme = myfun(1, 1.5, a=str())" << "str";
    QTest::newRow("nested_arg_name_type") << "def foo(xxx):\n"
                                             "  def bar(xxx): return xxx\n"
                                             "  return bar('test')\n"
                                             "checkme = foo(10)\n" << "str";
    QTest::newRow("method_args_type_1") << "class MyClass:\n"
                                           "   def method(self, arg): return self\n"
                                           "checkme = MyClass().method(12)" << "MyClass";
    QTest::newRow("method_args_type_2") << "class MyClass:\n"
                                           "   def method(self, arg): return arg\n"
                                           "checkme = MyClass().method(12)" << "int";
    QTest::newRow("clsmethod_args_type_1") << "class MyClass:\n"
                                              "   @classmethod\n"
                                              "   def method(cls, arg): return cls\n"
                                              "checkme = MyClass().method(12)" << "MyClass";
    QTest::newRow("clsmethod_args_type_2") << "class MyClass:\n"
                                              "   @classmethod\n"
                                              "   def method(cls, arg): return arg\n"
                                              "checkme = MyClass().method(12)" << "int";
    QTest::newRow("staticmethod_args_type") << "class MyClass:\n"
                                               "   @staticmethod\n"
                                               "   def method(arg): return arg\n"
                                               "checkme = MyClass().method(12)" << "int";
    QTest::newRow("staticmethod_vararg_type") << "class MyClass:\n"
                                                 "   @staticmethod\n"
                                                 "   def method(arg, *args): return args[0]\n"
                                                 "checkme = MyClass().method(12, 2.5)" << "float";
    QTest::newRow("method_explicit_self") << "class MyClass:\n"
                                             "   def method(self, arg): return arg\n"
                                             "instance = MyClass()\n"
                                             "checkme = MyClass.method(instance, 12)" << "int";
    QTest::newRow("method_vararg_explicit_self") << "class MyClass:\n"
                                                    "    def foo(self, arg, *args): return args[0]\n"
                                                    "mc = MyClass()\n"
                                                    "checkme = MyClass.foo(mc, 'str', 3, 4.5)" << "int";
    QTest::newRow("clsmethod_explicit_self") << "class MyClass:\n"
                                                "   @classmethod\n"
                                                "   def method(cls, arg1, arg2): return arg2\n"
                                                "instance = MyClass()\n"
                                                "checkme = MyClass.method('a', 12)" << "int";
    QTest::newRow("staticmethod_explicit_self") << "class MyClass:\n"
                                                   "   @staticmethod\n"
                                                   "   def method(arg1, arg2): return arg1\n"
                                                   "instance = MyClass()\n"
                                                   "checkme = MyClass.method('a', 12)" << "str";
    QTest::newRow("parent_constructor_arg_type") << "class Base:\n" // https://bugs.kde.org/show_bug.cgi?id=369364
                                                    "    def __init__(self, foo):\n"
                                                    "        self.foo = foo\n"
                                                    "class Derived(Base):\n"
                                                    "    def __init__(self, foo):\n"
                                                    "       Base.__init__(self, foo)\n"
                                                    "instance = Derived('string')\n"
                                                    "checkme = instance.foo" << "str";
    QTest::newRow("nested_class_self_inside") << "class Foo:\n"
                                                 "   def foo(self):\n"
                                                 "       class Bar:\n"
                                                 "           def bar(self): return self\n"
                                                 "       return Bar().bar()\n"
                                                 "checkme = Foo().foo()\n" << "Foo::foo::Bar";
    QTest::newRow("nested_class_self_after") << "class Foo:\n"
                                                "    class Bar: pass\n"
                                                "    def foo(self): return self\n"
                                                "checkme = Foo().foo()\n" << "Foo";

    QTest::newRow("tuple_unsure") << "q = (3, str())\nq=(str(), 3)\ncheckme, _ = q" << "unsure (int, str)";

    QTest::newRow("custom_iterable") << "class Gen2:\n"
                                        "    def __iter__(self): return self\n"
                                        "    def __next__(self): return 'blah'\n"
                                        "for checkme in Gen2(): pass" << "str";
    QTest::newRow("separate_iterator") << "class Foo:\n"
                                          "    def __iter__(self): return Bar()\n"
                                          "    def __next__(self): return 'blah'\n" // Not used (or shouldn't be!)
                                          "class Bar:\n"
                                          "    def __next__(self): return {1}\n"
                                          "checkme = [a for a in Foo()]" << "list of set of int";
    QTest::newRow("return_builtin_iterator") << "class Gen2:\n"
                                                "    contents = [1, 2, 3]\n"
                                                "    def __iter__(self): return iter(Gen2.contents)\n"
                                                "for checkme in Gen2(): pass" << "int";

    QTest::newRow("init_class") <<  "class Foo:\n"
                                    "  def __init__(self): pass\n"
                                    "  def __call__(self): return 1.5\n"
                                    "checkme = Foo()\n" << "Foo";
    QTest::newRow("init_class_no_decl") <<  "class Foo:\n"
                                            "  def __init__(self): pass\n"
                                            "  def __call__(self): return 1.5\n"
                                            "a = [Foo]\n"
                                            "checkme = a[0]()\n" << "Foo";
    QTest::newRow("call_class") << "class Foo:\n"
                                    "    def __call__(self):\n"
                                    "         return 0\n"
                                    "f = Foo()\n"
                                    "checkme = f()\n" << "int";
    QTest::newRow("call_class_no_decl") << "class Foo:\n"
                                           "  def __call__(self): return 1.5\n"
                                           "a = [Foo()]\n"
                                           "checkme = a[0]()" << "float";
    QTest::newRow("classmethod") << "class Foo:\n"
                                    "    @classmethod\n"
                                    "    def foo(cls):\n"
                                    "         k = cls()\n"
                                    "         return k\n"
                                    "f = Foo.foo()\n"
                                    "checkme = f\n" << "Foo";
    QTest::newRow("property_getter") << "class Foo:\n"
                                        "    @property\n"
                                        "    def bar(self): return 35\n"
                                        "checkme = Foo().bar" << "int";
    QTest::newRow("property_wrong") << "class Foo:\n"
                                       "    @property\n"
                                       "    def bar(self): return True\n"
                                       "checkme = Foo().bar()" << "mixed";
    QTest::newRow("property_setter") << "class Foo:\n"
                                        "    @property\n"
                                        "    def bar(self): return 35\n"
                                        "    @bar.setter\n"
                                        "    def bar(self, value): return 18.3\n" // Return should be ignored
                                        "checkme = Foo().bar" << "int";

    QTest::newRow("tuple_listof") << "l = [(1, 2), (3, 4)]\ncheckme = l[1][0]" << "int";

    QTest::newRow("getitem") << "class c:\n def __getitem__(self, slice): return 3.14\na = c()\ncheckme = a[2]" << "float";

    QTest::newRow("constructor_type_deduction") << "class myclass:\n"
                                                   "\tdef __init__(self, param): self.foo=param\n"
                                                   "checkme = myclass(3).foo" << "int";
    QTest::newRow("simpe_type_deduction") << "def myfunc(arg): return arg\n"
                                             "checkme = myfunc(3)" << "int";
    QTest::newRow("functionCall_functionArg_part1") << "def getstr(): return \"foo\"\n"
                                                 "def identity(f): return f\n"
                                                 "f1 = getstr\n"
                                                 "checkme = f1()" << "str";
    QTest::newRow("functionCall_functionArg_part2") << "def getstr(): return \"foo\"\n"
                                                 "def identity(f): return f\n"
                                                 "f1 = identity(getstr)\n"
                                                 "checkme = f1()\n" << "str";
    QTest::newRow("functionCall_functionArg_full") << "def getstr(): return \"foo\"\n"
                                                 "def identity(f): return f\n"
                                                 "f1 = getstr\n"
                                                 "f2 = identity(getstr)\n"
                                                 "a = getstr()\n"
                                                 "b = f1()\n"
                                                 "checkme = f2()\n" << "str";
    QTest::newRow("vararg_before_other_args") << "def myfun(a, b, *z, x): return z[0]\n"
                                                 "checkme = myfun(False, False, 1, x = False)" << "int";
    QTest::newRow("vararg_before_other_args2") << "def myfun(a, b, *z, x): return z[3]\n"
                                                  "checkme = myfun(False, False, 1, 2, 3, \"str\", x = False)" << "str";
    QTest::newRow("vararg_constructor") << "class myclass():\n"
                                           "  def __init__(self, *arg): self.prop = arg[0]\n"
                                           "obj = myclass(3, 5); checkme = obj.prop" << "int";

    QTest::newRow("declaration_order_var") << "aaa = 2\n"
                                              "checkme = aaa" << "int";
    QTest::newRow("declaration_order_var2") << "checkme = aaa\n"
                                               "aaa = 2" << "mixed";
    QTest::newRow("declaration_order_func_defarg") << "aaa = 2\n"
                                                      "def foo(x=aaa): return x\n"
                                                      "checkme = foo()" << "int";
    QTest::newRow("declaration_order_func_defarg2") << "def foo(x=aaa): return x\n"
                                                       "aaa = 2\n"
                                                       "checkme = foo()" << "mixed";
    QTest::newRow("declaration_order_func_body") << "aaa = 2\n"
                                                    "def foo(): return aaa\n"
                                                   "checkme = foo()" << "int";
    QTest::newRow("declaration_order_func_body2") << "def foo(): return aaa\n"
                                                     "aaa = 2\n"
                                                     "checkme = foo()" << "int";
    QTest::newRow("global_variable") << "a = 3\n"
                                        "def f1():\n"
                                        "  global a\n"
                                        "  return a\n"
                                        "checkme = f1()\n" << "int";
    QTest::newRow("global_variable2") << "a = 3\n"
                                        "def f1():\n"
                                        "  global a\n"
                                        "  a = \"str\"\n"
                                        "  return a\n"
                                        "checkme = f1()\n" << "str";
    QTest::newRow("global_scope_variable") << "a = 3\n"
                                        "def f1():\n"
                                        "  return a\n"
                                        "checkme = f1()\n" << "int";
    QTest::newRow("global_no_toplevel_dec") << "def f1():\n"
                                        "  global a\n  a = 3\n"
                                        "  return a\n"
                                        "checkme = f1()\n" << "int";

    QTest::newRow("top_level_vs_class_attr") <<
        "var = 3\n"
        "class MyClass:\n"
        "    var = 'str'\n"
        "    def f1(): return var\n"
        "checkme = MyClass.f1()" << "int";
    QTest::newRow("top_level_vs_instance_attr") <<
        "var = 3\n"
        "class MyClass:\n"
        "    def __init__(self): self.var = 'str'\n"
        "    def f1(): return var\n"
        "checkme = MyClass.f1()" << "int";
    QTest::newRow("intermediate_vs_class/instance_attrs") <<
        "def func():\n"
        "    aa, bb = 3, 4\n"
        "    class Foo:\n"
        "        aa = 'a'\n"
        "        def __init__(self):\n"
        "            self.bb = 'b'\n"
        "        def foo(self):\n"
        "            return aa, bb\n"
        "    return Foo().foo()\n"
        "checkme = func()" << "tuple of (int, int)";
    QTest::newRow("top_level_vs_nested_class_attrs") <<
        "aaa = 'foo'\n"
        "bbb = 'bar'\n"
        "class Foo:\n"
        "    aaa = 1\n"
        "    class Bar:\n"
        "        bbb = 2\n"
        "        def foo(self, ccc=aaa, ddd=bbb):\n" // Bar.bbb is visible here, Foo.aaa isn't.
        "            return ccc, ddd\n"
        "checkme = Foo().Bar().foo()\n" << "tuple of (str, int)";
    QTest::newRow("top_level_vs_nested_instance_attrs") <<
        "aaa = 'foo'\n"
        "bbb = 'bar'\n"
        "class Foo:\n"
        "    def __init__(self): self.aaa = 1\n"
        "    class Bar:\n"
        "        def __init__(self): self.bbb = 1\n"
        "        def foo(self, ccc=aaa, ddd=bbb):\n" // self.bbb is visible here, Foo().aaa isn't.
        "            return ccc, ddd\n"
        "checkme = Foo().Bar().foo()\n" << "tuple of (str, int)";
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 8, 0)
    QTest::newRow("assignment_expr_while") <<
        "file = open('foo.txt')\n"
        "while q := file.readline():\n"
        "    checkme = q\n" << "str";
    QTest::newRow("assignment_expr_comprehension") <<
        "checkme = [z for q in (1, 2, 3) if (z := q % 2)]" << "list of int";
    QTest::newRow("assignment_expr_context") <<
        "a = [z for q in (1, 2, 3) if (z := q % 2)]\n"
        "checkme = z" << "int";
    QTest::newRow("positional_params") <<
    "def foo(a, b, /, c, d):\n"
    "    return a, b, c, d\n"
    "checkme = foo(10, 'x', 2.3, d='y')\n" << "tuple of (int, str, float, str)";
    QTest::newRow("fstring_self_documenting") << "checkme = f'{expr=}'" << "str";
#endif
}

typedef QPair<Declaration*, int> pair;

void PyDUChainTest::testImportDeclarations() {
    QFETCH(QString, code);
    QFETCH(QStringList, expectedDecls);
    QFETCH(bool, shouldBeAliased);
    
    ReferencedTopDUContext ctx = parse(code.toUtf8());
    QVERIFY(ctx);
    QVERIFY(m_ast);
    
    DUChainReadLocker lock(DUChain::lock());
    foreach ( const QString& expected, expectedDecls ) {
        bool found = false;
        QString name = expected;
        const auto decls = ctx->allDeclarations(CursorInRevision::invalid(), ctx->topContext(), false);
        qCDebug(KDEV_PYTHON_DUCHAIN) << "FOUND DECLARATIONS:";
        foreach ( const pair& current, decls ) {
            qCDebug(KDEV_PYTHON_DUCHAIN) << current.first->toString() << current.first->identifier().identifier().byteArray() << name;
        }
        foreach ( const pair& current, decls ) {
            if ( ! ( current.first->identifier().identifier().byteArray() == name ) ) continue;
            qCDebug(KDEV_PYTHON_DUCHAIN) << "Found: " << current.first->toString() << " for " << name;
            AliasDeclaration* isAliased = dynamic_cast<AliasDeclaration*>(current.first);
            if ( isAliased && shouldBeAliased ) {
                found = true; // TODO fixme
            }
            else if ( ! isAliased  && ! shouldBeAliased ) {
                found = true;
            }
        }
        QVERIFY(found);
    }
}

void PyDUChainTest::testProblemCount()
{
    QFETCH(QString, code);
    QFETCH(int, problemsCount);

    ReferencedTopDUContext ctx = parse(code);
    QVERIFY(ctx);

    DUChainReadLocker lock;
    QEXPECT_FAIL("fstring_visit_inside", "Ranges are broken so we don't visit the expression", Continue);
    QCOMPARE(ctx->problems().size(), problemsCount);
}

void PyDUChainTest::testProblemCount_data()
{
    QTest::addColumn<QString>("code");
    QTest::addColumn<int>("problemsCount");

    QTest::newRow("list_comp") << "[foo for foo in range(3)]" << 0;
    QTest::newRow("list_comp_wrong") << "[bar for foo in range(3)]" << 1;
    QTest::newRow("list_comp_staticmethod") << "class A:\n @staticmethod\n def func(cls):\n"
                                        "  [a for a in [1, 2, 3]]" << 0;
    QTest::newRow("list_comp_other_decorator") << "def decorate(): pass\nclass A:\n @decorate\n def func(self):\n"
                                        "  [a for a in [1, 2, 3]]" << 0;
    QTest::newRow("list_comp_other_wrong") << "def decorate(): pass\nclass A:\n @decorate\n def func(self):\n"
                                        "  [x for a in [1, 2, 3]]" << 1;
    QTest::newRow("list_comp_staticmethod_wrong") << "class A:\n @staticmethod\n def func(cls):\n"
                                        "  [x for a in [1, 2, 3]]" << 1;
    QTest::newRow("misplaced_return_plain") << "return" << 1;
    QTest::newRow("misplaced_return_value") << "return 15" << 1;
    QTest::newRow("misplaced_return_class") << "class A:\n return 25" << 1;
    QTest::newRow("correct_return") << "def foo():\n return" << 0;
    QTest::newRow("lambda_argument_outside") << "def bar():\n lambda foo: 3\n foo" << 1;
    QTest::newRow("use_found_at_decl") << "foo = 3" << 0;
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 6, 0)
    QTest::newRow("fstring_visit_inside") << "checkme = f'{name}'" << 1;
#endif
}

void PyDUChainTest::testImportDeclarations_data() {
    QTest::addColumn<QString>("code");
    QTest::addColumn<QStringList>("expectedDecls");
    QTest::addColumn<bool>("shouldBeAliased");
    
    QTest::newRow("from_import") << "from testImportDeclarations.i import checkme" << ( QStringList() << "checkme" ) << true;
    QTest::newRow("import") << "import testImportDeclarations.i" << ( QStringList() << "testImportDeclarations" ) << false;
    QTest::newRow("import_as") << "import testImportDeclarations.i as checkme" << ( QStringList() << "checkme" ) << false;
    QTest::newRow("from_import_as") << "from testImportDeclarations.i import checkme as checkme" << ( QStringList() << "checkme" ) << true;
    QTest::newRow("from_import_missing") << "from testImportDeclarations.i import missing as checkme" << ( QStringList() ) << true;
}

typedef QPair<Declaration*, int> p;

void PyDUChainTest::testAutocompletionFlickering()
{
    TestFile f("foo = 3\nfoo2 = 2\nfo", "py");
    f.parse(TopDUContext::ForceUpdate);
    f.waitForParsed(500);
    
    ReferencedTopDUContext ctx1 = f.topContext();
    DUChainWriteLocker lock(DUChain::lock());
    QVERIFY(ctx1);
    auto decls1 = ctx1->allDeclarations(CursorInRevision::invalid(), ctx1->topContext());
    QList<DeclarationId> declIds;
    foreach ( p d, decls1 ) {
        declIds << d.first->id();
    }
    lock.unlock();
    
    f.setFileContents("foo = 3\nfoo2 = 2\nfoo");
    f.parse(TopDUContext::ForceUpdate);
    f.waitForParsed(500);
    
    ReferencedTopDUContext ctx2 = f.topContext();
    QVERIFY(ctx2);
    lock.lock();
    auto decls2 = ctx2->allDeclarations(CursorInRevision::invalid(), ctx2->topContext());
    foreach ( p d2, decls2 ) {
        qCDebug(KDEV_PYTHON_DUCHAIN) << "@1: " << d2.first->toString() << "::" << d2.first->id().hash() << "<>" << declIds.first().hash();
        QVERIFY(d2.first->id() == declIds.first());
        declIds.removeFirst();
    }
    lock.unlock();
    
    qDebug() << "=========================";
    
    TestFile g("def func():\n\tfoo = 3\n\tfoo2 = 2\n\tfo", "py");
    g.parse(TopDUContext::ForceUpdate);
    g.waitForParsed(500);
    
    ctx1 = g.topContext();
    lock.lock();
    QVERIFY(ctx1);
    decls1 = ctx1->allDeclarations(CursorInRevision::invalid(), ctx1->topContext(), false).first().first->internalContext()
                 ->allDeclarations(CursorInRevision::invalid(), ctx1->topContext());
    declIds.clear();
    foreach ( p d, decls1 ) {
        declIds << d.first->id();
    }
    lock.unlock();
    
    g.setFileContents("def func():\n\tfoo = 3\n\tfoo2 = 2\n\tfoo");
    g.parse(TopDUContext::ForceUpdate);
    g.waitForParsed(500);
    
    ctx2 = g.topContext();
    QVERIFY(ctx2);
    lock.lock();
    decls2 = ctx2->allDeclarations(CursorInRevision::invalid(), ctx2->topContext(), false).first().first->internalContext()
                 ->allDeclarations(CursorInRevision::invalid(), ctx2->topContext());
    foreach ( p d2, decls2 ) {
        qCDebug(KDEV_PYTHON_DUCHAIN) << "@2: " << d2.first->toString() << "::" << d2.first->id().hash() << "<>" << declIds.first().hash();
        QVERIFY(d2.first->id() == declIds.first());
        declIds.removeFirst();
    }
    lock.unlock();
}

void PyDUChainTest::testFunctionHints()
{
    QFETCH(QString, code);
    QFETCH(QString, expectedType);
    ReferencedTopDUContext ctx = parse(code);
    QVERIFY(ctx);
    DUChainWriteLocker lock;
    QList< Declaration* > decls = ctx->findDeclarations(KDevelop::Identifier("checkme"));
    QVERIFY(! decls.isEmpty());
    Declaration* d = decls.first();
    QVERIFY(d->abstractType());
    QCOMPARE(d->abstractType()->toString(), expectedType);
}

void PyDUChainTest::testFunctionHints_data()
{
    QTest::addColumn<QString>("code");
    QTest::addColumn<QString>("expectedType");
    
    QTest::newRow("func_return_type") << "def myfun(arg) -> int: pass\ncheckme = myfun(\"3\")" << "unsure (None, int)";
    QTest::newRow("argument_type") << "def myfun(arg : int): return arg\ncheckme = myfun(foobar)" << "int";
    QTest::newRow("argument_type_only_if_typeof") << "def myfun(arg : 3): return arg\ncheckme = myfun(foobar)" << "mixed";
}

void PyDUChainTest::testHintedTypes()
{
    QFETCH(QString, code);
    QFETCH(QString, expectedType);
    ReferencedTopDUContext ctx = parse(code);
    QVERIFY(ctx);
    DUChainWriteLocker lock;
    QList< Declaration* > decls = ctx->findDeclarations(KDevelop::Identifier("checkme"));
    QVERIFY(! decls.isEmpty());
    Declaration* d = decls.first();
    QVERIFY(d->abstractType());
    QCOMPARE(d->abstractType()->toString(), expectedType);
}

void PyDUChainTest::testHintedTypes_data()
{
    QTest::addColumn<QString>("code");
    QTest::addColumn<QString>("expectedType");

    QTest::newRow("simple_hint") << "def myfunc(x): return x\ncheckme = myfunc(3)" << "int";
    QTest::newRow("hint_unsure") << "def myfunc(x): return x\nmyfunc(3.5)\ncheckme = myfunc(3)" << "unsure (float, int)";
    QTest::newRow("unsure_attribute") << "def myfunc(x): return x.capitalize()\nmyfunc(3.5)\ncheckme = myfunc(str())" << "str";
}

void PyDUChainTest::testOperators()
{
    QFETCH(QString, code);
    QFETCH(QString, expectedType);
    code.prepend("from testOperators.example import *\n\n");
    ReferencedTopDUContext ctx = parse(code);
    QVERIFY(ctx);

    DUChainReadLocker lock(DUChain::lock());
    TypeTestVisitor* visitor = new TypeTestVisitor();
    visitor->ctx = TopDUContextPointer(ctx.data());
    visitor->searchingForType = expectedType;
    visitor->visitCode(m_ast.data());

    QVERIFY(visitor->found);
}

void PyDUChainTest::testOperators_data()
{
    QTest::addColumn<QString>("code");
    QTest::addColumn<QString>("expectedType");

    QTest::newRow("add") << "checkme = Example() + Example()" << "Add";
    QTest::newRow("sub") << "checkme = Example() - Example()" << "Sub";
    QTest::newRow("mul") << "checkme = Example() * Example()" << "Mul";
    QTest::newRow("floordiv") << "checkme = Example() // Example()" << "Floordiv";
    QTest::newRow("mod") << "checkme = Example() % Example()" << "Mod";
    QTest::newRow("pow") << "checkme = Example() ** Example()" << "Pow";
    QTest::newRow("lshift") << "checkme = Example() << Example()" << "Lshift";
    QTest::newRow("rshift") << "checkme = Example() >> Example()" << "Rshift";
    QTest::newRow("and") << "checkme = Example() & Example()" << "And";
    QTest::newRow("xor") << "checkme = Example() ^ Example()" << "Xor";
    QTest::newRow("or") << "checkme = Example() | Example()" << "Or";
}

void PyDUChainTest::testFunctionArgs()
{
    ReferencedTopDUContext ctx = parse("def ASDF(arg1, arg2):\n"
                                       "  arg1 = arg2");
    DUChainWriteLocker lock(DUChain::lock());
    QVERIFY(ctx);
    QVERIFY(m_ast);
//     dumpDUContext(ctx);

    QCOMPARE(ctx->childContexts().size(), 2);
    DUContext* funcArgCtx = ctx->childContexts().first();
    QCOMPARE(funcArgCtx->type(), DUContext::Function);
    QCOMPARE(funcArgCtx->localDeclarations().size(), 2);
    QVERIFY(!funcArgCtx->owner());
    
    Python::FunctionDeclaration* decl = dynamic_cast<Python::FunctionDeclaration*>(
                                    ctx->allDeclarations(CursorInRevision::invalid(), ctx->topContext()).first().first);
    QVERIFY(decl);
    QCOMPARE(decl->type<FunctionType>()->arguments().length(), 2);
    qDebug() << decl->type<FunctionType>()->arguments().length() << 2;

    DUContext* funcBodyCtx = ctx->childContexts().last();
    QCOMPARE(funcBodyCtx->type(), DUContext::Other);
    QVERIFY(funcBodyCtx->owner());
    QVERIFY(funcBodyCtx->localDeclarations().isEmpty());
}

void PyDUChainTest::testInheritance()
{
    QFETCH(QString, code);
    QFETCH(int, expectedBaseClasses);
    ReferencedTopDUContext ctx = parse(code);
    QVERIFY(ctx);
    DUChainReadLocker lock(DUChain::lock());
    auto decls = ctx->allDeclarations(CursorInRevision::invalid(), ctx->topContext(), false);
    bool found = false;
    bool classDeclFound = false;
    foreach ( const p& item, decls ) {
        if ( item.first->identifier().toString() == "B" ) {
            auto klass = dynamic_cast<ClassDeclaration*>(item.first);
            QVERIFY(klass);
            QCOMPARE(klass->baseClassesSize(), static_cast<unsigned int>(expectedBaseClasses));
            classDeclFound = true;
        }
        if ( item.first->identifier().toString() == "checkme" ) {
            QCOMPARE(item.first->abstractType()->toString(), QString("int"));
            found = true;
        }
    }
    QVERIFY(found);
    QVERIFY(classDeclFound);
}

void PyDUChainTest::testInheritance_data()
{
    QTest::addColumn<QString>("code");
    QTest::addColumn<int>("expectedBaseClasses");
    
    QTest::newRow("simple") << "class A():\n\tattr = 3\n\nclass B(A):\n\tpass\n\ninst=B()\ncheckme = inst.attr" << 1;
    QTest::newRow("context_import_prereq") << "import testInheritance.i\ninst=testInheritance.i.testclass()\n"
                                              "checkme = inst.attr\nclass B(): pass" << 1; // 1 because object
    QTest::newRow("context_import") << "import testInheritance.i\n\nclass B(testInheritance.i.testclass):\n"
                                       "\ti = 4\n\ninst=B()\ncheckme = inst.attr" << 1;
}

void PyDUChainTest::testClassContextRanges()
{
    QString code = "class my_class():\n pass\n \n \n \n \n";
    ReferencedTopDUContext ctx = parse(code);
    DUChainWriteLocker lock;
    DUContext* classContext = ctx->findContextAt(CursorInRevision(5, 0));
    QVERIFY(classContext);
    QVERIFY(classContext->type() == DUContext::Class);
}

void PyDUChainTest::testContainerTypes()
{
    QFETCH(QString, code);
    QFETCH(QString, contenttype);
    QFETCH(bool, use_type);
    ReferencedTopDUContext ctx = parse(code);
    QVERIFY(ctx);
    
    DUChainReadLocker lock(DUChain::lock());
    QList<Declaration*> decls = ctx->findDeclarations(QualifiedIdentifier("checkme"));
    QVERIFY(decls.length() > 0);
    QVERIFY(decls.first()->abstractType());
    if ( ! use_type ) {
        auto type = ListType::Ptr::dynamicCast(decls.first()->abstractType());
        QVERIFY(type);
        QVERIFY(type->contentType());
        QCOMPARE(type->contentType().abstractType()->toString(), contenttype);
    }
    else {
        QVERIFY(decls.first()->abstractType());
        QEXPECT_FAIL("dict_of_int_call", "returnContentEqualsContentOf isn't suitable", Continue);
        QEXPECT_FAIL("dict_from_tuples", "returnContentEqualsContentOf isn't suitable", Continue);
        QEXPECT_FAIL("comprehension_shadowing_ms", "Nothing is foolproof to a sufficiently capable fool", Continue);
        QEXPECT_FAIL("comprehension_shadowing_nest2", "See above", Continue);
        QCOMPARE(decls.first()->abstractType()->toString(), contenttype);
    }
}

void PyDUChainTest::testContainerTypes_data()
{
    QTest::addColumn<QString>("code");
    QTest::addColumn<QString>("contenttype");
    QTest::addColumn<bool>("use_type");

    QTest::newRow("list_of_int") << "checkme = [1, 2, 3]" << "int" << false;
    QTest::newRow("list_from_unpacked") << "foo = [1.3]\ncheckme = [1, *foo, 3]" << "unsure (int, float)" << false;
    QTest::newRow("list_of_int_call") << "checkme = list([1, 2, 3])" << "int" << false;
    QTest::newRow("list_from_tuple") << "checkme = list((1, 2, 3))" << "int" << false;
    QTest::newRow("list_from_dict") << "checkme = list({'a':1, 'b':2})" << "str" << false; // Gets key type!
    QTest::newRow("list_from_custom_iter") <<
        "class MyClass:\n"
        "    def __iter__(self): return self\n"
        "    def __next__(self): return 3.1417\n"
        "checkme = list(MyClass())" << "float" << false;
    QTest::newRow("generator") << "checkme = [i for i in [1, 2, 3]]" << "int" << false;
    QTest::newRow("list_access") << "list = [1, 2, 3]\ncheckme = list[0]" << "int" << true;
    QTest::newRow("set_of_int") << "checkme = {1, 2, 3}" << "int" << false;
    QTest::newRow("set_of_int_call") << "checkme = set({1, 2, 3})" << "int" << false;
    QTest::newRow("set_from_tuple") << "checkme = set((1, 2, 3))" << "int" << false;
    QTest::newRow("set_generator") << "checkme = {i for i in [1, 2, 3]}" << "int" << false;
    QTest::newRow("dict_of_str_int") << "checkme = {'a':1, 'b':2, 'c':3}" << "dict of str : int" << true;
    QTest::newRow("frozenset_of_int_call") << "checkme = frozenset({1, 2, 3})" << "int" << false;
    QTest::newRow("dict_of_int") << "checkme = {a:1, b:2, c:3}" << "int" << false;
    QTest::newRow("dict_of_int_call") << "checkme = dict({'a':1, 'b':2, 'c':3})" << "dict of str : int" << true;
    QTest::newRow("dict_from_tuples") << "checkme = dict([('a', 1), ('b', 2)])" << "dict of str : int" << true;
    QTest::newRow("dict_generator") << "checkme = {\"Foo\":i for i in [1, 2, 3]}" << "int" << false;
    QTest::newRow("dict_access") << "list = {'a':1, 'b':2, 'c':3}\ncheckme = list[0]" << "int" << true;
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 5, 0)
    QTest::newRow("set_from_unpacked") << "foo = [1.3]\ncheckme = {1, *foo, 3}" << "unsure (int, float)" << false;
    QTest::newRow("dict_from_unpacked") << "checkme = {**{'a': 1}}" << "dict of str : int" << true;
    QTest::newRow("dict_from_varied") << "checkme = {**{'a': 1}, 1: 1.5}" <<
                                         "dict of unsure (str, int) : unsure (int, float)" << true;
#endif
    QTest::newRow("generator_attribute") << "checkme = [item.capitalize() for item in ['foobar']]" << "str" << false;
    QTest::newRow("cannot_change_type") << "checkme = [\"Foo\", \"Bar\"]" << "str" << false;
    QTest::newRow("cannot_change_type2") << "[1, 2, 3].append(5)\ncheckme = [\"Foo\", \"Bar\"]" << "str" << false;

    QTest::newRow("list_append") << "d = []\nd.append(3)\ncheckme = d[0]" << "int" << true;
    QTest::newRow("list_extend") << "d = []; q = [int()]\nd.extend(q)\ncheckme = d[0]" << "int" << true;
    QTest::newRow("list_extend_with_tuple") << "d = []; q = (1, 2)\nd.extend(q)\ncheckme = d[0]" << "int" << true;
    QTest::newRow("list_extend_with_custom_iter") <<
        "class MyClass:\n"
        "    def __iter__(self): return self\n"
        "    def __next__(self): return 3.1417\n"
        "checkme = []\ncheckme.extend(MyClass())" << "float" << false;

    QTest::newRow("for_loop") << "d = [3]\nfor item in d:\n checkme = item" << "int" << true;
    QTest::newRow("for_loop_unsure") << "d = [3, \"foo\"]\nfor item in d:\n checkme = item" << "unsure (int, str)" << true;
    QTest::newRow("for_loop_tuple_1") << "d = [(3, 3.5)]\nfor a, b in d:\n checkme = a" << "int" << true;
    QTest::newRow("for_loop_tuple_2") << "d = [(3, 3.5)]\nfor a, b in d:\n checkme = b" << "float" << true;
    QTest::newRow("for_loop_tuple_unsure") << "d = [(3, 3.5), (3.5, 3)]\nfor a, b in d:\n checkme = b"
                                           << "unsure (float, int)" << true;
    // Proposed by Nicolás Alvarez; why not? https://bugs.kde.org/show_bug.cgi?id=359915
    QTest::newRow("comprehension_messy") << "users = {'a':19, 'b':42, 'c':35}\n"
                                            "sorted_list = sorted(users.items(), key=lambda kv: (-kv[1], kv[0]))\n"
                                            "checkme = [k for r,(k,v) in enumerate(sorted_list, 1)]" << "list of str" << true;
    QTest::newRow("comprehension_multiline") << "checkme = [a for\n a in \n (1, 2)]" << "list of int" << true;
    QTest::newRow("comprehension_multistage") << "nested = (1, 2), (3, 4)\n"
                                                 "checkme =  [foo for bar in nested for foo in bar]" << "list of int" << true;
    QTest::newRow("comprehension_shadowing_ms") << "nested = (1, 2), (3, 4)\n"
                                                   "checkme =  [foo for foo in nested for foo in foo]" << "list of int" << true;
    QTest::newRow("comprehension_shadowing_nest1") << "nested = (1, 2), (3, 4)\n"
                                                      "checkme = [foo for foo in [foo for foo in nested]]" << "list of tuple of (int, int)" << true;
    QTest::newRow("comprehension_shadowing_nest2") << "nested = (1, 2), (3, 4)\n"
                                                      "checkme = [[foo for foo in foo] for foo in nested]" << "list of list of int" << true;
    // From https://bugs.kde.org/show_bug.cgi?id=359912
    QTest::newRow("subscript_multi") <<
        "class Middle:\n def __getitem__(self, key):\n  return str()\n"
        "class Outer:\n def __getitem__(self, key):\n  return Middle()\n"
        "aaa = Outer()\ncheckme = aaa[0][0]" << "str" << true;
    QTest::newRow("subscript_func_call") <<
        "class Foo:\n def __getitem__(self, key):\n  return str()\n"
        "def bar():\n return Foo()\n"
        "checkme = bar()[0]" << "str" << true;
    QTest::newRow("subscript_unknown_index") << "a = 1,str()\ncheckme = a[5-4]" << "unsure (int, str)" << true;
    QTest::newRow("subscript_unsure") << "a = 1,2\na=[str()]\ncheckme = a[0]" << "unsure (int, str)" << true;
    QTest::newRow("subscript_unsure_getitem") <<
        "class Foo:\n def __getitem__(self, key):\n  return str()\n"
        "class Bar:\n def __getitem__(self, key):\n  return float()\n"
        "a = Foo()\na=Bar()\na=[1,2]\ncheckme = a[1]" << "unsure (str, float, int)" << true;
}

void PyDUChainTest::testVariableCreation()
{
    QFETCH(QString, code);
    QFETCH(QStringList, expected_local_declarations);
    QFETCH(QStringList, expected_types);

    ReferencedTopDUContext top = parse(code);
    QVERIFY(top);

    DUChainReadLocker lock;
    auto localDecls = top->localDeclarations();
    QVector<QString> localDeclNames;
    for ( const Declaration* d: localDecls ) {
        localDeclNames.append(d->identifier().toString());
    }
    Q_ASSERT(expected_types.size() == expected_local_declarations.size());
    int offset = 0;
    for ( const QString& expected : expected_local_declarations ) {
        int index = localDeclNames.indexOf(expected);
        QVERIFY(index != -1);
        QVERIFY(localDecls[index]->abstractType());
        QCOMPARE(localDecls[index]->abstractType()->toString(), expected_types[offset]);
        offset++;
    }
}

void PyDUChainTest::testVariableCreation_data()
{
    QTest::addColumn<QString>("code");
    QTest::addColumn<QStringList>("expected_local_declarations");
    QTest::addColumn<QStringList>("expected_types");

    QTest::newRow("simple") << "a = 3" << QStringList{"a"} << QStringList{"int"};
    QTest::newRow("tuple_wrong") << "a, b = 3" << QStringList{"a", "b"} << QStringList{"mixed", "mixed"};
    QTest::newRow("tuple_unpack_inplace") << "a, b = 3, 5.5" << QStringList{"a", "b"} << QStringList{"int", "float"};
    QTest::newRow("tuple_unpack_indirect") << "c = 3, 3.5\na, b = c" << QStringList{"a", "b"} << QStringList{"int", "float"};
    QTest::newRow("tuple_unpack_stacked_inplace") << "a, (b, c) = 1, (2, 3.5)" << QStringList{"a", "b", "c"}
                                                                             << QStringList{"int", "int", "float"};
    QTest::newRow("tuple_unpack_stacked_indirect") << "d = 3.5, (3, 1)\na, (b, c) = d"
                                                   << QStringList{"a", "b", "c"} << QStringList{"float", "int", "int"};
    QTest::newRow("unpack_from_list_inplace") << "a, b = [1, 2, 3]" << QStringList{"a", "b"} << QStringList{"int", "int"};
    QTest::newRow("unpack_from_list_indirect") << "c = [1, 2, 3]\na, b = c" << QStringList{"a", "b"}
                                                                            << QStringList{"int", "int"};
    QTest::newRow("unpack_custom_iterable") <<
        "class Foo:\n"
        "    def __iter__(self): return self\n"
        "    def __next__(self): return 1.5\n"
        "a, *b = Foo()" << QStringList{"a", "b"} << QStringList {"float", "list of float"};
    QTest::newRow("for_loop_simple") << "for i in range(3): pass" << QStringList{"i"} << QStringList{"int"};
    QTest::newRow("for_loop_unpack") << "for a, b in [(3, 5.1)]: pass" << QStringList{"a", "b"}
                                                                       << QStringList{"int", "float"};
    QTest::newRow("for_loop_stacked") << "for a, (b, c) in [(1, (2, 3.5))]: pass" << QStringList{"a", "b", "c"}
                                                                                << QStringList{"int", "int", "float"};
    QTest::newRow("for_loop_tuple") << "for a in 1, 2: pass" << QStringList{"a"} << QStringList{"int"};
    QTest::newRow("for_loop_dict") << "for a in {'foo': 1}: pass" << QStringList{"a"} << QStringList{"str"};
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 8, 0)
    QTest::newRow("assignment_expr") << "a = (b := 10)" << QStringList{"a", "b"} << QStringList{"int", "int"};
#endif
}

void PyDUChainTest::testCleanupMultiplePasses()
{
    for ( int j = 0; j < 20; j++ ) {
        ReferencedTopDUContext top = parse("from testCleanupMultiplePasses import foo\ndef fonc(): return 3+2j\nfoo.foo.func = fonc");
    }
}

void PyDUChainTest::testManyDeclarations()
{
    ReferencedTopDUContext top = parse("from testManyDeclarations import test\nk=test.Foo()");
}

void PyDUChainTest::testComments()
{
    QFETCH(QString, code);

    auto top = parse(code);
    QVERIFY(top);
    DUChainReadLocker lock;

    auto decls = top->findDeclarations(QualifiedIdentifier("a"));
    QCOMPARE(decls.size(), 1);
    auto a = decls.first();
    QCOMPARE(a->comment(), QByteArray("comment"));

    decls = top->findDeclarations(QualifiedIdentifier("b"));
    if ( decls.isEmpty() ) {
        decls = top->childContexts().last()->findDeclarations(QualifiedIdentifier("b"));
    }
    auto b = decls.first();
    QCOMPARE(b->comment(), QByteArray());
}

void PyDUChainTest::testComments_data()
{
    QTest::addColumn<QString>("code");

    QTest::newRow("variable") << "b=5\n\"\"\"comment\"\"\"\na=5\nb=5";
    QTest::newRow("function") << "def a():\n    \"\"\"comment\"\"\"\n    b=5";
    QTest::newRow("class") << "class a:\n    \"\"\"comment\"\"\"\n    b=5";
}
