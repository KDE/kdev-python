/*
    SPDX-FileCopyrightText: 2007 Andreas Pakulat <apaku@gmx.de>
    SPDX-FileCopyrightText: 2011 Sven Brauch <svenbrauch@googlemail.com>
    SPDX-FileCopyrightText: 2012 Patrick Spendrin <ps_ml@gmx.de>

    SPDX-License-Identifier: LGPL-2.0-or-later
*/

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
        case Ast::CodeAstType:                                  this->visitCode(static_cast<CodeAst*>(node)); break;
        case Ast::FunctionDefinitionAstType:                    this->visitFunctionDefinition(static_cast<FunctionDefinitionAst*>(node)); break;
        case Ast::ClassDefinitionAstType:                       this->visitClassDefinition(static_cast<ClassDefinitionAst*>(node)); break;
        case Ast::ReturnAstType:                                this->visitReturn(static_cast<ReturnAst*>(node)); break;
        case Ast::AwaitAstType:                                 this->visitAwait(static_cast<AwaitAst*>(node)); break;
        case Ast::DeleteAstType:                                this->visitDelete(static_cast<DeleteAst*>(node)); break;
        case Ast::AssignmentAstType:                            this->visitAssignment(static_cast<AssignmentAst*>(node)); break;
        case Ast::AugmentedAssignmentAstType:                   this->visitAugmentedAssignment(static_cast<AugmentedAssignmentAst*>(node)); break;
        case Ast::AnnotationAssignmentAstType:                  this->visitAnnotationAssignment(static_cast<AnnotationAssignmentAst*>(node)); break;
        case Ast::AssignmentExpressionAstType:                  this->visitAssignmentExpression(static_cast<AssignmentExpressionAst*>(node)); break;
        case Ast::ForAstType:                                   this->visitFor(static_cast<ForAst*>(node)); break;
        case Ast::WhileAstType:                                 this->visitWhile(static_cast<WhileAst*>(node)); break;
        case Ast::IfAstType:                                    this->visitIf(static_cast<IfAst*>(node)); break;
        case Ast::WithAstType:                                  this->visitWith(static_cast<WithAst*>(node)); break;
        case Ast::RaiseAstType:                                 this->visitRaise(static_cast<RaiseAst*>(node)); break;
        case Ast::TryAstType:                                   this->visitTry(static_cast<TryAst*>(node)); break;
        case Ast::AssertionAstType:                             this->visitAssertion(static_cast<AssertionAst*>(node)); break;
        case Ast::ImportAstType:                                this->visitImport(static_cast<ImportAst*>(node)); break;
        case Ast::ImportFromAstType:                            this->visitImportFrom(static_cast<ImportFromAst*>(node)); break;
        case Ast::GlobalAstType:                                this->visitGlobal(static_cast<GlobalAst*>(node)); break;
        case Ast::BreakAstType:                                 this->visitBreak(static_cast<BreakAst*>(node)); break;
        case Ast::ContinueAstType:                              this->visitContinue(static_cast<ContinueAst*>(node)); break;
        case Ast::PassAstType:                                  this->visitPass(static_cast<PassAst*>(node)); break;
        case Ast::NonlocalAstType:                              this->visitNonlocal(static_cast<NonlocalAst*>(node)); break;
        case Ast::BooleanOperationAstType:                      this->visitBooleanOperation(static_cast<BooleanOperationAst*>(node)); break;
        case Ast::BinaryOperationAstType:                       this->visitBinaryOperation(static_cast<BinaryOperationAst*>(node)); break;
        case Ast::UnaryOperationAstType:                        this->visitUnaryOperation(static_cast<UnaryOperationAst*>(node)); break;
        case Ast::LambdaAstType:                                this->visitLambda(static_cast<LambdaAst*>(node)); break;
        case Ast::IfExpressionAstType:                          this->visitIfExpression(static_cast<IfExpressionAst*>(node)); break;
        case Ast::DictAstType:                                  this->visitDict(static_cast<DictAst*>(node)); break;
        case Ast::SetAstType:                                   this->visitSet(static_cast<SetAst*>(node)); break;
        case Ast::ListComprehensionAstType:                     this->visitListComprehension(static_cast<ListComprehensionAst*>(node)); break;
        case Ast::SetComprehensionAstType:                      this->visitSetComprehension(static_cast<SetComprehensionAst*>(node)); break;
        case Ast::DictionaryComprehensionAstType:               this->visitDictionaryComprehension(static_cast<DictionaryComprehensionAst*>(node)); break;
        case Ast::GeneratorExpressionAstType:                   this->visitGeneratorExpression(static_cast<GeneratorExpressionAst*>(node)); break;
        case Ast::CompareAstType:                               this->visitCompare(static_cast<CompareAst*>(node)); break;
        case Ast::NumberAstType:                                this->visitNumber(static_cast<NumberAst*>(node)); break;
        case Ast::StringAstType:                                this->visitString(static_cast<StringAst*>(node)); break;
        case Ast::FormattedValueAstType:                        this->visitFormattedValue(static_cast<FormattedValueAst*>(node)); break;
        case Ast::JoinedStringAstType:                          this->visitJoinedString(static_cast<JoinedStringAst*>(node)); break;
        case Ast::BytesAstType:                                 this->visitBytes(static_cast<BytesAst*>(node)); break;
        case Ast::YieldAstType:                                 this->visitYield(static_cast<YieldAst*>(node)); break;
        case Ast::NameAstType:                                  this->visitName(static_cast<NameAst*>(node)); break;
        case Ast::NameConstantAstType:                          this->visitNameConstant(static_cast<NameConstantAst*>(node)); break;
        case Ast::CallAstType:                                  this->visitCall(static_cast<CallAst*>(node)); break;
        case Ast::AttributeAstType:                             this->visitAttribute(static_cast<AttributeAst*>(node)); break;
        case Ast::SubscriptAstType:                             this->visitSubscript(static_cast<SubscriptAst*>(node)); break;
        case Ast::StarredAstType:                               this->visitStarred(static_cast<StarredAst*>(node)); break;
        case Ast::ListAstType:                                  this->visitList(static_cast<ListAst*>(node)); break;
        case Ast::TupleAstType:                                 this->visitTuple(static_cast<TupleAst*>(node)); break;
        case Ast::EllipsisAstType:                              this->visitEllipsis(static_cast<EllipsisAst*>(node)); break;
        case Ast::SliceAstType:                                 this->visitSlice(static_cast<SliceAst*>(node)); break;
        case Ast::ArgumentsAstType:                             this->visitArguments(static_cast<ArgumentsAst*>(node)); break;
        case Ast::KeywordAstType:                               this->visitKeyword(static_cast<KeywordAst*>(node)); break;
        case Ast::ArgAstType:                                   this->visitArg(static_cast<ArgAst*>(node)); break;
        case Ast::ComprehensionAstType:                         this->visitComprehension(static_cast<ComprehensionAst*>(node)); break;
        case Ast::ExceptionHandlerAstType:                      this->visitExceptionHandler(static_cast<ExceptionHandlerAst*>(node)); break;
        case Ast::AliasAstType:                                 this->visitAlias(static_cast<AliasAst*>(node)); break;
        case Ast::ExpressionAstType:                            this->visitExpression(static_cast<ExpressionAst*>(node)); break;
        case Ast::YieldFromAstType:                             this->visitYieldFrom(static_cast<YieldFromAst*>(node)); break;
        case Ast::WithItemAstType:                              this->visitWithItem(static_cast<WithItemAst*>(node)); break;
        case Ast::MatchAstType:                                 this->visitMatch(static_cast<MatchAst*>(node)); break;
        case Ast::MatchCaseAstType:                             this->visitMatchCase(static_cast<MatchCaseAst*>(node)); break;
        case Ast::MatchValueAstType:                            this->visitMatchValue(static_cast<MatchValueAst*>(node)); break;
        case Ast::MatchSingletonAstType:                        this->visitMatchSingleton(static_cast<MatchSingletonAst*>(node)); break;
        case Ast::MatchSequenceAstType:                         this->visitMatchSequence(static_cast<MatchSequenceAst*>(node)); break;
        case Ast::MatchMappingAstType:                          this->visitMatchMapping(static_cast<MatchMappingAst*>(node)); break;
        case Ast::MatchClassAstType:                            this->visitMatchClass(static_cast<MatchClassAst*>(node)); break;
        case Ast::MatchStarAstType:                             this->visitMatchStar(static_cast<MatchStarAst*>(node)); break;
        case Ast::MatchAsAstType:                               this->visitMatchAs(static_cast<MatchAsAst*>(node)); break;
        case Ast::MatchOrAstType:                               this->visitMatchOr(static_cast<MatchOrAst*>(node)); break;
        case Ast::IdentifierAstType:                            break;
        case Ast::StatementAstType:                             break;
        case Ast::ConstantAstType:                              break;
        case Ast::PatternAstType:                               break;
        case Ast::LastAstType:                                  Q_ASSERT(false); break;
        case Ast::LastStatementType:                            Q_ASSERT(false); break;
        case Ast::LastExpressionType:                           Q_ASSERT(false); break;
        case Ast::LastPatternType:                              Q_ASSERT(false); break;
    }
}

}
