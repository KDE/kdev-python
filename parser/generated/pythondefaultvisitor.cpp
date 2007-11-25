// THIS FILE IS GENERATED
// WARNING! All changes made in this file will be lost!

#include "pythondefaultvisitor.h"

namespace Python
{

void DefaultVisitor::visitAnd_expr(And_exprAst *node)
{
    visitNode(node->and_expr);
    if (node->andd_shif_exprSequence)
    {
        const KDevPG::ListNode<Shift_exprAst*> *__it = node->andd_shif_exprSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitAnd_test(And_testAst *node)
{
    if (node->not_testSequence)
    {
        const KDevPG::ListNode<Not_testAst*> *__it = node->not_testSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitArg_list(Arg_listAst *node)
{
    if (node->argumentSequence)
    {
        const KDevPG::ListNode<ArgumentAst*> *__it = node->argumentSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitArglist(ArglistAst *node)
{
    visitNode(node->arg_list);
    visitNode(node->arglist_star);
    visitNode(node->arglist_doublestar);
}

void DefaultVisitor::visitArgument(ArgumentAst *node)
{
    visitNode(node->argument_test);
    visitNode(node->argument_equal_test);
    visitNode(node->gen_for);
}

void DefaultVisitor::visitArith_expr(Arith_exprAst *node)
{
    visitNode(node->arith_term);
    if (node->arith_op_listSequence)
    {
        const KDevPG::ListNode<Arith_opAst*> *__it = node->arith_op_listSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
    if (node->arith_term_listSequence)
    {
        const KDevPG::ListNode<TermAst*> *__it = node->arith_term_listSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitArith_op(Arith_opAst *)
{
}

void DefaultVisitor::visitAssert_stmt(Assert_stmtAst *node)
{
    visitNode(node->assert_not_test);
    visitNode(node->assert_raise_test);
}

void DefaultVisitor::visitAtom(AtomAst *node)
{
    visitNode(node->testlist_gexp);
    visitNode(node->listmaker);
    visitNode(node->dictmaker);
    visitNode(node->testlist1);
    visitNode(node->number);
}

void DefaultVisitor::visitAugassign(AugassignAst *)
{
}

void DefaultVisitor::visitBreak_stmt(Break_stmtAst *)
{
}

void DefaultVisitor::visitClassdef(ClassdefAst *node)
{
    visitNode(node->testlist);
    visitNode(node->class_suite);
}

void DefaultVisitor::visitComp_op(Comp_opAst *)
{
}

void DefaultVisitor::visitComparison(ComparisonAst *node)
{
    visitNode(node->comp_expr);
    if (node->comp_opSequence)
    {
        const KDevPG::ListNode<Comp_opAst*> *__it = node->comp_opSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
    if (node->comp_op_exprSequence)
    {
        const KDevPG::ListNode<ExprAst*> *__it = node->comp_op_exprSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitCompound_stmt(Compound_stmtAst *node)
{
    visitNode(node->if_stmt);
    visitNode(node->while_stmt);
    visitNode(node->for_stmt);
    visitNode(node->try_stmt);
    visitNode(node->fucdef);
    visitNode(node->classdef);
}

void DefaultVisitor::visitContinue_stmt(Continue_stmtAst *)
{
}

void DefaultVisitor::visitDecorator(DecoratorAst *node)
{
    visitNode(node->decorator_name);
    visitNode(node->arguments);
}

void DefaultVisitor::visitDecorators(DecoratorsAst *node)
{
    if (node->decoratorSequence)
    {
        const KDevPG::ListNode<DecoratorAst*> *__it = node->decoratorSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitDel_stmt(Del_stmtAst *node)
{
    visitNode(node->del_list);
}

void DefaultVisitor::visitDictmaker(DictmakerAst *node)
{
    if (node->key_listSequence)
    {
        const KDevPG::ListNode<TestAst*> *__it = node->key_listSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
    if (node->value_listSequence)
    {
        const KDevPG::ListNode<TestAst*> *__it = node->value_listSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitDotted_as_name(Dotted_as_nameAst *node)
{
    visitNode(node->import_dotted_name);
}

void DefaultVisitor::visitDotted_as_names(Dotted_as_namesAst *node)
{
    if (node->dotted_as_nameSequence)
    {
        const KDevPG::ListNode<Dotted_as_nameAst*> *__it = node->dotted_as_nameSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitDotted_name(Dotted_nameAst *)
{
}

void DefaultVisitor::visitExcept_clause(Except_clauseAst *node)
{
    visitNode(node->except_test);
    visitNode(node->except_target_test);
}

void DefaultVisitor::visitExec_stmt(Exec_stmtAst *node)
{
    visitNode(node->exec_code);
    visitNode(node->global_dict_exec);
    visitNode(node->local_dict_exec);
}

void DefaultVisitor::visitExpr(ExprAst *node)
{
    visitNode(node->expr);
    if (node->orr_exprSequence)
    {
        const KDevPG::ListNode<Xor_exprAst*> *__it = node->orr_exprSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitExpr_stmt(Expr_stmtAst *node)
{
    visitNode(node->testlist);
    visitNode(node->augassign);
    visitNode(node->anugassign_testlist);
    if (node->equal_testlistSequence)
    {
        const KDevPG::ListNode<TestlistAst*> *__it = node->equal_testlistSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitExprlist(ExprlistAst *node)
{
    if (node->exprSequence)
    {
        const KDevPG::ListNode<ExprAst*> *__it = node->exprSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
    if (node->exprlistSequence)
    {
        const KDevPG::ListNode<ExprAst*> *__it = node->exprlistSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitFact_op(Fact_opAst *)
{
}

void DefaultVisitor::visitFactor(FactorAst *node)
{
    visitNode(node->fact_op);
    visitNode(node->factor);
    visitNode(node->power);
}

void DefaultVisitor::visitFlow_stmt(Flow_stmtAst *node)
{
    visitNode(node->break_stmt);
    visitNode(node->continue_stmt);
    visitNode(node->return_stmt);
    visitNode(node->raise_stmt);
    visitNode(node->yield_stmt);
}

void DefaultVisitor::visitFor_stmt(For_stmtAst *node)
{
    visitNode(node->for_expr);
    visitNode(node->for_testlist);
    visitNode(node->for_suite);
    visitNode(node->for_else_suite);
}

void DefaultVisitor::visitFp_def(Fp_defAst *node)
{
    visitNode(node->fpdef);
    visitNode(node->fp_def_test);
}

void DefaultVisitor::visitFpdef(FpdefAst *node)
{
    visitNode(node->fplist);
}

void DefaultVisitor::visitFplist(FplistAst *node)
{
    if (node->fplist_fpdefSequence)
    {
        const KDevPG::ListNode<FpdefAst*> *__it = node->fplist_fpdefSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitFun_pos_param(Fun_pos_paramAst *)
{
}

void DefaultVisitor::visitFunc_def(Func_defAst *node)
{
    if (node->fp_defSequence)
    {
        const KDevPG::ListNode<Fp_defAst*> *__it = node->fp_defSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitFuncdef(FuncdefAst *node)
{
    visitNode(node->decorators);
    visitNode(node->fun_args);
    visitNode(node->fun_suite);
}

void DefaultVisitor::visitGen_for(Gen_forAst *node)
{
    visitNode(node->exprlist);
    visitNode(node->test);
    visitNode(node->gen_iter);
}

void DefaultVisitor::visitGen_if(Gen_ifAst *node)
{
    visitNode(node->test);
    visitNode(node->gen_iter);
}

void DefaultVisitor::visitGen_iter(Gen_iterAst *node)
{
    visitNode(node->gen_for);
    visitNode(node->gen_if);
}

void DefaultVisitor::visitGlobal_stmt(Global_stmtAst *)
{
}

void DefaultVisitor::visitIf_stmt(If_stmtAst *node)
{
    if (node->if_testSequence)
    {
        const KDevPG::ListNode<TestAst*> *__it = node->if_testSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
    visitNode(node->if_suite);
    if (node->elif_testSequence)
    {
        const KDevPG::ListNode<TestAst*> *__it = node->elif_testSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
    if (node->elif_suiteSequence)
    {
        const KDevPG::ListNode<SuiteAst*> *__it = node->elif_suiteSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
    visitNode(node->if_else_suite);
}

void DefaultVisitor::visitImport_as_name(Import_as_nameAst *)
{
}

void DefaultVisitor::visitImport_as_names(Import_as_namesAst *node)
{
    if (node->import_as_nameSequence)
    {
        const KDevPG::ListNode<Import_as_nameAst*> *__it = node->import_as_nameSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitImport_from(Import_fromAst *node)
{
    visitNode(node->import_from_name);
    visitNode(node->import_as_names);
    visitNode(node->import_from_as_name);
}

void DefaultVisitor::visitImport_name(Import_nameAst *node)
{
    visitNode(node->import_name);
}

void DefaultVisitor::visitImport_stmt(Import_stmtAst *node)
{
    visitNode(node->import_import);
    visitNode(node->import_from);
}

void DefaultVisitor::visitLambda_def(Lambda_defAst *node)
{
    visitNode(node->lambda_varargslist);
    visitNode(node->lambda_test);
}

void DefaultVisitor::visitList_for(List_forAst *node)
{
    visitNode(node->exprlist);
    visitNode(node->testlist_safe);
    visitNode(node->list_iter);
}

void DefaultVisitor::visitList_if(List_ifAst *node)
{
    visitNode(node->test);
    visitNode(node->list_iter);
}

void DefaultVisitor::visitList_iter(List_iterAst *node)
{
    visitNode(node->list_for);
    visitNode(node->list_if);
}

void DefaultVisitor::visitList_maker(List_makerAst *node)
{
    if (node->list_testSequence)
    {
        const KDevPG::ListNode<TestAst*> *__it = node->list_testSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitListmaker(ListmakerAst *node)
{
    visitNode(node->list_maker);
    visitNode(node->list_for);
}

void DefaultVisitor::visitNot_test(Not_testAst *node)
{
    visitNode(node->not_test);
    visitNode(node->comparison);
}

void DefaultVisitor::visitNumber(NumberAst *)
{
}

void DefaultVisitor::visitPass_stmt(Pass_stmtAst *)
{
}

void DefaultVisitor::visitPower(PowerAst *node)
{
    visitNode(node->atom);
    if (node->trailerSequence)
    {
        const KDevPG::ListNode<TrailerAst*> *__it = node->trailerSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
    visitNode(node->factor);
}

void DefaultVisitor::visitPrint_stmt(Print_stmtAst *node)
{
    if (node->print_argsSequence)
    {
        const KDevPG::ListNode<TestAst*> *__it = node->print_argsSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
    if (node->rshift_argsSequence)
    {
        const KDevPG::ListNode<TestAst*> *__it = node->rshift_argsSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitProject(ProjectAst *node)
{
    if (node->stmtSequence)
    {
        const KDevPG::ListNode<StmtAst*> *__it = node->stmtSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitRaise_stmt(Raise_stmtAst *node)
{
    visitNode(node->type);
    visitNode(node->value);
    visitNode(node->traceback);
}

void DefaultVisitor::visitReturn_stmt(Return_stmtAst *node)
{
    visitNode(node->return_expr);
}

void DefaultVisitor::visitShift_expr(Shift_exprAst *node)
{
    visitNode(node->arith_expr);
    if (node->shift_op_listSequence)
    {
        const KDevPG::ListNode<Shift_opAst*> *__it = node->shift_op_listSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
    if (node->arith_expr_listSequence)
    {
        const KDevPG::ListNode<Arith_exprAst*> *__it = node->arith_expr_listSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitShift_op(Shift_opAst *)
{
}

void DefaultVisitor::visitSimple_stmt(Simple_stmtAst *node)
{
    if (node->small_stmtSequence)
    {
        const KDevPG::ListNode<Small_stmtAst*> *__it = node->small_stmtSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitSliceop(SliceopAst *node)
{
    visitNode(node->slice_test);
}

void DefaultVisitor::visitSmall_stmt(Small_stmtAst *node)
{
    visitNode(node->expr_stmt);
    visitNode(node->print_stmt);
    visitNode(node->del_stmt);
    visitNode(node->pass_stmt);
    visitNode(node->flow_stmt);
    visitNode(node->import_stmt);
    visitNode(node->global_stmt);
    visitNode(node->exec_stmt);
    visitNode(node->assert_stmt);
}

void DefaultVisitor::visitStmt(StmtAst *node)
{
    visitNode(node->simple_stmt);
    visitNode(node->compound_stmt);
}

void DefaultVisitor::visitSubscript(SubscriptAst *node)
{
    visitNode(node->sub_test);
    visitNode(node->sub_colon_test);
    visitNode(node->sliceop);
}

void DefaultVisitor::visitSubscriptlist(SubscriptlistAst *node)
{
    if (node->subscriptSequence)
    {
        const KDevPG::ListNode<SubscriptAst*> *__it = node->subscriptSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitSuite(SuiteAst *node)
{
    visitNode(node->simple_stmt);
    if (node->stmtSequence)
    {
        const KDevPG::ListNode<StmtAst*> *__it = node->stmtSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitTerm(TermAst *node)
{
    visitNode(node->factor);
    if (node->term_op_listSequence)
    {
        const KDevPG::ListNode<Term_opAst*> *__it = node->term_op_listSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
    if (node->factor_listSequence)
    {
        const KDevPG::ListNode<FactorAst*> *__it = node->factor_listSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitTerm_op(Term_opAst *)
{
}

void DefaultVisitor::visitTest(TestAst *node)
{
    if (node->and_testSequence)
    {
        const KDevPG::ListNode<And_testAst*> *__it = node->and_testSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
    visitNode(node->lambda_def);
}

void DefaultVisitor::visitTest_list_gexp(Test_list_gexpAst *node)
{
    if (node->testSequence)
    {
        const KDevPG::ListNode<TestAst*> *__it = node->testSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitTestlist(TestlistAst *node)
{
    if (node->testSequence)
    {
        const KDevPG::ListNode<TestAst*> *__it = node->testSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
    if (node->testlistSequence)
    {
        const KDevPG::ListNode<TestAst*> *__it = node->testlistSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitTestlist1(Testlist1Ast *node)
{
    if (node->testSequence)
    {
        const KDevPG::ListNode<TestAst*> *__it = node->testSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitTestlist_gexp(Testlist_gexpAst *node)
{
    visitNode(node->test_list_gexp);
    visitNode(node->gen_for);
}

void DefaultVisitor::visitTestlist_safe(Testlist_safeAst *node)
{
    if (node->testSequence)
    {
        const KDevPG::ListNode<TestAst*> *__it = node->testSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitTrailer(TrailerAst *node)
{
    visitNode(node->trailer_arglist);
    visitNode(node->subscriptlist);
}

void DefaultVisitor::visitTry_stmt(Try_stmtAst *node)
{
    visitNode(node->try_suite);
    if (node->except_clauseSequence)
    {
        const KDevPG::ListNode<Except_clauseAst*> *__it = node->except_clauseSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
    if (node->except_suiteSequence)
    {
        const KDevPG::ListNode<SuiteAst*> *__it = node->except_suiteSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
    visitNode(node->try_else_suite);
    visitNode(node->finally_suite);
}

void DefaultVisitor::visitVarargslist(VarargslistAst *node)
{
    visitNode(node->func_def);
    visitNode(node->fun_pos_param);
}

void DefaultVisitor::visitWhile_stmt(While_stmtAst *node)
{
    visitNode(node->while_test);
    visitNode(node->while_suite);
    visitNode(node->while_else_suite);
}

void DefaultVisitor::visitXor_expr(Xor_exprAst *node)
{
    visitNode(node->xor_expr);
    if (node->hat_xor_exprSequence)
    {
        const KDevPG::ListNode<And_exprAst*> *__it = node->hat_xor_exprSequence->front(), *__end = __it;
        do
        {
            visitNode(__it->element);
            __it = __it->next;
        }
        while (__it != __end);
    }
}

void DefaultVisitor::visitYield_stmt(Yield_stmtAst *node)
{
    visitNode(node->yield_expr);
}


} // end of namespace Python

