/*
    This file is part of kdev-python, the python language plugin for KDevelop
    Copyright (C) 2014 Gregor Vollmer <gregor@celement.de>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

#include <language/duchain/topducontext.h>
#include <language/codegen/coderepresentation.h>
#include <tests/autotestshell.h>
#include <tests/testcore.h>
#include <language/duchain/duchain.h>
#include <QtTest/QtTest>
#include <language/duchain/types/functiontype.h>

#include "pythoneditorintegrator.h"
#include "astdefaultvisitor.h"
#include "astbuilder.h"

#include "pycythontest.h"
#include "../cythonsyntaxremover.h"
#include "../astbuilder.h"

#include <QDebug>
#include "../parserdebug.h"

using namespace Python;

QTEST_MAIN(PyCythonTest)
Q_DECLARE_METATYPE(KTextEditor::Range);

PyCythonTest::PyCythonTest(QObject* parent): QObject(parent)
{
    initShell();
}

void PyCythonTest::initShell()
{
    AutoTestShell::init();
    TestCore* core = new TestCore();
    core->initialize(KDevelop::Core::NoUi);
    DUChain::self()->disablePersistentStorage();
    KDevelop::CodeRepresentation::setDiskChangesForbidden(true);
}

CodeAst::Ptr PyCythonTest::getAst(QString code, KUrl filename)
{
    QSharedPointer<AstBuilder> builder(new AstBuilder);
    m_builder = builder;
    CodeAst::Ptr result = builder->parse(filename, code);
    return result;
}

class VerifyVisitor : public AstDefaultVisitor {
public:
    VerifyVisitor() : AstDefaultVisitor(), m_nodecount(0) { };
    virtual void visitNode(Ast* node) {
        m_nodecount += 1;
        QVERIFY(! node || node->astType < Ast::LastAstType);
        AstDefaultVisitor::visitNode(node);
    };
    virtual void visitName(NameAst* node) {
        QVERIFY(! node->identifier->value.isNull());
        AstDefaultVisitor::visitName(node);
    };
    virtual void visitCode(CodeAst* node) {
        AstDefaultVisitor::visitCode(node);
        qDebug() << "done, nodes visited:" << m_nodecount;
    };
    int m_nodecount;
};


void PyCythonTest::testCythonReplacement()
{
    QFETCH(QString, input);
    QFETCH(QString, output);
    QFETCH(bool, do_python_test);
    CythonSyntaxRemover stripper;
    QCOMPARE(stripper.stripCythonSyntax(input), output);
    if(do_python_test) {
        CodeAst::Ptr ast = getAst(input, KUrl("test.pyx"));
        VerifyVisitor v;
        v.visitCode(ast.data());
        QVERIFY(m_builder->m_problems.isEmpty());
    }
}

void PyCythonTest::testCythonReplacement_data()
{
    QTest::addColumn<QString>("input");
    QTest::addColumn<QString>("output");
    QTest::addColumn<bool>("do_python_test");
    QTest::newRow("cfunction") << "cdef foo(a, b): pass" << "def foo(a, b): pass" << true;
    QTest::newRow("cfunction_staticreturn1") << "cdef int foo(): pass" << "def foo(): pass" << true;
    QTest::newRow("cfunction_staticreturn2") << "cdef _SomeExtendedClass foo(): pass" << "def foo(): pass" << true;
    QTest::newRow("cfunction_staticreturn2") << "cdef float* foo(): pass" << "def foo(): pass" << true;
    QTest::newRow("cfunction_staticargs1") << "cdef foo(int a, b): pass" << "def foo(    a, b): pass" << true;
    QTest::newRow("cfunction_staticargs2") << "cdef foo(int* a, float b): pass" << "def foo(     a,       b): pass" << true;
    QTest::newRow("cfunction_staticargs3") << "cpdef addSubnodes(self, _Node node): pass" << "def addSubnodes(self,       node): pass" << true;
    QTest::newRow("cfunction_staticargsandreturn") << "cdef double* foo(int a, b): pass" << "def foo(    a, b): pass" << true;
    QTest::newRow("cfunction_exception1") << "cdef double* foo(int a, b) except *: pass" << "def foo(    a, b): pass" << true;
    QTest::newRow("cfunction_exception2") << "cdef double* foo(int a, b) except FoobarException: pass" << "def foo(    a, b): pass" << true;
    QTest::newRow("cdefclass1") << "cdef class Test:\n    cdef int a\n    cdef float* b" << "class Test:\n    pass\n    pass" << true;
    QTest::newRow("cdefclass2_pointer") << "cdef class SpatialList:\n    cdef spatial.SpatialList *thisptr\n" << "class SpatialList:\n    pass\n" << true;
    QTest::newRow("cdefclass_crash") << "cdef class Test:\n    def foo()" << "class Test:\n    def foo()" << false;
//     QTest::newRow("cdefclassproperty") << "cdef class Foo:\n    property Bar:\n        def __get__(self): pass";
    QTest::newRow("statictype") << "def foo():\n    cdef int bar\n    bar = 4\n" << "def foo():\n    pass\n    bar = 4\n" << true;
    QTest::newRow("cimport1") << "cimport foo" << "" << true;
    QTest::newRow("cimport2") << "cimport foo as bar" << "" << true;
    QTest::newRow("cimport3") << "from bar cimport foo" << "" << true;
    QTest::newRow("cimport4") << "from bar cimport foo as spam" << "" << true;
    QTest::newRow("longcode") <<  "from bar import foo\n\ncpdef helloWorld(int b) except (5 + \n3):\n    cdef int i\n    i = 5\n\n" << "from bar import foo\n\ndef helloWorld(    b):\n\n    pass\n    i = 5\n\n" << true;
    QTest::newRow("buffertypes") << "cpdef _OctreeNode findNode(self, np.ndarray[np.float64_t, ndim=1] coord): pass" << "def findNode(self,                                  coord): pass" << true;
    QTest::newRow("funcmultiline") << "cdef foobar(int foo,\n           float* bar,\n           np.ndarray[ndim = 1] spam):\n    pass" << "def foobar(    foo,\n                  bar,\n                                spam):\n    pass" << true;
    QTest::newRow("defaultargs_aka_crap") << "cdef foobar(int foo, float* bar=None,\n           ham=unicode(\"Spam)\\\")\"), _Node bloat=None):\n    pass" << "def foobar(    foo,        bar=None,\n           ham=unicode(\"Spam)\\\")\"),       bloat=None):\n    pass" << true;
    QTest::newRow("ctypedef") << "ctypedef np.float64_t DTYPE_t  # Hallo Welt" << "# Hallo Welt" << true;
    QTest::newRow("cdefvar1") << "def foo():\n    cdef int bar\n    bar = 3" << "def foo():\n    pass\n    bar = 3" << true;
    QTest::newRow("cdefvar2") << "def foo():\n    cdef float* bar, ham, spam\n" << "def foo():\n    pass\n" << true;
    QTest::newRow("cdefvar3") << "def foo():\n    cdef np.ndarray[dtype=float32, ndim=2] bar, ham, spam\n" << "def foo():\n    pass\n" << true;
}

void PyCythonTest::testCythonRanges() {
    QFETCH(QString, code);
    QFETCH(KTextEditor::Range, range);

    CodeAst::Ptr ast = getAst(code, KUrl("test.pyx"));
    QVERIFY(ast);
    foreach ( Ast* node, ast->body ) {
        if ( node->astType != Ast::FunctionDefinitionAstType ) {
            continue;
        }
        FunctionDefinitionAst* func = static_cast<FunctionDefinitionAst*>(node);
        QVERIFY(func->name);
        qCDebug(KDEV_PYTHON_PARSER) << func->name->range() << range;
        QCOMPARE(func->name->range(), range);
    }
}

void PyCythonTest::testCythonRanges_data()
{
    QTest::addColumn<QString>("code");
    QTest::addColumn<KTextEditor::Range>("range");

    QTest::newRow("cdef") << "cdef foobar(arg): pass" << KTextEditor::Range(0, 5, 0, 10);
    QTest::newRow("cdef_return") << "cdef float* foobar(arg): pass" << KTextEditor::Range(0, 12, 0, 17);
    QTest::newRow("normal_def") << "def foobar(arg): pass" << KTextEditor::Range(0, 4, 0, 9);
}


