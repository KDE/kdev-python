/***************************************************************************
 *   This file is part of KDevelop                                         *
 *   Copyright 2007 Andreas Pakulat <apaku@gmx.de>                         *
 *   Copyright 2012 Patrick Spendrin <ps_ml@gmx.de>                        *
 *   Copyright 2010-2014 Sven Brauch <svenbrauch@googlemail.com>           *
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
    virtual ~AstDefaultVisitor();

    virtual void visitCode(CodeAst* node);
    virtual void visitFunctionDefinition(FunctionDefinitionAst* node);
    virtual void visitClassDefinition(ClassDefinitionAst* node);
    virtual void visitReturn(ReturnAst* node);
    virtual void visitAwait(AwaitAst* node);
    virtual void visitDelete(DeleteAst* node);
    virtual void visitAssignment(AssignmentAst* node);
    virtual void visitAugmentedAssignment(AugmentedAssignmentAst* node);
    virtual void visitAnnotationAssignment(AnnotationAssignmentAst* node);
    virtual void visitFor(ForAst* node);
    virtual void visitWhile(WhileAst* node);
    virtual void visitIf(IfAst* node);
    virtual void visitWith(WithAst* node);
    virtual void visitRaise(RaiseAst* node);
    virtual void visitTry(TryAst* node);
    virtual void visitAssertion(AssertionAst* node);
    virtual void visitImport(ImportAst* node);
    virtual void visitImportFrom(ImportFromAst* node);
    virtual void visitGlobal(GlobalAst* node);
    virtual void visitBreak(BreakAst* node);
    virtual void visitContinue(ContinueAst* node);
    virtual void visitPass(PassAst* node);
    virtual void visitNonlocal(NonlocalAst* node);
    virtual void visitBooleanOperation(BooleanOperationAst* node);
    virtual void visitBinaryOperation(BinaryOperationAst* node);
    virtual void visitUnaryOperation(UnaryOperationAst* node);
    virtual void visitLambda(LambdaAst* node);
    virtual void visitIfExpression(IfExpressionAst* node);
    virtual void visitDict(DictAst* node);
    virtual void visitSet(SetAst* node);
    virtual void visitListComprehension(ListComprehensionAst* node);
    virtual void visitSetComprehension(SetComprehensionAst* node);
    virtual void visitDictionaryComprehension(DictionaryComprehensionAst* node);
    virtual void visitGeneratorExpression(GeneratorExpressionAst* node);
    virtual void visitCompare(CompareAst* node);
    virtual void visitNumber(NumberAst* node);
    virtual void visitString(StringAst* node);
    virtual void visitJoinedString(JoinedStringAst* node);
    virtual void visitFormattedValue(FormattedValueAst* node);
    virtual void visitBytes(BytesAst* node);
    virtual void visitYield(YieldAst* node);
    virtual void visitYieldFrom(YieldFromAst* node);
    virtual void visitName(NameAst* node);
    virtual void visitNameConstant(NameConstantAst* node);
    virtual void visitCall(CallAst* node);
    virtual void visitAttribute(AttributeAst* node);
    virtual void visitSubscript(SubscriptAst* node);
    virtual void visitStarred(StarredAst* node);
    virtual void visitList(ListAst* node);
    virtual void visitTuple(TupleAst* node);
    virtual void visitEllipsis(EllipsisAst* node);
    virtual void visitSlice(SliceAst* node);
    virtual void visitExtendedSlice(ExtendedSliceAst* node);
    virtual void visitIndex(IndexAst* node);
    virtual void visitArguments(ArgumentsAst* node);
    virtual void visitArg(ArgAst* node);
    virtual void visitKeyword(KeywordAst* node);
    virtual void visitComprehension(ComprehensionAst* node);
    virtual void visitExceptionHandler(ExceptionHandlerAst* node);
    virtual void visitAlias(AliasAst* node);
    virtual void visitExpression(ExpressionAst* node);
    virtual void visitWithItem(WithItemAst* node);
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
    virtual void visitCode(CodeAst* node) { AstDefaultVisitor::visitCode(node); }
    virtual void visitFunctionDefinition(FunctionDefinitionAst* node) { AstDefaultVisitor::visitFunctionDefinition(node); delete node; }
    virtual void visitClassDefinition(ClassDefinitionAst* node) { AstDefaultVisitor::visitClassDefinition(node); delete node; }
    virtual void visitReturn(ReturnAst* node) { AstDefaultVisitor::visitReturn(node); delete node; }
    virtual void visitDelete(DeleteAst* node) { AstDefaultVisitor::visitDelete(node); delete node; }
    virtual void visitAssignment(AssignmentAst* node) { AstDefaultVisitor::visitAssignment(node); delete node; }
    virtual void visitAugmentedAssignment(AugmentedAssignmentAst* node) { AstDefaultVisitor::visitAugmentedAssignment(node); delete node; }
    virtual void visitAnnotationAssignment(AnnotationAssignmentAst* node) { AstDefaultVisitor::visitAnnotationAssignment(node); delete node; }
    virtual void visitFor(ForAst* node) { AstDefaultVisitor::visitFor(node); delete node; }
    virtual void visitWhile(WhileAst* node) { AstDefaultVisitor::visitWhile(node); delete node; }
    virtual void visitIf(IfAst* node) { AstDefaultVisitor::visitIf(node); delete node; }
    virtual void visitWith(WithAst* node) { AstDefaultVisitor::visitWith(node); delete node; }
    virtual void visitRaise(RaiseAst* node) { AstDefaultVisitor::visitRaise(node); delete node; }
    virtual void visitTry(TryAst* node) { AstDefaultVisitor::visitTry(node); delete node; }
    virtual void visitAssertion(AssertionAst* node) { AstDefaultVisitor::visitAssertion(node); delete node; }
    virtual void visitImport(ImportAst* node) { AstDefaultVisitor::visitImport(node); delete node; }
    virtual void visitImportFrom(ImportFromAst* node) { AstDefaultVisitor::visitImportFrom(node); delete node; }
    virtual void visitGlobal(GlobalAst* node) { AstDefaultVisitor::visitGlobal(node); delete node; }
    virtual void visitBreak(BreakAst* node) { AstDefaultVisitor::visitBreak(node); delete node; }
    virtual void visitContinue(ContinueAst* node) { AstDefaultVisitor::visitContinue(node); delete node; }
    virtual void visitPass(PassAst* node) { AstDefaultVisitor::visitPass(node); delete node; }
    virtual void visitNonlocal(NonlocalAst* node) { AstDefaultVisitor::visitNonlocal(node); delete node; }
    virtual void visitBooleanOperation(BooleanOperationAst* node) { AstDefaultVisitor::visitBooleanOperation(node); delete node; }
    virtual void visitBinaryOperation(BinaryOperationAst* node) { AstDefaultVisitor::visitBinaryOperation(node); delete node; }
    virtual void visitUnaryOperation(UnaryOperationAst* node) { AstDefaultVisitor::visitUnaryOperation(node); delete node; }
    virtual void visitLambda(LambdaAst* node) { AstDefaultVisitor::visitLambda(node); delete node; }
    virtual void visitIfExpression(IfExpressionAst* node) { AstDefaultVisitor::visitIfExpression(node); delete node; }
    virtual void visitDict(DictAst* node) { AstDefaultVisitor::visitDict(node); delete node; }
    virtual void visitSet(SetAst* node) { AstDefaultVisitor::visitSet(node); delete node; }
    virtual void visitListComprehension(ListComprehensionAst* node) { AstDefaultVisitor::visitListComprehension(node); delete node; }
    virtual void visitSetComprehension(SetComprehensionAst* node) { AstDefaultVisitor::visitSetComprehension(node); delete node; }
    virtual void visitDictionaryComprehension(DictionaryComprehensionAst* node) { AstDefaultVisitor::visitDictionaryComprehension(node); delete node; }
    virtual void visitGeneratorExpression(GeneratorExpressionAst* node) { AstDefaultVisitor::visitGeneratorExpression(node); delete node; }
    virtual void visitCompare(CompareAst* node) { AstDefaultVisitor::visitCompare(node); delete node; }
    virtual void visitNumber(NumberAst* node) { AstDefaultVisitor::visitNumber(node); delete node; }
    virtual void visitString(StringAst* node) { AstDefaultVisitor::visitString(node); delete node; }
    virtual void visitJoinedString(JoinedStringAst* node) { AstDefaultVisitor::visitJoinedString(node); delete node; }
    virtual void visitFormattedValue(FormattedValueAst* node) { AstDefaultVisitor::visitFormattedValue(node); delete node; }
    virtual void visitBytes(BytesAst* node) { AstDefaultVisitor::visitBytes(node); delete node; }
    virtual void visitYield(YieldAst* node) { AstDefaultVisitor::visitYield(node); delete node; }
    virtual void visitYieldFrom(YieldFromAst* node) { AstDefaultVisitor::visitYieldFrom(node); delete node; }
    virtual void visitName(NameAst* node) { AstDefaultVisitor::visitName(node); delete node; }
    virtual void visitNameConstant(NameConstantAst* node) { AstDefaultVisitor::visitNameConstant(node); delete node; }
    virtual void visitCall(CallAst* node) { AstDefaultVisitor::visitCall(node); delete node; }
    virtual void visitAttribute(AttributeAst* node) { AstDefaultVisitor::visitAttribute(node); delete node; }
    virtual void visitSubscript(SubscriptAst* node) { AstDefaultVisitor::visitSubscript(node); delete node; }
    virtual void visitStarred(StarredAst* node) { AstDefaultVisitor::visitStarred(node); delete node; }
    virtual void visitList(ListAst* node) { AstDefaultVisitor::visitList(node); delete node; }
    virtual void visitTuple(TupleAst* node) { AstDefaultVisitor::visitTuple(node); delete node; }
    virtual void visitEllipsis(EllipsisAst* node) { AstDefaultVisitor::visitEllipsis(node); delete node; }
    virtual void visitSlice(SliceAst* node) { AstDefaultVisitor::visitSlice(node); delete node; }
    virtual void visitExtendedSlice(ExtendedSliceAst* node) { AstDefaultVisitor::visitExtendedSlice(node); delete node; }
    virtual void visitIndex(IndexAst* node) { AstDefaultVisitor::visitIndex(node); delete node; }
    virtual void visitArguments(ArgumentsAst* node) { AstDefaultVisitor::visitArguments(node); delete node; }
    virtual void visitArg(ArgAst* node) { AstDefaultVisitor::visitArg(node); delete node; }
    virtual void visitKeyword(KeywordAst* node) { AstDefaultVisitor::visitKeyword(node); delete node; }
    virtual void visitComprehension(ComprehensionAst* node) { AstDefaultVisitor::visitComprehension(node); delete node; }
    virtual void visitExceptionHandler(ExceptionHandlerAst* node) { AstDefaultVisitor::visitExceptionHandler(node); delete node; }
    virtual void visitAlias(AliasAst* node) { AstDefaultVisitor::visitAlias(node); delete node; }
    virtual void visitExpression(ExpressionAst* node) { AstDefaultVisitor::visitExpression(node); delete node; }
    virtual void visitWithItem(WithItemAst* node) { AstDefaultVisitor::visitWithItem(node); delete node; }
    virtual void visitIdentifier(Identifier* node) { AstDefaultVisitor::visitIdentifier(node); delete node; }
};

KDEVPYTHONPARSER_EXPORT void free_ast_recursive(CodeAst* node);

}

#endif
