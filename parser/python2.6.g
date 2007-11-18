-------------------------------------------------------------------------------
-- Copyright (c) 2006 Andreas Pakulat <apaku@gmx.de>
-- Copyright (c) 2007 Piyush Verma  <piyush.verma@gmail.com>
--
-- Permission is hereby granted, free of charge, to any person obtaining
-- a copy of this software and associated documentation files (the
-- "Software"), to deal in the Software without restriction, including
-- without limitation the rights to use, copy, modify, merge, publish,
-- distribute, sublicense, and/or sell copies of the Software, and to
-- permit persons to whom the Software is furnished to do so, subject to
-- the following conditions:
--
-- The above copyright notice and this permission notice shall be
-- included in all copies or substantial portions of the Software.
--
-- THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
-- EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
-- MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
-- NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
-- LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
-- OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
-- WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
-------------------------------------------------------------------------------

-----------------------------------------------------------
-- Grammar for Python2.4
-- Modelled after the Grammar files shipped with Python2.4
-- source, the Python Language Reference documentation,
-- also included with Python
-- And after the Python 2.3.3 Antlr grammar found on the
-- antlr grammar list page
-----------------------------------------------------------

-----------------------------------------------------------
-- TODO: Error recovery
-- %parserclass (private declaration)
-- [:
--   parser::java_compatibility_mode _M_compatibility_mode;
--
--   struct parser_state {
--   };
--   parser_state _M_state;
-- :]
-- parser::parser_state *parser::copy_current_state()
-- {
--     parser_state *state = new parser_state();
--     return state;
-- }
--
-- void parser::restore_state( parser::parser_state *state )
-- {
-- }
--
-- Then a rule like (stmt)* -> project can be written
-- as try/recover(stmt)* -> project and the parser
-- will skip any errornous statements

-----------------------------------------------------------
-- Global  declarations
-----------------------------------------------------------

[:

#include <QtCore/QString>

namespace Python
{
    class Lexer;
}
:]


------------------------------------------------------------
-- Export macro to use the parser in a shared lib
------------------------------------------------------------
%export_macro "KDEVPYTHONPARSER_EXPORT"
%export_macro_header "parserexport.h"

------------------------------------------------------------
-- Parser class members
------------------------------------------------------------

%parserclass (public declaration)
[:
  /**
   * Transform the raw input into tokens.
   * When this method returns, the parser's token stream has been filled
   * and any parse_*() method can be called.
   */
  void tokenize( const QString& contents );

  enum ProblemType {
      Error,
      Warning,
      Info
  };
  void reportProblem( parser::ProblemType type, const QString& message );
  QString tokenText(std::size_t begin, std::size_t end);
  void setDebug(bool debug);

:]

%parserclass (private declaration)
[:
   QString m_contents;
   bool m_debug;
:]

-----------------------------------------------------------
-- List of defined tokens
-----------------------------------------------------------

-- keywords
%token AND ("and"), AS ("as"), ASSERT ("assert"), BREAK ("break"), CLASS ("class"),
       CONTINUE ("continue"), DEF ("DEF"), DEL ("del"), ELIF ("elif"), ELSE ("else"),
       EXCEPT ("except"), EXEC ("exec"), FINALLY ("finally"), FOR ("for"),
       FROM ("from"), FUTURE ("future"), GLOBAL ("global"), IF ("if"),
       IMPORT ("import"), IN ("in"), IS ("is"), LAMBDA ("lambda"), NOT ("not"),
       OR ("or"), PASS ("pass"), PRINT ("print"), RAISE ("raise"),
       RETURN ("return"), TRY ("try"), WHILE ("while"), WITH ("with"), YIELD ("yield") ;;


-- indentation which is important in python and linebreak
%token INDENT ("indent"), DEDENT ("dedent"), LINEBREAK ("linebreak") ;;

-- Identifiers, Strings and numbers
%token IDENTIFIER ("identifier"), STRINGLITERAL ("stringliteral"),
       INTEGER ("integer"), FLOAT ("float"), IMAGNUM ("imagnum") ;;

-- delimiters
%token LPAREN ("lparen"), RPAREN ("rparen"), LBRACKET ("lbracket"), RBRACKET ("rbracket"),
       LBRACE ("lbrace"), RBRACE ("rbrace"), AT ("at"), COMMA ("comma"), COLON ("colon"),
       DOT ("dot"), BACKTICK ("backtick"), EQUAL ("equal"), SEMICOLON ("semicolon"),
       PLUSEQ ("pluseq"), MINUSEQ ("minuseq"), STAREQ ("stareq"), SLASHEQ ("slasheq"),
       DOUBLESLASHEQ ("doubleslasheq"), MODULOEQ ("moduloeq"), ANDEQ ("andeq"),
       OREQ ("oreq"), HATEQ ("hateq"), RSHIFTEQ ("rshifteq"), LSHIFTEQ ("lshifteq"),
       DOUBLESTAREQ ("doublestareq"), ELLIPSIS ("ellipsis")
       ;;

