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

#include "astdefaultvisitor.h"
#include "expressionvisitor.h"
#include "contextbuilder.h"
#include <language/duchain/types/functiontype.h>
#include "parser/parserConfig.h"
#include <astbuilder.h>
#include <language/duchain/aliasdeclaration.h>

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
    
    KUrl doc_url = KUrl(DOCFILE_PATH);
    doc_url.cleanPath(KUrl::SimplifyDirSeparators);

    DUChain::self()->updateContextForUrl(IndexedString(doc_url), KDevelop::TopDUContext::AllDeclarationsContextsAndUses);
    DUChain::self()->waitForUpdate(IndexedString(doc_url), KDevelop::TopDUContext::AllDeclarationsContextsAndUses);
    
    QFile f("/tmp/i.py");
    f.open(QIODevice::WriteOnly);
    f.write("def checkme(): pass\n");
    f.close();
    
    DUChain::self()->updateContextForUrl(IndexedString("/tmp/i.py"), KDevelop::TopDUContext::ForceUpdate);
    DUChain::self()->waitForUpdate(IndexedString("/tmp/i.py"), KDevelop::TopDUContext::ForceUpdate);

    DUChain::self()->disablePersistentStorage();
    KDevelop::CodeRepresentation::setDiskChangesForbidden(true);
}

ReferencedTopDUContext PyDUChainTest::parse(const QString& code)
{
    ParseSession* session = new ParseSession;
    session->setContents( code + "\n" ); // append a newline in case the parser doesnt like it without one
    
    static int mytest=0;
    KUrl filename("/tmp/pyduchaintest" + QString::number(mytest++) + ".py");
    QFile f(filename.path());
    f.open(QIODevice::WriteOnly);
    f.write(code.toAscii());
    f.close();
    
    DUChainReadLocker lock(DUChain::lock());
    ReferencedTopDUContext chain = DUChain::self()->chainForDocument(IndexedString(filename));
    lock.unlock();
    if ( chain ) {
        DUChainWriteLocker wlock(DUChain::lock());
        DUChain::self()->removeDocumentChain(chain.data());
    }
    DUChain::self()->updateContextForUrl(IndexedString(filename), KDevelop::TopDUContext::ForceUpdate);
    DUChain::self()->waitForUpdate(IndexedString(filename), KDevelop::TopDUContext::ForceUpdate);
    lock.lock();
    ReferencedTopDUContext ret = DUChain::self()->chainForDocument(IndexedString(filename));
    Q_ASSERT(ret.data());
    
    AstBuilder* a = new AstBuilder();
    m_ast = a->parse(filename, const_cast<QString&>(code));
    
    return ret;
}

void PyDUChainTest::testCrashes() {
    QFETCH(QString, code);
    ReferencedTopDUContext ctx = parse(code);
    QVERIFY(ctx);
}

void PyDUChainTest::testCrashes_data() {
    QTest::addColumn<QString>("code");
    
    QTest::newRow("unicode escape char") << "print u\"\\xe9\"";
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
        if ( r == searchingForRange && node->name->value == searchingForIdentifier ) {
            found = true;
            return;
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
    DUChainWriteLocker lock(DUChain::lock());
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
        if ( d->abstractType()->toString().replace("__kdevpythondocumentation_builtin_", "") == searchingForType ) {
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
    QTest::newRow("listtype_with_contents") << "checkme = [1, 2, 3, 4, 5]" << "list";
    QTest::newRow("listtype_extended") << "some_misc_var = []; checkme = some_misc_var" << "list";
    QTest::newRow("dicttype") << "checkme = {}" << "dict";
    QTest::newRow("dicttype_extended") << "some_misc_var = {}; checkme = some_misc_var" << "dict";
    QTest::newRow("bool") << "checkme = True" << "bool";
    QTest::newRow("float") << "checkme = 3.7" << "float";
    
    QTest::newRow("list_access_right_open_slice") << "checkme = some_list[2:]" << "list";
    QTest::newRow("list_access_left_open_slice") << "checkme = some_list[:2]" << "list";
    QTest::newRow("list_access_closed_slice") << "checkme = some_list[2:17]" << "list";
    QTest::newRow("list_access_step") << "checkme = some_list[::2]" << "list";
    QTest::newRow("list_access_singleItem") << "checkme = some_list[42]" << "null";
    
    QTest::newRow("funccall_number") << "def foo(): return 3; \ncheckme = foo();" << "float";
    QTest::newRow("funccall_string") << "def foo(): return 'a'; \ncheckme = foo();" << "string";
    QTest::newRow("funccall_list") << "def foo(): return []; \ncheckme = foo();" << "list";
    QTest::newRow("funccall_dict") << "def foo(): return {}; \ncheckme = foo();" << "dict";
    
    QTest::newRow("tuple1") << "checkme, foo = 3, \"str\"" << "float";
    QTest::newRow("tuple2") << "foo, checkme = 3, \"str\"" << "string";
//    QTest::newRow("funccall_dict") << "def foo(): return foo; checkme = foo();" << (uint) IntegralType::TypeFunction;
}

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
        int start, end;
        QStringList split = expected.split(",");
        name = split[0];
        start = split[1].toInt();
        end = split[2].toInt();
        QList<Declaration*> foundDecls = ctx->findDeclarations(QualifiedIdentifier(name));
        kDebug() << "Found " << foundDecls.length() << " Declarations for " << name;
        QVERIFY(foundDecls.length() > 0);
        foreach ( Declaration* current, foundDecls ) {
            bool isAliased = false;
            if ( current->topContext() != ctx->topContext() ) isAliased = true;
            if ( isAliased && shouldBeAliased ) {
                found = true; // TODO fixme
            }
            else if ( ! shouldBeAliased ) {
                kDebug() << "Found identifier: " << current->identifier().toString() << current->range().castToSimpleRange() << "(should be " << start << "," << end << ")";
                if ( current->range().start.column == start && current->range().end.column == end ) {
                    found = true;
                    break;
                }
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
    QTest::newRow("import") << "import checkme" << ( QStringList() << "checkme,7,14" ) << false;
    QTest::newRow("import_as") << "import foo as checkme" << ( QStringList() << "checkme,14,21" ) << false;
    QTest::newRow("from_import_as") << "from i import checkme as checkme" << ( QStringList() << "checkme,23,30" ) << true;
}

