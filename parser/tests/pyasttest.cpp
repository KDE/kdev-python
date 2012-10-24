/*
    This file is part of kdev-python, the python language plugin for KDevelop
    Copyright (C) 2012  Sven Brauch svenbrauch@googlemail.com

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
#include <language/duchain/dumpchain.h>
#include <language/codegen/coderepresentation.h>
#include <tests/autotestshell.h>
#include <tests/testcore.h>
#include <language/duchain/duchain.h>
#include <QtTest/QtTest>
#include <KStandardDirs>
#include <language/duchain/types/functiontype.h>
#include <language/duchain/aliasdeclaration.h>

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

#include "pyasttest.h"
#include "../astbuilder.h"

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

CodeAst* PyAstTest::getAst(QString code)
{
    KDevPG::MemoryPool pool;
    AstBuilder* builder = new AstBuilder(&pool);
    CodeAst* result = builder->parse(KUrl("<empty>"), code);
    return result;
}

class VerifyVisitor : public AstDefaultVisitor {
public:
    VerifyVisitor() : AstDefaultVisitor() { };
    virtual void visitNode(Ast* node) {
        QVERIFY(node);
        QVERIFY(node->astType <= Ast::LastAstType);
        AstDefaultVisitor::visitNode(node);
    };
    virtual void visitName(NameAst* node) {
        QVERIFY(! node->identifier->value.isNull());
    };
};

void PyAstTest::testCode(QString code)
{
    CodeAst* ast = getAst(code);
    VerifyVisitor v;
    v.visitCode(ast);
}

void PyAstTest::testClass()
{
    testCode("class c: pass");
}