-- operators
%token PLUS ("plus"), MINUS ("minus"), STAR ("star"), DOUBLESTAR ("doublestar"),
       SLASH ("slash"), DOUBLESLASH ("doubleslash"), MODULO ("modulo"), LSHIFT ("lshift"),
       RSHIFT ("rshift"), ANDOP ("andop"), OROP ("orop"), HAT ("hat"), TILDE ("tilde"),
       LESS ("less"), GREATER ("greater"), LESSEQ ("lesseq"), GREATEREQ ("greatereq"),
       ISEQUAL ("equal"), UNEQUAL ("unequal") ;;


-- token that makes the parser fail in any case:
%token INVALID ("invalid token") ;;

-- The actual grammar starts here.

   ( statement | LINEBREAK )*
-> code ;;

   IDENTIFIER | literal | enclosure
-> atom ;;

   parenth_form | list_display | generator_expression | dict_display
   | string_conversion | yield_atom
-> enclosure ;;

   STRINGLITERAL | INTEGER | FLOAT | IMAGNUM
-> literal ;;

   LPAREN ( expression_list | 0 ) RPAREN
-> parenth_form ;;

   LBRACKET ( expression_list | list_comprehension | 0 ) RBRACKET
-> list_display ;;

   expression list_for
-> list_comprehension ;;

   FOR target_list IN old_expression_list ( list_iter | 0 )
-> list_for ;;

   old_expression ( ( COMMA old_expression )+ ( COMMA | 0 ) )
-> old_expression_list ;;

   list_for | list_if
-> list_iter ;;

   IF old_expression ( list_iter | 0 )
-> list_if ;;

   LPAREN expression genexpr_for RPAREN
-> generator_expression ;;

   FOR target_list IN or_test ( genexpr_iter | 0 )
-> genexpr_for ;;

   genexpr_for | genexpr_if
-> genexpr_iter ;;

   IF old_expression ( genexpr_iter | 0 )
-> genexpr_if ;;

   LBRACE ( key_datum_list | 0 ) RBRACE
-> dict_display ;;

   key_datum ( COMMA key_datum )* ( COMMA | 0 )
-> key_datum_list ;;

   expression COLON expression
-> key_datum ;;

   BACKTICK expression_list BACKTICK
-> string_conversion ;;

   LPAREN yield_expression RPAREN
-> yield_atom ;;

   YIELD ( expression_list | 0 )
-> yield_expression ;;

   atom | attributeref | subscription | slicing | call
-> primary ;;

   primary DOT IDENTIFIER
-> attributeref ;;

   primary LBRACKET expression_list RBRACKET
-> subscription ;;

   simple_slicing | extended_slicing
-> slicing ;;

   primary LBRACKET short_slice RBRACKET
-> simple_slicing ;;

   primary LBRACKET slice_list RBRACKET
-> extended_slicing ;;

   slice_item ( COMMA slice_item )* ( COMMA | 0 )
-> slice_list ;;

   expression | proper_slice | ELLIPSIS
-> slice_item ;;

   short_slice | long_slice
-> proper_slice ;;

   ( lower_bound | 0 ) COLON ( upper_bound | 0 )
-> short_slice ;;

   short_slice COLON ( stride | 0 )
-> long_slice ;;

   expression
-> lower_bound ;;

   expression
-> lower_bound ;;

   expression
-> upper_bound ;;

   expression
-> stride ;;

   primary LPAREN ( argument_list ( COMMA | 0 ) | expression genexpr_for | 0 ) RPAREN
-> call ;;

   ( positional_arguments ( COMMA keyword_arguments | 0 ) ( COMMA STAR expression | 0 )
   ( COMMA DOUBLESTAR expression | 0 ) ) | ( keyword_arguments ( COMMA STAR expression | 0 )
   ( COMMA DOUBLESTAR expression | 0 ) ) | ( STAR expression
   ( COMMA DOUBLESTAR expression | 0 ) ) | COMMA DOUBLESTAR expression
-> argument_list ;;

   expression ( COMMA expression )*
-> positional_arguments ;;

   keyword_item ( COMMA keyword_item )*
-> keyword_arguments ;;

   IDENTIFIER EQUAL expression
-> keyword_item ;;

   primary ( DOUBLESTAR u_expr | 0 )
-> power ;;

   power | MINUS u_expr | PLUS u_expr | TILDE u_expr
-> u_expr ;;

   u_expr | m_expr STAR u_expr | m_expr SLASH u_expr | m_expr DOUBLESLASH u_expr
   | m_expr MODULO u_expr
-> m_expr ;;

   m_expr | a_expr PLUS m_expr | a_expr MINUS m_expr
