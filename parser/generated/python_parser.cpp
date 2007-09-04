// THIS FILE IS GENERATED
// WARNING! All changes made in this file will be lost!

#include "python_parser.h"


#include "pythonlexer.h"
#include <QtCore/QDebug>

namespace Python
  {

  void parser::tokenize( const QString& contents )
  {
    m_contents =  contents;
    Lexer lexer( this,  contents );
    int kind =  parser::Token_EOF;

    do
      {
        kind =  lexer.nextTokenKind();

        if  ( !kind ) // when the lexer returns 0, the end of file is reached
          {
            parser::token_type &tt =  this->token_stream->next();
            tt.kind =  parser::Token_LINEBREAK;
            tt.begin =  lexer.tokenBegin();
            tt.end =  lexer.tokenEnd();
            kind =  parser::Token_EOF;
          }
        parser::token_type &t =  this->token_stream->next();
        t.begin =  lexer.tokenBegin();
        t.end =  lexer.tokenEnd();
        t.kind =  kind;

        if ( m_debug )
          qDebug() <<  kind <<  tokenText(t.begin, t.end) <<  t.begin <<  t.end;
      }

    while  ( kind !=  parser::Token_EOF );

    this->yylex(); // produce the look ahead token
  }


  QString parser::tokenText(std::size_t begin,  std::size_t end)
  {
    return  m_contents.mid(begin, end - begin + 1);
  }


  void parser::reportProblem( parser::ProblemType type,  const QString& message )
  {
    if  (type ==  Error)
      qDebug() <<  "** ERROR:" <<  message;
    else if  (type ==  Warning)
      qDebug() <<  "** WARNING:" <<  message;
    else if  (type ==  Info)
      qDebug() <<  "** Info:" <<  message;
  }


  // custom error recovery
  void parser::yy_expected_token(int /*expected*/,  std::size_t /*where*/,  char const *name)
  {
    reportProblem( parser::Error,  QString("Expected token \"%1\"").arg(name));
  }

  void parser::yy_expected_symbol(int /*expected_symbol*/,  char const *name)
  {
    std::size_t line;
    std::size_t col;
    size_t index =  token_stream->index() - 1;
    token_type &token =  token_stream->token(index);
    qDebug() <<  "token starts at:" <<  token.begin;
    qDebug() <<  "index is:" <<  index;
    token_stream->start_position(index,  &line,  &col);
    QString tokenValue =  tokenText(token.begin,  token.end);
    reportProblem( parser::Error,
                   QString("Expected symbol \"%1\" (current token: \"%2\" [%3] at line: %4 col: %5)")
                   .arg(name)
                   .arg(token.kind !=  0 ?  tokenValue :  "EOF")
                   .arg(token.kind)
                   .arg(line)
                   .arg(col));
  }

  void parser::setDebug( bool debug )
  {
    m_debug =  debug;
  }



} // end of namespace cool


