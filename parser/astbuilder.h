/***************************************************************************
 *   This file is part of KDevelop                                         *
 *   Copyright 2007 Andreas Pakulat <apaku@gmx.de>                         *
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU Library General Public License as       *
 *   published by the Free Software Foundation; either version 2 of the    *
 *   License, or (at your option) any later version.                       *
 *                                                                         *
 *   This program is distributed in the hope that it will be useful,       *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
 *   GNU General Public License for more details.                          *
 *                                                                         *
 *   You should have received a copy of the GNU Library General Public     *
 *   License along with this program; if not, write to the                 *
 *   Free Software Foundation, Inc.,                                       *
 *   51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.         *
 ***************************************************************************/

#ifndef ASTBUILDER_H
#define ASTBUILDER_H

#include <QtCore/QStack>

#include "ast.h"
#include <kurl.h>
#include <QDomDocument>
#include "kdebug.h"
#include "QXmlStreamReader"
#include <language/duchain/topducontext.h>

namespace PythonParser
{
    class Parser;
    class AstNode;
}

namespace Python
{
    class Ast;
    class CodeAst;

typedef QMap<QString, QString> stringDictionary;

class AstBuilder
{
    
public:
    CodeAst* parse(KUrl filename, const QString& contents);
    QList<KDevelop::ProblemPointer> m_problems;
private:
    CodeAst* parseXmlAst(QString xml);
    QString getXmlForFile(KUrl filename, const QString& contents);
    void parseXmlAstNode(QXmlStreamReader* xmlast, QXmlStreamReader::TokenType token);
    bool parseAstNode(QString name, QString text, const QList<QXmlStreamAttribute>& attributes);
    
    KDevelop::TopDUContext* m_topContext;
    
    QList<Ast*> m_nodeStack;
    
    // one map for regular ast nodes, and the others for primitive nodes of different types
    QMap<int, Ast*> m_nodeMap;
    QMap<int, ExpressionAst::Context> m_contextNodeMap;
    QMap<int, Ast::BooleanOperationTypes> m_boolOpNodeMap;
    QMap<int, Ast::ComparisonOperatorTypes> m_compOpNodeMap;
    QMap<int, Ast::OperatorTypes> m_opNodeMap;
    QMap<int, Ast::UnaryOperatorTypes> m_unaryOpNodeMap;
    
    QStack<Ast*> m_astStack;
    QMap<int, stringDictionary> m_attributeStore;
    Ast* m_currentNode;
    
    Ast::BooleanOperationTypes resolveBooleanOperator(const QString& identifier);
    Ast::ComparisonOperatorTypes resolveComparisonOperator(const QString& identifier);
    Ast::OperatorTypes resolveOperator(const QString& identifier);
    Ast::UnaryOperatorTypes resolveUnaryOperator(const QString& identifier);
    ExpressionAst::Context resolveContext(const QString& identifier);
    
    QList<Ast::BooleanOperationTypes> resolveBooleanOperatorList(const QString& identifiers);
    QList<Ast::ComparisonOperatorTypes> resolveComparisonOperatorList(const QString& identifiers);
    QList<Ast::OperatorTypes> resolveOperatorList(const QString& identifiers);
    QList<Ast::UnaryOperatorTypes> resolveUnaryOperatorList(const QString& identifiers);
    QList<ExpressionAst::Context> resolveContextList(const QString& identifiers);
    
    void populateAst();
    
    template<typename T> QList<T*> resolveNodeList(const QString& commaSeperatedIdentifiers);
    template<typename T> T* resolveNode(const QString& identifier);
    
    Identifier* createIdentifier(const QString& name, Ast* range);
    
