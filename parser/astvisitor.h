/*
    SPDX-FileCopyrightText: 2007 Andreas Pakulat <apaku@gmx.de>
    SPDX-FileCopyrightText: 2012 Sven Brauch <svenbrauch@googlemail.com>
    SPDX-FileCopyrightText: 2012 Patrick Spendrin <ps_ml@gmx.de>

    SPDX-License-Identifier: LGPL-2.0-or-later
*/

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

    virtual void visitNode(Ast* node);

    template <typename T> void visitNodeList( const QList<T*>& l ) {
        foreach ( T* node, l ) {
            visitNode(node);
        }
    }

    virtual void visitCode(CodeAst* node) { Q_UNUSED(node); };
    virtual void visitStatement(StatementAst* node) { Q_UNUSED(node); };
    virtual void visitFunctionDefinition(FunctionDefinitionAst* node) { Q_UNUSED(node); };
    virtual void visitClassDefinition(ClassDefinitionAst* node) { Q_UNUSED(node); };
    virtual void visitReturn(ReturnAst* node) { Q_UNUSED(node); };
    virtual void visitAwait(AwaitAst* node) { Q_UNUSED(node); };
    virtual void visitDelete(DeleteAst* node) { Q_UNUSED(node); };
    virtual void visitAssignment(AssignmentAst* node) { Q_UNUSED(node); };
    virtual void visitAugmentedAssignment(AugmentedAssignmentAst* node) { Q_UNUSED(node); };
    virtual void visitAnnotationAssignment(AnnotationAssignmentAst* node) { Q_UNUSED(node); };
    virtual void visitAssignmentExpression(AssignmentExpressionAst* node) { Q_UNUSED(node); };
    virtual void visitFor(ForAst* node) { Q_UNUSED(node); };
    virtual void visitWhile(WhileAst* node) { Q_UNUSED(node); };
    virtual void visitIf(IfAst* node) { Q_UNUSED(node); };
    virtual void visitWith(WithAst* node) { Q_UNUSED(node); };
    virtual void visitRaise(RaiseAst* node) { Q_UNUSED(node); };
    virtual void visitTry(TryAst* node) { Q_UNUSED(node); };
    virtual void visitAssertion(AssertionAst* node) { Q_UNUSED(node); };
    virtual void visitImport(ImportAst* node) { Q_UNUSED(node); };
    virtual void visitImportFrom(ImportFromAst* node) { Q_UNUSED(node); };
    virtual void visitGlobal(GlobalAst* node) { Q_UNUSED(node); };
    virtual void visitBreak(BreakAst* node) { Q_UNUSED(node); };
    virtual void visitContinue(ContinueAst* node) { Q_UNUSED(node); };
    virtual void visitPass(PassAst* node) { Q_UNUSED(node); };
    virtual void visitNonlocal(NonlocalAst* node) { Q_UNUSED(node); };
    virtual void visitExpression(ExpressionAst* node) { Q_UNUSED(node); };
    virtual void visitYieldFrom(YieldFromAst* node) { Q_UNUSED(node); };
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
    virtual void visitNumber(NumberAst* node) { Q_UNUSED(node); };
    virtual void visitString(StringAst* node) { Q_UNUSED(node); };
    virtual void visitFormattedValue(FormattedValueAst* node) { Q_UNUSED(node); };
    virtual void visitJoinedString(JoinedStringAst* node) { Q_UNUSED(node); };
    virtual void visitBytes(BytesAst* node) { Q_UNUSED(node); };
    virtual void visitYield(YieldAst* node) { Q_UNUSED(node); };
    virtual void visitName(NameAst* node) { Q_UNUSED(node); };
    virtual void visitNameConstant(NameConstantAst* node) { Q_UNUSED(node); };
    virtual void visitCall(CallAst* node) { Q_UNUSED(node); };
    virtual void visitAttribute(AttributeAst* node) { Q_UNUSED(node); };
    virtual void visitSubscript(SubscriptAst* node) { Q_UNUSED(node); };
    virtual void visitStarred(StarredAst* node) { Q_UNUSED(node); };
    virtual void visitList(ListAst* node) { Q_UNUSED(node); };
    virtual void visitTuple(TupleAst* node) { Q_UNUSED(node); };
    virtual void visitEllipsis(EllipsisAst* node) { Q_UNUSED(node); };
    virtual void visitSlice(SliceAst* node) { Q_UNUSED(node); };
    virtual void visitArguments(ArgumentsAst* node) { Q_UNUSED(node); };
    virtual void visitKeyword(KeywordAst* node) { Q_UNUSED(node); };
    virtual void visitArg(ArgAst* node) { Q_UNUSED(node); };
    virtual void visitComprehension(ComprehensionAst* node) { Q_UNUSED(node); };
    virtual void visitExceptionHandler(ExceptionHandlerAst* node) { Q_UNUSED(node); };
    virtual void visitAlias(AliasAst* node) { Q_UNUSED(node); };
    virtual void visitWithItem(WithItemAst* node) { Q_UNUSED(node); };
    virtual void visitMatch(MatchAst* node) { Q_UNUSED(node); };
    virtual void visitMatchCase(MatchCaseAst* node) { Q_UNUSED(node); };
    virtual void visitMatchValue(MatchValueAst* node) { Q_UNUSED(node); };
    virtual void visitMatchSingleton(MatchSingletonAst* node) { Q_UNUSED(node); };
    virtual void visitMatchSequence(MatchSequenceAst* node) { Q_UNUSED(node); };
    virtual void visitMatchMapping(MatchMappingAst* node) { Q_UNUSED(node); };
    virtual void visitMatchClass(MatchClassAst* node) { Q_UNUSED(node); };
    virtual void visitMatchStar(MatchStarAst* node) { Q_UNUSED(node); };
    virtual void visitMatchAs(MatchAsAst* node) { Q_UNUSED(node); };
    virtual void visitMatchOr(MatchOrAst* node) { Q_UNUSED(node); };

};
}

#endif
