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

%namespace shift_expression
[: 
    enum shift_operator_enum {
        op_lshift,
        op_rshift,
    };
:]

%namespace arith_expression
[:
    enum arith_operator_enum {
        op_plus,
        op_minus,
    };
:]

%namespace term
[:
    enum term_operator_enum {
        op_star,
        op_slash,
        op_modulo,
        op_doubleslash,
    };
:]

%namespace factor
[:
    enum factor_operator_enum {
        op_factor_plus,
        op_factor_minus,
        op_factor_tilde,
    };
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
       PRINT ("print"), FINALLY ("finally"), AS ("as") ;;

-- indentation which is important in python and linebreak
%token INDENT ("indent"), DEDENT ("dedent"), LINEBREAK ("linebreak") ;;

-- Identifiers, Strings and numbers
%token STRINGLITERAL ("stringliteral"), IDENTIFIER ("identifier"),
       INTEGER ("integer"), FLOAT ("float"), IMAGNUM ("imagnum"),
        LONGSTRING ("longstring"), STRINGBODY ("stringbody"), SHORTSTRING ("shrtstring") ;;

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
       TILDEEQ ("tildeeq"), OREQ ("oreq"), ANDD ("andd") , ORR ("orr");;


-- token that makes the parser fail in any case:
%token INVALID ("invalid token") ;;

-- The actual grammar starts here.

   ( #stmt = stmt )*
-> project ;;

   AT decorator_name = dotted_name ( LPAREN ( arguments=arglist | 0) RPAREN | 0 ) LINEBREAK
-> decorator ;;

   (#decorator = decorator )*
-> decorators ;;

-- Function Definition
   ( decorators = decorators | 0 )
    DEF func_name=IDENTIFIER LPAREN ( ?[: LA(1).kind != Token_RPAREN :] ( #fun_args = varargslist )*
    | 0 )
    RPAREN COLON fun_suite=suite
-> funcdef ;;

-- Function Defintion
    fpdef ( EQUAL test | 0 )
-> fp_def ;;

    fp_def ( COMMA [:if(yytoken == Token_RPAREN  || yytoken == Token_STAR || yytoken == Token_DOUBLESTAR ) { break; } :] fp_def )*
-> func_def ;;

-- Function variable Arguement List
    func_def (
    ?[: yytoken != Token_RPAREN  && LA(2).kind == Token_IDENTIFIER:] (fun_pos_param = fun_pos_param )
    | 0 
    )
-> varargslist ;;

-- The Vararguement trailer, defines *args and **args
    ( STAR IDENTIFIER ( COMMA DOUBLESTAR IDENTIFIER | 0 )
        | DOUBLESTAR IDENTIFIER )
-> fun_pos_param;;

-- Function Parameter Definition
   LPAREN (fplist = fplist) RPAREN
    |  IDENTIFIER
-> fpdef ;;


-- Function parameter List
    #fpdef=fpdef
    ( COMMA [: if ( yytoken == Token_RPAREN )
                  { break; } :]
            #fpdef=fpdef )*
-> fplist ;;

-- A statement could be simple statement/ a compont statement OR just a Linebreak
    simple_stmt = simple_stmt 
    | compound_stmt = compound_stmt 
    | LINEBREAK
-> stmt ;;

   #small_stmt = small_stmt 
    ( SEMICOLON [: if( yytoken == Token_LINEBREAK || yytoken == Token_DEDENT) { break;} :] #small_stmt = small_stmt )*  LINEBREAK
-> simple_stmt ;;


     expr_stmt = expr_stmt
   | print_stmt = print_stmt
   | del_stmt = del_stmt
   | pass_stmt = pass_stmt
   | flow_stmt = flow_stmt
   | import_stmt = import_stmt
   | global_stmt= global_stmt
   | exec_stmt = exec_stmt
   | assert_stmt = assert_stmt
-> small_stmt ;;

   (#testlist = testlist) ( augassign = augassign #testlist = testlist
    | ( EQUAL #testlist = testlist )+
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

   PRINT (#print_args=test ( COMMA [: if(yytoken == Token_SEMICOLON || yytoken == Token_LINEBREAK) {break; } :]#print_args=test )*
    | RSHIFT #rshift_args=test ( COMMA [: if(yytoken == Token_SEMICOLON || yytoken == Token_LINEBREAK) {break; } :]#rshift_test=test )*)
-> print_stmt ;;

   DEL del_list=exprlist
-> del_stmt ;;

   PASS
-> pass_stmt ;;

   break_stmt=break_stmt 
    | continue_stmt=continue_stmt 
    | return_stmt=return_stmt 
    | raise_stmt=raise_stmt 
    | yield_stmt=yield_stmt
-> flow_stmt ;;

   BREAK
-> break_stmt ;;

   CONTINUE
-> continue_stmt ;;

   RETURN ( return_expr=testlist | 0 )
-> return_stmt ;;

   YIELD yield_expr=testlist
-> yield_stmt ;;

   RAISE ( raise_type=test ( COMMA raise_type=test ( COMMA raise_type=test | 0 ) | 0 ) | 0 )
-> raise_stmt ;;

   import_name=import_name 
    | import_from=import_from
-> import_stmt ;;

   IMPORT import_name=dotted_as_names
-> import_name ;;

   FROM import_from_name=dotted_name IMPORT ( STAR | LPAREN import_as_names=import_as_names RPAREN | import_as_names=import_as_names )
-> import_from ;;

   imported_name=IDENTIFIER ( AS imported_as=IDENTIFIER | 0 )
-> import_as_name ;;

   import_dotted_name=dotted_name ( AS imported_as=IDENTIFIER | 0 )
-> dotted_as_name ;;

   #import_as_name=import_as_name
    ( COMMA [: if( yytoken == Token_RPAREN || yytoken == Token_LINEBREAK || yytoken == Token_SEMICOLON ) { break;} :] #import_as_name=import_as_name)*
-> import_as_names ;;

   #dotted_as_name=dotted_as_name ( COMMA #dotted_as_name=dotted_as_name )*
-> dotted_as_names ;;

   dotted_name=IDENTIFIER ( DOT dotted_name=IDENTIFIER )*
-> dotted_name ;;

   GLOBAL #global_name=IDENTIFIER ( COMMA #global_name=IDENTIFIER )*
-> global_stmt ;;

   EXEC exec_expr=expr ( IN exec_test=test ( COMMA exec_test=test | 0 ) | 0 )
-> exec_stmt ;;

   ASSERT assert_test=test ( COMMA assert_test=test | 0 )
-> assert_stmt ;;

   if_stmt=if_stmt
   | while_stmt=while_stmt
   | for_stmt=for_stmt
   | try_stmt=try_stmt
   | fucdef=funcdef
   | classdef=classdef
-> compound_stmt ;;

   IF #if_test=test COLON if_suite=suite ( ELIF #elif_test=test COLON elif_suite=suite )* ( ELSE COLON if_else_suite=suite | 0 )
-> if_stmt ;;

   WHILE while_test=test COLON while_suite=suite ( ELSE COLON while_else_suite=suite | 0 )
-> while_stmt ;;

   FOR for_expr=exprlist IN for_testlist=testlist COLON for_suite=suite ( ELSE COLON for_else_suite=suite | 0 )
-> for_stmt ;;

   TRY COLON try_suite=suite
    ( ( except_clause=except_clause COLON except_suite=suite )+ ( ELSE COLON try_else_suite=suite | 0 ) | FINALLY COLON finally_suite=suite )
-> try_stmt ;;

   EXCEPT ( except_test=test ( COMMA except_test=test | 0 ) | 0 )
-> except_clause ;;

   simple_stmt=simple_stmt | (LINEBREAK)+ INDENT (#stmt=stmt)+ DEDENT
-> suite ;;

   #and_test=and_test ( OR #and_test=and_test )* | lambda_def=lambda_def
-> test ;;

   #not_test=not_test ( AND #not_test=not_test )*
-> and_test ;;

   NOT not_test=not_test | comparison=comparison
-> not_test ;;

   #expr=expr ( #comp_op=comp_op #expr=expr )*
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

   #xor_expr=xor_expr ( ORR #xor_expr=xor_expr )*
-> expr ;;

   #and_expr=and_expr ( HAT #and_expr=and_expr )*
-> xor_expr ;;

   #shift_expr=shift_expr ( ANDD #shif_expr=shift_expr )*
-> and_expr ;;

   #arith_expr=arith_expr 
    ( ( LSHIFT  [: (*yynode)->shift_operator = shift_expression::op_lshift; :]
    | RSHIFT    [: (*yynode)->shift_operator = shift_expression::op_rshift; :]
    ) #arith_expr=arith_expr )*
-> shift_expr [ 
    member variable shift_operator: shift_expression::shift_operator_enum; ];;

   #arith_term=term (( 
    ( PLUS      [: (*yynode)->arith_operator = arith_expression::op_plus;   :]
    | MINUS     [: (*yynode)->arith_operator = arith_expression::op_minus;  :]
    ) #arith_term=term )+ | 0)
-> arith_expr [ 
    member variable arith_operator: arith_expression::arith_operator_enum; ];;

   #factor=factor (( 
    ( STAR      [: (*yynode)->term_operator = term::op_star;                :]
    | SLASH     [: (*yynode)->term_operator = term::op_slash;               :]
    | MODULO    [: (*yynode)->term_operator = term::op_modulo;              :]
    | DOUBLESLASH [: (*yynode)->term_operator = term::op_doubleslash;       :]
    ) #factor=factor )+ | 0)
-> term [ 
    member variable term_operator: term::term_operator_enum; ];;

   ( 
    PLUS        [: (*yynode)->factor_operator = factor::op_factor_plus;     :]
    | MINUS     [: (*yynode)->factor_operator = factor::op_factor_minus;    :]
    | TILDE     [: (*yynode)->factor_operator = factor::op_factor_tilde ;   :]
    ) #factor=factor | #power=power
-> factor [ 
    member variable factor_operator: factor::factor_operator_enum;   ];;

   ( atom=atom )
    (#trailer=trailer)* ( DOUBLESTAR factor=factor | 0 )
-> power ;;

   LPAREN ( testlist_gexp=testlist_gexp | 0 ) RPAREN
   | LBRACKET listmaker=listmaker RBRACKET
   | LBRACE dictmaker=dictmaker RBRACE
   | BACKTICK testlist1=testlist1 BACKTICK
   | atom_identifier_name=IDENTIFIER
   | number=number
   | (#stringliteral=STRINGLITERAL)+
   | longstringliteral=longstringliteral
   | shortstringliteral=shortstringliteral
-> atom ;;

   SHORTSTRING ( STRINGBODY )+ SHORTSTRING
-> shortstringliteral ;;

   LONGSTRING ( STRINGBODY )+ LONGSTRING
-> longstringliteral ;;

   INTEGER
   | FLOAT
   | IMAGNUM
-> number ;;

   ( #list_test=test ( COMMA [: if (yytoken == Token_RBRACKET) { break; } :] #list_test=test )* | 0)
-> list_maker ;;

    list_maker=list_maker (list_for=list_for | 0)
-> listmaker ;;

   #test=test ( COMMA [: if (yytoken == Token_RBRACE) { break; } :] #test=test )*
-> test_list_gexp ;;

    test_list_gexp=test_list_gexp ( gen_for=gen_for | 0 )
-> testlist_gexp ;;

   LAMBDA ( lambda_varargslist=varargslist | 0 ) COLON lambda_test=test
-> lambda_def ;;

   LPAREN ( trailer_arglist=arglist | 0 ) RPAREN | LBRACKET subscriptlist=subscriptlist RBRACKET | DOT tariler_dot_name=IDENTIFIER
-> trailer ;;

   #subscript=subscript ( COMMA [: if (yytoken == Token_RBRACKET) { break; } :]
    #subscript=subscript )*
-> subscriptlist ;;

-- Sub Scripts Check if the curent token is not a COLON it should be a test
-- If a COLON it skips the 'test'. if the next token is not RBRACKET or COMMA after test it can be a COLON.
-- Else it ends.
   subcript_ellipsis=ELLIPSIS
    | ( ?[: yytoken != Token_COLON :] test=test | 0 )
    ( ?[: yytoken == Token_RBRACKET || yytoken == Token_COMMA :] 0
        | COLON ( test=test | 0 ) ( sliceop=sliceop | 0 ) )
-> subscript ;;

   COLON ( slice_test=test | 0 )
-> sliceop ;;

   #expr=expr
    ( COMMA [: if (yytoken == Token_IN || yytoken == Token_SEMICOLON || yytoken == Token_LINEBREAK ) { break; } :]
    #expr=expr )*
-> exprlist ;;

   #test=test ( COMMA [: if( yytoken == Token_COLON || yytoken == Token_SEMICOLON || yytoken == Token_RPAREN || yytoken == Token_LINEBREAK) {break;} :]
    #test=test )*
-> testlist ;;

   #test=test ( ( COMMA #test=test )+ ( COMMA | 0 ) | 0 )
-> testlist_safe ;;

   (#test=test COLON #test=test | 0) ( COMMA [: if (yytoken == Token_RBRACE) { break; } :]
    #test=test COLON #test=test )*
-> dictmaker ;;

   CLASS class_name=IDENTIFIER ( ( LPAREN testlist=testlist RPAREN ) | 0 ) COLON class_suite=suite
-> classdef ;;

   #arguement=argument
    ( COMMA [: if(yytoken == Token_RPAREN || yytoken == Token_STAR || yytoken == Token_DOUBLESTAR) { break; } :] #arguement=argument)*
-> arg_list ;;

    arg_list=arg_list
    ( STAR test=test ( ?[: LA(2).kind == Token_DOUBLESTAR :] COMMA arglist_star_doublestar=DOUBLESTAR test=test )
    | arglist_doublestar=DOUBLESTAR test=test | 0)
-> arglist ;;

   test=test ( EQUAL test=test ( ?[: LA(2).kind == Token_FOR :] LPAREN gen_for=gen_for RPAREN | 0 )
    | ?[: yytoken == Token_FOR :] gen_for=gen_for
    | ?[: yytoken == Token_RPAREN || yytoken == Token_STAR || yytoken == Token_DOUBLESTAR || yytoken == Token_COMMA :] 0 )
-> argument ;;

   list_for=list_for | list_if=list_if
-> list_iter ;;

   FOR exprlist=exprlist IN testlist_safe=testlist_safe ( list_iter=list_iter | 0 )
-> list_for ;;

   IF test=test ( list_iter=list_iter | 0 )
-> list_if ;;

   gen_for=gen_for
    | gen_if=gen_if
-> gen_iter ;;

   FOR exprlist=exprlist IN test=test ( gen_iter=gen_iter | 0 )
-> gen_for ;;

   IF test=test ( gen_iter=gen_iter | 0 )
-> gen_if ;;

   #test=test ( COMMA #test=test )*
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
            while(lexer.dedentationLevel()>1)
            {
                parser::token_type &t = this->token_stream->next();
                t.kind = parser::Token_DEDENT;
                t.begin = lexer.tokenBegin();
                t.end = lexer.tokenEnd();
                t.text = contents;
                std::cerr<<t.kind<<std::endl;
                lexer.setDedentationLevel(lexer.dedentationLevel()-1);
            }
            lexer.setDedentationLevel(0);
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

