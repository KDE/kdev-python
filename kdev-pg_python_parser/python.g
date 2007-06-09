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
-- Global  declarations
-----------------------------------------------------------

[:
namespace ruby
{
  class Lexer;
}
:]


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
  void tokenize( char *contents );

  enum problem_type {
      error,
      warning,
      info
  };
  void report_problem( parser::problem_type type, const char* message );
  void report_problem( parser::problem_type type, std::string message );

:]

-----------------------------------------------------------
-- List of defined tokens
-----------------------------------------------------------

-- keywords
%token AND ("and"), DEL ("del"), FOR ("for"), IS ("is"), RAISE ("raise"),
       ASSERT ("assert"), ELIF ("elif"), FROM ("from"), LAMBDA ("lambda"),
       RETURN ("returns"), BREAK ("break"), ELSE ("else"), GLOBAL ("global"),
       NOT ("not"), TRY ("try"), CLASS ("class"), EXCEPT ("except"), IF ("if"),
       OR ("or"), WHILE ("while"), CONTINUE ("continue"), EXEC ("exec"),
       IMPORT ("import"), PASS ("pass"), YIELD ("yield"), DEF ("def"), IN ("in"),
       PRINT ("print"), FINALLY ("finally") ;;

-- indentation which is important in python and linebreak
%token INDENT ("indent"), DEDENT ("dedent"), LINEBREAK ("linebreak") ;;

-- Identifiers, Strings and numbers
%token STRINGLITERAL ("stringliteral"), IDENTIFIER ("identifier"),
       INTEGER ("integer"), FLOAT ("float"), IMAGNUM ("imagnum") ;;

-- separators
%token LPAREN ("lparen"), RPAREN ("rparen"), LBRACE ("lbrace"), RBRACE ("rbrace"),
       LBRACKET ("lbracket"), RBRACKET ("rbracket"), COMMA ("comma"), AT ("at"),
       SEMICOLON ("semicolon"), COLON ("colon"), DOT ("dot"), BACKTICK ("backtick") ;;

-- operators
%token ELLIPSIS ("ellipsis"), STAR ("star"), DOUBLESTAR ("doublestar"), EQUAL ("equal"),
       PLUS ("plus"), MINUS ("minus"), TILDE ("tilde"), SLASH ("slash"),
       DOUBLESLASH ("doubleslash"), MODULO ("modulo"), AND ("and"), LSHIFT ("lshift"),
       RSHIFT ("rshift"), PLUSEQ ("pluseq"), MINUSEQ ("minuseq"), SLASHEQ ("slasheq"),
       DOUBLESLASHEQ ("doubleslasheq"), MODULOEQ ("moduloeq"), ANDEQ ("andeq"),
       STAREQ ("stareq"), DOUBLESTAREQ ("doublestareq"), LSHIFTEQ ("lshifteq"),
       RSHIFTEQ ("rshifteq"), LESS ("less"), GREATER ("greater"), GREATEREQ ("greatereq"),
       LESSEQ ("lesseq"), UNEQUAL ("unequal"), OR ("or"), HAT ("hat"), ISEQUAL ("isequal"),
       TILDEEQ ("tildeeq"), OREQ ("oreq") ;;


-- token that makes the parser fail in any case:
%token INVALID ("invalid token") ;;

