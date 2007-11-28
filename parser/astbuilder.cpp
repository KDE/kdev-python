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

#include <QDebug>

#include "pythonparser.h"
#include "ast.h"
#include <kdev-pg-token-stream.h>

namespace Python
{


template <typename T> T* safeNodeCast( Ast* node )
{
    T* ast = dynamic_cast<T*>(node);
    Q_ASSERT(ast);
    return ast;
}

template <typename T> QList<T*> generateSpecializedList( const QList<Ast*>& list )
{
    QList<T*> l;
    foreach( Ast* ast, list )
    {
        T* temp = safeNodeCast<T>( ast );
        l << temp;
    }
    return l;
}

void AstBuilder::setStartEnd( Ast* ast, PythonParser::AstNode* node )
{
    ast->start = parser->tokenStream->token( node->startToken ).begin;
    ast->end = parser->tokenStream->token( node->endToken ).end;
    parser->tokenStream->startPosition( node->startToken, &ast->startLine, &ast->startCol );
    parser->tokenStream->endPosition( node->endToken, &ast->endLine, &ast->endCol );
}

QString AstBuilder::tokenText( qint64 tokenidx )
{
    KDevPG::TokenStream::Token token = parser->tokenStream->token( tokenidx );
    return parser->tokenText( token.begin, token.end );
}

AstBuilder::AstBuilder(PythonParser::Parser* p)
    : parser(p)
{
}

void AstBuilder::visitAndExpr(PythonParser::AndExprAst *node)
{
    qDebug() << "visitAndExpr start";
    qDebug() << "visitAndExpr end";
}

void AstBuilder::visitAndTest(PythonParser::AndTestAst *node)
{
    qDebug() << "visitAndTest start";
    qDebug() << "visitAndTest end";
}

void AstBuilder::visitArglist(PythonParser::ArglistAst *node)
{
    qDebug() << "visitArglist start";
    qDebug() << "visitArglist end";
}

void AstBuilder::visitArgument(PythonParser::ArgumentAst *node)
{
    qDebug() << "visitArgument start";
    qDebug() << "visitArgument end";
}

void AstBuilder::visitArithExpr(PythonParser::ArithExprAst *node)
{
    qDebug() << "visitArithExpr start";
    qDebug() << "visitArithExpr end";
}

void AstBuilder::visitArithOp(PythonParser::ArithOpAst *node)
{
    qDebug() << "visitArithOp start";
    qDebug() << "visitArithOp end";
}

void AstBuilder::visitAssertStmt(PythonParser::AssertStmtAst *node)
{
    qDebug() << "visitAssertStmt start";
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
    qDebug() << "visitAssertStmt end";
}

void AstBuilder::visitAtom(PythonParser::AtomAst *node)
{
    qDebug() << "visitAtom start";
    qDebug() << "visitAtom end";
}

void AstBuilder::visitAugassign(PythonParser::AugassignAst *node)
{
    qDebug() << "visitAugassign start";
    qDebug() << "visitAugassign end";
}

void AstBuilder::visitBreakStmt(PythonParser::BreakStmtAst *node)
{
    qDebug() << "visitBreakStmt start";
    StatementAst* ast = new StatementAst( mNodeStack.top(), Ast::BreakAst );
    setStartEnd( ast, node );
    mNodeStack.push( ast );
    qDebug() << "visitBreakStmt end";
}

void AstBuilder::visitClassdef(PythonParser::ClassdefAst *node)
{
    qDebug() << "visitClassdef start";
    ClassDefinitionAst* ast = new ClassDefinitionAst( mNodeStack.top() );
    setStartEnd( ast, node );
    ast->className = tokenText( node->className );
    visitNode( node->testlist );
    ast->inheritance = generateSpecializedList<ExpressionAst>( mListStack.pop() );
    visitNode( node->classSuite );
    ast->classBody = generateSpecializedList<StatementAst>( mListStack.pop() );
    mNodeStack.push(ast);
    qDebug() << "visitClassdef end";
}

void AstBuilder::visitCompOp(PythonParser::CompOpAst *node)
{
    qDebug() << "visitCompOp start";
    qDebug() << "visitCompOp end";
}

void AstBuilder::visitComparison(PythonParser::ComparisonAst *node)
{
    qDebug() << "visitComparison start";
    qDebug() << "visitComparison end";
}

void AstBuilder::visitCompoundStmt(PythonParser::CompoundStmtAst *node)
{
    qDebug() << "visitCompoundStmt start";
    PythonParser::DefaultVisitor::visitCompoundStmt( node );
    qDebug() << "visitCompoundStmt end";
}

void AstBuilder::visitContinueStmt(PythonParser::ContinueStmtAst *node)
{
    qDebug() << "visitContinueStmt start";
    qDebug() << "visitContinueStmt end";
}

void AstBuilder::visitDecorator(PythonParser::DecoratorAst *node)
{
    qDebug() << "visitDecorator start";
    qDebug() << "visitDecorator end";
}

void AstBuilder::visitDecorators(PythonParser::DecoratorsAst *node)
{
    qDebug() << "visitDecorators start";
    qDebug() << "visitDecorators end";
}

void AstBuilder::visitDefparam(PythonParser::DefparamAst *node)
{
    qDebug() << "visitFpdef start";
    qDebug() << "visitFpdef start";
}

void AstBuilder::visitDelStmt(PythonParser::DelStmtAst *node)
{
    qDebug() << "visitDelStmt start";
    qDebug() << "visitDelStmt end";
}

void AstBuilder::visitDictmaker(PythonParser::DictmakerAst *node)
{
    qDebug() << "visitDictmaker start";
    qDebug() << "visitDictmaker end";
}

void AstBuilder::visitDottedAsName(PythonParser::DottedAsNameAst *node)
{
    qDebug() << "visitDottedAsName start";
    qDebug() << "visitDottedAsName end";
}

void AstBuilder::visitDottedAsNames(PythonParser::DottedAsNamesAst *node)
{
    qDebug() << "visitDottedAsNames start";
    qDebug() << "visitDottedAsNames end";
}

void AstBuilder::visitDottedName(PythonParser::DottedNameAst *node)
{
    qDebug() << "visitDottedName start";
    qDebug() << "visitDottedName end";
}

void AstBuilder::visitExceptClause(PythonParser::ExceptClauseAst *node)
{
    qDebug() << "visitExceptClause start";
    qDebug() << "visitExceptClause end";
}

void AstBuilder::visitExecStmt(PythonParser::ExecStmtAst *node)
{
    qDebug() << "visitExecStmt start";
    qDebug() << "visitExecStmt end";
}

void AstBuilder::visitExpr(PythonParser::ExprAst *node)
{
    qDebug() << "visitExpr start";
    qDebug() << "visitExpr end";
}

void AstBuilder::visitExprStmt(PythonParser::ExprStmtAst *node)
{
    qDebug() << "visitExprStmt start";
    qDebug() << "visitExprStmt end";
}

void AstBuilder::visitExprlist(PythonParser::ExprlistAst *node)
{
    qDebug() << "visitExprlist start";
    qDebug() << "visitExprlist end";
}

void AstBuilder::visitFactOp(PythonParser::FactOpAst *node)
{
    qDebug() << "visitFactOp start";
    qDebug() << "visitFactOp end";
}

void AstBuilder::visitFactor(PythonParser::FactorAst *node)
{
    qDebug() << "visitFactor start";
    qDebug() << "visitFactor end";
}

void AstBuilder::visitFlowStmt(PythonParser::FlowStmtAst *node)
{
    qDebug() << "visitFlowStmt start";
    qDebug() << "visitFlowStmt end";
}

void AstBuilder::visitForStmt(PythonParser::ForStmtAst *node)
{
    qDebug() << "visitForStmt start";
    qDebug() << "visitForStmt end";
}

void AstBuilder::visitFpDef(PythonParser::FpDefAst *node)
{
    qDebug() << "visitFpDef start";
    qDebug() << "visitFpDef end";
}

void AstBuilder::visitFplist(PythonParser::FplistAst *node)
{
    qDebug() << "visitFplist start";
    qDebug() << "visitFplist end";
}

void AstBuilder::visitFunPosParam(PythonParser::FunPosParamAst *node)
{
    qDebug() << "visitFunPosParam start";
    qDebug() << "visitFunPosParam end";
}

void AstBuilder::visitFuncdecl(PythonParser::FuncdeclAst *node)
{
    qDebug() << "visitFuncdecl start";
    qDebug() << "visitFuncdecl end";
}

void AstBuilder::visitFuncDef(PythonParser::FuncDefAst *node)
{
    qDebug() << "visitFuncDef start";
    qDebug() << "visitFuncDef end";
}

void AstBuilder::visitGenFor(PythonParser::GenForAst *node)
{
    qDebug() << "visitGenFor start";
    qDebug() << "visitGenFor end";
}

void AstBuilder::visitGenIf(PythonParser::GenIfAst *node)
{
    qDebug() << "visitGenIf start";
    qDebug() << "visitGenIf end";
}

void AstBuilder::visitGenIter(PythonParser::GenIterAst *node)
{
    qDebug() << "visitGenIter start";
    qDebug() << "visitGenIter end";
}

void AstBuilder::visitGlobalStmt(PythonParser::GlobalStmtAst *node)
{
    qDebug() << "visitGlobalStmt start";
    qDebug() << "visitGlobalStmt end";
}

void AstBuilder::visitIfStmt(PythonParser::IfStmtAst *node)
{
    qDebug() << "visitIfStmt start";
    qDebug() << "visitIfStmt end";
}

void AstBuilder::visitImportAsName(PythonParser::ImportAsNameAst *node)
{
    qDebug() << "visitImportAsName start";
    qDebug() << "visitImportAsName end";
}

void AstBuilder::visitImportAsNames(PythonParser::ImportAsNamesAst *node)
{
    qDebug() << "visitImportAsNames start";
    qDebug() << "visitImportAsNames end";
}

void AstBuilder::visitImportFrom(PythonParser::ImportFromAst *node)
{
    qDebug() << "visitImportFrom start";
    qDebug() << "visitImportFrom end";
}

void AstBuilder::visitImportName(PythonParser::ImportNameAst *node)
{
    qDebug() << "visitImportName start";
    qDebug() << "visitImportName end";
}

void AstBuilder::visitImportStmt(PythonParser::ImportStmtAst *node)
{
    qDebug() << "visitImportStmt start";
    qDebug() << "visitImportStmt end";
}

void AstBuilder::visitLambdaDef(PythonParser::LambdaDefAst *node)
{
    qDebug() << "visitLambdaDef start";
    qDebug() << "visitLambdaDef end";
}

void AstBuilder::visitListFor(PythonParser::ListForAst *node)
{
    qDebug() << "visitListFor start";
    qDebug() << "visitListFor end";
}

void AstBuilder::visitListIf(PythonParser::ListIfAst *node)
{
    qDebug() << "visitListIf start";
    qDebug() << "visitListIf end";
}

void AstBuilder::visitListIter(PythonParser::ListIterAst *node)
{
    qDebug() << "visitListIter start";
    qDebug() << "visitListIter end";
}

void AstBuilder::visitListmaker(PythonParser::ListmakerAst *node)
{
    qDebug() << "visitFpDef start";
    qDebug() << "visitFpDef end";
}

void AstBuilder::visitListMakerTest(PythonParser::ListMakerTestAst *node)
{
    qDebug() << "visitListMakerTest start";
    qDebug() << "visitListMakerTest end";
}

void AstBuilder::visitNotTest(PythonParser::NotTestAst *node)
{
    qDebug() << "visitNotTest start";
    qDebug() << "visitNotTest end";
}

void AstBuilder::visitNumber(PythonParser::NumberAst *node)
{
    qDebug() << "visitNumber start";
    qDebug() << "visitNumber end";
}

void AstBuilder::visitPassStmt(PythonParser::PassStmtAst *node)
{
    qDebug() << "visitPassStmt start";
    qDebug() << "visitPassStmt end";
}

void AstBuilder::visitPower(PythonParser::PowerAst *node)
{
    qDebug() << "visitPower start";
    qDebug() << "visitPower end";
}

void AstBuilder::visitPlainArgumentsList(PythonParser::PlainArgumentsListAst *node)
{
    qDebug() << "visitPlainArgumentsList start";
    qDebug() << "visitPlainArgumentsList end";
}

void AstBuilder::visitPrintStmt(PythonParser::PrintStmtAst *node)
{
    qDebug() << "visitPrintStmt start";
    qDebug() << "visitPrintStmt end";
}

void AstBuilder::visitProject(PythonParser::ProjectAst *node)
{
    qDebug() << "visitProject start";
    CodeAst* code = new CodeAst();
    setStartEnd( code, node );
    mNodeStack.push( code );
    mListStack.push( QList<Ast*>() );
    PythonParser::DefaultVisitor::visitProject( node );
    code->statements = generateSpecializedList<StatementAst>( mListStack.pop() );
    qDebug() << "visitProject end";
}

void AstBuilder::visitRaiseStmt(PythonParser::RaiseStmtAst *node)
{
    qDebug() << "visitRaiseStmt start";
    qDebug() << "visitRaiseStmt end";
}

void AstBuilder::visitReturnStmt(PythonParser::ReturnStmtAst *node)
{
    qDebug() << "visitReturnStmt start";
    qDebug() << "visitReturnStmt end";
}

void AstBuilder::visitShiftExpr(PythonParser::ShiftExprAst *node)
{
    qDebug() << "visitShiftExpr start";
    qDebug() << "visitShiftExpr end";
}

void AstBuilder::visitShiftOp(PythonParser::ShiftOpAst *node)
{
    qDebug() << "visitShiftOp start";
    qDebug() << "visitShiftOp end";
}

void AstBuilder::visitSimpleStmt(PythonParser::SimpleStmtAst *node)
{
    qDebug() << "visitSimpleStmt start";
    PythonParser::DefaultVisitor::visitSimpleStmt( node );
    qDebug() << "visitSimpleStmt end";
}

void AstBuilder::visitSliceop(PythonParser::SliceopAst *node)
{
    qDebug() << "visitSliceop start";
    qDebug() << "visitSliceop end";
}

void AstBuilder::visitSmallStmt(PythonParser::SmallStmtAst *node)
{
    qDebug() << "visitSmallStmt start";
    PythonParser::DefaultVisitor::visitSmallStmt( node );
    qDebug() << "visitSmallStmt end";
}

void AstBuilder::visitStmt(PythonParser::StmtAst *node)
{
    qDebug() << "visitStmt start";
    if( node->simpleStmt || node->compoundStmt )
    {
        PythonParser::DefaultVisitor::visitStmt( node );
        StatementAst* ast = safeNodeCast<StatementAst>(mNodeStack.pop());
        QList<Ast*>& stmtlist = mListStack.top();
        stmtlist << ast;
    }else
    {
        qDebug() << "Found linebreak";
    }
    qDebug() << "visitStmt end";
}

void AstBuilder::visitSubscript(PythonParser::SubscriptAst *node)
{
    qDebug() << "visitSubscript start";
    qDebug() << "visitSubscript end";
}

void AstBuilder::visitSubscriptlist(PythonParser::SubscriptlistAst *node)
{
    qDebug() << "visitSubscriptlist start";
    qDebug() << "visitSubscriptlist end";
}

void AstBuilder::visitSuite(PythonParser::SuiteAst *node)
{
    qDebug() << "visitSuite start";
    qDebug() << "visitSuite end";
}

void AstBuilder::visitTerm(PythonParser::TermAst *node)
{
    qDebug() << "visitTerm start";
    qDebug() << "visitTerm end";
}

void AstBuilder::visitTermOp(PythonParser::TermOpAst *node)
{
    qDebug() << "visitTermOp start";
    qDebug() << "visitTermOp end";
}

void AstBuilder::visitTest(PythonParser::TestAst *node)
{
    qDebug() << "visitTest start";
    qDebug() << "visitTest end";
}

void AstBuilder::visitTestListGexp(PythonParser::TestListGexpAst *node)
{
    qDebug() << "visitTestListGexp start";
    qDebug() << "visitTestListGexp end";
}

void AstBuilder::visitTestlist(PythonParser::TestlistAst *node)
{
    qDebug() << "visitTestlist start";
    qDebug() << "visitTestlist end";
}

void AstBuilder::visitCodeexpr(PythonParser::CodeexprAst *node)
{
    qDebug() << "visitCodeexpr start";
    qDebug() << "visitCodeexpr end";
}

void AstBuilder::visitTestlistGexp(PythonParser::TestlistGexpAst *node)
{
    qDebug() << "visitTestlistGexp start";
    qDebug() << "visitTestlistGexp end";
}

void AstBuilder::visitTestlistSafe(PythonParser::TestlistSafeAst *node)
{
    qDebug() << "visitTestlistSafe start";
    qDebug() << "visitTestlistSafe end";
}

void AstBuilder::visitTrailer(PythonParser::TrailerAst *node)
{
    qDebug() << "visitTrailer start";
    qDebug() << "visitTrailer end";
}

void AstBuilder::visitTryStmt(PythonParser::TryStmtAst *node)
{
    qDebug() << "visitTryStmt start";
    qDebug() << "visitTryStmt end";
}

void AstBuilder::visitVarargslist(PythonParser::VarargslistAst *node)
{
    qDebug() << "visitVarargslist start";
    qDebug() << "visitVarargslist end";
}

void AstBuilder::visitWhileStmt(PythonParser::WhileStmtAst *node)
{
    qDebug() << "visitWhileStmt start";
    qDebug() << "visitWhileStmt end";
}

void AstBuilder::visitXorExpr(PythonParser::XorExprAst *node)
{
    qDebug() << "visitXorExpr start";
    qDebug() << "visitXorExpr end";
}

void AstBuilder::visitYieldStmt(PythonParser::YieldStmtAst *node)
{
    qDebug() << "visitYieldStmt start";
    qDebug() << "visitYieldStmt end";
}

CodeAst* AstBuilder::codeAst()
{
    return safeNodeCast<CodeAst>( mNodeStack.top() );
}

}
