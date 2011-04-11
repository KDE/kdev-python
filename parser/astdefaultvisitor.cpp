/***************************************************************************
 *   This file is part of KDevelop                                         *
 *   Copyright 2007 Andreas Pakulat <apaku@gmx.de>                         *
 * Copyright 2010 Sven Brauch <svenbrauch@googlemail.com>                  *
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
#include <kdebug.h>

namespace Python
{

AstDefaultVisitor::AstDefaultVisitor() { }
AstDefaultVisitor::~AstDefaultVisitor() { }

// The Ast "ends" here, those dont have child nodes
// note that Identifier is not a node in this Ast
void AstDefaultVisitor::visitName(NameAst* node) { Q_UNUSED(node); }
void AstDefaultVisitor::visitPass(PassAst* node) { Q_UNUSED(node); }
void AstDefaultVisitor::visitAlias(AliasAst* node) { Q_UNUSED(node); }
void AstDefaultVisitor::visitBreak(BreakAst* node) { Q_UNUSED(node); }
void AstDefaultVisitor::visitContinue(ContinueAst* node) { Q_UNUSED(node); }
void AstDefaultVisitor::visitEllipsis(EllipsisAst* node) { Q_UNUSED(node); }
void AstDefaultVisitor::visitGlobal(GlobalAst* node) { Q_UNUSED(node); }
void AstDefaultVisitor::visitNumber(NumberAst* node) { Q_UNUSED(node); }
void AstDefaultVisitor::visitString(StringAst* node) { Q_UNUSED(node); }

void AstDefaultVisitor::visitCode(CodeAst* node)
{
    kDebug() << "Visiting code:" << node;
    kDebug() << node->body;
    foreach (Ast* statement, node->body) {
        visitNode(statement);
    }
}

void AstDefaultVisitor::visitExpression(ExpressionAst* node)
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
    foreach (ExpressionAst* expression, node->targets) {
        visitNode(expression);
    }
}

void AstDefaultVisitor::visitExec(ExecAst* node)
{
    visitNode(node->body);
    visitNode(node->globals);
    visitNode(node->locals);
}

void AstDefaultVisitor::visitExtendedSlice(ExtendedSliceAst* node)
{
    foreach (SliceAst* slice, node->dims) {
        visitNode(slice);
    }
}

void AstDefaultVisitor::visitFor(ForAst* node)
{
    visitNode(node->target);
    visitNode(node->iterator);
    foreach (Ast* statement, node->body) {
        visitNode(statement);
    }
    foreach (Ast* statement, node->orelse) {
        visitNode(statement);
    }
}

void AstDefaultVisitor::visitGeneratorExpression(GeneratorExpressionAst* node)
{
    visitNode(node->element);
    foreach (ComprehensionAst* comp, node->generators) {
        visitNode(comp);
    }
}

void AstDefaultVisitor::visitIf(IfAst* node)
{
    visitNode(node->condition);
    foreach (Ast* statement, node->body) {
        visitNode(statement);
    }
    foreach (Ast* statement, node->orelse) {
        visitNode(statement);
    }
}

void AstDefaultVisitor::visitIfExpression(IfExpressionAst* node)
{
    visitNode(node->condition);
    visitNode(node->body);
    visitNode(node->orelse);
}

void AstDefaultVisitor::visitImport(ImportAst* node)
{
    foreach (AliasAst* alias, node->names) {
        visitNode(alias);
    }
}

void AstDefaultVisitor::visitImportFrom(ImportFromAst* node)
{
    foreach (AliasAst* alias, node->names) {
        visitNode(alias);
    }
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

void AstDefaultVisitor::visitRepr(ReprAst* node)
{
    visitNode(node->value);
}

void AstDefaultVisitor::visitReturn(ReturnAst* node)
{
    visitNode(node->value);
}

void AstDefaultVisitor::visitSet(SetAst* node)
{
    foreach (ExpressionAst* expression, node->elements) {
        visitNode(expression);
    }
}

void AstDefaultVisitor::visitSetComprehension(SetComprehensionAst* node)
{
    visitNode(node->element);
    foreach (ComprehensionAst* comp, node->generators) {
        visitNode(comp);
    }
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

void AstDefaultVisitor::visitTryExcept(TryExceptAst* node)
{
    foreach (Ast* statement, node->body) {
        visitNode(statement);
    }
    foreach (ExceptionHandlerAst* handler, node->handlers) {
        visitNode(handler);
    }
    foreach (Ast* statement, node->orelse) {
        visitNode(statement);
    }
}

void AstDefaultVisitor::visitTryFinally(TryFinallyAst* node)
{
    foreach (Ast* statement, node->body) {
        visitNode(statement);
    }
    foreach (Ast* statement, node->finalbody) {
        visitNode(statement);
    }
}

void AstDefaultVisitor::visitTuple(TupleAst* node)
{
    foreach (ExpressionAst* expression, node->elements) {
        visitNode(expression);
    }
}

void AstDefaultVisitor::visitUnaryOperation(UnaryOperationAst* node)
{
    visitNode(node->operand);
}

void AstDefaultVisitor::visitWhile(WhileAst* node)
{
    visitNode(node->condition);
    foreach (Ast* statement, node->body) {
        visitNode(statement);
    }
    foreach (Ast* statement, node->orelse) {
        visitNode(statement);
    }
}

void AstDefaultVisitor::visitWith(WithAst* node)
{
    visitNode(node->contextExpression);
    visitNode(node->optionalVars);
    foreach (Ast* statement, node->body) {
        visitNode(statement);
    }
}

void AstDefaultVisitor::visitYield(YieldAst* node)
{
    visitNode(node->value);
}

void AstDefaultVisitor::visitList(ListAst* node)
{
    foreach (ExpressionAst* expression, node->elements) {
        visitNode(expression);
    }
}

void AstDefaultVisitor::visitListComprehension(ListComprehensionAst* node)
{
    visitNode(node->element);
    foreach (ComprehensionAst* comp, node->generators) {
        visitNode(comp);
    }
}

void AstDefaultVisitor::visitExceptionHandler(ExceptionHandlerAst* node)
{
    visitNode(node->type);
    visitNode(node->name);
    foreach (Ast* statement, node->body) {
        visitNode(statement);
    }
}

void AstDefaultVisitor::visitDict(DictAst* node)
{
    foreach (ExpressionAst* expression, node->keys) {
        visitNode(expression);
    }
    foreach (ExpressionAst* expression, node->values) {
        visitNode(expression);
    }
}

void AstDefaultVisitor::visitDictionaryComprehension(DictionaryComprehensionAst* node)
{
    visitNode(node->key);
    visitNode(node->value);
    foreach (ComprehensionAst* comp, node->generators) {
        visitNode(comp);
    }
}

void AstDefaultVisitor::visitAugmentedAssignment(AugmentedAssignmentAst* node)
{
    visitNode(node->target);
    visitNode(node->value);
}

void AstDefaultVisitor::visitBinaryOperation(BinaryOperationAst* node)
{
    visitNode(node->lhs);
    visitNode(node->rhs);
}

void AstDefaultVisitor::visitBooleanOperation(BooleanOperationAst* node)
{
    foreach (ExpressionAst* expression, node->values) {
        visitNode(expression);
    }
}

void AstDefaultVisitor::visitClassDefinition(ClassDefinitionAst* node)
{
    foreach (ExpressionAst* expression, node->baseClasses) {
        visitNode(expression);
    }
    foreach (Ast* statement, node->body) {
        visitNode(statement);
    }
    foreach (ExpressionAst* expression, node->decorators) {
        visitNode(expression);
    }
}

void AstDefaultVisitor::visitCompare(CompareAst* node)
{
    visitNode(node->leftmostElement);
    foreach (ExpressionAst* expression, node->comparands) {
        visitNode(expression);
    }
}

void AstDefaultVisitor::visitComprehension(ComprehensionAst* node)
{
    visitNode(node->target);
    visitNode(node->iterator);
    foreach (ExpressionAst* expression, node->conditions) {
        visitNode(expression);
    }
}

void AstDefaultVisitor::visitAssignment(AssignmentAst* node)
{
    foreach (ExpressionAst* expression, node->targets) {
        visitNode(expression);
    };
    visitNode(node->value);
}

void AstDefaultVisitor::visitPrint(PrintAst* node)
{
    visitNode(node->destination);
    foreach (ExpressionAst* expression, node->values) {
        visitNode(expression);
    }
}

void AstDefaultVisitor::visitCall(CallAst* node)
{
    visitNode(node->function);
    visitNode(node->keywordArguments);
    visitNode(node->starArguments);
    foreach (ExpressionAst* argument, node->arguments) {
        visitNode(argument);
    }
}

void AstDefaultVisitor::visitFunctionDefinition(FunctionDefinitionAst* node)
{
    foreach (NameAst* decorator, node->decorators) {
        visitNode(decorator);
    }
    visitNode(node->arguments);
    foreach (Ast* stmt, node->body) {
        visitNode(stmt);
    }
}

void AstDefaultVisitor::visitAttribute(AttributeAst* node)
{
    visitNode(node->value);
}

void AstDefaultVisitor::visitKeyword(KeywordAst* node)
{
    visitNode(node->value);
}

void AstDefaultVisitor::visitArguments(ArgumentsAst* node)
{
    foreach (ExpressionAst* expression, node->arguments) {
        visitNode(expression);
    }
}

}

