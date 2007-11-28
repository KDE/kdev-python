// THIS FILE IS GENERATED
// WARNING! All changes made in this file will be lost!

#ifndef PYTHON_DEFAULT_VISITOR_H_INCLUDED
#define PYTHON_DEFAULT_VISITOR_H_INCLUDED

#include "pythonvisitor.h"

#include <parserexport.h>
namespace PythonParser
{

class KDEVPYTHONPARSER_EXPORT DefaultVisitor: public Visitor
{
public:
    virtual void visitAndExpr(AndExprAst *node);
    virtual void visitAndTest(AndTestAst *node);
    virtual void visitArglist(ArglistAst *node);
    virtual void visitArgument(ArgumentAst *node);
    virtual void visitArithExpr(ArithExprAst *node);
    virtual void visitArithOp(ArithOpAst *node);
    virtual void visitAssertStmt(AssertStmtAst *node);
    virtual void visitAtom(AtomAst *node);
    virtual void visitAugassign(AugassignAst *node);
    virtual void visitBreakStmt(BreakStmtAst *node);
    virtual void visitClassdef(ClassdefAst *node);
    virtual void visitCodeexpr(CodeexprAst *node);
    virtual void visitCompOp(CompOpAst *node);
    virtual void visitComparison(ComparisonAst *node);
    virtual void visitCompoundStmt(CompoundStmtAst *node);
    virtual void visitContinueStmt(ContinueStmtAst *node);
    virtual void visitDecorator(DecoratorAst *node);
    virtual void visitDecorators(DecoratorsAst *node);
    virtual void visitDefparam(DefparamAst *node);
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
    virtual void visitFplist(FplistAst *node);
    virtual void visitFunPosParam(FunPosParamAst *node);
    virtual void visitFuncDef(FuncDefAst *node);
    virtual void visitFuncdecl(FuncdeclAst *node);
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
    virtual void visitListMakerTest(ListMakerTestAst *node);
    virtual void visitListmaker(ListmakerAst *node);
    virtual void visitNotTest(NotTestAst *node);
    virtual void visitNumber(NumberAst *node);
    virtual void visitPassStmt(PassStmtAst *node);
    virtual void visitPlainArgumentsList(PlainArgumentsListAst *node);
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
    virtual void visitTestlistGexp(TestlistGexpAst *node);
    virtual void visitTestlistSafe(TestlistSafeAst *node);
    virtual void visitTrailer(TrailerAst *node);
    virtual void visitTryStmt(TryStmtAst *node);
    virtual void visitVarargslist(VarargslistAst *node);
    virtual void visitWhileStmt(WhileStmtAst *node);
    virtual void visitXorExpr(XorExprAst *node);
    virtual void visitYieldStmt(YieldStmtAst *node);
};

} // end of namespace PythonParser

#endif