-> a_expr ;;

   a_expr | shift_expr ( LSHIFT | RSHIFT ) a_expr
-> shift_expr ;;

   shift_expr | and_expr ANDOP shift_expr
-> and_expr ;;

   and_expr | xor_expr HAT and_expr
-> xor_expr ;;

   xor_expr | or_expr OROP xor_expr
-> or_expr ;;

   or_expr ( comp_operator or_expr )*
-> comparison ;;

   LESS | GREATER | ISEQUAL | GREATEREQ | LESSEQ | UNEQUAL | IS ( NOT | 0 )
   | ( NOT | 0 ) IN
-> comp_operator ;;

   conditional_expression | lambda_form
-> expression ;;

   or_test | old_lambda_form
-> old_expression ;;

   or_test ( IF or_test ELSE expression | 0 )
-> conditional_expression ;;

   and_test | or_test OR and_test
-> or_test ;;

   not_test | and_test AND not_test
-> and_test ;;

   comparison | NOT not_test
-> not_test ;;

   LAMBDA ( parameter_list | 0 ) COLON expression
-> lambda_form ;;


   LAMBDA ( parameter_list | 0 ) COLON old_expression
-> old_lambda_form ;;

   expression ( COMMA expression )* ( COMMA | 0 )
-> expression_list ;;

   expression_stmt | assert_stmt | assignment_stmt | augmented_assignment_stmt
   | pass_stmt | del_stmt | print_stmt | return_stmt | yield_stmt | raise_stmt
   | break_stmt | continue_stmt | import_stmt | global_stmt | exec_stmt
-> simple_stmt ;;

   expression_list
-> expression_stmt ;;

   ( target_list EQUAL )+ ( expression_list | yield_expression )
-> assignment_stmt ;;

   target ( COMMA target )* ( COMMA | 0 )
-> target_list ;;

   IDENTIFIER | LPAREN target_list RPAREN | LBRACKET target_list RBRACKET
   | attributeref | subscription | slicing
-> target ;;

   target augop ( expression_list | yield_expression )
-> augmented_assignment_stmt ;;

   PLUSEQ | MINUSEQ | STAREQ | SLASHEQ | MODULOEQ | DOUBLESTAREQ | RSHIFTEQ
   | LSHIFTEQ | ANDEQ | HATEQ | OREQ
-> augop ;;

   ASSERT expression ( COMMA expression | 0 )
-> assert_stmt ;;

   PASS
-> pass_stmt ;;

   DEL target_list
-> del_stmt ;;

   PRINT ( ( expression ( COMMA expression )* ( COMMA | 0 ) | 0 )
   | RSHIFT expression ( ( COMMA expression )+ ( COMMA | 0 ) | 0 ) )
-> print_stmt ;;

   RETURN ( expression_list | 0 )
-> return_stmt ;;

   yield_expression
-> yield_stmt ;;

   RAISE ( expression ( COMMA expression ( COMMA expression | 0 ) | 0 ) | 0 )
-> raise_stmt ;;

   BREAK
-> break_stmt ;;

   CONTINUE
-> continue_stmt ;;

   IMPORT module ( AS name | 0 ) ( COMMA module ( AS name | 0 ) )*
   | FROM relative_module IMPORT IDENTIFIER ( AS name | 0 )
     ( COMMA IDENTIFIER ( AS name | 0 ) )*
   | FROM relative_module IMPORT LPAREN IDENTIFIER ( AS name | 0 )
     ( COMMA IDENTIFIER ( AS name | 0 ) )* ( COMMA | 0 ) RPAREN
   | FROM module IMPORT STAR
-> import_stmt ;;

   ( IDENTIFIER DOT )* IDENTIFIER
-> module ;;

   ( DOT )* module | ( DOT )+
-> relative_module ;;

   IDENTIFIER
-> name ;;

   FROM FUTURE IMPORT feature ( AS name | 0 ) ( COMMA feature ( AS name | 0 ) )*
   | FROM FUTURE IMPORT LPAREN feature ( AS name | 0 )
     ( COMMA feature ( AS name | 0 ) )* ( COMMA | 0 ) RPAREN
-> future_stmt ;;

   IDENTIFIER
-> feature ;;

   GLOBAL IDENTIFIER ( COMMA IDENTIFIER )*
-> global_stmt ;;

   EXEC or_expr ( IN expression ( COMMA expression | 0 ) | 0 )
-> exec_stmt ;;

   if_stmt | while_stmt | for_stmt | try_stmt | with_stmt | funcdef | classdef
-> compount_stmt ;;

   stmt_list LINEBREAK | LINEBREAK INDENT ( statement )+ DEDENT
-> suite ;;

   stmt_list LINEBREAK | compount_stmt
-> statement ;;

   simple_stmt ( SEMICOLON simple_stmt )* SEMICOLON
