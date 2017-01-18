/***************************************************************************
 *   This file is part of KDevelop                                         *
 *   Copyright 2007 Andreas Pakulat <apaku@gmx.de>                         *
 * Copyright 2010 Sven Brauch <svenbrauch@googlemail.com>                  *
 *   Copyright 2012 Patrick Spendrin <ps_ml@gmx.de>                        *
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

#include "astdefaultvisitor.h"
#include "ast.h"

namespace Python
{

void free_ast_recursive(CodeAst *node)
{
    AstFreeVisitor v;
    v.visitCode(node);
}

AstDefaultVisitor::AstDefaultVisitor() { }
AstDefaultVisitor::~AstDefaultVisitor() { }

// The Ast "ends" here, those dont have child nodes
// note that Identifier is not a node in this Ast
void AstDefaultVisitor::visitNameConstant(NameConstantAst* node) { Q_UNUSED(node); }
void AstDefaultVisitor::visitPass(PassAst* node) { Q_UNUSED(node); }
void AstDefaultVisitor::visitNonlocal(NonlocalAst* node) { Q_UNUSED(node); }
void AstDefaultVisitor::visitBreak(BreakAst* node) { Q_UNUSED(node); }
void AstDefaultVisitor::visitContinue(ContinueAst* node) { Q_UNUSED(node); }
void AstDefaultVisitor::visitEllipsis(EllipsisAst* node) { Q_UNUSED(node); }
void AstDefaultVisitor::visitNumber(NumberAst* node) { Q_UNUSED(node); }
void AstDefaultVisitor::visitString(StringAst* node) { Q_UNUSED(node); }
void AstDefaultVisitor::visitBytes(BytesAst* node) { Q_UNUSED(node); }
void AstDefaultVisitor::visitIdentifier(Identifier* node) { Q_UNUSED(node); }

void AstDefaultVisitor::visitJoinedString(JoinedStringAst* node) {
//TODO: Fix range/context/??? bugs, then re-enable this.
    Q_UNUSED(node);
//     foreach (Ast* value, node->values) {
//         visitNode(value);
//     }
}

void AstDefaultVisitor::visitFormattedValue(FormattedValueAst* node) {
// TODO: Fix range issues, then re-enable (if required)
    Q_UNUSED(node);
//     visitNode(node->value);
//     visitNode(node->formatSpec);
}

void AstDefaultVisitor::visitStarred(StarredAst* node) {
    visitNode(node->value);
}

void AstDefaultVisitor::visitArg(ArgAst* node) {
    visitNode(node->annotation);
    visitNode(node->argumentName);
    visitIdentifier(node->argumentName);
}

void AstDefaultVisitor::visitAlias(AliasAst* node) {
    visitIdentifier(node->name);
    visitIdentifier(node->asName);
}

void AstDefaultVisitor::visitName(NameAst* node) {
    visitIdentifier(node->identifier);
}

void AstDefaultVisitor::visitGlobal(GlobalAst* node) {
    visitNodeList(node->names);
}

void AstDefaultVisitor::visitCode(CodeAst* node)
{
    visitNodeList(node->body);
    visitIdentifier(node->name);
}

void AstDefaultVisitor::visitExpression(ExpressionAst* node)
{
    visitNode(node->value);
}

void AstDefaultVisitor::visitYieldFrom(YieldFromAst* node)
{
    visitNode(node->value);
}

void AstDefaultVisitor::visitAssertion(AssertionAst* node)
{
    visitNode(node->condition);
    visitNode(node->message);
}

void AstDefaultVisitor::visitDelete(DeleteAst* node)
{
    visitNodeList(node->targets);
}

void AstDefaultVisitor::visitExtendedSlice(ExtendedSliceAst* node)
{
    visitNodeList(node->dims);
}

void AstDefaultVisitor::visitFor(ForAst* node)
{
    visitNode(node->target);
    visitNode(node->iterator);
    visitNodeList(node->body);
    visitNodeList(node->orelse);
}

void AstDefaultVisitor::visitGeneratorExpression(GeneratorExpressionAst* node)
{
    visitNode(node->element);
    visitNodeList(node->generators);
}

void AstDefaultVisitor::visitIf(IfAst* node)
{
    visitNode(node->condition);
    visitNodeList(node->body);
    visitNodeList(node->orelse);
}

void AstDefaultVisitor::visitIfExpression(IfExpressionAst* node)
{
    visitNode(node->condition);
    visitNode(node->body);
    visitNode(node->orelse);
}

void AstDefaultVisitor::visitImport(ImportAst* node)
{
    visitNodeList(node->names);
}

void AstDefaultVisitor::visitImportFrom(ImportFromAst* node)
{
    visitNodeList(node->names);
    visitIdentifier(node->module);
}

void AstDefaultVisitor::visitIndex(IndexAst* node)
{
    visitNode(node->value);
}

void AstDefaultVisitor::visitLambda(LambdaAst* node)
{
    visitNode(node->arguments);
    visitNode(node->body);
}

void AstDefaultVisitor::visitRaise(RaiseAst* node)
{
    visitNode(node->type);
}

void AstDefaultVisitor::visitReturn(ReturnAst* node)
{
    visitNode(node->value);
}

void AstDefaultVisitor::visitAwait(AwaitAst* node) {
    visitNode(node->value);
}

void AstDefaultVisitor::visitSet(SetAst* node)
{
    visitNodeList(node->elements);
}

void AstDefaultVisitor::visitSetComprehension(SetComprehensionAst* node)
{
    visitNode(node->element);
    visitNodeList(node->generators);
}

void AstDefaultVisitor::visitSlice(SliceAst* node)
{
    visitNode(node->lower);
    visitNode(node->upper);
    visitNode(node->step);
}

void AstDefaultVisitor::visitSubscript(SubscriptAst* node)
{
    visitNode(node->value);
    visitNode(node->slice);
}

void AstDefaultVisitor::visitTry(TryAst* node)
{
    visitNodeList(node->body);
    visitNodeList(node->handlers);
    visitNodeList(node->orelse);
    visitNodeList(node->finally);
}

void AstDefaultVisitor::visitTuple(TupleAst* node)
{
    visitNodeList(node->elements);
}

void AstDefaultVisitor::visitUnaryOperation(UnaryOperationAst* node)
{
    visitNode(node->operand);
}

void AstDefaultVisitor::visitWhile(WhileAst* node)
{
    visitNode(node->condition);
    visitNodeList(node->body);
    visitNodeList(node->orelse);
}

void AstDefaultVisitor::visitWith(WithAst* node)
{
    visitNodeList(node->items);
    visitNodeList(node->body);
}

void AstDefaultVisitor::visitWithItem(WithItemAst* node)
{
    visitNode(node->contextExpression);
    visitNode(node->optionalVars);
}

void AstDefaultVisitor::visitYield(YieldAst* node)
{
    visitNode(node->value);
}

void AstDefaultVisitor::visitList(ListAst* node)
{
    visitNodeList(node->elements);
}

void AstDefaultVisitor::visitListComprehension(ListComprehensionAst* node)
{
    visitNode(node->element);
    visitNodeList(node->generators);
}

void AstDefaultVisitor::visitExceptionHandler(ExceptionHandlerAst* node)
{
    visitNode(node->type);
    visitNode(node->name);
    visitNodeList(node->body);
}

void AstDefaultVisitor::visitDict(DictAst* node)
{
    visitNodeList(node->keys);
    visitNodeList(node->values);
}

void AstDefaultVisitor::visitDictionaryComprehension(DictionaryComprehensionAst* node)
{
    visitNode(node->key);
    visitNode(node->value);
    visitNodeList(node->generators);
}

void AstDefaultVisitor::visitAugmentedAssignment(AugmentedAssignmentAst* node)
{
    visitNode(node->target);
    visitNode(node->value);
}

void AstDefaultVisitor::visitAnnotationAssignment(AnnotationAssignmentAst* node)
{
    visitNode(node->target);
    visitNode(node->annotation);
    visitNode(node->value);
}

void AstDefaultVisitor::visitBinaryOperation(BinaryOperationAst* node)
{
    visitNode(node->lhs);
    visitNode(node->rhs);
}

void AstDefaultVisitor::visitBooleanOperation(BooleanOperationAst* node)
{
    visitNodeList(node->values);
}

void AstDefaultVisitor::visitClassDefinition(ClassDefinitionAst* node)
{
    visitNodeList(node->baseClasses);
    visitNodeList(node->body);
    visitNodeList(node->decorators);
    visitIdentifier(node->name);
}

void AstDefaultVisitor::visitCompare(CompareAst* node)
{
    visitNode(node->leftmostElement);
    visitNodeList(node->comparands);
}

void AstDefaultVisitor::visitComprehension(ComprehensionAst* node)
{
    visitNode(node->target);
    visitNode(node->iterator);
    visitNodeList(node->conditions);
}

void AstDefaultVisitor::visitAssignment(AssignmentAst* node)
{
    visitNodeList(node->targets);
    visitNode(node->value);
}

void AstDefaultVisitor::visitCall(CallAst* node)
{
    visitNode(node->function);
    visitNodeList(node->arguments);
    visitNodeList(node->keywords);
}

void AstDefaultVisitor::visitFunctionDefinition(FunctionDefinitionAst* node)
{
    visitNodeList(node->decorators);
    visitNode(node->arguments);
    visitNode(node->returns);
    visitNodeList(node->body);
    visitIdentifier(node->name);
}

void AstDefaultVisitor::visitAttribute(AttributeAst* node)
{
    visitNode(node->value);
    visitIdentifier(node->attribute);
}

void AstDefaultVisitor::visitKeyword(KeywordAst* node)
{
    visitNode(node->value);
    visitIdentifier(node->argumentName);
}

void AstDefaultVisitor::visitArguments(ArgumentsAst* node)
{
    visitNodeList(node->arguments);
    visitNodeList(node->defaultValues);
}

}

