// THIS FILE IS GENERATED
// WARNING! All changes made in this file will be lost!

#include "python_default_visitor.h"

namespace python
  {

  void default_visitor::visit_and_expr(and_expr_ast *node)
  {
    visit_node(node->and_expr);

    if  (node->andd_shif_expr_sequence)
      {
        const list_node<shift_expr_ast*> *__it =  node->andd_shif_expr_sequence->to_front(),  *__end =  __it;

        do
          {
            visit_node(__it->element);
            __it =  __it->next;
          }

        while  (__it !=  __end);
      }
  }

  void default_visitor::visit_and_test(and_test_ast *node)
  {
    if  (node->not_test_sequence)
      {
        const list_node<not_test_ast*> *__it =  node->not_test_sequence->to_front(),  *__end =  __it;

        do
          {
            visit_node(__it->element);
            __it =  __it->next;
          }

        while  (__it !=  __end);
      }
  }

  void default_visitor::visit_arg_list(arg_list_ast *node)
  {
    if  (node->argument_sequence)
      {
        const list_node<argument_ast*> *__it =  node->argument_sequence->to_front(),  *__end =  __it;

        do
          {
            visit_node(__it->element);
            __it =  __it->next;
          }

        while  (__it !=  __end);
      }
  }

  void default_visitor::visit_arglist(arglist_ast *node)
  {
    visit_node(node->arg_list);
    visit_node(node->arglist_star);
    visit_node(node->arglist_doublestar);
  }

  void default_visitor::visit_argument(argument_ast *node)
  {
    visit_node(node->argument_test);
    visit_node(node->argument_equal_test);
    visit_node(node->gen_for);
  }

  void default_visitor::visit_arith_expr(arith_expr_ast *node)
  {
    visit_node(node->arith_term);

    if  (node->arith_op_list_sequence)
      {
        const list_node<arith_op_ast*> *__it =  node->arith_op_list_sequence->to_front(),  *__end =  __it;

        do
          {
            visit_node(__it->element);
            __it =  __it->next;
          }

        while  (__it !=  __end);
      }

    if  (node->arith_term_list_sequence)
      {
        const list_node<term_ast*> *__it =  node->arith_term_list_sequence->to_front(),  *__end =  __it;

        do
          {
            visit_node(__it->element);
            __it =  __it->next;
          }

        while  (__it !=  __end);
      }
  }

  void default_visitor::visit_arith_op(arith_op_ast *)
{}

  void default_visitor::visit_assert_stmt(assert_stmt_ast *node)
  {
    visit_node(node->assert_not_test);
    visit_node(node->assert_raise_test);
  }

  void default_visitor::visit_atom(atom_ast *node)
  {
    visit_node(node->testlist_gexp);
    visit_node(node->listmaker);
    visit_node(node->dictmaker);
    visit_node(node->testlist1);
    visit_node(node->number);
    visit_node(node->longstringliteral);
    visit_node(node->shortstringliteral);
  }

  void default_visitor::visit_augassign(augassign_ast *)
  {}

  void default_visitor::visit_break_stmt(break_stmt_ast *)
  {}

  void default_visitor::visit_classdef(classdef_ast *node)
  {
    visit_node(node->testlist);
    visit_node(node->class_suite);
  }

  void default_visitor::visit_comp_op(comp_op_ast *)
  {}

  void default_visitor::visit_comparison(comparison_ast *node)
  {
    visit_node(node->comp_expr);

    if  (node->comp_op_sequence)
      {
        const list_node<comp_op_ast*> *__it =  node->comp_op_sequence->to_front(),  *__end =  __it;

        do
          {
            visit_node(__it->element);
            __it =  __it->next;
          }

        while  (__it !=  __end);
      }

    if  (node->comp_op_expr_sequence)
      {
        const list_node<expr_ast*> *__it =  node->comp_op_expr_sequence->to_front(),  *__end =  __it;

        do
          {
            visit_node(__it->element);
            __it =  __it->next;
          }

        while  (__it !=  __end);
      }
  }

  void default_visitor::visit_compound_stmt(compound_stmt_ast *node)
  {
    visit_node(node->if_stmt);
    visit_node(node->while_stmt);
    visit_node(node->for_stmt);
    visit_node(node->try_stmt);
    visit_node(node->fucdef);
    visit_node(node->classdef);
  }

  void default_visitor::visit_continue_stmt(continue_stmt_ast *)
  {}

  void default_visitor::visit_decorator(decorator_ast *node)
  {
    visit_node(node->decorator_name);
    visit_node(node->arguments);
  }

  void default_visitor::visit_decorators(decorators_ast *node)
  {
    if  (node->decorator_sequence)
      {
        const list_node<decorator_ast*> *__it =  node->decorator_sequence->to_front(),  *__end =  __it;

        do
          {
            visit_node(__it->element);
            __it =  __it->next;
          }

        while  (__it !=  __end);
      }
  }

  void default_visitor::visit_del_stmt(del_stmt_ast *node)
  {
    visit_node(node->del_list);
  }

  void default_visitor::visit_dictmaker(dictmaker_ast *node)
  {
    if  (node->key_list_sequence)
      {
        const list_node<test_ast*> *__it =  node->key_list_sequence->to_front(),  *__end =  __it;

        do
          {
            visit_node(__it->element);
            __it =  __it->next;
          }

        while  (__it !=  __end);
      }

    if  (node->value_list_sequence)
      {
        const list_node<test_ast*> *__it =  node->value_list_sequence->to_front(),  *__end =  __it;

        do
          {
            visit_node(__it->element);
            __it =  __it->next;
          }

        while  (__it !=  __end);
      }
  }

  void default_visitor::visit_dotted_as_name(dotted_as_name_ast *node)
  {
    visit_node(node->import_dotted_name);
  }

  void default_visitor::visit_dotted_as_names(dotted_as_names_ast *node)
  {
    if  (node->dotted_as_name_sequence)
      {
        const list_node<dotted_as_name_ast*> *__it =  node->dotted_as_name_sequence->to_front(),  *__end =  __it;

        do
          {
            visit_node(__it->element);
            __it =  __it->next;
          }

        while  (__it !=  __end);
      }
  }

  void default_visitor::visit_dotted_name(dotted_name_ast *)
{}

  void default_visitor::visit_except_clause(except_clause_ast *node)
  {
    visit_node(node->except_test);
    visit_node(node->except_target_test);
  }

  void default_visitor::visit_exec_stmt(exec_stmt_ast *node)
  {
    visit_node(node->exec_code);
    visit_node(node->global_dict_exec);
    visit_node(node->local_dict_exec);
  }

  void default_visitor::visit_expr(expr_ast *node)
  {
    visit_node(node->expr);

    if  (node->orr_expr_sequence)
      {
        const list_node<xor_expr_ast*> *__it =  node->orr_expr_sequence->to_front(),  *__end =  __it;

        do
          {
            visit_node(__it->element);
            __it =  __it->next;
          }

        while  (__it !=  __end);
      }
  }

  void default_visitor::visit_expr_stmt(expr_stmt_ast *node)
  {
    visit_node(node->testlist);
    visit_node(node->augassign);
    visit_node(node->anugassign_testlist);

    if  (node->equal_testlist_sequence)
      {
        const list_node<testlist_ast*> *__it =  node->equal_testlist_sequence->to_front(),  *__end =  __it;

        do
          {
            visit_node(__it->element);
            __it =  __it->next;
          }

        while  (__it !=  __end);
      }
  }

  void default_visitor::visit_exprlist(exprlist_ast *node)
  {
    if  (node->expr_sequence)
      {
        const list_node<expr_ast*> *__it =  node->expr_sequence->to_front(),  *__end =  __it;

        do
          {
            visit_node(__it->element);
            __it =  __it->next;
          }

        while  (__it !=  __end);
      }

    if  (node->exprlist_sequence)
      {
        const list_node<expr_ast*> *__it =  node->exprlist_sequence->to_front(),  *__end =  __it;

        do
          {
            visit_node(__it->element);
            __it =  __it->next;
          }

        while  (__it !=  __end);
      }
  }

  void default_visitor::visit_fact_op(fact_op_ast *)
{}

  void default_visitor::visit_factor(factor_ast *node)
  {
    visit_node(node->fact_op);
    visit_node(node->factor);
    visit_node(node->power);
  }

  void default_visitor::visit_flow_stmt(flow_stmt_ast *node)
  {
    visit_node(node->break_stmt);
    visit_node(node->continue_stmt);
    visit_node(node->return_stmt);
    visit_node(node->raise_stmt);
    visit_node(node->yield_stmt);
  }

  void default_visitor::visit_for_stmt(for_stmt_ast *node)
  {
    visit_node(node->for_expr);
    visit_node(node->for_testlist);
    visit_node(node->for_suite);
    visit_node(node->for_else_suite);
  }

  void default_visitor::visit_fp_def(fp_def_ast *node)
  {
    visit_node(node->fpdef);
    visit_node(node->fp_def_test);
  }

  void default_visitor::visit_fpdef(fpdef_ast *node)
  {
    visit_node(node->fplist);
  }

  void default_visitor::visit_fplist(fplist_ast *node)
  {
    if  (node->fplist_fpdef_sequence)
      {
        const list_node<fpdef_ast*> *__it =  node->fplist_fpdef_sequence->to_front(),  *__end =  __it;

        do
          {
            visit_node(__it->element);
            __it =  __it->next;
          }

        while  (__it !=  __end);
      }
  }

  void default_visitor::visit_fun_pos_param(fun_pos_param_ast *)
{}

  void default_visitor::visit_func_def(func_def_ast *node)
  {
    if  (node->fp_def_sequence)
      {
        const list_node<fp_def_ast*> *__it =  node->fp_def_sequence->to_front(),  *__end =  __it;

        do
          {
            visit_node(__it->element);
            __it =  __it->next;
          }

        while  (__it !=  __end);
      }
  }

  void default_visitor::visit_funcdef(funcdef_ast *node)
  {
    visit_node(node->decorators);

    if  (node->fun_args_sequence)
      {
        const list_node<varargslist_ast*> *__it =  node->fun_args_sequence->to_front(),  *__end =  __it;

        do
          {
            visit_node(__it->element);
            __it =  __it->next;
          }

        while  (__it !=  __end);
      }

    visit_node(node->fun_suite);
  }

  void default_visitor::visit_gen_for(gen_for_ast *node)
  {
    visit_node(node->exprlist);
    visit_node(node->test);
    visit_node(node->gen_iter);
  }

  void default_visitor::visit_gen_if(gen_if_ast *node)
  {
    visit_node(node->test);
    visit_node(node->gen_iter);
  }

  void default_visitor::visit_gen_iter(gen_iter_ast *node)
  {
    visit_node(node->gen_for);
    visit_node(node->gen_if);
  }

  void default_visitor::visit_global_stmt(global_stmt_ast *)
  {}

  void default_visitor::visit_if_stmt(if_stmt_ast *node)
  {
    if  (node->if_test_sequence)
      {
        const list_node<test_ast*> *__it =  node->if_test_sequence->to_front(),  *__end =  __it;

        do
          {
            visit_node(__it->element);
            __it =  __it->next;
          }

        while  (__it !=  __end);
      }

    visit_node(node->if_suite);

    if  (node->elif_test_sequence)
      {
        const list_node<test_ast*> *__it =  node->elif_test_sequence->to_front(),  *__end =  __it;

        do
          {
            visit_node(__it->element);
            __it =  __it->next;
          }

        while  (__it !=  __end);
      }

    if  (node->elif_suite_sequence)
      {
        const list_node<suite_ast*> *__it =  node->elif_suite_sequence->to_front(),  *__end =  __it;

        do
          {
            visit_node(__it->element);
            __it =  __it->next;
          }

        while  (__it !=  __end);
      }

    visit_node(node->if_else_suite);
  }

  void default_visitor::visit_import_as_name(import_as_name_ast *)
{}

  void default_visitor::visit_import_as_names(import_as_names_ast *node)
  {
    if  (node->import_as_name_sequence)
      {
        const list_node<import_as_name_ast*> *__it =  node->import_as_name_sequence->to_front(),  *__end =  __it;

        do
          {
            visit_node(__it->element);
            __it =  __it->next;
          }

        while  (__it !=  __end);
      }
  }

  void default_visitor::visit_import_from(import_from_ast *node)
  {
    visit_node(node->import_from_name);
    visit_node(node->import_as_names);
    visit_node(node->import_from_as_name);
  }

  void default_visitor::visit_import_name(import_name_ast *node)
  {
    visit_node(node->import_name);
  }

  void default_visitor::visit_import_stmt(import_stmt_ast *node)
  {
    visit_node(node->import_import);
    visit_node(node->import_from);
  }

  void default_visitor::visit_lambda_def(lambda_def_ast *node)
  {
    visit_node(node->lambda_varargslist);
    visit_node(node->lambda_test);
  }

  void default_visitor::visit_list_for(list_for_ast *node)
  {
    visit_node(node->exprlist);
    visit_node(node->testlist_safe);
    visit_node(node->list_iter);
  }

  void default_visitor::visit_list_if(list_if_ast *node)
  {
    visit_node(node->test);
    visit_node(node->list_iter);
  }

  void default_visitor::visit_list_iter(list_iter_ast *node)
  {
    visit_node(node->list_for);
    visit_node(node->list_if);
  }

  void default_visitor::visit_list_maker(list_maker_ast *node)
  {
    if  (node->list_test_sequence)
      {
        const list_node<test_ast*> *__it =  node->list_test_sequence->to_front(),  *__end =  __it;

        do
          {
            visit_node(__it->element);
            __it =  __it->next;
          }

        while  (__it !=  __end);
      }
  }

  void default_visitor::visit_listmaker(listmaker_ast *node)
  {
    visit_node(node->list_maker);
    visit_node(node->list_for);
  }

  void default_visitor::visit_longstringliteral(longstringliteral_ast *)
  {}

  void default_visitor::visit_not_test(not_test_ast *node)
  {
    visit_node(node->not_test);
    visit_node(node->comparison);
  }

  void default_visitor::visit_number(number_ast *)
  {}

  void default_visitor::visit_pass_stmt(pass_stmt_ast *)
  {}

  void default_visitor::visit_power(power_ast *node)
  {
    visit_node(node->atom);

    if  (node->trailer_sequence)
      {
        const list_node<trailer_ast*> *__it =  node->trailer_sequence->to_front(),  *__end =  __it;

        do
          {
            visit_node(__it->element);
            __it =  __it->next;
          }

        while  (__it !=  __end);
      }

    visit_node(node->factor);
  }

  void default_visitor::visit_print_stmt(print_stmt_ast *node)
  {
    if  (node->print_args_sequence)
      {
        const list_node<test_ast*> *__it =  node->print_args_sequence->to_front(),  *__end =  __it;

        do
          {
            visit_node(__it->element);
            __it =  __it->next;
          }

        while  (__it !=  __end);
      }

    if  (node->rshift_args_sequence)
      {
        const list_node<test_ast*> *__it =  node->rshift_args_sequence->to_front(),  *__end =  __it;

        do
          {
            visit_node(__it->element);
            __it =  __it->next;
          }

        while  (__it !=  __end);
      }
  }

  void default_visitor::visit_project(project_ast *node)
  {
    if  (node->stmt_sequence)
      {
        const list_node<stmt_ast*> *__it =  node->stmt_sequence->to_front(),  *__end =  __it;

        do
          {
            visit_node(__it->element);
            __it =  __it->next;
          }

        while  (__it !=  __end);
      }
  }

  void default_visitor::visit_raise_stmt(raise_stmt_ast *node)
  {
    visit_node(node->type);
    visit_node(node->value);
    visit_node(node->traceback);
  }

  void default_visitor::visit_return_stmt(return_stmt_ast *node)
                                    {
                                      visit_node(node->return_expr);
                                    }

                                    void default_visitor::visit_shift_expr(shift_expr_ast *node)
                                    {
                                      visit_node(node->arith_expr);

                                      if  (node->shift_op_list_sequence)
                                        {
                                          const list_node<shift_op_ast*> *__it =  node->shift_op_list_sequence->to_front(),  *__end =  __it;

                                          do
                                            {
                                              visit_node(__it->element);
                                              __it =  __it->next;
                                            }

                                          while  (__it !=  __end);
                                        }

                                      if  (node->arith_expr_list_sequence)
                                        {
                                          const list_node<arith_expr_ast*> *__it =  node->arith_expr_list_sequence->to_front(),  *__end =  __it;

                                          do
                                            {
                                              visit_node(__it->element);
                                              __it =  __it->next;
                                            }

                                          while  (__it !=  __end);
                                        }
                                    }

                                    void default_visitor::visit_shift_op(shift_op_ast *)
                                  {}

                                    void default_visitor::visit_shortstringliteral(shortstringliteral_ast *)
                                    {}

                                    void default_visitor::visit_simple_stmt(simple_stmt_ast *node)
                                    {
                                      if  (node->small_stmt_sequence)
                                        {
                                          const list_node<small_stmt_ast*> *__it =  node->small_stmt_sequence->to_front(),  *__end =  __it;

                                          do
                                            {
                                              visit_node(__it->element);
                                              __it =  __it->next;
                                            }

                                          while  (__it !=  __end);
                                        }
                                    }

                                    void default_visitor::visit_sliceop(sliceop_ast *node)
                                    {
                                      visit_node(node->slice_test);
                                    }

                                    void default_visitor::visit_small_stmt(small_stmt_ast *node)
                                    {
                                      visit_node(node->expr_stmt);
                                      visit_node(node->print_stmt);
                                      visit_node(node->del_stmt);
                                      visit_node(node->pass_stmt);
                                      visit_node(node->flow_stmt);
                                      visit_node(node->import_stmt);
                                      visit_node(node->global_stmt);
                                      visit_node(node->exec_stmt);
                                      visit_node(node->assert_stmt);
                                    }

                                    void default_visitor::visit_stmt(stmt_ast *node)
                                    {
                                      visit_node(node->simple_stmt);
                                      visit_node(node->compound_stmt);
                                    }

                                    void default_visitor::visit_subscript(subscript_ast *node)
                                    {
                                      visit_node(node->sub_test);
                                      visit_node(node->sub_colon_test);
                                      visit_node(node->sliceop);
                                    }

                                    void default_visitor::visit_subscriptlist(subscriptlist_ast *node)
                                    {
                                      if  (node->subscript_sequence)
                                        {
                                          const list_node<subscript_ast*> *__it =  node->subscript_sequence->to_front(),  *__end =  __it;

                                          do
                                            {
                                              visit_node(__it->element);
                                              __it =  __it->next;
                                            }

                                          while  (__it !=  __end);
                                        }
                                    }

                                    void default_visitor::visit_suite(suite_ast *node)
                                    {
                                      visit_node(node->simple_stmt);

                                      if  (node->stmt_sequence)
                                        {
                                          const list_node<stmt_ast*> *__it =  node->stmt_sequence->to_front(),  *__end =  __it;

                                          do
                                            {
                                              visit_node(__it->element);
                                              __it =  __it->next;
                                            }

                                          while  (__it !=  __end);
                                        }
                                    }

                                    void default_visitor::visit_term(term_ast *node)
                                    {
                                      visit_node(node->factor);

                                      if  (node->term_op_list_sequence)
                                        {
                                          const list_node<term_op_ast*> *__it =  node->term_op_list_sequence->to_front(),  *__end =  __it;

                                          do
                                            {
                                              visit_node(__it->element);
                                              __it =  __it->next;
                                            }

                                          while  (__it !=  __end);
                                        }

                                      if  (node->factor_list_sequence)
                                        {
                                          const list_node<factor_ast*> *__it =  node->factor_list_sequence->to_front(),  *__end =  __it;

                                          do
                                            {
                                              visit_node(__it->element);
                                              __it =  __it->next;
                                            }

                                          while  (__it !=  __end);
                                        }
                                    }

                                    void default_visitor::visit_term_op(term_op_ast *)
                                  {}

                                    void default_visitor::visit_test(test_ast *node)
                                    {
                                      if  (node->and_test_sequence)
                                        {
                                          const list_node<and_test_ast*> *__it =  node->and_test_sequence->to_front(),  *__end =  __it;

                                          do
                                            {
                                              visit_node(__it->element);
                                              __it =  __it->next;
                                            }

                                          while  (__it !=  __end);
                                        }

                                      visit_node(node->lambda_def);
                                    }

                                    void default_visitor::visit_test_list_gexp(test_list_gexp_ast *node)
                                    {
                                      if  (node->test_sequence)
                                        {
                                          const list_node<test_ast*> *__it =  node->test_sequence->to_front(),  *__end =  __it;

                                          do
                                            {
                                              visit_node(__it->element);
                                              __it =  __it->next;
                                            }

                                          while  (__it !=  __end);
                                        }
                                    }

                                    void default_visitor::visit_testlist(testlist_ast *node)
                                    {
                                      if  (node->test_sequence)
                                        {
                                          const list_node<test_ast*> *__it =  node->test_sequence->to_front(),  *__end =  __it;

                                          do
                                            {
                                              visit_node(__it->element);
                                              __it =  __it->next;
                                            }

                                          while  (__it !=  __end);
                                        }

                                      if  (node->testlist_sequence)
                                        {
                                          const list_node<test_ast*> *__it =  node->testlist_sequence->to_front(),  *__end =  __it;

                                          do
                                            {
                                              visit_node(__it->element);
                                              __it =  __it->next;
                                            }

                                          while  (__it !=  __end);
                                        }
                                    }

                                    void default_visitor::visit_testlist1(testlist1_ast *node)
                                    {
                                      if  (node->test_sequence)
                                        {
                                          const list_node<test_ast*> *__it =  node->test_sequence->to_front(),  *__end =  __it;

                                          do
                                            {
                                              visit_node(__it->element);
                                              __it =  __it->next;
                                            }

                                          while  (__it !=  __end);
                                        }
                                    }

                                    void default_visitor::visit_testlist_gexp(testlist_gexp_ast *node)
                                    {
                                      visit_node(node->test_list_gexp);
                                      visit_node(node->gen_for);
                                    }

                                    void default_visitor::visit_testlist_safe(testlist_safe_ast *node)
                                    {
                                      if  (node->test_sequence)
                                        {
                                          const list_node<test_ast*> *__it =  node->test_sequence->to_front(),  *__end =  __it;

                                          do
                                            {
                                              visit_node(__it->element);
                                              __it =  __it->next;
                                            }

                                          while  (__it !=  __end);
                                        }
                                    }

                                    void default_visitor::visit_trailer(trailer_ast *node)
                                    {
                                      visit_node(node->trailer_arglist);
                                      visit_node(node->subscriptlist);
                                    }

                                    void default_visitor::visit_try_stmt(try_stmt_ast *node)
                                    {
                                      visit_node(node->try_suite);

                                      if  (node->except_clause_sequence)
                                        {
                                          const list_node<except_clause_ast*> *__it =  node->except_clause_sequence->to_front(),  *__end =  __it;

                                          do
                                            {
                                              visit_node(__it->element);
                                              __it =  __it->next;
                                            }

                                          while  (__it !=  __end);
                                        }

                                      if  (node->except_suite_sequence)
                                        {
                                          const list_node<suite_ast*> *__it =  node->except_suite_sequence->to_front(),  *__end =  __it;

                                          do
                                            {
                                              visit_node(__it->element);
                                              __it =  __it->next;
                                            }

                                          while  (__it !=  __end);
                                        }

                                      visit_node(node->try_else_suite);
                                      visit_node(node->finally_suite);
                                    }

                                    void default_visitor::visit_varargslist(varargslist_ast *node)
                                    {
                                      visit_node(node->func_def);
                                      visit_node(node->fun_pos_param);
                                    }

                                    void default_visitor::visit_while_stmt(while_stmt_ast *node)
                                    {
                                      visit_node(node->while_test);
                                      visit_node(node->while_suite);
                                      visit_node(node->while_else_suite);
                                    }

                                    void default_visitor::visit_xor_expr(xor_expr_ast *node)
                                    {
                                      visit_node(node->xor_expr);

                                      if  (node->hat_xor_expr_sequence)
                                        {
                                          const list_node<and_expr_ast*> *__it =  node->hat_xor_expr_sequence->to_front(),  *__end =  __it;

                                          do
                                            {
                                              visit_node(__it->element);
                                              __it =  __it->next;
                                            }

                                          while  (__it !=  __end);
                                        }
                                    }

                                    void default_visitor::visit_yield_stmt(yield_stmt_ast *node)
                                    {
                                      visit_node(node->yield_expr);
                                    }


                                  } // end of namespace python


