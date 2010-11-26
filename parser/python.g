-------------------------------------------------------------------------------
-- Copyright (c) 2006 Andreas Pakulat <apaku@gmx.de>
-- Copyright (c) 2007 Piyush Verma  <piyush.verma@gmail.com>
--
-- 
-- This program is free software; you can redistribute it and/or
-- modify it under the terms of the GNU General Public License
-- as published by the Free Software Foundation; either version 2
-- of the License, or (at your option) any later version.
--
-- This program is distributed in the hope that it will be useful,
-- but WITHOUT ANY WARRANTY; without even the implied warranty of
-- MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
-- GNU General Public License for more details.
--
-- You should have received a copy of the GNU General Public License
-- along with this program; if not, write to the Free Software
-- Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
-- 02110-1301, USA.
-------------------------------------------------------------------------------

-----------------------------------------------------------
-- Grammar for Python2.5
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
--   parser::pythonCompatibilityMode m_compatibilityMode;
--
--   struct ParserState {
--   };
--   ParserState m_state;
-- :]
-- Parser::parserState *Parser::copyCurrentState()
-- {
--     ParserState *state = new ParserState();
--     return state;
-- }
--
-- void Parser::restoreState( Parser::ParserState *state )
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
#include <kdebug.h>

namespace PythonParser
{
    class Lexer;

    enum OperatorType {
        LeftShiftOp,
        RightShiftOp,
        PlusOp,
        MinusOp,
        StarOp,
        SlashOp,
        ModuloOp,
        DoubleSlashOp,
        UnaryPlusOp,
        UnaryMinusOp,
        UnaryTildeOp,
        PlusEqOp,
        MinusEqOp,
        StarEqOp,
        SlashEqOp,
        ModuloEqOp,
        AndEqOp,
        OrEqOp,
        HatEqOp,
        LeftShiftEqOp,
        RightShiftEqOp,
        DoublestarEqOp,
        DoubleslashEqOp,
        LessOp,
        GreaterOp,
        IsEqualOp,
        GreaterEqOp,
        LessEqOp,
        UnEqualOp,
        InOp,
        NotInOp,
        IsOp,
        IsNotOp
    };
    enum NumericType  {
        IntegerNumeric,
        FloatNumeric,
        ImaginaryNumeric
    };
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
  void reportProblem( Parser::ProblemType type, const QString& message );
  QString tokenText(qint64 begin, qint64 end);
  void setDebug(bool debug);

:]