    FunctionDefinitionAst* populateFunctionDefinitionAst(Ast* ast, const stringDictionary& currentAttributes);
    AssignmentAst* populateAssignmentAst(Ast* ast, const stringDictionary& currentAttributes);
    CodeAst* populateCodeAst(Ast* ast, const stringDictionary& currentAttributes);
    ClassDefinitionAst* populateClassDefinitonAst(Ast* ast, const stringDictionary& currentAttributes);
    NameAst* populateNameAst(Ast* ast, const stringDictionary& currentAttributes);
    ReturnAst* populateReturnAst(Ast* ast, const stringDictionary& currentAttributes);
    DeleteAst* populateDeleteAst(Ast* ast, const stringDictionary& currentAttributes);
    ForAst* populateForAst(Ast* ast, const stringDictionary& currentAttributes);
    WhileAst* populateWhileAst(Ast* ast, const stringDictionary& currentAttributes);
    PrintAst* populatePrintAst(Ast* ast, const stringDictionary& currentAttributes);
    IfAst* populateIfAst(Ast* ast, const stringDictionary& currentAttributes);
    LambdaAst* populateLambdaAst(Ast* ast, const stringDictionary& currentAttributes);
    BooleanOperationAst* populateBooleanOperationAst(Ast* ast, const stringDictionary& currentAttributes);
    CallAst* populateCallAst(Ast* ast, const stringDictionary& currentAttributes);
    DictAst* populateDictAst(Ast* ast, const stringDictionary& currentAttributes);
    ListAst* populateListAst(Ast* ast, const stringDictionary& currentAttributes);
    TupleAst* populateTupleAst(Ast* ast, const stringDictionary& currentAttributes);
    AugmentedAssignmentAst* populateAugmentedAssignmentAst(Ast* ast, const stringDictionary& currentAttributes);
    WithAst* populateWithAst(Ast* ast, const stringDictionary& currentAttributes);
    RaiseAst* populateRaiseAst(Ast* ast, const stringDictionary& currentAttributes);
    TryExceptAst* populateTryExceptAst(Ast* ast, const stringDictionary& currentAttributes);
    TryFinallyAst* populateTryFinallyAst(Ast* ast, const stringDictionary& currentAttributes);
    AssertionAst* populateAssertionAst(Ast* ast, const stringDictionary& currentAttributes);
    ImportAst* populateImportAst(Ast* ast, const stringDictionary& currentAttributes);
    ImportFromAst* populateImportFromAst(Ast* ast, const stringDictionary& currentAttributes);
    ExecAst* populateExecAst(Ast* ast, const stringDictionary& currentAttributes);
    GlobalAst* populateGlobalAst(Ast* ast, const stringDictionary& currentAttributes);
    BinaryOperationAst* populateBinaryOperationAst(Ast* ast, const stringDictionary& currentAttributes);
    AliasAst* populateAliasAst(Ast* ast, const stringDictionary& currentAttributes);
    UnaryOperationAst* populateUnaryOperationAst(Ast* ast, const stringDictionary& currentAttributes);
    IfExpressionAst* populateIfExpressionAst(Ast* ast, const stringDictionary& currentAttributes);
    ListComprehensionAst* populateListComprehensionAst(Ast* ast, const stringDictionary& currentAttributes);
    GeneratorExpressionAst* populateGeneratorExpressionAst(Ast* ast, const stringDictionary& currentAttributes);
    ComprehensionAst* populateComprehensionAst(Ast* ast, const stringDictionary& currentAttributes);
    CompareAst* populateCompareAst(Ast* ast, const stringDictionary& currentAttributes);
    NumberAst* populateNumberAst(Ast* ast, const stringDictionary& currentAttributes);
    StringAst* populateStringAst(Ast* ast, const stringDictionary& currentAttributes);
    AttributeAst* populateAttributeAst(Ast* ast, const stringDictionary& currentAttributes);
    SubscriptAst* populateSubscriptAst(Ast* ast, const stringDictionary& currentAttributes);
    SliceAst* populateSliceAst(Ast* ast, const stringDictionary& currentAttributes);
    KeywordAst* populateKeywordAst(Ast* ast, const stringDictionary& currentAttributes);
    ArgumentsAst* populateArgumentsAst(Ast* ast, const stringDictionary& currentAttributes);
    IndexAst* populateIndexAst(Ast* ast, const stringDictionary& currentAttributes);
    ExceptionHandlerAst* populateExceptionHandlerAst(Ast* ast, const stringDictionary& currentAttributes);
};

}

#endif