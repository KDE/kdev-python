// THIS FILE IS GENERATED
// WARNING! All changes made in this file will be lost!

#ifndef python_VISITOR_H_INCLUDED
#define python_VISITOR_H_INCLUDED

#include "python_ast.h"

namespace python
  {

  class visitor
    {
      typedef void (visitor::*parser_fun_t)(ast_node *);
      static parser_fun_t _S_parser_table[];

    public:
      virtual ~visitor()
      {}

      virtual void visit_node(ast_node *node)
      {
        if  (node)
          (this->*_S_parser_table[node->kind -  1000])(node);
      }

      virtual void visit_and_expr(and_expr_ast *)
    {}

      virtual void visit_and_test(and_test_ast *)
      {}

      virtual void visit_arg_list(arg_list_ast *)
      {}

      virtual void visit_arglist(arglist_ast *)
      {}

      virtual void visit_argument(argument_ast *)
      {}

      virtual void visit_arith_expr(arith_expr_ast *)
      {}

      virtual void visit_arith_op(arith_op_ast *)
      {}

      virtual void visit_assert_stmt(assert_stmt_ast *)
      {}

      virtual void visit_atom(atom_ast *)
      {}

      virtual void visit_augassign(augassign_ast *)
      {}

      virtual void visit_break_stmt(break_stmt_ast *)
      {}

      virtual void visit_classdef(classdef_ast *)
      {}

      virtual void visit_comp_op(comp_op_ast *)
      {}

      virtual void visit_comparison(comparison_ast *)
      {}

      virtual void visit_compound_stmt(compound_stmt_ast *)
      {}

      virtual void visit_continue_stmt(continue_stmt_ast *)
      {}

      virtual void visit_decorator(decorator_ast *)
      {}

      virtual void visit_decorators(decorators_ast *)
      {}

      virtual void visit_del_stmt(del_stmt_ast *)
      {}

      virtual void visit_dictmaker(dictmaker_ast *)
      {}

      virtual void visit_dotted_as_name(dotted_as_name_ast *)
      {}

      virtual void visit_dotted_as_names(dotted_as_names_ast *)
      {}

      virtual void visit_dotted_name(dotted_name_ast *)
      {}

      virtual void visit_except_clause(except_clause_ast *)
      {}

      virtual void visit_exec_stmt(exec_stmt_ast *)
      {}

      virtual void visit_expr(expr_ast *)
      {}

      virtual void visit_expr_stmt(expr_stmt_ast *)
      {}

      virtual void visit_exprlist(exprlist_ast *)
      {}

      virtual void visit_fact_op(fact_op_ast *)
      {}

      virtual void visit_factor(factor_ast *)
      {}

      virtual void visit_flow_stmt(flow_stmt_ast *)
      {}

      virtual void visit_for_stmt(for_stmt_ast *)
      {}

      virtual void visit_fp_def(fp_def_ast *)
      {}

      virtual void visit_fpdef(fpdef_ast *)
      {}

      virtual void visit_fplist(fplist_ast *)
      {}

      virtual void visit_fun_pos_param(fun_pos_param_ast *)
      {}

      virtual void visit_func_def(func_def_ast *)
      {}

      virtual void visit_funcdef(funcdef_ast *)
      {}

      virtual void visit_gen_for(gen_for_ast *)
      {}

      virtual void visit_gen_if(gen_if_ast *)
      {}

      virtual void visit_gen_iter(gen_iter_ast *)
      {}

      virtual void visit_global_stmt(global_stmt_ast *)
      {}

      virtual void visit_if_stmt(if_stmt_ast *)
      {}

      virtual void visit_import_as_name(import_as_name_ast *)
      {}

      virtual void visit_import_as_names(import_as_names_ast *)
      {}

      virtual void visit_import_from(import_from_ast *)
      {}

      virtual void visit_import_name(import_name_ast *)
      {}

      virtual void visit_import_stmt(import_stmt_ast *)
      {}

      virtual void visit_lambda_def(lambda_def_ast *)
      {}

      virtual void visit_list_for(list_for_ast *)
      {}

      virtual void visit_list_if(list_if_ast *)
      {}

      virtual void visit_list_iter(list_iter_ast *)
      {}

      virtual void visit_list_maker(list_maker_ast *)
      {}

      virtual void visit_listmaker(listmaker_ast *)
      {}

      virtual void visit_longstringliteral(longstringliteral_ast *)
      {}

      virtual void visit_not_test(not_test_ast *)
      {}

      virtual void visit_number(number_ast *)
      {}

      virtual void visit_pass_stmt(pass_stmt_ast *)
      {}

      virtual void visit_power(power_ast *)
      {}

      virtual void visit_print_stmt(print_stmt_ast *)
      {}

      virtual void visit_project(project_ast *)
      {}

      virtual void visit_raise_stmt(raise_stmt_ast *)
      {}

      virtual void visit_return_stmt(return_stmt_ast *)
                               {}

                               virtual void visit_shift_expr(shift_expr_ast *)
                               {}

                               virtual void visit_shift_op(shift_op_ast *)
                               {}

                               virtual void visit_shortstringliteral(shortstringliteral_ast *)
                               {}

                               virtual void visit_simple_stmt(simple_stmt_ast *)
                               {}

                               virtual void visit_sliceop(sliceop_ast *)
                               {}

                               virtual void visit_small_stmt(small_stmt_ast *)
                               {}

                               virtual void visit_stmt(stmt_ast *)
                               {}

                               virtual void visit_subscript(subscript_ast *)
                               {}

                               virtual void visit_subscriptlist(subscriptlist_ast *)
                               {}

                               virtual void visit_suite(suite_ast *)
                               {}

                               virtual void visit_term(term_ast *)
                               {}

                               virtual void visit_term_op(term_op_ast *)
                               {}

                               virtual void visit_test(test_ast *)
                               {}

                               virtual void visit_test_list_gexp(test_list_gexp_ast *)
                               {}

                               virtual void visit_testlist(testlist_ast *)
                               {}

                               virtual void visit_testlist1(testlist1_ast *)
                               {}

                               virtual void visit_testlist_gexp(testlist_gexp_ast *)
                               {}

                               virtual void visit_testlist_safe(testlist_safe_ast *)
                               {}

                               virtual void visit_trailer(trailer_ast *)
                               {}

                               virtual void visit_try_stmt(try_stmt_ast *)
                               {}

                               virtual void visit_varargslist(varargslist_ast *)
                               {}

                               virtual void visit_while_stmt(while_stmt_ast *)
                               {}

                               virtual void visit_xor_expr(xor_expr_ast *)
                               {}

                               virtual void visit_yield_stmt(yield_stmt_ast *)
                               {}

                             }

                           ;

} // end of namespace python

#endif