namespace Python
  {

  bool parser::parse_and_expr(and_expr_ast **yynode)
  {
    *yynode =  create<and_expr_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_STRINGLITERAL
         ||  yytoken ==  Token_IDENTIFIER
         ||  yytoken ==  Token_INTEGER
         ||  yytoken ==  Token_FLOAT
         ||  yytoken ==  Token_IMAGNUM
         ||  yytoken ==  Token_LPAREN
         ||  yytoken ==  Token_LBRACE
         ||  yytoken ==  Token_LBRACKET
         ||  yytoken ==  Token_BACKTICK
         ||  yytoken ==  Token_PLUS
         ||  yytoken ==  Token_MINUS
         ||  yytoken ==  Token_TILDE)
      {
        shift_expr_ast *__node_0 =  0;

        if  (!parse_shift_expr(&__node_0))
          {
            yy_expected_symbol(ast_node::Kind_shift_expr,  "shift_expr");
            return  false;
          }

        (*yynode)->and_expr =  __node_0;

        while  (yytoken ==  Token_ANDD)
          {
            if  (yytoken !=  Token_ANDD)
              {
                yy_expected_token(yytoken,  Token_ANDD,  "andd");
                return  false;
              }

            yylex();

            shift_expr_ast *__node_1 =  0;

            if  (!parse_shift_expr(&__node_1))
              {
                yy_expected_symbol(ast_node::Kind_shift_expr,  "shift_expr");
                return  false;
              }

            (*yynode)->andd_shif_expr_sequence =  snoc((*yynode)->andd_shif_expr_sequence,  __node_1,  memory_pool);

          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_and_test(and_test_ast **yynode)
  {
    *yynode =  create<and_test_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_NOT
         ||  yytoken ==  Token_STRINGLITERAL
         ||  yytoken ==  Token_IDENTIFIER
         ||  yytoken ==  Token_INTEGER
         ||  yytoken ==  Token_FLOAT
         ||  yytoken ==  Token_IMAGNUM
         ||  yytoken ==  Token_LPAREN
         ||  yytoken ==  Token_LBRACE
         ||  yytoken ==  Token_LBRACKET
         ||  yytoken ==  Token_BACKTICK
         ||  yytoken ==  Token_PLUS
         ||  yytoken ==  Token_MINUS
         ||  yytoken ==  Token_TILDE)
      {
        not_test_ast *__node_2 =  0;

        if  (!parse_not_test(&__node_2))
          {
            yy_expected_symbol(ast_node::Kind_not_test,  "not_test");
            return  false;
          }

        (*yynode)->not_test_sequence =  snoc((*yynode)->not_test_sequence,  __node_2,  memory_pool);

        while  (yytoken ==  Token_AND)
          {
            if  (yytoken !=  Token_AND)
              {
                yy_expected_token(yytoken,  Token_AND,  "and");
                return  false;
              }

            yylex();

            not_test_ast *__node_3 =  0;

            if  (!parse_not_test(&__node_3))
              {
                yy_expected_symbol(ast_node::Kind_not_test,  "not_test");
                return  false;
              }

            (*yynode)->not_test_sequence =  snoc((*yynode)->not_test_sequence,  __node_3,  memory_pool);

          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_arg_list(arg_list_ast **yynode)
  {
    *yynode =  create<arg_list_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_LAMBDA
         ||  yytoken ==  Token_NOT
         ||  yytoken ==  Token_STRINGLITERAL
         ||  yytoken ==  Token_IDENTIFIER
         ||  yytoken ==  Token_INTEGER
         ||  yytoken ==  Token_FLOAT
         ||  yytoken ==  Token_IMAGNUM
         ||  yytoken ==  Token_LPAREN
         ||  yytoken ==  Token_LBRACE
         ||  yytoken ==  Token_LBRACKET
         ||  yytoken ==  Token_BACKTICK
         ||  yytoken ==  Token_PLUS
         ||  yytoken ==  Token_MINUS
         ||  yytoken ==  Token_TILDE)
      {
        argument_ast *__node_4 =  0;

        if  (!parse_argument(&__node_4))
          {
            yy_expected_symbol(ast_node::Kind_argument,  "argument");
            return  false;
          }

        (*yynode)->argument_sequence =  snoc((*yynode)->argument_sequence,  __node_4,  memory_pool);

        while  (yytoken ==  Token_COMMA)
          {
            if  (yytoken !=  Token_COMMA)
              {
                yy_expected_token(yytoken,  Token_COMMA,  "comma");
                return  false;
              }

            yylex();

            if (yytoken ==  Token_RPAREN ||  yytoken ==  Token_STAR ||  yytoken ==  Token_DOUBLESTAR)
              {
                break;
              }

            argument_ast *__node_5 =  0;

            if  (!parse_argument(&__node_5))
              {
                yy_expected_symbol(ast_node::Kind_argument,  "argument");
                return  false;
              }

            (*yynode)->argument_sequence =  snoc((*yynode)->argument_sequence,  __node_5,  memory_pool);

          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_arglist(arglist_ast **yynode)
  {
    *yynode =  create<arglist_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_LAMBDA
         ||  yytoken ==  Token_NOT
         ||  yytoken ==  Token_STRINGLITERAL
         ||  yytoken ==  Token_IDENTIFIER
         ||  yytoken ==  Token_INTEGER
         ||  yytoken ==  Token_FLOAT
         ||  yytoken ==  Token_IMAGNUM
         ||  yytoken ==  Token_LPAREN
         ||  yytoken ==  Token_LBRACE
         ||  yytoken ==  Token_LBRACKET
         ||  yytoken ==  Token_BACKTICK
         ||  yytoken ==  Token_STAR
         ||  yytoken ==  Token_DOUBLESTAR
         ||  yytoken ==  Token_PLUS
         ||  yytoken ==  Token_MINUS
         ||  yytoken ==  Token_TILDE ||  yytoken ==  Token_RPAREN)
      {
        if  (yytoken ==  Token_LAMBDA
             ||  yytoken ==  Token_NOT
             ||  yytoken ==  Token_STRINGLITERAL
             ||  yytoken ==  Token_IDENTIFIER
             ||  yytoken ==  Token_INTEGER
             ||  yytoken ==  Token_FLOAT
             ||  yytoken ==  Token_IMAGNUM
             ||  yytoken ==  Token_LPAREN
             ||  yytoken ==  Token_LBRACE
             ||  yytoken ==  Token_LBRACKET
             ||  yytoken ==  Token_BACKTICK
             ||  yytoken ==  Token_PLUS
             ||  yytoken ==  Token_MINUS
             ||  yytoken ==  Token_TILDE)
          {
            arg_list_ast *__node_6 =  0;

            if  (!parse_arg_list(&__node_6))
              {
                yy_expected_symbol(ast_node::Kind_arg_list,  "arg_list");
                return  false;
              }

            (*yynode)->arg_list =  __node_6;

          }

        else if  (true /*epsilon*/)
        {}
        else
          {
            return  false;
          }

        if  (yytoken ==  Token_STAR)
          {
            if  (yytoken !=  Token_STAR)
              {
                yy_expected_token(yytoken,  Token_STAR,  "star");
                return  false;
              }

            yylex();

            test_ast *__node_7 =  0;

            if  (!parse_test(&__node_7))
              {
                yy_expected_symbol(ast_node::Kind_test,  "test");
                return  false;
              }

            (*yynode)->arglist_star =  __node_7;

            if  ((yytoken ==  Token_COMMA) &&  ( LA(1).kind !=  Token_RPAREN ))
              {
                if  (yytoken !=  Token_COMMA)
                  {
                    yy_expected_token(yytoken,  Token_COMMA,  "comma");
                    return  false;
                  }

                yylex();

                if  (yytoken !=  Token_DOUBLESTAR)
                  {
                    yy_expected_token(yytoken,  Token_DOUBLESTAR,  "doublestar");
                    return  false;
                  }

                yylex();

                test_ast *__node_8 =  0;

                if  (!parse_test(&__node_8))
                  {
                    yy_expected_symbol(ast_node::Kind_test,  "test");
                    return  false;
                  }

                (*yynode)->arglist_doublestar =  __node_8;

              }

            else if  (true /*epsilon*/)
            {}
            else
              {
                return  false;
              }
          }

        else if  (yytoken ==  Token_DOUBLESTAR)
          {
            if  (yytoken !=  Token_DOUBLESTAR)
              {
                yy_expected_token(yytoken,  Token_DOUBLESTAR,  "doublestar");
                return  false;
              }

            yylex();

            test_ast *__node_9 =  0;

            if  (!parse_test(&__node_9))
              {
                yy_expected_symbol(ast_node::Kind_test,  "test");
                return  false;
              }

            (*yynode)->arglist_doublestar =  __node_9;

          }

        else if  (true /*epsilon*/)
        {}
        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_argument(argument_ast **yynode)
  {
    *yynode =  create<argument_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_LAMBDA
         ||  yytoken ==  Token_NOT
         ||  yytoken ==  Token_STRINGLITERAL
         ||  yytoken ==  Token_IDENTIFIER
         ||  yytoken ==  Token_INTEGER
         ||  yytoken ==  Token_FLOAT
         ||  yytoken ==  Token_IMAGNUM
         ||  yytoken ==  Token_LPAREN
         ||  yytoken ==  Token_LBRACE
         ||  yytoken ==  Token_LBRACKET
         ||  yytoken ==  Token_BACKTICK
         ||  yytoken ==  Token_PLUS
         ||  yytoken ==  Token_MINUS
         ||  yytoken ==  Token_TILDE)
      {
        test_ast *__node_10 =  0;

        if  (!parse_test(&__node_10))
          {
            yy_expected_symbol(ast_node::Kind_test,  "test");
            return  false;
          }

        (*yynode)->argument_test =  __node_10;

        if  (yytoken ==  Token_EQUAL)
          {
            if  (yytoken !=  Token_EQUAL)
              {
                yy_expected_token(yytoken,  Token_EQUAL,  "equal");
                return  false;
              }

            yylex();

            test_ast *__node_11 =  0;

            if  (!parse_test(&__node_11))
              {
                yy_expected_symbol(ast_node::Kind_test,  "test");
                return  false;
              }

            (*yynode)->argument_equal_test =  __node_11;

            if  ((yytoken ==  Token_LPAREN) &&  ( LA(2).kind ==  Token_FOR ))
              {
                if  (yytoken !=  Token_LPAREN)
                  {
                    yy_expected_token(yytoken,  Token_LPAREN,  "lparen");
                    return  false;
                  }

                yylex();

                gen_for_ast *__node_12 =  0;

                if  (!parse_gen_for(&__node_12))
                  {
                    yy_expected_symbol(ast_node::Kind_gen_for,  "gen_for");
                    return  false;
                  }

                (*yynode)->gen_for =  __node_12;

                if  (yytoken !=  Token_RPAREN)
                  {
                    yy_expected_token(yytoken,  Token_RPAREN,  "rparen");
                    return  false;
                  }

                yylex();

              }

            else if  (true /*epsilon*/)
            {}
            else
              {
                return  false;
              }
          }

        else if  ((yytoken ==  Token_FOR) &&  ( yytoken ==  Token_FOR ))
          {
            gen_for_ast *__node_13 =  0;

            if  (!parse_gen_for(&__node_13))
              {
                yy_expected_symbol(ast_node::Kind_gen_for,  "gen_for");
                return  false;
              }

            (*yynode)->gen_for =  __node_13;

          }

        else if  ((true /*epsilon*/) &&  ( yytoken ==  Token_RPAREN ||  yytoken ==  Token_STAR ||  yytoken ==  Token_DOUBLESTAR ||  yytoken ==  Token_COMMA ))
        {}
        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_arith_expr(arith_expr_ast **yynode)
  {
    *yynode =  create<arith_expr_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_STRINGLITERAL
         ||  yytoken ==  Token_IDENTIFIER
         ||  yytoken ==  Token_INTEGER
         ||  yytoken ==  Token_FLOAT
         ||  yytoken ==  Token_IMAGNUM
         ||  yytoken ==  Token_LPAREN
         ||  yytoken ==  Token_LBRACE
         ||  yytoken ==  Token_LBRACKET
         ||  yytoken ==  Token_BACKTICK
         ||  yytoken ==  Token_PLUS
         ||  yytoken ==  Token_MINUS
         ||  yytoken ==  Token_TILDE)
      {
        term_ast *__node_14 =  0;

        if  (!parse_term(&__node_14))
          {
            yy_expected_symbol(ast_node::Kind_term,  "term");
            return  false;
          }

        (*yynode)->arith_term =  __node_14;

        if  (yytoken ==  Token_PLUS
             ||  yytoken ==  Token_MINUS)
          {
            do
              {
                arith_op_ast *__node_15 =  0;

                if  (!parse_arith_op(&__node_15))
                  {
                    yy_expected_symbol(ast_node::Kind_arith_op,  "arith_op");
                    return  false;
                  }

                (*yynode)->arith_op_list_sequence =  snoc((*yynode)->arith_op_list_sequence,  __node_15,  memory_pool);

                term_ast *__node_16 =  0;

                if  (!parse_term(&__node_16))
                  {
                    yy_expected_symbol(ast_node::Kind_term,  "term");
                    return  false;
                  }

                (*yynode)->arith_term_list_sequence =  snoc((*yynode)->arith_term_list_sequence,  __node_16,  memory_pool);

              }

            while  (yytoken ==  Token_PLUS
                    ||  yytoken ==  Token_MINUS);
          }

        else if  (true /*epsilon*/)
        {}
        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_arith_op(arith_op_ast **yynode)
  {
    *yynode =  create<arith_op_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_PLUS
         ||  yytoken ==  Token_MINUS)
      {
        if  (yytoken ==  Token_PLUS)
          {
            if  (yytoken !=  Token_PLUS)
              {
                yy_expected_token(yytoken,  Token_PLUS,  "plus");
                return  false;
              }

            yylex();

            (*yynode)->arith_operator =  Python::op_plus;
          }

        else if  (yytoken ==  Token_MINUS)
          {
            if  (yytoken !=  Token_MINUS)
              {
                yy_expected_token(yytoken,  Token_MINUS,  "minus");
                return  false;
              }

            yylex();

            (*yynode)->arith_operator =  Python::op_minus;
          }

        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_assert_stmt(assert_stmt_ast **yynode)
  {
    *yynode =  create<assert_stmt_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_ASSERT)
      {
        if  (yytoken !=  Token_ASSERT)
          {
            yy_expected_token(yytoken,  Token_ASSERT,  "assert");
            return  false;
          }

        yylex();

        test_ast *__node_17 =  0;

        if  (!parse_test(&__node_17))
          {
            yy_expected_symbol(ast_node::Kind_test,  "test");
            return  false;
          }

        (*yynode)->assert_not_test =  __node_17;

        if  (yytoken ==  Token_COMMA)
          {
            if  (yytoken !=  Token_COMMA)
              {
                yy_expected_token(yytoken,  Token_COMMA,  "comma");
                return  false;
              }

            yylex();

            test_ast *__node_18 =  0;

            if  (!parse_test(&__node_18))
              {
                yy_expected_symbol(ast_node::Kind_test,  "test");
                return  false;
              }

            (*yynode)->assert_raise_test =  __node_18;

          }

        else if  (true /*epsilon*/)
        {}
        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_atom(atom_ast **yynode)
  {
    *yynode =  create<atom_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_STRINGLITERAL
         ||  yytoken ==  Token_IDENTIFIER
         ||  yytoken ==  Token_INTEGER
         ||  yytoken ==  Token_FLOAT
         ||  yytoken ==  Token_IMAGNUM
         ||  yytoken ==  Token_LPAREN
         ||  yytoken ==  Token_LBRACE
         ||  yytoken ==  Token_LBRACKET
         ||  yytoken ==  Token_BACKTICK)
      {
        if  (yytoken ==  Token_LPAREN)
          {
            if  (yytoken !=  Token_LPAREN)
              {
                yy_expected_token(yytoken,  Token_LPAREN,  "lparen");
                return  false;
              }

            yylex();

            if  (yytoken ==  Token_LAMBDA
                 ||  yytoken ==  Token_NOT
                 ||  yytoken ==  Token_STRINGLITERAL
                 ||  yytoken ==  Token_IDENTIFIER
                 ||  yytoken ==  Token_INTEGER
                 ||  yytoken ==  Token_FLOAT
                 ||  yytoken ==  Token_IMAGNUM
                 ||  yytoken ==  Token_LPAREN
                 ||  yytoken ==  Token_LBRACE
                 ||  yytoken ==  Token_LBRACKET
                 ||  yytoken ==  Token_BACKTICK
                 ||  yytoken ==  Token_PLUS
                 ||  yytoken ==  Token_MINUS
                 ||  yytoken ==  Token_TILDE)
              {
                testlist_gexp_ast *__node_19 =  0;

                if  (!parse_testlist_gexp(&__node_19))
                  {
                    yy_expected_symbol(ast_node::Kind_testlist_gexp,  "testlist_gexp");
                    return  false;
                  }

                (*yynode)->testlist_gexp =  __node_19;

              }

            else if  (true /*epsilon*/)
            {}
            else
              {
                return  false;
              }

            if  (yytoken !=  Token_RPAREN)
              {
                yy_expected_token(yytoken,  Token_RPAREN,  "rparen");
                return  false;
              }

            yylex();

          }

        else if  (yytoken ==  Token_LBRACKET)
          {
            if  (yytoken !=  Token_LBRACKET)
              {
                yy_expected_token(yytoken,  Token_LBRACKET,  "lbracket");
                return  false;
              }

            yylex();

            listmaker_ast *__node_20 =  0;

            if  (!parse_listmaker(&__node_20))
              {
                yy_expected_symbol(ast_node::Kind_listmaker,  "listmaker");
                return  false;
              }

            (*yynode)->listmaker =  __node_20;

            if  (yytoken !=  Token_RBRACKET)
              {
                yy_expected_token(yytoken,  Token_RBRACKET,  "rbracket");
                return  false;
              }

            yylex();

          }

        else if  (yytoken ==  Token_LBRACE)
          {
            if  (yytoken !=  Token_LBRACE)
              {
                yy_expected_token(yytoken,  Token_LBRACE,  "lbrace");
                return  false;
              }

            yylex();

            dictmaker_ast *__node_21 =  0;

            if  (!parse_dictmaker(&__node_21))
              {
                yy_expected_symbol(ast_node::Kind_dictmaker,  "dictmaker");
                return  false;
              }

            (*yynode)->dictmaker =  __node_21;

            if  (yytoken !=  Token_RBRACE)
              {
                yy_expected_token(yytoken,  Token_RBRACE,  "rbrace");
                return  false;
              }

            yylex();

          }

        else if  (yytoken ==  Token_BACKTICK)
          {
            if  (yytoken !=  Token_BACKTICK)
              {
                yy_expected_token(yytoken,  Token_BACKTICK,  "backtick");
                return  false;
              }

            yylex();

            testlist1_ast *__node_22 =  0;

            if  (!parse_testlist1(&__node_22))
              {
                yy_expected_symbol(ast_node::Kind_testlist1,  "testlist1");
                return  false;
              }

            (*yynode)->testlist1 =  __node_22;

            if  (yytoken !=  Token_BACKTICK)
              {
                yy_expected_token(yytoken,  Token_BACKTICK,  "backtick");
                return  false;
              }

            yylex();

          }

        else if  (yytoken ==  Token_IDENTIFIER)
          {
            if  (yytoken !=  Token_IDENTIFIER)
              {
                yy_expected_token(yytoken,  Token_IDENTIFIER,  "identifier");
                return  false;
              }

            (*yynode)->atom_identifier_name =  token_stream->index() -  1;
            yylex();

          }

        else if  (yytoken ==  Token_INTEGER
                  ||  yytoken ==  Token_FLOAT
                  ||  yytoken ==  Token_IMAGNUM)
          {
            number_ast *__node_23 =  0;

            if  (!parse_number(&__node_23))
              {
                yy_expected_symbol(ast_node::Kind_number,  "number");
                return  false;
              }

            (*yynode)->number =  __node_23;

          }

        else if  (yytoken ==  Token_STRINGLITERAL)
          {
            do
              {
                if  (yytoken !=  Token_STRINGLITERAL)
                  {
                    yy_expected_token(yytoken,  Token_STRINGLITERAL,  "stringliteral");
                    return  false;
                  }

                (*yynode)->stringliteral_sequence =  snoc((*yynode)->stringliteral_sequence,  token_stream->index() -  1,  memory_pool);
                yylex();

              }

            while  (yytoken ==  Token_STRINGLITERAL);
          }

        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_augassign(augassign_ast **yynode)
  {
    *yynode =  create<augassign_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_PLUSEQ
         ||  yytoken ==  Token_MINUSEQ
         ||  yytoken ==  Token_SLASHEQ
         ||  yytoken ==  Token_DOUBLESLASHEQ
         ||  yytoken ==  Token_MODULOEQ
         ||  yytoken ==  Token_ANDEQ
         ||  yytoken ==  Token_STAREQ
         ||  yytoken ==  Token_DOUBLESTAREQ
         ||  yytoken ==  Token_LSHIFTEQ
         ||  yytoken ==  Token_RSHIFTEQ
         ||  yytoken ==  Token_TILDEEQ
         ||  yytoken ==  Token_OREQ)
      {
        if  (yytoken ==  Token_PLUSEQ)
          {
            if  (yytoken !=  Token_PLUSEQ)
              {
                yy_expected_token(yytoken,  Token_PLUSEQ,  "pluseq");
                return  false;
              }

            yylex();

            (*yynode)->augassign_eq =  Python::eq_plus;
          }

        else if  (yytoken ==  Token_MINUSEQ)
          {
            if  (yytoken !=  Token_MINUSEQ)
              {
                yy_expected_token(yytoken,  Token_MINUSEQ,  "minuseq");
                return  false;
              }

            yylex();

            (*yynode)->augassign_eq =  Python::eq_minus;
          }

        else if  (yytoken ==  Token_STAREQ)
          {
            if  (yytoken !=  Token_STAREQ)
              {
                yy_expected_token(yytoken,  Token_STAREQ,  "stareq");
                return  false;
              }

            yylex();

            (*yynode)->augassign_eq =  Python::eq_star;
          }

        else if  (yytoken ==  Token_SLASHEQ)
          {
            if  (yytoken !=  Token_SLASHEQ)
              {
                yy_expected_token(yytoken,  Token_SLASHEQ,  "slasheq");
                return  false;
              }

            yylex();

            (*yynode)->augassign_eq =  Python::eq_slash;
          }

        else if  (yytoken ==  Token_MODULOEQ)
          {
            if  (yytoken !=  Token_MODULOEQ)
              {
                yy_expected_token(yytoken,  Token_MODULOEQ,  "moduloeq");
                return  false;
              }

            yylex();

            (*yynode)->augassign_eq =  Python::eq_modulo;
          }

        else if  (yytoken ==  Token_ANDEQ)
          {
            if  (yytoken !=  Token_ANDEQ)
              {
                yy_expected_token(yytoken,  Token_ANDEQ,  "andeq");
                return  false;
              }

            yylex();

            (*yynode)->augassign_eq =  Python::eq_and;
          }

        else if  (yytoken ==  Token_OREQ)
          {
            if  (yytoken !=  Token_OREQ)
              {
                yy_expected_token(yytoken,  Token_OREQ,  "oreq");
                return  false;
              }

            yylex();

            (*yynode)->augassign_eq =  Python::eq_or;
          }

        else if  (yytoken ==  Token_TILDEEQ)
          {
            if  (yytoken !=  Token_TILDEEQ)
              {
                yy_expected_token(yytoken,  Token_TILDEEQ,  "tildeeq");
                return  false;
              }

            yylex();

            (*yynode)->augassign_eq =  Python::eq_tilde;
          }

        else if  (yytoken ==  Token_LSHIFTEQ)
          {
            if  (yytoken !=  Token_LSHIFTEQ)
              {
                yy_expected_token(yytoken,  Token_LSHIFTEQ,  "lshifteq");
                return  false;
              }

            yylex();

            (*yynode)->augassign_eq =  Python::eq_lshift;
          }

        else if  (yytoken ==  Token_RSHIFTEQ)
          {
            if  (yytoken !=  Token_RSHIFTEQ)
              {
                yy_expected_token(yytoken,  Token_RSHIFTEQ,  "rshifteq");
                return  false;
              }

            yylex();

            (*yynode)->augassign_eq =  Python::eq_rshift;
          }

        else if  (yytoken ==  Token_DOUBLESTAREQ)
          {
            if  (yytoken !=  Token_DOUBLESTAREQ)
              {
                yy_expected_token(yytoken,  Token_DOUBLESTAREQ,  "doublestareq");
                return  false;
              }

            yylex();

            (*yynode)->augassign_eq =  Python::eq_doublestar;
          }

        else if  (yytoken ==  Token_DOUBLESLASHEQ)
          {
            if  (yytoken !=  Token_DOUBLESLASHEQ)
              {
                yy_expected_token(yytoken,  Token_DOUBLESLASHEQ,  "doubleslasheq");
                return  false;
              }

            yylex();

            (*yynode)->augassign_eq =  Python::eq_doubleslash;
          }

        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_break_stmt(break_stmt_ast **yynode)
  {
    *yynode =  create<break_stmt_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_BREAK)
      {
        if  (yytoken !=  Token_BREAK)
          {
            yy_expected_token(yytoken,  Token_BREAK,  "break");
            return  false;
          }

        yylex();

      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_classdef(classdef_ast **yynode)
  {
    *yynode =  create<classdef_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_CLASS)
      {
        if  (yytoken !=  Token_CLASS)
          {
            yy_expected_token(yytoken,  Token_CLASS,  "class");
            return  false;
          }

        yylex();

        if  (yytoken !=  Token_IDENTIFIER)
          {
            yy_expected_token(yytoken,  Token_IDENTIFIER,  "identifier");
            return  false;
          }

        (*yynode)->class_name =  token_stream->index() -  1;
        yylex();

        if  (yytoken ==  Token_LPAREN)
          {
            if  (yytoken !=  Token_LPAREN)
              {
                yy_expected_token(yytoken,  Token_LPAREN,  "lparen");
                return  false;
              }

            yylex();

            testlist_ast *__node_24 =  0;

            if  (!parse_testlist(&__node_24))
              {
                yy_expected_symbol(ast_node::Kind_testlist,  "testlist");
                return  false;
              }

            (*yynode)->testlist =  __node_24;

            if  (yytoken !=  Token_RPAREN)
              {
                yy_expected_token(yytoken,  Token_RPAREN,  "rparen");
                return  false;
              }

            yylex();

          }

        else if  (true /*epsilon*/)
        {}
        else
          {
            return  false;
          }

        if  (yytoken !=  Token_COLON)
          {
            yy_expected_token(yytoken,  Token_COLON,  "colon");
            return  false;
          }

        yylex();

        suite_ast *__node_25 =  0;

        if  (!parse_suite(&__node_25))
          {
            yy_expected_symbol(ast_node::Kind_suite,  "suite");
            return  false;
          }

        (*yynode)->class_suite =  __node_25;

      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_comp_op(comp_op_ast **yynode)
  {
    *yynode =  create<comp_op_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_IS
         ||  yytoken ==  Token_NOT
         ||  yytoken ==  Token_IN
         ||  yytoken ==  Token_LESS
         ||  yytoken ==  Token_GREATER
         ||  yytoken ==  Token_GREATEREQ
         ||  yytoken ==  Token_LESSEQ
         ||  yytoken ==  Token_UNEQUAL
         ||  yytoken ==  Token_ISEQUAL)
      {
        if  (yytoken ==  Token_LESS)
          {
            if  (yytoken !=  Token_LESS)
              {
                yy_expected_token(yytoken,  Token_LESS,  "less");
                return  false;
              }

            yylex();

            (*yynode)->comp_operator =  Python::op_less;
          }

        else if  (yytoken ==  Token_GREATER)
          {
            if  (yytoken !=  Token_GREATER)
              {
                yy_expected_token(yytoken,  Token_GREATER,  "greater");
                return  false;
              }

            yylex();

            (*yynode)->comp_operator =  Python::op_greater;
          }

        else if  (yytoken ==  Token_ISEQUAL)
          {
            if  (yytoken !=  Token_ISEQUAL)
              {
                yy_expected_token(yytoken,  Token_ISEQUAL,  "isequal");
                return  false;
              }

            yylex();

            (*yynode)->comp_operator =  Python::op_isequal;
          }

        else if  (yytoken ==  Token_GREATEREQ)
          {
            if  (yytoken !=  Token_GREATEREQ)
              {
                yy_expected_token(yytoken,  Token_GREATEREQ,  "greatereq");
                return  false;
              }

            yylex();

            (*yynode)->comp_operator =  Python::op_greatereq;
          }

        else if  (yytoken ==  Token_LESSEQ)
          {
            if  (yytoken !=  Token_LESSEQ)
              {
                yy_expected_token(yytoken,  Token_LESSEQ,  "lesseq");
                return  false;
              }

            yylex();

            (*yynode)->comp_operator =  Python::op_lesseq;
          }

        else if  (yytoken ==  Token_UNEQUAL)
          {
            if  (yytoken !=  Token_UNEQUAL)
              {
                yy_expected_token(yytoken,  Token_UNEQUAL,  "unequal");
                return  false;
              }

            yylex();

            (*yynode)->comp_operator =  Python::op_unequal;
          }

        else if  (yytoken ==  Token_IN)
          {
            if  (yytoken !=  Token_IN)
              {
                yy_expected_token(yytoken,  Token_IN,  "in");
                return  false;
              }

            yylex();

            (*yynode)->comp_operator =  Python::op_in;
          }

        else if  (yytoken ==  Token_NOT)
          {
            if  (yytoken !=  Token_NOT)
              {
                yy_expected_token(yytoken,  Token_NOT,  "not");
                return  false;
              }

            yylex();

            if  (yytoken !=  Token_IN)
              {
                yy_expected_token(yytoken,  Token_IN,  "in");
                return  false;
              }

            yylex();

            (*yynode)->comp_operator =  Python::op_not_in;
          }

        else if  (yytoken ==  Token_IS)
          {
            if  (yytoken !=  Token_IS)
              {
                yy_expected_token(yytoken,  Token_IS,  "is");
                return  false;
              }

            yylex();

            if  (yytoken ==  Token_NOT)
              {
                if  (yytoken !=  Token_NOT)
                  {
                    yy_expected_token(yytoken,  Token_NOT,  "not");
                    return  false;
                  }

                yylex();

                (*yynode)->comp_operator =  Python::op_is_not;
              }

            else if  (true /*epsilon*/)
              {
                (*yynode)->comp_operator =  Python::op_is;
              }

            else
              {
                return  false;
              }
          }

        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_comparison(comparison_ast **yynode)
  {
    *yynode =  create<comparison_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_STRINGLITERAL
         ||  yytoken ==  Token_IDENTIFIER
         ||  yytoken ==  Token_INTEGER
         ||  yytoken ==  Token_FLOAT
         ||  yytoken ==  Token_IMAGNUM
         ||  yytoken ==  Token_LPAREN
         ||  yytoken ==  Token_LBRACE
         ||  yytoken ==  Token_LBRACKET
         ||  yytoken ==  Token_BACKTICK
         ||  yytoken ==  Token_PLUS
         ||  yytoken ==  Token_MINUS
         ||  yytoken ==  Token_TILDE)
      {
        expr_ast *__node_26 =  0;

        if  (!parse_expr(&__node_26))
          {
            yy_expected_symbol(ast_node::Kind_expr,  "expr");
            return  false;
          }

        (*yynode)->comp_expr =  __node_26;

        while  (yytoken ==  Token_IS
                ||  yytoken ==  Token_NOT
                ||  yytoken ==  Token_IN
                ||  yytoken ==  Token_LESS
                ||  yytoken ==  Token_GREATER
                ||  yytoken ==  Token_GREATEREQ
                ||  yytoken ==  Token_LESSEQ
                ||  yytoken ==  Token_UNEQUAL
                ||  yytoken ==  Token_ISEQUAL)
          {
            comp_op_ast *__node_27 =  0;

            if  (!parse_comp_op(&__node_27))
              {
                yy_expected_symbol(ast_node::Kind_comp_op,  "comp_op");
                return  false;
              }

            (*yynode)->comp_op_sequence =  snoc((*yynode)->comp_op_sequence,  __node_27,  memory_pool);

            expr_ast *__node_28 =  0;

            if  (!parse_expr(&__node_28))
              {
                yy_expected_symbol(ast_node::Kind_expr,  "expr");
                return  false;
              }

            (*yynode)->comp_op_expr_sequence =  snoc((*yynode)->comp_op_expr_sequence,  __node_28,  memory_pool);

          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_compound_stmt(compound_stmt_ast **yynode)
  {
    *yynode =  create<compound_stmt_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_FOR
         ||  yytoken ==  Token_TRY
         ||  yytoken ==  Token_CLASS
         ||  yytoken ==  Token_IF
         ||  yytoken ==  Token_WHILE
         ||  yytoken ==  Token_DEF
         ||  yytoken ==  Token_AT)
      {
        if  (yytoken ==  Token_IF)
          {
            if_stmt_ast *__node_29 =  0;

            if  (!parse_if_stmt(&__node_29))
              {
                yy_expected_symbol(ast_node::Kind_if_stmt,  "if_stmt");
                return  false;
              }

            (*yynode)->if_stmt =  __node_29;

          }

        else if  (yytoken ==  Token_WHILE)
          {
            while_stmt_ast *__node_30 =  0;

            if  (!parse_while_stmt(&__node_30))
              {
                yy_expected_symbol(ast_node::Kind_while_stmt,  "while_stmt");
                return  false;
              }

            (*yynode)->while_stmt =  __node_30;

          }

        else if  (yytoken ==  Token_FOR)
          {
            for_stmt_ast *__node_31 =  0;

            if  (!parse_for_stmt(&__node_31))
              {
                yy_expected_symbol(ast_node::Kind_for_stmt,  "for_stmt");
                return  false;
              }

            (*yynode)->for_stmt =  __node_31;

          }

        else if  (yytoken ==  Token_TRY)
          {
            try_stmt_ast *__node_32 =  0;

            if  (!parse_try_stmt(&__node_32))
              {
                yy_expected_symbol(ast_node::Kind_try_stmt,  "try_stmt");
                return  false;
              }

            (*yynode)->try_stmt =  __node_32;

          }

        else if  (yytoken ==  Token_DEF
                  ||  yytoken ==  Token_AT)
          {
            funcdef_ast *__node_33 =  0;

            if  (!parse_funcdef(&__node_33))
              {
                yy_expected_symbol(ast_node::Kind_funcdef,  "funcdef");
                return  false;
              }

            (*yynode)->fucdef =  __node_33;

          }

        else if  (yytoken ==  Token_CLASS)
          {
            classdef_ast *__node_34 =  0;

            if  (!parse_classdef(&__node_34))
              {
                yy_expected_symbol(ast_node::Kind_classdef,  "classdef");
                return  false;
              }

            (*yynode)->classdef =  __node_34;

          }

        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_continue_stmt(continue_stmt_ast **yynode)
  {
    *yynode =  create<continue_stmt_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_CONTINUE)
      {
        if  (yytoken !=  Token_CONTINUE)
          {
            yy_expected_token(yytoken,  Token_CONTINUE,  "continue");
            return  false;
          }

        yylex();

      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_decorator(decorator_ast **yynode)
  {
    *yynode =  create<decorator_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_AT)
      {
        if  (yytoken !=  Token_AT)
          {
            yy_expected_token(yytoken,  Token_AT,  "at");
            return  false;
          }

        yylex();

        dotted_name_ast *__node_35 =  0;

        if  (!parse_dotted_name(&__node_35))
          {
            yy_expected_symbol(ast_node::Kind_dotted_name,  "dotted_name");
            return  false;
          }

        (*yynode)->decorator_name =  __node_35;

        if  (yytoken ==  Token_LPAREN)
          {
            if  (yytoken !=  Token_LPAREN)
              {
                yy_expected_token(yytoken,  Token_LPAREN,  "lparen");
                return  false;
              }

            yylex();

            if  (yytoken ==  Token_LAMBDA
                 ||  yytoken ==  Token_NOT
                 ||  yytoken ==  Token_STRINGLITERAL
                 ||  yytoken ==  Token_IDENTIFIER
                 ||  yytoken ==  Token_INTEGER
                 ||  yytoken ==  Token_FLOAT
                 ||  yytoken ==  Token_IMAGNUM
                 ||  yytoken ==  Token_LPAREN
                 ||  yytoken ==  Token_LBRACE
                 ||  yytoken ==  Token_LBRACKET
                 ||  yytoken ==  Token_BACKTICK
                 ||  yytoken ==  Token_STAR
                 ||  yytoken ==  Token_DOUBLESTAR
                 ||  yytoken ==  Token_PLUS
                 ||  yytoken ==  Token_MINUS
                 ||  yytoken ==  Token_TILDE)
              {
                arglist_ast *__node_36 =  0;

                if  (!parse_arglist(&__node_36))
                  {
                    yy_expected_symbol(ast_node::Kind_arglist,  "arglist");
                    return  false;
                  }

                (*yynode)->arguments =  __node_36;

              }

            else if  (true /*epsilon*/)
            {}
            else
              {
                return  false;
              }

            if  (yytoken !=  Token_RPAREN)
              {
                yy_expected_token(yytoken,  Token_RPAREN,  "rparen");
                return  false;
              }

            yylex();

          }

        else if  (true /*epsilon*/)
        {}
        else
          {
            return  false;
          }

        if  (yytoken !=  Token_LINEBREAK)
          {
            yy_expected_token(yytoken,  Token_LINEBREAK,  "linebreak");
            return  false;
          }

        yylex();

      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_decorators(decorators_ast **yynode)
  {
    *yynode =  create<decorators_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_AT ||  yytoken ==  Token_DEF)
      {
        while  (yytoken ==  Token_AT)
          {
            decorator_ast *__node_37 =  0;

            if  (!parse_decorator(&__node_37))
              {
                yy_expected_symbol(ast_node::Kind_decorator,  "decorator");
                return  false;
              }

            (*yynode)->decorator_sequence =  snoc((*yynode)->decorator_sequence,  __node_37,  memory_pool);

          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_del_stmt(del_stmt_ast **yynode)
  {
    *yynode =  create<del_stmt_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_DEL)
      {
        if  (yytoken !=  Token_DEL)
          {
            yy_expected_token(yytoken,  Token_DEL,  "del");
            return  false;
          }

        yylex();

        exprlist_ast *__node_38 =  0;

        if  (!parse_exprlist(&__node_38))
          {
            yy_expected_symbol(ast_node::Kind_exprlist,  "exprlist");
            return  false;
          }

        (*yynode)->del_list =  __node_38;

      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_dictmaker(dictmaker_ast **yynode)
  {
    *yynode =  create<dictmaker_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_LAMBDA
         ||  yytoken ==  Token_NOT
         ||  yytoken ==  Token_STRINGLITERAL
         ||  yytoken ==  Token_IDENTIFIER
         ||  yytoken ==  Token_INTEGER
         ||  yytoken ==  Token_FLOAT
         ||  yytoken ==  Token_IMAGNUM
         ||  yytoken ==  Token_LPAREN
         ||  yytoken ==  Token_LBRACE
         ||  yytoken ==  Token_LBRACKET
         ||  yytoken ==  Token_COMMA
         ||  yytoken ==  Token_BACKTICK
         ||  yytoken ==  Token_PLUS
         ||  yytoken ==  Token_MINUS
         ||  yytoken ==  Token_TILDE ||  yytoken ==  Token_RBRACE)
      {
        if  (yytoken ==  Token_LAMBDA
             ||  yytoken ==  Token_NOT
             ||  yytoken ==  Token_STRINGLITERAL
             ||  yytoken ==  Token_IDENTIFIER
             ||  yytoken ==  Token_INTEGER
             ||  yytoken ==  Token_FLOAT
             ||  yytoken ==  Token_IMAGNUM
             ||  yytoken ==  Token_LPAREN
             ||  yytoken ==  Token_LBRACE
             ||  yytoken ==  Token_LBRACKET
             ||  yytoken ==  Token_BACKTICK
             ||  yytoken ==  Token_PLUS
             ||  yytoken ==  Token_MINUS
             ||  yytoken ==  Token_TILDE)
          {
            test_ast *__node_39 =  0;

            if  (!parse_test(&__node_39))
              {
                yy_expected_symbol(ast_node::Kind_test,  "test");
                return  false;
              }

            (*yynode)->key_list_sequence =  snoc((*yynode)->key_list_sequence,  __node_39,  memory_pool);

            if  (yytoken !=  Token_COLON)
              {
                yy_expected_token(yytoken,  Token_COLON,  "colon");
                return  false;
              }

            yylex();

            test_ast *__node_40 =  0;

            if  (!parse_test(&__node_40))
              {
                yy_expected_symbol(ast_node::Kind_test,  "test");
                return  false;
              }

            (*yynode)->value_list_sequence =  snoc((*yynode)->value_list_sequence,  __node_40,  memory_pool);

          }

        else if  (true /*epsilon*/)
        {}
        else
          {
            return  false;
          }

        while  (yytoken ==  Token_COMMA)
          {
            if  (yytoken !=  Token_COMMA)
              {
                yy_expected_token(yytoken,  Token_COMMA,  "comma");
                return  false;
              }

            yylex();

            if  (yytoken ==  Token_RBRACE)
              {
                break;
              }

            test_ast *__node_41 =  0;

            if  (!parse_test(&__node_41))
              {
                yy_expected_symbol(ast_node::Kind_test,  "test");
                return  false;
              }

            (*yynode)->key_list_sequence =  snoc((*yynode)->key_list_sequence,  __node_41,  memory_pool);

            if  (yytoken !=  Token_COLON)
              {
                yy_expected_token(yytoken,  Token_COLON,  "colon");
                return  false;
              }

            yylex();

            test_ast *__node_42 =  0;

            if  (!parse_test(&__node_42))
              {
                yy_expected_symbol(ast_node::Kind_test,  "test");
                return  false;
              }

            (*yynode)->value_list_sequence =  snoc((*yynode)->value_list_sequence,  __node_42,  memory_pool);

          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_dotted_as_name(dotted_as_name_ast **yynode)
  {
    *yynode =  create<dotted_as_name_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_IDENTIFIER)
      {
        dotted_name_ast *__node_43 =  0;

        if  (!parse_dotted_name(&__node_43))
          {
            yy_expected_symbol(ast_node::Kind_dotted_name,  "dotted_name");
            return  false;
          }

        (*yynode)->import_dotted_name =  __node_43;

        if  (yytoken ==  Token_AS)
          {
            if  (yytoken !=  Token_AS)
              {
                yy_expected_token(yytoken,  Token_AS,  "as");
                return  false;
              }

            yylex();

            if  (yytoken !=  Token_IDENTIFIER)
              {
                yy_expected_token(yytoken,  Token_IDENTIFIER,  "identifier");
                return  false;
              }

            (*yynode)->imported_as =  token_stream->index() -  1;
            yylex();

          }

        else if  (true /*epsilon*/)
        {}
        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_dotted_as_names(dotted_as_names_ast **yynode)
  {
    *yynode =  create<dotted_as_names_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_IDENTIFIER)
      {
        dotted_as_name_ast *__node_44 =  0;

        if  (!parse_dotted_as_name(&__node_44))
          {
            yy_expected_symbol(ast_node::Kind_dotted_as_name,  "dotted_as_name");
            return  false;
          }

        (*yynode)->dotted_as_name_sequence =  snoc((*yynode)->dotted_as_name_sequence,  __node_44,  memory_pool);

        while  (yytoken ==  Token_COMMA)
          {
            if  (yytoken !=  Token_COMMA)
              {
                yy_expected_token(yytoken,  Token_COMMA,  "comma");
                return  false;
              }

            yylex();

            dotted_as_name_ast *__node_45 =  0;

            if  (!parse_dotted_as_name(&__node_45))
              {
                yy_expected_symbol(ast_node::Kind_dotted_as_name,  "dotted_as_name");
                return  false;
              }

            (*yynode)->dotted_as_name_sequence =  snoc((*yynode)->dotted_as_name_sequence,  __node_45,  memory_pool);

          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_dotted_name(dotted_name_ast **yynode)
  {
    *yynode =  create<dotted_name_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_IDENTIFIER)
      {
        if  (yytoken !=  Token_IDENTIFIER)
          {
            yy_expected_token(yytoken,  Token_IDENTIFIER,  "identifier");
            return  false;
          }

        (*yynode)->dotted_name =  token_stream->index() -  1;
        yylex();

        while  (yytoken ==  Token_DOT)
          {
            if  (yytoken !=  Token_DOT)
              {
                yy_expected_token(yytoken,  Token_DOT,  "dot");
                return  false;
              }

            yylex();

            if  (yytoken !=  Token_IDENTIFIER)
              {
                yy_expected_token(yytoken,  Token_IDENTIFIER,  "identifier");
                return  false;
              }

            (*yynode)->dotted_name =  token_stream->index() -  1;
            yylex();

          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_except_clause(except_clause_ast **yynode)
  {
    *yynode =  create<except_clause_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_EXCEPT)
      {
        if  (yytoken !=  Token_EXCEPT)
          {
            yy_expected_token(yytoken,  Token_EXCEPT,  "except");
            return  false;
          }

        yylex();

        if  (yytoken ==  Token_LAMBDA
             ||  yytoken ==  Token_NOT
             ||  yytoken ==  Token_STRINGLITERAL
             ||  yytoken ==  Token_IDENTIFIER
             ||  yytoken ==  Token_INTEGER
             ||  yytoken ==  Token_FLOAT
             ||  yytoken ==  Token_IMAGNUM
             ||  yytoken ==  Token_LPAREN
             ||  yytoken ==  Token_LBRACE
             ||  yytoken ==  Token_LBRACKET
             ||  yytoken ==  Token_BACKTICK
             ||  yytoken ==  Token_PLUS
             ||  yytoken ==  Token_MINUS
             ||  yytoken ==  Token_TILDE)
          {
            test_ast *__node_46 =  0;

            if  (!parse_test(&__node_46))
              {
                yy_expected_symbol(ast_node::Kind_test,  "test");
                return  false;
              }

            (*yynode)->except_test =  __node_46;

            if  (yytoken ==  Token_COMMA)
              {
                if  (yytoken !=  Token_COMMA)
                  {
                    yy_expected_token(yytoken,  Token_COMMA,  "comma");
                    return  false;
                  }

                yylex();

                test_ast *__node_47 =  0;

                if  (!parse_test(&__node_47))
                  {
                    yy_expected_symbol(ast_node::Kind_test,  "test");
                    return  false;
                  }

                (*yynode)->except_target_test =  __node_47;

              }

            else if  (true /*epsilon*/)
            {}
            else
              {
                return  false;
              }
          }

        else if  (true /*epsilon*/)
        {}
        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_exec_stmt(exec_stmt_ast **yynode)
  {
    *yynode =  create<exec_stmt_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_EXEC)
      {
        if  (yytoken !=  Token_EXEC)
          {
            yy_expected_token(yytoken,  Token_EXEC,  "exec");
            return  false;
          }

        yylex();

        expr_ast *__node_48 =  0;

        if  (!parse_expr(&__node_48))
          {
            yy_expected_symbol(ast_node::Kind_expr,  "expr");
            return  false;
          }

        (*yynode)->exec_code =  __node_48;

        if  (yytoken ==  Token_IN)
          {
            if  (yytoken !=  Token_IN)
              {
                yy_expected_token(yytoken,  Token_IN,  "in");
                return  false;
              }

            yylex();

            test_ast *__node_49 =  0;

            if  (!parse_test(&__node_49))
              {
                yy_expected_symbol(ast_node::Kind_test,  "test");
                return  false;
              }

            (*yynode)->global_dict_exec =  __node_49;

            if  (yytoken ==  Token_COMMA)
              {
                if  (yytoken !=  Token_COMMA)
                  {
                    yy_expected_token(yytoken,  Token_COMMA,  "comma");
                    return  false;
                  }

                yylex();

                test_ast *__node_50 =  0;

                if  (!parse_test(&__node_50))
                  {
                    yy_expected_symbol(ast_node::Kind_test,  "test");
                    return  false;
                  }

                (*yynode)->local_dict_exec =  __node_50;

              }

            else if  (true /*epsilon*/)
            {}
            else
              {
                return  false;
              }
          }

        else if  (true /*epsilon*/)
        {}
        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_expr(expr_ast **yynode)
  {
    *yynode =  create<expr_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_STRINGLITERAL
         ||  yytoken ==  Token_IDENTIFIER
         ||  yytoken ==  Token_INTEGER
         ||  yytoken ==  Token_FLOAT
         ||  yytoken ==  Token_IMAGNUM
         ||  yytoken ==  Token_LPAREN
         ||  yytoken ==  Token_LBRACE
         ||  yytoken ==  Token_LBRACKET
         ||  yytoken ==  Token_BACKTICK
         ||  yytoken ==  Token_PLUS
         ||  yytoken ==  Token_MINUS
         ||  yytoken ==  Token_TILDE)
      {
        xor_expr_ast *__node_51 =  0;

        if  (!parse_xor_expr(&__node_51))
          {
            yy_expected_symbol(ast_node::Kind_xor_expr,  "xor_expr");
            return  false;
          }

        (*yynode)->expr =  __node_51;

        while  (yytoken ==  Token_ORR)
          {
            if  (yytoken !=  Token_ORR)
              {
                yy_expected_token(yytoken,  Token_ORR,  "orr");
                return  false;
              }

            yylex();

            xor_expr_ast *__node_52 =  0;

            if  (!parse_xor_expr(&__node_52))
              {
                yy_expected_symbol(ast_node::Kind_xor_expr,  "xor_expr");
                return  false;
              }

            (*yynode)->orr_expr_sequence =  snoc((*yynode)->orr_expr_sequence,  __node_52,  memory_pool);

          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_expr_stmt(expr_stmt_ast **yynode)
  {
    *yynode =  create<expr_stmt_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_LAMBDA
         ||  yytoken ==  Token_NOT
         ||  yytoken ==  Token_STRINGLITERAL
         ||  yytoken ==  Token_IDENTIFIER
         ||  yytoken ==  Token_INTEGER
         ||  yytoken ==  Token_FLOAT
         ||  yytoken ==  Token_IMAGNUM
         ||  yytoken ==  Token_LPAREN
         ||  yytoken ==  Token_LBRACE
         ||  yytoken ==  Token_LBRACKET
         ||  yytoken ==  Token_BACKTICK
         ||  yytoken ==  Token_PLUS
         ||  yytoken ==  Token_MINUS
         ||  yytoken ==  Token_TILDE)
      {
        testlist_ast *__node_53 =  0;

        if  (!parse_testlist(&__node_53))
          {
            yy_expected_symbol(ast_node::Kind_testlist,  "testlist");
            return  false;
          }

        (*yynode)->testlist =  __node_53;

        if  (yytoken ==  Token_PLUSEQ
             ||  yytoken ==  Token_MINUSEQ
             ||  yytoken ==  Token_SLASHEQ
             ||  yytoken ==  Token_DOUBLESLASHEQ
             ||  yytoken ==  Token_MODULOEQ
             ||  yytoken ==  Token_ANDEQ
             ||  yytoken ==  Token_STAREQ
             ||  yytoken ==  Token_DOUBLESTAREQ
             ||  yytoken ==  Token_LSHIFTEQ
             ||  yytoken ==  Token_RSHIFTEQ
             ||  yytoken ==  Token_TILDEEQ
             ||  yytoken ==  Token_OREQ)
          {
            augassign_ast *__node_54 =  0;

            if  (!parse_augassign(&__node_54))
              {
                yy_expected_symbol(ast_node::Kind_augassign,  "augassign");
                return  false;
              }

            (*yynode)->augassign =  __node_54;

            testlist_ast *__node_55 =  0;

            if  (!parse_testlist(&__node_55))
              {
                yy_expected_symbol(ast_node::Kind_testlist,  "testlist");
                return  false;
              }

            (*yynode)->anugassign_testlist =  __node_55;

          }

        else if  (yytoken ==  Token_EQUAL)
          {
            do
              {
                if  (yytoken !=  Token_EQUAL)
                  {
                    yy_expected_token(yytoken,  Token_EQUAL,  "equal");
                    return  false;
                  }

                yylex();

                testlist_ast *__node_56 =  0;

                if  (!parse_testlist(&__node_56))
                  {
                    yy_expected_symbol(ast_node::Kind_testlist,  "testlist");
                    return  false;
                  }

                (*yynode)->equal_testlist_sequence =  snoc((*yynode)->equal_testlist_sequence,  __node_56,  memory_pool);

              }

            while  (yytoken ==  Token_EQUAL);
          }

        else if  ((true /*epsilon*/) &&  ( yytoken ==  Token_SEMICOLON ||  yytoken ==  Token_LINEBREAK ))
        {}
        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_exprlist(exprlist_ast **yynode)
  {
    *yynode =  create<exprlist_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_STRINGLITERAL
         ||  yytoken ==  Token_IDENTIFIER
         ||  yytoken ==  Token_INTEGER
         ||  yytoken ==  Token_FLOAT
         ||  yytoken ==  Token_IMAGNUM
         ||  yytoken ==  Token_LPAREN
         ||  yytoken ==  Token_LBRACE
         ||  yytoken ==  Token_LBRACKET
         ||  yytoken ==  Token_BACKTICK
         ||  yytoken ==  Token_PLUS
         ||  yytoken ==  Token_MINUS
         ||  yytoken ==  Token_TILDE)
      {
        expr_ast *__node_57 =  0;

        if  (!parse_expr(&__node_57))
          {
            yy_expected_symbol(ast_node::Kind_expr,  "expr");
            return  false;
          }

        (*yynode)->expr_sequence =  snoc((*yynode)->expr_sequence,  __node_57,  memory_pool);

        while  (yytoken ==  Token_COMMA)
          {
            if  (yytoken !=  Token_COMMA)
              {
                yy_expected_token(yytoken,  Token_COMMA,  "comma");
                return  false;
              }

            yylex();

            if  (yytoken ==  Token_IN ||  yytoken ==  Token_SEMICOLON ||  yytoken ==  Token_LINEBREAK )
              {
                break;
              }

            expr_ast *__node_58 =  0;

            if  (!parse_expr(&__node_58))
              {
                yy_expected_symbol(ast_node::Kind_expr,  "expr");
                return  false;
              }

            (*yynode)->exprlist_sequence =  snoc((*yynode)->exprlist_sequence,  __node_58,  memory_pool);

          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_fact_op(fact_op_ast **yynode)
  {
    *yynode =  create<fact_op_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_PLUS
         ||  yytoken ==  Token_MINUS
         ||  yytoken ==  Token_TILDE)
      {
        if  (yytoken ==  Token_PLUS)
          {
            if  (yytoken !=  Token_PLUS)
              {
                yy_expected_token(yytoken,  Token_PLUS,  "plus");
                return  false;
              }

            yylex();

            (*yynode)->factor_operator =  Python::op_factor_plus;
          }

        else if  (yytoken ==  Token_MINUS)
          {
            if  (yytoken !=  Token_MINUS)
              {
                yy_expected_token(yytoken,  Token_MINUS,  "minus");
                return  false;
              }

            yylex();

            (*yynode)->factor_operator =  Python::op_factor_minus;
          }

        else if  (yytoken ==  Token_TILDE)
          {
            if  (yytoken !=  Token_TILDE)
              {
                yy_expected_token(yytoken,  Token_TILDE,  "tilde");
                return  false;
              }

            yylex();

            (*yynode)->factor_operator =  Python::op_factor_tilde ;
          }

        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_factor(factor_ast **yynode)
  {
    *yynode =  create<factor_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_STRINGLITERAL
         ||  yytoken ==  Token_IDENTIFIER
         ||  yytoken ==  Token_INTEGER
         ||  yytoken ==  Token_FLOAT
         ||  yytoken ==  Token_IMAGNUM
         ||  yytoken ==  Token_LPAREN
         ||  yytoken ==  Token_LBRACE
         ||  yytoken ==  Token_LBRACKET
         ||  yytoken ==  Token_BACKTICK
         ||  yytoken ==  Token_PLUS
         ||  yytoken ==  Token_MINUS
         ||  yytoken ==  Token_TILDE)
      {
        if  (yytoken ==  Token_PLUS
             ||  yytoken ==  Token_MINUS
             ||  yytoken ==  Token_TILDE)
          {
            fact_op_ast *__node_59 =  0;

            if  (!parse_fact_op(&__node_59))
              {
                yy_expected_symbol(ast_node::Kind_fact_op,  "fact_op");
                return  false;
              }

            (*yynode)->fact_op =  __node_59;

            factor_ast *__node_60 =  0;

            if  (!parse_factor(&__node_60))
              {
                yy_expected_symbol(ast_node::Kind_factor,  "factor");
                return  false;
              }

            (*yynode)->factor =  __node_60;

          }

        else if  (yytoken ==  Token_STRINGLITERAL
                  ||  yytoken ==  Token_IDENTIFIER
                  ||  yytoken ==  Token_INTEGER
                  ||  yytoken ==  Token_FLOAT
                  ||  yytoken ==  Token_IMAGNUM
                  ||  yytoken ==  Token_LPAREN
                  ||  yytoken ==  Token_LBRACE
                  ||  yytoken ==  Token_LBRACKET
                  ||  yytoken ==  Token_BACKTICK)
          {
            power_ast *__node_61 =  0;

            if  (!parse_power(&__node_61))
              {
                yy_expected_symbol(ast_node::Kind_power,  "power");
                return  false;
              }

            (*yynode)->power =  __node_61;

          }

        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_flow_stmt(flow_stmt_ast **yynode)
  {
    *yynode =  create<flow_stmt_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_RAISE
         ||  yytoken ==  Token_RETURN
         ||  yytoken ==  Token_BREAK
         ||  yytoken ==  Token_CONTINUE
         ||  yytoken ==  Token_YIELD)
      {
        if  (yytoken ==  Token_BREAK)
          {
            break_stmt_ast *__node_62 =  0;

            if  (!parse_break_stmt(&__node_62))
              {
                yy_expected_symbol(ast_node::Kind_break_stmt,  "break_stmt");
                return  false;
              }

            (*yynode)->break_stmt =  __node_62;

          }

        else if  (yytoken ==  Token_CONTINUE)
          {
            continue_stmt_ast *__node_63 =  0;

            if  (!parse_continue_stmt(&__node_63))
              {
                yy_expected_symbol(ast_node::Kind_continue_stmt,  "continue_stmt");
                return  false;
              }

            (*yynode)->continue_stmt =  __node_63;

          }

        else if  (yytoken ==  Token_RETURN)
          {
            return_stmt_ast *__node_64 =  0;

            if  (!parse_return_stmt(&__node_64))
              {
                yy_expected_symbol(ast_node::Kind_return_stmt,  "return_stmt");
                return  false;
              }

            (*yynode)->return_stmt =  __node_64;

          }

        else if  (yytoken ==  Token_RAISE)
          {
            raise_stmt_ast *__node_65 =  0;

            if  (!parse_raise_stmt(&__node_65))
              {
                yy_expected_symbol(ast_node::Kind_raise_stmt,  "raise_stmt");
                return  false;
              }

            (*yynode)->raise_stmt =  __node_65;

          }

        else if  (yytoken ==  Token_YIELD)
          {
            yield_stmt_ast *__node_66 =  0;

            if  (!parse_yield_stmt(&__node_66))
              {
                yy_expected_symbol(ast_node::Kind_yield_stmt,  "yield_stmt");
                return  false;
              }

            (*yynode)->yield_stmt =  __node_66;

          }

        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_for_stmt(for_stmt_ast **yynode)
  {
    *yynode =  create<for_stmt_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_FOR)
      {
        if  (yytoken !=  Token_FOR)
          {
            yy_expected_token(yytoken,  Token_FOR,  "for");
            return  false;
          }

        yylex();

        exprlist_ast *__node_67 =  0;

        if  (!parse_exprlist(&__node_67))
          {
            yy_expected_symbol(ast_node::Kind_exprlist,  "exprlist");
            return  false;
          }

        (*yynode)->for_expr =  __node_67;

        if  (yytoken !=  Token_IN)
          {
            yy_expected_token(yytoken,  Token_IN,  "in");
            return  false;
          }

        yylex();

        testlist_ast *__node_68 =  0;

        if  (!parse_testlist(&__node_68))
          {
            yy_expected_symbol(ast_node::Kind_testlist,  "testlist");
            return  false;
          }

        (*yynode)->for_testlist =  __node_68;

        if  (yytoken !=  Token_COLON)
          {
            yy_expected_token(yytoken,  Token_COLON,  "colon");
            return  false;
          }

        yylex();

        suite_ast *__node_69 =  0;

        if  (!parse_suite(&__node_69))
          {
            yy_expected_symbol(ast_node::Kind_suite,  "suite");
            return  false;
          }

        (*yynode)->for_suite =  __node_69;

        if  (yytoken ==  Token_ELSE)
          {
            if  (yytoken !=  Token_ELSE)
              {
                yy_expected_token(yytoken,  Token_ELSE,  "else");
                return  false;
              }

            yylex();

            if  (yytoken !=  Token_COLON)
              {
                yy_expected_token(yytoken,  Token_COLON,  "colon");
                return  false;
              }

            yylex();

            suite_ast *__node_70 =  0;

            if  (!parse_suite(&__node_70))
              {
                yy_expected_symbol(ast_node::Kind_suite,  "suite");
                return  false;
              }

            (*yynode)->for_else_suite =  __node_70;

          }

        else if  (true /*epsilon*/)
        {}
        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_fp_def(fp_def_ast **yynode)
  {
    *yynode =  create<fp_def_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_IDENTIFIER
         ||  yytoken ==  Token_LPAREN)
      {
        fpdef_ast *__node_71 =  0;

        if  (!parse_fpdef(&__node_71))
          {
            yy_expected_symbol(ast_node::Kind_fpdef,  "fpdef");
            return  false;
          }

        (*yynode)->fpdef =  __node_71;

        if  (yytoken ==  Token_EQUAL)
          {
            if  (yytoken !=  Token_EQUAL)
              {
                yy_expected_token(yytoken,  Token_EQUAL,  "equal");
                return  false;
              }

            yylex();

            test_ast *__node_72 =  0;

            if  (!parse_test(&__node_72))
              {
                yy_expected_symbol(ast_node::Kind_test,  "test");
                return  false;
              }

            (*yynode)->fp_def_test =  __node_72;

          }

        else if  (true /*epsilon*/)
        {}
        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_fpdef(fpdef_ast **yynode)
  {
    *yynode =  create<fpdef_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_IDENTIFIER
         ||  yytoken ==  Token_LPAREN)
      {
        if  (yytoken ==  Token_LPAREN)
          {
            if  (yytoken !=  Token_LPAREN)
              {
                yy_expected_token(yytoken,  Token_LPAREN,  "lparen");
                return  false;
              }

            yylex();

            fplist_ast *__node_73 =  0;

            if  (!parse_fplist(&__node_73))
              {
                yy_expected_symbol(ast_node::Kind_fplist,  "fplist");
                return  false;
              }

            (*yynode)->fplist =  __node_73;

            if  (yytoken !=  Token_RPAREN)
              {
                yy_expected_token(yytoken,  Token_RPAREN,  "rparen");
                return  false;
              }

            yylex();

          }

        else if  (yytoken ==  Token_IDENTIFIER)
          {
            if  (yytoken !=  Token_IDENTIFIER)
              {
                yy_expected_token(yytoken,  Token_IDENTIFIER,  "identifier");
                return  false;
              }

            yylex();

          }

        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_fplist(fplist_ast **yynode)
  {
    *yynode =  create<fplist_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_IDENTIFIER
         ||  yytoken ==  Token_LPAREN)
      {
        fpdef_ast *__node_74 =  0;

        if  (!parse_fpdef(&__node_74))
          {
            yy_expected_symbol(ast_node::Kind_fpdef,  "fpdef");
            return  false;
          }

        (*yynode)->fplist_fpdef_sequence =  snoc((*yynode)->fplist_fpdef_sequence,  __node_74,  memory_pool);

        while  (yytoken ==  Token_COMMA)
          {
            if  (yytoken !=  Token_COMMA)
              {
                yy_expected_token(yytoken,  Token_COMMA,  "comma");
                return  false;
              }

            yylex();

            if  ( yytoken ==  Token_RPAREN )
              {
                break;
              }

            fpdef_ast *__node_75 =  0;

            if  (!parse_fpdef(&__node_75))
              {
                yy_expected_symbol(ast_node::Kind_fpdef,  "fpdef");
                return  false;
              }

            (*yynode)->fplist_fpdef_sequence =  snoc((*yynode)->fplist_fpdef_sequence,  __node_75,  memory_pool);

          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_fun_pos_param(fun_pos_param_ast **yynode)
  {
    *yynode =  create<fun_pos_param_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_STAR
         ||  yytoken ==  Token_DOUBLESTAR)
      {
        if  (yytoken ==  Token_STAR)
          {
            if  (yytoken !=  Token_STAR)
              {
                yy_expected_token(yytoken,  Token_STAR,  "star");
                return  false;
              }

            yylex();

            if  (yytoken !=  Token_IDENTIFIER)
              {
                yy_expected_token(yytoken,  Token_IDENTIFIER,  "identifier");
                return  false;
              }

            (*yynode)->star_id =  token_stream->index() -  1;
            yylex();

            if  (yytoken ==  Token_COMMA)
              {
                if  (yytoken !=  Token_COMMA)
                  {
                    yy_expected_token(yytoken,  Token_COMMA,  "comma");
                    return  false;
                  }

                yylex();

                if  (yytoken !=  Token_DOUBLESTAR)
                  {
                    yy_expected_token(yytoken,  Token_DOUBLESTAR,  "doublestar");
                    return  false;
                  }

                yylex();

                if  (yytoken !=  Token_IDENTIFIER)
                  {
                    yy_expected_token(yytoken,  Token_IDENTIFIER,  "identifier");
                    return  false;
                  }

                (*yynode)->double_star_id =  token_stream->index() -  1;
                yylex();

              }

            else if  (true /*epsilon*/)
            {}
            else
              {
                return  false;
              }
          }

        else if  (yytoken ==  Token_DOUBLESTAR)
          {
            if  (yytoken !=  Token_DOUBLESTAR)
              {
                yy_expected_token(yytoken,  Token_DOUBLESTAR,  "doublestar");
                return  false;
              }

            yylex();

            if  (yytoken !=  Token_IDENTIFIER)
              {
                yy_expected_token(yytoken,  Token_IDENTIFIER,  "identifier");
                return  false;
              }

            (*yynode)->double_star_id =  token_stream->index() -  1;
            yylex();

          }

        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_func_def(func_def_ast **yynode)
  {
    *yynode =  create<func_def_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_IDENTIFIER
         ||  yytoken ==  Token_LPAREN)
      {
        fp_def_ast *__node_76 =  0;

        if  (!parse_fp_def(&__node_76))
          {
            yy_expected_symbol(ast_node::Kind_fp_def,  "fp_def");
            return  false;
          }

        (*yynode)->fp_def_sequence =  snoc((*yynode)->fp_def_sequence,  __node_76,  memory_pool);

        while  (yytoken ==  Token_COMMA)
          {
            if  (yytoken !=  Token_COMMA)
              {
                yy_expected_token(yytoken,  Token_COMMA,  "comma");
                return  false;
              }

            yylex();

            if (yytoken ==  Token_RPAREN  ||  yytoken ==  Token_STAR ||  yytoken ==  Token_DOUBLESTAR )
              {
                break;
              }

            fp_def_ast *__node_77 =  0;

            if  (!parse_fp_def(&__node_77))
              {
                yy_expected_symbol(ast_node::Kind_fp_def,  "fp_def");
                return  false;
              }

            (*yynode)->fp_def_sequence =  snoc((*yynode)->fp_def_sequence,  __node_77,  memory_pool);

          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_funcdef(funcdef_ast **yynode)
  {
    *yynode =  create<funcdef_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_DEF
         ||  yytoken ==  Token_AT)
      {
        if  (yytoken ==  Token_AT)
          {
            decorators_ast *__node_78 =  0;

            if  (!parse_decorators(&__node_78))
              {
                yy_expected_symbol(ast_node::Kind_decorators,  "decorators");
                return  false;
              }

            (*yynode)->decorators =  __node_78;

          }

        else if  (true /*epsilon*/)
        {}
        else
          {
            return  false;
          }

        if  (yytoken !=  Token_DEF)
          {
            yy_expected_token(yytoken,  Token_DEF,  "def");
            return  false;
          }

        yylex();

        if  (yytoken !=  Token_IDENTIFIER)
          {
            yy_expected_token(yytoken,  Token_IDENTIFIER,  "identifier");
            return  false;
          }

        (*yynode)->func_name =  token_stream->index() -  1;
        yylex();

        if  (yytoken !=  Token_LPAREN)
          {
            yy_expected_token(yytoken,  Token_LPAREN,  "lparen");
            return  false;
          }

        yylex();

        if  ((yytoken ==  Token_IDENTIFIER
              ||  yytoken ==  Token_LPAREN
              ||  yytoken ==  Token_STAR
              ||  yytoken ==  Token_DOUBLESTAR) &&  ( LA(1).kind !=  Token_RPAREN ))
          {
            varargslist_ast *__node_79 =  0;

            if  (!parse_varargslist(&__node_79))
              {
                yy_expected_symbol(ast_node::Kind_varargslist,  "varargslist");
                return  false;
              }

            (*yynode)->fun_args =  __node_79;

          }

        else if  (true /*epsilon*/)
        {}
        else
          {
            return  false;
          }

        if  (yytoken !=  Token_RPAREN)
          {
            yy_expected_token(yytoken,  Token_RPAREN,  "rparen");
            return  false;
          }

        yylex();

        if  (yytoken !=  Token_COLON)
          {
            yy_expected_token(yytoken,  Token_COLON,  "colon");
            return  false;
          }

        yylex();

        suite_ast *__node_80 =  0;

        if  (!parse_suite(&__node_80))
          {
            yy_expected_symbol(ast_node::Kind_suite,  "suite");
            return  false;
          }

        (*yynode)->fun_suite =  __node_80;

      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_gen_for(gen_for_ast **yynode)
  {
    *yynode =  create<gen_for_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_FOR)
      {
        if  (yytoken !=  Token_FOR)
          {
            yy_expected_token(yytoken,  Token_FOR,  "for");
            return  false;
          }

        yylex();

        exprlist_ast *__node_81 =  0;

        if  (!parse_exprlist(&__node_81))
          {
            yy_expected_symbol(ast_node::Kind_exprlist,  "exprlist");
            return  false;
          }

        (*yynode)->exprlist =  __node_81;

        if  (yytoken !=  Token_IN)
          {
            yy_expected_token(yytoken,  Token_IN,  "in");
            return  false;
          }

        yylex();

        test_ast *__node_82 =  0;

        if  (!parse_test(&__node_82))
          {
            yy_expected_symbol(ast_node::Kind_test,  "test");
            return  false;
          }

        (*yynode)->test =  __node_82;

        if  (yytoken ==  Token_FOR
             ||  yytoken ==  Token_IF)
          {
            gen_iter_ast *__node_83 =  0;

            if  (!parse_gen_iter(&__node_83))
              {
                yy_expected_symbol(ast_node::Kind_gen_iter,  "gen_iter");
                return  false;
              }

            (*yynode)->gen_iter =  __node_83;

          }

        else if  (true /*epsilon*/)
        {}
        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_gen_if(gen_if_ast **yynode)
  {
    *yynode =  create<gen_if_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_IF)
      {
        if  (yytoken !=  Token_IF)
          {
            yy_expected_token(yytoken,  Token_IF,  "if");
            return  false;
          }

        yylex();

        test_ast *__node_84 =  0;

        if  (!parse_test(&__node_84))
          {
            yy_expected_symbol(ast_node::Kind_test,  "test");
            return  false;
          }

        (*yynode)->test =  __node_84;

        if  (yytoken ==  Token_FOR
             ||  yytoken ==  Token_IF)
          {
            gen_iter_ast *__node_85 =  0;

            if  (!parse_gen_iter(&__node_85))
              {
                yy_expected_symbol(ast_node::Kind_gen_iter,  "gen_iter");
                return  false;
              }

            (*yynode)->gen_iter =  __node_85;

          }

        else if  (true /*epsilon*/)
        {}
        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_gen_iter(gen_iter_ast **yynode)
  {
    *yynode =  create<gen_iter_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_FOR
         ||  yytoken ==  Token_IF)
      {
        if  (yytoken ==  Token_FOR)
          {
            gen_for_ast *__node_86 =  0;

            if  (!parse_gen_for(&__node_86))
              {
                yy_expected_symbol(ast_node::Kind_gen_for,  "gen_for");
                return  false;
              }

            (*yynode)->gen_for =  __node_86;

          }

        else if  (yytoken ==  Token_IF)
          {
            gen_if_ast *__node_87 =  0;

            if  (!parse_gen_if(&__node_87))
              {
                yy_expected_symbol(ast_node::Kind_gen_if,  "gen_if");
                return  false;
              }

            (*yynode)->gen_if =  __node_87;

          }

        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_global_stmt(global_stmt_ast **yynode)
  {
    *yynode =  create<global_stmt_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_GLOBAL)
      {
        if  (yytoken !=  Token_GLOBAL)
          {
            yy_expected_token(yytoken,  Token_GLOBAL,  "global");
            return  false;
          }

        yylex();

        if  (yytoken !=  Token_IDENTIFIER)
          {
            yy_expected_token(yytoken,  Token_IDENTIFIER,  "identifier");
            return  false;
          }

        (*yynode)->global_name_sequence =  snoc((*yynode)->global_name_sequence,  token_stream->index() -  1,  memory_pool);
        yylex();

        while  (yytoken ==  Token_COMMA)
          {
            if  (yytoken !=  Token_COMMA)
              {
                yy_expected_token(yytoken,  Token_COMMA,  "comma");
                return  false;
              }

            yylex();

            if  (yytoken !=  Token_IDENTIFIER)
              {
                yy_expected_token(yytoken,  Token_IDENTIFIER,  "identifier");
                return  false;
              }

            (*yynode)->global_name_sequence =  snoc((*yynode)->global_name_sequence,  token_stream->index() -  1,  memory_pool);
            yylex();

          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_if_stmt(if_stmt_ast **yynode)
  {
    *yynode =  create<if_stmt_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_IF)
      {
        if  (yytoken !=  Token_IF)
          {
            yy_expected_token(yytoken,  Token_IF,  "if");
            return  false;
          }

        yylex();

        test_ast *__node_88 =  0;

        if  (!parse_test(&__node_88))
          {
            yy_expected_symbol(ast_node::Kind_test,  "test");
            return  false;
          }

        (*yynode)->if_test_sequence =  snoc((*yynode)->if_test_sequence,  __node_88,  memory_pool);

        if  (yytoken !=  Token_COLON)
          {
            yy_expected_token(yytoken,  Token_COLON,  "colon");
            return  false;
          }

        yylex();

        suite_ast *__node_89 =  0;

        if  (!parse_suite(&__node_89))
          {
            yy_expected_symbol(ast_node::Kind_suite,  "suite");
            return  false;
          }

        (*yynode)->if_suite =  __node_89;

        while  (yytoken ==  Token_ELIF)
          {
            if  (yytoken !=  Token_ELIF)
              {
                yy_expected_token(yytoken,  Token_ELIF,  "elif");
                return  false;
              }

            yylex();

            test_ast *__node_90 =  0;

            if  (!parse_test(&__node_90))
              {
                yy_expected_symbol(ast_node::Kind_test,  "test");
                return  false;
              }

            (*yynode)->elif_test_sequence =  snoc((*yynode)->elif_test_sequence,  __node_90,  memory_pool);

            if  (yytoken !=  Token_COLON)
              {
                yy_expected_token(yytoken,  Token_COLON,  "colon");
                return  false;
              }

            yylex();

            suite_ast *__node_91 =  0;

            if  (!parse_suite(&__node_91))
              {
                yy_expected_symbol(ast_node::Kind_suite,  "suite");
                return  false;
              }

            (*yynode)->elif_suite_sequence =  snoc((*yynode)->elif_suite_sequence,  __node_91,  memory_pool);

          }

        if  (yytoken ==  Token_ELSE)
          {
            if  (yytoken !=  Token_ELSE)
              {
                yy_expected_token(yytoken,  Token_ELSE,  "else");
                return  false;
              }

            yylex();

            if  (yytoken !=  Token_COLON)
              {
                yy_expected_token(yytoken,  Token_COLON,  "colon");
                return  false;
              }

            yylex();

            suite_ast *__node_92 =  0;

            if  (!parse_suite(&__node_92))
              {
                yy_expected_symbol(ast_node::Kind_suite,  "suite");
                return  false;
              }

            (*yynode)->if_else_suite =  __node_92;

          }

        else if  (true /*epsilon*/)
        {}
        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_import_as_name(import_as_name_ast **yynode)
  {
    *yynode =  create<import_as_name_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_IDENTIFIER)
      {
        if  (yytoken !=  Token_IDENTIFIER)
          {
            yy_expected_token(yytoken,  Token_IDENTIFIER,  "identifier");
            return  false;
          }

        (*yynode)->imported_name =  token_stream->index() -  1;
        yylex();

        if  (yytoken ==  Token_AS)
          {
            if  (yytoken !=  Token_AS)
              {
                yy_expected_token(yytoken,  Token_AS,  "as");
                return  false;
              }

            yylex();

            if  (yytoken !=  Token_IDENTIFIER)
              {
                yy_expected_token(yytoken,  Token_IDENTIFIER,  "identifier");
                return  false;
              }

            (*yynode)->imported_as =  token_stream->index() -  1;
            yylex();

          }

        else if  (true /*epsilon*/)
        {}
        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_import_as_names(import_as_names_ast **yynode)
  {
    *yynode =  create<import_as_names_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_IDENTIFIER)
      {
        import_as_name_ast *__node_93 =  0;

        if  (!parse_import_as_name(&__node_93))
          {
            yy_expected_symbol(ast_node::Kind_import_as_name,  "import_as_name");
            return  false;
          }

        (*yynode)->import_as_name_sequence =  snoc((*yynode)->import_as_name_sequence,  __node_93,  memory_pool);

        while  (yytoken ==  Token_COMMA)
          {
            if  (yytoken !=  Token_COMMA)
              {
                yy_expected_token(yytoken,  Token_COMMA,  "comma");
                return  false;
              }

            yylex();

            if ( yytoken ==  Token_RPAREN ||  yytoken ==  Token_LINEBREAK ||  yytoken ==  Token_SEMICOLON )
              {
                break;
              }

            import_as_name_ast *__node_94 =  0;

            if  (!parse_import_as_name(&__node_94))
              {
                yy_expected_symbol(ast_node::Kind_import_as_name,  "import_as_name");
                return  false;
              }

            (*yynode)->import_as_name_sequence =  snoc((*yynode)->import_as_name_sequence,  __node_94,  memory_pool);

          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_import_from(import_from_ast **yynode)
  {
    *yynode =  create<import_from_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_FROM)
      {
        if  (yytoken !=  Token_FROM)
          {
            yy_expected_token(yytoken,  Token_FROM,  "from");
            return  false;
          }

        yylex();

        dotted_name_ast *__node_95 =  0;

        if  (!parse_dotted_name(&__node_95))
          {
            yy_expected_symbol(ast_node::Kind_dotted_name,  "dotted_name");
            return  false;
          }

        (*yynode)->import_from_name =  __node_95;

        if  (yytoken !=  Token_IMPORT)
          {
            yy_expected_token(yytoken,  Token_IMPORT,  "import");
            return  false;
          }

        yylex();

        if  (yytoken ==  Token_STAR)
          {
            if  (yytoken !=  Token_STAR)
              {
                yy_expected_token(yytoken,  Token_STAR,  "star");
                return  false;
              }

            yylex();

          }

        else if  (yytoken ==  Token_LPAREN)
          {
            if  (yytoken !=  Token_LPAREN)
              {
                yy_expected_token(yytoken,  Token_LPAREN,  "lparen");
                return  false;
              }

            yylex();

            import_as_names_ast *__node_96 =  0;

            if  (!parse_import_as_names(&__node_96))
              {
                yy_expected_symbol(ast_node::Kind_import_as_names,  "import_as_names");
                return  false;
              }

            (*yynode)->import_as_names =  __node_96;

            if  (yytoken !=  Token_RPAREN)
              {
                yy_expected_token(yytoken,  Token_RPAREN,  "rparen");
                return  false;
              }

            yylex();

          }

        else if  (yytoken ==  Token_IDENTIFIER)
          {
            import_as_names_ast *__node_97 =  0;

            if  (!parse_import_as_names(&__node_97))
              {
                yy_expected_symbol(ast_node::Kind_import_as_names,  "import_as_names");
                return  false;
              }

            (*yynode)->import_from_as_name =  __node_97;

          }

        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_import_name(import_name_ast **yynode)
  {
    *yynode =  create<import_name_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_IMPORT)
      {
        if  (yytoken !=  Token_IMPORT)
          {
            yy_expected_token(yytoken,  Token_IMPORT,  "import");
            return  false;
          }

        yylex();

        dotted_as_names_ast *__node_98 =  0;

        if  (!parse_dotted_as_names(&__node_98))
          {
            yy_expected_symbol(ast_node::Kind_dotted_as_names,  "dotted_as_names");
            return  false;
          }

        (*yynode)->import_name =  __node_98;

      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_import_stmt(import_stmt_ast **yynode)
  {
    *yynode =  create<import_stmt_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_FROM
         ||  yytoken ==  Token_IMPORT)
      {
        if  (yytoken ==  Token_IMPORT)
          {
            import_name_ast *__node_99 =  0;

            if  (!parse_import_name(&__node_99))
              {
                yy_expected_symbol(ast_node::Kind_import_name,  "import_name");
                return  false;
              }

            (*yynode)->import_import =  __node_99;

          }

        else if  (yytoken ==  Token_FROM)
          {
            import_from_ast *__node_100 =  0;

            if  (!parse_import_from(&__node_100))
              {
                yy_expected_symbol(ast_node::Kind_import_from,  "import_from");
                return  false;
              }

            (*yynode)->import_from =  __node_100;

          }

        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_lambda_def(lambda_def_ast **yynode)
  {
    *yynode =  create<lambda_def_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_LAMBDA)
      {
        if  (yytoken !=  Token_LAMBDA)
          {
            yy_expected_token(yytoken,  Token_LAMBDA,  "lambda");
            return  false;
          }

        yylex();

        if  (yytoken ==  Token_IDENTIFIER
             ||  yytoken ==  Token_LPAREN
             ||  yytoken ==  Token_STAR
             ||  yytoken ==  Token_DOUBLESTAR)
          {
            varargslist_ast *__node_101 =  0;

            if  (!parse_varargslist(&__node_101))
              {
                yy_expected_symbol(ast_node::Kind_varargslist,  "varargslist");
                return  false;
              }

            (*yynode)->lambda_varargslist =  __node_101;

          }

        else if  (true /*epsilon*/)
        {}
        else
          {
            return  false;
          }

        if  (yytoken !=  Token_COLON)
          {
            yy_expected_token(yytoken,  Token_COLON,  "colon");
            return  false;
          }

        yylex();

        test_ast *__node_102 =  0;

        if  (!parse_test(&__node_102))
          {
            yy_expected_symbol(ast_node::Kind_test,  "test");
            return  false;
          }

        (*yynode)->lambda_test =  __node_102;

      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_list_for(list_for_ast **yynode)
  {
    *yynode =  create<list_for_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_FOR)
      {
        if  (yytoken !=  Token_FOR)
          {
            yy_expected_token(yytoken,  Token_FOR,  "for");
            return  false;
          }

        yylex();

        exprlist_ast *__node_103 =  0;

        if  (!parse_exprlist(&__node_103))
          {
            yy_expected_symbol(ast_node::Kind_exprlist,  "exprlist");
            return  false;
          }

        (*yynode)->exprlist =  __node_103;

        if  (yytoken !=  Token_IN)
          {
            yy_expected_token(yytoken,  Token_IN,  "in");
            return  false;
          }

        yylex();

        testlist_safe_ast *__node_104 =  0;

        if  (!parse_testlist_safe(&__node_104))
          {
            yy_expected_symbol(ast_node::Kind_testlist_safe,  "testlist_safe");
            return  false;
          }

        (*yynode)->testlist_safe =  __node_104;

        if  (yytoken ==  Token_FOR
             ||  yytoken ==  Token_IF)
          {
            list_iter_ast *__node_105 =  0;

            if  (!parse_list_iter(&__node_105))
              {
                yy_expected_symbol(ast_node::Kind_list_iter,  "list_iter");
                return  false;
              }

            (*yynode)->list_iter =  __node_105;

          }

        else if  (true /*epsilon*/)
        {}
        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_list_if(list_if_ast **yynode)
  {
    *yynode =  create<list_if_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_IF)
      {
        if  (yytoken !=  Token_IF)
          {
            yy_expected_token(yytoken,  Token_IF,  "if");
            return  false;
          }

        yylex();

        test_ast *__node_106 =  0;

        if  (!parse_test(&__node_106))
          {
            yy_expected_symbol(ast_node::Kind_test,  "test");
            return  false;
          }

        (*yynode)->test =  __node_106;

        if  (yytoken ==  Token_FOR
             ||  yytoken ==  Token_IF)
          {
            list_iter_ast *__node_107 =  0;

            if  (!parse_list_iter(&__node_107))
              {
                yy_expected_symbol(ast_node::Kind_list_iter,  "list_iter");
                return  false;
              }

            (*yynode)->list_iter =  __node_107;

          }

        else if  (true /*epsilon*/)
        {}
        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_list_iter(list_iter_ast **yynode)
  {
    *yynode =  create<list_iter_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_FOR
         ||  yytoken ==  Token_IF)
      {
        if  (yytoken ==  Token_FOR)
          {
            list_for_ast *__node_108 =  0;

            if  (!parse_list_for(&__node_108))
              {
                yy_expected_symbol(ast_node::Kind_list_for,  "list_for");
                return  false;
              }

            (*yynode)->list_for =  __node_108;

          }

        else if  (yytoken ==  Token_IF)
          {
            list_if_ast *__node_109 =  0;

            if  (!parse_list_if(&__node_109))
              {
                yy_expected_symbol(ast_node::Kind_list_if,  "list_if");
                return  false;
              }

            (*yynode)->list_if =  __node_109;

          }

        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_list_maker(list_maker_ast **yynode)
  {
    *yynode =  create<list_maker_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_LAMBDA
         ||  yytoken ==  Token_NOT
         ||  yytoken ==  Token_STRINGLITERAL
         ||  yytoken ==  Token_IDENTIFIER
         ||  yytoken ==  Token_INTEGER
         ||  yytoken ==  Token_FLOAT
         ||  yytoken ==  Token_IMAGNUM
         ||  yytoken ==  Token_LPAREN
         ||  yytoken ==  Token_LBRACE
         ||  yytoken ==  Token_LBRACKET
         ||  yytoken ==  Token_BACKTICK
         ||  yytoken ==  Token_PLUS
         ||  yytoken ==  Token_MINUS
         ||  yytoken ==  Token_TILDE ||  yytoken ==  Token_FOR
         ||  yytoken ==  Token_RBRACKET)
      {
        if  (yytoken ==  Token_LAMBDA
             ||  yytoken ==  Token_NOT
             ||  yytoken ==  Token_STRINGLITERAL
             ||  yytoken ==  Token_IDENTIFIER
             ||  yytoken ==  Token_INTEGER
             ||  yytoken ==  Token_FLOAT
             ||  yytoken ==  Token_IMAGNUM
             ||  yytoken ==  Token_LPAREN
             ||  yytoken ==  Token_LBRACE
             ||  yytoken ==  Token_LBRACKET
             ||  yytoken ==  Token_BACKTICK
             ||  yytoken ==  Token_PLUS
             ||  yytoken ==  Token_MINUS
             ||  yytoken ==  Token_TILDE)
          {
            test_ast *__node_110 =  0;

            if  (!parse_test(&__node_110))
              {
                yy_expected_symbol(ast_node::Kind_test,  "test");
                return  false;
              }

            (*yynode)->list_test_sequence =  snoc((*yynode)->list_test_sequence,  __node_110,  memory_pool);

            while  (yytoken ==  Token_COMMA)
              {
                if  (yytoken !=  Token_COMMA)
                  {
                    yy_expected_token(yytoken,  Token_COMMA,  "comma");
                    return  false;
                  }

                yylex();

                if  (yytoken ==  Token_RBRACKET)
                  {
                    break;
                  }

                test_ast *__node_111 =  0;

                if  (!parse_test(&__node_111))
                  {
                    yy_expected_symbol(ast_node::Kind_test,  "test");
                    return  false;
                  }

                (*yynode)->list_test_sequence =  snoc((*yynode)->list_test_sequence,  __node_111,  memory_pool);

              }
          }

        else if  (true /*epsilon*/)
        {}
        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_listmaker(listmaker_ast **yynode)
  {
    *yynode =  create<listmaker_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_FOR
         ||  yytoken ==  Token_LAMBDA
         ||  yytoken ==  Token_NOT
         ||  yytoken ==  Token_STRINGLITERAL
         ||  yytoken ==  Token_IDENTIFIER
         ||  yytoken ==  Token_INTEGER
         ||  yytoken ==  Token_FLOAT
         ||  yytoken ==  Token_IMAGNUM
         ||  yytoken ==  Token_LPAREN
         ||  yytoken ==  Token_LBRACE
         ||  yytoken ==  Token_LBRACKET
         ||  yytoken ==  Token_BACKTICK
         ||  yytoken ==  Token_PLUS
         ||  yytoken ==  Token_MINUS
         ||  yytoken ==  Token_TILDE ||  yytoken ==  Token_RBRACKET)
      {
        list_maker_ast *__node_112 =  0;

        if  (!parse_list_maker(&__node_112))
          {
            yy_expected_symbol(ast_node::Kind_list_maker,  "list_maker");
            return  false;
          }

        (*yynode)->list_maker =  __node_112;

        if  (yytoken ==  Token_FOR)
          {
            list_for_ast *__node_113 =  0;

            if  (!parse_list_for(&__node_113))
              {
                yy_expected_symbol(ast_node::Kind_list_for,  "list_for");
                return  false;
              }

            (*yynode)->list_for =  __node_113;

          }

        else if  (true /*epsilon*/)
        {}
        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_not_test(not_test_ast **yynode)
  {
    *yynode =  create<not_test_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_NOT
         ||  yytoken ==  Token_STRINGLITERAL
         ||  yytoken ==  Token_IDENTIFIER
         ||  yytoken ==  Token_INTEGER
         ||  yytoken ==  Token_FLOAT
         ||  yytoken ==  Token_IMAGNUM
         ||  yytoken ==  Token_LPAREN
         ||  yytoken ==  Token_LBRACE
         ||  yytoken ==  Token_LBRACKET
         ||  yytoken ==  Token_BACKTICK
         ||  yytoken ==  Token_PLUS
         ||  yytoken ==  Token_MINUS
         ||  yytoken ==  Token_TILDE)
      {
        if  (yytoken ==  Token_NOT)
          {
            if  (yytoken !=  Token_NOT)
              {
                yy_expected_token(yytoken,  Token_NOT,  "not");
                return  false;
              }

            yylex();

            not_test_ast *__node_114 =  0;

            if  (!parse_not_test(&__node_114))
              {
                yy_expected_symbol(ast_node::Kind_not_test,  "not_test");
                return  false;
              }

            (*yynode)->not_test =  __node_114;

          }

        else if  (yytoken ==  Token_STRINGLITERAL
                  ||  yytoken ==  Token_IDENTIFIER
                  ||  yytoken ==  Token_INTEGER
                  ||  yytoken ==  Token_FLOAT
                  ||  yytoken ==  Token_IMAGNUM
                  ||  yytoken ==  Token_LPAREN
                  ||  yytoken ==  Token_LBRACE
                  ||  yytoken ==  Token_LBRACKET
                  ||  yytoken ==  Token_BACKTICK
                  ||  yytoken ==  Token_PLUS
                  ||  yytoken ==  Token_MINUS
                  ||  yytoken ==  Token_TILDE)
          {
            comparison_ast *__node_115 =  0;

            if  (!parse_comparison(&__node_115))
              {
                yy_expected_symbol(ast_node::Kind_comparison,  "comparison");
                return  false;
              }

            (*yynode)->comparison =  __node_115;

          }

        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_number(number_ast **yynode)
  {
    *yynode =  create<number_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_INTEGER
         ||  yytoken ==  Token_FLOAT
         ||  yytoken ==  Token_IMAGNUM)
      {
        if  (yytoken ==  Token_INTEGER)
          {
            if  (yytoken !=  Token_INTEGER)
              {
                yy_expected_token(yytoken,  Token_INTEGER,  "integer");
                return  false;
              }

            yylex();

            (*yynode)->num_type =  Python::type_int;
          }

        else if  (yytoken ==  Token_FLOAT)
          {
            if  (yytoken !=  Token_FLOAT)
              {
                yy_expected_token(yytoken,  Token_FLOAT,  "float");
                return  false;
              }

            yylex();

            (*yynode)->num_type =  Python::type_float;
          }

        else if  (yytoken ==  Token_IMAGNUM)
          {
            if  (yytoken !=  Token_IMAGNUM)
              {
                yy_expected_token(yytoken,  Token_IMAGNUM,  "imagnum");
                return  false;
              }

            yylex();

            (*yynode)->num_type =  Python::type_imagnum;
          }

        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_pass_stmt(pass_stmt_ast **yynode)
  {
    *yynode =  create<pass_stmt_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_PASS)
      {
        if  (yytoken !=  Token_PASS)
          {
            yy_expected_token(yytoken,  Token_PASS,  "pass");
            return  false;
          }

        yylex();

      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_power(power_ast **yynode)
  {
    *yynode =  create<power_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_STRINGLITERAL
         ||  yytoken ==  Token_IDENTIFIER
         ||  yytoken ==  Token_INTEGER
         ||  yytoken ==  Token_FLOAT
         ||  yytoken ==  Token_IMAGNUM
         ||  yytoken ==  Token_LPAREN
         ||  yytoken ==  Token_LBRACE
         ||  yytoken ==  Token_LBRACKET
         ||  yytoken ==  Token_BACKTICK)
      {
        atom_ast *__node_116 =  0;

        if  (!parse_atom(&__node_116))
          {
            yy_expected_symbol(ast_node::Kind_atom,  "atom");
            return  false;
          }

        (*yynode)->atom =  __node_116;

        while  (yytoken ==  Token_LPAREN
                ||  yytoken ==  Token_LBRACKET
                ||  yytoken ==  Token_DOT)
          {
            trailer_ast *__node_117 =  0;

            if  (!parse_trailer(&__node_117))
              {
                yy_expected_symbol(ast_node::Kind_trailer,  "trailer");
                return  false;
              }

            (*yynode)->trailer_sequence =  snoc((*yynode)->trailer_sequence,  __node_117,  memory_pool);

          }

        if  (yytoken ==  Token_DOUBLESTAR)
          {
            if  (yytoken !=  Token_DOUBLESTAR)
              {
                yy_expected_token(yytoken,  Token_DOUBLESTAR,  "doublestar");
                return  false;
              }

            yylex();

            factor_ast *__node_118 =  0;

            if  (!parse_factor(&__node_118))
              {
                yy_expected_symbol(ast_node::Kind_factor,  "factor");
                return  false;
              }

            (*yynode)->factor =  __node_118;

          }

        else if  (true /*epsilon*/)
        {}
        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_print_stmt(print_stmt_ast **yynode)
  {
    *yynode =  create<print_stmt_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_PRINT)
      {
        if  (yytoken !=  Token_PRINT)
          {
            yy_expected_token(yytoken,  Token_PRINT,  "print");
            return  false;
          }

        yylex();

        if  (yytoken ==  Token_LAMBDA
             ||  yytoken ==  Token_NOT
             ||  yytoken ==  Token_STRINGLITERAL
             ||  yytoken ==  Token_IDENTIFIER
             ||  yytoken ==  Token_INTEGER
             ||  yytoken ==  Token_FLOAT
             ||  yytoken ==  Token_IMAGNUM
             ||  yytoken ==  Token_LPAREN
             ||  yytoken ==  Token_LBRACE
             ||  yytoken ==  Token_LBRACKET
             ||  yytoken ==  Token_BACKTICK
             ||  yytoken ==  Token_PLUS
             ||  yytoken ==  Token_MINUS
             ||  yytoken ==  Token_TILDE)
          {
            test_ast *__node_119 =  0;

            if  (!parse_test(&__node_119))
              {
                yy_expected_symbol(ast_node::Kind_test,  "test");
                return  false;
              }

            (*yynode)->print_args_sequence =  snoc((*yynode)->print_args_sequence,  __node_119,  memory_pool);

            while  (yytoken ==  Token_COMMA)
              {
                if  (yytoken !=  Token_COMMA)
                  {
                    yy_expected_token(yytoken,  Token_COMMA,  "comma");
                    return  false;
                  }

                yylex();

                if (yytoken ==  Token_SEMICOLON ||  yytoken ==  Token_LINEBREAK)
                  {
                    break;
                  }

                test_ast *__node_120 =  0;

                if  (!parse_test(&__node_120))
                  {
                    yy_expected_symbol(ast_node::Kind_test,  "test");
                    return  false;
                  }

                (*yynode)->print_args_sequence =  snoc((*yynode)->print_args_sequence,  __node_120,  memory_pool);

              }
          }

        else if  (yytoken ==  Token_RSHIFT)
          {
            if  (yytoken !=  Token_RSHIFT)
              {
                yy_expected_token(yytoken,  Token_RSHIFT,  "rshift");
                return  false;
              }

            yylex();

            test_ast *__node_121 =  0;

            if  (!parse_test(&__node_121))
              {
                yy_expected_symbol(ast_node::Kind_test,  "test");
                return  false;
              }

            (*yynode)->rshift_args_sequence =  snoc((*yynode)->rshift_args_sequence,  __node_121,  memory_pool);

            while  (yytoken ==  Token_COMMA)
              {
                if  (yytoken !=  Token_COMMA)
                  {
                    yy_expected_token(yytoken,  Token_COMMA,  "comma");
                    return  false;
                  }

                yylex();

                if (yytoken ==  Token_SEMICOLON ||  yytoken ==  Token_LINEBREAK)
                  {
                    break;
                  }

                test_ast *__node_122 =  0;

                if  (!parse_test(&__node_122))
                  {
                    yy_expected_symbol(ast_node::Kind_test,  "test");
                    return  false;
                  }

                (*yynode)->rshift_args_sequence =  snoc((*yynode)->rshift_args_sequence,  __node_122,  memory_pool);

              }
          }

        else if  (true /*epsilon*/)
        {}
        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_project(project_ast **yynode)
  {
    *yynode =  create<project_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_DEL
         ||  yytoken ==  Token_FOR
         ||  yytoken ==  Token_RAISE
         ||  yytoken ==  Token_ASSERT
         ||  yytoken ==  Token_FROM
         ||  yytoken ==  Token_LAMBDA
         ||  yytoken ==  Token_RETURN
         ||  yytoken ==  Token_BREAK
         ||  yytoken ==  Token_GLOBAL
         ||  yytoken ==  Token_NOT
         ||  yytoken ==  Token_TRY
         ||  yytoken ==  Token_CLASS
         ||  yytoken ==  Token_IF
         ||  yytoken ==  Token_WHILE
         ||  yytoken ==  Token_CONTINUE
         ||  yytoken ==  Token_EXEC
         ||  yytoken ==  Token_IMPORT
         ||  yytoken ==  Token_PASS
         ||  yytoken ==  Token_YIELD
         ||  yytoken ==  Token_DEF
         ||  yytoken ==  Token_PRINT
         ||  yytoken ==  Token_LINEBREAK
         ||  yytoken ==  Token_STRINGLITERAL
         ||  yytoken ==  Token_IDENTIFIER
         ||  yytoken ==  Token_INTEGER
         ||  yytoken ==  Token_FLOAT
         ||  yytoken ==  Token_IMAGNUM
         ||  yytoken ==  Token_LPAREN
         ||  yytoken ==  Token_LBRACE
         ||  yytoken ==  Token_LBRACKET
         ||  yytoken ==  Token_AT
         ||  yytoken ==  Token_BACKTICK
         ||  yytoken ==  Token_PLUS
         ||  yytoken ==  Token_MINUS
         ||  yytoken ==  Token_TILDE ||  yytoken ==  Token_EOF)
      {
        while  (yytoken ==  Token_DEL
                ||  yytoken ==  Token_FOR
                ||  yytoken ==  Token_RAISE
                ||  yytoken ==  Token_ASSERT
                ||  yytoken ==  Token_FROM
                ||  yytoken ==  Token_LAMBDA
                ||  yytoken ==  Token_RETURN
                ||  yytoken ==  Token_BREAK
                ||  yytoken ==  Token_GLOBAL
                ||  yytoken ==  Token_NOT
                ||  yytoken ==  Token_TRY
                ||  yytoken ==  Token_CLASS
                ||  yytoken ==  Token_IF
                ||  yytoken ==  Token_WHILE
                ||  yytoken ==  Token_CONTINUE
                ||  yytoken ==  Token_EXEC
                ||  yytoken ==  Token_IMPORT
                ||  yytoken ==  Token_PASS
                ||  yytoken ==  Token_YIELD
                ||  yytoken ==  Token_DEF
                ||  yytoken ==  Token_PRINT
                ||  yytoken ==  Token_LINEBREAK
                ||  yytoken ==  Token_STRINGLITERAL
                ||  yytoken ==  Token_IDENTIFIER
                ||  yytoken ==  Token_INTEGER
                ||  yytoken ==  Token_FLOAT
                ||  yytoken ==  Token_IMAGNUM
                ||  yytoken ==  Token_LPAREN
                ||  yytoken ==  Token_LBRACE
                ||  yytoken ==  Token_LBRACKET
                ||  yytoken ==  Token_AT
                ||  yytoken ==  Token_BACKTICK
                ||  yytoken ==  Token_PLUS
                ||  yytoken ==  Token_MINUS
                ||  yytoken ==  Token_TILDE)
          {
            stmt_ast *__node_123 =  0;

            if  (!parse_stmt(&__node_123))
              {
                yy_expected_symbol(ast_node::Kind_stmt,  "stmt");
                return  false;
              }

            (*yynode)->stmt_sequence =  snoc((*yynode)->stmt_sequence,  __node_123,  memory_pool);

          }

        if  (Token_EOF !=  yytoken)
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_raise_stmt(raise_stmt_ast **yynode)
  {
    *yynode =  create<raise_stmt_ast>();

    (*yynode)->start_token =  token_stream->index() -  1;

    if  (yytoken ==  Token_RAISE)
      {
        if  (yytoken !=  Token_RAISE)
          {
            yy_expected_token(yytoken,  Token_RAISE,  "raise");
            return  false;
          }

        yylex();

        if  (yytoken ==  Token_LAMBDA
             ||  yytoken ==  Token_NOT
             ||  yytoken ==  Token_STRINGLITERAL
             ||  yytoken ==  Token_IDENTIFIER
             ||  yytoken ==  Token_INTEGER
             ||  yytoken ==  Token_FLOAT
             ||  yytoken ==  Token_IMAGNUM
             ||  yytoken ==  Token_LPAREN
             ||  yytoken ==  Token_LBRACE
             ||  yytoken ==  Token_LBRACKET
             ||  yytoken ==  Token_BACKTICK
             ||  yytoken ==  Token_PLUS
             ||  yytoken ==  Token_MINUS
             ||  yytoken ==  Token_TILDE)
          {
            test_ast *__node_124 =  0;

            if  (!parse_test(&__node_124))
              {
                yy_expected_symbol(ast_node::Kind_test,  "test");
                return  false;
              }

            (*yynode)->type =  __node_124;

            if  (yytoken ==  Token_COMMA)
              {
                if  (yytoken !=  Token_COMMA)
                  {
                    yy_expected_token(yytoken,  Token_COMMA,  "comma");
                    return  false;
                  }

                yylex();

                test_ast *__node_125 =  0;

                if  (!parse_test(&__node_125))
                  {
                    yy_expected_symbol(ast_node::Kind_test,  "test");
                    return  false;
                  }

                (*yynode)->value =  __node_125;

                if  (yytoken ==  Token_COMMA)
                  {
                    if  (yytoken !=  Token_COMMA)
                      {
                        yy_expected_token(yytoken,  Token_COMMA,  "comma");
                        return  false;
                      }

                    yylex();

                    test_ast *__node_126 =  0;

                    if  (!parse_test(&__node_126))
                      {
                        yy_expected_symbol(ast_node::Kind_test,  "test");
                        return  false;
                      }

                    (*yynode)->traceback =  __node_126;

                  }

                else if  (true /*epsilon*/)
                {}
                else
                  {
                    return  false;
                  }
              }

            else if  (true /*epsilon*/)
            {}
            else
              {
                return  false;
              }
          }

        else if  (true /*epsilon*/)
        {}
        else
          {
            return  false;
          }
      }

    else
      {
        return  false;
      }

    (*yynode)->end_token =  token_stream->index() -  1;

    return  true;
  }

  bool parser::parse_return_stmt(return_stmt_ast **yynode)
                           {
                             *yynode =  create<return_stmt_ast>();

                             (*yynode)->start_token =  token_stream->index() -  1;

                             if  (yytoken ==  Token_RETURN)
                               {
                                 if  (yytoken !=  Token_RETURN)
                                   {
                                     yy_expected_token(yytoken,  Token_RETURN,  "returns");
                                     return  false;
                                   }

                                 yylex();

                                 if  (yytoken ==  Token_LAMBDA
                                      ||  yytoken ==  Token_NOT
                                      ||  yytoken ==  Token_STRINGLITERAL
                                      ||  yytoken ==  Token_IDENTIFIER
                                      ||  yytoken ==  Token_INTEGER
                                      ||  yytoken ==  Token_FLOAT
                                      ||  yytoken ==  Token_IMAGNUM
                                      ||  yytoken ==  Token_LPAREN
                                      ||  yytoken ==  Token_LBRACE
                                      ||  yytoken ==  Token_LBRACKET
                                      ||  yytoken ==  Token_BACKTICK
                                      ||  yytoken ==  Token_PLUS
                                      ||  yytoken ==  Token_MINUS
                                      ||  yytoken ==  Token_TILDE)
                                   {
                                     testlist_ast *__node_127 =  0;

                                     if  (!parse_testlist(&__node_127))
                                       {
                                         yy_expected_symbol(ast_node::Kind_testlist,  "testlist");
                                         return  false;
                                       }

                                     (*yynode)->return_expr =  __node_127;

                                   }

                                 else if  (true /*epsilon*/)
                                 {}
                                 else
                                   {
                                     return  false;
                                   }
                               }

                             else
                               {
                                 return  false;
                               }

                             (*yynode)->end_token =  token_stream->index() -  1;

                             return  true;
                           }

                           bool parser::parse_shift_expr(shift_expr_ast **yynode)
                           {
                             *yynode =  create<shift_expr_ast>();

                             (*yynode)->start_token =  token_stream->index() -  1;

                             if  (yytoken ==  Token_STRINGLITERAL
                                  ||  yytoken ==  Token_IDENTIFIER
                                  ||  yytoken ==  Token_INTEGER
                                  ||  yytoken ==  Token_FLOAT
                                  ||  yytoken ==  Token_IMAGNUM
                                  ||  yytoken ==  Token_LPAREN
                                  ||  yytoken ==  Token_LBRACE
                                  ||  yytoken ==  Token_LBRACKET
                                  ||  yytoken ==  Token_BACKTICK
                                  ||  yytoken ==  Token_PLUS
                                  ||  yytoken ==  Token_MINUS
                                  ||  yytoken ==  Token_TILDE)
                               {
                                 arith_expr_ast *__node_128 =  0;

                                 if  (!parse_arith_expr(&__node_128))
                                   {
                                     yy_expected_symbol(ast_node::Kind_arith_expr,  "arith_expr");
                                     return  false;
                                   }

                                 (*yynode)->arith_expr =  __node_128;

                                 while  (yytoken ==  Token_LSHIFT
                                         ||  yytoken ==  Token_RSHIFT)
                                   {
                                     shift_op_ast *__node_129 =  0;

                                     if  (!parse_shift_op(&__node_129))
                                       {
                                         yy_expected_symbol(ast_node::Kind_shift_op,  "shift_op");
                                         return  false;
                                       }

                                     (*yynode)->shift_op_list_sequence =  snoc((*yynode)->shift_op_list_sequence,  __node_129,  memory_pool);

                                     arith_expr_ast *__node_130 =  0;

                                     if  (!parse_arith_expr(&__node_130))
                                       {
                                         yy_expected_symbol(ast_node::Kind_arith_expr,  "arith_expr");
                                         return  false;
                                       }

                                     (*yynode)->arith_expr_list_sequence =  snoc((*yynode)->arith_expr_list_sequence,  __node_130,  memory_pool);

                                   }
                               }

                             else
                               {
                                 return  false;
                               }

                             (*yynode)->end_token =  token_stream->index() -  1;

                             return  true;
                           }

                           bool parser::parse_shift_op(shift_op_ast **yynode)
                           {
                             *yynode =  create<shift_op_ast>();

                             (*yynode)->start_token =  token_stream->index() -  1;

                             if  (yytoken ==  Token_LSHIFT
                                  ||  yytoken ==  Token_RSHIFT)
                               {
                                 if  (yytoken ==  Token_LSHIFT)
                                   {
                                     if  (yytoken !=  Token_LSHIFT)
                                       {
                                         yy_expected_token(yytoken,  Token_LSHIFT,  "lshift");
                                         return  false;
                                       }

                                     yylex();

                                     (*yynode)->shift_operator =  Python::op_lshift;
                                   }

                                 else if  (yytoken ==  Token_RSHIFT)
                                   {
                                     if  (yytoken !=  Token_RSHIFT)
                                       {
                                         yy_expected_token(yytoken,  Token_RSHIFT,  "rshift");
                                         return  false;
                                       }

                                     yylex();

                                     (*yynode)->shift_operator =  Python::op_rshift;
                                   }

                                 else
                                   {
                                     return  false;
                                   }
                               }

                             else
                               {
                                 return  false;
                               }

                             (*yynode)->end_token =  token_stream->index() -  1;

                             return  true;
                           }

                           bool parser::parse_simple_stmt(simple_stmt_ast **yynode)
                           {
                             *yynode =  create<simple_stmt_ast>();

                             (*yynode)->start_token =  token_stream->index() -  1;

                             if  (yytoken ==  Token_DEL
                                  ||  yytoken ==  Token_RAISE
                                  ||  yytoken ==  Token_ASSERT
                                  ||  yytoken ==  Token_FROM
                                  ||  yytoken ==  Token_LAMBDA
                                  ||  yytoken ==  Token_RETURN
                                  ||  yytoken ==  Token_BREAK
                                  ||  yytoken ==  Token_GLOBAL
                                  ||  yytoken ==  Token_NOT
                                  ||  yytoken ==  Token_CONTINUE
                                  ||  yytoken ==  Token_EXEC
                                  ||  yytoken ==  Token_IMPORT
                                  ||  yytoken ==  Token_PASS
                                  ||  yytoken ==  Token_YIELD
                                  ||  yytoken ==  Token_PRINT
                                  ||  yytoken ==  Token_STRINGLITERAL
                                  ||  yytoken ==  Token_IDENTIFIER
                                  ||  yytoken ==  Token_INTEGER
                                  ||  yytoken ==  Token_FLOAT
                                  ||  yytoken ==  Token_IMAGNUM
                                  ||  yytoken ==  Token_LPAREN
                                  ||  yytoken ==  Token_LBRACE
                                  ||  yytoken ==  Token_LBRACKET
                                  ||  yytoken ==  Token_BACKTICK
                                  ||  yytoken ==  Token_PLUS
                                  ||  yytoken ==  Token_MINUS
                                  ||  yytoken ==  Token_TILDE)
                               {
                                 small_stmt_ast *__node_131 =  0;

                                 if  (!parse_small_stmt(&__node_131))
                                   {
                                     yy_expected_symbol(ast_node::Kind_small_stmt,  "small_stmt");
                                     return  false;
                                   }

                                 (*yynode)->small_stmt_sequence =  snoc((*yynode)->small_stmt_sequence,  __node_131,  memory_pool);

                                 while  (yytoken ==  Token_SEMICOLON)
                                   {
                                     if  (yytoken !=  Token_SEMICOLON)
                                       {
                                         yy_expected_token(yytoken,  Token_SEMICOLON,  "semicolon");
                                         return  false;
                                       }

                                     yylex();

                                     if ( yytoken ==  Token_LINEBREAK ||  yytoken ==  Token_DEDENT)
                                       {
                                         break;
                                       }

                                     small_stmt_ast *__node_132 =  0;

                                     if  (!parse_small_stmt(&__node_132))
                                       {
                                         yy_expected_symbol(ast_node::Kind_small_stmt,  "small_stmt");
                                         return  false;
                                       }

                                     (*yynode)->small_stmt_sequence =  snoc((*yynode)->small_stmt_sequence,  __node_132,  memory_pool);

                                   }

                                 if  (yytoken !=  Token_LINEBREAK)
                                   {
                                     yy_expected_token(yytoken,  Token_LINEBREAK,  "linebreak");
                                     return  false;
                                   }

                                 yylex();

                               }

                             else
                               {
                                 return  false;
                               }

                             (*yynode)->end_token =  token_stream->index() -  1;

                             return  true;
                           }

                           bool parser::parse_sliceop(sliceop_ast **yynode)
                           {
                             *yynode =  create<sliceop_ast>();

                             (*yynode)->start_token =  token_stream->index() -  1;

                             if  (yytoken ==  Token_COLON)
                               {
                                 if  (yytoken !=  Token_COLON)
                                   {
                                     yy_expected_token(yytoken,  Token_COLON,  "colon");
                                     return  false;
                                   }

                                 yylex();

                                 if  (yytoken ==  Token_LAMBDA
                                      ||  yytoken ==  Token_NOT
                                      ||  yytoken ==  Token_STRINGLITERAL
                                      ||  yytoken ==  Token_IDENTIFIER
                                      ||  yytoken ==  Token_INTEGER
                                      ||  yytoken ==  Token_FLOAT
                                      ||  yytoken ==  Token_IMAGNUM
                                      ||  yytoken ==  Token_LPAREN
                                      ||  yytoken ==  Token_LBRACE
                                      ||  yytoken ==  Token_LBRACKET
                                      ||  yytoken ==  Token_BACKTICK
                                      ||  yytoken ==  Token_PLUS
                                      ||  yytoken ==  Token_MINUS
                                      ||  yytoken ==  Token_TILDE)
                                   {
                                     test_ast *__node_133 =  0;

                                     if  (!parse_test(&__node_133))
                                       {
                                         yy_expected_symbol(ast_node::Kind_test,  "test");
                                         return  false;
                                       }

                                     (*yynode)->slice_test =  __node_133;

                                   }

                                 else if  (true /*epsilon*/)
                                 {}
                                 else
                                   {
                                     return  false;
                                   }
                               }

                             else
                               {
                                 return  false;
                               }

                             (*yynode)->end_token =  token_stream->index() -  1;

                             return  true;
                           }

                           bool parser::parse_small_stmt(small_stmt_ast **yynode)
                           {
                             *yynode =  create<small_stmt_ast>();

                             (*yynode)->start_token =  token_stream->index() -  1;

                             if  (yytoken ==  Token_DEL
                                  ||  yytoken ==  Token_RAISE
                                  ||  yytoken ==  Token_ASSERT
                                  ||  yytoken ==  Token_FROM
                                  ||  yytoken ==  Token_LAMBDA
                                  ||  yytoken ==  Token_RETURN
                                  ||  yytoken ==  Token_BREAK
                                  ||  yytoken ==  Token_GLOBAL
                                  ||  yytoken ==  Token_NOT
                                  ||  yytoken ==  Token_CONTINUE
                                  ||  yytoken ==  Token_EXEC
                                  ||  yytoken ==  Token_IMPORT
                                  ||  yytoken ==  Token_PASS
                                  ||  yytoken ==  Token_YIELD
                                  ||  yytoken ==  Token_PRINT
                                  ||  yytoken ==  Token_STRINGLITERAL
                                  ||  yytoken ==  Token_IDENTIFIER
                                  ||  yytoken ==  Token_INTEGER
                                  ||  yytoken ==  Token_FLOAT
                                  ||  yytoken ==  Token_IMAGNUM
                                  ||  yytoken ==  Token_LPAREN
                                  ||  yytoken ==  Token_LBRACE
                                  ||  yytoken ==  Token_LBRACKET
                                  ||  yytoken ==  Token_BACKTICK
                                  ||  yytoken ==  Token_PLUS
                                  ||  yytoken ==  Token_MINUS
                                  ||  yytoken ==  Token_TILDE)
                               {
                                 if  (yytoken ==  Token_LAMBDA
                                      ||  yytoken ==  Token_NOT
                                      ||  yytoken ==  Token_STRINGLITERAL
                                      ||  yytoken ==  Token_IDENTIFIER
                                      ||  yytoken ==  Token_INTEGER
                                      ||  yytoken ==  Token_FLOAT
                                      ||  yytoken ==  Token_IMAGNUM
                                      ||  yytoken ==  Token_LPAREN
                                      ||  yytoken ==  Token_LBRACE
                                      ||  yytoken ==  Token_LBRACKET
                                      ||  yytoken ==  Token_BACKTICK
                                      ||  yytoken ==  Token_PLUS
                                      ||  yytoken ==  Token_MINUS
                                      ||  yytoken ==  Token_TILDE)
                                   {
                                     expr_stmt_ast *__node_134 =  0;

                                     if  (!parse_expr_stmt(&__node_134))
                                       {
                                         yy_expected_symbol(ast_node::Kind_expr_stmt,  "expr_stmt");
                                         return  false;
                                       }

                                     (*yynode)->expr_stmt =  __node_134;

                                   }

                                 else if  (yytoken ==  Token_PRINT)
                                   {
                                     print_stmt_ast *__node_135 =  0;

                                     if  (!parse_print_stmt(&__node_135))
                                       {
                                         yy_expected_symbol(ast_node::Kind_print_stmt,  "print_stmt");
                                         return  false;
                                       }

                                     (*yynode)->print_stmt =  __node_135;

                                   }

                                 else if  (yytoken ==  Token_DEL)
                                   {
                                     del_stmt_ast *__node_136 =  0;

                                     if  (!parse_del_stmt(&__node_136))
                                       {
                                         yy_expected_symbol(ast_node::Kind_del_stmt,  "del_stmt");
                                         return  false;
                                       }

                                     (*yynode)->del_stmt =  __node_136;

                                   }

                                 else if  (yytoken ==  Token_PASS)
                                   {
                                     pass_stmt_ast *__node_137 =  0;

                                     if  (!parse_pass_stmt(&__node_137))
                                       {
                                         yy_expected_symbol(ast_node::Kind_pass_stmt,  "pass_stmt");
                                         return  false;
                                       }

                                     (*yynode)->pass_stmt =  __node_137;

                                   }

                                 else if  (yytoken ==  Token_RAISE
                                           ||  yytoken ==  Token_RETURN
                                           ||  yytoken ==  Token_BREAK
                                           ||  yytoken ==  Token_CONTINUE
                                           ||  yytoken ==  Token_YIELD)
                                   {
                                     flow_stmt_ast *__node_138 =  0;

                                     if  (!parse_flow_stmt(&__node_138))
                                       {
                                         yy_expected_symbol(ast_node::Kind_flow_stmt,  "flow_stmt");
                                         return  false;
                                       }

                                     (*yynode)->flow_stmt =  __node_138;

                                   }

                                 else if  (yytoken ==  Token_FROM
                                           ||  yytoken ==  Token_IMPORT)
                                   {
                                     import_stmt_ast *__node_139 =  0;

                                     if  (!parse_import_stmt(&__node_139))
                                       {
                                         yy_expected_symbol(ast_node::Kind_import_stmt,  "import_stmt");
                                         return  false;
                                       }

                                     (*yynode)->import_stmt =  __node_139;

                                   }

                                 else if  (yytoken ==  Token_GLOBAL)
                                   {
                                     global_stmt_ast *__node_140 =  0;

                                     if  (!parse_global_stmt(&__node_140))
                                       {
                                         yy_expected_symbol(ast_node::Kind_global_stmt,  "global_stmt");
                                         return  false;
                                       }

                                     (*yynode)->global_stmt =  __node_140;

                                   }

                                 else if  (yytoken ==  Token_EXEC)
                                   {
                                     exec_stmt_ast *__node_141 =  0;

                                     if  (!parse_exec_stmt(&__node_141))
                                       {
                                         yy_expected_symbol(ast_node::Kind_exec_stmt,  "exec_stmt");
                                         return  false;
                                       }

                                     (*yynode)->exec_stmt =  __node_141;

                                   }

                                 else if  (yytoken ==  Token_ASSERT)
                                   {
                                     assert_stmt_ast *__node_142 =  0;

                                     if  (!parse_assert_stmt(&__node_142))
                                       {
                                         yy_expected_symbol(ast_node::Kind_assert_stmt,  "assert_stmt");
                                         return  false;
                                       }

                                     (*yynode)->assert_stmt =  __node_142;

                                   }

                                 else
                                   {
                                     return  false;
                                   }
                               }

                             else
                               {
                                 return  false;
                               }

                             (*yynode)->end_token =  token_stream->index() -  1;

                             return  true;
                           }

                           bool parser::parse_stmt(stmt_ast **yynode)
                           {
                             *yynode =  create<stmt_ast>();

                             (*yynode)->start_token =  token_stream->index() -  1;

                             if  (yytoken ==  Token_DEL
                                  ||  yytoken ==  Token_FOR
                                  ||  yytoken ==  Token_RAISE
                                  ||  yytoken ==  Token_ASSERT
                                  ||  yytoken ==  Token_FROM
                                  ||  yytoken ==  Token_LAMBDA
                                  ||  yytoken ==  Token_RETURN
                                  ||  yytoken ==  Token_BREAK
                                  ||  yytoken ==  Token_GLOBAL
                                  ||  yytoken ==  Token_NOT
                                  ||  yytoken ==  Token_TRY
                                  ||  yytoken ==  Token_CLASS
                                  ||  yytoken ==  Token_IF
                                  ||  yytoken ==  Token_WHILE
                                  ||  yytoken ==  Token_CONTINUE
                                  ||  yytoken ==  Token_EXEC
                                  ||  yytoken ==  Token_IMPORT
                                  ||  yytoken ==  Token_PASS
                                  ||  yytoken ==  Token_YIELD
                                  ||  yytoken ==  Token_DEF
                                  ||  yytoken ==  Token_PRINT
                                  ||  yytoken ==  Token_LINEBREAK
                                  ||  yytoken ==  Token_STRINGLITERAL
                                  ||  yytoken ==  Token_IDENTIFIER
                                  ||  yytoken ==  Token_INTEGER
                                  ||  yytoken ==  Token_FLOAT
                                  ||  yytoken ==  Token_IMAGNUM
                                  ||  yytoken ==  Token_LPAREN
                                  ||  yytoken ==  Token_LBRACE
                                  ||  yytoken ==  Token_LBRACKET
                                  ||  yytoken ==  Token_AT
                                  ||  yytoken ==  Token_BACKTICK
                                  ||  yytoken ==  Token_PLUS
                                  ||  yytoken ==  Token_MINUS
                                  ||  yytoken ==  Token_TILDE)
                               {
                                 if  (yytoken ==  Token_DEL
                                      ||  yytoken ==  Token_RAISE
                                      ||  yytoken ==  Token_ASSERT
                                      ||  yytoken ==  Token_FROM
                                      ||  yytoken ==  Token_LAMBDA
                                      ||  yytoken ==  Token_RETURN
                                      ||  yytoken ==  Token_BREAK
                                      ||  yytoken ==  Token_GLOBAL
                                      ||  yytoken ==  Token_NOT
                                      ||  yytoken ==  Token_CONTINUE
                                      ||  yytoken ==  Token_EXEC
                                      ||  yytoken ==  Token_IMPORT
                                      ||  yytoken ==  Token_PASS
                                      ||  yytoken ==  Token_YIELD
                                      ||  yytoken ==  Token_PRINT
                                      ||  yytoken ==  Token_STRINGLITERAL
                                      ||  yytoken ==  Token_IDENTIFIER
                                      ||  yytoken ==  Token_INTEGER
                                      ||  yytoken ==  Token_FLOAT
                                      ||  yytoken ==  Token_IMAGNUM
                                      ||  yytoken ==  Token_LPAREN
                                      ||  yytoken ==  Token_LBRACE
                                      ||  yytoken ==  Token_LBRACKET
                                      ||  yytoken ==  Token_BACKTICK
                                      ||  yytoken ==  Token_PLUS
                                      ||  yytoken ==  Token_MINUS
                                      ||  yytoken ==  Token_TILDE)
                                   {
                                     simple_stmt_ast *__node_143 =  0;

                                     if  (!parse_simple_stmt(&__node_143))
                                       {
                                         yy_expected_symbol(ast_node::Kind_simple_stmt,  "simple_stmt");
                                         return  false;
                                       }

                                     (*yynode)->simple_stmt =  __node_143;

                                   }

                                 else if  (yytoken ==  Token_FOR
                                           ||  yytoken ==  Token_TRY
                                           ||  yytoken ==  Token_CLASS
                                           ||  yytoken ==  Token_IF
                                           ||  yytoken ==  Token_WHILE
                                           ||  yytoken ==  Token_DEF
                                           ||  yytoken ==  Token_AT)
                                   {
                                     compound_stmt_ast *__node_144 =  0;

                                     if  (!parse_compound_stmt(&__node_144))
                                       {
                                         yy_expected_symbol(ast_node::Kind_compound_stmt,  "compound_stmt");
                                         return  false;
                                       }

                                     (*yynode)->compound_stmt =  __node_144;

                                   }

                                 else if  (yytoken ==  Token_LINEBREAK)
                                   {
                                     if  (yytoken !=  Token_LINEBREAK)
                                       {
                                         yy_expected_token(yytoken,  Token_LINEBREAK,  "linebreak");
                                         return  false;
                                       }

                                     yylex();

                                   }

                                 else
                                   {
                                     return  false;
                                   }
                               }

                             else
                               {
                                 return  false;
                               }

                             (*yynode)->end_token =  token_stream->index() -  1;

                             return  true;
                           }

                           bool parser::parse_subscript(subscript_ast **yynode)
                           {
                             *yynode =  create<subscript_ast>();

                             (*yynode)->start_token =  token_stream->index() -  1;

                             if  (yytoken ==  Token_LAMBDA
                                  ||  yytoken ==  Token_NOT
                                  ||  yytoken ==  Token_STRINGLITERAL
                                  ||  yytoken ==  Token_IDENTIFIER
                                  ||  yytoken ==  Token_INTEGER
                                  ||  yytoken ==  Token_FLOAT
                                  ||  yytoken ==  Token_IMAGNUM
                                  ||  yytoken ==  Token_LPAREN
                                  ||  yytoken ==  Token_LBRACE
                                  ||  yytoken ==  Token_LBRACKET
                                  ||  yytoken ==  Token_COLON
                                  ||  yytoken ==  Token_BACKTICK
                                  ||  yytoken ==  Token_ELLIPSIS
                                  ||  yytoken ==  Token_PLUS
                                  ||  yytoken ==  Token_MINUS
                                  ||  yytoken ==  Token_TILDE ||  yytoken ==  Token_RBRACKET
                                  ||  yytoken ==  Token_COMMA)
                               {
                                 if  (yytoken ==  Token_ELLIPSIS)
                                   {
                                     if  (yytoken !=  Token_ELLIPSIS)
                                       {
                                         yy_expected_token(yytoken,  Token_ELLIPSIS,  "ellipsis");
                                         return  false;
                                       }

                                     (*yynode)->subcript_ellipsis =  token_stream->index() -  1;
                                     yylex();

                                   }

                                 else if  (yytoken ==  Token_LAMBDA
                                           ||  yytoken ==  Token_NOT
                                           ||  yytoken ==  Token_STRINGLITERAL
                                           ||  yytoken ==  Token_IDENTIFIER
                                           ||  yytoken ==  Token_INTEGER
                                           ||  yytoken ==  Token_FLOAT
                                           ||  yytoken ==  Token_IMAGNUM
                                           ||  yytoken ==  Token_LPAREN
                                           ||  yytoken ==  Token_LBRACE
                                           ||  yytoken ==  Token_LBRACKET
                                           ||  yytoken ==  Token_COLON
                                           ||  yytoken ==  Token_BACKTICK
                                           ||  yytoken ==  Token_PLUS
                                           ||  yytoken ==  Token_MINUS
                                           ||  yytoken ==  Token_TILDE)
                                   {
                                     if  ((yytoken ==  Token_LAMBDA
                                           ||  yytoken ==  Token_NOT
                                           ||  yytoken ==  Token_STRINGLITERAL
                                           ||  yytoken ==  Token_IDENTIFIER
                                           ||  yytoken ==  Token_INTEGER
                                           ||  yytoken ==  Token_FLOAT
                                           ||  yytoken ==  Token_IMAGNUM
                                           ||  yytoken ==  Token_LPAREN
                                           ||  yytoken ==  Token_LBRACE
                                           ||  yytoken ==  Token_LBRACKET
                                           ||  yytoken ==  Token_BACKTICK
                                           ||  yytoken ==  Token_PLUS
                                           ||  yytoken ==  Token_MINUS
                                           ||  yytoken ==  Token_TILDE) &&  ( yytoken !=  Token_COLON ))
                                       {
                                         test_ast *__node_145 =  0;

                                         if  (!parse_test(&__node_145))
                                           {
                                             yy_expected_symbol(ast_node::Kind_test,  "test");
                                             return  false;
                                           }

                                         (*yynode)->sub_test =  __node_145;

                                       }

                                     else if  (true /*epsilon*/)
                                     {}
                                     else
                                       {
                                         return  false;
                                       }

                                     if  ((true /*epsilon*/) &&  ( yytoken ==  Token_RBRACKET ||  yytoken ==  Token_COMMA ))
                                     {}
                                     else if  (yytoken ==  Token_COLON)
                                       {
                                         if  (yytoken !=  Token_COLON)
                                           {
                                             yy_expected_token(yytoken,  Token_COLON,  "colon");
                                             return  false;
                                           }

                                         yylex();

                                         if  (yytoken ==  Token_LAMBDA
                                              ||  yytoken ==  Token_NOT
                                              ||  yytoken ==  Token_STRINGLITERAL
                                              ||  yytoken ==  Token_IDENTIFIER
                                              ||  yytoken ==  Token_INTEGER
                                              ||  yytoken ==  Token_FLOAT
                                              ||  yytoken ==  Token_IMAGNUM
                                              ||  yytoken ==  Token_LPAREN
                                              ||  yytoken ==  Token_LBRACE
                                              ||  yytoken ==  Token_LBRACKET
                                              ||  yytoken ==  Token_BACKTICK
                                              ||  yytoken ==  Token_PLUS
                                              ||  yytoken ==  Token_MINUS
                                              ||  yytoken ==  Token_TILDE)
                                           {
                                             test_ast *__node_146 =  0;

                                             if  (!parse_test(&__node_146))
                                               {
                                                 yy_expected_symbol(ast_node::Kind_test,  "test");
                                                 return  false;
                                               }

                                             (*yynode)->sub_colon_test =  __node_146;

                                           }

                                         else if  (true /*epsilon*/)
                                         {}
                                         else
                                           {
                                             return  false;
                                           }

                                         if  (yytoken ==  Token_COLON)
                                           {
                                             sliceop_ast *__node_147 =  0;

                                             if  (!parse_sliceop(&__node_147))
                                               {
                                                 yy_expected_symbol(ast_node::Kind_sliceop,  "sliceop");
                                                 return  false;
                                               }

                                             (*yynode)->sliceop =  __node_147;

                                           }

                                         else if  (true /*epsilon*/)
                                         {}
                                         else
                                           {
                                             return  false;
                                           }
                                       }

                                     else
                                       {
                                         return  false;
                                       }
                                   }

                                 else
                                   {
                                     return  false;
                                   }
                               }

                             else
                               {
                                 return  false;
                               }

                             (*yynode)->end_token =  token_stream->index() -  1;

                             return  true;
                           }

                           bool parser::parse_subscriptlist(subscriptlist_ast **yynode)
                           {
                             *yynode =  create<subscriptlist_ast>();

                             (*yynode)->start_token =  token_stream->index() -  1;

                             if  (yytoken ==  Token_LAMBDA
                                  ||  yytoken ==  Token_NOT
                                  ||  yytoken ==  Token_STRINGLITERAL
                                  ||  yytoken ==  Token_IDENTIFIER
                                  ||  yytoken ==  Token_INTEGER
                                  ||  yytoken ==  Token_FLOAT
                                  ||  yytoken ==  Token_IMAGNUM
                                  ||  yytoken ==  Token_LPAREN
                                  ||  yytoken ==  Token_LBRACE
                                  ||  yytoken ==  Token_LBRACKET
                                  ||  yytoken ==  Token_COMMA
                                  ||  yytoken ==  Token_COLON
                                  ||  yytoken ==  Token_BACKTICK
                                  ||  yytoken ==  Token_ELLIPSIS
                                  ||  yytoken ==  Token_PLUS
                                  ||  yytoken ==  Token_MINUS
                                  ||  yytoken ==  Token_TILDE ||  yytoken ==  Token_RBRACKET)
                               {
                                 subscript_ast *__node_148 =  0;

                                 if  (!parse_subscript(&__node_148))
                                   {
                                     yy_expected_symbol(ast_node::Kind_subscript,  "subscript");
                                     return  false;
                                   }

                                 (*yynode)->subscript_sequence =  snoc((*yynode)->subscript_sequence,  __node_148,  memory_pool);

                                 while  (yytoken ==  Token_COMMA)
                                   {
                                     if  (yytoken !=  Token_COMMA)
                                       {
                                         yy_expected_token(yytoken,  Token_COMMA,  "comma");
                                         return  false;
                                       }

                                     yylex();

                                     if  (yytoken ==  Token_RBRACKET)
                                       {
                                         break;
                                       }

                                     subscript_ast *__node_149 =  0;

                                     if  (!parse_subscript(&__node_149))
                                       {
                                         yy_expected_symbol(ast_node::Kind_subscript,  "subscript");
                                         return  false;
                                       }

                                     (*yynode)->subscript_sequence =  snoc((*yynode)->subscript_sequence,  __node_149,  memory_pool);

                                   }
                               }

                             else
                               {
                                 return  false;
                               }

                             (*yynode)->end_token =  token_stream->index() -  1;

                             return  true;
                           }

                           bool parser::parse_suite(suite_ast **yynode)
                           {
                             *yynode =  create<suite_ast>();

                             (*yynode)->start_token =  token_stream->index() -  1;

                             if  (yytoken ==  Token_DEL
                                  ||  yytoken ==  Token_RAISE
                                  ||  yytoken ==  Token_ASSERT
                                  ||  yytoken ==  Token_FROM
                                  ||  yytoken ==  Token_LAMBDA
                                  ||  yytoken ==  Token_RETURN
                                  ||  yytoken ==  Token_BREAK
                                  ||  yytoken ==  Token_GLOBAL
                                  ||  yytoken ==  Token_NOT
                                  ||  yytoken ==  Token_CONTINUE
                                  ||  yytoken ==  Token_EXEC
                                  ||  yytoken ==  Token_IMPORT
                                  ||  yytoken ==  Token_PASS
                                  ||  yytoken ==  Token_YIELD
                                  ||  yytoken ==  Token_PRINT
                                  ||  yytoken ==  Token_LINEBREAK
                                  ||  yytoken ==  Token_STRINGLITERAL
                                  ||  yytoken ==  Token_IDENTIFIER
                                  ||  yytoken ==  Token_INTEGER
                                  ||  yytoken ==  Token_FLOAT
                                  ||  yytoken ==  Token_IMAGNUM
                                  ||  yytoken ==  Token_LPAREN
                                  ||  yytoken ==  Token_LBRACE
                                  ||  yytoken ==  Token_LBRACKET
                                  ||  yytoken ==  Token_BACKTICK
                                  ||  yytoken ==  Token_PLUS
                                  ||  yytoken ==  Token_MINUS
                                  ||  yytoken ==  Token_TILDE)
                               {
                                 if  (yytoken ==  Token_DEL
                                      ||  yytoken ==  Token_RAISE
                                      ||  yytoken ==  Token_ASSERT
                                      ||  yytoken ==  Token_FROM
                                      ||  yytoken ==  Token_LAMBDA
                                      ||  yytoken ==  Token_RETURN
                                      ||  yytoken ==  Token_BREAK
                                      ||  yytoken ==  Token_GLOBAL
                                      ||  yytoken ==  Token_NOT
                                      ||  yytoken ==  Token_CONTINUE
                                      ||  yytoken ==  Token_EXEC
                                      ||  yytoken ==  Token_IMPORT
                                      ||  yytoken ==  Token_PASS
                                      ||  yytoken ==  Token_YIELD
                                      ||  yytoken ==  Token_PRINT
                                      ||  yytoken ==  Token_STRINGLITERAL
                                      ||  yytoken ==  Token_IDENTIFIER
                                      ||  yytoken ==  Token_INTEGER
                                      ||  yytoken ==  Token_FLOAT
                                      ||  yytoken ==  Token_IMAGNUM
                                      ||  yytoken ==  Token_LPAREN
                                      ||  yytoken ==  Token_LBRACE
                                      ||  yytoken ==  Token_LBRACKET
                                      ||  yytoken ==  Token_BACKTICK
                                      ||  yytoken ==  Token_PLUS
                                      ||  yytoken ==  Token_MINUS
                                      ||  yytoken ==  Token_TILDE)
                                   {
                                     simple_stmt_ast *__node_150 =  0;

                                     if  (!parse_simple_stmt(&__node_150))
                                       {
                                         yy_expected_symbol(ast_node::Kind_simple_stmt,  "simple_stmt");
                                         return  false;
                                       }

                                     (*yynode)->simple_stmt =  __node_150;

                                   }

                                 else if  (yytoken ==  Token_LINEBREAK)
                                   {
                                     do
                                       {
                                         if  (yytoken !=  Token_LINEBREAK)
                                           {
                                             yy_expected_token(yytoken,  Token_LINEBREAK,  "linebreak");
                                             return  false;
                                           }

                                         yylex();

                                       }

                                     while  (yytoken ==  Token_LINEBREAK);
                                     if  (yytoken !=  Token_INDENT)
                                       {
                                         yy_expected_token(yytoken,  Token_INDENT,  "indent");
                                         return  false;
                                       }

                                     yylex();

                                     do
                                       {
                                         stmt_ast *__node_151 =  0;

                                         if  (!parse_stmt(&__node_151))
                                           {
                                             yy_expected_symbol(ast_node::Kind_stmt,  "stmt");
                                             return  false;
                                           }

                                         (*yynode)->stmt_sequence =  snoc((*yynode)->stmt_sequence,  __node_151,  memory_pool);

                                       }

                                     while  (yytoken ==  Token_DEL
                                             ||  yytoken ==  Token_FOR
                                             ||  yytoken ==  Token_RAISE
                                             ||  yytoken ==  Token_ASSERT
                                             ||  yytoken ==  Token_FROM
                                             ||  yytoken ==  Token_LAMBDA
                                             ||  yytoken ==  Token_RETURN
                                             ||  yytoken ==  Token_BREAK
                                             ||  yytoken ==  Token_GLOBAL
                                             ||  yytoken ==  Token_NOT
                                             ||  yytoken ==  Token_TRY
                                             ||  yytoken ==  Token_CLASS
                                             ||  yytoken ==  Token_IF
                                             ||  yytoken ==  Token_WHILE
                                             ||  yytoken ==  Token_CONTINUE
                                             ||  yytoken ==  Token_EXEC
                                             ||  yytoken ==  Token_IMPORT
                                             ||  yytoken ==  Token_PASS
                                             ||  yytoken ==  Token_YIELD
                                             ||  yytoken ==  Token_DEF
                                             ||  yytoken ==  Token_PRINT
                                             ||  yytoken ==  Token_LINEBREAK
                                             ||  yytoken ==  Token_STRINGLITERAL
                                             ||  yytoken ==  Token_IDENTIFIER
                                             ||  yytoken ==  Token_INTEGER
                                             ||  yytoken ==  Token_FLOAT
                                             ||  yytoken ==  Token_IMAGNUM
                                             ||  yytoken ==  Token_LPAREN
                                             ||  yytoken ==  Token_LBRACE
                                             ||  yytoken ==  Token_LBRACKET
                                             ||  yytoken ==  Token_AT
                                             ||  yytoken ==  Token_BACKTICK
                                             ||  yytoken ==  Token_PLUS
                                             ||  yytoken ==  Token_MINUS
                                             ||  yytoken ==  Token_TILDE);
                                     if  (yytoken !=  Token_DEDENT)
                                       {
                                         yy_expected_token(yytoken,  Token_DEDENT,  "dedent");
                                         return  false;
                                       }

                                     yylex();

                                   }

                                 else
                                   {
                                     return  false;
                                   }
                               }

                             else
                               {
                                 return  false;
                               }

                             (*yynode)->end_token =  token_stream->index() -  1;

                             return  true;
                           }

                           bool parser::parse_term(term_ast **yynode)
                           {
                             *yynode =  create<term_ast>();

                             (*yynode)->start_token =  token_stream->index() -  1;

                             if  (yytoken ==  Token_STRINGLITERAL
                                  ||  yytoken ==  Token_IDENTIFIER
                                  ||  yytoken ==  Token_INTEGER
                                  ||  yytoken ==  Token_FLOAT
                                  ||  yytoken ==  Token_IMAGNUM
                                  ||  yytoken ==  Token_LPAREN
                                  ||  yytoken ==  Token_LBRACE
                                  ||  yytoken ==  Token_LBRACKET
                                  ||  yytoken ==  Token_BACKTICK
                                  ||  yytoken ==  Token_PLUS
                                  ||  yytoken ==  Token_MINUS
                                  ||  yytoken ==  Token_TILDE)
                               {
                                 factor_ast *__node_152 =  0;

                                 if  (!parse_factor(&__node_152))
                                   {
                                     yy_expected_symbol(ast_node::Kind_factor,  "factor");
                                     return  false;
                                   }

                                 (*yynode)->factor =  __node_152;

                                 if  (yytoken ==  Token_STAR
                                      ||  yytoken ==  Token_SLASH
                                      ||  yytoken ==  Token_DOUBLESLASH
                                      ||  yytoken ==  Token_MODULO)
                                   {
                                     do
                                       {
                                         term_op_ast *__node_153 =  0;

                                         if  (!parse_term_op(&__node_153))
                                           {
                                             yy_expected_symbol(ast_node::Kind_term_op,  "term_op");
                                             return  false;
                                           }

                                         (*yynode)->term_op_list_sequence =  snoc((*yynode)->term_op_list_sequence,  __node_153,  memory_pool);

                                         factor_ast *__node_154 =  0;

                                         if  (!parse_factor(&__node_154))
                                           {
                                             yy_expected_symbol(ast_node::Kind_factor,  "factor");
                                             return  false;
                                           }

                                         (*yynode)->factor_list_sequence =  snoc((*yynode)->factor_list_sequence,  __node_154,  memory_pool);

                                       }

                                     while  (yytoken ==  Token_STAR
                                             ||  yytoken ==  Token_SLASH
                                             ||  yytoken ==  Token_DOUBLESLASH
                                             ||  yytoken ==  Token_MODULO);
                                   }

                                 else if  (true /*epsilon*/)
                                 {}
                                 else
                                   {
                                     return  false;
                                   }
                               }

                             else
                               {
                                 return  false;
                               }

                             (*yynode)->end_token =  token_stream->index() -  1;

                             return  true;
                           }

                           bool parser::parse_term_op(term_op_ast **yynode)
                           {
                             *yynode =  create<term_op_ast>();

                             (*yynode)->start_token =  token_stream->index() -  1;

                             if  (yytoken ==  Token_STAR
                                  ||  yytoken ==  Token_SLASH
                                  ||  yytoken ==  Token_DOUBLESLASH
                                  ||  yytoken ==  Token_MODULO)
                               {
                                 if  (yytoken ==  Token_STAR)
                                   {
                                     if  (yytoken !=  Token_STAR)
                                       {
                                         yy_expected_token(yytoken,  Token_STAR,  "star");
                                         return  false;
                                       }

                                     yylex();

                                     (*yynode)->term_operator =  Python::op_star;
                                   }

                                 else if  (yytoken ==  Token_SLASH)
                                   {
                                     if  (yytoken !=  Token_SLASH)
                                       {
                                         yy_expected_token(yytoken,  Token_SLASH,  "slash");
                                         return  false;
                                       }

                                     yylex();

                                     (*yynode)->term_operator =  Python::op_slash;
                                   }

                                 else if  (yytoken ==  Token_MODULO)
                                   {
                                     if  (yytoken !=  Token_MODULO)
                                       {
                                         yy_expected_token(yytoken,  Token_MODULO,  "modulo");
                                         return  false;
                                       }

                                     yylex();

                                     (*yynode)->term_operator =  Python::op_modulo;
                                   }

                                 else if  (yytoken ==  Token_DOUBLESLASH)
                                   {
                                     if  (yytoken !=  Token_DOUBLESLASH)
                                       {
                                         yy_expected_token(yytoken,  Token_DOUBLESLASH,  "doubleslash");
                                         return  false;
                                       }

                                     yylex();

                                     (*yynode)->term_operator =  Python::op_doubleslash;
                                   }

                                 else
                                   {
                                     return  false;
                                   }
                               }

                             else
                               {
                                 return  false;
                               }

                             (*yynode)->end_token =  token_stream->index() -  1;

                             return  true;
                           }

                           bool parser::parse_test(test_ast **yynode)
                           {
                             *yynode =  create<test_ast>();

                             (*yynode)->start_token =  token_stream->index() -  1;

                             if  (yytoken ==  Token_LAMBDA
                                  ||  yytoken ==  Token_NOT
                                  ||  yytoken ==  Token_STRINGLITERAL
                                  ||  yytoken ==  Token_IDENTIFIER
                                  ||  yytoken ==  Token_INTEGER
                                  ||  yytoken ==  Token_FLOAT
                                  ||  yytoken ==  Token_IMAGNUM
                                  ||  yytoken ==  Token_LPAREN
                                  ||  yytoken ==  Token_LBRACE
                                  ||  yytoken ==  Token_LBRACKET
                                  ||  yytoken ==  Token_BACKTICK
                                  ||  yytoken ==  Token_PLUS
                                  ||  yytoken ==  Token_MINUS
                                  ||  yytoken ==  Token_TILDE)
                               {
                                 if  (yytoken ==  Token_NOT
                                      ||  yytoken ==  Token_STRINGLITERAL
                                      ||  yytoken ==  Token_IDENTIFIER
                                      ||  yytoken ==  Token_INTEGER
                                      ||  yytoken ==  Token_FLOAT
                                      ||  yytoken ==  Token_IMAGNUM
                                      ||  yytoken ==  Token_LPAREN
                                      ||  yytoken ==  Token_LBRACE
                                      ||  yytoken ==  Token_LBRACKET
                                      ||  yytoken ==  Token_BACKTICK
                                      ||  yytoken ==  Token_PLUS
                                      ||  yytoken ==  Token_MINUS
                                      ||  yytoken ==  Token_TILDE)
                                   {
                                     and_test_ast *__node_155 =  0;

                                     if  (!parse_and_test(&__node_155))
                                       {
                                         yy_expected_symbol(ast_node::Kind_and_test,  "and_test");
                                         return  false;
                                       }

                                     (*yynode)->and_test_sequence =  snoc((*yynode)->and_test_sequence,  __node_155,  memory_pool);

                                     while  (yytoken ==  Token_OR)
                                       {
                                         if  (yytoken !=  Token_OR)
                                           {
                                             yy_expected_token(yytoken,  Token_OR,  "or");
                                             return  false;
                                           }

                                         yylex();

                                         and_test_ast *__node_156 =  0;

                                         if  (!parse_and_test(&__node_156))
                                           {
                                             yy_expected_symbol(ast_node::Kind_and_test,  "and_test");
                                             return  false;
                                           }

                                         (*yynode)->and_test_sequence =  snoc((*yynode)->and_test_sequence,  __node_156,  memory_pool);

                                       }
                                   }

                                 else if  (yytoken ==  Token_LAMBDA)
                                   {
                                     lambda_def_ast *__node_157 =  0;

                                     if  (!parse_lambda_def(&__node_157))
                                       {
                                         yy_expected_symbol(ast_node::Kind_lambda_def,  "lambda_def");
                                         return  false;
                                       }

                                     (*yynode)->lambda_def =  __node_157;

                                   }

                                 else
                                   {
                                     return  false;
                                   }
                               }

                             else
                               {
                                 return  false;
                               }

                             (*yynode)->end_token =  token_stream->index() -  1;

                             return  true;
                           }

                           bool parser::parse_test_list_gexp(test_list_gexp_ast **yynode)
                           {
                             *yynode =  create<test_list_gexp_ast>();

                             (*yynode)->start_token =  token_stream->index() -  1;

                             if  (yytoken ==  Token_LAMBDA
                                  ||  yytoken ==  Token_NOT
                                  ||  yytoken ==  Token_STRINGLITERAL
                                  ||  yytoken ==  Token_IDENTIFIER
                                  ||  yytoken ==  Token_INTEGER
                                  ||  yytoken ==  Token_FLOAT
                                  ||  yytoken ==  Token_IMAGNUM
                                  ||  yytoken ==  Token_LPAREN
                                  ||  yytoken ==  Token_LBRACE
                                  ||  yytoken ==  Token_LBRACKET
                                  ||  yytoken ==  Token_BACKTICK
                                  ||  yytoken ==  Token_PLUS
                                  ||  yytoken ==  Token_MINUS
                                  ||  yytoken ==  Token_TILDE)
                               {
                                 test_ast *__node_158 =  0;

                                 if  (!parse_test(&__node_158))
                                   {
                                     yy_expected_symbol(ast_node::Kind_test,  "test");
                                     return  false;
                                   }

                                 (*yynode)->test_sequence =  snoc((*yynode)->test_sequence,  __node_158,  memory_pool);

                                 while  (yytoken ==  Token_COMMA)
                                   {
                                     if  (yytoken !=  Token_COMMA)
                                       {
                                         yy_expected_token(yytoken,  Token_COMMA,  "comma");
                                         return  false;
                                       }

                                     yylex();

                                     if ( yytoken ==  Token_COLON ||  yytoken ==  Token_SEMICOLON ||  yytoken ==  Token_RPAREN ||  yytoken ==  Token_LINEBREAK)
                                       {
                                         break;
                                       }

                                     test_ast *__node_159 =  0;

                                     if  (!parse_test(&__node_159))
                                       {
                                         yy_expected_symbol(ast_node::Kind_test,  "test");
                                         return  false;
                                       }

                                     (*yynode)->test_sequence =  snoc((*yynode)->test_sequence,  __node_159,  memory_pool);

                                   }
                               }

                             else
                               {
                                 return  false;
                               }

                             (*yynode)->end_token =  token_stream->index() -  1;

                             return  true;
                           }

                           bool parser::parse_testlist(testlist_ast **yynode)
                           {
                             *yynode =  create<testlist_ast>();

                             (*yynode)->start_token =  token_stream->index() -  1;

                             if  (yytoken ==  Token_LAMBDA
                                  ||  yytoken ==  Token_NOT
                                  ||  yytoken ==  Token_STRINGLITERAL
                                  ||  yytoken ==  Token_IDENTIFIER
                                  ||  yytoken ==  Token_INTEGER
                                  ||  yytoken ==  Token_FLOAT
                                  ||  yytoken ==  Token_IMAGNUM
                                  ||  yytoken ==  Token_LPAREN
                                  ||  yytoken ==  Token_LBRACE
                                  ||  yytoken ==  Token_LBRACKET
                                  ||  yytoken ==  Token_BACKTICK
                                  ||  yytoken ==  Token_PLUS
                                  ||  yytoken ==  Token_MINUS
                                  ||  yytoken ==  Token_TILDE)
                               {
                                 test_ast *__node_160 =  0;

                                 if  (!parse_test(&__node_160))
                                   {
                                     yy_expected_symbol(ast_node::Kind_test,  "test");
                                     return  false;
                                   }

                                 (*yynode)->test_sequence =  snoc((*yynode)->test_sequence,  __node_160,  memory_pool);

                                 while  (yytoken ==  Token_COMMA)
                                   {
                                     if  (yytoken !=  Token_COMMA)
                                       {
                                         yy_expected_token(yytoken,  Token_COMMA,  "comma");
                                         return  false;
                                       }

                                     yylex();

                                     if ( yytoken ==  Token_COLON ||  yytoken ==  Token_SEMICOLON ||  yytoken ==  Token_RPAREN ||  yytoken ==  Token_LINEBREAK)
                                       {
                                         break;
                                       }

                                     test_ast *__node_161 =  0;

                                     if  (!parse_test(&__node_161))
                                       {
                                         yy_expected_symbol(ast_node::Kind_test,  "test");
                                         return  false;
                                       }

                                     (*yynode)->testlist_sequence =  snoc((*yynode)->testlist_sequence,  __node_161,  memory_pool);

                                   }
                               }

                             else
                               {
                                 return  false;
                               }

                             (*yynode)->end_token =  token_stream->index() -  1;

                             return  true;
                           }

                           bool parser::parse_testlist1(testlist1_ast **yynode)
                           {
                             *yynode =  create<testlist1_ast>();

                             (*yynode)->start_token =  token_stream->index() -  1;

                             if  (yytoken ==  Token_LAMBDA
                                  ||  yytoken ==  Token_NOT
                                  ||  yytoken ==  Token_STRINGLITERAL
                                  ||  yytoken ==  Token_IDENTIFIER
                                  ||  yytoken ==  Token_INTEGER
                                  ||  yytoken ==  Token_FLOAT
                                  ||  yytoken ==  Token_IMAGNUM
                                  ||  yytoken ==  Token_LPAREN
                                  ||  yytoken ==  Token_LBRACE
                                  ||  yytoken ==  Token_LBRACKET
                                  ||  yytoken ==  Token_BACKTICK
                                  ||  yytoken ==  Token_PLUS
                                  ||  yytoken ==  Token_MINUS
                                  ||  yytoken ==  Token_TILDE)
                               {
                                 test_ast *__node_162 =  0;

                                 if  (!parse_test(&__node_162))
                                   {
                                     yy_expected_symbol(ast_node::Kind_test,  "test");
                                     return  false;
                                   }

                                 (*yynode)->test_sequence =  snoc((*yynode)->test_sequence,  __node_162,  memory_pool);

                                 while  (yytoken ==  Token_COMMA)
                                   {
                                     if  (yytoken !=  Token_COMMA)
                                       {
                                         yy_expected_token(yytoken,  Token_COMMA,  "comma");
                                         return  false;
                                       }

                                     yylex();

                                     test_ast *__node_163 =  0;

                                     if  (!parse_test(&__node_163))
                                       {
                                         yy_expected_symbol(ast_node::Kind_test,  "test");
                                         return  false;
                                       }

                                     (*yynode)->test_sequence =  snoc((*yynode)->test_sequence,  __node_163,  memory_pool);

                                   }
                               }

                             else
                               {
                                 return  false;
                               }

                             (*yynode)->end_token =  token_stream->index() -  1;

                             return  true;
                           }

                           bool parser::parse_testlist_gexp(testlist_gexp_ast **yynode)
                           {
                             *yynode =  create<testlist_gexp_ast>();

                             (*yynode)->start_token =  token_stream->index() -  1;

                             if  (yytoken ==  Token_LAMBDA
                                  ||  yytoken ==  Token_NOT
                                  ||  yytoken ==  Token_STRINGLITERAL
                                  ||  yytoken ==  Token_IDENTIFIER
                                  ||  yytoken ==  Token_INTEGER
                                  ||  yytoken ==  Token_FLOAT
                                  ||  yytoken ==  Token_IMAGNUM
                                  ||  yytoken ==  Token_LPAREN
                                  ||  yytoken ==  Token_LBRACE
                                  ||  yytoken ==  Token_LBRACKET
                                  ||  yytoken ==  Token_BACKTICK
                                  ||  yytoken ==  Token_PLUS
                                  ||  yytoken ==  Token_MINUS
                                  ||  yytoken ==  Token_TILDE)
                               {
                                 test_list_gexp_ast *__node_164 =  0;

                                 if  (!parse_test_list_gexp(&__node_164))
                                   {
                                     yy_expected_symbol(ast_node::Kind_test_list_gexp,  "test_list_gexp");
                                     return  false;
                                   }

                                 (*yynode)->test_list_gexp =  __node_164;

                                 if  (yytoken ==  Token_FOR)
                                   {
                                     gen_for_ast *__node_165 =  0;

                                     if  (!parse_gen_for(&__node_165))
                                       {
                                         yy_expected_symbol(ast_node::Kind_gen_for,  "gen_for");
                                         return  false;
                                       }

                                     (*yynode)->gen_for =  __node_165;

                                   }

                                 else if  (true /*epsilon*/)
                                 {}
                                 else
                                   {
                                     return  false;
                                   }
                               }

                             else
                               {
                                 return  false;
                               }

                             (*yynode)->end_token =  token_stream->index() -  1;

                             return  true;
                           }

                           bool parser::parse_testlist_safe(testlist_safe_ast **yynode)
                           {
                             *yynode =  create<testlist_safe_ast>();

                             (*yynode)->start_token =  token_stream->index() -  1;

                             if  (yytoken ==  Token_LAMBDA
                                  ||  yytoken ==  Token_NOT
                                  ||  yytoken ==  Token_STRINGLITERAL
                                  ||  yytoken ==  Token_IDENTIFIER
                                  ||  yytoken ==  Token_INTEGER
                                  ||  yytoken ==  Token_FLOAT
                                  ||  yytoken ==  Token_IMAGNUM
                                  ||  yytoken ==  Token_LPAREN
                                  ||  yytoken ==  Token_LBRACE
                                  ||  yytoken ==  Token_LBRACKET
                                  ||  yytoken ==  Token_BACKTICK
                                  ||  yytoken ==  Token_PLUS
                                  ||  yytoken ==  Token_MINUS
                                  ||  yytoken ==  Token_TILDE)
                               {
                                 test_ast *__node_166 =  0;

                                 if  (!parse_test(&__node_166))
                                   {
                                     yy_expected_symbol(ast_node::Kind_test,  "test");
                                     return  false;
                                   }

                                 (*yynode)->test_sequence =  snoc((*yynode)->test_sequence,  __node_166,  memory_pool);

                                 if  (yytoken ==  Token_COMMA)
                                   {
                                     do
                                       {
                                         if  (yytoken !=  Token_COMMA)
                                           {
                                             yy_expected_token(yytoken,  Token_COMMA,  "comma");
                                             return  false;
                                           }

                                         yylex();

                                         test_ast *__node_167 =  0;

                                         if  (!parse_test(&__node_167))
                                           {
                                             yy_expected_symbol(ast_node::Kind_test,  "test");
                                             return  false;
                                           }

                                         (*yynode)->test_sequence =  snoc((*yynode)->test_sequence,  __node_167,  memory_pool);

                                       }

                                     while  (yytoken ==  Token_COMMA);
                                     if  (yytoken ==  Token_COMMA)
                                       {
                                         if  (yytoken !=  Token_COMMA)
                                           {
                                             yy_expected_token(yytoken,  Token_COMMA,  "comma");
                                             return  false;
                                           }

                                         yylex();

                                       }

                                     else if  (true /*epsilon*/)
                                     {}
                                     else
                                       {
                                         return  false;
                                       }
                                   }

                                 else if  (true /*epsilon*/)
                                 {}
                                 else
                                   {
                                     return  false;
                                   }
                               }

                             else
                               {
                                 return  false;
                               }

                             (*yynode)->end_token =  token_stream->index() -  1;

                             return  true;
                           }

                           bool parser::parse_trailer(trailer_ast **yynode)
                           {
                             *yynode =  create<trailer_ast>();

                             (*yynode)->start_token =  token_stream->index() -  1;

                             if  (yytoken ==  Token_LPAREN
                                  ||  yytoken ==  Token_LBRACKET
                                  ||  yytoken ==  Token_DOT)
                               {
                                 if  (yytoken ==  Token_LPAREN)
                                   {
                                     if  (yytoken !=  Token_LPAREN)
                                       {
                                         yy_expected_token(yytoken,  Token_LPAREN,  "lparen");
                                         return  false;
                                       }

                                     yylex();

                                     if  (yytoken ==  Token_LAMBDA
                                          ||  yytoken ==  Token_NOT
                                          ||  yytoken ==  Token_STRINGLITERAL
                                          ||  yytoken ==  Token_IDENTIFIER
                                          ||  yytoken ==  Token_INTEGER
                                          ||  yytoken ==  Token_FLOAT
                                          ||  yytoken ==  Token_IMAGNUM
                                          ||  yytoken ==  Token_LPAREN
                                          ||  yytoken ==  Token_LBRACE
                                          ||  yytoken ==  Token_LBRACKET
                                          ||  yytoken ==  Token_BACKTICK
                                          ||  yytoken ==  Token_STAR
                                          ||  yytoken ==  Token_DOUBLESTAR
                                          ||  yytoken ==  Token_PLUS
                                          ||  yytoken ==  Token_MINUS
                                          ||  yytoken ==  Token_TILDE)
                                       {
                                         arglist_ast *__node_168 =  0;

                                         if  (!parse_arglist(&__node_168))
                                           {
                                             yy_expected_symbol(ast_node::Kind_arglist,  "arglist");
                                             return  false;
                                           }

                                         (*yynode)->trailer_arglist =  __node_168;

                                       }

                                     else if  (true /*epsilon*/)
                                     {}
                                     else
                                       {
                                         return  false;
                                       }

                                     if  (yytoken !=  Token_RPAREN)
                                       {
                                         yy_expected_token(yytoken,  Token_RPAREN,  "rparen");
                                         return  false;
                                       }

                                     yylex();

                                   }

                                 else if  (yytoken ==  Token_LBRACKET)
                                   {
                                     if  (yytoken !=  Token_LBRACKET)
                                       {
                                         yy_expected_token(yytoken,  Token_LBRACKET,  "lbracket");
                                         return  false;
                                       }

                                     yylex();

                                     subscriptlist_ast *__node_169 =  0;

                                     if  (!parse_subscriptlist(&__node_169))
                                       {
                                         yy_expected_symbol(ast_node::Kind_subscriptlist,  "subscriptlist");
                                         return  false;
                                       }

                                     (*yynode)->subscriptlist =  __node_169;

                                     if  (yytoken !=  Token_RBRACKET)
                                       {
                                         yy_expected_token(yytoken,  Token_RBRACKET,  "rbracket");
                                         return  false;
                                       }

                                     yylex();

                                   }

                                 else if  (yytoken ==  Token_DOT)
                                   {
                                     if  (yytoken !=  Token_DOT)
                                       {
                                         yy_expected_token(yytoken,  Token_DOT,  "dot");
                                         return  false;
                                       }

                                     yylex();

                                     if  (yytoken !=  Token_IDENTIFIER)
                                       {
                                         yy_expected_token(yytoken,  Token_IDENTIFIER,  "identifier");
                                         return  false;
                                       }

                                     (*yynode)->tariler_dot_name =  token_stream->index() -  1;
                                     yylex();

                                   }

                                 else
                                   {
                                     return  false;
                                   }
                               }

                             else
                               {
                                 return  false;
                               }

                             (*yynode)->end_token =  token_stream->index() -  1;

                             return  true;
                           }

                           bool parser::parse_try_stmt(try_stmt_ast **yynode)
                           {
                             *yynode =  create<try_stmt_ast>();

                             (*yynode)->start_token =  token_stream->index() -  1;

                             if  (yytoken ==  Token_TRY)
                               {
                                 if  (yytoken !=  Token_TRY)
                                   {
                                     yy_expected_token(yytoken,  Token_TRY,  "try");
                                     return  false;
                                   }

                                 yylex();

                                 if  (yytoken !=  Token_COLON)
                                   {
                                     yy_expected_token(yytoken,  Token_COLON,  "colon");
                                     return  false;
                                   }

                                 yylex();

                                 suite_ast *__node_170 =  0;

                                 if  (!parse_suite(&__node_170))
                                   {
                                     yy_expected_symbol(ast_node::Kind_suite,  "suite");
                                     return  false;
                                   }

                                 (*yynode)->try_suite =  __node_170;

                                 if  (yytoken ==  Token_EXCEPT)
                                   {
                                     do
                                       {
                                         except_clause_ast *__node_171 =  0;

                                         if  (!parse_except_clause(&__node_171))
                                           {
                                             yy_expected_symbol(ast_node::Kind_except_clause,  "except_clause");
                                             return  false;
                                           }

                                         (*yynode)->except_clause_sequence =  snoc((*yynode)->except_clause_sequence,  __node_171,  memory_pool);

                                         if  (yytoken !=  Token_COLON)
                                           {
                                             yy_expected_token(yytoken,  Token_COLON,  "colon");
                                             return  false;
                                           }

                                         yylex();

                                         suite_ast *__node_172 =  0;

                                         if  (!parse_suite(&__node_172))
                                           {
                                             yy_expected_symbol(ast_node::Kind_suite,  "suite");
                                             return  false;
                                           }

                                         (*yynode)->except_suite_sequence =  snoc((*yynode)->except_suite_sequence,  __node_172,  memory_pool);

                                       }

                                     while  (yytoken ==  Token_EXCEPT);
                                     if  (yytoken ==  Token_ELSE)
                                       {
                                         if  (yytoken !=  Token_ELSE)
                                           {
                                             yy_expected_token(yytoken,  Token_ELSE,  "else");
                                             return  false;
                                           }

                                         yylex();

                                         if  (yytoken !=  Token_COLON)
                                           {
                                             yy_expected_token(yytoken,  Token_COLON,  "colon");
                                             return  false;
                                           }

                                         yylex();

                                         suite_ast *__node_173 =  0;

                                         if  (!parse_suite(&__node_173))
                                           {
                                             yy_expected_symbol(ast_node::Kind_suite,  "suite");
                                             return  false;
                                           }

                                         (*yynode)->try_else_suite =  __node_173;

                                       }

                                     else if  (true /*epsilon*/)
                                     {}
                                     else
                                       {
                                         return  false;
                                       }
                                   }

                                 else if  (yytoken ==  Token_FINALLY)
                                   {
                                     if  (yytoken !=  Token_FINALLY)
                                       {
                                         yy_expected_token(yytoken,  Token_FINALLY,  "finally");
                                         return  false;
                                       }

                                     yylex();

                                     if  (yytoken !=  Token_COLON)
                                       {
                                         yy_expected_token(yytoken,  Token_COLON,  "colon");
                                         return  false;
                                       }

                                     yylex();

                                     suite_ast *__node_174 =  0;

                                     if  (!parse_suite(&__node_174))
                                       {
                                         yy_expected_symbol(ast_node::Kind_suite,  "suite");
                                         return  false;
                                       }

                                     (*yynode)->finally_suite =  __node_174;

                                   }

                                 else
                                   {
                                     return  false;
                                   }
                               }

                             else
                               {
                                 return  false;
                               }

                             (*yynode)->end_token =  token_stream->index() -  1;

                             return  true;
                           }

                           bool parser::parse_varargslist(varargslist_ast **yynode)
                           {
                             *yynode =  create<varargslist_ast>();

                             (*yynode)->start_token =  token_stream->index() -  1;

                             if  (yytoken ==  Token_IDENTIFIER
                                  ||  yytoken ==  Token_LPAREN
                                  ||  yytoken ==  Token_STAR
                                  ||  yytoken ==  Token_DOUBLESTAR ||  yytoken ==  Token_RPAREN
                                  ||  yytoken ==  Token_COLON)
                               {
                                 if  (yytoken ==  Token_IDENTIFIER
                                      ||  yytoken ==  Token_LPAREN)
                                   {
                                     func_def_ast *__node_175 =  0;

                                     if  (!parse_func_def(&__node_175))
                                       {
                                         yy_expected_symbol(ast_node::Kind_func_def,  "func_def");
                                         return  false;
                                       }

                                     (*yynode)->func_def =  __node_175;

                                   }

                                 else if  (true /*epsilon*/)
                                 {}
                                 else
                                   {
                                     return  false;
                                   }

                                 if  ((yytoken ==  Token_STAR
                                       ||  yytoken ==  Token_DOUBLESTAR) &&  ( yytoken !=  Token_RPAREN  &&  LA(2).kind ==  Token_IDENTIFIER))
                                   {
                                     fun_pos_param_ast *__node_176 =  0;

                                     if  (!parse_fun_pos_param(&__node_176))
                                       {
                                         yy_expected_symbol(ast_node::Kind_fun_pos_param,  "fun_pos_param");
                                         return  false;
                                       }

                                     (*yynode)->fun_pos_param =  __node_176;

                                   }

                                 else if  (true /*epsilon*/)
                                 {}
                                 else
                                   {
                                     return  false;
                                   }
                               }

                             else
                               {
                                 return  false;
                               }

                             (*yynode)->end_token =  token_stream->index() -  1;

                             return  true;
                           }

                           bool parser::parse_while_stmt(while_stmt_ast **yynode)
                           {
                             *yynode =  create<while_stmt_ast>();

                             (*yynode)->start_token =  token_stream->index() -  1;

                             if  (yytoken ==  Token_WHILE)
                               {
                                 if  (yytoken !=  Token_WHILE)
                                   {
                                     yy_expected_token(yytoken,  Token_WHILE,  "while");
                                     return  false;
                                   }

                                 yylex();

                                 test_ast *__node_177 =  0;

                                 if  (!parse_test(&__node_177))
                                   {
                                     yy_expected_symbol(ast_node::Kind_test,  "test");
                                     return  false;
                                   }

                                 (*yynode)->while_test =  __node_177;

                                 if  (yytoken !=  Token_COLON)
                                   {
                                     yy_expected_token(yytoken,  Token_COLON,  "colon");
                                     return  false;
                                   }

                                 yylex();

                                 suite_ast *__node_178 =  0;

                                 if  (!parse_suite(&__node_178))
                                   {
                                     yy_expected_symbol(ast_node::Kind_suite,  "suite");
                                     return  false;
                                   }

                                 (*yynode)->while_suite =  __node_178;

                                 if  (yytoken ==  Token_ELSE)
                                   {
                                     if  (yytoken !=  Token_ELSE)
                                       {
                                         yy_expected_token(yytoken,  Token_ELSE,  "else");
                                         return  false;
                                       }

                                     yylex();

                                     if  (yytoken !=  Token_COLON)
                                       {
                                         yy_expected_token(yytoken,  Token_COLON,  "colon");
                                         return  false;
                                       }

                                     yylex();

                                     suite_ast *__node_179 =  0;

                                     if  (!parse_suite(&__node_179))
                                       {
                                         yy_expected_symbol(ast_node::Kind_suite,  "suite");
                                         return  false;
                                       }

                                     (*yynode)->while_else_suite =  __node_179;

                                   }

                                 else if  (true /*epsilon*/)
                                 {}
                                 else
                                   {
                                     return  false;
                                   }
                               }

                             else
                               {
                                 return  false;
                               }

                             (*yynode)->end_token =  token_stream->index() -  1;

                             return  true;
                           }

                           bool parser::parse_xor_expr(xor_expr_ast **yynode)
                           {
                             *yynode =  create<xor_expr_ast>();

                             (*yynode)->start_token =  token_stream->index() -  1;

                             if  (yytoken ==  Token_STRINGLITERAL
                                  ||  yytoken ==  Token_IDENTIFIER
                                  ||  yytoken ==  Token_INTEGER
                                  ||  yytoken ==  Token_FLOAT
                                  ||  yytoken ==  Token_IMAGNUM
                                  ||  yytoken ==  Token_LPAREN
                                  ||  yytoken ==  Token_LBRACE
                                  ||  yytoken ==  Token_LBRACKET
                                  ||  yytoken ==  Token_BACKTICK
                                  ||  yytoken ==  Token_PLUS
                                  ||  yytoken ==  Token_MINUS
                                  ||  yytoken ==  Token_TILDE)
                               {
                                 and_expr_ast *__node_180 =  0;

                                 if  (!parse_and_expr(&__node_180))
                                   {
                                     yy_expected_symbol(ast_node::Kind_and_expr,  "and_expr");
                                     return  false;
                                   }

                                 (*yynode)->xor_expr =  __node_180;

                                 while  (yytoken ==  Token_HAT)
                                   {
                                     if  (yytoken !=  Token_HAT)
                                       {
                                         yy_expected_token(yytoken,  Token_HAT,  "hat");
                                         return  false;
                                       }

                                     yylex();

                                     and_expr_ast *__node_181 =  0;

                                     if  (!parse_and_expr(&__node_181))
                                       {
                                         yy_expected_symbol(ast_node::Kind_and_expr,  "and_expr");
                                         return  false;
                                       }

                                     (*yynode)->hat_xor_expr_sequence =  snoc((*yynode)->hat_xor_expr_sequence,  __node_181,  memory_pool);

                                   }
                               }

                             else
                               {
                                 return  false;
                               }

                             (*yynode)->end_token =  token_stream->index() -  1;

                             return  true;
                           }

                           bool parser::parse_yield_stmt(yield_stmt_ast **yynode)
                           {
                             *yynode =  create<yield_stmt_ast>();

                             (*yynode)->start_token =  token_stream->index() -  1;

                             if  (yytoken ==  Token_YIELD)
                               {
                                 if  (yytoken !=  Token_YIELD)
                                   {
                                     yy_expected_token(yytoken,  Token_YIELD,  "yield");
                                     return  false;
                                   }

                                 yylex();

                                 testlist_ast *__node_182 =  0;

                                 if  (!parse_testlist(&__node_182))
                                   {
                                     yy_expected_symbol(ast_node::Kind_testlist,  "testlist");
                                     return  false;
                                   }

                                 (*yynode)->yield_expr =  __node_182;

                               }

                             else
                               {
                                 return  false;
                               }

                             (*yynode)->end_token =  token_stream->index() -  1;

                             return  true;
                           }


                         } // end of namespace Python


