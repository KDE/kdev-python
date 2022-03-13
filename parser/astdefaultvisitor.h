/*
    SPDX-FileCopyrightText: 2007 Andreas Pakulat <apaku@gmx.de>
    SPDX-FileCopyrightText: 2012 Patrick Spendrin <ps_ml@gmx.de>
    SPDX-FileCopyrightText: 2010-2014 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: LGPL-2.0-or-later
*/

#ifndef PYTHONASTDEFAULTVISITOR_H
#define PYTHONASTDEFAULTVISITOR_H

#include "astvisitor.h"
#include "parserexport.h"

/**
 * Note: This has been generated using utilities/generate.py
 * but you can modifiy it, it's not regenerated automatically
 */

namespace Python
{

class KDEVPYTHONPARSER_EXPORT AstDefaultVisitor : public AstVisitor
{
public:
    AstDefaultVisitor();
    ~AstDefaultVisitor() override;

    void visitCode(CodeAst* node) override;
    void visitFunctionDefinition(FunctionDefinitionAst* node) override;
    void visitClassDefinition(ClassDefinitionAst* node) override;
    void visitReturn(ReturnAst* node) override;
    void visitAwait(AwaitAst* node) override;
    void visitDelete(DeleteAst* node) override;
    void visitAssignment(AssignmentAst* node) override;
    void visitAugmentedAssignment(AugmentedAssignmentAst* node) override;
    void visitAnnotationAssignment(AnnotationAssignmentAst* node) override;
    void visitAssignmentExpression(AssignmentExpressionAst* node) override;
    void visitFor(ForAst* node) override;
    void visitWhile(WhileAst* node) override;
    void visitIf(IfAst* node) override;
    void visitWith(WithAst* node) override;
    void visitRaise(RaiseAst* node) override;
    void visitTry(TryAst* node) override;
    void visitAssertion(AssertionAst* node) override;
    void visitImport(ImportAst* node) override;
    void visitImportFrom(ImportFromAst* node) override;
    void visitGlobal(GlobalAst* node) override;
    void visitBreak(BreakAst* node) override;
    void visitContinue(ContinueAst* node) override;
    void visitPass(PassAst* node) override;
    void visitNonlocal(NonlocalAst* node) override;
    void visitBooleanOperation(BooleanOperationAst* node) override;
    void visitBinaryOperation(BinaryOperationAst* node) override;
    void visitUnaryOperation(UnaryOperationAst* node) override;
    void visitLambda(LambdaAst* node) override;
    void visitIfExpression(IfExpressionAst* node) override;
    void visitDict(DictAst* node) override;
    void visitSet(SetAst* node) override;
    void visitListComprehension(ListComprehensionAst* node) override;
    void visitSetComprehension(SetComprehensionAst* node) override;
    void visitDictionaryComprehension(DictionaryComprehensionAst* node) override;
    void visitGeneratorExpression(GeneratorExpressionAst* node) override;
    void visitCompare(CompareAst* node) override;
    void visitNumber(NumberAst* node) override;
    void visitString(StringAst* node) override;
    void visitJoinedString(JoinedStringAst* node) override;
    void visitFormattedValue(FormattedValueAst* node) override;
    void visitBytes(BytesAst* node) override;
    void visitYield(YieldAst* node) override;
    void visitYieldFrom(YieldFromAst* node) override;
    void visitName(NameAst* node) override;
    void visitNameConstant(NameConstantAst* node) override;
    void visitConstant(ConstantAst* node) override;
    void visitCall(CallAst* node) override;
    void visitAttribute(AttributeAst* node) override;
    void visitSubscript(SubscriptAst* node) override;
    void visitStarred(StarredAst* node) override;
    void visitList(ListAst* node) override;
    void visitTuple(TupleAst* node) override;
    void visitEllipsis(EllipsisAst* node) override;
    void visitSlice(SliceAst* node) override;
    void visitArguments(ArgumentsAst* node) override;
    void visitArg(ArgAst* node) override;
    void visitKeyword(KeywordAst* node) override;
    void visitComprehension(ComprehensionAst* node) override;
    void visitExceptionHandler(ExceptionHandlerAst* node) override;
    void visitAlias(AliasAst* node) override;
    void visitExpression(ExpressionAst* node) override;
    void visitWithItem(WithItemAst* node) override;
    virtual void visitIdentifier(Identifier* node);
};

class KDEVPYTHONPARSER_EXPORT AstFreeVisitor : public AstDefaultVisitor {
public:
    /*
     * lines = open('test.dat', 'r').readlines()
     * for line in lines: print line.replace(';\n', ' { AstDefaultVisitor::visit'+ line.split('visit')[1] \
     * .split('(')[0] +'(node); delete node; }')
     */

