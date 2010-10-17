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

#ifndef PYTHONASTVISITOR_H
#define PYTHONASTVISITOR_H

#include "ast.h"
#include "parserexport.h"

/**
 * Note: This has been generated using utilities/generate.py
 * but you can modifiy it, it's not regenerated automatically
 */

namespace Python
{

class KDEVPYTHONPARSER_EXPORT AstVisitor
{
public:
    AstVisitor();
    virtual ~AstVisitor();

    typedef void (AstVisitor::*visitFunc)(Ast *);
    
    void visitNode(Ast* node);

    virtual void visitCode(CodeAst* node) { Q_UNUSED(node); };
    virtual void visitStatement(StatementAst* node) { Q_UNUSED(node); };
    virtual void visitFunctionDefinition(FunctionDefinitionAst* node) { Q_UNUSED(node); };
    virtual void visitClassDefinition(ClassDefinitionAst* node) { Q_UNUSED(node); };
    virtual void visitReturn(ReturnAst* node) { Q_UNUSED(node); };
    virtual void visitDelete(DeleteAst* node) { Q_UNUSED(node); };
    virtual void visitAssignment(AssignmentAst* node) { Q_UNUSED(node); };
    virtual void visitAugmentedAssignment(AugmentedAssignmentAst* node) { Q_UNUSED(node); };
    virtual void visitFor(ForAst* node) { Q_UNUSED(node); };
    virtual void visitWhile(WhileAst* node) { Q_UNUSED(node); };
    virtual void visitIf(IfAst* node) { Q_UNUSED(node); };
    virtual void visitWith(WithAst* node) { Q_UNUSED(node); };
    virtual void visitRaise(RaiseAst* node) { Q_UNUSED(node); };
    virtual void visitTryExcept(TryExceptAst* node) { Q_UNUSED(node); };
    virtual void visitTryFinally(TryFinallyAst* node) { Q_UNUSED(node); };
    virtual void visitAssertion(AssertionAst* node) { Q_UNUSED(node); };
    virtual void visitImport(ImportAst* node) { Q_UNUSED(node); };
    virtual void visitImportFrom(ImportFromAst* node) { Q_UNUSED(node); };
    virtual void visitExec(ExecAst* node) { Q_UNUSED(node); };
    virtual void visitGlobal(GlobalAst* node) { Q_UNUSED(node); };
    virtual void visitBreak(BreakAst* node) { Q_UNUSED(node); };
    virtual void visitContinue(ContinueAst* node) { Q_UNUSED(node); };
    virtual void visitPrint(PrintAst* node) { Q_UNUSED(node); };
    virtual void visitPass(PassAst* node) { Q_UNUSED(node); };
    virtual void visitExpression(ExpressionAst* node) { Q_UNUSED(node); };
    virtual void visitBooleanOperation(BooleanOperationAst* node) { Q_UNUSED(node); };
    virtual void visitBinaryOperation(BinaryOperationAst* node) { Q_UNUSED(node); };
    virtual void visitUnaryOperation(UnaryOperationAst* node) { Q_UNUSED(node); };
    virtual void visitLambda(LambdaAst* node) { Q_UNUSED(node); };
    virtual void visitIfExpression(IfExpressionAst* node) { Q_UNUSED(node); };
    virtual void visitDict(DictAst* node) { Q_UNUSED(node); };
    virtual void visitSet(SetAst* node) { Q_UNUSED(node); };
    virtual void visitListComprehension(ListComprehensionAst* node) { Q_UNUSED(node); };
    virtual void visitSetComprehension(SetComprehensionAst* node) { Q_UNUSED(node); };
    virtual void visitDictionaryComprehension(DictionaryComprehensionAst* node) { Q_UNUSED(node); };
    virtual void visitGeneratorExpression(GeneratorExpressionAst* node) { Q_UNUSED(node); };
    virtual void visitCompare(CompareAst* node) { Q_UNUSED(node); };
    virtual void visitRepr(ReprAst* node) { Q_UNUSED(node); };
    virtual void visitNumber(NumberAst* node) { Q_UNUSED(node); };
    virtual void visitString(StringAst* node) { Q_UNUSED(node); };
    virtual void visitYield(YieldAst* node) { Q_UNUSED(node); };
    virtual void visitName(NameAst* node) { Q_UNUSED(node); };
    virtual void visitCall(CallAst* node) { Q_UNUSED(node); };
    virtual void visitAttribute(AttributeAst* node) { Q_UNUSED(node); };
    virtual void visitSubscript(SubscriptAst* node) { Q_UNUSED(node); };
    virtual void visitList(ListAst* node) { Q_UNUSED(node); };
    virtual void visitTuple(TupleAst* node) { Q_UNUSED(node); };
    virtual void visitEllipsis(EllipsisAst* node) { Q_UNUSED(node); };
    virtual void visitSlice(SliceAst* node) { Q_UNUSED(node); };
    virtual void visitExtendedSlice(ExtendedSliceAst* node) { Q_UNUSED(node); };
    virtual void visitIndex(IndexAst* node) { Q_UNUSED(node); };
    virtual void visitArguments(ArgumentsAst* node) { Q_UNUSED(node); };
    virtual void visitKeyword(KeywordAst* node) { Q_UNUSED(node); };
    virtual void visitComprehension(ComprehensionAst* node) { Q_UNUSED(node); };
    virtual void visitExceptionHandler(ExceptionHandlerAst* node) { Q_UNUSED(node); };
    virtual void visitAlias(AliasAst* node) { Q_UNUSED(node); };

};
}

#endif
