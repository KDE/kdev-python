// THIS FILE IS GENERATED
// WARNING! All changes made in this file will be lost!

#ifndef python_AST_H_INCLUDED
#define python_AST_H_INCLUDED

#include <kdev-pg-list.h>



namespace python
  {
  class Lexer;

  enum shift_operator_enum {
    op_lshift,
    op_rshift
  };
  enum arith_operator_enum {
    op_plus,
    op_minus
  };
  enum term_operator_enum {
    op_star,
    op_slash,
    op_modulo,
    op_doubleslash
  };
  enum factor_operator_enum {
    op_factor_plus,
    op_factor_minus,
    op_factor_tilde
  };
  enum augassign_eq_enum  {
    eq_plus,
    eq_minus,
    eq_star,
    eq_slash,
    eq_modulo,
    eq_and,
    eq_or,
    eq_tilde,
    eq_lshift,
    eq_rshift,
    eq_doublestar,
    eq_doubleslash
  };
  enum comp_operator_enum   {
    op_less,
    op_greater,
    op_isequal,
    op_greatereq,
    op_lesseq,
    op_unequal,
    op_in,
    op_not_in,
    op_is,
    op_is_not
  };
  enum num_type_enum  {
    type_int,
    type_float,
    type_imagnum
  };
}

namespace python
  {

  struct and_expr_ast;
  struct and_test_ast;
  struct arg_list_ast;
  struct arglist_ast;
  struct argument_ast;
  struct arith_expr_ast;
  struct arith_op_ast;
  struct assert_stmt_ast;
  struct atom_ast;
  struct augassign_ast;
  struct break_stmt_ast;
  struct classdef_ast;
  struct comp_op_ast;
  struct comparison_ast;
  struct compound_stmt_ast;
  struct continue_stmt_ast;
  struct decorator_ast;
  struct decorators_ast;
  struct del_stmt_ast;
  struct dictmaker_ast;
  struct dotted_as_name_ast;
  struct dotted_as_names_ast;
  struct dotted_name_ast;
  struct except_clause_ast;
  struct exec_stmt_ast;
  struct expr_ast;
  struct expr_stmt_ast;
  struct exprlist_ast;
  struct fact_op_ast;
  struct factor_ast;
  struct flow_stmt_ast;
  struct for_stmt_ast;
  struct fp_def_ast;
  struct fpdef_ast;
  struct fplist_ast;
  struct fun_pos_param_ast;
  struct func_def_ast;
  struct funcdef_ast;
  struct gen_for_ast;
  struct gen_if_ast;
  struct gen_iter_ast;
  struct global_stmt_ast;
  struct if_stmt_ast;
  struct import_as_name_ast;
  struct import_as_names_ast;
  struct import_from_ast;
  struct import_name_ast;
  struct import_stmt_ast;
  struct lambda_def_ast;
  struct list_for_ast;
  struct list_if_ast;
  struct list_iter_ast;
  struct list_maker_ast;
  struct listmaker_ast;
  struct longstringliteral_ast;
  struct not_test_ast;
  struct number_ast;
  struct pass_stmt_ast;
  struct power_ast;
  struct print_stmt_ast;
  struct project_ast;
  struct raise_stmt_ast;
  struct return_stmt_ast;
  struct shift_expr_ast;
  struct shift_op_ast;
  struct shortstringliteral_ast;
  struct simple_stmt_ast;
  struct sliceop_ast;
  struct small_stmt_ast;
  struct stmt_ast;
  struct subscript_ast;
  struct subscriptlist_ast;
  struct suite_ast;
  struct term_ast;
  struct term_op_ast;
  struct test_ast;
  struct test_list_gexp_ast;
  struct testlist_ast;
  struct testlist1_ast;
  struct testlist_gexp_ast;
  struct testlist_safe_ast;
  struct trailer_ast;
  struct try_stmt_ast;
  struct varargslist_ast;
  struct while_stmt_ast;
  struct xor_expr_ast;
  struct yield_stmt_ast;


  struct ast_node
    {
      enum ast_node_kind_enum {
        Kind_and_expr = 1000,
        Kind_and_test = 1001,
        Kind_arg_list = 1002,
        Kind_arglist = 1003,
        Kind_argument = 1004,
        Kind_arith_expr = 1005,
        Kind_arith_op = 1006,
        Kind_assert_stmt = 1007,
        Kind_atom = 1008,
        Kind_augassign = 1009,
        Kind_break_stmt = 1010,
        Kind_classdef = 1011,
        Kind_comp_op = 1012,
        Kind_comparison = 1013,
        Kind_compound_stmt = 1014,
        Kind_continue_stmt = 1015,
        Kind_decorator = 1016,
        Kind_decorators = 1017,
        Kind_del_stmt = 1018,
        Kind_dictmaker = 1019,
        Kind_dotted_as_name = 1020,
        Kind_dotted_as_names = 1021,
        Kind_dotted_name = 1022,
        Kind_except_clause = 1023,
        Kind_exec_stmt = 1024,
        Kind_expr = 1025,
        Kind_expr_stmt = 1026,
        Kind_exprlist = 1027,
        Kind_fact_op = 1028,
        Kind_factor = 1029,
        Kind_flow_stmt = 1030,
        Kind_for_stmt = 1031,
        Kind_fp_def = 1032,
        Kind_fpdef = 1033,
        Kind_fplist = 1034,
        Kind_fun_pos_param = 1035,
        Kind_func_def = 1036,
        Kind_funcdef = 1037,
        Kind_gen_for = 1038,
        Kind_gen_if = 1039,
        Kind_gen_iter = 1040,
        Kind_global_stmt = 1041,
        Kind_if_stmt = 1042,
        Kind_import_as_name = 1043,
        Kind_import_as_names = 1044,
        Kind_import_from = 1045,
        Kind_import_name = 1046,
        Kind_import_stmt = 1047,
        Kind_lambda_def = 1048,
        Kind_list_for = 1049,
        Kind_list_if = 1050,
        Kind_list_iter = 1051,
        Kind_list_maker = 1052,
        Kind_listmaker = 1053,
        Kind_longstringliteral = 1054,
        Kind_not_test = 1055,
        Kind_number = 1056,
        Kind_pass_stmt = 1057,
        Kind_power = 1058,
        Kind_print_stmt = 1059,
        Kind_project = 1060,
        Kind_raise_stmt = 1061,
        Kind_return_stmt = 1062,
        Kind_shift_expr = 1063,
        Kind_shift_op = 1064,
        Kind_shortstringliteral = 1065,
        Kind_simple_stmt = 1066,
        Kind_sliceop = 1067,
        Kind_small_stmt = 1068,
        Kind_stmt = 1069,
        Kind_subscript = 1070,
        Kind_subscriptlist = 1071,
        Kind_suite = 1072,
        Kind_term = 1073,
        Kind_term_op = 1074,
        Kind_test = 1075,
        Kind_test_list_gexp = 1076,
        Kind_testlist = 1077,
        Kind_testlist1 = 1078,
        Kind_testlist_gexp = 1079,
        Kind_testlist_safe = 1080,
        Kind_trailer = 1081,
        Kind_try_stmt = 1082,
        Kind_varargslist = 1083,
        Kind_while_stmt = 1084,
        Kind_xor_expr = 1085,
        Kind_yield_stmt = 1086,
        AST_NODE_KIND_COUNT
      };

      int kind;
      std::size_t start_token;
      std::size_t end_token;
    };

  struct and_expr_ast: public ast_node
    {
      enum
      {
        KIND = Kind_and_expr
      };

      shift_expr_ast *and_expr;
      const list_node<shift_expr_ast *> *andd_shif_expr_sequence;
    };

  struct and_test_ast: public ast_node
    {
      enum
      {
        KIND = Kind_and_test
      };

      const list_node<not_test_ast *> *not_test_sequence;
    };

  struct arg_list_ast: public ast_node
    {
      enum
      {
        KIND = Kind_arg_list
      };

      const list_node<argument_ast *> *argument_sequence;
    };

  struct arglist_ast: public ast_node
    {
      enum
      {
        KIND = Kind_arglist
      };

      arg_list_ast *arg_list;
      test_ast *arglist_star;
      test_ast *arglist_doublestar;
    };

  struct argument_ast: public ast_node
    {
      enum
      {
        KIND = Kind_argument
      };

      test_ast *argument_test;
      test_ast *argument_equal_test;
      gen_for_ast *gen_for;
    };

  struct arith_expr_ast: public ast_node
    {
      enum
      {
        KIND = Kind_arith_expr
      };

      term_ast *arith_term;
      const list_node<arith_op_ast *> *arith_op_list_sequence;
      const list_node<term_ast *> *arith_term_list_sequence;
    };

  struct arith_op_ast: public ast_node
    {
      enum
      {
        KIND = Kind_arith_op
      };

      python::arith_operator_enum arith_operator;
    };

  struct assert_stmt_ast: public ast_node
    {
      enum
      {
        KIND = Kind_assert_stmt
      };

      test_ast *assert_not_test;
      test_ast *assert_raise_test;
    };

  struct atom_ast: public ast_node
    {
      enum
      {
        KIND = Kind_atom
      };

      testlist_gexp_ast *testlist_gexp;
      listmaker_ast *listmaker;
      dictmaker_ast *dictmaker;
      testlist1_ast *testlist1;
      std::size_t atom_identifier_name;
      number_ast *number;
      const list_node<std::size_t > *stringliteral_sequence;
      longstringliteral_ast *longstringliteral;
      shortstringliteral_ast *shortstringliteral;
    };

  struct augassign_ast: public ast_node
    {
      enum
      {
        KIND = Kind_augassign
      };

      python::augassign_eq_enum augassign_eq;
    };

  struct break_stmt_ast: public ast_node
    {
      enum
      {
        KIND = Kind_break_stmt
      };

    };

  struct classdef_ast: public ast_node
    {
      enum
      {
        KIND = Kind_classdef
      };

      std::size_t class_name;
      testlist_ast *testlist;
      suite_ast *class_suite;
    };

  struct comp_op_ast: public ast_node
    {
      enum
      {
        KIND = Kind_comp_op
      };

      python::comp_operator_enum comp_operator;
    };

  struct comparison_ast: public ast_node
    {
      enum
      {
        KIND = Kind_comparison
      };

      expr_ast *comp_expr;
      const list_node<comp_op_ast *> *comp_op_sequence;
      const list_node<expr_ast *> *comp_op_expr_sequence;
    };

  struct compound_stmt_ast: public ast_node
    {
      enum
      {
        KIND = Kind_compound_stmt
      };

      if_stmt_ast *if_stmt;
      while_stmt_ast *while_stmt;
      for_stmt_ast *for_stmt;
      try_stmt_ast *try_stmt;
      funcdef_ast *fucdef;
      classdef_ast *classdef;
    };

  struct continue_stmt_ast: public ast_node
    {
      enum
      {
        KIND = Kind_continue_stmt
      };

    };

  struct decorator_ast: public ast_node
    {
      enum
      {
        KIND = Kind_decorator
      };

      dotted_name_ast *decorator_name;
      arglist_ast *arguments;
    };

  struct decorators_ast: public ast_node
    {
      enum
      {
        KIND = Kind_decorators
      };

      const list_node<decorator_ast *> *decorator_sequence;
    };

  struct del_stmt_ast: public ast_node
    {
      enum
      {
        KIND = Kind_del_stmt
      };

      exprlist_ast *del_list;
    };

  struct dictmaker_ast: public ast_node
    {
      enum
      {
        KIND = Kind_dictmaker
      };

      const list_node<test_ast *> *key_list_sequence;
      const list_node<test_ast *> *value_list_sequence;
    };

  struct dotted_as_name_ast: public ast_node
    {
      enum
      {
        KIND = Kind_dotted_as_name
      };

      dotted_name_ast *import_dotted_name;
      std::size_t imported_as;
    };

  struct dotted_as_names_ast: public ast_node
    {
      enum
      {
        KIND = Kind_dotted_as_names
      };

      const list_node<dotted_as_name_ast *> *dotted_as_name_sequence;
    };

  struct dotted_name_ast: public ast_node
    {
      enum
      {
        KIND = Kind_dotted_name
      };

      std::size_t dotted_name;
    };

  struct except_clause_ast: public ast_node
    {
      enum
      {
        KIND = Kind_except_clause
      };

      test_ast *except_test;
      test_ast *except_target_test;
    };

  struct exec_stmt_ast: public ast_node
    {
      enum
      {
        KIND = Kind_exec_stmt
      };

      expr_ast *exec_code;
      test_ast *global_dict_exec;
      test_ast *local_dict_exec;
    };

  struct expr_ast: public ast_node
    {
      enum
      {
        KIND = Kind_expr
      };

      xor_expr_ast *expr;
      const list_node<xor_expr_ast *> *orr_expr_sequence;
    };

  struct expr_stmt_ast: public ast_node
    {
      enum
      {
        KIND = Kind_expr_stmt
      };

      testlist_ast *testlist;
      augassign_ast *augassign;
      testlist_ast *anugassign_testlist;
      const list_node<testlist_ast *> *equal_testlist_sequence;
    };

  struct exprlist_ast: public ast_node
    {
      enum
      {
        KIND = Kind_exprlist
      };

      const list_node<expr_ast *> *expr_sequence;
      const list_node<expr_ast *> *exprlist_sequence;
    };

  struct fact_op_ast: public ast_node
    {
      enum
      {
        KIND = Kind_fact_op
      };

      python::factor_operator_enum factor_operator;
    };

  struct factor_ast: public ast_node
    {
      enum
      {
        KIND = Kind_factor
      };

      fact_op_ast *fact_op;
      factor_ast *factor;
      power_ast *power;
    };

  struct flow_stmt_ast: public ast_node
    {
      enum
      {
        KIND = Kind_flow_stmt
      };

      break_stmt_ast *break_stmt;
      continue_stmt_ast *continue_stmt;
      return_stmt_ast *return_stmt;
      raise_stmt_ast *raise_stmt;
      yield_stmt_ast *yield_stmt;
    };

  struct for_stmt_ast: public ast_node
    {
      enum
      {
        KIND = Kind_for_stmt
      };

      exprlist_ast *for_expr;
      testlist_ast *for_testlist;
      suite_ast *for_suite;
      suite_ast *for_else_suite;
    };

  struct fp_def_ast: public ast_node
    {
      enum
      {
        KIND = Kind_fp_def
      };

      fpdef_ast *fpdef;
      test_ast *fp_def_test;
    };

  struct fpdef_ast: public ast_node
    {
      enum
      {
        KIND = Kind_fpdef
      };

      fplist_ast *fplist;
    };

  struct fplist_ast: public ast_node
    {
      enum
      {
        KIND = Kind_fplist
      };

      const list_node<fpdef_ast *> *fplist_fpdef_sequence;
    };

  struct fun_pos_param_ast: public ast_node
    {
      enum
      {
        KIND = Kind_fun_pos_param
      };

      std::size_t star_id;
      std::size_t double_star_id;
    };

  struct func_def_ast: public ast_node
    {
      enum
      {
        KIND = Kind_func_def
      };

      const list_node<fp_def_ast *> *fp_def_sequence;
    };

  struct funcdef_ast: public ast_node
    {
      enum
      {
        KIND = Kind_funcdef
      };

      decorators_ast *decorators;
      std::size_t func_name;
      const list_node<varargslist_ast *> *fun_args_sequence;
      suite_ast *fun_suite;
    };

  struct gen_for_ast: public ast_node
    {
      enum
      {
        KIND = Kind_gen_for
      };

      exprlist_ast *exprlist;
      test_ast *test;
      gen_iter_ast *gen_iter;
    };

  struct gen_if_ast: public ast_node
    {
      enum
      {
        KIND = Kind_gen_if
      };

      test_ast *test;
      gen_iter_ast *gen_iter;
    };

  struct gen_iter_ast: public ast_node
    {
      enum
      {
        KIND = Kind_gen_iter
      };

      gen_for_ast *gen_for;
      gen_if_ast *gen_if;
    };

  struct global_stmt_ast: public ast_node
    {
      enum
      {
        KIND = Kind_global_stmt
      };

      const list_node<std::size_t > *global_name_sequence;
    };

  struct if_stmt_ast: public ast_node
    {
      enum
      {
        KIND = Kind_if_stmt
      };

      const list_node<test_ast *> *if_test_sequence;
      suite_ast *if_suite;
      const list_node<test_ast *> *elif_test_sequence;
      const list_node<suite_ast *> *elif_suite_sequence;
      suite_ast *if_else_suite;
    };

  struct import_as_name_ast: public ast_node
    {
      enum
      {
        KIND = Kind_import_as_name
      };

      std::size_t imported_name;
      std::size_t imported_as;
    };

  struct import_as_names_ast: public ast_node
    {
      enum
      {
        KIND = Kind_import_as_names
      };

      const list_node<import_as_name_ast *> *import_as_name_sequence;
    };

  struct import_from_ast: public ast_node
    {
      enum
      {
        KIND = Kind_import_from
      };

      dotted_name_ast *import_from_name;
      import_as_names_ast *import_as_names;
      import_as_names_ast *import_from_as_name;
    };

  struct import_name_ast: public ast_node
    {
      enum
      {
        KIND = Kind_import_name
      };

      dotted_as_names_ast *import_name;
    };

  struct import_stmt_ast: public ast_node
    {
      enum
      {
        KIND = Kind_import_stmt
      };

      import_name_ast *import_import;
      import_from_ast *import_from;
    };

  struct lambda_def_ast: public ast_node
    {
      enum
      {
        KIND = Kind_lambda_def
      };

      varargslist_ast *lambda_varargslist;
      test_ast *lambda_test;
    };

  struct list_for_ast: public ast_node
    {
      enum
      {
        KIND = Kind_list_for
      };

      exprlist_ast *exprlist;
      testlist_safe_ast *testlist_safe;
      list_iter_ast *list_iter;
    };

  struct list_if_ast: public ast_node
    {
      enum
      {
        KIND = Kind_list_if
      };

      test_ast *test;
      list_iter_ast *list_iter;
    };

  struct list_iter_ast: public ast_node
    {
      enum
      {
        KIND = Kind_list_iter
      };

      list_for_ast *list_for;
      list_if_ast *list_if;
    };

  struct list_maker_ast: public ast_node
    {
      enum
      {
        KIND = Kind_list_maker
      };

      const list_node<test_ast *> *list_test_sequence;
    };

  struct listmaker_ast: public ast_node
    {
      enum
      {
        KIND = Kind_listmaker
      };

      list_maker_ast *list_maker;
      list_for_ast *list_for;
    };

  struct longstringliteral_ast: public ast_node
    {
      enum
      {
        KIND = Kind_longstringliteral
      };

      const list_node<std::size_t > *string_body_sequence;
    };

  struct not_test_ast: public ast_node
    {
      enum
      {
        KIND = Kind_not_test
      };

      not_test_ast *not_test;
      comparison_ast *comparison;
    };

  struct number_ast: public ast_node
    {
      enum
      {
        KIND = Kind_number
      };

      python::num_type_enum num_type;
    };

  struct pass_stmt_ast: public ast_node
    {
      enum
      {
        KIND = Kind_pass_stmt
      };

    };

  struct power_ast: public ast_node
    {
      enum
      {
        KIND = Kind_power
      };

      atom_ast *atom;
      const list_node<trailer_ast *> *trailer_sequence;
      factor_ast *factor;
    };

  struct print_stmt_ast: public ast_node
    {
      enum
      {
        KIND = Kind_print_stmt
      };

      const list_node<test_ast *> *print_args_sequence;
      const list_node<test_ast *> *rshift_args_sequence;
    };

  struct project_ast: public ast_node
    {
      enum
      {
        KIND = Kind_project
      };

      const list_node<stmt_ast *> *stmt_sequence;
    };

  struct raise_stmt_ast: public ast_node
    {
      enum
      {
        KIND = Kind_raise_stmt
      };

      test_ast *type;
      test_ast *value;
      test_ast *traceback;
    };

  struct return_stmt_ast: public ast_node
                 {
                   enum
                   {
                     KIND = Kind_return_stmt
                   };

                   testlist_ast *return_expr;
                 };

  struct shift_expr_ast: public ast_node
    {
      enum
      {
        KIND = Kind_shift_expr
      };

      arith_expr_ast *arith_expr;
      const list_node<shift_op_ast *> *shift_op_list_sequence;
      const list_node<arith_expr_ast *> *arith_expr_list_sequence;
    };

  struct shift_op_ast: public ast_node
    {
      enum
      {
        KIND = Kind_shift_op
      };

      python::shift_operator_enum shift_operator;
    };

  struct shortstringliteral_ast: public ast_node
    {
      enum
      {
        KIND = Kind_shortstringliteral
      };

    };

  struct simple_stmt_ast: public ast_node
    {
      enum
      {
        KIND = Kind_simple_stmt
      };

      const list_node<small_stmt_ast *> *small_stmt_sequence;
    };

  struct sliceop_ast: public ast_node
    {
      enum
      {
        KIND = Kind_sliceop
      };

      test_ast *slice_test;
    };

  struct small_stmt_ast: public ast_node
    {
      enum
      {
        KIND = Kind_small_stmt
      };

      expr_stmt_ast *expr_stmt;
      print_stmt_ast *print_stmt;
      del_stmt_ast *del_stmt;
      pass_stmt_ast *pass_stmt;
      flow_stmt_ast *flow_stmt;
      import_stmt_ast *import_stmt;
      global_stmt_ast *global_stmt;
      exec_stmt_ast *exec_stmt;
      assert_stmt_ast *assert_stmt;
    };

  struct stmt_ast: public ast_node
    {
      enum
      {
        KIND = Kind_stmt
      };

      simple_stmt_ast *simple_stmt;
      compound_stmt_ast *compound_stmt;
    };

  struct subscript_ast: public ast_node
    {
      enum
      {
        KIND = Kind_subscript
      };

      std::size_t subcript_ellipsis;
      test_ast *sub_test;
      test_ast *sub_colon_test;
      sliceop_ast *sliceop;
    };

  struct subscriptlist_ast: public ast_node
    {
      enum
      {
        KIND = Kind_subscriptlist
      };

      const list_node<subscript_ast *> *subscript_sequence;
    };

  struct suite_ast: public ast_node
    {
      enum
      {
        KIND = Kind_suite
      };

      simple_stmt_ast *simple_stmt;
      const list_node<stmt_ast *> *stmt_sequence;
    };

  struct term_ast: public ast_node
    {
      enum
      {
        KIND = Kind_term
      };

      factor_ast *factor;
      const list_node<term_op_ast *> *term_op_list_sequence;
      const list_node<factor_ast *> *factor_list_sequence;
    };

  struct term_op_ast: public ast_node
    {
      enum
      {
        KIND = Kind_term_op
      };

      python::term_operator_enum term_operator;
    };

  struct test_ast: public ast_node
    {
      enum
      {
        KIND = Kind_test
      };

      const list_node<and_test_ast *> *and_test_sequence;
      lambda_def_ast *lambda_def;
    };

  struct test_list_gexp_ast: public ast_node
    {
      enum
      {
        KIND = Kind_test_list_gexp
      };

      const list_node<test_ast *> *test_sequence;
    };

  struct testlist_ast: public ast_node
    {
      enum
      {
        KIND = Kind_testlist
      };

      const list_node<test_ast *> *test_sequence;
      const list_node<test_ast *> *testlist_sequence;
    };

  struct testlist1_ast: public ast_node
    {
      enum
      {
        KIND = Kind_testlist1
      };

      const list_node<test_ast *> *test_sequence;
    };

  struct testlist_gexp_ast: public ast_node
    {
      enum
      {
        KIND = Kind_testlist_gexp
      };

      test_list_gexp_ast *test_list_gexp;
      gen_for_ast *gen_for;
    };

  struct testlist_safe_ast: public ast_node
    {
      enum
      {
        KIND = Kind_testlist_safe
      };

      const list_node<test_ast *> *test_sequence;
    };

  struct trailer_ast: public ast_node
    {
      enum
      {
        KIND = Kind_trailer
      };

      arglist_ast *trailer_arglist;
      subscriptlist_ast *subscriptlist;
      std::size_t tariler_dot_name;
    };

  struct try_stmt_ast: public ast_node
    {
      enum
      {
        KIND = Kind_try_stmt
      };

      suite_ast *try_suite;
      const list_node<except_clause_ast *> *except_clause_sequence;
      const list_node<suite_ast *> *except_suite_sequence;
      suite_ast *try_else_suite;
      suite_ast *finally_suite;
    };

  struct varargslist_ast: public ast_node
    {
      enum
      {
        KIND = Kind_varargslist
      };

      func_def_ast *func_def;
      fun_pos_param_ast *fun_pos_param;
    };

  struct while_stmt_ast: public ast_node
    {
      enum
      {
        KIND = Kind_while_stmt
      };

      test_ast *while_test;
      suite_ast *while_suite;
      suite_ast *while_else_suite;
    };

  struct xor_expr_ast: public ast_node
    {
      enum
      {
        KIND = Kind_xor_expr
      };

      and_expr_ast *xor_expr;
      const list_node<and_expr_ast *> *hat_xor_expr_sequence;
    };

  struct yield_stmt_ast: public ast_node
    {
      enum
      {
        KIND = Kind_yield_stmt
      };

      testlist_ast *yield_expr;
    };



} // end of namespace python

#endif


