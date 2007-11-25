// THIS FILE IS GENERATED
// WARNING! All changes made in this file will be lost!

#ifndef PYTHON_DEFAULT_VISITOR_H_INCLUDED
#define PYTHON_DEFAULT_VISITOR_H_INCLUDED

#include "pythonvisitor.h"

#include <parserexport.h>
namespace Python
{

class KDEVPYTHONPARSER_EXPORT DefaultVisitor: public Visitor
{
public:
    virtual void visitAnd_expr(And_exprAst *node);
    virtual void visitAnd_test(And_testAst *node);
    virtual void visitArg_list(Arg_listAst *node);
    virtual void visitArglist(ArglistAst *node);
    virtual void visitArgument(ArgumentAst *node);
    virtual void visitArith_expr(Arith_exprAst *node);
    virtual void visitArith_op(Arith_opAst *node);
    virtual void visitAssert_stmt(Assert_stmtAst *node);
    virtual void visitAtom(AtomAst *node);
    virtual void visitAugassign(AugassignAst *node);
    virtual void visitBreak_stmt(Break_stmtAst *node);
    virtual void visitClassdef(ClassdefAst *node);
    virtual void visitComp_op(Comp_opAst *node);
    virtual void visitComparison(ComparisonAst *node);
    virtual void visitCompound_stmt(Compound_stmtAst *node);
    virtual void visitContinue_stmt(Continue_stmtAst *node);
    virtual void visitDecorator(DecoratorAst *node);
    virtual void visitDecorators(DecoratorsAst *node);
    virtual void visitDel_stmt(Del_stmtAst *node);
    virtual void visitDictmaker(DictmakerAst *node);
    virtual void visitDotted_as_name(Dotted_as_nameAst *node);
    virtual void visitDotted_as_names(Dotted_as_namesAst *node);
    virtual void visitDotted_name(Dotted_nameAst *node);
    virtual void visitExcept_clause(Except_clauseAst *node);
    virtual void visitExec_stmt(Exec_stmtAst *node);
    virtual void visitExpr(ExprAst *node);
    virtual void visitExpr_stmt(Expr_stmtAst *node);
    virtual void visitExprlist(ExprlistAst *node);
    virtual void visitFact_op(Fact_opAst *node);
    virtual void visitFactor(FactorAst *node);
    virtual void visitFlow_stmt(Flow_stmtAst *node);
    virtual void visitFor_stmt(For_stmtAst *node);
    virtual void visitFp_def(Fp_defAst *node);
    virtual void visitFpdef(FpdefAst *node);
    virtual void visitFplist(FplistAst *node);
    virtual void visitFun_pos_param(Fun_pos_paramAst *node);
    virtual void visitFunc_def(Func_defAst *node);
    virtual void visitFuncdef(FuncdefAst *node);
    virtual void visitGen_for(Gen_forAst *node);
    virtual void visitGen_if(Gen_ifAst *node);
    virtual void visitGen_iter(Gen_iterAst *node);
    virtual void visitGlobal_stmt(Global_stmtAst *node);
    virtual void visitIf_stmt(If_stmtAst *node);
    virtual void visitImport_as_name(Import_as_nameAst *node);
    virtual void visitImport_as_names(Import_as_namesAst *node);
    virtual void visitImport_from(Import_fromAst *node);
    virtual void visitImport_name(Import_nameAst *node);
    virtual void visitImport_stmt(Import_stmtAst *node);
    virtual void visitLambda_def(Lambda_defAst *node);
    virtual void visitList_for(List_forAst *node);
    virtual void visitList_if(List_ifAst *node);
    virtual void visitList_iter(List_iterAst *node);
    virtual void visitList_maker(List_makerAst *node);
    virtual void visitListmaker(ListmakerAst *node);
    virtual void visitNot_test(Not_testAst *node);
    virtual void visitNumber(NumberAst *node);
    virtual void visitPass_stmt(Pass_stmtAst *node);
    virtual void visitPower(PowerAst *node);
    virtual void visitPrint_stmt(Print_stmtAst *node);
    virtual void visitProject(ProjectAst *node);
    virtual void visitRaise_stmt(Raise_stmtAst *node);
    virtual void visitReturn_stmt(Return_stmtAst *node);
    virtual void visitShift_expr(Shift_exprAst *node);
    virtual void visitShift_op(Shift_opAst *node);
    virtual void visitSimple_stmt(Simple_stmtAst *node);
    virtual void visitSliceop(SliceopAst *node);
    virtual void visitSmall_stmt(Small_stmtAst *node);
    virtual void visitStmt(StmtAst *node);
    virtual void visitSubscript(SubscriptAst *node);
    virtual void visitSubscriptlist(SubscriptlistAst *node);
    virtual void visitSuite(SuiteAst *node);
    virtual void visitTerm(TermAst *node);
    virtual void visitTerm_op(Term_opAst *node);
    virtual void visitTest(TestAst *node);
    virtual void visitTest_list_gexp(Test_list_gexpAst *node);
    virtual void visitTestlist(TestlistAst *node);
    virtual void visitTestlist1(Testlist1Ast *node);
    virtual void visitTestlist_gexp(Testlist_gexpAst *node);
    virtual void visitTestlist_safe(Testlist_safeAst *node);
    virtual void visitTrailer(TrailerAst *node);
    virtual void visitTry_stmt(Try_stmtAst *node);
    virtual void visitVarargslist(VarargslistAst *node);
    virtual void visitWhile_stmt(While_stmtAst *node);
    virtual void visitXor_expr(Xor_exprAst *node);
    virtual void visitYield_stmt(Yield_stmtAst *node);
};

} // end of namespace Python

#endif

