/*
    SPDX-FileCopyrightText: 2012 Sven Brauch svenbrauch @googlemail.com

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#include <language/duchain/topducontext.h>
#include <language/codegen/coderepresentation.h>
#include <tests/autotestshell.h>
#include <tests/testcore.h>
#include <language/duchain/duchain.h>
#include <language/duchain/types/functiontype.h>
#include <language/duchain/aliasdeclaration.h>

#include "parsesession.h"
#include "pythoneditorintegrator.h"
#include "kdevpythonversion.h"
#include "declarationbuilder.h"
#include "usebuilder.h"
#include "astdefaultvisitor.h"
#include "expressionvisitor.h"
#include "contextbuilder.h"
#include "astbuilder.h"

#include "duchain/helpers.h"

#include "pyasttest.h"
#include "../astbuilder.h"
#include "../parserdebug.h"

#include <ktexteditor_version.h>

#include <QDebug>
#include <QtTest>

using namespace Python;

QTEST_MAIN(PyAstTest)

PyAstTest::PyAstTest(QObject* parent): QObject(parent)
{
    initShell();
}

void PyAstTest::initShell()
{
    AutoTestShell::init();
    TestCore* core = new TestCore();
    core->initialize(KDevelop::Core::NoUi);
    DUChain::self()->disablePersistentStorage();
    KDevelop::CodeRepresentation::setDiskChangesForbidden(true);
}

CodeAst::Ptr PyAstTest::getAst(QString code)
{
    QSharedPointer<AstBuilder> builder(new AstBuilder);
    CodeAst::Ptr result = builder->parse(QUrl(QStringLiteral("<empty>")), code);
    qDebug() << result->dump();
    return result;
}

class VerifyVisitor : public AstDefaultVisitor {
public:
    VerifyVisitor() : AstDefaultVisitor(), m_nodecount(0) { };
    void visitNode(Ast* node) override {
        m_nodecount += 1;
        QVERIFY(! node || node->astType < Ast::LastAstType);
        AstDefaultVisitor::visitNode(node);
    };
    void visitName(NameAst* node) override {
        QVERIFY(! node->identifier->value.isNull());
        AstDefaultVisitor::visitName(node);
    };
    void visitCode(CodeAst* node) override {
        AstDefaultVisitor::visitCode(node);
        qDebug() << "done, nodes visited:" << m_nodecount;
    };
    int m_nodecount;
};

void PyAstTest::testCode(QString code)
{
    CodeAst::Ptr ast = getAst(code);
    VerifyVisitor v;
    v.visitCode(ast.data());
}

void PyAstTest::testExceptionHandlers()
{
    QString code = QStringLiteral("try: pass\n"
                   "except FooBar as baz: pass\n"
                   "except Cat as baz: pass\n"
                   "except Dawg as asdf: pass\n");
    CodeAst::Ptr ast = getAst(code);
    VerifyVisitor v;
    v.visitCode(ast.data());
    QCOMPARE(ast->body.size(), 1);
    QVERIFY(ast->body.first()->astType == Ast::TryAstType);
    TryAst* try_ = static_cast<TryAst*>(ast->body.first());
    QCOMPARE(try_->handlers.size(), 3);
    for ( ExceptionHandlerAst* handler : try_->handlers ) {
        QVERIFY(handler->name);
        QCOMPARE(handler->name->astType, Ast::IdentifierAstType);
    }
}

void PyAstTest::testStatements()
{
    QFETCH(QString, code);
    testCode(code);
}

void PyAstTest::testStatements_data()
{
    QTest::addColumn<QString>("code");
    QTest::newRow("assign_int") << "a = 3";
    QTest::newRow("funcdef") << "def myfun(): pass";
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 5, 0)
    QTest::newRow("asyncfuncdef") << "async def myfun(): pass";
    QTest::newRow("asyncfuncdef2") << "async    def myfun(): pass";
    QTest::newRow("asyncfuncdef_await") << "async def myfun(): await 3";
#endif
    QTest::newRow("funcdef_args") << "def myfun(arg1, arg2): pass";
    QTest::newRow("funcdef_vararg") << "def myfun(arg1, *arg): pass";
    QTest::newRow("funcdef_kwarg") << "def myfun(**arg): pass";
    QTest::newRow("classdef_inheritance") << "class myclass(parent): pass";
    QTest::newRow("return") << "return 3";
    QTest::newRow("for") << "for i in 1, 2, 3: pass";
    QTest::newRow("while") << "while True: pass";
    QTest::newRow("if") << "if True: pass";
    QTest::newRow("ifElse") << "if True: pass\nelse:pass";
    QTest::newRow("with") << "with x as y: pass";
    QTest::newRow("raise") << "raise Exception";
    QTest::newRow("tryexcept") << "try:pass\nexcept:pass";
    QTest::newRow("tryexceptfinally") << "try:pass\nexcept:pass\nfinally:pass";
    QTest::newRow("assert") << "assert false";
    QTest::newRow("import") << "import foobar";
    QTest::newRow("importfrom") << "from foobar import bazbang";
    QTest::newRow("global") << "global x";
    QTest::newRow("break") << "while True: break";
    QTest::newRow("continue") << "while True: continue";
    QTest::newRow("pass") << "pass";
    QTest::newRow("nonlocal") << "nonlocal x";
    QTest::newRow("delete") << "del x";
    QTest::newRow("augassign_plus") << "a += b";
    QTest::newRow("augassign_minus") << "a -= b";
    QTest::newRow("augassign_mul") << "a *= b";
    QTest::newRow("augassign_div") << "a /= b";
    QTest::newRow("augassign_or") << "a &= b";
    QTest::newRow("augassign_and") << "a |= b";
    QTest::newRow("augassign_xor") << "a ^= b";
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 5, 0)
    QTest::newRow("augassign_matmul") << "a @= b";
#endif
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 6, 0)
    QTest::newRow("varannotation1") << "primes: List[int] = []";
    QTest::newRow("varannotation2") << "captain: str  # Note: no initial value!";
#endif

#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 10, 0)
    QTest::newRow("match_value") << "match x:\n case 1:\n  pass";
    QTest::newRow("match_singleton") << "match x:\n case True:\n  pass";
    QTest::newRow("match_sequence") << "match x:\n case [a, b]:\n  pass";
    QTest::newRow("match_mapping") << "match x:\n case {'type': 'update'}:\n  pass";
    // TODO: Mapping rest
    QTest::newRow("match_class") << "class Node:\n __match_args__=('type',)\ntype=1\nmatch x:\n case Node():\n  pass";
    QTest::newRow("match_star") << "match x:\n case [a, b, *c]:\n  pass";
    QTest::newRow("match_as") << "match x:\n case a:\n  pass";
    QTest::newRow("match_as_empty") << "match x:\n case _:\n  pass";
    QTest::newRow("match_or") << "match x:\n case a|b:\n  pass";
    QTest::newRow("match_guard") << "match x:\n case [a, b, c] if c != 0:\n  pass";
#endif

}

void PyAstTest::testSlices()
{
    QFETCH(QString, code);
    testCode(code);
}

void PyAstTest::testSlices_data()
{
    QTest::addColumn<QString>("code");
    QTest::newRow("slice1") << "x[1]";
    QTest::newRow("slice2") << "x[2:3]";
    QTest::newRow("slice3") << "x[::]";
    QTest::newRow("slice4") << "x[1:2:3]";
    QTest::newRow("slice_ellipsis") << "myList[1:2, ..., 0]";
}

void PyAstTest::testOther()
{
    QFETCH(QString, code);
    testCode(code);
}

void PyAstTest::testOther_data()
{
    QTest::addColumn<QString>("code");
    QTest::newRow("args") << "foo(bar, baz, *bang, **baa)";
    QTest::newRow("kws") << "foo(bar=baz, bang=3)";
    QTest::newRow("excpthandler") << "try:pass\nexcept foo as bar: pass";
    QTest::newRow("alias") << "import foo as bar";
}

void PyAstTest::testExpressions()
{
    QFETCH(QString, code);
    testCode(code);
}

void PyAstTest::testExpressions_data()
{
    QTest::addColumn<QString>("code");

    QTest::newRow("boolop") << "b or c";
    QTest::newRow("binop") << "b ^ c";
    QTest::newRow("unop") << "not a";
    QTest::newRow("lambda") << "lambda x: y";
    QTest::newRow("ifexpr") << "3 if 4 else 5";
    QTest::newRow("dict") << "{}";
    QTest::newRow("set") << "(3, 5)";
    QTest::newRow("listcomp") << "[x for x in y]";
    QTest::newRow("setcomp") << "(x for x in y)";
    QTest::newRow("dictcomp") << "{x:y for x, y in z}";
    QTest::newRow("comp") << "x < y";
    QTest::newRow("number") << "3";
    QTest::newRow("string") << "\"foo\"";
    QTest::newRow("bytes") << "b\"bytes\"";
    QTest::newRow("yield") << "yield x";
    QTest::newRow("name") << "foo";
    QTest::newRow("call") << "foo()";
    QTest::newRow("attribute") << "foo.bar";
    QTest::newRow("attribute_nontoplevel") << "while True: foo.bar";
    QTest::newRow("subscript") << "foo[3]";
    QTest::newRow("starred") << "*[1, 2, 3 ,4]";
    QTest::newRow("list") << "[]";
    QTest::newRow("tuple") << "()";
    QTest::newRow("None") << "None";
    QTest::newRow("False") << "False";
    QTest::newRow("True") << "True";
    QTest::newRow("Set") << "{1, 2, 3}";
    QTest::newRow("SetComp") << "{1 for x in [1, 2, 3]}";
    QTest::newRow("ExtSlice") << "A[1:3,3:5]";
    QTest::newRow("FString") << "f\"hi {a.b}\"";
    QTest::newRow("Formatted") << "'%s %s' % ('one', 'two')";

#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 6, 0)
    QTest::newRow("async_generator") << "async def foo(): result = [i async for i in aiter() if i % 2]";
    QTest::newRow("await_generator") << "async def foo(): result = [await fun() for fun in funcs]";

    QTest::newRow("underscore_literals") << "0x_FF_FF_FF_FF";
    QTest::newRow("formatted_string_literal") << "f\"He said his name is {name}.\"";
#endif
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 5, 0)
    QTest::newRow("dstar_unpack") << "ext_map = {\n"
        "       **{ext: self.obj_extension for ext in self.src_extensions},\n"
        "       **{ext: self.res_extension for ext in self._rc_extensions + self._mc_extensions},\n"
    "}";
    QTest::newRow("async_for") << "[i async for i in foo()]";
    QTest::newRow("async_for_stmt") << "async for x in y: pass";
    QTest::newRow("async_with_stmt") << "async with x as y: pass";
#endif
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 8, 0)
    QTest::newRow("assignment_expr_1") << "a = (b := 10)";
    QTest::newRow("assignment_expr_2") << "a = [q for z in (1, 2, 3) if (q := 2*z)]";
    QTest::newRow("positional_params") << "def foo(a, b, /, c, d, *, e): pass";
#endif
}

void PyAstTest::testCorrectedFuncRanges()
{
    QFETCH(QString, code);
    QFETCH(KTextEditor::Range, range);

    CodeAst::Ptr ast = getAst(code);
    QVERIFY(ast);
    for ( Ast* node : ast->body ) {
        if ( node->astType != Ast::FunctionDefinitionAstType ) {
            continue;
        }
        FunctionDefinitionAst* func = static_cast<FunctionDefinitionAst*>(node);
        QVERIFY(func->name);
        qCDebug(KDEV_PYTHON_PARSER) << func->name->range() << range;
        QCOMPARE(func->name->range(), range);
    }
}

void PyAstTest::testCorrectedFuncRanges_data()
{
    QTest::addColumn<QString>("code");
    QTest::addColumn<KTextEditor::Range>("range");

    QTest::newRow("decorator") << "@decorate\ndef func(arg): pass" << KTextEditor::Range(1, 4, 1, 7);
    QTest::newRow("decorator_arg") << "@decorate(yomama=3)\ndef func(arg): pass" << KTextEditor::Range(1, 4, 1, 7);
    QTest::newRow("two_decorators") << "@decorate2\n@decorate\ndef func(arg): pass" << KTextEditor::Range(2, 4, 2, 7);
    QTest::newRow("decorate_class") << "class foo:\n @decorate2\n @decorate\n def func(arg): pass" << KTextEditor::Range(3, 5, 3, 8);
}

void PyAstTest::testNewPython3()
{
    QFETCH(QString, code);
    testCode(code);
}

void PyAstTest::testNewPython3_data()
{
    QTest::addColumn<QString>("code");
    QTest::newRow("funcannotation1") << "def haul(item: Haulable, *vargs: PackAnimal) -> Distance: pass";
    QTest::newRow("funcannotation2") << "def foo() -> expr: pass";
    QTest::newRow("funcannotation3") << "def foo(a: 'x', b: 5 + 6, c: list) -> max(2, 9): pass";
    QTest::newRow("kwonly1") << "def compare(a, b, *, key=None): pass";
    QTest::newRow("kwonly2") << "def foo(a: 'x', b: 5 + 6, c: list) -> max(2, 9): pass";
    QTest::newRow("listunpack") << "(a, *rest, b) = range(5)";
    QTest::newRow("metaclass") << "class C(metaclass=M): pass";
    QTest::newRow("exception_chain") << "raise SecondaryException() from primary_exception";
    QTest::newRow("yield_from") << "def foo(): yield from [1, 2, 3]";
}

void PyAstTest::testClass()
{
    testCode(QStringLiteral("class c: pass"));
}

#include "moc_pyasttest.cpp"