-> stmt_list ;;

   IF expression COLON suite ( ELIF expression COLON suite )* ( ELSE COLON suite | 0 )
-> if_stmt ;;

   WHILE expression COLON suite ( ELSE COLON suite | 0 )
-> while_stmt ;;

   FOR target_list IN expression_list COLON suite ( ELSE COLON suite | 0 )
-> for_stmt ;;

   try1_stmt | try2_stmt
-> try_stmt ;;

   TRY COLON suite ( EXCEPT ( expression ( COMMA target | 0 ) | 0 ) COLON suite )+
   ( ELSE COLON suite | 0 ) ( FINALLY COLON suite | 0 )
-> try1_stmt ;;

   TRY COLON suite FINALLY COLON suite
-> try2_stmt ;;

   WITH expression ( AS target | 0 ) COLON suite
-> with_stmt ;;

   ( decorators | 0 ) DEF funcname LPAREN ( parameter_list | 0 ) RPAREN COLON suite
-> funcdef ;;

   ( decorator )+
-> decorators ;;

   AT dotted_name ( LPAREN ( argument_list ( COMMA | 0 ) | 0 ) RPAREN | 0 ) LINEBREAK
-> decorator ;;

   IDENTIFIER ( DOT IDENTIFIER )*
-> dotted_name ;;

   ( defparameter COMMA )* ( STAR IDENTIFIER ( COMMA DOUBLESTAR IDENTIFIER | 0 )
     | DOUBLESTAR IDENTIFIER | defparameter ( COMMA | 0 ) )
-> parameter_list ;;

   parameter ( EQUAL expression | 0 )
-> defparameter ;;

   parameter ( COMMA parameter )* ( COMMA | 0 )
-> sublist ;;

   IDENTIFIER | LPAREN sublist RPAREN
-> parameter ;;

   IDENTIFIER
-> funcname ;;

   CLASS classname ( inheritance | 0 ) COLON suite
-> classdef ;;

   LPAREN ( expression_list | 0 ) RPAREN
-> inheritance ;;

   IDENTIFIER
-> classname ;;

-----------------------------------------------------------------
-- Code segments copied to the implementation (.cpp) file.
-- If existent, kdevelop-pg's current syntax requires this block
-- to occur at the end of the file.
-----------------------------------------------------------------

[:
#include "pythonlexer.h"
#include <QtCore/QDebug>

namespace Python
{

void parser::tokenize( const QString& contents )
{
    m_contents = contents;
    Lexer lexer( this, contents );
    int kind = parser::Token_EOF;

    do
    {
        kind = lexer.nextTokenKind();
        if ( !kind ) // when the lexer returns 0, the end of file is reached
        {
            parser::token_type &tt = this->token_stream->next();
            tt.kind = parser::Token_LINEBREAK;
            tt.begin = lexer.tokenBegin();
            tt.end = lexer.tokenEnd();
            kind = parser::Token_EOF;
        }
        parser::token_type &t = this->token_stream->next();
        t.begin = lexer.tokenBegin();
        t.end = lexer.tokenEnd();
        t.kind = kind;
        if( m_debug )
            qDebug() << kind << tokenText(t.begin,t.end) << t.begin << t.end;
    }
    while ( kind != parser::Token_EOF );

    this->yylex(); // produce the look ahead token
}


QString parser::tokenText(std::size_t begin, std::size_t end)
{
    return m_contents.mid(begin,end-begin+1);
}


void parser::reportProblem( parser::ProblemType type, const QString& message )
{
    if (type == Error)
            qDebug() << "** ERROR:" << message;
    else if (type == Warning)
        qDebug() << "** WARNING:" << message;
    else if (type == Info)
        qDebug() << "** Info:" << message;
}


// custom error recovery
void parser::yy_expected_token(int /*expected*/, std::size_t /*where*/, char const *name)
{
    reportProblem( parser::Error, QString("Expected token \"%1\"").arg(name));
}

void parser::yy_expected_symbol(int /*expected_symbol*/, char const *name)
{
    std::size_t line;
    std::size_t col;
    size_t index = token_stream->index()-1;
    token_type &token = token_stream->token(index);
    qDebug() << "token starts at:" << token.begin;
    qDebug() << "index is:" << index;
    token_stream->start_position(index, &line, &col);
    QString tokenValue = tokenText(token.begin, token.end);
    reportProblem( parser::Error,
                   QString("Expected symbol \"%1\" (current token: \"%2\" [%3] at line: %4 col: %5)")
                  .arg(name)
                  .arg(token.kind != 0 ? tokenValue : "EOF")
                  .arg(token.kind)
                  .arg(line)
                  .arg(col));
}

void parser::setDebug( bool debug )
{
    m_debug = debug;
}



} // end of namespace Python

:]
