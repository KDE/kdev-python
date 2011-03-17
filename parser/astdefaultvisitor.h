/***************************************************************************
 *   This file is part of KDevelop                                         *
 *   Copyright 2007 Andreas Pakulat <apaku@gmx.de>                         *
 *   Copyright 2010-2011 Sven Brauch <svenbrauch@googlemail.com>           *
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
    virtual void visitDelete(DeleteAst* node);
    virtual void visitAssignment(AssignmentAst* node);
    virtual void visitAugmentedAssignment(AugmentedAssignmentAst* node);
    virtual void visitFor(ForAst* node);
    virtual void visitWhile(WhileAst* node);
    virtual void visitIf(IfAst* node);
    virtual void visitWith(WithAst* node);
    virtual void visitRaise(RaiseAst* node);
    virtual void visitTryExcept(TryExceptAst* node);
    virtual void visitTryFinally(TryFinallyAst* node);
    virtual void visitAssertion(AssertionAst* node);
    virtual void visitImport(ImportAst* node);
    virtual void visitImportFrom(ImportFromAst* node);
    virtual void visitExec(ExecAst* node);
    virtual void visitGlobal(GlobalAst* node);
    virtual void visitBreak(BreakAst* node);
    virtual void visitContinue(ContinueAst* node);
    virtual void visitPrint(PrintAst* node);
    virtual void visitPass(PassAst* node);
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
    virtual void visitRepr(ReprAst* node);
    virtual void visitNumber(NumberAst* node);
    virtual void visitString(StringAst* node);
    virtual void visitYield(YieldAst* node);
    virtual void visitName(NameAst* node);
    virtual void visitCall(CallAst* node);
    virtual void visitAttribute(AttributeAst* node);
    virtual void visitSubscript(SubscriptAst* node);
    virtual void visitList(ListAst* node);
    virtual void visitTuple(TupleAst* node);
    virtual void visitEllipsis(EllipsisAst* node);
    virtual void visitSlice(SliceAst* node);
    virtual void visitExtendedSlice(ExtendedSliceAst* node);
    virtual void visitIndex(IndexAst* node);
    virtual void visitArguments(ArgumentsAst* node);
    virtual void visitKeyword(KeywordAst* node);
    virtual void visitComprehension(ComprehensionAst* node);
    virtual void visitExceptionHandler(ExceptionHandlerAst* node);
    virtual void visitAlias(AliasAst* node);
    virtual void visitExpression(ExpressionAst* node);
};

}

#endif
