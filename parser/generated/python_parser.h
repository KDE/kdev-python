// THIS FILE IS GENERATED
// WARNING! All changes made in this file will be lost!

#ifndef python_H_INCLUDED
#define python_H_INCLUDED

#include "python_ast.h"
#include <kdev-pg-memory-pool.h>
#include <kdev-pg-allocator.h>
#include <kdev-pg-token-stream.h>

namespace python
  {

  class parser
    {

    public:
      typedef kdev_pg_token_stream token_stream_type;
      typedef kdev_pg_token_stream::token_type token_type;
      kdev_pg_token_stream *token_stream;
      int yytoken;

      inline token_type LA(std::size_t k =  1) const
        {
          return  token_stream->token(token_stream->index() -  1 +  k -  1);
        }

      inline int yylex()
      {
        return  (yytoken =  token_stream->next_token());
      }

      inline void rewind(std::size_t index)
      {
        token_stream->rewind(index);
        yylex();
      }

      // token stream
      void set_token_stream(kdev_pg_token_stream *s)
      {
        token_stream =  s;
      }

      // error handling
      void yy_expected_symbol(int kind,  char const *name);
      void yy_expected_token(int kind,  std::size_t token,  char const *name);

      bool yy_block_errors;
      inline bool block_errors(bool block)
      {
        bool previous =  yy_block_errors;
        yy_block_errors =  block;
        return  previous;
      }

      // memory pool
      typedef kdev_pg_memory_pool memory_pool_type;

      kdev_pg_memory_pool *memory_pool;
      void set_memory_pool(kdev_pg_memory_pool *p)
      {
        memory_pool =  p;
      }

      template  <class T>
      inline T *create()
      {
        T *node =  new (memory_pool->allocate(sizeof(T))) T();
        node->kind =  T::KIND;
        return  node;
      }

      enum token_type_enum
      {
        Token_AND =  1000,
        Token_ANDD =  1001,
        Token_ANDEQ =  1002,
        Token_AS =  1003,
        Token_ASSERT =  1004,
        Token_AT =  1005,
        Token_BACKTICK =  1006,
        Token_BREAK =  1007,
        Token_CLASS =  1008,
        Token_COLON =  1009,
        Token_COMMA =  1010,
        Token_CONTINUE =  1011,
        Token_DEDENT =  1012,
        Token_DEF =  1013,
        Token_DEL =  1014,
        Token_DOT =  1015,
        Token_DOUBLESLASH =  1016,
        Token_DOUBLESLASHEQ =  1017,
        Token_DOUBLESTAR =  1018,
        Token_DOUBLESTAREQ =  1019,
        Token_ELIF =  1020,
        Token_ELLIPSIS =  1021,
        Token_ELSE =  1022,
        Token_EOF =  1023,
        Token_EQUAL =  1024,
        Token_EXCEPT =  1025,
        Token_EXEC =  1026,
        Token_FINALLY =  1027,
        Token_FLOAT =  1028,
        Token_FOR =  1029,
        Token_FROM =  1030,
        Token_GLOBAL =  1031,
        Token_GREATER =  1032,
        Token_GREATEREQ =  1033,
        Token_HAT =  1034,
        Token_IDENTIFIER =  1035,
        Token_IF =  1036,
        Token_IMAGNUM =  1037,
        Token_IMPORT =  1038,
        Token_IN =  1039,
        Token_INDENT =  1040,
        Token_INTEGER =  1041,
        Token_INVALID =  1042,
        Token_IS =  1043,
        Token_ISEQUAL =  1044,
        Token_LAMBDA =  1045,
        Token_LBRACE =  1046,
        Token_LBRACKET =  1047,
        Token_LESS =  1048,
        Token_LESSEQ =  1049,
        Token_LINEBREAK =  1050,
        Token_LONGSTRING =  1051,
        Token_LPAREN =  1052,
        Token_LSHIFT =  1053,
        Token_LSHIFTEQ =  1054,
        Token_MINUS =  1055,
        Token_MINUSEQ =  1056,
        Token_MODULO =  1057,
        Token_MODULOEQ =  1058,
        Token_NOT =  1059,
        Token_OR =  1060,
        Token_OREQ =  1061,
        Token_ORR =  1062,
        Token_PASS =  1063,
        Token_PLUS =  1064,
        Token_PLUSEQ =  1065,
        Token_PRINT =  1066,
        Token_RAISE =  1067,
        Token_RBRACE =  1068,
        Token_RBRACKET =  1069,
        Token_RETURN =  1070,
        Token_RPAREN =  1071,
        Token_RSHIFT =  1072,
        Token_RSHIFTEQ =  1073,
        Token_SEMICOLON =  1074,
        Token_SHORTSTRING =  1075,
        Token_SLASH =  1076,
        Token_SLASHEQ =  1077,
        Token_STAR =  1078,
        Token_STAREQ =  1079,
        Token_STRINGBODY =  1080,
        Token_STRINGLITERAL =  1081,
        Token_TILDE =  1082,
        Token_TILDEEQ =  1083,
        Token_TRY =  1084,
        Token_UNEQUAL =  1085,
        Token_WHILE =  1086,
        Token_YIELD =  1087,
        token_type_size
      }; // token_type_enum

      // user defined declarations:

    public:

      /**
       * Transform the raw input into tokens.
       * When this method returns, the parser's token stream has been filled
       * and any parse_*() method can be called.
       */
      void tokenize( char *contents );

      enum problem_type {
        error,
        warning,
        info
      };
      void report_problem( parser::problem_type type,  const char* message );
      void report_problem( parser::problem_type type,  std::string message );
      char* tokenText(std::size_t begin);


    private:

      char* m_contents;


    public:
      parser()
      {
        memory_pool =  0;
        token_stream =  0;
        yytoken =  Token_EOF;
        yy_block_errors =  false;
      }

      virtual ~parser()
      {}

      bool parse_and_expr(and_expr_ast **yynode);
      bool parse_and_test(and_test_ast **yynode);
      bool parse_arg_list(arg_list_ast **yynode);
      bool parse_arglist(arglist_ast **yynode);
      bool parse_argument(argument_ast **yynode);
      bool parse_arith_expr(arith_expr_ast **yynode);
      bool parse_arith_op(arith_op_ast **yynode);
      bool parse_assert_stmt(assert_stmt_ast **yynode);
      bool parse_atom(atom_ast **yynode);
      bool parse_augassign(augassign_ast **yynode);
      bool parse_break_stmt(break_stmt_ast **yynode);
      bool parse_classdef(classdef_ast **yynode);
      bool parse_comp_op(comp_op_ast **yynode);
      bool parse_comparison(comparison_ast **yynode);
      bool parse_compound_stmt(compound_stmt_ast **yynode);
      bool parse_continue_stmt(continue_stmt_ast **yynode);
      bool parse_decorator(decorator_ast **yynode);
      bool parse_decorators(decorators_ast **yynode);
      bool parse_del_stmt(del_stmt_ast **yynode);
      bool parse_dictmaker(dictmaker_ast **yynode);
      bool parse_dotted_as_name(dotted_as_name_ast **yynode);
      bool parse_dotted_as_names(dotted_as_names_ast **yynode);
      bool parse_dotted_name(dotted_name_ast **yynode);
      bool parse_except_clause(except_clause_ast **yynode);
      bool parse_exec_stmt(exec_stmt_ast **yynode);
      bool parse_expr(expr_ast **yynode);
      bool parse_expr_stmt(expr_stmt_ast **yynode);
      bool parse_exprlist(exprlist_ast **yynode);
      bool parse_fact_op(fact_op_ast **yynode);
      bool parse_factor(factor_ast **yynode);
      bool parse_flow_stmt(flow_stmt_ast **yynode);
      bool parse_for_stmt(for_stmt_ast **yynode);
      bool parse_fp_def(fp_def_ast **yynode);
      bool parse_fpdef(fpdef_ast **yynode);
      bool parse_fplist(fplist_ast **yynode);
      bool parse_fun_pos_param(fun_pos_param_ast **yynode);
      bool parse_func_def(func_def_ast **yynode);
      bool parse_funcdef(funcdef_ast **yynode);
      bool parse_gen_for(gen_for_ast **yynode);
      bool parse_gen_if(gen_if_ast **yynode);
      bool parse_gen_iter(gen_iter_ast **yynode);
      bool parse_global_stmt(global_stmt_ast **yynode);
      bool parse_if_stmt(if_stmt_ast **yynode);
      bool parse_import_as_name(import_as_name_ast **yynode);
      bool parse_import_as_names(import_as_names_ast **yynode);
      bool parse_import_from(import_from_ast **yynode);
      bool parse_import_name(import_name_ast **yynode);
      bool parse_import_stmt(import_stmt_ast **yynode);
      bool parse_lambda_def(lambda_def_ast **yynode);
      bool parse_list_for(list_for_ast **yynode);
      bool parse_list_if(list_if_ast **yynode);
      bool parse_list_iter(list_iter_ast **yynode);
      bool parse_list_maker(list_maker_ast **yynode);
      bool parse_listmaker(listmaker_ast **yynode);
      bool parse_longstringliteral(longstringliteral_ast **yynode);
      bool parse_not_test(not_test_ast **yynode);
      bool parse_number(number_ast **yynode);
      bool parse_pass_stmt(pass_stmt_ast **yynode);
      bool parse_power(power_ast **yynode);
      bool parse_print_stmt(print_stmt_ast **yynode);
      bool parse_project(project_ast **yynode);
      bool parse_raise_stmt(raise_stmt_ast **yynode);
      bool parse_return_stmt(return_stmt_ast **yynode);
      bool parse_shift_expr(shift_expr_ast **yynode);
      bool parse_shift_op(shift_op_ast **yynode);
      bool parse_shortstringliteral(shortstringliteral_ast **yynode);
      bool parse_simple_stmt(simple_stmt_ast **yynode);
      bool parse_sliceop(sliceop_ast **yynode);
      bool parse_small_stmt(small_stmt_ast **yynode);
      bool parse_stmt(stmt_ast **yynode);
      bool parse_subscript(subscript_ast **yynode);
      bool parse_subscriptlist(subscriptlist_ast **yynode);
      bool parse_suite(suite_ast **yynode);
      bool parse_term(term_ast **yynode);
      bool parse_term_op(term_op_ast **yynode);
      bool parse_test(test_ast **yynode);
      bool parse_test_list_gexp(test_list_gexp_ast **yynode);
      bool parse_testlist(testlist_ast **yynode);
      bool parse_testlist1(testlist1_ast **yynode);
      bool parse_testlist_gexp(testlist_gexp_ast **yynode);
      bool parse_testlist_safe(testlist_safe_ast **yynode);
      bool parse_trailer(trailer_ast **yynode);
      bool parse_try_stmt(try_stmt_ast **yynode);
      bool parse_varargslist(varargslist_ast **yynode);
      bool parse_while_stmt(while_stmt_ast **yynode);
      bool parse_xor_expr(xor_expr_ast **yynode);
      bool parse_yield_stmt(yield_stmt_ast **yynode);
    };

} // end of namespace python

#endif


