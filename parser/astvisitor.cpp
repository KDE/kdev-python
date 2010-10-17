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

#include "astvisitor.h"

/**
 * Note: This has been generated using utilities/generate.py
 * but you can modifiy it, it's not regenerated automatically
 */

namespace Python
{
    
AstVisitor::AstVisitor() { }
AstVisitor::~AstVisitor() { }


void AstVisitor::visitNode(Ast* node)
{
    if ( ! node ) return;
    switch ( node->astType ) {
        case Ast::CodeAstType:                                  AstVisitor::visitCode(dynamic_cast<CodeAst>(node)); break;                    
        case Ast::FunctionDefinitionAstType:                    AstVisitor::visitFunctionDefinition(dynamic_cast<FunctionDefinitionAst>(node)); break;
        case Ast::ClassDefinitionAstType:                       AstVisitor::visitClassDefinition(dynamic_cast<ClassDefinitionAst>(node)); break;
        case Ast::ReturnAstType:                                AstVisitor::visitReturn(dynamic_cast<ReturnAst>(node)); break;
        case Ast::DeleteAstType:                                AstVisitor::visitDelete(dynamic_cast<DeleteAst>(node)); break;                      
        case Ast::AssignmentAstType:                            AstVisitor::visitAssignment(dynamic_cast<AssignmentAst>(node)); break;
        case Ast::AugmentedAssignmentAstType:                   AstVisitor::visitAugmentedAssignment(dynamic_cast<AugmentedAssignmentAst>(node)); break;
        case Ast::ForAstType:                                   AstVisitor::visitFor(dynamic_cast<ForAst>(node)); break;
        case Ast::WhileAstType:                                 AstVisitor::visitWhile(dynamic_cast<WhileAst>(node)); break;
        case Ast::IfAstType:                                    AstVisitor::visitIf(dynamic_cast<IfAst>(node)); break;
        case Ast::WithAstType:                                  AstVisitor::visitWith(dynamic_cast<WithAst>(node)); break;
        case Ast::RaiseAstType:                                 AstVisitor::visitRaise(dynamic_cast<RaiseAst>(node)); break;
        case Ast::TryExceptAstType:                             AstVisitor::visitTryExcept(dynamic_cast<TryExceptAst>(node)); break;
        case Ast::TryFinallyAstType:                            AstVisitor::visitTryFinally(dynamic_cast<TryFinallyAst>(node)); break;
        case Ast::AssertionAstType:                             AstVisitor::visitAssertion(dynamic_cast<AssertionAst>(node)); break;
        case Ast::ImportAstType:                                AstVisitor::visitImport(dynamic_cast<ImportAst>(node)); break;
        case Ast::ImportFromAstType:                            AstVisitor::visitImportFrom(dynamic_cast<ImportFromAst>(node)); break;
        case Ast::ExecAstType:                                  AstVisitor::visitExec(dynamic_cast<ExecAst>(node)); break;
        case Ast::GlobalAstType:                                AstVisitor::visitGlobal(dynamic_cast<GlobalAst>(node)); break;
        case Ast::BreakAstType:                                 AstVisitor::visitBreak(dynamic_cast<BreakAst>(node)); break;
        case Ast::ContinueAstType:                              AstVisitor::visitContinue(dynamic_cast<ContinueAst>(node)); break;
        case Ast::PrintAstType:                                 AstVisitor::visitPrint(dynamic_cast<PrintAst>(node)); break;
        case Ast::PassAstType:                                  AstVisitor::visitPass(dynamic_cast<PassAst>(node)); break;
        case Ast::BooleanOperationAstType:                      AstVisitor::visitBooleanOperation(dynamic_cast<BooleanOperationAst>(node)); break;
        case Ast::BinaryOperationAstType:                       AstVisitor::visitBinaryOperation(dynamic_cast<BinaryOperationAst>(node)); break;
        case Ast::UnaryOperationAstType:                        AstVisitor::visitUnaryOperation(dynamic_cast<UnaryOperationAst>(node)); break;
        case Ast::LambdaAstType:                                AstVisitor::visitLambda(dynamic_cast<LambdaAst>(node)); break;
        case Ast::IfExpressionAstType:                          AstVisitor::visitIfExpression(dynamic_cast<IfExpressionAst>(node)); break;
        case Ast::DictAstType:                                  AstVisitor::visitDict(dynamic_cast<DictAst>(node)); break;
        case Ast::SetAstType:                                   AstVisitor::visitSet(dynamic_cast<SetAst>(node)); break;
        case Ast::ListComprehensionAstType:                     AstVisitor::visitListComprehension(dynamic_cast<ListComprehensionAst>(node)); break;
        case Ast::SetComprehensionAstType:                      AstVisitor::visitSetComprehension(dynamic_cast<SetComprehensionAst>(node)); break;
        case Ast::DictionaryComprehensionAstType:               AstVisitor::visitDictionaryComprehension(dynamic_cast<DictionaryComprehensionAst>(node)); break;
        case Ast::GeneratorExpressionAstType:                   AstVisitor::visitGeneratorExpression(dynamic_cast<GeneratorExpressionAst>(node)); break;
        case Ast::CompareAstType:                               AstVisitor::visitCompare(dynamic_cast<CompareAst>(node)); break;
        case Ast::ReprAstType:                                  AstVisitor::visitRepr(dynamic_cast<ReprAst>(node)); break;
        case Ast::NumberAstType:                                AstVisitor::visitNumber(dynamic_cast<NumberAst>(node)); break;
        case Ast::StringAstType:                                AstVisitor::visitString(dynamic_cast<StringAst>(node)); break;
        case Ast::YieldAstType:                                 AstVisitor::visitYield(dynamic_cast<YieldAst>(node)); break;
        case Ast::NameAstType:                                  AstVisitor::visitName(dynamic_cast<NameAst>(node)); break;
        case Ast::CallAstType:                                  AstVisitor::visitCall(dynamic_cast<CallAst>(node)); break;
        case Ast::AttributeAstType:                             AstVisitor::visitAttribute(dynamic_cast<AttributeAst>(node)); break;
        case Ast::SubscriptAstType:                             AstVisitor::visitSubscript(dynamic_cast<SubscriptAst>(node)); break;
        case Ast::ListAstType:                                  AstVisitor::visitList(dynamic_cast<ListAst>(node)); break;
        case Ast::TupleAstType:                                 AstVisitor::visitTuple(dynamic_cast<TupleAst>(node)); break;
        case Ast::SliceAstType:                                 AstVisitor::visitSlice(dynamic_cast<SliceAst>(node)); break;
        case Ast::EllipsisAstType:                              AstVisitor::visitEllipsis(dynamic_cast<EllipsisAst>(node)); break;
        case Ast::SliceAstType:                                 AstVisitor::visitSlice(dynamic_cast<SliceAst>(node)); break;
        case Ast::ExtendedSliceAstType:                         AstVisitor::visitExtendedSlice(dynamic_cast<ExtendedSliceAst>(node)); break;
        case Ast::IndexAstType:                                 AstVisitor::visitIndex(dynamic_cast<IndexAst>(node)); break;
        case Ast::ArgumentsAstType:                             AstVisitor::visitArguments(dynamic_cast<ArgumentsAst>(node)); break;
        case Ast::KeywordAstType:                               AstVisitor::visitKeyword(dynamic_cast<KeywordAst>(node)); break;
        case Ast::ComprehensionAstType:                         AstVisitor::visitComprehension(dynamic_cast<ComprehensionAst>(node)); break;
        case Ast::ExceptionHandlerAstType:                      AstVisitor::visitExceptionHandler(dynamic_cast<ExceptionHandlerAst>(node)); break;
        case Ast::AliasAstType:                                 AstVisitor::visitAlias(dynamic_cast<AliasAst>(node)); break;
        case Ast::ExpressionAstType:                            break;
    }
}

}
