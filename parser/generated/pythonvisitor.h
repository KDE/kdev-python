// THIS FILE IS GENERATED
// WARNING! All changes made in this file will be lost!

#ifndef PYTHON_VISITOR_H_INCLUDED
#define PYTHON_VISITOR_H_INCLUDED

#include "pythonast.h"

#include <parserexport.h>
namespace PythonParser
{

class KDEVPYTHONPARSER_EXPORT Visitor
{
    typedef void (Visitor::*ParserFuncType)(AstNode *);
    static ParserFuncType sParserTable[];

public:
    virtual ~Visitor() {}
    virtual void visitNode(AstNode *node)
    {
        if (node) (this->*sParserTable[node->kind - 1000])(node);
    }
    virtual void visitAndExpr(AndExprAst *) {}
    virtual void visitAndTest(AndTestAst *) {}
    virtual void visitArglist(ArglistAst *) {}
    virtual void visitArgument(ArgumentAst *) {}
    virtual void visitArithExpr(ArithExprAst *) {}
    virtual void visitArithOp(ArithOpAst *) {}
    virtual void visitAssertStmt(AssertStmtAst *) {}
    virtual void visitAtom(AtomAst *) {}
    virtual void visitAugassign(AugassignAst *) {}
    virtual void visitBreakStmt(BreakStmtAst *) {}
    virtual void visitClassdef(ClassdefAst *) {}
    virtual void visitCompOp(CompOpAst *) {}
    virtual void visitComparison(ComparisonAst *) {}
    virtual void visitCompoundStmt(CompoundStmtAst *) {}
    virtual void visitContinueStmt(ContinueStmtAst *) {}
    virtual void visitDecorator(DecoratorAst *) {}
    virtual void visitDecorators(DecoratorsAst *) {}
    virtual void visitDelStmt(DelStmtAst *) {}
    virtual void visitDictmaker(DictmakerAst *) {}
    virtual void visitDottedAsName(DottedAsNameAst *) {}
    virtual void visitDottedAsNames(DottedAsNamesAst *) {}
    virtual void visitDottedName(DottedNameAst *) {}
    virtual void visitExceptClause(ExceptClauseAst *) {}
    virtual void visitExecStmt(ExecStmtAst *) {}
    virtual void visitExpr(ExprAst *) {}
    virtual void visitExprStmt(ExprStmtAst *) {}
    virtual void visitExprlist(ExprlistAst *) {}
    virtual void visitFactOp(FactOpAst *) {}
    virtual void visitFactor(FactorAst *) {}
    virtual void visitFlowStmt(FlowStmtAst *) {}
    virtual void visitForStmt(ForStmtAst *) {}
    virtual void visitFpDef(FpDefAst *) {}
    virtual void visitFpdef(FpdefAst *) {}
    virtual void visitFplist(FplistAst *) {}
    virtual void visitFunPosParam(FunPosParamAst *) {}
    virtual void visitFuncDef(FuncDefAst *) {}
    virtual void visitFuncdef(FuncdefAst *) {}
    virtual void visitGenFor(GenForAst *) {}
    virtual void visitGenIf(GenIfAst *) {}
    virtual void visitGenIter(GenIterAst *) {}
    virtual void visitGlobalStmt(GlobalStmtAst *) {}
    virtual void visitIfStmt(IfStmtAst *) {}
    virtual void visitImportAsName(ImportAsNameAst *) {}
    virtual void visitImportAsNames(ImportAsNamesAst *) {}
    virtual void visitImportFrom(ImportFromAst *) {}
    virtual void visitImportName(ImportNameAst *) {}
    virtual void visitImportStmt(ImportStmtAst *) {}
    virtual void visitLambdaDef(LambdaDefAst *) {}
    virtual void visitListFor(ListForAst *) {}
    virtual void visitListIf(ListIfAst *) {}
    virtual void visitListIter(ListIterAst *) {}
    virtual void visitListMaker(ListMakerAst *) {}
    virtual void visitListmaker(ListmakerAst *) {}
    virtual void visitNotTest(NotTestAst *) {}
    virtual void visitNumber(NumberAst *) {}
    virtual void visitPassStmt(PassStmtAst *) {}
    virtual void visitPlainArgumentsList(PlainArgumentsListAst *) {}
    virtual void visitPower(PowerAst *) {}
    virtual void visitPrintStmt(PrintStmtAst *) {}
    virtual void visitProject(ProjectAst *) {}
    virtual void visitRaiseStmt(RaiseStmtAst *) {}
    virtual void visitReturnStmt(ReturnStmtAst *) {}
    virtual void visitShiftExpr(ShiftExprAst *) {}
    virtual void visitShiftOp(ShiftOpAst *) {}
    virtual void visitSimpleStmt(SimpleStmtAst *) {}
    virtual void visitSliceop(SliceopAst *) {}
    virtual void visitSmallStmt(SmallStmtAst *) {}
    virtual void visitStmt(StmtAst *) {}
    virtual void visitSubscript(SubscriptAst *) {}
    virtual void visitSubscriptlist(SubscriptlistAst *) {}
    virtual void visitSuite(SuiteAst *) {}
    virtual void visitTerm(TermAst *) {}
    virtual void visitTermOp(TermOpAst *) {}
    virtual void visitTest(TestAst *) {}
    virtual void visitTestListGexp(TestListGexpAst *) {}
    virtual void visitTestlist(TestlistAst *) {}
    virtual void visitTestlist1(Testlist1Ast *) {}
    virtual void visitTestlistGexp(TestlistGexpAst *) {}
    virtual void visitTestlistSafe(TestlistSafeAst *) {}
    virtual void visitTrailer(TrailerAst *) {}
    virtual void visitTryStmt(TryStmtAst *) {}
    virtual void visitVarargslist(VarargslistAst *) {}
    virtual void visitWhileStmt(WhileStmtAst *) {}
    virtual void visitXorExpr(XorExprAst *) {}
    virtual void visitYieldStmt(YieldStmtAst *) {}
};

} // end of namespace PythonParser

#endif