    // The CodeAst should not free itself, as this is supposed to be called from ~CodeAst.
    void visitCode(CodeAst* node) override { AstDefaultVisitor::visitCode(node); }
    void visitFunctionDefinition(FunctionDefinitionAst* node) override { AstDefaultVisitor::visitFunctionDefinition(node); delete node; }
    void visitClassDefinition(ClassDefinitionAst* node) override { AstDefaultVisitor::visitClassDefinition(node); delete node; }
    void visitReturn(ReturnAst* node) override { AstDefaultVisitor::visitReturn(node); delete node; }
    void visitDelete(DeleteAst* node) override { AstDefaultVisitor::visitDelete(node); delete node; }
    void visitAssignment(AssignmentAst* node) override { AstDefaultVisitor::visitAssignment(node); delete node; }
    void visitAugmentedAssignment(AugmentedAssignmentAst* node) override { AstDefaultVisitor::visitAugmentedAssignment(node); delete node; }
    void visitAnnotationAssignment(AnnotationAssignmentAst* node) override { AstDefaultVisitor::visitAnnotationAssignment(node); delete node; }
    void visitAssignmentExpression(AssignmentExpressionAst* node) override { AstDefaultVisitor::visitAssignmentExpression(node); delete node; }
    void visitFor(ForAst* node) override { AstDefaultVisitor::visitFor(node); delete node; }
    void visitWhile(WhileAst* node) override { AstDefaultVisitor::visitWhile(node); delete node; }
    void visitIf(IfAst* node) override { AstDefaultVisitor::visitIf(node); delete node; }
    void visitWith(WithAst* node) override { AstDefaultVisitor::visitWith(node); delete node; }
    void visitRaise(RaiseAst* node) override { AstDefaultVisitor::visitRaise(node); delete node; }
    void visitTry(TryAst* node) override { AstDefaultVisitor::visitTry(node); delete node; }
    void visitAssertion(AssertionAst* node) override { AstDefaultVisitor::visitAssertion(node); delete node; }
    void visitImport(ImportAst* node) override { AstDefaultVisitor::visitImport(node); delete node; }
    void visitImportFrom(ImportFromAst* node) override { AstDefaultVisitor::visitImportFrom(node); delete node; }
    void visitGlobal(GlobalAst* node) override { AstDefaultVisitor::visitGlobal(node); delete node; }
    void visitBreak(BreakAst* node) override { AstDefaultVisitor::visitBreak(node); delete node; }
    void visitContinue(ContinueAst* node) override { AstDefaultVisitor::visitContinue(node); delete node; }
    void visitPass(PassAst* node) override { AstDefaultVisitor::visitPass(node); delete node; }
    void visitNonlocal(NonlocalAst* node) override { AstDefaultVisitor::visitNonlocal(node); delete node; }
    void visitBooleanOperation(BooleanOperationAst* node) override { AstDefaultVisitor::visitBooleanOperation(node); delete node; }
    void visitBinaryOperation(BinaryOperationAst* node) override { AstDefaultVisitor::visitBinaryOperation(node); delete node; }
    void visitUnaryOperation(UnaryOperationAst* node) override { AstDefaultVisitor::visitUnaryOperation(node); delete node; }
    void visitLambda(LambdaAst* node) override { AstDefaultVisitor::visitLambda(node); delete node; }
    void visitIfExpression(IfExpressionAst* node) override { AstDefaultVisitor::visitIfExpression(node); delete node; }
    void visitDict(DictAst* node) override { AstDefaultVisitor::visitDict(node); delete node; }
    void visitSet(SetAst* node) override { AstDefaultVisitor::visitSet(node); delete node; }
    void visitListComprehension(ListComprehensionAst* node) override { AstDefaultVisitor::visitListComprehension(node); delete node; }
    void visitSetComprehension(SetComprehensionAst* node) override { AstDefaultVisitor::visitSetComprehension(node); delete node; }
    void visitDictionaryComprehension(DictionaryComprehensionAst* node) override { AstDefaultVisitor::visitDictionaryComprehension(node); delete node; }
    void visitGeneratorExpression(GeneratorExpressionAst* node) override { AstDefaultVisitor::visitGeneratorExpression(node); delete node; }
    void visitCompare(CompareAst* node) override { AstDefaultVisitor::visitCompare(node); delete node; }
    void visitNumber(NumberAst* node) override { AstDefaultVisitor::visitNumber(node); delete node; }
    void visitString(StringAst* node) override { AstDefaultVisitor::visitString(node); delete node; }
    void visitJoinedString(JoinedStringAst* node) override { AstDefaultVisitor::visitJoinedString(node); delete node; }
    void visitFormattedValue(FormattedValueAst* node) override { AstDefaultVisitor::visitFormattedValue(node); delete node; }
    void visitBytes(BytesAst* node) override { AstDefaultVisitor::visitBytes(node); delete node; }
    void visitYield(YieldAst* node) override { AstDefaultVisitor::visitYield(node); delete node; }
    void visitYieldFrom(YieldFromAst* node) override { AstDefaultVisitor::visitYieldFrom(node); delete node; }
    void visitName(NameAst* node) override { AstDefaultVisitor::visitName(node); delete node; }
    void visitNameConstant(NameConstantAst* node) override { AstDefaultVisitor::visitNameConstant(node); delete node; }
    void visitConstant(ConstantAst* node) override { AstDefaultVisitor::visitConstant(node); delete node; }
    void visitCall(CallAst* node) override { AstDefaultVisitor::visitCall(node); delete node; }
    void visitAttribute(AttributeAst* node) override { AstDefaultVisitor::visitAttribute(node); delete node; }
    void visitSubscript(SubscriptAst* node) override { AstDefaultVisitor::visitSubscript(node); delete node; }
    void visitStarred(StarredAst* node) override { AstDefaultVisitor::visitStarred(node); delete node; }
    void visitList(ListAst* node) override { AstDefaultVisitor::visitList(node); delete node; }
    void visitTuple(TupleAst* node) override { AstDefaultVisitor::visitTuple(node); delete node; }
    void visitEllipsis(EllipsisAst* node) override { AstDefaultVisitor::visitEllipsis(node); delete node; }
    void visitSlice(SliceAst* node) override { AstDefaultVisitor::visitSlice(node); delete node; }
    void visitArguments(ArgumentsAst* node) override { AstDefaultVisitor::visitArguments(node); delete node; }
    void visitArg(ArgAst* node) override { AstDefaultVisitor::visitArg(node); delete node; }
    void visitKeyword(KeywordAst* node) override { AstDefaultVisitor::visitKeyword(node); delete node; }
    void visitComprehension(ComprehensionAst* node) override { AstDefaultVisitor::visitComprehension(node); delete node; }
    void visitExceptionHandler(ExceptionHandlerAst* node) override { AstDefaultVisitor::visitExceptionHandler(node); delete node; }
    void visitAlias(AliasAst* node) override { AstDefaultVisitor::visitAlias(node); delete node; }
    void visitExpression(ExpressionAst* node) override { AstDefaultVisitor::visitExpression(node); delete node; }
    void visitWithItem(WithItemAst* node) override { AstDefaultVisitor::visitWithItem(node); delete node; }
    void visitIdentifier(Identifier* node) override { AstDefaultVisitor::visitIdentifier(node); delete node; }
};

KDEVPYTHONPARSER_EXPORT void free_ast_recursive(CodeAst* node);

}

#endif
