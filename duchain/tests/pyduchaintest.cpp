/*****************************************************************************
 * Copyright 2010 (c) Miquel Canes Gonzalez <miquelcanes@gmail.com>          *
 * Copyright 2012 (c) Sven Brauch <svenbrauch@googlemail.com>                *
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
#include <KStandardDirs>
#include <language/duchain/types/functiontype.h>
#include <language/duchain/aliasdeclaration.h>
#include <language/backgroundparser/backgroundparser.h>
#include <interfaces/ilanguagecontroller.h>

#include "parsesession.h"
#include "pythoneditorintegrator.h"
#include "declarationbuilder.h"
#include "usebuilder.h"
#include "astdefaultvisitor.h"
#include "expressionvisitor.h"
#include "contextbuilder.h"
#include "astbuilder.h"

#include "types/variablelengthcontainer.h"
#include "duchain/helpers.h"

QTEST_MAIN(PyDUChainTest)

using namespace KDevelop;
using namespace Python;


PyDUChainTest::PyDUChainTest(QObject* parent): QObject(parent), m_pool()
{
    initShell();
}

void PyDUChainTest::initShell()
{
    AutoTestShell::init();
    TestCore* core = new TestCore();
    core->initialize(KDevelop::Core::NoUi);
    
    KUrl doc_url = KUrl(KStandardDirs::locate("data", "kdevpythonsupport/documentation_files/builtindocumentation.py"));
    doc_url.cleanPath(KUrl::SimplifyDirSeparators);
    
    kDebug() << doc_url;

    DUChain::self()->updateContextForUrl(IndexedString(doc_url), KDevelop::TopDUContext::AllDeclarationsContextsAndUses);
    ICore::self()->languageController()->backgroundParser()->parseDocuments();
    DUChain::self()->waitForUpdate(IndexedString(doc_url), KDevelop::TopDUContext::AllDeclarationsContextsAndUses);
    
    QFile f("/tmp/i.py");
    f.open(QIODevice::WriteOnly);
    f.write("def checkme(): pass\nlocalvar1 = 3\nlocalvar2 = 5\n");
    f.close();
    
    DUChain::self()->updateContextForUrl(IndexedString("/tmp/i.py"), KDevelop::TopDUContext::AllDeclarationsContextsAndUses);
    ICore::self()->languageController()->backgroundParser()->parseDocuments();
    DUChain::self()->waitForUpdate(IndexedString("/tmp/i.py"), KDevelop::TopDUContext::AllDeclarationsContextsAndUses);
    
    DUChain::self()->disablePersistentStorage();
    KDevelop::CodeRepresentation::setDiskChangesForbidden(true);
}

ReferencedTopDUContext PyDUChainTest::parse_int(const QString& code, const QString& suffix)
{
    ParseSession* session = new ParseSession(&m_pool);
    session->setContents( code + "\n" ); // append a newline in case the parser doesnt like it without one
    
    static int mytest=0;
    KUrl filename;
    if ( suffix.isNull() ) {
        filename = "/tmp/pyduchaintest" + QString::number(mytest++) + ".py";
    }
    else {
        filename = "/tmp/pyduchaintest__" + suffix + ".py";
    }
    QFile f(filename.path());
    f.open(QIODevice::WriteOnly);
    f.write(code.toAscii());
    f.close();
    
    KDevelop::DUChain::self()->updateContextForUrl(KDevelop::IndexedString(filename), 
                                                   static_cast<TopDUContext::Features>(TopDUContext::AllDeclarationsContextsAndUses | TopDUContext::ForceUpdate),
                                                   this, 1
                                                  );
    ICore::self()->languageController()->backgroundParser()->parseDocuments();
    AstBuilder* a = new AstBuilder(&m_pool);
    m_ast = a->parse(filename, const_cast<QString&>(code));
    return DUChain::self()->waitForUpdate(IndexedString(filename), TopDUContext::ForceUpdate);
}

ReferencedTopDUContext PyDUChainTest::parse(const QString& code, const QString& suffix)
{
    return parse_int(code, suffix);
}

void PyDUChainTest::testMultiFromImport()
{
    ReferencedTopDUContext ctx = parse("import i.localvar1\nimport i.localvar2\na=i.localvar1\nb=i.localvar2\n");
    QVERIFY(ctx);
    DUChainReadLocker lock;
    QList<Declaration*> a = ctx->findDeclarations(QualifiedIdentifier("a"));
    QList<Declaration*> b = ctx->findDeclarations(QualifiedIdentifier("b"));
    QVERIFY(! a.isEmpty());
    QVERIFY(! b.isEmpty());
    kDebug() << a.first()->abstractType()->toString();
    QVERIFY(b.first()->abstractType()->toString().endsWith("int"));
    QVERIFY(a.first()->abstractType()->toString().endsWith("int"));
}

void PyDUChainTest::testCrashes() {
    QFETCH(QString, code);
    ReferencedTopDUContext ctx = parse(code);
    QVERIFY(ctx);
}

void PyDUChainTest::testCrashes_data() {
    QTest::addColumn<QString>("code");
    
    QTest::newRow("unicode escape char") << "print u\"\\xe9\"";
    QTest::newRow("negative slice index") << "t = (1, 2, 3)\nd = t[-1]";
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
}

void PyDUChainTest::testClassVariables()
{
    ReferencedTopDUContext ctx = parse("class c():\n myvar = 3;\n def meth(self):\n  print myvar", "classvars");
    QVERIFY(ctx.data());
    DUChainWriteLocker lock(DUChain::lock());
    CursorInRevision relevantPosition(3, 10);
    DUContext* c = ctx->findContextAt(relevantPosition);
    QVERIFY(c);
    int useIndex = c->findUseAt(relevantPosition);
    if ( useIndex != -1 ) {
//         QVERIFY(useIndex != -1);
        QVERIFY(useIndex < c->usesCount());
        const Use* u = &(c->uses()[useIndex]);
        QVERIFY(not u->usedDeclaration(c->topContext()));
    }
}

void PyDUChainTest::testFlickering()
{
    QFETCH(QStringList, code);
    QFETCH(int, before);
    QFETCH(int, after);
    
    ReferencedTopDUContext ctx = parse(code[0], "flickering");
    DUChainWriteLocker lock(DUChain::lock());
    int count = ctx->localDeclarations().size();
    qDebug() << "Declaration count before: " << count;
    QVERIFY(count == before);
    lock.unlock();
    ctx = parse(code[1], "flickering");
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
    QVERIFY(func->findDeclarations(QualifiedIdentifier("vararg")).first()->abstractType()->toString() == "__kdevpythondocumentation_builtin_list");
    QVERIFY(func->findDeclarations(QualifiedIdentifier("kwarg")).first()->abstractType()->toString() == "__kdevpythondocumentation_builtin_dict");
}

void PyDUChainTest::testSimple()
{
    QFETCH(QString, code);
    QFETCH(int, decls);
    QFETCH(int, uses);
    
    ReferencedTopDUContext ctx = parse(code);
    DUChainWriteLocker lock(DUChain::lock());
    QVERIFY(ctx);
    
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
    QTest::newRow("bool") << "a = True" << 1 << 0;
    QTest::newRow("op") << "a = True and True;" << 1 << 0;
}

class AttributeRangeTestVisitor : public AstDefaultVisitor {
public:
    bool found;
    SimpleRange searchingForRange;
    QString searchingForIdentifier;
    virtual void visitAttribute(AttributeAst* node) {
        SimpleRange r(0, node->startCol, 0, node->endCol);
        qDebug() << "Found attr: " << r << node->attribute->value << ", looking for: " << searchingForRange << searchingForIdentifier;
        if ( r == searchingForRange && node->attribute->value == searchingForIdentifier ) {
            found = true;
            return;
        }
        AstDefaultVisitor::visitAttribute(node);
    }
    virtual void visitFunctionDefinition(FunctionDefinitionAst* node) {
        SimpleRange r(0, node->name->startCol, 0, node->name->endCol);
        qDebug() << "Found func: " << r << node->name->value << ", looking for: " << searchingForRange << searchingForIdentifier;
        qDebug() << node->arguments->vararg << node->arguments->kwarg;
        if ( r == searchingForRange && node->name->value == searchingForIdentifier ) {
            found = true;
            return;
        }
        if ( node->arguments->vararg ) {
            SimpleRange r(0, node->arguments->vararg_col_offset, 0, node->arguments->vararg_col_offset+node->arguments->vararg->value.length());
            qDebug() << "Found vararg: " << node->arguments->vararg->value << r;
            if ( r == searchingForRange && node->arguments->vararg->value == searchingForIdentifier ) {
                found = true;
                return;
            }
        }
        if ( node->arguments->kwarg ) {
            SimpleRange r(0, node->arguments->arg_col_offset, 0, node->arguments->arg_col_offset+node->arguments->kwarg->value.length());
            qDebug() << "Found kwarg: " << node->arguments->kwarg->value << r;
            if ( r == searchingForRange && node->arguments->kwarg->value == searchingForIdentifier ) {
                found = true;
                return;
            }
        }
        AstDefaultVisitor::visitFunctionDefinition(node);
    }
    virtual void visitClassDefinition(ClassDefinitionAst* node) {
        SimpleRange r(0, node->name->startCol, 0, node->name->endCol);
        qDebug() << "Found cls: " << r << node->name->value << ", looking for: " << searchingForRange << searchingForIdentifier;
        if ( r == searchingForRange && node->name->value == searchingForIdentifier ) {
            found = true;
            return;
        }
        AstDefaultVisitor::visitClassDefinition(node);
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
        SimpleRange r(0, scol, 0, ecol);
        
        AttributeRangeTestVisitor* visitor = new AttributeRangeTestVisitor();
        visitor->searchingForRange = r;
        visitor->searchingForIdentifier = identifier;
        visitor->visitCode(m_ast);
        
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
    QTest::newRow("attr_three_attributes") << "base.attr.subattr" << 3 << ( QStringList() << "5,8,attr" << "10,16,subattr" );
    QTest::newRow("attr_functionCall") << "base.attr().subattr" << 3 << ( QStringList() << "5,8,attr" << "12,18,subattr" );
    QTest::newRow("attr_stringSubscript") << "base.attr[\"a.b.c..de\"].subattr" << 3 << ( QStringList() << "5,8,attr" << "23,29,subattr" );
    QTest::newRow("attr_functionCallWithArguments") << "base.attr(arg1, arg2).subattr" << 5 << ( QStringList() << "5,8,attr" << "22,28,subattr" );
    QTest::newRow("attr_functionCallWithArgument_withInner") << "base.attr(arg1.parg2).subattr" << 5 << ( QStringList() << "5,8,attr" << "22,28,subattr" << "15,19,parg2" );
    
    QTest::newRow("funcrange_def") << "def func(): pass" << 1 << ( QStringList() << "4,7,func" );
    QTest::newRow("funcrange_spaces_def") << "def    func(): pass" << 1 << ( QStringList() << "7,10,func" );
    QTest::newRow("classdef_range") << "class cls(): pass" << 1 << ( QStringList() << "6,8,cls" );
    QTest::newRow("classdef_range_inheritance") << "class cls(parent1, parent2): pass" << 1 << ( QStringList() << "6,8,cls" );
    QTest::newRow("classdef_range_inheritance_spaces") << "class       cls(  parent1,    parent2     ):pass" << 1 << ( QStringList() << "12,14,cls" );
    QTest::newRow("vararg_kwarg") << "def func(*vararg, **kwargs): pass" << 2 << ( QStringList() << "10,16,vararg" << "20,26,kwargs" );
}

class TypeTestVisitor : public AstDefaultVisitor {
public:
    QString searchingForType;
    TopDUContextPointer ctx;
    bool found;
    virtual void visitName(NameAst* node) {
        if ( node->identifier->value != "checkme" ) return;
        QList<Declaration*> decls = ctx->findDeclarations(QualifiedIdentifier(node->identifier->value));
        if ( ! decls.length() ) {
            kDebug() << "No declaration found for " << node->identifier->value;
            return;
        }
        Declaration* d = decls.last();
        kDebug() << "Declaration: " << node->identifier->value << d->type<StructureType>();
        QVERIFY(d->abstractType());
        kDebug() << "found: " << node->identifier->value << "is" << d->abstractType()->toString() << "should be" << searchingForType;
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
    
    ReferencedTopDUContext ctx = parse(code.toAscii());
    QVERIFY(ctx);
    QVERIFY(m_ast);
    
    DUChainReadLocker lock(DUChain::lock());
    TypeTestVisitor* visitor = new TypeTestVisitor();
    visitor->ctx = TopDUContextPointer(ctx.data());
    visitor->searchingForType = expectedType;
    visitor->visitCode(m_ast);
    
    QCOMPARE(visitor->found, true);
}

void PyDUChainTest::testTypes_data()
{
    QTest::addColumn<QString>("code");
    QTest::addColumn<QString>("expectedType");
    
    QTest::newRow("listtype") << "checkme = []" << "list";
    QTest::newRow("listtype_func") << "checkme = list()" << "list";
    QTest::newRow("listtype_with_contents") << "checkme = [1, 2, 3, 4, 5]" << "list of int";
    QTest::newRow("listtype_extended") << "some_misc_var = []; checkme = some_misc_var" << "list";
    QTest::newRow("dicttype") << "checkme = {}" << "dict";
    QTest::newRow("dicttype_get") << "d = {0.4:5}; checkme = d.get(0)" << "int";
    QTest::newRow("dicttype_func") << "checkme = dict()" << "dict";
    QTest::newRow("dicttype_extended") << "some_misc_var = {}; checkme = some_misc_var" << "dict";
    QTest::newRow("bool") << "checkme = True" << "bool";
    QTest::newRow("float") << "checkme = 3.7" << "float";
    QTest::newRow("int") << "checkme = 3" << "int";
    
    QTest::newRow("list_access_right_open_slice") << "some_list = []; checkme = some_list[2:]" << "list";
    QTest::newRow("list_access_left_open_slice") << "some_list = []; checkme = some_list[:2]" << "list";
    QTest::newRow("list_access_closed_slice") << "some_list = []; checkme = some_list[2:17]" << "list";
    QTest::newRow("list_access_step") << "some_list = []; checkme = some_list[::2]" << "list";
    QTest::newRow("list_access_singleItem") << "some_list = []; checkme = some_list[42]" << "mixed";
    
    QTest::newRow("funccall_number") << "def foo(): return 3; \ncheckme = foo();" << "int";
    QTest::newRow("funccall_string") << "def foo(): return 'a'; \ncheckme = foo();" << "string";
    QTest::newRow("funccall_list") << "def foo(): return []; \ncheckme = foo();" << "list";
    QTest::newRow("funccall_dict") << "def foo(): return {}; \ncheckme = foo();" << "dict";
    
    QTest::newRow("tuple1") << "checkme, foo = 3, \"str\"" << "int";
    QTest::newRow("tuple2") << "foo, checkme = 3, \"str\"" << "string";
    QTest::newRow("tuple_type") << "checkme = 1, 2" << "tuple";
    
    QTest::newRow("dict_iteritems") << "d = {1:2, 3:4}\nfor checkme, k in d.iteritems(): pass" << "int";
    
    QTest::newRow("class_method_import") << "class c:\n attr = \"foo\"\n def m():\n  return attr;\n  return 3;\ni=c()\ncheckme=i.m()" << "int";
    QTest::newRow("getsListDecorator") << "foo = [1, 2, 3]\ncheckme = foo.reverse()" << "list of int";
    
    QTest::newRow("diff_local_classattr") << "class c(): attr = 1\ninst=c()\ncheckme = c.attr" << "int";
    QTest::newRow("diff_local_classattr2") << "local=3\nclass c(): attr = 1\ninst=c()\ncheckme = c.local" << "mixed";
    QTest::newRow("diff_local_classattr3") << "attr=3.5\nclass c(): attr = 1\ninst=c()\ncheckme = c.attr" << "int";
//     QTest::newRow("class_method_self") << "class c:\n def func(checkme, arg, arg2):\n  pass\n" << "c";
//    QTest::newRow("funccall_dict") << "def foo(): return foo; checkme = foo();" << (uint) IntegralType::TypeFunction;
    
    QTest::newRow("tuple_simple") << "mytuple = 3, 5.5\ncheckme, foobar = mytuple" << "int";
    QTest::newRow("tuple_simple2") << "mytuple = 3, 5.5\nfoobar, checkme = mytuple" << "float";
    QTest::newRow("tuple_simple3") << "mytuple = 3, 5.5, \"str\", 3, \"str\"\na, b, c, d, checkme = mytuple" << "string";
    
    QTest::newRow("tuple_funcret") << "def myfun(): return 3, 5\ncheckme, a = myfun()" << "int";
    QTest::newRow("tuple_funcret2") << "def myfun():\n t = 3, 5\n return t\ncheckme, a = myfun()" << "int";
    
    QTest::newRow("tuple_indexaccess") << "t = 3, 5.5\ncheckme = t[0]" << "int";
    QTest::newRow("tuple_indexaccess2") << "t = 3, 5.5\ncheckme = t[1]" << "float";
    
    QTest::newRow("tuple_loop") << "t = [(1, \"str\")]\nfor checkme, a in t: pass" << "int";
    
    QTest::newRow("args_type") << "def myfun(*args): checkme = args\nmyfun(3)" << "list of string";
    
    QTest::newRow("tuple_listof") << "l = [(1, 2), (3, 4)]\ncheckme = l[1][0]" << "int";
    
    QTest::newRow("functionCall_functionArg") << "def getstr(): return \"foo\"\n"
                                                 "def identity(f): return f\n"
                                                 "f1 = getstr\n"
                                                 "f2 = identity(getstr)\n"
                                                 "a = getstr()\n"
                                                 "b = f1()\n"
                                                 "checkme = f2()\n" << "string";
}

typedef QPair<Declaration*, int> pair;

void PyDUChainTest::testImportDeclarations() {
    QFETCH(QString, code);
    QFETCH(QStringList, expectedDecls);
    QFETCH(bool, shouldBeAliased);
    
    ReferencedTopDUContext ctx = parse(code.toAscii());
    QVERIFY(ctx);
    QVERIFY(m_ast);
    
    DUChainReadLocker lock(DUChain::lock());
    foreach ( QString expected, expectedDecls ) {
        bool found = false;
        QString name;
        QStringList split = expected.split(",");
        name = split[0];
//         int start, end;
//         start = split[1].toInt();
//         end = split[2].toInt();
        QList<pair> decls = ctx->allDeclarations(CursorInRevision::invalid(), ctx->topContext(), false);
        kDebug() << "FOUND DECLARATIONS:";
        foreach ( pair current, decls ) {
            kDebug() << current.first->toString() << current.first->identifier().identifier().byteArray() << name;
        }
        foreach ( pair current, decls ) {
            if ( ! ( current.first->identifier().identifier().byteArray() == name ) ) continue;
            kDebug() << "Found: " << current.first->toString() << " for " << name;
            AliasDeclaration* isAliased = dynamic_cast<AliasDeclaration*>(current.first);
            if ( isAliased && shouldBeAliased ) {
                found = true; // TODO fixme
            }
            else if ( ! shouldBeAliased && ! isAliased ) {
                found = true;
            }
        }
        QVERIFY(found);
    }
}

void PyDUChainTest::testImportDeclarations_data() {
    QTest::addColumn<QString>("code");
    QTest::addColumn<QStringList>("expectedDecls");
    QTest::addColumn<bool>("shouldBeAliased");
    
    QTest::newRow("from_import") << "from i import checkme" << ( QStringList() << "checkme,16,23" ) << true;
    QTest::newRow("import") << "import i" << ( QStringList() << "i,7,14" ) << false;
    QTest::newRow("import_as") << "import i as checkme" << ( QStringList() << "checkme,14,21" ) << false;
    QTest::newRow("from_import_as") << "from i import checkme as checkme" << ( QStringList() << "checkme,23,30" ) << true;
}

typedef QPair<Declaration*, int> p;

void PyDUChainTest::testAutocompletionFlickering()
{
    ReferencedTopDUContext ctx1 = parse("foo = 3\nfoo2 = 2\nfo", "autocompletion1");
    DUChainWriteLocker lock(DUChain::lock());
    QVERIFY(ctx1);
    QList<p> decls1 = ctx1->allDeclarations(CursorInRevision::invalid(), ctx1->topContext());
    QList<DeclarationId> declIds;
    foreach ( p d, decls1 ) {
        declIds << d.first->id();
    }
    lock.unlock();
    ReferencedTopDUContext ctx2 = parse("foo = 3\nfoo2 = 2\nfoo", "autocompletion1");
    QVERIFY(ctx2);
    lock.lock();
    QList<p> decls2 = ctx2->allDeclarations(CursorInRevision::invalid(), ctx2->topContext());
    foreach ( p d2, decls2 ) {
        kDebug() << "@1: " << d2.first->toString() << "::" << d2.first->id().hash() << "<>" << declIds.first().hash();
        QVERIFY(d2.first->id() == declIds.first());
        declIds.removeFirst();
    }
    lock.unlock();
    
    qDebug() << "=========================";
    
    ctx1 = parse("def func():\n\tfoo = 3\n\tfoo2 = 2\n\tfo", "autocompletion2");
    lock.lock();
    QVERIFY(ctx1);
    decls1 = ctx1->allDeclarations(CursorInRevision::invalid(), ctx1->topContext(), false).first().first->internalContext()
                 ->allDeclarations(CursorInRevision::invalid(), ctx1->topContext());
    declIds.clear();
    foreach ( p d, decls1 ) {
        declIds << d.first->id();
    }
    lock.unlock();
    ctx2 = parse("def func():\n\tfoo = 3\n\tfoo2 = 2\n\tfoo", "autocompletion2");
    QVERIFY(ctx2);
    lock.lock();
    decls2 = ctx2->allDeclarations(CursorInRevision::invalid(), ctx2->topContext(), false).first().first->internalContext()
                 ->allDeclarations(CursorInRevision::invalid(), ctx2->topContext());
    foreach ( p d2, decls2 ) {
        kDebug() << "@2: " << d2.first->toString() << "::" << d2.first->id().hash() << "<>" << declIds.first().hash();
        QVERIFY(d2.first->id() == declIds.first());
        declIds.removeFirst();
    }
    lock.unlock();
}

void PyDUChainTest::testDecorators()
{
    QFETCH(QString, code);
//     QFETCH(int, amountOfDecorators);
    QFETCH(QStringList, names);
    ReferencedTopDUContext ctx = parse(code);
    QVERIFY(ctx);
    DUChainReadLocker lock(DUChain::lock());
    Python::FunctionDeclaration* decl = dynamic_cast<Python::FunctionDeclaration*>(
        ctx->allDeclarations(CursorInRevision::invalid(), ctx->topContext()).first().first);
    QVERIFY(decl);
    foreach ( const QString& decoratorName, names ) {
        QVERIFY(Helper::findDecoratorByName<Python::FunctionDeclaration>(decl, decoratorName));
    }
}

void PyDUChainTest::testDecorators_data()
{
    QTest::addColumn<QString>("code");
    QTest::addColumn<int>("amountOfDecorators");
    QTest::addColumn<QStringList>("names");
    
    QTest::newRow("one_decorator") << "@foo\ndef func(): pass" << 1 << ( QStringList() << "foo" );
    QTest::newRow("decorator_with_args") << "@foo(2, \"bar\")\ndef func(): pass" << 1 << ( QStringList() << "foo");
    QTest::newRow("two_decorators") << "@foo\n@bar(17)\ndef func(): pass" << 2 << ( QStringList() << "foo" << "bar" );
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
    ReferencedTopDUContext ctx = parse(code);
    QVERIFY(ctx);
    DUChainReadLocker lock(DUChain::lock());
    QList<p> decls = ctx->allDeclarations(CursorInRevision::invalid(), ctx->topContext(), false);
    bool found = false;
    foreach ( const p& item, decls ) {
        kDebug() << "Checking declaration: " << item.first->identifier() << item.first->abstractType()->toString();
        if ( item.first->identifier().toString() == "checkme" ) {
            QVERIFY(item.first->abstractType()->toString() == "__kdevpythondocumentation_builtin_int");
            found = true;
        }
    }
    QVERIFY(found);
}

void PyDUChainTest::testInheritance_data()
{
    QTest::addColumn<QString>("code");
    
    QTest::newRow("simple") << "class A():\n\tattr = 3\n\nclass B(A):\n\tpass\n\ninst=B()\ncheckme = inst.attr";
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
    ReferencedTopDUContext ctx = parse(code.toAscii());
    QVERIFY(ctx);
    
    DUChainReadLocker lock(DUChain::lock());
    QList<Declaration*> decls = ctx->findDeclarations(QualifiedIdentifier("checkme"));
    QVERIFY(decls.length() > 0);
    QVERIFY(decls.first()->abstractType());
    kDebug() << "TEST type is: " << decls.first()->abstractType().unsafeData()->toString();
    if ( ! use_type ) {
        VariableLengthContainer* type = dynamic_cast<VariableLengthContainer*>(decls.first()->abstractType().unsafeData());
        QVERIFY(type);
        QVERIFY(type->contentType());
        QVERIFY(type->contentType().abstractType()->toString().replace("__kdevpythondocumentation_builtin_", "") == contenttype);
    }
    else {
        QVERIFY(decls.first()->abstractType());
        QVERIFY(decls.first()->abstractType()->toString().replace("__kdevpythondocumentation_builtin_", "") == contenttype);
    }
}

void PyDUChainTest::testContainerTypes_data()
{
    QTest::addColumn<QString>("code");
    QTest::addColumn<QString>("contenttype");
    QTest::addColumn<bool>("use_type");
    
    QTest::newRow("list_of_int") << "checkme = [1, 2, 3]" << "int" << false;
    QTest::newRow("list_of_int_call") << "checkme = list([1, 2, 3])" << "int" << false;
    QTest::newRow("generator") << "checkme = [i for i in [1, 2, 3]]" << "int" << false;
    QTest::newRow("list_access") << "list = [1, 2, 3]\ncheckme = list[0]" << "int" << true;
    QTest::newRow("set_of_int") << "checkme = {1, 2, 3}" << "int" << false;
    QTest::newRow("set_of_int_call") << "checkme = set({1, 2, 3})" << "int" << false;
    QTest::newRow("set_generator") << "checkme = {i for i in [1, 2, 3]}" << "int" << false;
    QTest::newRow("dict_of_int") << "checkme = {a:1, b:2, c:3}" << "int" << false;
    QTest::newRow("dict_of_int_call") << "checkme = dict({a:1, b:2, c:3})" << "int" << false;
    QTest::newRow("dict_generator") << "checkme = {\"Foo\":i for i in [1, 2, 3]}" << "int" << false;
    QTest::newRow("dict_access") << "list = {a:1, b:2, c:3}\ncheckme = list[0]" << "int" << true;
    QTest::newRow("generator_attribute") << "checkme = [item.capitalize() for item in ['foobar']]" << "string" << false;
    QTest::newRow("cannot_change_type") << "checkme = [\"Foo\", \"Bar\"]" << "string" << false;
    QTest::newRow("cannot_change_type") << "[1, 2, 3].append(5)\ncheckme = [\"Foo\", \"Bar\"]" << "string" << false;
    
    QTest::newRow("list_append") << "d = []\nd.append(3)\ncheckme = d[0]" << "int" << true;
}

