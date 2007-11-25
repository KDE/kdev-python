// THIS FILE IS GENERATED
// WARNING! All changes made in this file will be lost!

#ifndef PYTHON_VISITOR_H_INCLUDED
#define PYTHON_VISITOR_H_INCLUDED

#include "pythonast.h"

#include <parserexport.h>
namespace Python
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
    virtual void visitAnd_expr(And_exprAst *) {}
    virtual void visitAnd_test(And_testAst *) {}
    virtual void visitArg_list(Arg_listAst *) {}
    virtual void visitArglist(ArglistAst *) {}
    virtual void visitArgument(ArgumentAst *) {}
    virtual void visitArith_expr(Arith_exprAst *) {}
    virtual void visitArith_op(Arith_opAst *) {}
    virtual void visitAssert_stmt(Assert_stmtAst *) {}
    virtual void visitAtom(AtomAst *) {}
    virtual void visitAugassign(AugassignAst *) {}
    virtual void visitBreak_stmt(Break_stmtAst *) {}
    virtual void visitClassdef(ClassdefAst *) {}
    virtual void visitComp_op(Comp_opAst *) {}
    virtual void visitComparison(ComparisonAst *) {}
    virtual void visitCompound_stmt(Compound_stmtAst *) {}
    virtual void visitContinue_stmt(Continue_stmtAst *) {}
    virtual void visitDecorator(DecoratorAst *) {}
    virtual void visitDecorators(DecoratorsAst *) {}
    virtual void visitDel_stmt(Del_stmtAst *) {}
    virtual void visitDictmaker(DictmakerAst *) {}
    virtual void visitDotted_as_name(Dotted_as_nameAst *) {}
    virtual void visitDotted_as_names(Dotted_as_namesAst *) {}
    virtual void visitDotted_name(Dotted_nameAst *) {}
    virtual void visitExcept_clause(Except_clauseAst *) {}
    virtual void visitExec_stmt(Exec_stmtAst *) {}
    virtual void visitExpr(ExprAst *) {}
    virtual void visitExpr_stmt(Expr_stmtAst *) {}
    virtual void visitExprlist(ExprlistAst *) {}
    virtual void visitFact_op(Fact_opAst *) {}
    virtual void visitFactor(FactorAst *) {}
    virtual void visitFlow_stmt(Flow_stmtAst *) {}
    virtual void visitFor_stmt(For_stmtAst *) {}
    virtual void visitFp_def(Fp_defAst *) {}
    virtual void visitFpdef(FpdefAst *) {}
    virtual void visitFplist(FplistAst *) {}
    virtual void visitFun_pos_param(Fun_pos_paramAst *) {}
    virtual void visitFunc_def(Func_defAst *) {}
    virtual void visitFuncdef(FuncdefAst *) {}
    virtual void visitGen_for(Gen_forAst *) {}
    virtual void visitGen_if(Gen_ifAst *) {}
    virtual void visitGen_iter(Gen_iterAst *) {}
    virtual void visitGlobal_stmt(Global_stmtAst *) {}
    virtual void visitIf_stmt(If_stmtAst *) {}
    virtual void visitImport_as_name(Import_as_nameAst *) {}
    virtual void visitImport_as_names(Import_as_namesAst *) {}
    virtual void visitImport_from(Import_fromAst *) {}
    virtual void visitImport_name(Import_nameAst *) {}
    virtual void visitImport_stmt(Import_stmtAst *) {}
    virtual void visitLambda_def(Lambda_defAst *) {}
    virtual void visitList_for(List_forAst *) {}
    virtual void visitList_if(List_ifAst *) {}
    virtual void visitList_iter(List_iterAst *) {}
    virtual void visitList_maker(List_makerAst *) {}
    virtual void visitListmaker(ListmakerAst *) {}
    virtual void visitNot_test(Not_testAst *) {}
    virtual void visitNumber(NumberAst *) {}
    virtual void visitPass_stmt(Pass_stmtAst *) {}
    virtual void visitPower(PowerAst *) {}
    virtual void visitPrint_stmt(Print_stmtAst *) {}
    virtual void visitProject(ProjectAst *) {}
    virtual void visitRaise_stmt(Raise_stmtAst *) {}
    virtual void visitReturn_stmt(Return_stmtAst *) {}
    virtual void visitShift_expr(Shift_exprAst *) {}
    virtual void visitShift_op(Shift_opAst *) {}
    virtual void visitSimple_stmt(Simple_stmtAst *) {}
    virtual void visitSliceop(SliceopAst *) {}
    virtual void visitSmall_stmt(Small_stmtAst *) {}
    virtual void visitStmt(StmtAst *) {}
    virtual void visitSubscript(SubscriptAst *) {}
    virtual void visitSubscriptlist(SubscriptlistAst *) {}
    virtual void visitSuite(SuiteAst *) {}
    virtual void visitTerm(TermAst *) {}
    virtual void visitTerm_op(Term_opAst *) {}
    virtual void visitTest(TestAst *) {}
    virtual void visitTest_list_gexp(Test_list_gexpAst *) {}
    virtual void visitTestlist(TestlistAst *) {}
    virtual void visitTestlist1(Testlist1Ast *) {}
    virtual void visitTestlist_gexp(Testlist_gexpAst *) {}
    virtual void visitTestlist_safe(Testlist_safeAst *) {}
    virtual void visitTrailer(TrailerAst *) {}
    virtual void visitTry_stmt(Try_stmtAst *) {}
    virtual void visitVarargslist(VarargslistAst *) {}
    virtual void visitWhile_stmt(While_stmtAst *) {}
    virtual void visitXor_expr(Xor_exprAst *) {}
    virtual void visitYield_stmt(Yield_stmtAst *) {}
};

} // end of namespace Python

#endif

