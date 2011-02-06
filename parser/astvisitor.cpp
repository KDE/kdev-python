/***************************************************************************
 *   This file is part of KDevelop                                         *
 *   Copyright 2007 Andreas Pakulat <apaku@gmx.de>                         *
 *   Copyright 2011 Sven Brauch <svenbrauch@googlemail.com>                *
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
        case Ast::CodeAstType:                                  this->visitCode(dynamic_cast<CodeAst*>(node)); break;                    
        case Ast::FunctionDefinitionAstType:                    this->visitFunctionDefinition(dynamic_cast<FunctionDefinitionAst*>(node)); break;
        case Ast::ClassDefinitionAstType:                       this->visitClassDefinition(dynamic_cast<ClassDefinitionAst*>(node)); break;
        case Ast::ReturnAstType:                                this->visitReturn(dynamic_cast<ReturnAst*>(node)); break;
        case Ast::DeleteAstType:                                this->visitDelete(dynamic_cast<DeleteAst*>(node)); break;                      
        case Ast::AssignmentAstType:                            this->visitAssignment(dynamic_cast<AssignmentAst*>(node)); break;
        case Ast::AugmentedAssignmentAstType:                   this->visitAugmentedAssignment(dynamic_cast<AugmentedAssignmentAst*>(node)); break;
        case Ast::ForAstType:                                   this->visitFor(dynamic_cast<ForAst*>(node)); break;
        case Ast::WhileAstType:                                 this->visitWhile(dynamic_cast<WhileAst*>(node)); break;
        case Ast::IfAstType:                                    this->visitIf(dynamic_cast<IfAst*>(node)); break;
        case Ast::WithAstType:                                  this->visitWith(dynamic_cast<WithAst*>(node)); break;
        case Ast::RaiseAstType:                                 this->visitRaise(dynamic_cast<RaiseAst*>(node)); break;
        case Ast::TryExceptAstType:                             this->visitTryExcept(dynamic_cast<TryExceptAst*>(node)); break;
        case Ast::TryFinallyAstType:                            this->visitTryFinally(dynamic_cast<TryFinallyAst*>(node)); break;
        case Ast::AssertionAstType:                             this->visitAssertion(dynamic_cast<AssertionAst*>(node)); break;
        case Ast::ImportAstType:                                this->visitImport(dynamic_cast<ImportAst*>(node)); break;
        case Ast::ImportFromAstType:                            this->visitImportFrom(dynamic_cast<ImportFromAst*>(node)); break;
        case Ast::ExecAstType:                                  this->visitExec(dynamic_cast<ExecAst*>(node)); break;
        case Ast::GlobalAstType:                                this->visitGlobal(dynamic_cast<GlobalAst*>(node)); break;
        case Ast::BreakAstType:                                 this->visitBreak(dynamic_cast<BreakAst*>(node)); break;
        case Ast::ContinueAstType:                              this->visitContinue(dynamic_cast<ContinueAst*>(node)); break;
        case Ast::PrintAstType:                                 this->visitPrint(dynamic_cast<PrintAst*>(node)); break;
        case Ast::PassAstType:                                  this->visitPass(dynamic_cast<PassAst*>(node)); break;
        case Ast::BooleanOperationAstType:                      this->visitBooleanOperation(dynamic_cast<BooleanOperationAst*>(node)); break;
        case Ast::BinaryOperationAstType:                       this->visitBinaryOperation(dynamic_cast<BinaryOperationAst*>(node)); break;
        case Ast::UnaryOperationAstType:                        this->visitUnaryOperation(dynamic_cast<UnaryOperationAst*>(node)); break;
        case Ast::LambdaAstType:                                this->visitLambda(dynamic_cast<LambdaAst*>(node)); break;
        case Ast::IfExpressionAstType:                          this->visitIfExpression(dynamic_cast<IfExpressionAst*>(node)); break;
        case Ast::DictAstType:                                  this->visitDict(dynamic_cast<DictAst*>(node)); break;
        case Ast::SetAstType:                                   this->visitSet(dynamic_cast<SetAst*>(node)); break;
        case Ast::ListComprehensionAstType:                     this->visitListComprehension(dynamic_cast<ListComprehensionAst*>(node)); break;
        case Ast::SetComprehensionAstType:                      this->visitSetComprehension(dynamic_cast<SetComprehensionAst*>(node)); break;
        case Ast::DictionaryComprehensionAstType:               this->visitDictionaryComprehension(dynamic_cast<DictionaryComprehensionAst*>(node)); break;
        case Ast::GeneratorExpressionAstType:                   this->visitGeneratorExpression(dynamic_cast<GeneratorExpressionAst*>(node)); break;
        case Ast::CompareAstType:                               this->visitCompare(dynamic_cast<CompareAst*>(node)); break;
        case Ast::ReprAstType:                                  this->visitRepr(dynamic_cast<ReprAst*>(node)); break;
        case Ast::NumberAstType:                                this->visitNumber(dynamic_cast<NumberAst*>(node)); break;
        case Ast::StringAstType:                                this->visitString(dynamic_cast<StringAst*>(node)); break;
        case Ast::YieldAstType:                                 this->visitYield(dynamic_cast<YieldAst*>(node)); break;
        case Ast::NameAstType:                                  this->visitName(dynamic_cast<NameAst*>(node)); break;
        case Ast::CallAstType:                                  this->visitCall(dynamic_cast<CallAst*>(node)); break;
        case Ast::AttributeAstType:                             this->visitAttribute(dynamic_cast<AttributeAst*>(node)); break;
        case Ast::SubscriptAstType:                             this->visitSubscript(dynamic_cast<SubscriptAst*>(node)); break;
        case Ast::ListAstType:                                  this->visitList(dynamic_cast<ListAst*>(node)); break;
        case Ast::TupleAstType:                                 this->visitTuple(dynamic_cast<TupleAst*>(node)); break;
        case Ast::EllipsisAstType:                              this->visitEllipsis(dynamic_cast<EllipsisAst*>(node)); break;
        case Ast::SliceAstType:                                 this->visitSlice(dynamic_cast<SliceAst*>(node)); break;
        case Ast::ExtendedSliceAstType:                         this->visitExtendedSlice(dynamic_cast<ExtendedSliceAst*>(node)); break;
        case Ast::IndexAstType:                                 this->visitIndex(dynamic_cast<IndexAst*>(node)); break;
        case Ast::ArgumentsAstType:                             this->visitArguments(dynamic_cast<ArgumentsAst*>(node)); break;
        case Ast::KeywordAstType:                               this->visitKeyword(dynamic_cast<KeywordAst*>(node)); break;
        case Ast::ComprehensionAstType:                         this->visitComprehension(dynamic_cast<ComprehensionAst*>(node)); break;
        case Ast::ExceptionHandlerAstType:                      this->visitExceptionHandler(dynamic_cast<ExceptionHandlerAst*>(node)); break;
        case Ast::AliasAstType:                                 this->visitAlias(dynamic_cast<AliasAst*>(node)); break;
        case Ast::ExpressionAstType:                            this->visitExpression(dynamic_cast<ExpressionAst*>(node)); break;
        case Ast::StatementAstType:                             break;
    }
}

}
