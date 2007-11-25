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

#ifndef astbuilder_H
#define astbuilder_H

class AstBuilder
{
public:
    AstBuilder();

    virtual void visitAndExpr(AndExprAst *node);
    virtual void visitAndTest(AndTestAst *node);
    virtual void visitArgList(ArgListAst *node);
    virtual void visitArglist(ArglistAst *node);
    virtual void visitArgument(ArgumentAst *node);
    virtual void visitArithExpr(ArithExprAst *node);
    virtual void visitArithOp(ArithOpAst *node);
    virtual void visitAssertStmt(AssertStmtAst *node);
    virtual void visitAtom(AtomAst *node);
    virtual void visitAugassign(AugassignAst *node);
    virtual void visitBreakStmt(BreakStmtAst *node);
    virtual void visitClassdef(ClassdefAst *node);
    virtual void visitCompOp(CompOpAst *node);
    virtual void visitComparison(ComparisonAst *node);
    virtual void visitCompoundStmt(CompoundStmtAst *node);
    virtual void visitContinueStmt(ContinueStmtAst *node);
    virtual void visitDecorator(DecoratorAst *node);
    virtual void visitDecorators(DecoratorsAst *node);
    virtual void visitDelStmt(DelStmtAst *node);
    virtual void visitDictmaker(DictmakerAst *node);
    virtual void visitDottedAsName(DottedAsNameAst *node);
    virtual void visitDottedAsNames(DottedAsNamesAst *node);
    virtual void visitDottedName(DottedNameAst *node);
    virtual void visitExceptClause(ExceptClauseAst *node);
    virtual void visitExecStmt(ExecStmtAst *node);
    virtual void visitExpr(ExprAst *node);
    virtual void visitExprStmt(ExprStmtAst *node);
    virtual void visitExprlist(ExprlistAst *node);
    virtual void visitFactOp(FactOpAst *node);
    virtual void visitFactor(FactorAst *node);
    virtual void visitFlowStmt(FlowStmtAst *node);
    virtual void visitForStmt(ForStmtAst *node);
    virtual void visitFpDef(FpDefAst *node);
    virtual void visitFpdef(FpdefAst *node);
    virtual void visitFplist(FplistAst *node);
    virtual void visitFunPosParam(FunPosParamAst *node);
    virtual void visitFuncDef(FuncDefAst *node);
    virtual void visitFuncdef(FuncdefAst *node);
    virtual void visitGenFor(GenForAst *node);
    virtual void visitGenIf(GenIfAst *node);
    virtual void visitGenIter(GenIterAst *node);
    virtual void visitGlobalStmt(GlobalStmtAst *node);
    virtual void visitIfStmt(IfStmtAst *node);
    virtual void visitImportAsName(ImportAsNameAst *node);
    virtual void visitImportAsNames(ImportAsNamesAst *node);
    virtual void visitImportFrom(ImportFromAst *node);
    virtual void visitImportName(ImportNameAst *node);
    virtual void visitImportStmt(ImportStmtAst *node);
    virtual void visitLambdaDef(LambdaDefAst *node);
    virtual void visitListFor(ListForAst *node);
    virtual void visitListIf(ListIfAst *node);
    virtual void visitListIter(ListIterAst *node);
    virtual void visitListMaker(ListMakerAst *node);
    virtual void visitListmaker(ListmakerAst *node);
    virtual void visitNotTest(NotTestAst *node);
    virtual void visitNumber(NumberAst *node);
    virtual void visitPassStmt(PassStmtAst *node);
    virtual void visitPower(PowerAst *node);
    virtual void visitPrintStmt(PrintStmtAst *node);
    virtual void visitProject(ProjectAst *node);
    virtual void visitRaiseStmt(RaiseStmtAst *node);
    virtual void visitReturnStmt(ReturnStmtAst *node);
    virtual void visitShiftExpr(ShiftExprAst *node);
    virtual void visitShiftOp(ShiftOpAst *node);
    virtual void visitSimpleStmt(SimpleStmtAst *node);
    virtual void visitSliceop(SliceopAst *node);
    virtual void visitSmallStmt(SmallStmtAst *node);
    virtual void visitStmt(StmtAst *node);
    virtual void visitSubscript(SubscriptAst *node);
    virtual void visitSubscriptlist(SubscriptlistAst *node);
    virtual void visitSuite(SuiteAst *node);
    virtual void visitTerm(TermAst *node);
    virtual void visitTermOp(TermOpAst *node);
    virtual void visitTest(TestAst *node);
    virtual void visitTestListGexp(TestListGexpAst *node);
    virtual void visitTestlist(TestlistAst *node);
    virtual void visitTestlist1(Testlist1Ast *node);
    virtual void visitTestlistGexp(TestlistGexpAst *node);
    virtual void visitTestlistSafe(TestlistSafeAst *node);
    virtual void visitTrailer(TrailerAst *node);
    virtual void visitTryStmt(TryStmtAst *node);
    virtual void visitVarargslist(VarargslistAst *node);
    virtual void visitWhileStmt(WhileStmtAst *node);
    virtual void visitXorExpr(XorExprAst *node);
    virtual void visitYieldStmt(YieldStmtAst *node);

};

#endif