-- The actual grammar starts here.

   (#klass= LINEBREAK | stmt )*
-> project ;;

   AT dotted_name ( LPAREN ( arglist | 0) RPAREN | 0 ) LINEBREAK
-> decorator ;;

   decorator*
-> decorators ;;


-- Function Definition
   ( decorators | 0 ) DEF IDENTIFIER LPAREN ( ?[: LA(1).kind != Token_RPAREN :] (vargs = varargslist )*
    | 0 )
    RPAREN COLON suite
-> funcdef ;;

-- Function Defintion
    fpdef ( EQUAL test | 0 )
-> fp_def ;;

    fp_def ( COMMA [:if(yytoken == Token_RPAREN  || yytoken == Token_STAR || yytoken == Token_DOUBLESTAR ) { break; } :] fp_def )*
-> func_def ;;

-- Function variable Arguement List
    func_def (?[: yytoken != Token_RPAREN  && LA(2).kind == Token_IDENTIFIER:] #argparam = argparam | 0 )
-> varargslist ;;

-- The Vararguement trailer, defines *args and **args
    ( STAR IDENTIFIER ( COMMA DOUBLESTAR IDENTIFIER | 0 )
        | DOUBLESTAR IDENTIFIER )
-> argparam;;

-- Function Parameter Definition
   LPAREN (list = fplist) RPAREN
    |  IDENTIFIER
-> fpdef ;;


-- Function parameter List
    fpdef
    ( COMMA [: if ( yytoken == Token_RPAREN )
                  { break; } :]
            fpdef )*
-> fplist ;;

   simple_stmt | compound_stmt
-> stmt ;;

   small_stmt ( SEMICOLON [: if( yytoken == Token_LINEBREAK) { break;} :]small_stmt )*  LINEBREAK
-> simple_stmt ;;


     expr_stmt
   | print_stmt
   | del_stmt
   | pass_stmt
   | flow_stmt
   | import_stmt
   | global_stmt
   | exec_stmt
   | assert_stmt
-> small_stmt ;;

   testlist ( augassign testlist
    | ( EQUAL testlist )+
    | ?[: yytoken == Token_SEMICOLON || yytoken == Token_LINEBREAK :] 0 )
-> expr_stmt ;;

   PLUSEQ
   | MINUSEQ
   | STAREQ
   | SLASHEQ
   | MODULOEQ
   | ANDEQ
   | OREQ
   | TILDEEQ
   | LSHIFTEQ
   | RSHIFTEQ
   | DOUBLESTAREQ
   | DOUBLESLASHEQ
-> augassign ;;

   PRINT ( ( test (COMMA test COMMA)* | (COMMA test)*) | RSHIFT test ( ( COMMA test COMMA )+ ( COMMA test )+ ))
-> print_stmt ;;

   DEL exprlist
-> del_stmt ;;

   PASS
-> pass_stmt ;;

   break_stmt | continue_stmt | return_stmt | raise_stmt | yield_stmt
-> flow_stmt ;;

   BREAK
-> break_stmt ;;

   CONTINUE
-> continue_stmt ;;

   RETURN ( testlist | 0 )
-> return_stmt ;;

   YIELD testlist
-> yield_stmt ;;

   RAISE ( test ( COMMA test ( COMMA test | 0 ) | 0 ) | 0 )
-> raise_stmt ;;

   import_name | import_from
-> import_stmt ;;

   IMPORT dotted_as_names
-> import_name ;;

   FROM dotted_name IMPORT ( STAR | LPAREN import_as_names RPAREN | import_as_names )
-> import_from ;;

   IDENTIFIER ( IDENTIFIER IDENTIFIER | 0 )
-> import_as_name ;;

   dotted_name ( IDENTIFIER IDENTIFIER | 0 )
-> dotted_as_name ;;

   import_as_name ( COMMA import_as_name COMMA)* | ( COMMA import_as_name )*
-> import_as_names ;;

   dotted_as_name ( COMMA dotted_as_name )*
-> dotted_as_names ;;

   IDENTIFIER ( DOT IDENTIFIER )*
-> dotted_name ;;

   GLOBAL IDENTIFIER ( COMMA IDENTIFIER )*
-> global_stmt ;;

   EXEC expr ( IN test ( COMMA test | 0 ) | 0 )
-> exec_stmt ;;

   ASSERT test ( COMMA test | 0 )
-> assert_stmt ;;

   if_stmt
   | while_stmt
   | for_stmt
   | try_stmt
   | funcdef
   | classdef
-> compound_stmt ;;

   IF test COLON suite ( ELIF test COLON suite )* ( ELSE COLON suite | 0 )
-> if_stmt ;;

   WHILE test COLON suite ( ELSE COLON suite | 0 )
-> while_stmt ;;

   FOR exprlist IN testlist COLON suite ( ELSE COLON suite | 0 )
-> for_stmt ;;

   TRY COLON suite
    ( ( except_clause COLON suite )+ ( ELSE COLON suite | 0 ) | FINALLY COLON suite )
-> try_stmt ;;

   EXCEPT ( test ( COMMA test | 0 ) | 0 )
-> except_clause ;;

   simple_stmt | (LINEBREAK)+ INDENT stmt+ DEDENT
-> suite ;;

   and_test ( OR and_test )* | lambda_def
-> test ;;

   not_test ( AND not_test )*
-> and_test ;;

   NOT not_test | comparison
-> not_test ;;

   expr ( comp_op expr )*
-> comparison ;;

   LESS
   | GREATER
   | ISEQUAL
   | GREATEREQ
   | LESSEQ
   | UNEQUAL
   | IN
   | NOT IN
   | IS (NOT | 0)
-> comp_op ;;

   xor_expr (( OR xor_expr )+ | 0)
-> expr ;;

   and_expr (( HAT and_expr )+ | 0)
-> xor_expr ;;

   shift_expr (( AND shift_expr )+ | 0)
-> and_expr ;;

   arith_expr (( ( LSHIFT | RSHIFT ) arith_expr )+ | 0)
-> shift_expr ;;

   term (( ( PLUS | MINUS ) term )+ | 0)
-> arith_expr ;;

   factor (( ( STAR | SLASH | MODULO | DOUBLESLASH ) factor )+ | 0)
-> term ;;

   ( PLUS | MINUS | TILDE ) factor | power
-> factor ;;

   ( atom )
    (trailer)* ( DOUBLESTAR factor | 0 )
-> power ;;

   LPAREN ( testlist_gexp | 0 ) RPAREN
   | LBRACKET listmaker RBRACKET
   | LBRACE dictmaker RBRACE
   | BACKTICK testlist1 BACKTICK
   | IDENTIFIER
   | number
   | STRINGLITERAL
-> atom ;;

   INTEGER
   | FLOAT
   | IMAGNUM
-> number ;;

   ( test ( COMMA [: if (yytoken == Token_RBRACKET) { break; } :] test )* | 0)
-> list_maker ;;

    list_maker (list_for | 0)
-> listmaker ;;

   test ( COMMA [: if (yytoken == Token_RBRACE) { break; } :] test )*
-> test_list_gexp ;;
    test_list_gexp ( gen_for | 0 )
-> testlist_gexp ;;

   LAMBDA ( varargslist | 0 ) COLON test
-> lambda_def ;;

   LPAREN ( arglist | 0 ) RPAREN | LBRACKET subscriptlist RBRACKET | DOT IDENTIFIER
-> trailer ;;

   subscript ( COMMA [: if (yytoken == Token_RBRACKET) { break; } :]
    subscript )*
-> subscriptlist ;;

-- Sub Scripts Check if the curent token is not a COLON it should be a test
-- If a COLON it skips the 'test'. if the next token is not RBRACKET or COMMA after test it can be a COLON.
-- Else it ends.
   ELLIPSIS
    | ( ?[: yytoken != Token_COLON :] test )
    ( ?[: yytoken == Token_RBRACKET || yytoken == Token_COMMA :] 0
        | COLON ( test | 0 ) ( sliceop | 0 ) )
-> subscript ;;

   COLON ( test | 0 )
-> sliceop ;;

   expr
    ( COMMA [: if (yytoken == Token_IN) { break; } :]
    expr )*
-> exprlist ;;

   test ( COMMA test )*
-> testlist ;;

   test ( ( COMMA test )+ ( COMMA | 0 ) | 0 )
-> testlist_safe ;;

   (test COLON test | 0) ( COMMA [: if (yytoken == Token_RBRACE) { break; } :]
    test COLON test )*
-> dictmaker ;;

   CLASS IDENTIFIER ( ( LPAREN testlist RPAREN ) | 0 ) COLON suite
-> classdef ;;

   argument
    ( COMMA [: if(yytoken == Token_RPAREN || yytoken == Token_STAR || yytoken == Token_DOUBLESTAR) { break; } :] argument)*
-> arg_list ;;

    arg_list
    ( STAR test ( ?[: LA(2).kind == Token_DOUBLESTAR :] COMMA DOUBLESTAR test )
    | DOUBLESTAR test | 0)
-> arglist ;;

   test ( ( gen_for | 0 ) | EQUAL test ( LPAREN gen_for RPAREN | 0 ) )
-> argument ;;

   list_for | list_if
-> list_iter ;;

   FOR exprlist IN testlist_safe ( list_iter | 0 )
-> list_for ;;

   IF test ( list_iter | 0 )
-> list_if ;;

   gen_for | gen_if
-> gen_iter ;;

   FOR exprlist IN test ( gen_iter | 0 )
-> gen_for ;;

   IF test ( gen_iter | 0 )
-> gen_if ;;

   test ( COMMA test )*
-> testlist1 ;;

-----------------------------------------------------------------
-- Code segments copied to the implementation (.cpp) file.
-- If existent, kdevelop-pg's current syntax requires this block
-- to occur at the end of the file.
-----------------------------------------------------------------

[:
#include "python_lexer.h"


namespace python
{

void parser::tokenize( char *contents )
{
    Lexer lexer( this, contents );
    int kind = parser::Token_EOF;

    do
    {
        kind = lexer.yylex();
        if( kind == parser::Token_DEDENT)
        {
            int x = kind;
            parser::token_type &t = this->token_stream->next();
            kind = parser::Token_LINEBREAK;
            t.kind = kind;
            t.begin = lexer.tokenBegin();
            t.end = lexer.tokenEnd();
            t.text = contents;
            std::cerr<<t.kind<<std::endl;
            while(lexer.dedent_level>1)
            {
                parser::token_type &t = this->token_stream->next();
                t.kind = parser::Token_DEDENT;
                t.begin = lexer.tokenBegin();
                t.end = lexer.tokenEnd();
                t.text = contents;
                std::cerr<<t.kind<<std::endl;
                lexer.dedent_level--;
            }
            lexer.dedent_level=0;
            kind = x;
        }
        else if( kind == parser::Token_INDENT)
        {
            int x = kind;
            kind = parser::Token_LINEBREAK;
            parser::token_type &t = this->token_stream->next();
            t.kind = kind;
            t.begin = lexer.tokenBegin();
            t.end = lexer.tokenEnd();
            t.text = contents;
            std::cerr<<t.kind<<std::endl;
            kind = x;
        }
        std::cerr << kind;
        std::cerr << lexer.YYText() << std::endl; //" "; // debug output

        if ( !kind ) // when the lexer returns 0, the end of file is reached
            kind = parser::Token_EOF;

        parser::token_type &t = this->token_stream->next();
        t.kind = kind;
        t.begin = lexer.tokenBegin();
        t.end = lexer.tokenEnd();
        t.text = contents;
    }
    while ( kind != parser::Token_EOF );

    this->yylex(); // produce the look ahead token
}

} // end of namespace cool

:]

-- kate: space-indent on; indent-width 4; tab-width: 4; replace-tabs on; auto-insert-doxygen on

