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
--   parser::javaCompatibilityMode _MCompatibilityMode;
--
--   struct parserState {
--   };
--   parserState _MState;
-- :]
-- parser::parserState *parser::copyCurrentState()
-- {
--     parserState *state = new parserState();
--     return state;
-- }
--
-- void parser::restoreState( parser::parserState *state )
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

    enum OperatorType {
        LeftShiftOp,
        RightShiftOp,
        PlusOp,
        MinusOp,
        StarOp,
        SlashOp,
        ModuloOp,
        DoubleSlashOp,
        BinaryPlusOp,
        BinaryMinusOp,
        BinaryTildeOp,
        PlusEqOp,
        MinusEqOp,
        StarEqOp,
        SlashEqOp,
        ModuloEqOp,
        AndEqOp,
        OrEqOp,
        TildeEqOp,
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
       LESSEQ ("lesseq"), UNEQUAL ("unequal"), OR ("or"), HAT ("hat"), ISEQUAL ("isequal"),
       TILDEEQ ("tildeeq"), OREQ ("oreq"), ANDD ("andd") , ORR ("orr");;


-- token that makes the parser fail in any case:
%token INVALID ("invalid token") ;;

-- The actual grammar starts here.

   ( #stmt = stmt )*
-> project ;;

   AT decoratorName = dottedName ( LPAREN ( arguments=arglist | 0) RPAREN | 0 ) LINEBREAK
-> decorator ;;

   (#decorator = decorator )*
-> decorators ;;

-- Function Definition: Can start with Decorators.
-- varargslist defines the Function Variable Arguements
   ( decorators = decorators | 0 )
    DEF funcName=IDENTIFIER LPAREN ( ?[: LA(1).kind != Token_RPAREN :] ( funArgs = varargslist )
    | 0 )
    RPAREN COLON funSuite=suite
-> funcdef ;;

-- Function variable Arguement List
    (funcDef=funcDef | 0 ) (
    ?[: yytoken != Token_RPAREN  && LA(2).kind == Token_IDENTIFIER:] (funPosParam = funPosParam )
    | 0
    )
-> varargslist ;;

-- The Vararguement trailer, defines *args and **args
    ( STAR starId=IDENTIFIER ( COMMA DOUBLESTAR doubleStarId=IDENTIFIER | 0 )
        | DOUBLESTAR doubleStarId=IDENTIFIER )
-> funPosParam;;

-- Function Definition
    #fpDef=fpDef ( COMMA [:if(yytoken == Token_RPAREN  || yytoken == Token_STAR || yytoken == Token_DOUBLESTAR ) { break; } :] #fpDef=fpDef )*
-> funcDef ;;


-- Function parameter Defintion
    fpdef=fpdef ( EQUAL fpDefTest=test | 0 )
-> fpDef ;;

-- Function Parameter Definition
   LPAREN (fplist = fplist) RPAREN
    |  IDENTIFIER
-> fpdef ;;


-- Function parameter List
    #fplistFpdef=fpdef
    ( COMMA [: if ( yytoken == Token_RPAREN )
                  { break; } :]
            #fplistFpdef=fpdef )*
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

   (testlist = testlist) ( augassign = augassign anugassignTestlist = testlist
    | ( EQUAL #equalTestlist = testlist )+
    | ?[: yytoken == Token_SEMICOLON || yytoken == Token_LINEBREAK :] 0 )
-> exprStmt ;;

   PLUSEQ           [: (*yynode)->assignOp = Python::PlusEqOp;   :]
   | MINUSEQ        [: (*yynode)->assignOp = Python::MinusEqOp;  :]
   | STAREQ         [: (*yynode)->assignOp = Python::StarEqOp;   :]
   | SLASHEQ        [: (*yynode)->assignOp = Python::SlashEqOp;  :]
   | MODULOEQ       [: (*yynode)->assignOp = Python::ModuloEqOp; :]
   | ANDEQ          [: (*yynode)->assignOp = Python::AndEqOp;    :]
   | OREQ           [: (*yynode)->assignOp = Python::OrEqOp;     :]
   | TILDEEQ        [: (*yynode)->assignOp = Python::TildeEqOp;  :]
   | LSHIFTEQ       [: (*yynode)->assignOp = Python::LeftShiftEqOp; :]
   | RSHIFTEQ       [: (*yynode)->assignOp = Python::RightShiftEqOp; :]
   | DOUBLESTAREQ   [: (*yynode)->assignOp = Python::DoublestarEqOp; :]
   | DOUBLESLASHEQ  [: (*yynode)->assignOp = Python::DoubleslashEqOp;:]
-> augassign [
    member variable assignOp : Python::OperatorType; ];;

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

   YIELD yieldExpr=testlist
-> yieldStmt ;;

   RAISE ( type=test ( COMMA value=test ( COMMA traceback=test | 0 ) | 0 ) | 0 )
-> raiseStmt ;;

   importImport=importName
    | importFrom=importFrom
-> importStmt ;;

   IMPORT importName=dottedAsNames
-> importName ;;

   FROM importFromName=dottedName IMPORT ( STAR | LPAREN importAsNames=importAsNames RPAREN | importFromAsName=importAsNames )
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

   dottedName=IDENTIFIER ( DOT dottedName=IDENTIFIER )*
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
   | fucdef=funcdef
   | classdef=classdef
-> compoundStmt ;;

   IF #ifTest=test COLON ifSuite=suite ( ELIF #elifTest=test COLON #elifSuite=suite )* ( ELSE COLON ifElseSuite=suite | 0 )
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

   LESS         [: (*yynode)->compOp = Python::LessOp;      :]
   | GREATER    [: (*yynode)->compOp = Python::GreaterOp;   :]
   | ISEQUAL    [: (*yynode)->compOp = Python::IsEqualOp;   :]
   | GREATEREQ  [: (*yynode)->compOp = Python::GreaterEqOp; :]
   | LESSEQ     [: (*yynode)->compOp = Python::LessEqOp;    :]
   | UNEQUAL    [: (*yynode)->compOp = Python::UnEqualOp;   :]
   | IN         [: (*yynode)->compOp = Python::InOp;        :]
   | NOT IN     [: (*yynode)->compOp = Python::NotInOp;    :]
   | IS (NOT    [: (*yynode)->compOp = Python::IsNotOp;    :]
        | 0     [: (*yynode)->compOp = Python::IsOp;        :]
    )
-> compOp [
        member variable compOp : Python::OperatorType; ];;

   expr=xorExpr ( ORR #orrExpr=xorExpr )*
-> expr ;;

   xorExpr=andExpr ( HAT #hatXorExpr=andExpr )*
-> xorExpr ;;

   andExpr=shiftExpr ( ANDD #anddShifExpr=shiftExpr )*
-> andExpr ;;

   arithExpr=arithExpr
    ( #shiftOpList=shiftOp #arithExprList=arithExpr )*
-> shiftExpr ;;

    LSHIFT      [: (*yynode)->shiftOp = Python::LeftShiftOp;   :]
    | RSHIFT    [: (*yynode)->shiftOp = Python::RightShiftOp;   :]
-> shiftOp [
    member variable shiftOp : Python::OperatorType; ];;

   arithTerm=term
    ((#arithOpList = arithOp #arithTermList=term )+ | 0)
-> arithExpr ;;

    PLUS        [: (*yynode)->arithOp = Python::PlusOp;     :]
    | MINUS     [: (*yynode)->arithOp = Python::MinusOp;    :]
-> arithOp [
    member variable arithOp: Python::OperatorType; ] ;;

   factor=factor
    ((#termOpList = termOp #factorList=factor )+ | 0)
-> term ;;

    STAR        [: (*yynode)->termOp = Python::StarOp;      :]
    | SLASH     [: (*yynode)->termOp = Python::SlashOp;     :]
    | MODULO    [: (*yynode)->termOp = Python::ModuloOp;    :]
    | DOUBLESLASH [: (*yynode)->termOp = Python::DoubleSlashOp; :]
-> termOp [
    member variable termOp : Python::OperatorType; ];;

   ( factOp=factOp) factor=factor | power=power
-> factor ;;

    PLUS        [: (*yynode)->facOp = Python::BinaryPlusOp;     :]
    | MINUS     [: (*yynode)->facOp = Python::BinaryMinusOp;    :]
    | TILDE     [: (*yynode)->facOp = Python::BinaryTildeOp ;   :]
-> factOp [
    member variable facOp : Python::OperatorType;   ];;

   ( atom=atom )
    (#trailer=trailer)* ( DOUBLESTAR factor=factor | 0 )
-> power ;;

   LPAREN ( testlistGexp=testlistGexp | 0 ) RPAREN
   | LBRACKET listmaker=listmaker RBRACKET
   | LBRACE dictmaker=dictmaker RBRACE
   | BACKTICK testlist1=testlist1 BACKTICK
   | atomIdentifierName=IDENTIFIER
   | number=number
   | (#stringliteral=STRINGLITERAL)+
-> atom ;;


   INTEGER      [: (*yynode)->numType = Python::IntegerNumeric;      :]
   | FLOAT      [: (*yynode)->numType = Python::FloatNumeric;    :]
   | IMAGNUM    [: (*yynode)->numType = Python::ImaginaryNumeric;  :]
-> number [
    member variable numType: Python::NumericType; ];;

   ( #listTest=test ( COMMA [: if (yytoken == Token_RBRACKET) { break; } :] #listTest=test )* | 0)
-> listMaker ;;

    listMaker=listMaker (listFor=listFor | 0)
-> listmaker ;;

   #test=test ( COMMA [: if( yytoken == Token_COLON || yytoken == Token_SEMICOLON || yytoken == Token_RPAREN || yytoken == Token_LINEBREAK) { break; } :] #test=test )*
-> testListGexp ;;

    testListGexp=testListGexp ( genFor=genFor | 0 )
-> testlistGexp ;;

   LAMBDA ( lambdaVarargslist=varargslist | 0 ) COLON lambdaTest=test
-> lambdaDef ;;

   LPAREN ( trailerArglist=arglist | 0 ) RPAREN | LBRACKET subscriptlist=subscriptlist RBRACKET | DOT tarilerDotName=IDENTIFIER
-> trailer ;;

   #subscript=subscript ( COMMA [: if (yytoken == Token_RBRACKET) { break; } :]
    #subscript=subscript )*
-> subscriptlist ;;

-- Sub Scripts Check if the curent token is not a COLON it should be a test
-- If a COLON it skips the 'test'. if the next token is not RBRACKET or COMMA after test it can be a COLON.
-- Else it ends.
   subcriptEllipsis=ELLIPSIS
    | ( ?[: yytoken != Token_COLON :] subTest=test | 0 )
    ( ?[: yytoken == Token_RBRACKET || yytoken == Token_COMMA :] 0
        | COLON ( subColonTest=test | 0 ) ( sliceop=sliceop | 0 ) )
-> subscript ;;

   COLON ( sliceTest=test | 0 )
-> sliceop ;;

   #expr=expr
    ( COMMA [: if (yytoken == Token_IN || yytoken == Token_SEMICOLON || yytoken == Token_LINEBREAK ) { break; } :]
    #exprlist=expr )*
-> exprlist ;;

   #test=test ( COMMA [: if( yytoken == Token_COLON || yytoken == Token_SEMICOLON || yytoken == Token_RPAREN || yytoken == Token_LINEBREAK) {break;} :]
    #testlist=test )*
-> testlist ;;

   #test=test ( ( COMMA #test=test )+ ( COMMA | 0 ) | 0 )
-> testlistSafe ;;

   (#keyList=test COLON #valueList=test | 0) ( COMMA [: if (yytoken == Token_RBRACE) { break; } :]
    #keyList=test COLON #valueList=test )*
-> dictmaker ;;

   CLASS className=IDENTIFIER ( ( LPAREN testlist=testlist RPAREN ) | 0 ) COLON classSuite=suite
-> classdef ;;

   #argument=argument
    ( COMMA [: if(yytoken == Token_RPAREN || yytoken == Token_STAR || yytoken == Token_DOUBLESTAR) { break; } :] #argument=argument)*
-> argList ;;

    (argList=argList | 0)
    (
        ( STAR arglistStar=test (?[: LA(1).kind != Token_RPAREN :] COMMA DOUBLESTAR arglistDoublestar=test | 0)
        | DOUBLESTAR arglistDoublestar=test)
    | 0 )
-> arglist ;;

   argumentTest=test ( EQUAL argumentEqualTest=test ( ?[: LA(2).kind == Token_FOR :] LPAREN genFor=genFor RPAREN | 0 )
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
-> testlist1 ;;

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
            Parser::Token &tt = tokenStream->next();
            tt.kind = Parser::Token_LINEBREAK;
            tt.begin = lexer.tokenBegin();
            tt.end = lexer.tokenEnd();
            kind = Parser::Token_EOF;
        }
        Parser::Token &t = tokenStream->next();
        t.begin = lexer.tokenBegin();
        t.end = lexer.tokenEnd();
        t.kind = kind;
        if( mDebug )
            qDebug() << kind << tokenText(t.begin,t.end) << t.begin << t.end;
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
            qDebug() << "** ERROR:" << message;
    else if (type == Warning)
        qDebug() << "** WARNING:" << message;
    else if (type == Info)
        qDebug() << "** Info:" << message;
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
    qDebug() << "token starts at:" << token.begin;
    qDebug() << "index is:" << index;
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

