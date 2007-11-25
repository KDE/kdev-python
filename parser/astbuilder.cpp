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

#include "astbuilder.h"

namespace Python
{


template <typename T> T* safeNodeCast( Ast* node )
{
    T* ast = dynamic_cast<T*>(node);
    Q_ASSERT(ast);
    return ast;
}


void AstBuilder::setStartEnd( Ast* ast, PythonParser::AstNode* node )
{
    ast->start = tokenStream->token( node->startToken ).begin;
    ast->end = tokenStream->token( node->endToken ).end;
    tokenStream->startPosition( node->startToken, &ast->startLine, &ast->startCol );
    tokenStream->endPosition( node->endToken, &ast->endLine, &ast->endCol );
}

AstBuilder::AstBuilder(KDevPG::TokenStream* stream)
    : tokenStream(stream)
{
}

void AstBuilder::visitAndExpr(PythonParser::AndExprAst *node)
{
}

void AstBuilder::visitAndTest(PythonParser::AndTestAst *node)
{
}

void AstBuilder::visitArglist(PythonParser::ArglistAst *node)
{
}

void AstBuilder::visitArgument(PythonParser::ArgumentAst *node)
{
}

void AstBuilder::visitArithExpr(PythonParser::ArithExprAst *node)
{
}

void AstBuilder::visitArithOp(PythonParser::ArithOpAst *node)
{
}

void AstBuilder::visitAssertStmt(PythonParser::AssertStmtAst *node)
{
    AssertAst* ast = new AssertAst( mNodeStack.top() );
    setStartEnd( ast, node );
    visitNode( node->assertNotTest );
    ast->assertTest = safeNodeCast<ExpressionAst>(mNodeStack.pop());
    if( node->assertRaiseTest )
    {
        visitNode( node->assertRaiseTest );
        ast->exceptionValue = safeNodeCast<ExpressionAst>(mNodeStack.pop());
    }
    mNodeStack.push(ast);
}

void AstBuilder::visitAtom(PythonParser::AtomAst *node)
{
}

void AstBuilder::visitAugassign(PythonParser::AugassignAst *node)
{
}

void AstBuilder::visitBreakStmt(PythonParser::BreakStmtAst *node)
{
    StatementAst* ast = new StatementAst( mNodeStack.top() );
    setStartEnd( ast, node );
    ast->astType = Ast::BreakAst;
    mNodeStack.push( ast );
}

void AstBuilder::visitClassdef(PythonParser::ClassdefAst *node)
{
}

void AstBuilder::visitCompOp(PythonParser::CompOpAst *node)
{
}

void AstBuilder::visitComparison(PythonParser::ComparisonAst *node)
{
}

void AstBuilder::visitCompoundStmt(PythonParser::CompoundStmtAst *node)
{
    PythonParser::DefaultVisitor::visitCompoundStmt( node );
}

void AstBuilder::visitContinueStmt(PythonParser::ContinueStmtAst *node)
{
}

void AstBuilder::visitDecorator(PythonParser::DecoratorAst *node)
{
}

void AstBuilder::visitDecorators(PythonParser::DecoratorsAst *node)
{
}

void AstBuilder::visitDelStmt(PythonParser::DelStmtAst *node)
{
}

void AstBuilder::visitDictmaker(PythonParser::DictmakerAst *node)
{
}

void AstBuilder::visitDottedAsName(PythonParser::DottedAsNameAst *node)
{
}

void AstBuilder::visitDottedAsNames(PythonParser::DottedAsNamesAst *node)
{
}

void AstBuilder::visitDottedName(PythonParser::DottedNameAst *node)
{
}

void AstBuilder::visitExceptClause(PythonParser::ExceptClauseAst *node)
{
}

void AstBuilder::visitExecStmt(PythonParser::ExecStmtAst *node)
{
}

void AstBuilder::visitExpr(PythonParser::ExprAst *node)
{
}

void AstBuilder::visitExprStmt(PythonParser::ExprStmtAst *node)
{
}

void AstBuilder::visitExprlist(PythonParser::ExprlistAst *node)
{
}

void AstBuilder::visitFactOp(PythonParser::FactOpAst *node)
{
}

void AstBuilder::visitFactor(PythonParser::FactorAst *node)
{
}

void AstBuilder::visitFlowStmt(PythonParser::FlowStmtAst *node)
{
}

void AstBuilder::visitForStmt(PythonParser::ForStmtAst *node)
{
}

void AstBuilder::visitFpDef(PythonParser::FpDefAst *node)
{
}

void AstBuilder::visitFpdef(PythonParser::FpdefAst *node)
{
}

void AstBuilder::visitFplist(PythonParser::FplistAst *node)
{
}

void AstBuilder::visitFunPosParam(PythonParser::FunPosParamAst *node)
{
}

void AstBuilder::visitFuncDef(PythonParser::FuncDefAst *node)
{
}

void AstBuilder::visitFuncdef(PythonParser::FuncdefAst *node)
{
}

void AstBuilder::visitGenFor(PythonParser::GenForAst *node)
{
}

void AstBuilder::visitGenIf(PythonParser::GenIfAst *node)
{
}

void AstBuilder::visitGenIter(PythonParser::GenIterAst *node)
{
}

void AstBuilder::visitGlobalStmt(PythonParser::GlobalStmtAst *node)
{
}

void AstBuilder::visitIfStmt(PythonParser::IfStmtAst *node)
{
}

void AstBuilder::visitImportAsName(PythonParser::ImportAsNameAst *node)
{
}

void AstBuilder::visitImportAsNames(PythonParser::ImportAsNamesAst *node)
{
}

void AstBuilder::visitImportFrom(PythonParser::ImportFromAst *node)
{
}

void AstBuilder::visitImportName(PythonParser::ImportNameAst *node)
{
}

void AstBuilder::visitImportStmt(PythonParser::ImportStmtAst *node)
{
}

void AstBuilder::visitLambdaDef(PythonParser::LambdaDefAst *node)
{
}

void AstBuilder::visitListFor(PythonParser::ListForAst *node)
{
}

void AstBuilder::visitListIf(PythonParser::ListIfAst *node)
{
}

void AstBuilder::visitListIter(PythonParser::ListIterAst *node)
{
}

void AstBuilder::visitListMaker(PythonParser::ListMakerAst *node)
{
}

void AstBuilder::visitListmaker(PythonParser::ListmakerAst *node)
{
}

void AstBuilder::visitNotTest(PythonParser::NotTestAst *node)
{
}

void AstBuilder::visitNumber(PythonParser::NumberAst *node)
{
}

void AstBuilder::visitPassStmt(PythonParser::PassStmtAst *node)
{
}

void AstBuilder::visitPower(PythonParser::PowerAst *node)
{
}

void AstBuilder::visitPlainArgumentsList(PythonParser::PlainArgumentsListAst *node)
{
}

void AstBuilder::visitPrintStmt(PythonParser::PrintStmtAst *node)
{
}

void AstBuilder::visitProject(PythonParser::ProjectAst *node)
{
    CodeAst* code = new CodeAst();
    setStartEnd( code, node );
    mNodeStack.push( code );
    PythonParser::DefaultVisitor::visitProject( node );

}

void AstBuilder::visitRaiseStmt(PythonParser::RaiseStmtAst *node)
{
}

void AstBuilder::visitReturnStmt(PythonParser::ReturnStmtAst *node)
{
}

void AstBuilder::visitShiftExpr(PythonParser::ShiftExprAst *node)
{
}

void AstBuilder::visitShiftOp(PythonParser::ShiftOpAst *node)
{
}

void AstBuilder::visitSimpleStmt(PythonParser::SimpleStmtAst *node)
{
    PythonParser::DefaultVisitor::visitSimpleStmt( node );
}

void AstBuilder::visitSliceop(PythonParser::SliceopAst *node)
{
}

void AstBuilder::visitSmallStmt(PythonParser::SmallStmtAst *node)
{
    PythonParser::DefaultVisitor::visitSmallStmt( node );
}

void AstBuilder::visitStmt(PythonParser::StmtAst *node)
{
    PythonParser::DefaultVisitor::visitStmt( node );
    StatementAst* ast = safeNodeCast<StatementAst>(mNodeStack.pop());
    CodeAst* code = safeNodeCast<CodeAst>(mNodeStack.top());
    code->statements.append( ast );
}

void AstBuilder::visitSubscript(PythonParser::SubscriptAst *node)
{
}

void AstBuilder::visitSubscriptlist(PythonParser::SubscriptlistAst *node)
{
}

void AstBuilder::visitSuite(PythonParser::SuiteAst *node)
{
}

void AstBuilder::visitTerm(PythonParser::TermAst *node)
{
}

void AstBuilder::visitTermOp(PythonParser::TermOpAst *node)
{
}

void AstBuilder::visitTest(PythonParser::TestAst *node)
{
}

void AstBuilder::visitTestListGexp(PythonParser::TestListGexpAst *node)
{
}

void AstBuilder::visitTestlist(PythonParser::TestlistAst *node)
{
}


void AstBuilder::visitCodeexpr(PythonParser::CodeexprAst *node)
{
}

void AstBuilder::visitTestlistGexp(PythonParser::TestlistGexpAst *node)
{
}

void AstBuilder::visitTestlistSafe(PythonParser::TestlistSafeAst *node)
{
}

void AstBuilder::visitTrailer(PythonParser::TrailerAst *node)
{
}

void AstBuilder::visitTryStmt(PythonParser::TryStmtAst *node)
{
}

void AstBuilder::visitVarargslist(PythonParser::VarargslistAst *node)
{
}

void AstBuilder::visitWhileStmt(PythonParser::WhileStmtAst *node)
{
}

void AstBuilder::visitXorExpr(PythonParser::XorExprAst *node)
{
}

void AstBuilder::visitYieldStmt(PythonParser::YieldStmtAst *node)
{
}

}
