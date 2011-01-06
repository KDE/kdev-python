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

ReferencedTopDUContext PyDUChainTest::parse(const QString& code)
{
    ParseSession* session = new ParseSession;
    session->setContents( code + "\n" ); // append a newline in case the parser doesnt like it without one
    
    static int mytest=0;
    KUrl filename("/test"+QString::number(mytest++));
    session->setCurrentDocument(filename);
    
    QPair<CodeAst*, bool> parserResults = session->parse(0);
    CodeAst* ast = parserResults.first;
    m_ast = ast;
    
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
    
    ReferencedTopDUContext ctx = parse(code);
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
    
    ReferencedTopDUContext ctx = parse(code.toAscii());
    QVERIFY(ctx);
    
    QVERIFY(m_ast);
    
    for ( int i = 0; i < column_ranges.length(); i++ ) {
        DUChainReadLocker lock(DUChain::lock());
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
    uint searchingForType;
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
        QVERIFY(d->type<IntegralType>());
        kDebug() << "found: " << node->identifier->value << "is" << d->type<IntegralType>().constData()->dataType() << "should be" << searchingForType;
        if ( d->type<IntegralType>().constData()->dataType() == searchingForType ) {
            found = true;
            return;
        }
        AstDefaultVisitor::visitName(node);
    };
};

void PyDUChainTest::testTypes()
{
    QFETCH(QString, code);
    QFETCH(uint, expectedType);
    
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
    QTest::addColumn<uint>("expectedType");
    
    QTest::newRow("listtype") << "checkme = []" << (uint) IntegralTypeExtended::TypeList;
    QTest::newRow("listtype_extended") << "some_misc_var = []; checkme = some_misc_var" << (uint) IntegralTypeExtended::TypeList;
    QTest::newRow("dicttype") << "checkme = {}" << (uint) IntegralTypeExtended::TypeDict;
    QTest::newRow("dicttype_extended") << "some_misc_var = {}; checkme = some_misc_var" << (uint) IntegralTypeExtended::TypeDict;
    QTest::newRow("bool") << "checkme = True" << (uint) IntegralType::TypeBoolean;
    QTest::newRow("float") << "checkme = 3.7" << (uint) IntegralType::TypeFloat;
    
    QTest::newRow("list_access_right_open_slice") << "checkme = some_list[2:]" << (uint) IntegralTypeExtended::TypeList;
    QTest::newRow("list_access_left_open_slice") << "checkme = some_list[:2]" << (uint) IntegralTypeExtended::TypeList;
    QTest::newRow("list_access_closed_slice") << "checkme = some_list[2:17]" << (uint) IntegralTypeExtended::TypeList;
    QTest::newRow("list_access_step") << "checkme = some_list[::2]" << (uint) IntegralTypeExtended::TypeList;
    QTest::newRow("list_access_singleItem") << "checkme = some_list[42]" << (uint) IntegralType::TypeNull;
}