%parserclass (private declaration)
[:
   QString mContents;
   bool mDebug;
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
       LESSEQ ("lesseq"), UNEQUAL ("unequal"), OR ("or"), BITXOR ("bitxor"), ISEQUAL ("isequal"),
       TILDEEQ ("tildeeq"), OREQ ("oreq"), BITAND ("bitand") , BITOR ("bitor");;


-- token that makes the parser fail in any case:
%token INVALID ("invalid token") ;;

-- The actual grammar starts here.

   ( #stmt = stmt )*
-> project ;;

   AT decoratorName = dottedName ( LPAREN ( arguments=arglist | 0) RPAREN | 0 ) LINEBREAK
-> decorator ;;

   (#decorator = decorator )+
-> decorators ;;

-- Function Definition: Can start with Decorators.
-- varargslist defines the Function Variable Arguements
   ( decorators = decorators | 0 )
    DEF funcName=IDENTIFIER LPAREN ( ?[: LA(1).kind != Token_RPAREN :] ( funArgs = varargslist )
    | 0 )
    RPAREN COLON funSuite=suite
-> funcdecl ;;

-- Function variable Arguement List
    ( funcDef=funcDef | 0 ) (
    ?[: yytoken != Token_RPAREN  && LA(2).kind == Token_IDENTIFIER:] (funPosParam = funPosParam )
    | 0
    )
-> varargslist ;;

-- The Vararguement trailer, defines *args and **args
    ( listParam=listParam ( COMMA dictParam=dictParam | 0 )
        | dictParam=dictParam )
-> funPosParam;;

   DOUBLESTAR doubleStarId=IDENTIFIER
-> dictParam;;

   STAR starId=IDENTIFIER
-> listParam;;

-- Function Definition
    #fpDef=fpDef ( COMMA [:if(yytoken == Token_RPAREN  || yytoken == Token_STAR || yytoken == Token_DOUBLESTAR ) { break; } :] #fpDef=fpDef )*
-> funcDef ;;


-- Function parameter Defintion
    defparam=defparam ( EQUAL fpDefTest=test | 0 )
-> fpDef ;;

-- Function Parameter Definition
   LPAREN (fplist = fplist) RPAREN
    |  paramname=IDENTIFIER
-> defparam ;;


-- Function parameter List
    #fplistFpdef=defparam
    ( COMMA [: if ( yytoken == Token_RPAREN )
                  { break; } :]
            #fplistFpdef=defparam )*
-> fplist ;;

-- A statement could be simple statement, a compound statement OR just a Linebreak
    simpleStmt = simpleStmt
    | compoundStmt = compoundStmt
    | LINEBREAK
-> stmt ;;

-- simple statement, TODO this needs more work for simpleStmts at the enf of files
   #smallStmt = smallStmt
    ( SEMICOLON [: if( yytoken == Token_LINEBREAK || yytoken == Token_DEDENT) { break;} :] #smallStmt = smallStmt )*  LINEBREAK
-> simpleStmt ;;

-- a small statement could be of any such kinds
     exprStmt = exprStmt
   | printStmt = printStmt
   | delStmt = delStmt
   | passStmt = passStmt
   | flowStmt = flowStmt
   | importStmt = importStmt
   | globalStmt= globalStmt
   | execStmt = execStmt
   | assertStmt = assertStmt
-> smallStmt ;;

   (testlist = testlist) ( augassign = augassign ( anugassignTestlist = testlist | yield=yieldExpr )
    | ( EQUAL ( yield=yieldExpr | #equalTestlist = testlist ) )+
    | ?[: yytoken == Token_SEMICOLON || yytoken == Token_LINEBREAK :] 0 )
-> exprStmt ;;

   PLUSEQ           [: (*yynode)->assignOp = PythonParser::PlusEqOp;   :]
   | MINUSEQ        [: (*yynode)->assignOp = PythonParser::MinusEqOp;  :]
   | STAREQ         [: (*yynode)->assignOp = PythonParser::StarEqOp;   :]
   | SLASHEQ        [: (*yynode)->assignOp = PythonParser::SlashEqOp;  :]
   | MODULOEQ       [: (*yynode)->assignOp = PythonParser::ModuloEqOp; :]
   | ANDEQ          [: (*yynode)->assignOp = PythonParser::AndEqOp;    :]
   | OREQ           [: (*yynode)->assignOp = PythonParser::OrEqOp;     :]
   | TILDEEQ        [: (*yynode)->assignOp = PythonParser::HatEqOp;  :]
   | LSHIFTEQ       [: (*yynode)->assignOp = PythonParser::LeftShiftEqOp; :]
   | RSHIFTEQ       [: (*yynode)->assignOp = PythonParser::RightShiftEqOp; :]
   | DOUBLESTAREQ   [: (*yynode)->assignOp = PythonParser::DoublestarEqOp; :]
   | DOUBLESLASHEQ  [: (*yynode)->assignOp = PythonParser::DoubleslashEqOp;:]
-> augassign [
    member variable assignOp : PythonParser::OperatorType; ];;

   PRINT
    (
    (#printArgs=test ( COMMA [: if(yytoken == Token_SEMICOLON || yytoken == Token_LINEBREAK) {break; } :]#printArgs=test )*)
    | RSHIFT #rshiftArgs=test ( ( COMMA [: if(yytoken == Token_SEMICOLON || yytoken == Token_LINEBREAK) {break; } :]#rshiftArgs=test )*)
    | 0
    )
-> printStmt ;;

   DEL delList=exprlist
-> delStmt ;;

   PASS
-> passStmt ;;

   breakStmt=breakStmt
    | continueStmt=continueStmt
    | returnStmt=returnStmt
    | raiseStmt=raiseStmt
    | yieldStmt=yieldStmt
-> flowStmt ;;

   BREAK
-> breakStmt ;;

   CONTINUE
-> continueStmt ;;

   RETURN ( returnExpr=testlist | 0 )
-> returnStmt ;;

   YIELD ( expr=testlist | 0 )
-> yieldExpr ;;

   yield=yieldExpr
-> yieldStmt ;;

   RAISE ( type=test ( COMMA value=test ( COMMA traceback=test | 0 ) | 0 ) | 0 )
-> raiseStmt ;;

   importImport=importName
    | importFrom=importFrom
-> importStmt ;;

   IMPORT importName=dottedAsNames
-> importName ;;

   FROM importFromName=dottedName IMPORT ( STAR | LPAREN importAsNames=importAsNames RPAREN | importAsNames=importAsNames )
-> importFrom ;;

   importedName=IDENTIFIER ( AS importedAs=IDENTIFIER | 0 )
-> importAsName ;;

   importDottedName=dottedName ( AS importedAs=IDENTIFIER | 0 )
-> dottedAsName ;;

   #importAsName=importAsName
    ( COMMA [: if( yytoken == Token_RPAREN || yytoken == Token_LINEBREAK || yytoken == Token_SEMICOLON ) { break;} :] #importAsName=importAsName)*
-> importAsNames ;;

   #dottedAsName=dottedAsName ( COMMA #dottedAsName=dottedAsName )*
-> dottedAsNames ;;

   #dottedName=IDENTIFIER ( DOT #dottedName=IDENTIFIER )*
-> dottedName ;;

   GLOBAL #globalName=IDENTIFIER ( COMMA #globalName=IDENTIFIER )*
-> globalStmt ;;

   EXEC execCode=expr ( IN globalDictExec=test ( COMMA localDictExec=test | 0 ) | 0 )
-> execStmt ;;

   ASSERT assertNotTest=test ( COMMA assertRaiseTest=test | 0 )
-> assertStmt ;;

   ifStmt=ifStmt
   | whileStmt=whileStmt
   | forStmt=forStmt
   | tryStmt=tryStmt
   | funcdecl=funcdecl
   | classdef=classdef
-> compoundStmt ;;

   IF ifTest=test COLON ifSuite=suite ( ELIF #elifTest=test COLON #elifSuite=suite )* ( ELSE COLON ifElseSuite=suite | 0 )
-> ifStmt ;;

   WHILE whileTest=test COLON whileSuite=suite ( ELSE COLON whileElseSuite=suite | 0 )
-> whileStmt ;;

   FOR forExpr=exprlist IN forTestlist=testlist COLON forSuite=suite ( ELSE COLON forElseSuite=suite | 0 )
-> forStmt ;;

   TRY COLON trySuite=suite
    ( ( #exceptClause=exceptClause COLON #exceptSuite=suite )+ ( ELSE COLON tryElseSuite=suite | 0 ) | FINALLY COLON finallySuite=suite )
-> tryStmt ;;

   EXCEPT ( exceptTest=test ( COMMA exceptTargetTest=test | 0 ) | 0 )
-> exceptClause ;;

   simpleStmt=simpleStmt | (LINEBREAK)+ INDENT (#stmt=stmt)+ DEDENT
-> suite ;;

   #andTest=andTest ( OR #andTest=andTest )* | lambdaDef=lambdaDef
-> test ;;

   #notTest=notTest ( AND #notTest=notTest )*
-> andTest ;;

   NOT notTest=notTest | comparison=comparison
-> notTest ;;

   compExpr=expr ( #compOp=compOp #compOpExpr=expr )*
-> comparison ;;

   LESS         [: (*yynode)->compOp = PythonParser::LessOp;      :]
   | GREATER    [: (*yynode)->compOp = PythonParser::GreaterOp;   :]
   | ISEQUAL    [: (*yynode)->compOp = PythonParser::IsEqualOp;   :]
   | GREATEREQ  [: (*yynode)->compOp = PythonParser::GreaterEqOp; :]
   | LESSEQ     [: (*yynode)->compOp = PythonParser::LessEqOp;    :]
   | UNEQUAL    [: (*yynode)->compOp = PythonParser::UnEqualOp;   :]
   | IN         [: (*yynode)->compOp = PythonParser::InOp;        :]
   | NOT IN     [: (*yynode)->compOp = PythonParser::NotInOp;    :]
   | IS (NOT    [: (*yynode)->compOp = PythonParser::IsNotOp;    :]
        | 0     [: (*yynode)->compOp = PythonParser::IsOp;        :]
    )
-> compOp [
        member variable compOp : PythonParser::OperatorType; ];;

   expr=xorExpr ( BITOR #orrExpr=xorExpr )*
-> expr ;;

   xorExpr=andExpr ( BITXOR #hatXorExpr=andExpr )*
-> xorExpr ;;

   andExpr=shiftExpr ( BITAND #anddShifExpr=shiftExpr )*
-> andExpr ;;

   arithExpr=arithExpr
    ( #shiftOpList=shiftOp #arithExprList=arithExpr )*
-> shiftExpr ;;

    LSHIFT      [: (*yynode)->shiftOp = PythonParser::LeftShiftOp;   :]
    | RSHIFT    [: (*yynode)->shiftOp = PythonParser::RightShiftOp;   :]
-> shiftOp [
    member variable shiftOp : PythonParser::OperatorType; ];;

   arithTerm=term
    ((#arithOpList = arithOp #arithTermList=term )+ | 0)
-> arithExpr ;;

    PLUS        [: (*yynode)->arithOp = PythonParser::PlusOp;     :]
    | MINUS     [: (*yynode)->arithOp = PythonParser::MinusOp;    :]
-> arithOp [
    member variable arithOp: PythonParser::OperatorType; ] ;;

   factor=factor
    ((#termOp = termOp #factors=factor )+ | 0)
-> term ;;

    STAR        [: (*yynode)->op = PythonParser::StarOp;      :]
    | SLASH     [: (*yynode)->op = PythonParser::SlashOp;     :]
    | MODULO    [: (*yynode)->op = PythonParser::ModuloOp;    :]
    | DOUBLESLASH [: (*yynode)->op = PythonParser::DoubleSlashOp; :]
-> termOp [
    member variable op : PythonParser::OperatorType; ];;

   ( factOp=factOp) factor=factor | power=power
-> factor ;;

    PLUS        [: (*yynode)->op = PythonParser::UnaryPlusOp;     :]
    | MINUS     [: (*yynode)->op = PythonParser::UnaryMinusOp;    :]
    | TILDE     [: (*yynode)->op = PythonParser::UnaryTildeOp ;   :]
-> factOp [
    member variable op : PythonParser::OperatorType;   ];;

   ( atom=atom )
    (#trailer=trailer)* ( DOUBLESTAR factor=factor | 0 )
-> power ;;

   LPAREN ( yield=yieldExpr |
            ( testlist=testlist ( genFor=genFor | 0 ) ) | 0 ) RPAREN
   | LBRACKET listmaker=listmaker RBRACKET
   | LBRACE dictmaker=dictmaker RBRACE
   | BACKTICK codeexpr=codeexpr BACKTICK
   | atomIdentifierName=IDENTIFIER
   | number=number
   | (#stringliteral=STRINGLITERAL)+
-> atom ;;


   value=INTEGER      [: (*yynode)->numType = PythonParser::IntegerNumeric;      :]
   | value=FLOAT      [: (*yynode)->numType = PythonParser::FloatNumeric;    :]
   | value=IMAGNUM    [: (*yynode)->numType = PythonParser::ImaginaryNumeric;  :]
-> number [
    member variable numType: PythonParser::NumericType; ];;

   ( #listTest=test ( COMMA [: if (yytoken == Token_RBRACKET) { break; } :] #listTest=test )* | 0)
-> listMakerTest ;;

    listMakerTest=listMakerTest (listFor=listFor | 0)
-> listmaker ;;

   LAMBDA ( lambdaVarargslist=varargslist | 0 ) COLON lambdaTest=test
-> lambdaDef ;;

   LPAREN ( trailerArglist=arglist | 0 ) RPAREN | LBRACKET subscriptlist=subscriptlist RBRACKET | DOT trailerDotName=IDENTIFIER
-> trailer ;;

   #subscript=subscript ( COMMA [: (*yynode)->hasComma = true; if (yytoken == Token_RBRACKET) { break; } :]
    #subscript=subscript )*
-> subscriptlist [
    member variable hasComma: bool; ] ;;

-- Sub Scripts Check if the curent token is not a COLON it should be a test
-- If a COLON it skips the 'test'. if the next token is not RBRACKET or COMMA after test it can be a COLON.
-- Else it ends.
   ELLIPSIS [: (*yynode)->isEllipsis = true; :]
    | ( ?[: yytoken != Token_COLON :] begin=test | 0 )
    ( ?[: yytoken == Token_RBRACKET || yytoken == Token_COMMA :] 0
        | COLON [: (*yynode)->hasColon = true; :] ( end=test | 0 )
          ( COLON [: (*yynode)->hasColon = true; :]
            ( step=test | 0 ) | 0 ) )
-> subscript
    [: (*yynode)->isEllipsis = false;
       (*yynode)->hasColon = false; :]
    [  member variable isEllipsis: bool;
       member variable hasColon: bool; ] ;;

   #expr=expr
    ( COMMA [: if (yytoken == Token_IN || yytoken == Token_SEMICOLON || yytoken == Token_LINEBREAK ) { break; } :]
    #expr=expr )*
-> exprlist ;;

   #tests=test ( COMMA [: if( yytoken == Token_COLON || yytoken == Token_SEMICOLON || yytoken == Token_RPAREN || yytoken == Token_LINEBREAK) {break;} :]
    #tests=test )*
-> testlist ;;

   #test=test ( ( COMMA #test=test )+ ( COMMA | 0 ) | 0 )
-> testlistSafe ;;

   (#keyList=test COLON #valueList=test | 0) ( COMMA [: if (yytoken == Token_RBRACE) { break; } :]
    #keyList=test COLON #valueList=test )*
-> dictmaker ;;

   CLASS className=IDENTIFIER ( ( LPAREN testlist=testlist RPAREN ) | 0 ) COLON classSuite=suite
-> classdef ;;

   #arguments=argument
    ( COMMA [: if(yytoken == Token_RPAREN || yytoken == Token_STAR || yytoken == Token_DOUBLESTAR) { break; } :] #arguments=argument)*
-> plainArgumentsList ;;

    (argListBegin=plainArgumentsList | 0)
    (
        ( STAR arglistStar=test (?[: LA(1).kind != Token_RPAREN :] COMMA DOUBLESTAR arglistDoublestar=test | 0)
        | DOUBLESTAR arglistDoublestar=test)
    | 0 )
-> arglist ;;

   argumentTest=test ( EQUAL argumentEqualTest=test
    | ?[: yytoken == Token_FOR :] genFor=genFor
    | ?[: yytoken == Token_RPAREN || yytoken == Token_STAR || yytoken == Token_DOUBLESTAR || yytoken == Token_COMMA :] 0 )
-> argument ;;

   listFor=listFor | listIf=listIf
-> listIter ;;

   FOR exprlist=exprlist IN testlistSafe=testlistSafe ( listIter=listIter | 0 )
-> listFor ;;

   IF test=test ( listIter=listIter | 0 )
-> listIf ;;

   genFor=genFor
    | genIf=genIf
-> genIter ;;

   FOR exprlist=exprlist IN test=test ( genIter=genIter | 0 )
-> genFor ;;

   IF test=test ( genIter=genIter | 0 )
-> genIf ;;

   #test=test ( COMMA #test=test )*
-> codeexpr ;;

-----------------------------------------------------------------
-- Code segments copied to the implementation (.cpp) file.
-- If existent, kdevelop-pg's current syntax requires this block
-- to occur at the end of the file.
-----------------------------------------------------------------

[:
#include "pythonlexer.h"
#include <QtCore/QDebug>

namespace PythonParser
{

void Parser::tokenize( const QString& contents )
{
    mContents = contents;
    Lexer lexer( this, contents );
    int kind = Parser::Token_EOF;

    do
    {
        kind = lexer.nextTokenKind();
        if ( !kind ) // when the lexer returns 0, the end of file is reached
        {
            //Parser::Token &tt = tokenStream->next();
            //tt.kind = Parser::Token_LINEBREAK;
            //tt.begin = lexer.tokenBegin();
            //tt.end = lexer.tokenEnd();
            kind = Parser::Token_EOF;
        }
        Parser::Token &t = tokenStream->next();
        t.begin = lexer.tokenBegin();
        t.end = lexer.tokenEnd();
        t.kind = kind;
        if( mDebug )
            kDebug() << kind << tokenText(t.begin,t.end) << t.begin << t.end;
    }
    while ( kind != Parser::Token_EOF );

    yylex(); // produce the look ahead token
}


QString Parser::tokenText(qint64 begin, qint64 end)
{
    return mContents.mid(begin,end-begin+1);
}


void Parser::reportProblem( Parser::ProblemType type, const QString& message )
{
    if (type == Error)
            kDebug() << "** ERROR:" << message;
    else if (type == Warning)
        kDebug() << "** WARNING:" << message;
    else if (type == Info)
        kDebug() << "** Info:" << message;
}


// custom error recovery
void Parser::expectedToken(int /*expected*/, qint64 /*where*/, const QString& name)
{
    reportProblem( Parser::Error, QString("Expected token \"%1\"").arg(name));
}

void Parser::expectedSymbol(int /*expectedSymbol*/, const QString& name)
{
    qint64 line;
    qint64 col;
    qint64 index = tokenStream->index()-1;
    Token &token = tokenStream->token(index);
    kDebug() << "token starts at:" << token.begin;
    kDebug() << "index is:" << index;
    tokenStream->startPosition(index, &line, &col);
    QString tokenValue = tokenText(token.begin, token.end);
    reportProblem( Parser::Error,
                   QString("Expected symbol \"%1\" (current token: \"%2\" [%3] at line: %4 col: %5)")
                  .arg(name)
                  .arg(token.kind != 0 ? tokenValue : "EOF")
                  .arg(token.kind)
                  .arg(line)
                  .arg(col));
}

void Parser::setDebug( bool debug )
{
    mDebug = debug;
}



} // end of namespace cool

:]

-- kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on

