// THIS FILE IS GENERATED
// WARNING! All changes made in this file will be lost!

#include "pythonparser.h"


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
        if ( mDebug )
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


namespace PythonParser
{

bool Parser::parseAndExpr(AndExprAst **yynode)
{
    *yynode = create<AndExprAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_LBRACE
        || yytoken == Token_STRINGLITERAL
        || yytoken == Token_FLOAT
        || yytoken == Token_TILDE
        || yytoken == Token_BACKTICK
        || yytoken == Token_LBRACKET
        || yytoken == Token_INTEGER
        || yytoken == Token_MINUS
        || yytoken == Token_LPAREN
        || yytoken == Token_IDENTIFIER
        || yytoken == Token_PLUS
        || yytoken == Token_IMAGNUM)
    {
        ShiftExprAst *__node_0 = 0;
        if (!parseShiftExpr(&__node_0))
        {
            expectedSymbol(AstNode::ShiftExprKind, "shiftExpr");
            return false;
        }
        (*yynode)->andExpr = __node_0;

        while (yytoken == Token_BITAND)
        {
            if (yytoken != Token_BITAND)
            {
                expectedToken(yytoken, Token_BITAND, "bitand");
                return false;
            }
            yylex();

            ShiftExprAst *__node_1 = 0;
            if (!parseShiftExpr(&__node_1))
            {
                expectedSymbol(AstNode::ShiftExprKind, "shiftExpr");
                return false;
            }
            (*yynode)->anddShifExprSequence = snoc((*yynode)->anddShifExprSequence, __node_1, memoryPool);

        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseAndTest(AndTestAst **yynode)
{
    *yynode = create<AndTestAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_NOT
        || yytoken == Token_LBRACE
        || yytoken == Token_STRINGLITERAL
        || yytoken == Token_FLOAT
        || yytoken == Token_TILDE
        || yytoken == Token_BACKTICK
        || yytoken == Token_LBRACKET
        || yytoken == Token_INTEGER
        || yytoken == Token_MINUS
        || yytoken == Token_LPAREN
        || yytoken == Token_IDENTIFIER
        || yytoken == Token_PLUS
        || yytoken == Token_IMAGNUM)
    {
        NotTestAst *__node_2 = 0;
        if (!parseNotTest(&__node_2))
        {
            expectedSymbol(AstNode::NotTestKind, "notTest");
            return false;
        }
        (*yynode)->notTestSequence = snoc((*yynode)->notTestSequence, __node_2, memoryPool);

        while (yytoken == Token_AND)
        {
            if (yytoken != Token_AND)
            {
                expectedToken(yytoken, Token_AND, "and");
                return false;
            }
            yylex();

            NotTestAst *__node_3 = 0;
            if (!parseNotTest(&__node_3))
            {
                expectedSymbol(AstNode::NotTestKind, "notTest");
                return false;
            }
            (*yynode)->notTestSequence = snoc((*yynode)->notTestSequence, __node_3, memoryPool);

        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseArglist(ArglistAst **yynode)
{
    *yynode = create<ArglistAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_FLOAT
        || yytoken == Token_STRINGLITERAL
        || yytoken == Token_MINUS
        || yytoken == Token_DOUBLESTAR
        || yytoken == Token_BACKTICK
        || yytoken == Token_LBRACE
        || yytoken == Token_IMAGNUM
        || yytoken == Token_IDENTIFIER
        || yytoken == Token_TILDE
        || yytoken == Token_NOT
        || yytoken == Token_LPAREN
        || yytoken == Token_INTEGER
        || yytoken == Token_PLUS
        || yytoken == Token_STAR
        || yytoken == Token_LAMBDA
        || yytoken == Token_LBRACKET || yytoken == Token_EOF
        || yytoken == Token_RPAREN)
    {
        if (yytoken == Token_NOT
            || yytoken == Token_LBRACE
            || yytoken == Token_STRINGLITERAL
            || yytoken == Token_FLOAT
            || yytoken == Token_TILDE
            || yytoken == Token_BACKTICK
            || yytoken == Token_LAMBDA
            || yytoken == Token_LBRACKET
            || yytoken == Token_INTEGER
            || yytoken == Token_MINUS
            || yytoken == Token_LPAREN
            || yytoken == Token_IDENTIFIER
            || yytoken == Token_PLUS
            || yytoken == Token_IMAGNUM)
        {
            PlainArgumentsListAst *__node_4 = 0;
            if (!parsePlainArgumentsList(&__node_4))
            {
                expectedSymbol(AstNode::PlainArgumentsListKind, "plainArgumentsList");
                return false;
            }
            (*yynode)->argListBegin = __node_4;

        }
        else if (true /*epsilon*/)
        {
        }
        else
        {
            return false;
        }
        if (yytoken == Token_STAR)
        {
            if (yytoken != Token_STAR)
            {
                expectedToken(yytoken, Token_STAR, "star");
                return false;
            }
            yylex();

            TestAst *__node_5 = 0;
            if (!parseTest(&__node_5))
            {
                expectedSymbol(AstNode::TestKind, "test");
                return false;
            }
            (*yynode)->arglistStar = __node_5;

            if ((yytoken == Token_COMMA) && ( LA(1).kind != Token_RPAREN ))
            {
                if (yytoken != Token_COMMA)
                {
                    expectedToken(yytoken, Token_COMMA, "comma");
                    return false;
                }
                yylex();

                if (yytoken != Token_DOUBLESTAR)
                {
                    expectedToken(yytoken, Token_DOUBLESTAR, "doublestar");
                    return false;
                }
                yylex();

                TestAst *__node_6 = 0;
                if (!parseTest(&__node_6))
                {
                    expectedSymbol(AstNode::TestKind, "test");
                    return false;
                }
                (*yynode)->arglistDoublestar = __node_6;

            }
            else if (true /*epsilon*/)
            {
            }
            else
            {
                return false;
            }
        }
        else if (yytoken == Token_DOUBLESTAR)
        {
            if (yytoken != Token_DOUBLESTAR)
            {
                expectedToken(yytoken, Token_DOUBLESTAR, "doublestar");
                return false;
            }
            yylex();

            TestAst *__node_7 = 0;
            if (!parseTest(&__node_7))
            {
                expectedSymbol(AstNode::TestKind, "test");
                return false;
            }
            (*yynode)->arglistDoublestar = __node_7;

        }
        else if (true /*epsilon*/)
        {
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseArgument(ArgumentAst **yynode)
{
    *yynode = create<ArgumentAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_NOT
        || yytoken == Token_LBRACE
        || yytoken == Token_STRINGLITERAL
        || yytoken == Token_FLOAT
        || yytoken == Token_TILDE
        || yytoken == Token_BACKTICK
        || yytoken == Token_LAMBDA
        || yytoken == Token_LBRACKET
        || yytoken == Token_INTEGER
        || yytoken == Token_MINUS
        || yytoken == Token_LPAREN
        || yytoken == Token_IDENTIFIER
        || yytoken == Token_PLUS
        || yytoken == Token_IMAGNUM)
    {
        TestAst *__node_8 = 0;
        if (!parseTest(&__node_8))
        {
            expectedSymbol(AstNode::TestKind, "test");
            return false;
        }
        (*yynode)->argumentTest = __node_8;

        if (yytoken == Token_EQUAL)
        {
            if (yytoken != Token_EQUAL)
            {
                expectedToken(yytoken, Token_EQUAL, "equal");
                return false;
            }
            yylex();

            TestAst *__node_9 = 0;
            if (!parseTest(&__node_9))
            {
                expectedSymbol(AstNode::TestKind, "test");
                return false;
            }
            (*yynode)->argumentEqualTest = __node_9;

        }
        else if ((yytoken == Token_FOR) && ( yytoken == Token_FOR ))
        {
            GenForAst *__node_10 = 0;
            if (!parseGenFor(&__node_10))
            {
                expectedSymbol(AstNode::GenForKind, "genFor");
                return false;
            }
            (*yynode)->genFor = __node_10;

        }
        else if ((true /*epsilon*/) && ( yytoken == Token_RPAREN || yytoken == Token_STAR || yytoken == Token_DOUBLESTAR || yytoken == Token_COMMA ))
        {
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseArithExpr(ArithExprAst **yynode)
{
    *yynode = create<ArithExprAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_LBRACE
        || yytoken == Token_STRINGLITERAL
        || yytoken == Token_FLOAT
        || yytoken == Token_TILDE
        || yytoken == Token_BACKTICK
        || yytoken == Token_LBRACKET
        || yytoken == Token_INTEGER
        || yytoken == Token_MINUS
        || yytoken == Token_LPAREN
        || yytoken == Token_IDENTIFIER
        || yytoken == Token_PLUS
        || yytoken == Token_IMAGNUM)
    {
        TermAst *__node_11 = 0;
        if (!parseTerm(&__node_11))
        {
            expectedSymbol(AstNode::TermKind, "term");
            return false;
        }
        (*yynode)->arithTerm = __node_11;

        if (yytoken == Token_MINUS
            || yytoken == Token_PLUS)
        {
            do
            {
                ArithOpAst *__node_12 = 0;
                if (!parseArithOp(&__node_12))
                {
                    expectedSymbol(AstNode::ArithOpKind, "arithOp");
                    return false;
                }
                (*yynode)->arithOpListSequence = snoc((*yynode)->arithOpListSequence, __node_12, memoryPool);

                TermAst *__node_13 = 0;
                if (!parseTerm(&__node_13))
                {
                    expectedSymbol(AstNode::TermKind, "term");
                    return false;
                }
                (*yynode)->arithTermListSequence = snoc((*yynode)->arithTermListSequence, __node_13, memoryPool);

            }
            while (yytoken == Token_MINUS
                   || yytoken == Token_PLUS);
        }
        else if (true /*epsilon*/)
        {
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseArithOp(ArithOpAst **yynode)
{
    *yynode = create<ArithOpAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_MINUS
        || yytoken == Token_PLUS)
    {
        if (yytoken == Token_PLUS)
        {
            if (yytoken != Token_PLUS)
            {
                expectedToken(yytoken, Token_PLUS, "plus");
                return false;
            }
            yylex();

            (*yynode)->arithOp = PythonParser::PlusOp;
        }
        else if (yytoken == Token_MINUS)
        {
            if (yytoken != Token_MINUS)
            {
                expectedToken(yytoken, Token_MINUS, "minus");
                return false;
            }
            yylex();

            (*yynode)->arithOp = PythonParser::MinusOp;
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseAssertStmt(AssertStmtAst **yynode)
{
    *yynode = create<AssertStmtAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_ASSERT)
    {
        if (yytoken != Token_ASSERT)
        {
            expectedToken(yytoken, Token_ASSERT, "assert");
            return false;
        }
        yylex();

        TestAst *__node_14 = 0;
        if (!parseTest(&__node_14))
        {
            expectedSymbol(AstNode::TestKind, "test");
            return false;
        }
        (*yynode)->assertNotTest = __node_14;

        if (yytoken == Token_COMMA)
        {
            if (yytoken != Token_COMMA)
            {
                expectedToken(yytoken, Token_COMMA, "comma");
                return false;
            }
            yylex();

            TestAst *__node_15 = 0;
            if (!parseTest(&__node_15))
            {
                expectedSymbol(AstNode::TestKind, "test");
                return false;
            }
            (*yynode)->assertRaiseTest = __node_15;

        }
        else if (true /*epsilon*/)
        {
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseAtom(AtomAst **yynode)
{
    *yynode = create<AtomAst>();

    (*yynode)->startToken = tokenStream->index() - 1;
    (*yynode)->atomIdentifierName = -1;

    if (yytoken == Token_LBRACE
        || yytoken == Token_STRINGLITERAL
        || yytoken == Token_FLOAT
        || yytoken == Token_BACKTICK
        || yytoken == Token_LBRACKET
        || yytoken == Token_INTEGER
        || yytoken == Token_LPAREN
        || yytoken == Token_IDENTIFIER
        || yytoken == Token_IMAGNUM)
    {
        if (yytoken == Token_LPAREN)
        {
            if (yytoken != Token_LPAREN)
            {
                expectedToken(yytoken, Token_LPAREN, "lparen");
                return false;
            }
            yylex();

            if (yytoken == Token_YIELD)
            {
                YieldExprAst *__node_16 = 0;
                if (!parseYieldExpr(&__node_16))
                {
                    expectedSymbol(AstNode::YieldExprKind, "yieldExpr");
                    return false;
                }
                (*yynode)->yield = __node_16;

            }
            else if (yytoken == Token_NOT
                     || yytoken == Token_LBRACE
                     || yytoken == Token_STRINGLITERAL
                     || yytoken == Token_FLOAT
                     || yytoken == Token_TILDE
                     || yytoken == Token_BACKTICK
                     || yytoken == Token_LAMBDA
                     || yytoken == Token_LBRACKET
                     || yytoken == Token_INTEGER
                     || yytoken == Token_MINUS
                     || yytoken == Token_LPAREN
                     || yytoken == Token_IDENTIFIER
                     || yytoken == Token_PLUS
                     || yytoken == Token_IMAGNUM)
            {
                TestlistAst *__node_17 = 0;
                if (!parseTestlist(&__node_17))
                {
                    expectedSymbol(AstNode::TestlistKind, "testlist");
                    return false;
                }
                (*yynode)->testlist = __node_17;

                if (yytoken == Token_FOR)
                {
                    GenForAst *__node_18 = 0;
                    if (!parseGenFor(&__node_18))
                    {
                        expectedSymbol(AstNode::GenForKind, "genFor");
                        return false;
                    }
                    (*yynode)->genFor = __node_18;

                }
                else if (true /*epsilon*/)
                {
                }
                else
                {
                    return false;
                }
            }
            else if (true /*epsilon*/)
            {
            }
            else
            {
                return false;
            }
            if (yytoken != Token_RPAREN)
            {
                expectedToken(yytoken, Token_RPAREN, "rparen");
                return false;
            }
            yylex();

        }
        else if (yytoken == Token_LBRACKET)
        {
            if (yytoken != Token_LBRACKET)
            {
                expectedToken(yytoken, Token_LBRACKET, "lbracket");
                return false;
            }
            yylex();

            ListmakerAst *__node_19 = 0;
            if (!parseListmaker(&__node_19))
            {
                expectedSymbol(AstNode::ListmakerKind, "listmaker");
                return false;
            }
            (*yynode)->listmaker = __node_19;

            if (yytoken != Token_RBRACKET)
            {
                expectedToken(yytoken, Token_RBRACKET, "rbracket");
                return false;
            }
            yylex();

        }
        else if (yytoken == Token_LBRACE)
        {
            if (yytoken != Token_LBRACE)
            {
                expectedToken(yytoken, Token_LBRACE, "lbrace");
                return false;
            }
            yylex();

            DictmakerAst *__node_20 = 0;
            if (!parseDictmaker(&__node_20))
            {
                expectedSymbol(AstNode::DictmakerKind, "dictmaker");
                return false;
            }
            (*yynode)->dictmaker = __node_20;

            if (yytoken != Token_RBRACE)
            {
                expectedToken(yytoken, Token_RBRACE, "rbrace");
                return false;
            }
            yylex();

        }
        else if (yytoken == Token_BACKTICK)
        {
            if (yytoken != Token_BACKTICK)
            {
                expectedToken(yytoken, Token_BACKTICK, "backtick");
                return false;
            }
            yylex();

            CodeexprAst *__node_21 = 0;
            if (!parseCodeexpr(&__node_21))
            {
                expectedSymbol(AstNode::CodeexprKind, "codeexpr");
                return false;
            }
            (*yynode)->codeexpr = __node_21;

            if (yytoken != Token_BACKTICK)
            {
                expectedToken(yytoken, Token_BACKTICK, "backtick");
                return false;
            }
            yylex();

        }
        else if (yytoken == Token_IDENTIFIER)
        {
            if (yytoken != Token_IDENTIFIER)
            {
                expectedToken(yytoken, Token_IDENTIFIER, "identifier");
                return false;
            }
            (*yynode)->atomIdentifierName = tokenStream->index() - 1;
            yylex();

        }
        else if (yytoken == Token_FLOAT
                 || yytoken == Token_INTEGER
                 || yytoken == Token_IMAGNUM)
        {
            NumberAst *__node_22 = 0;
            if (!parseNumber(&__node_22))
            {
                expectedSymbol(AstNode::NumberKind, "number");
                return false;
            }
            (*yynode)->number = __node_22;

        }
        else if (yytoken == Token_STRINGLITERAL)
        {
            do
            {
                if (yytoken != Token_STRINGLITERAL)
                {
                    expectedToken(yytoken, Token_STRINGLITERAL, "stringliteral");
                    return false;
                }
                (*yynode)->stringliteralSequence = snoc((*yynode)->stringliteralSequence, tokenStream->index() - 1, memoryPool);
                yylex();

            }
            while (yytoken == Token_STRINGLITERAL);
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseAugassign(AugassignAst **yynode)
{
    *yynode = create<AugassignAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_SLASHEQ
        || yytoken == Token_ANDEQ
        || yytoken == Token_LSHIFTEQ
        || yytoken == Token_MINUSEQ
        || yytoken == Token_OREQ
        || yytoken == Token_MODULOEQ
        || yytoken == Token_DOUBLESTAREQ
        || yytoken == Token_PLUSEQ
        || yytoken == Token_TILDEEQ
        || yytoken == Token_DOUBLESLASHEQ
        || yytoken == Token_STAREQ
        || yytoken == Token_RSHIFTEQ)
    {
        if (yytoken == Token_PLUSEQ)
        {
            if (yytoken != Token_PLUSEQ)
            {
                expectedToken(yytoken, Token_PLUSEQ, "pluseq");
                return false;
            }
            yylex();

            (*yynode)->assignOp = PythonParser::PlusEqOp;
        }
        else if (yytoken == Token_MINUSEQ)
        {
            if (yytoken != Token_MINUSEQ)
            {
                expectedToken(yytoken, Token_MINUSEQ, "minuseq");
                return false;
            }
            yylex();

            (*yynode)->assignOp = PythonParser::MinusEqOp;
        }
        else if (yytoken == Token_STAREQ)
        {
            if (yytoken != Token_STAREQ)
            {
                expectedToken(yytoken, Token_STAREQ, "stareq");
                return false;
            }
            yylex();

            (*yynode)->assignOp = PythonParser::StarEqOp;
        }
        else if (yytoken == Token_SLASHEQ)
        {
            if (yytoken != Token_SLASHEQ)
            {
                expectedToken(yytoken, Token_SLASHEQ, "slasheq");
                return false;
            }
            yylex();

            (*yynode)->assignOp = PythonParser::SlashEqOp;
        }
        else if (yytoken == Token_MODULOEQ)
        {
            if (yytoken != Token_MODULOEQ)
            {
                expectedToken(yytoken, Token_MODULOEQ, "moduloeq");
                return false;
            }
            yylex();

            (*yynode)->assignOp = PythonParser::ModuloEqOp;
        }
        else if (yytoken == Token_ANDEQ)
        {
            if (yytoken != Token_ANDEQ)
            {
                expectedToken(yytoken, Token_ANDEQ, "andeq");
                return false;
            }
            yylex();

            (*yynode)->assignOp = PythonParser::AndEqOp;
        }
        else if (yytoken == Token_OREQ)
        {
            if (yytoken != Token_OREQ)
            {
                expectedToken(yytoken, Token_OREQ, "oreq");
                return false;
            }
            yylex();

            (*yynode)->assignOp = PythonParser::OrEqOp;
        }
        else if (yytoken == Token_TILDEEQ)
        {
            if (yytoken != Token_TILDEEQ)
            {
                expectedToken(yytoken, Token_TILDEEQ, "tildeeq");
                return false;
            }
            yylex();

            (*yynode)->assignOp = PythonParser::HatEqOp;
        }
        else if (yytoken == Token_LSHIFTEQ)
        {
            if (yytoken != Token_LSHIFTEQ)
            {
                expectedToken(yytoken, Token_LSHIFTEQ, "lshifteq");
                return false;
            }
            yylex();

            (*yynode)->assignOp = PythonParser::LeftShiftEqOp;
        }
        else if (yytoken == Token_RSHIFTEQ)
        {
            if (yytoken != Token_RSHIFTEQ)
            {
                expectedToken(yytoken, Token_RSHIFTEQ, "rshifteq");
                return false;
            }
            yylex();

            (*yynode)->assignOp = PythonParser::RightShiftEqOp;
        }
        else if (yytoken == Token_DOUBLESTAREQ)
        {
            if (yytoken != Token_DOUBLESTAREQ)
            {
                expectedToken(yytoken, Token_DOUBLESTAREQ, "doublestareq");
                return false;
            }
            yylex();

            (*yynode)->assignOp = PythonParser::DoublestarEqOp;
        }
        else if (yytoken == Token_DOUBLESLASHEQ)
        {
            if (yytoken != Token_DOUBLESLASHEQ)
            {
                expectedToken(yytoken, Token_DOUBLESLASHEQ, "doubleslasheq");
                return false;
            }
            yylex();

            (*yynode)->assignOp = PythonParser::DoubleslashEqOp;
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseBreakStmt(BreakStmtAst **yynode)
{
    *yynode = create<BreakStmtAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_BREAK)
    {
        if (yytoken != Token_BREAK)
        {
            expectedToken(yytoken, Token_BREAK, "break");
            return false;
        }
        yylex();

    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseClassdef(ClassdefAst **yynode)
{
    *yynode = create<ClassdefAst>();

    (*yynode)->startToken = tokenStream->index() - 1;
    (*yynode)->className = -1;

    if (yytoken == Token_CLASS)
    {
        if (yytoken != Token_CLASS)
        {
            expectedToken(yytoken, Token_CLASS, "class");
            return false;
        }
        yylex();

        if (yytoken != Token_IDENTIFIER)
        {
            expectedToken(yytoken, Token_IDENTIFIER, "identifier");
            return false;
        }
        (*yynode)->className = tokenStream->index() - 1;
        yylex();

        if (yytoken == Token_LPAREN)
        {
            if (yytoken != Token_LPAREN)
            {
                expectedToken(yytoken, Token_LPAREN, "lparen");
                return false;
            }
            yylex();

            TestlistAst *__node_23 = 0;
            if (!parseTestlist(&__node_23))
            {
                expectedSymbol(AstNode::TestlistKind, "testlist");
                return false;
            }
            (*yynode)->testlist = __node_23;

            if (yytoken != Token_RPAREN)
            {
                expectedToken(yytoken, Token_RPAREN, "rparen");
                return false;
            }
            yylex();

        }
        else if (true /*epsilon*/)
        {
        }
        else
        {
            return false;
        }
        if (yytoken != Token_COLON)
        {
            expectedToken(yytoken, Token_COLON, "colon");
            return false;
        }
        yylex();

        SuiteAst *__node_24 = 0;
        if (!parseSuite(&__node_24))
        {
            expectedSymbol(AstNode::SuiteKind, "suite");
            return false;
        }
        (*yynode)->classSuite = __node_24;

    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseCodeexpr(CodeexprAst **yynode)
{
    *yynode = create<CodeexprAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_NOT
        || yytoken == Token_LBRACE
        || yytoken == Token_STRINGLITERAL
        || yytoken == Token_FLOAT
        || yytoken == Token_TILDE
        || yytoken == Token_BACKTICK
        || yytoken == Token_LAMBDA
        || yytoken == Token_LBRACKET
        || yytoken == Token_INTEGER
        || yytoken == Token_MINUS
        || yytoken == Token_LPAREN
        || yytoken == Token_IDENTIFIER
        || yytoken == Token_PLUS
        || yytoken == Token_IMAGNUM)
    {
        TestAst *__node_25 = 0;
        if (!parseTest(&__node_25))
        {
            expectedSymbol(AstNode::TestKind, "test");
            return false;
        }
        (*yynode)->testSequence = snoc((*yynode)->testSequence, __node_25, memoryPool);

        while (yytoken == Token_COMMA)
        {
            if (yytoken != Token_COMMA)
            {
                expectedToken(yytoken, Token_COMMA, "comma");
                return false;
            }
            yylex();

            TestAst *__node_26 = 0;
            if (!parseTest(&__node_26))
            {
                expectedSymbol(AstNode::TestKind, "test");
                return false;
            }
            (*yynode)->testSequence = snoc((*yynode)->testSequence, __node_26, memoryPool);

        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseCompOp(CompOpAst **yynode)
{
    *yynode = create<CompOpAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_NOT
        || yytoken == Token_GREATEREQ
        || yytoken == Token_IN
        || yytoken == Token_GREATER
        || yytoken == Token_UNEQUAL
        || yytoken == Token_LESS
        || yytoken == Token_LESSEQ
        || yytoken == Token_ISEQUAL
        || yytoken == Token_IS)
    {
        if (yytoken == Token_LESS)
        {
            if (yytoken != Token_LESS)
            {
                expectedToken(yytoken, Token_LESS, "less");
                return false;
            }
            yylex();

            (*yynode)->compOp = PythonParser::LessOp;
        }
        else if (yytoken == Token_GREATER)
        {
            if (yytoken != Token_GREATER)
            {
                expectedToken(yytoken, Token_GREATER, "greater");
                return false;
            }
            yylex();

            (*yynode)->compOp = PythonParser::GreaterOp;
        }
        else if (yytoken == Token_ISEQUAL)
        {
            if (yytoken != Token_ISEQUAL)
            {
                expectedToken(yytoken, Token_ISEQUAL, "isequal");
                return false;
            }
            yylex();

            (*yynode)->compOp = PythonParser::IsEqualOp;
        }
        else if (yytoken == Token_GREATEREQ)
        {
            if (yytoken != Token_GREATEREQ)
            {
                expectedToken(yytoken, Token_GREATEREQ, "greatereq");
                return false;
            }
            yylex();

            (*yynode)->compOp = PythonParser::GreaterEqOp;
        }
        else if (yytoken == Token_LESSEQ)
        {
            if (yytoken != Token_LESSEQ)
            {
                expectedToken(yytoken, Token_LESSEQ, "lesseq");
                return false;
            }
            yylex();

            (*yynode)->compOp = PythonParser::LessEqOp;
        }
        else if (yytoken == Token_UNEQUAL)
        {
            if (yytoken != Token_UNEQUAL)
            {
                expectedToken(yytoken, Token_UNEQUAL, "unequal");
                return false;
            }
            yylex();

            (*yynode)->compOp = PythonParser::UnEqualOp;
        }
        else if (yytoken == Token_IN)
        {
            if (yytoken != Token_IN)
            {
                expectedToken(yytoken, Token_IN, "in");
                return false;
            }
            yylex();

            (*yynode)->compOp = PythonParser::InOp;
        }
        else if (yytoken == Token_NOT)
        {
            if (yytoken != Token_NOT)
            {
                expectedToken(yytoken, Token_NOT, "not");
                return false;
            }
            yylex();

            if (yytoken != Token_IN)
            {
                expectedToken(yytoken, Token_IN, "in");
                return false;
            }
            yylex();

            (*yynode)->compOp = PythonParser::NotInOp;
        }
        else if (yytoken == Token_IS)
        {
            if (yytoken != Token_IS)
            {
                expectedToken(yytoken, Token_IS, "is");
                return false;
            }
            yylex();

            if (yytoken == Token_NOT)
            {
                if (yytoken != Token_NOT)
                {
                    expectedToken(yytoken, Token_NOT, "not");
                    return false;
                }
                yylex();

                (*yynode)->compOp = PythonParser::IsNotOp;
            }
            else if (true /*epsilon*/)
            {
                (*yynode)->compOp = PythonParser::IsOp;
            }
            else
            {
                return false;
            }
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseComparison(ComparisonAst **yynode)
{
    *yynode = create<ComparisonAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_LBRACE
        || yytoken == Token_STRINGLITERAL
        || yytoken == Token_FLOAT
        || yytoken == Token_TILDE
        || yytoken == Token_BACKTICK
        || yytoken == Token_LBRACKET
        || yytoken == Token_INTEGER
        || yytoken == Token_MINUS
        || yytoken == Token_LPAREN
        || yytoken == Token_IDENTIFIER
        || yytoken == Token_PLUS
        || yytoken == Token_IMAGNUM)
    {
        ExprAst *__node_27 = 0;
        if (!parseExpr(&__node_27))
        {
            expectedSymbol(AstNode::ExprKind, "expr");
            return false;
        }
        (*yynode)->compExpr = __node_27;

        while (yytoken == Token_NOT
               || yytoken == Token_GREATEREQ
               || yytoken == Token_IN
               || yytoken == Token_GREATER
               || yytoken == Token_UNEQUAL
               || yytoken == Token_LESS
               || yytoken == Token_LESSEQ
               || yytoken == Token_ISEQUAL
               || yytoken == Token_IS)
        {
            CompOpAst *__node_28 = 0;
            if (!parseCompOp(&__node_28))
            {
                expectedSymbol(AstNode::CompOpKind, "compOp");
                return false;
            }
            (*yynode)->compOpSequence = snoc((*yynode)->compOpSequence, __node_28, memoryPool);

            ExprAst *__node_29 = 0;
            if (!parseExpr(&__node_29))
            {
                expectedSymbol(AstNode::ExprKind, "expr");
                return false;
            }
            (*yynode)->compOpExprSequence = snoc((*yynode)->compOpExprSequence, __node_29, memoryPool);

        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseCompoundStmt(CompoundStmtAst **yynode)
{
    *yynode = create<CompoundStmtAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_WHILE
        || yytoken == Token_FOR
        || yytoken == Token_CLASS
        || yytoken == Token_DEF
        || yytoken == Token_AT
        || yytoken == Token_TRY
        || yytoken == Token_IF)
    {
        if (yytoken == Token_IF)
        {
            IfStmtAst *__node_30 = 0;
            if (!parseIfStmt(&__node_30))
            {
                expectedSymbol(AstNode::IfStmtKind, "ifStmt");
                return false;
            }
            (*yynode)->ifStmt = __node_30;

        }
        else if (yytoken == Token_WHILE)
        {
            WhileStmtAst *__node_31 = 0;
            if (!parseWhileStmt(&__node_31))
            {
                expectedSymbol(AstNode::WhileStmtKind, "whileStmt");
                return false;
            }
            (*yynode)->whileStmt = __node_31;

        }
        else if (yytoken == Token_FOR)
        {
            ForStmtAst *__node_32 = 0;
            if (!parseForStmt(&__node_32))
            {
                expectedSymbol(AstNode::ForStmtKind, "forStmt");
                return false;
            }
            (*yynode)->forStmt = __node_32;

        }
        else if (yytoken == Token_TRY)
        {
            TryStmtAst *__node_33 = 0;
            if (!parseTryStmt(&__node_33))
            {
                expectedSymbol(AstNode::TryStmtKind, "tryStmt");
                return false;
            }
            (*yynode)->tryStmt = __node_33;

        }
        else if (yytoken == Token_DEF
                 || yytoken == Token_AT)
        {
            FuncdeclAst *__node_34 = 0;
            if (!parseFuncdecl(&__node_34))
            {
                expectedSymbol(AstNode::FuncdeclKind, "funcdecl");
                return false;
            }
            (*yynode)->funcdecl = __node_34;

        }
        else if (yytoken == Token_CLASS)
        {
            ClassdefAst *__node_35 = 0;
            if (!parseClassdef(&__node_35))
            {
                expectedSymbol(AstNode::ClassdefKind, "classdef");
                return false;
            }
            (*yynode)->classdef = __node_35;

        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseContinueStmt(ContinueStmtAst **yynode)
{
    *yynode = create<ContinueStmtAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_CONTINUE)
    {
        if (yytoken != Token_CONTINUE)
        {
            expectedToken(yytoken, Token_CONTINUE, "continue");
            return false;
        }
        yylex();

    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseDecorator(DecoratorAst **yynode)
{
    *yynode = create<DecoratorAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_AT)
    {
        if (yytoken != Token_AT)
        {
            expectedToken(yytoken, Token_AT, "at");
            return false;
        }
        yylex();

        DottedNameAst *__node_36 = 0;
        if (!parseDottedName(&__node_36))
        {
            expectedSymbol(AstNode::DottedNameKind, "dottedName");
            return false;
        }
        (*yynode)->decoratorName = __node_36;

        if (yytoken == Token_LPAREN)
        {
            if (yytoken != Token_LPAREN)
            {
                expectedToken(yytoken, Token_LPAREN, "lparen");
                return false;
            }
            yylex();

            if (yytoken == Token_NOT
                || yytoken == Token_LBRACE
                || yytoken == Token_STRINGLITERAL
                || yytoken == Token_FLOAT
                || yytoken == Token_TILDE
                || yytoken == Token_BACKTICK
                || yytoken == Token_LAMBDA
                || yytoken == Token_LBRACKET
                || yytoken == Token_DOUBLESTAR
                || yytoken == Token_INTEGER
                || yytoken == Token_MINUS
                || yytoken == Token_LPAREN
                || yytoken == Token_STAR
                || yytoken == Token_IDENTIFIER
                || yytoken == Token_PLUS
                || yytoken == Token_IMAGNUM)
            {
                ArglistAst *__node_37 = 0;
                if (!parseArglist(&__node_37))
                {
                    expectedSymbol(AstNode::ArglistKind, "arglist");
                    return false;
                }
                (*yynode)->arguments = __node_37;

            }
            else if (true /*epsilon*/)
            {
            }
            else
            {
                return false;
            }
            if (yytoken != Token_RPAREN)
            {
                expectedToken(yytoken, Token_RPAREN, "rparen");
                return false;
            }
            yylex();

        }
        else if (true /*epsilon*/)
        {
        }
        else
        {
            return false;
        }
        if (yytoken != Token_LINEBREAK)
        {
            expectedToken(yytoken, Token_LINEBREAK, "linebreak");
            return false;
        }
        yylex();

    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseDecorators(DecoratorsAst **yynode)
{
    *yynode = create<DecoratorsAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_AT)
    {
        do
        {
            DecoratorAst *__node_38 = 0;
            if (!parseDecorator(&__node_38))
            {
                expectedSymbol(AstNode::DecoratorKind, "decorator");
                return false;
            }
            (*yynode)->decoratorSequence = snoc((*yynode)->decoratorSequence, __node_38, memoryPool);

        }
        while (yytoken == Token_AT);
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseDefparam(DefparamAst **yynode)
{
    *yynode = create<DefparamAst>();

    (*yynode)->startToken = tokenStream->index() - 1;
    (*yynode)->paramname = -1;

    if (yytoken == Token_LPAREN
        || yytoken == Token_IDENTIFIER)
    {
        if (yytoken == Token_LPAREN)
        {
            if (yytoken != Token_LPAREN)
            {
                expectedToken(yytoken, Token_LPAREN, "lparen");
                return false;
            }
            yylex();

            FplistAst *__node_39 = 0;
            if (!parseFplist(&__node_39))
            {
                expectedSymbol(AstNode::FplistKind, "fplist");
                return false;
            }
            (*yynode)->fplist = __node_39;

            if (yytoken != Token_RPAREN)
            {
                expectedToken(yytoken, Token_RPAREN, "rparen");
                return false;
            }
            yylex();

        }
        else if (yytoken == Token_IDENTIFIER)
        {
            if (yytoken != Token_IDENTIFIER)
            {
                expectedToken(yytoken, Token_IDENTIFIER, "identifier");
                return false;
            }
            (*yynode)->paramname = tokenStream->index() - 1;
            yylex();

        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseDelStmt(DelStmtAst **yynode)
{
    *yynode = create<DelStmtAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_DEL)
    {
        if (yytoken != Token_DEL)
        {
            expectedToken(yytoken, Token_DEL, "del");
            return false;
        }
        yylex();

        ExprlistAst *__node_40 = 0;
        if (!parseExprlist(&__node_40))
        {
            expectedSymbol(AstNode::ExprlistKind, "exprlist");
            return false;
        }
        (*yynode)->delList = __node_40;

    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseDictParam(DictParamAst **yynode)
{
    *yynode = create<DictParamAst>();

    (*yynode)->startToken = tokenStream->index() - 1;
    (*yynode)->doubleStarId = -1;

    if (yytoken == Token_DOUBLESTAR)
    {
        if (yytoken != Token_DOUBLESTAR)
        {
            expectedToken(yytoken, Token_DOUBLESTAR, "doublestar");
            return false;
        }
        yylex();

        if (yytoken != Token_IDENTIFIER)
        {
            expectedToken(yytoken, Token_IDENTIFIER, "identifier");
            return false;
        }
        (*yynode)->doubleStarId = tokenStream->index() - 1;
        yylex();

    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseDictmaker(DictmakerAst **yynode)
{
    *yynode = create<DictmakerAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_NOT
        || yytoken == Token_LBRACE
        || yytoken == Token_STRINGLITERAL
        || yytoken == Token_FLOAT
        || yytoken == Token_TILDE
        || yytoken == Token_BACKTICK
        || yytoken == Token_LAMBDA
        || yytoken == Token_LBRACKET
        || yytoken == Token_INTEGER
        || yytoken == Token_MINUS
        || yytoken == Token_LPAREN
        || yytoken == Token_IDENTIFIER
        || yytoken == Token_COMMA
        || yytoken == Token_PLUS
        || yytoken == Token_IMAGNUM || yytoken == Token_EOF
        || yytoken == Token_RBRACE)
    {
        if (yytoken == Token_NOT
            || yytoken == Token_LBRACE
            || yytoken == Token_STRINGLITERAL
            || yytoken == Token_FLOAT
            || yytoken == Token_TILDE
            || yytoken == Token_BACKTICK
            || yytoken == Token_LAMBDA
            || yytoken == Token_LBRACKET
            || yytoken == Token_INTEGER
            || yytoken == Token_MINUS
            || yytoken == Token_LPAREN
            || yytoken == Token_IDENTIFIER
            || yytoken == Token_PLUS
            || yytoken == Token_IMAGNUM)
        {
            TestAst *__node_41 = 0;
            if (!parseTest(&__node_41))
            {
                expectedSymbol(AstNode::TestKind, "test");
                return false;
            }
            (*yynode)->keyListSequence = snoc((*yynode)->keyListSequence, __node_41, memoryPool);

            if (yytoken != Token_COLON)
            {
                expectedToken(yytoken, Token_COLON, "colon");
                return false;
            }
            yylex();

            TestAst *__node_42 = 0;
            if (!parseTest(&__node_42))
            {
                expectedSymbol(AstNode::TestKind, "test");
                return false;
            }
            (*yynode)->valueListSequence = snoc((*yynode)->valueListSequence, __node_42, memoryPool);

        }
        else if (true /*epsilon*/)
        {
        }
        else
        {
            return false;
        }
        while (yytoken == Token_COMMA)
        {
            if (yytoken != Token_COMMA)
            {
                expectedToken(yytoken, Token_COMMA, "comma");
                return false;
            }
            yylex();

            if (yytoken == Token_RBRACE)
            {
                break;
            }
            TestAst *__node_43 = 0;
            if (!parseTest(&__node_43))
            {
                expectedSymbol(AstNode::TestKind, "test");
                return false;
            }
            (*yynode)->keyListSequence = snoc((*yynode)->keyListSequence, __node_43, memoryPool);

            if (yytoken != Token_COLON)
            {
                expectedToken(yytoken, Token_COLON, "colon");
                return false;
            }
            yylex();

            TestAst *__node_44 = 0;
            if (!parseTest(&__node_44))
            {
                expectedSymbol(AstNode::TestKind, "test");
                return false;
            }
            (*yynode)->valueListSequence = snoc((*yynode)->valueListSequence, __node_44, memoryPool);

        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseDottedAsName(DottedAsNameAst **yynode)
{
    *yynode = create<DottedAsNameAst>();

    (*yynode)->startToken = tokenStream->index() - 1;
    (*yynode)->importedAs = -1;

    if (yytoken == Token_IDENTIFIER)
    {
        DottedNameAst *__node_45 = 0;
        if (!parseDottedName(&__node_45))
        {
            expectedSymbol(AstNode::DottedNameKind, "dottedName");
            return false;
        }
        (*yynode)->importDottedName = __node_45;

        if (yytoken == Token_AS)
        {
            if (yytoken != Token_AS)
            {
                expectedToken(yytoken, Token_AS, "as");
                return false;
            }
            yylex();

            if (yytoken != Token_IDENTIFIER)
            {
                expectedToken(yytoken, Token_IDENTIFIER, "identifier");
                return false;
            }
            (*yynode)->importedAs = tokenStream->index() - 1;
            yylex();

        }
        else if (true /*epsilon*/)
        {
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseDottedAsNames(DottedAsNamesAst **yynode)
{
    *yynode = create<DottedAsNamesAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_IDENTIFIER)
    {
        DottedAsNameAst *__node_46 = 0;
        if (!parseDottedAsName(&__node_46))
        {
            expectedSymbol(AstNode::DottedAsNameKind, "dottedAsName");
            return false;
        }
        (*yynode)->dottedAsNameSequence = snoc((*yynode)->dottedAsNameSequence, __node_46, memoryPool);

        while (yytoken == Token_COMMA)
        {
            if (yytoken != Token_COMMA)
            {
                expectedToken(yytoken, Token_COMMA, "comma");
                return false;
            }
            yylex();

            DottedAsNameAst *__node_47 = 0;
            if (!parseDottedAsName(&__node_47))
            {
                expectedSymbol(AstNode::DottedAsNameKind, "dottedAsName");
                return false;
            }
            (*yynode)->dottedAsNameSequence = snoc((*yynode)->dottedAsNameSequence, __node_47, memoryPool);

        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseDottedName(DottedNameAst **yynode)
{
    *yynode = create<DottedNameAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_IDENTIFIER)
    {
        if (yytoken != Token_IDENTIFIER)
        {
            expectedToken(yytoken, Token_IDENTIFIER, "identifier");
            return false;
        }
        (*yynode)->dottedNameSequence = snoc((*yynode)->dottedNameSequence, tokenStream->index() - 1, memoryPool);
        yylex();

        while (yytoken == Token_DOT)
        {
            if (yytoken != Token_DOT)
            {
                expectedToken(yytoken, Token_DOT, "dot");
                return false;
            }
            yylex();

            if (yytoken != Token_IDENTIFIER)
            {
                expectedToken(yytoken, Token_IDENTIFIER, "identifier");
                return false;
            }
            (*yynode)->dottedNameSequence = snoc((*yynode)->dottedNameSequence, tokenStream->index() - 1, memoryPool);
            yylex();

        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseExceptClause(ExceptClauseAst **yynode)
{
    *yynode = create<ExceptClauseAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_EXCEPT)
    {
        if (yytoken != Token_EXCEPT)
        {
            expectedToken(yytoken, Token_EXCEPT, "except");
            return false;
        }
        yylex();

        if (yytoken == Token_NOT
            || yytoken == Token_LBRACE
            || yytoken == Token_STRINGLITERAL
            || yytoken == Token_FLOAT
            || yytoken == Token_TILDE
            || yytoken == Token_BACKTICK
            || yytoken == Token_LAMBDA
            || yytoken == Token_LBRACKET
            || yytoken == Token_INTEGER
            || yytoken == Token_MINUS
            || yytoken == Token_LPAREN
            || yytoken == Token_IDENTIFIER
            || yytoken == Token_PLUS
            || yytoken == Token_IMAGNUM)
        {
            TestAst *__node_48 = 0;
            if (!parseTest(&__node_48))
            {
                expectedSymbol(AstNode::TestKind, "test");
                return false;
            }
            (*yynode)->exceptTest = __node_48;

            if (yytoken == Token_COMMA)
            {
                if (yytoken != Token_COMMA)
                {
                    expectedToken(yytoken, Token_COMMA, "comma");
                    return false;
                }
                yylex();

                TestAst *__node_49 = 0;
                if (!parseTest(&__node_49))
                {
                    expectedSymbol(AstNode::TestKind, "test");
                    return false;
                }
                (*yynode)->exceptTargetTest = __node_49;

            }
            else if (true /*epsilon*/)
            {
            }
            else
            {
                return false;
            }
        }
        else if (true /*epsilon*/)
        {
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseExecStmt(ExecStmtAst **yynode)
{
    *yynode = create<ExecStmtAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_EXEC)
    {
        if (yytoken != Token_EXEC)
        {
            expectedToken(yytoken, Token_EXEC, "exec");
            return false;
        }
        yylex();

        ExprAst *__node_50 = 0;
        if (!parseExpr(&__node_50))
        {
            expectedSymbol(AstNode::ExprKind, "expr");
            return false;
        }
        (*yynode)->execCode = __node_50;

        if (yytoken == Token_IN)
        {
            if (yytoken != Token_IN)
            {
                expectedToken(yytoken, Token_IN, "in");
                return false;
            }
            yylex();

            TestAst *__node_51 = 0;
            if (!parseTest(&__node_51))
            {
                expectedSymbol(AstNode::TestKind, "test");
                return false;
            }
            (*yynode)->globalDictExec = __node_51;

            if (yytoken == Token_COMMA)
            {
                if (yytoken != Token_COMMA)
                {
                    expectedToken(yytoken, Token_COMMA, "comma");
                    return false;
                }
                yylex();

                TestAst *__node_52 = 0;
                if (!parseTest(&__node_52))
                {
                    expectedSymbol(AstNode::TestKind, "test");
                    return false;
                }
                (*yynode)->localDictExec = __node_52;

            }
            else if (true /*epsilon*/)
            {
            }
            else
            {
                return false;
            }
        }
        else if (true /*epsilon*/)
        {
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseExpr(ExprAst **yynode)
{
    *yynode = create<ExprAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_LBRACE
        || yytoken == Token_STRINGLITERAL
        || yytoken == Token_FLOAT
        || yytoken == Token_TILDE
        || yytoken == Token_BACKTICK
        || yytoken == Token_LBRACKET
        || yytoken == Token_INTEGER
        || yytoken == Token_MINUS
        || yytoken == Token_LPAREN
        || yytoken == Token_IDENTIFIER
        || yytoken == Token_PLUS
        || yytoken == Token_IMAGNUM)
    {
        XorExprAst *__node_53 = 0;
        if (!parseXorExpr(&__node_53))
        {
            expectedSymbol(AstNode::XorExprKind, "xorExpr");
            return false;
        }
        (*yynode)->expr = __node_53;

        while (yytoken == Token_BITOR)
        {
            if (yytoken != Token_BITOR)
            {
                expectedToken(yytoken, Token_BITOR, "bitor");
                return false;
            }
            yylex();

            XorExprAst *__node_54 = 0;
            if (!parseXorExpr(&__node_54))
            {
                expectedSymbol(AstNode::XorExprKind, "xorExpr");
                return false;
            }
            (*yynode)->orrExprSequence = snoc((*yynode)->orrExprSequence, __node_54, memoryPool);

        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseExprStmt(ExprStmtAst **yynode)
{
    *yynode = create<ExprStmtAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_NOT
        || yytoken == Token_LBRACE
        || yytoken == Token_STRINGLITERAL
        || yytoken == Token_FLOAT
        || yytoken == Token_TILDE
        || yytoken == Token_BACKTICK
        || yytoken == Token_LAMBDA
        || yytoken == Token_LBRACKET
        || yytoken == Token_INTEGER
        || yytoken == Token_MINUS
        || yytoken == Token_LPAREN
        || yytoken == Token_IDENTIFIER
        || yytoken == Token_PLUS
        || yytoken == Token_IMAGNUM)
    {
        TestlistAst *__node_55 = 0;
        if (!parseTestlist(&__node_55))
        {
            expectedSymbol(AstNode::TestlistKind, "testlist");
            return false;
        }
        (*yynode)->testlist = __node_55;

        if (yytoken == Token_SLASHEQ
            || yytoken == Token_ANDEQ
            || yytoken == Token_LSHIFTEQ
            || yytoken == Token_MINUSEQ
            || yytoken == Token_OREQ
            || yytoken == Token_MODULOEQ
            || yytoken == Token_DOUBLESTAREQ
            || yytoken == Token_PLUSEQ
            || yytoken == Token_TILDEEQ
            || yytoken == Token_DOUBLESLASHEQ
            || yytoken == Token_STAREQ
            || yytoken == Token_RSHIFTEQ)
        {
            AugassignAst *__node_56 = 0;
            if (!parseAugassign(&__node_56))
            {
                expectedSymbol(AstNode::AugassignKind, "augassign");
                return false;
            }
            (*yynode)->augassign = __node_56;

            if (yytoken == Token_NOT
                || yytoken == Token_LBRACE
                || yytoken == Token_STRINGLITERAL
                || yytoken == Token_FLOAT
                || yytoken == Token_TILDE
                || yytoken == Token_BACKTICK
                || yytoken == Token_LAMBDA
                || yytoken == Token_LBRACKET
                || yytoken == Token_INTEGER
                || yytoken == Token_MINUS
                || yytoken == Token_LPAREN
                || yytoken == Token_IDENTIFIER
                || yytoken == Token_PLUS
                || yytoken == Token_IMAGNUM)
            {
                TestlistAst *__node_57 = 0;
                if (!parseTestlist(&__node_57))
                {
                    expectedSymbol(AstNode::TestlistKind, "testlist");
                    return false;
                }
                (*yynode)->anugassignTestlist = __node_57;

            }
            else if (yytoken == Token_YIELD)
            {
                YieldExprAst *__node_58 = 0;
                if (!parseYieldExpr(&__node_58))
                {
                    expectedSymbol(AstNode::YieldExprKind, "yieldExpr");
                    return false;
                }
                (*yynode)->yield = __node_58;

            }
            else
            {
                return false;
            }
        }
        else if (yytoken == Token_EQUAL)
        {
            do
            {
                if (yytoken != Token_EQUAL)
                {
                    expectedToken(yytoken, Token_EQUAL, "equal");
                    return false;
                }
                yylex();

                if (yytoken == Token_YIELD)
                {
                    YieldExprAst *__node_59 = 0;
                    if (!parseYieldExpr(&__node_59))
                    {
                        expectedSymbol(AstNode::YieldExprKind, "yieldExpr");
                        return false;
                    }
                    (*yynode)->yield = __node_59;

                }
                else if (yytoken == Token_NOT
                         || yytoken == Token_LBRACE
                         || yytoken == Token_STRINGLITERAL
                         || yytoken == Token_FLOAT
                         || yytoken == Token_TILDE
                         || yytoken == Token_BACKTICK
                         || yytoken == Token_LAMBDA
                         || yytoken == Token_LBRACKET
                         || yytoken == Token_INTEGER
                         || yytoken == Token_MINUS
                         || yytoken == Token_LPAREN
                         || yytoken == Token_IDENTIFIER
                         || yytoken == Token_PLUS
                         || yytoken == Token_IMAGNUM)
                {
                    TestlistAst *__node_60 = 0;
                    if (!parseTestlist(&__node_60))
                    {
                        expectedSymbol(AstNode::TestlistKind, "testlist");
                        return false;
                    }
                    (*yynode)->equalTestlistSequence = snoc((*yynode)->equalTestlistSequence, __node_60, memoryPool);

                }
                else
                {
                    return false;
                }
            }
            while (yytoken == Token_EQUAL);
        }
        else if ((true /*epsilon*/) && ( yytoken == Token_SEMICOLON || yytoken == Token_LINEBREAK ))
        {
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseExprlist(ExprlistAst **yynode)
{
    *yynode = create<ExprlistAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_LBRACE
        || yytoken == Token_STRINGLITERAL
        || yytoken == Token_FLOAT
        || yytoken == Token_TILDE
        || yytoken == Token_BACKTICK
        || yytoken == Token_LBRACKET
        || yytoken == Token_INTEGER
        || yytoken == Token_MINUS
        || yytoken == Token_LPAREN
        || yytoken == Token_IDENTIFIER
        || yytoken == Token_PLUS
        || yytoken == Token_IMAGNUM)
    {
        ExprAst *__node_61 = 0;
        if (!parseExpr(&__node_61))
        {
            expectedSymbol(AstNode::ExprKind, "expr");
            return false;
        }
        (*yynode)->exprSequence = snoc((*yynode)->exprSequence, __node_61, memoryPool);

        while (yytoken == Token_COMMA)
        {
            if (yytoken != Token_COMMA)
            {
                expectedToken(yytoken, Token_COMMA, "comma");
                return false;
            }
            yylex();

            if (yytoken == Token_IN || yytoken == Token_SEMICOLON || yytoken == Token_LINEBREAK )
            {
                break;
            }
            ExprAst *__node_62 = 0;
            if (!parseExpr(&__node_62))
            {
                expectedSymbol(AstNode::ExprKind, "expr");
                return false;
            }
            (*yynode)->exprSequence = snoc((*yynode)->exprSequence, __node_62, memoryPool);

        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseFactOp(FactOpAst **yynode)
{
    *yynode = create<FactOpAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_TILDE
        || yytoken == Token_MINUS
        || yytoken == Token_PLUS)
    {
        if (yytoken == Token_PLUS)
        {
            if (yytoken != Token_PLUS)
            {
                expectedToken(yytoken, Token_PLUS, "plus");
                return false;
            }
            yylex();

            (*yynode)->op = PythonParser::UnaryPlusOp;
        }
        else if (yytoken == Token_MINUS)
        {
            if (yytoken != Token_MINUS)
            {
                expectedToken(yytoken, Token_MINUS, "minus");
                return false;
            }
            yylex();

            (*yynode)->op = PythonParser::UnaryMinusOp;
        }
        else if (yytoken == Token_TILDE)
        {
            if (yytoken != Token_TILDE)
            {
                expectedToken(yytoken, Token_TILDE, "tilde");
                return false;
            }
            yylex();

            (*yynode)->op = PythonParser::UnaryTildeOp ;
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseFactor(FactorAst **yynode)
{
    *yynode = create<FactorAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_LBRACE
        || yytoken == Token_STRINGLITERAL
        || yytoken == Token_FLOAT
        || yytoken == Token_TILDE
        || yytoken == Token_BACKTICK
        || yytoken == Token_LBRACKET
        || yytoken == Token_INTEGER
        || yytoken == Token_MINUS
        || yytoken == Token_LPAREN
        || yytoken == Token_IDENTIFIER
        || yytoken == Token_PLUS
        || yytoken == Token_IMAGNUM)
    {
        if (yytoken == Token_TILDE
            || yytoken == Token_MINUS
            || yytoken == Token_PLUS)
        {
            FactOpAst *__node_63 = 0;
            if (!parseFactOp(&__node_63))
            {
                expectedSymbol(AstNode::FactOpKind, "factOp");
                return false;
            }
            (*yynode)->factOp = __node_63;

            FactorAst *__node_64 = 0;
            if (!parseFactor(&__node_64))
            {
                expectedSymbol(AstNode::FactorKind, "factor");
                return false;
            }
            (*yynode)->factor = __node_64;

        }
        else if (yytoken == Token_LBRACE
                 || yytoken == Token_STRINGLITERAL
                 || yytoken == Token_FLOAT
                 || yytoken == Token_BACKTICK
                 || yytoken == Token_LBRACKET
                 || yytoken == Token_INTEGER
                 || yytoken == Token_LPAREN
                 || yytoken == Token_IDENTIFIER
                 || yytoken == Token_IMAGNUM)
        {
            PowerAst *__node_65 = 0;
            if (!parsePower(&__node_65))
            {
                expectedSymbol(AstNode::PowerKind, "power");
                return false;
            }
            (*yynode)->power = __node_65;

        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseFlowStmt(FlowStmtAst **yynode)
{
    *yynode = create<FlowStmtAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_RETURN
        || yytoken == Token_RAISE
        || yytoken == Token_YIELD
        || yytoken == Token_BREAK
        || yytoken == Token_CONTINUE)
    {
        if (yytoken == Token_BREAK)
        {
            BreakStmtAst *__node_66 = 0;
            if (!parseBreakStmt(&__node_66))
            {
                expectedSymbol(AstNode::BreakStmtKind, "breakStmt");
                return false;
            }
            (*yynode)->breakStmt = __node_66;

        }
        else if (yytoken == Token_CONTINUE)
        {
            ContinueStmtAst *__node_67 = 0;
            if (!parseContinueStmt(&__node_67))
            {
                expectedSymbol(AstNode::ContinueStmtKind, "continueStmt");
                return false;
            }
            (*yynode)->continueStmt = __node_67;

        }
        else if (yytoken == Token_RETURN)
        {
            ReturnStmtAst *__node_68 = 0;
            if (!parseReturnStmt(&__node_68))
            {
                expectedSymbol(AstNode::ReturnStmtKind, "returnStmt");
                return false;
            }
            (*yynode)->returnStmt = __node_68;

        }
        else if (yytoken == Token_RAISE)
        {
            RaiseStmtAst *__node_69 = 0;
            if (!parseRaiseStmt(&__node_69))
            {
                expectedSymbol(AstNode::RaiseStmtKind, "raiseStmt");
                return false;
            }
            (*yynode)->raiseStmt = __node_69;

        }
        else if (yytoken == Token_YIELD)
        {
            YieldStmtAst *__node_70 = 0;
            if (!parseYieldStmt(&__node_70))
            {
                expectedSymbol(AstNode::YieldStmtKind, "yieldStmt");
                return false;
            }
            (*yynode)->yieldStmt = __node_70;

        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseForStmt(ForStmtAst **yynode)
{
    *yynode = create<ForStmtAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_FOR)
    {
        if (yytoken != Token_FOR)
        {
            expectedToken(yytoken, Token_FOR, "for");
            return false;
        }
        yylex();

        ExprlistAst *__node_71 = 0;
        if (!parseExprlist(&__node_71))
        {
            expectedSymbol(AstNode::ExprlistKind, "exprlist");
            return false;
        }
        (*yynode)->forExpr = __node_71;

        if (yytoken != Token_IN)
        {
            expectedToken(yytoken, Token_IN, "in");
            return false;
        }
        yylex();

        TestlistAst *__node_72 = 0;
        if (!parseTestlist(&__node_72))
        {
            expectedSymbol(AstNode::TestlistKind, "testlist");
            return false;
        }
        (*yynode)->forTestlist = __node_72;

        if (yytoken != Token_COLON)
        {
            expectedToken(yytoken, Token_COLON, "colon");
            return false;
        }
        yylex();

        SuiteAst *__node_73 = 0;
        if (!parseSuite(&__node_73))
        {
            expectedSymbol(AstNode::SuiteKind, "suite");
            return false;
        }
        (*yynode)->forSuite = __node_73;

        if (yytoken == Token_ELSE)
        {
            if (yytoken != Token_ELSE)
            {
                expectedToken(yytoken, Token_ELSE, "else");
                return false;
            }
            yylex();

            if (yytoken != Token_COLON)
            {
                expectedToken(yytoken, Token_COLON, "colon");
                return false;
            }
            yylex();

            SuiteAst *__node_74 = 0;
            if (!parseSuite(&__node_74))
            {
                expectedSymbol(AstNode::SuiteKind, "suite");
                return false;
            }
            (*yynode)->forElseSuite = __node_74;

        }
        else if (true /*epsilon*/)
        {
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseFpDef(FpDefAst **yynode)
{
    *yynode = create<FpDefAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_LPAREN
        || yytoken == Token_IDENTIFIER)
    {
        DefparamAst *__node_75 = 0;
        if (!parseDefparam(&__node_75))
        {
            expectedSymbol(AstNode::DefparamKind, "defparam");
            return false;
        }
        (*yynode)->defparam = __node_75;

        if (yytoken == Token_EQUAL)
        {
            if (yytoken != Token_EQUAL)
            {
                expectedToken(yytoken, Token_EQUAL, "equal");
                return false;
            }
            yylex();

            TestAst *__node_76 = 0;
            if (!parseTest(&__node_76))
            {
                expectedSymbol(AstNode::TestKind, "test");
                return false;
            }
            (*yynode)->fpDefTest = __node_76;

        }
        else if (true /*epsilon*/)
        {
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseFplist(FplistAst **yynode)
{
    *yynode = create<FplistAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_LPAREN
        || yytoken == Token_IDENTIFIER)
    {
        DefparamAst *__node_77 = 0;
        if (!parseDefparam(&__node_77))
        {
            expectedSymbol(AstNode::DefparamKind, "defparam");
            return false;
        }
        (*yynode)->fplistFpdefSequence = snoc((*yynode)->fplistFpdefSequence, __node_77, memoryPool);

        while (yytoken == Token_COMMA)
        {
            if (yytoken != Token_COMMA)
            {
                expectedToken(yytoken, Token_COMMA, "comma");
                return false;
            }
            yylex();

            if ( yytoken == Token_RPAREN )
            {
                break;
            }
            DefparamAst *__node_78 = 0;
            if (!parseDefparam(&__node_78))
            {
                expectedSymbol(AstNode::DefparamKind, "defparam");
                return false;
            }
            (*yynode)->fplistFpdefSequence = snoc((*yynode)->fplistFpdefSequence, __node_78, memoryPool);

        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseFunPosParam(FunPosParamAst **yynode)
{
    *yynode = create<FunPosParamAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_DOUBLESTAR
        || yytoken == Token_STAR)
    {
        if (yytoken == Token_STAR)
        {
            ListParamAst *__node_79 = 0;
            if (!parseListParam(&__node_79))
            {
                expectedSymbol(AstNode::ListParamKind, "listParam");
                return false;
            }
            (*yynode)->listParam = __node_79;

            if (yytoken == Token_COMMA)
            {
                if (yytoken != Token_COMMA)
                {
                    expectedToken(yytoken, Token_COMMA, "comma");
                    return false;
                }
                yylex();

                DictParamAst *__node_80 = 0;
                if (!parseDictParam(&__node_80))
                {
                    expectedSymbol(AstNode::DictParamKind, "dictParam");
                    return false;
                }
                (*yynode)->dictParam = __node_80;

            }
            else if (true /*epsilon*/)
            {
            }
            else
            {
                return false;
            }
        }
        else if (yytoken == Token_DOUBLESTAR)
        {
            DictParamAst *__node_81 = 0;
            if (!parseDictParam(&__node_81))
            {
                expectedSymbol(AstNode::DictParamKind, "dictParam");
                return false;
            }
            (*yynode)->dictParam = __node_81;

        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseFuncDef(FuncDefAst **yynode)
{
    *yynode = create<FuncDefAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_LPAREN
        || yytoken == Token_IDENTIFIER)
    {
        FpDefAst *__node_82 = 0;
        if (!parseFpDef(&__node_82))
        {
            expectedSymbol(AstNode::FpDefKind, "fpDef");
            return false;
        }
        (*yynode)->fpDefSequence = snoc((*yynode)->fpDefSequence, __node_82, memoryPool);

        while (yytoken == Token_COMMA)
        {
            if (yytoken != Token_COMMA)
            {
                expectedToken(yytoken, Token_COMMA, "comma");
                return false;
            }
            yylex();

            if (yytoken == Token_RPAREN  || yytoken == Token_STAR || yytoken == Token_DOUBLESTAR )
            {
                break;
            }
            FpDefAst *__node_83 = 0;
            if (!parseFpDef(&__node_83))
            {
                expectedSymbol(AstNode::FpDefKind, "fpDef");
                return false;
            }
            (*yynode)->fpDefSequence = snoc((*yynode)->fpDefSequence, __node_83, memoryPool);

        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseFuncdecl(FuncdeclAst **yynode)
{
    *yynode = create<FuncdeclAst>();

    (*yynode)->startToken = tokenStream->index() - 1;
    (*yynode)->funcName = -1;

    if (yytoken == Token_DEF
        || yytoken == Token_AT)
    {
        if (yytoken == Token_AT)
        {
            DecoratorsAst *__node_84 = 0;
            if (!parseDecorators(&__node_84))
            {
                expectedSymbol(AstNode::DecoratorsKind, "decorators");
                return false;
            }
            (*yynode)->decorators = __node_84;

        }
        else if (true /*epsilon*/)
        {
        }
        else
        {
            return false;
        }
        if (yytoken != Token_DEF)
        {
            expectedToken(yytoken, Token_DEF, "def");
            return false;
        }
        yylex();

        if (yytoken != Token_IDENTIFIER)
        {
            expectedToken(yytoken, Token_IDENTIFIER, "identifier");
            return false;
        }
        (*yynode)->funcName = tokenStream->index() - 1;
        yylex();

        if (yytoken != Token_LPAREN)
        {
            expectedToken(yytoken, Token_LPAREN, "lparen");
            return false;
        }
        yylex();

        if ((yytoken == Token_DOUBLESTAR
             || yytoken == Token_LPAREN
             || yytoken == Token_STAR
             || yytoken == Token_IDENTIFIER) && ( LA(1).kind != Token_RPAREN ))
        {
            VarargslistAst *__node_85 = 0;
            if (!parseVarargslist(&__node_85))
            {
                expectedSymbol(AstNode::VarargslistKind, "varargslist");
                return false;
            }
            (*yynode)->funArgs = __node_85;

        }
        else if (true /*epsilon*/)
        {
        }
        else
        {
            return false;
        }
        if (yytoken != Token_RPAREN)
        {
            expectedToken(yytoken, Token_RPAREN, "rparen");
            return false;
        }
        yylex();

        if (yytoken != Token_COLON)
        {
            expectedToken(yytoken, Token_COLON, "colon");
            return false;
        }
        yylex();

        SuiteAst *__node_86 = 0;
        if (!parseSuite(&__node_86))
        {
            expectedSymbol(AstNode::SuiteKind, "suite");
            return false;
        }
        (*yynode)->funSuite = __node_86;

    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseGenFor(GenForAst **yynode)
{
    *yynode = create<GenForAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_FOR)
    {
        if (yytoken != Token_FOR)
        {
            expectedToken(yytoken, Token_FOR, "for");
            return false;
        }
        yylex();

        ExprlistAst *__node_87 = 0;
        if (!parseExprlist(&__node_87))
        {
            expectedSymbol(AstNode::ExprlistKind, "exprlist");
            return false;
        }
        (*yynode)->exprlist = __node_87;

        if (yytoken != Token_IN)
        {
            expectedToken(yytoken, Token_IN, "in");
            return false;
        }
        yylex();

        TestAst *__node_88 = 0;
        if (!parseTest(&__node_88))
        {
            expectedSymbol(AstNode::TestKind, "test");
            return false;
        }
        (*yynode)->test = __node_88;

        if (yytoken == Token_FOR
            || yytoken == Token_IF)
        {
            GenIterAst *__node_89 = 0;
            if (!parseGenIter(&__node_89))
            {
                expectedSymbol(AstNode::GenIterKind, "genIter");
                return false;
            }
            (*yynode)->genIter = __node_89;

        }
        else if (true /*epsilon*/)
        {
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseGenIf(GenIfAst **yynode)
{
    *yynode = create<GenIfAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_IF)
    {
        if (yytoken != Token_IF)
        {
            expectedToken(yytoken, Token_IF, "if");
            return false;
        }
        yylex();

        TestAst *__node_90 = 0;
        if (!parseTest(&__node_90))
        {
            expectedSymbol(AstNode::TestKind, "test");
            return false;
        }
        (*yynode)->test = __node_90;

        if (yytoken == Token_FOR
            || yytoken == Token_IF)
        {
            GenIterAst *__node_91 = 0;
            if (!parseGenIter(&__node_91))
            {
                expectedSymbol(AstNode::GenIterKind, "genIter");
                return false;
            }
            (*yynode)->genIter = __node_91;

        }
        else if (true /*epsilon*/)
        {
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseGenIter(GenIterAst **yynode)
{
    *yynode = create<GenIterAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_FOR
        || yytoken == Token_IF)
    {
        if (yytoken == Token_FOR)
        {
            GenForAst *__node_92 = 0;
            if (!parseGenFor(&__node_92))
            {
                expectedSymbol(AstNode::GenForKind, "genFor");
                return false;
            }
            (*yynode)->genFor = __node_92;

        }
        else if (yytoken == Token_IF)
        {
            GenIfAst *__node_93 = 0;
            if (!parseGenIf(&__node_93))
            {
                expectedSymbol(AstNode::GenIfKind, "genIf");
                return false;
            }
            (*yynode)->genIf = __node_93;

        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseGlobalStmt(GlobalStmtAst **yynode)
{
    *yynode = create<GlobalStmtAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_GLOBAL)
    {
        if (yytoken != Token_GLOBAL)
        {
            expectedToken(yytoken, Token_GLOBAL, "global");
            return false;
        }
        yylex();

        if (yytoken != Token_IDENTIFIER)
        {
            expectedToken(yytoken, Token_IDENTIFIER, "identifier");
            return false;
        }
        (*yynode)->globalNameSequence = snoc((*yynode)->globalNameSequence, tokenStream->index() - 1, memoryPool);
        yylex();

        while (yytoken == Token_COMMA)
        {
            if (yytoken != Token_COMMA)
            {
                expectedToken(yytoken, Token_COMMA, "comma");
                return false;
            }
            yylex();

            if (yytoken != Token_IDENTIFIER)
            {
                expectedToken(yytoken, Token_IDENTIFIER, "identifier");
                return false;
            }
            (*yynode)->globalNameSequence = snoc((*yynode)->globalNameSequence, tokenStream->index() - 1, memoryPool);
            yylex();

        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseIfStmt(IfStmtAst **yynode)
{
    *yynode = create<IfStmtAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_IF)
    {
        if (yytoken != Token_IF)
        {
            expectedToken(yytoken, Token_IF, "if");
            return false;
        }
        yylex();

        TestAst *__node_94 = 0;
        if (!parseTest(&__node_94))
        {
            expectedSymbol(AstNode::TestKind, "test");
            return false;
        }
        (*yynode)->ifTest = __node_94;

        if (yytoken != Token_COLON)
        {
            expectedToken(yytoken, Token_COLON, "colon");
            return false;
        }
        yylex();

        SuiteAst *__node_95 = 0;
        if (!parseSuite(&__node_95))
        {
            expectedSymbol(AstNode::SuiteKind, "suite");
            return false;
        }
        (*yynode)->ifSuite = __node_95;

        while (yytoken == Token_ELIF)
        {
            if (yytoken != Token_ELIF)
            {
                expectedToken(yytoken, Token_ELIF, "elif");
                return false;
            }
            yylex();

            TestAst *__node_96 = 0;
            if (!parseTest(&__node_96))
            {
                expectedSymbol(AstNode::TestKind, "test");
                return false;
            }
            (*yynode)->elifTestSequence = snoc((*yynode)->elifTestSequence, __node_96, memoryPool);

            if (yytoken != Token_COLON)
            {
                expectedToken(yytoken, Token_COLON, "colon");
                return false;
            }
            yylex();

            SuiteAst *__node_97 = 0;
            if (!parseSuite(&__node_97))
            {
                expectedSymbol(AstNode::SuiteKind, "suite");
                return false;
            }
            (*yynode)->elifSuiteSequence = snoc((*yynode)->elifSuiteSequence, __node_97, memoryPool);

        }
        if (yytoken == Token_ELSE)
        {
            if (yytoken != Token_ELSE)
            {
                expectedToken(yytoken, Token_ELSE, "else");
                return false;
            }
            yylex();

            if (yytoken != Token_COLON)
            {
                expectedToken(yytoken, Token_COLON, "colon");
                return false;
            }
            yylex();

            SuiteAst *__node_98 = 0;
            if (!parseSuite(&__node_98))
            {
                expectedSymbol(AstNode::SuiteKind, "suite");
                return false;
            }
            (*yynode)->ifElseSuite = __node_98;

        }
        else if (true /*epsilon*/)
        {
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseImportAsName(ImportAsNameAst **yynode)
{
    *yynode = create<ImportAsNameAst>();

    (*yynode)->startToken = tokenStream->index() - 1;
    (*yynode)->importedName = -1;
    (*yynode)->importedAs = -1;

    if (yytoken == Token_IDENTIFIER)
    {
        if (yytoken != Token_IDENTIFIER)
        {
            expectedToken(yytoken, Token_IDENTIFIER, "identifier");
            return false;
        }
        (*yynode)->importedName = tokenStream->index() - 1;
        yylex();

        if (yytoken == Token_AS)
        {
            if (yytoken != Token_AS)
            {
                expectedToken(yytoken, Token_AS, "as");
                return false;
            }
            yylex();

            if (yytoken != Token_IDENTIFIER)
            {
                expectedToken(yytoken, Token_IDENTIFIER, "identifier");
                return false;
            }
            (*yynode)->importedAs = tokenStream->index() - 1;
            yylex();

        }
        else if (true /*epsilon*/)
        {
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseImportAsNames(ImportAsNamesAst **yynode)
{
    *yynode = create<ImportAsNamesAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_IDENTIFIER)
    {
        ImportAsNameAst *__node_99 = 0;
        if (!parseImportAsName(&__node_99))
        {
            expectedSymbol(AstNode::ImportAsNameKind, "importAsName");
            return false;
        }
        (*yynode)->importAsNameSequence = snoc((*yynode)->importAsNameSequence, __node_99, memoryPool);

        while (yytoken == Token_COMMA)
        {
            if (yytoken != Token_COMMA)
            {
                expectedToken(yytoken, Token_COMMA, "comma");
                return false;
            }
            yylex();

            if ( yytoken == Token_RPAREN || yytoken == Token_LINEBREAK || yytoken == Token_SEMICOLON )
            {
                break;
            }
            ImportAsNameAst *__node_100 = 0;
            if (!parseImportAsName(&__node_100))
            {
                expectedSymbol(AstNode::ImportAsNameKind, "importAsName");
                return false;
            }
            (*yynode)->importAsNameSequence = snoc((*yynode)->importAsNameSequence, __node_100, memoryPool);

        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseImportFrom(ImportFromAst **yynode)
{
    *yynode = create<ImportFromAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_FROM)
    {
        if (yytoken != Token_FROM)
        {
            expectedToken(yytoken, Token_FROM, "from");
            return false;
        }
        yylex();

        DottedNameAst *__node_101 = 0;
        if (!parseDottedName(&__node_101))
        {
            expectedSymbol(AstNode::DottedNameKind, "dottedName");
            return false;
        }
        (*yynode)->importFromName = __node_101;

        if (yytoken != Token_IMPORT)
        {
            expectedToken(yytoken, Token_IMPORT, "import");
            return false;
        }
        yylex();

        if (yytoken == Token_STAR)
        {
            if (yytoken != Token_STAR)
            {
                expectedToken(yytoken, Token_STAR, "star");
                return false;
            }
            yylex();

        }
        else if (yytoken == Token_LPAREN)
        {
            if (yytoken != Token_LPAREN)
            {
                expectedToken(yytoken, Token_LPAREN, "lparen");
                return false;
            }
            yylex();

            ImportAsNamesAst *__node_102 = 0;
            if (!parseImportAsNames(&__node_102))
            {
                expectedSymbol(AstNode::ImportAsNamesKind, "importAsNames");
                return false;
            }
            (*yynode)->importAsNames = __node_102;

            if (yytoken != Token_RPAREN)
            {
                expectedToken(yytoken, Token_RPAREN, "rparen");
                return false;
            }
            yylex();

        }
        else if (yytoken == Token_IDENTIFIER)
        {
            ImportAsNamesAst *__node_103 = 0;
            if (!parseImportAsNames(&__node_103))
            {
                expectedSymbol(AstNode::ImportAsNamesKind, "importAsNames");
                return false;
            }
            (*yynode)->importAsNames = __node_103;

        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseImportName(ImportNameAst **yynode)
{
    *yynode = create<ImportNameAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_IMPORT)
    {
        if (yytoken != Token_IMPORT)
        {
            expectedToken(yytoken, Token_IMPORT, "import");
            return false;
        }
        yylex();

        DottedAsNamesAst *__node_104 = 0;
        if (!parseDottedAsNames(&__node_104))
        {
            expectedSymbol(AstNode::DottedAsNamesKind, "dottedAsNames");
            return false;
        }
        (*yynode)->importName = __node_104;

    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseImportStmt(ImportStmtAst **yynode)
{
    *yynode = create<ImportStmtAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_IMPORT
        || yytoken == Token_FROM)
    {
        if (yytoken == Token_IMPORT)
        {
            ImportNameAst *__node_105 = 0;
            if (!parseImportName(&__node_105))
            {
                expectedSymbol(AstNode::ImportNameKind, "importName");
                return false;
            }
            (*yynode)->importImport = __node_105;

        }
        else if (yytoken == Token_FROM)
        {
            ImportFromAst *__node_106 = 0;
            if (!parseImportFrom(&__node_106))
            {
                expectedSymbol(AstNode::ImportFromKind, "importFrom");
                return false;
            }
            (*yynode)->importFrom = __node_106;

        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseLambdaDef(LambdaDefAst **yynode)
{
    *yynode = create<LambdaDefAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_LAMBDA)
    {
        if (yytoken != Token_LAMBDA)
        {
            expectedToken(yytoken, Token_LAMBDA, "lambda");
            return false;
        }
        yylex();

        if (yytoken == Token_DOUBLESTAR
            || yytoken == Token_LPAREN
            || yytoken == Token_STAR
            || yytoken == Token_IDENTIFIER)
        {
            VarargslistAst *__node_107 = 0;
            if (!parseVarargslist(&__node_107))
            {
                expectedSymbol(AstNode::VarargslistKind, "varargslist");
                return false;
            }
            (*yynode)->lambdaVarargslist = __node_107;

        }
        else if (true /*epsilon*/)
        {
        }
        else
        {
            return false;
        }
        if (yytoken != Token_COLON)
        {
            expectedToken(yytoken, Token_COLON, "colon");
            return false;
        }
        yylex();

        TestAst *__node_108 = 0;
        if (!parseTest(&__node_108))
        {
            expectedSymbol(AstNode::TestKind, "test");
            return false;
        }
        (*yynode)->lambdaTest = __node_108;

    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseListFor(ListForAst **yynode)
{
    *yynode = create<ListForAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_FOR)
    {
        if (yytoken != Token_FOR)
        {
            expectedToken(yytoken, Token_FOR, "for");
            return false;
        }
        yylex();

        ExprlistAst *__node_109 = 0;
        if (!parseExprlist(&__node_109))
        {
            expectedSymbol(AstNode::ExprlistKind, "exprlist");
            return false;
        }
        (*yynode)->exprlist = __node_109;

        if (yytoken != Token_IN)
        {
            expectedToken(yytoken, Token_IN, "in");
            return false;
        }
        yylex();

        TestlistSafeAst *__node_110 = 0;
        if (!parseTestlistSafe(&__node_110))
        {
            expectedSymbol(AstNode::TestlistSafeKind, "testlistSafe");
            return false;
        }
        (*yynode)->testlistSafe = __node_110;

        if (yytoken == Token_FOR
            || yytoken == Token_IF)
        {
            ListIterAst *__node_111 = 0;
            if (!parseListIter(&__node_111))
            {
                expectedSymbol(AstNode::ListIterKind, "listIter");
                return false;
            }
            (*yynode)->listIter = __node_111;

        }
        else if (true /*epsilon*/)
        {
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseListIf(ListIfAst **yynode)
{
    *yynode = create<ListIfAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_IF)
    {
        if (yytoken != Token_IF)
        {
            expectedToken(yytoken, Token_IF, "if");
            return false;
        }
        yylex();

        TestAst *__node_112 = 0;
        if (!parseTest(&__node_112))
        {
            expectedSymbol(AstNode::TestKind, "test");
            return false;
        }
        (*yynode)->test = __node_112;

        if (yytoken == Token_FOR
            || yytoken == Token_IF)
        {
            ListIterAst *__node_113 = 0;
            if (!parseListIter(&__node_113))
            {
                expectedSymbol(AstNode::ListIterKind, "listIter");
                return false;
            }
            (*yynode)->listIter = __node_113;

        }
        else if (true /*epsilon*/)
        {
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseListIter(ListIterAst **yynode)
{
    *yynode = create<ListIterAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_FOR
        || yytoken == Token_IF)
    {
        if (yytoken == Token_FOR)
        {
            ListForAst *__node_114 = 0;
            if (!parseListFor(&__node_114))
            {
                expectedSymbol(AstNode::ListForKind, "listFor");
                return false;
            }
            (*yynode)->listFor = __node_114;

        }
        else if (yytoken == Token_IF)
        {
            ListIfAst *__node_115 = 0;
            if (!parseListIf(&__node_115))
            {
                expectedSymbol(AstNode::ListIfKind, "listIf");
                return false;
            }
            (*yynode)->listIf = __node_115;

        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseListMakerTest(ListMakerTestAst **yynode)
{
    *yynode = create<ListMakerTestAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_NOT
        || yytoken == Token_LBRACE
        || yytoken == Token_STRINGLITERAL
        || yytoken == Token_FLOAT
        || yytoken == Token_TILDE
        || yytoken == Token_BACKTICK
        || yytoken == Token_LAMBDA
        || yytoken == Token_LBRACKET
        || yytoken == Token_INTEGER
        || yytoken == Token_MINUS
        || yytoken == Token_LPAREN
        || yytoken == Token_IDENTIFIER
        || yytoken == Token_PLUS
        || yytoken == Token_IMAGNUM || yytoken == Token_EOF
        || yytoken == Token_RBRACKET
        || yytoken == Token_FOR)
    {
        if (yytoken == Token_NOT
            || yytoken == Token_LBRACE
            || yytoken == Token_STRINGLITERAL
            || yytoken == Token_FLOAT
            || yytoken == Token_TILDE
            || yytoken == Token_BACKTICK
            || yytoken == Token_LAMBDA
            || yytoken == Token_LBRACKET
            || yytoken == Token_INTEGER
            || yytoken == Token_MINUS
            || yytoken == Token_LPAREN
            || yytoken == Token_IDENTIFIER
            || yytoken == Token_PLUS
            || yytoken == Token_IMAGNUM)
        {
            TestAst *__node_116 = 0;
            if (!parseTest(&__node_116))
            {
                expectedSymbol(AstNode::TestKind, "test");
                return false;
            }
            (*yynode)->listTestSequence = snoc((*yynode)->listTestSequence, __node_116, memoryPool);

            while (yytoken == Token_COMMA)
            {
                if (yytoken != Token_COMMA)
                {
                    expectedToken(yytoken, Token_COMMA, "comma");
                    return false;
                }
                yylex();

                if (yytoken == Token_RBRACKET)
                {
                    break;
                }
                TestAst *__node_117 = 0;
                if (!parseTest(&__node_117))
                {
                    expectedSymbol(AstNode::TestKind, "test");
                    return false;
                }
                (*yynode)->listTestSequence = snoc((*yynode)->listTestSequence, __node_117, memoryPool);

            }
        }
        else if (true /*epsilon*/)
        {
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseListParam(ListParamAst **yynode)
{
    *yynode = create<ListParamAst>();

    (*yynode)->startToken = tokenStream->index() - 1;
    (*yynode)->starId = -1;

    if (yytoken == Token_STAR)
    {
        if (yytoken != Token_STAR)
        {
            expectedToken(yytoken, Token_STAR, "star");
            return false;
        }
        yylex();

        if (yytoken != Token_IDENTIFIER)
        {
            expectedToken(yytoken, Token_IDENTIFIER, "identifier");
            return false;
        }
        (*yynode)->starId = tokenStream->index() - 1;
        yylex();

    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseListmaker(ListmakerAst **yynode)
{
    *yynode = create<ListmakerAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_NOT
        || yytoken == Token_LBRACE
        || yytoken == Token_STRINGLITERAL
        || yytoken == Token_FOR
        || yytoken == Token_FLOAT
        || yytoken == Token_TILDE
        || yytoken == Token_BACKTICK
        || yytoken == Token_LAMBDA
        || yytoken == Token_LBRACKET
        || yytoken == Token_INTEGER
        || yytoken == Token_MINUS
        || yytoken == Token_LPAREN
        || yytoken == Token_IDENTIFIER
        || yytoken == Token_PLUS
        || yytoken == Token_IMAGNUM || yytoken == Token_RBRACKET
        || yytoken == Token_EOF)
    {
        ListMakerTestAst *__node_118 = 0;
        if (!parseListMakerTest(&__node_118))
        {
            expectedSymbol(AstNode::ListMakerTestKind, "listMakerTest");
            return false;
        }
        (*yynode)->listMakerTest = __node_118;

        if (yytoken == Token_FOR)
        {
            ListForAst *__node_119 = 0;
            if (!parseListFor(&__node_119))
            {
                expectedSymbol(AstNode::ListForKind, "listFor");
                return false;
            }
            (*yynode)->listFor = __node_119;

        }
        else if (true /*epsilon*/)
        {
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseNotTest(NotTestAst **yynode)
{
    *yynode = create<NotTestAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_NOT
        || yytoken == Token_LBRACE
        || yytoken == Token_STRINGLITERAL
        || yytoken == Token_FLOAT
        || yytoken == Token_TILDE
        || yytoken == Token_BACKTICK
        || yytoken == Token_LBRACKET
        || yytoken == Token_INTEGER
        || yytoken == Token_MINUS
        || yytoken == Token_LPAREN
        || yytoken == Token_IDENTIFIER
        || yytoken == Token_PLUS
        || yytoken == Token_IMAGNUM)
    {
        if (yytoken == Token_NOT)
        {
            if (yytoken != Token_NOT)
            {
                expectedToken(yytoken, Token_NOT, "not");
                return false;
            }
            yylex();

            NotTestAst *__node_120 = 0;
            if (!parseNotTest(&__node_120))
            {
                expectedSymbol(AstNode::NotTestKind, "notTest");
                return false;
            }
            (*yynode)->notTest = __node_120;

        }
        else if (yytoken == Token_LBRACE
                 || yytoken == Token_STRINGLITERAL
                 || yytoken == Token_FLOAT
                 || yytoken == Token_TILDE
                 || yytoken == Token_BACKTICK
                 || yytoken == Token_LBRACKET
                 || yytoken == Token_INTEGER
                 || yytoken == Token_MINUS
                 || yytoken == Token_LPAREN
                 || yytoken == Token_IDENTIFIER
                 || yytoken == Token_PLUS
                 || yytoken == Token_IMAGNUM)
        {
            ComparisonAst *__node_121 = 0;
            if (!parseComparison(&__node_121))
            {
                expectedSymbol(AstNode::ComparisonKind, "comparison");
                return false;
            }
            (*yynode)->comparison = __node_121;

        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseNumber(NumberAst **yynode)
{
    *yynode = create<NumberAst>();

    (*yynode)->startToken = tokenStream->index() - 1;
    (*yynode)->value = -1;
    (*yynode)->value = -1;
    (*yynode)->value = -1;

    if (yytoken == Token_FLOAT
        || yytoken == Token_INTEGER
        || yytoken == Token_IMAGNUM)
    {
        if (yytoken == Token_INTEGER)
        {
            if (yytoken != Token_INTEGER)
            {
                expectedToken(yytoken, Token_INTEGER, "integer");
                return false;
            }
            (*yynode)->value = tokenStream->index() - 1;
            yylex();

            (*yynode)->numType = PythonParser::IntegerNumeric;
        }
        else if (yytoken == Token_FLOAT)
        {
            if (yytoken != Token_FLOAT)
            {
                expectedToken(yytoken, Token_FLOAT, "float");
                return false;
            }
            (*yynode)->value = tokenStream->index() - 1;
            yylex();

            (*yynode)->numType = PythonParser::FloatNumeric;
        }
        else if (yytoken == Token_IMAGNUM)
        {
            if (yytoken != Token_IMAGNUM)
            {
                expectedToken(yytoken, Token_IMAGNUM, "imagnum");
                return false;
            }
            (*yynode)->value = tokenStream->index() - 1;
            yylex();

            (*yynode)->numType = PythonParser::ImaginaryNumeric;
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parsePassStmt(PassStmtAst **yynode)
{
    *yynode = create<PassStmtAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_PASS)
    {
        if (yytoken != Token_PASS)
        {
            expectedToken(yytoken, Token_PASS, "pass");
            return false;
        }
        yylex();

    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parsePlainArgumentsList(PlainArgumentsListAst **yynode)
{
    *yynode = create<PlainArgumentsListAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_NOT
        || yytoken == Token_LBRACE
        || yytoken == Token_STRINGLITERAL
        || yytoken == Token_FLOAT
        || yytoken == Token_TILDE
        || yytoken == Token_BACKTICK
        || yytoken == Token_LAMBDA
        || yytoken == Token_LBRACKET
        || yytoken == Token_INTEGER
        || yytoken == Token_MINUS
        || yytoken == Token_LPAREN
        || yytoken == Token_IDENTIFIER
        || yytoken == Token_PLUS
        || yytoken == Token_IMAGNUM)
    {
        ArgumentAst *__node_122 = 0;
        if (!parseArgument(&__node_122))
        {
            expectedSymbol(AstNode::ArgumentKind, "argument");
            return false;
        }
        (*yynode)->argumentsSequence = snoc((*yynode)->argumentsSequence, __node_122, memoryPool);

        while (yytoken == Token_COMMA)
        {
            if (yytoken != Token_COMMA)
            {
                expectedToken(yytoken, Token_COMMA, "comma");
                return false;
            }
            yylex();

            if (yytoken == Token_RPAREN || yytoken == Token_STAR || yytoken == Token_DOUBLESTAR)
            {
                break;
            }
            ArgumentAst *__node_123 = 0;
            if (!parseArgument(&__node_123))
            {
                expectedSymbol(AstNode::ArgumentKind, "argument");
                return false;
            }
            (*yynode)->argumentsSequence = snoc((*yynode)->argumentsSequence, __node_123, memoryPool);

        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parsePower(PowerAst **yynode)
{
    *yynode = create<PowerAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_LBRACE
        || yytoken == Token_STRINGLITERAL
        || yytoken == Token_FLOAT
        || yytoken == Token_BACKTICK
        || yytoken == Token_LBRACKET
        || yytoken == Token_INTEGER
        || yytoken == Token_LPAREN
        || yytoken == Token_IDENTIFIER
        || yytoken == Token_IMAGNUM)
    {
        AtomAst *__node_124 = 0;
        if (!parseAtom(&__node_124))
        {
            expectedSymbol(AstNode::AtomKind, "atom");
            return false;
        }
        (*yynode)->atom = __node_124;

        while (yytoken == Token_LBRACKET
               || yytoken == Token_LPAREN
               || yytoken == Token_DOT)
        {
            TrailerAst *__node_125 = 0;
            if (!parseTrailer(&__node_125))
            {
                expectedSymbol(AstNode::TrailerKind, "trailer");
                return false;
            }
            (*yynode)->trailerSequence = snoc((*yynode)->trailerSequence, __node_125, memoryPool);

        }
        if (yytoken == Token_DOUBLESTAR)
        {
            if (yytoken != Token_DOUBLESTAR)
            {
                expectedToken(yytoken, Token_DOUBLESTAR, "doublestar");
                return false;
            }
            yylex();

            FactorAst *__node_126 = 0;
            if (!parseFactor(&__node_126))
            {
                expectedSymbol(AstNode::FactorKind, "factor");
                return false;
            }
            (*yynode)->factor = __node_126;

        }
        else if (true /*epsilon*/)
        {
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parsePrintStmt(PrintStmtAst **yynode)
{
    *yynode = create<PrintStmtAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_PRINT)
    {
        if (yytoken != Token_PRINT)
        {
            expectedToken(yytoken, Token_PRINT, "print");
            return false;
        }
        yylex();

        if (yytoken == Token_NOT
            || yytoken == Token_LBRACE
            || yytoken == Token_STRINGLITERAL
            || yytoken == Token_FLOAT
            || yytoken == Token_TILDE
            || yytoken == Token_BACKTICK
            || yytoken == Token_LAMBDA
            || yytoken == Token_LBRACKET
            || yytoken == Token_INTEGER
            || yytoken == Token_MINUS
            || yytoken == Token_LPAREN
            || yytoken == Token_IDENTIFIER
            || yytoken == Token_PLUS
            || yytoken == Token_IMAGNUM)
        {
            TestAst *__node_127 = 0;
            if (!parseTest(&__node_127))
            {
                expectedSymbol(AstNode::TestKind, "test");
                return false;
            }
            (*yynode)->printArgsSequence = snoc((*yynode)->printArgsSequence, __node_127, memoryPool);

            while (yytoken == Token_COMMA)
            {
                if (yytoken != Token_COMMA)
                {
                    expectedToken(yytoken, Token_COMMA, "comma");
                    return false;
                }
                yylex();

                if (yytoken == Token_SEMICOLON || yytoken == Token_LINEBREAK)
                {
                    break;
                }
                TestAst *__node_128 = 0;
                if (!parseTest(&__node_128))
                {
                    expectedSymbol(AstNode::TestKind, "test");
                    return false;
                }
                (*yynode)->printArgsSequence = snoc((*yynode)->printArgsSequence, __node_128, memoryPool);

            }
        }
        else if (yytoken == Token_RSHIFT)
        {
            if (yytoken != Token_RSHIFT)
            {
                expectedToken(yytoken, Token_RSHIFT, "rshift");
                return false;
            }
            yylex();

            TestAst *__node_129 = 0;
            if (!parseTest(&__node_129))
            {
                expectedSymbol(AstNode::TestKind, "test");
                return false;
            }
            (*yynode)->rshiftArgsSequence = snoc((*yynode)->rshiftArgsSequence, __node_129, memoryPool);

            while (yytoken == Token_COMMA)
            {
                if (yytoken != Token_COMMA)
                {
                    expectedToken(yytoken, Token_COMMA, "comma");
                    return false;
                }
                yylex();

                if (yytoken == Token_SEMICOLON || yytoken == Token_LINEBREAK)
                {
                    break;
                }
                TestAst *__node_130 = 0;
                if (!parseTest(&__node_130))
                {
                    expectedSymbol(AstNode::TestKind, "test");
                    return false;
                }
                (*yynode)->rshiftArgsSequence = snoc((*yynode)->rshiftArgsSequence, __node_130, memoryPool);

            }
        }
        else if (true /*epsilon*/)
        {
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseProject(ProjectAst **yynode)
{
    *yynode = create<ProjectAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_FLOAT
        || yytoken == Token_STRINGLITERAL
        || yytoken == Token_PRINT
        || yytoken == Token_YIELD
        || yytoken == Token_EXEC
        || yytoken == Token_MINUS
        || yytoken == Token_CLASS
        || yytoken == Token_GLOBAL
        || yytoken == Token_BACKTICK
        || yytoken == Token_RETURN
        || yytoken == Token_LBRACE
        || yytoken == Token_IMAGNUM
        || yytoken == Token_IDENTIFIER
        || yytoken == Token_DEF
        || yytoken == Token_IMPORT
        || yytoken == Token_WHILE
        || yytoken == Token_TILDE
        || yytoken == Token_NOT
        || yytoken == Token_BREAK
        || yytoken == Token_FROM
        || yytoken == Token_RAISE
        || yytoken == Token_DEL
        || yytoken == Token_LPAREN
        || yytoken == Token_INTEGER
        || yytoken == Token_LINEBREAK
        || yytoken == Token_PASS
        || yytoken == Token_CONTINUE
        || yytoken == Token_IF
        || yytoken == Token_PLUS
        || yytoken == Token_TRY
        || yytoken == Token_AT
        || yytoken == Token_LAMBDA
        || yytoken == Token_ASSERT
        || yytoken == Token_LBRACKET
        || yytoken == Token_FOR || yytoken == Token_EOF)
    {
        while (yytoken == Token_FLOAT
               || yytoken == Token_STRINGLITERAL
               || yytoken == Token_PRINT
               || yytoken == Token_YIELD
               || yytoken == Token_EXEC
               || yytoken == Token_MINUS
               || yytoken == Token_CLASS
               || yytoken == Token_GLOBAL
               || yytoken == Token_BACKTICK
               || yytoken == Token_RETURN
               || yytoken == Token_LBRACE
               || yytoken == Token_IMAGNUM
               || yytoken == Token_IDENTIFIER
               || yytoken == Token_DEF
               || yytoken == Token_IMPORT
               || yytoken == Token_WHILE
               || yytoken == Token_TILDE
               || yytoken == Token_NOT
               || yytoken == Token_BREAK
               || yytoken == Token_FROM
               || yytoken == Token_RAISE
               || yytoken == Token_DEL
               || yytoken == Token_LPAREN
               || yytoken == Token_INTEGER
               || yytoken == Token_LINEBREAK
               || yytoken == Token_PASS
               || yytoken == Token_CONTINUE
               || yytoken == Token_IF
               || yytoken == Token_PLUS
               || yytoken == Token_TRY
               || yytoken == Token_AT
               || yytoken == Token_LAMBDA
               || yytoken == Token_ASSERT
               || yytoken == Token_LBRACKET
               || yytoken == Token_FOR)
        {
            StmtAst *__node_131 = 0;
            if (!parseStmt(&__node_131))
            {
                expectedSymbol(AstNode::StmtKind, "stmt");
                return false;
            }
            (*yynode)->stmtSequence = snoc((*yynode)->stmtSequence, __node_131, memoryPool);

        }
        if (Token_EOF != yytoken)
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseRaiseStmt(RaiseStmtAst **yynode)
{
    *yynode = create<RaiseStmtAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_RAISE)
    {
        if (yytoken != Token_RAISE)
        {
            expectedToken(yytoken, Token_RAISE, "raise");
            return false;
        }
        yylex();

        if (yytoken == Token_NOT
            || yytoken == Token_LBRACE
            || yytoken == Token_STRINGLITERAL
            || yytoken == Token_FLOAT
            || yytoken == Token_TILDE
            || yytoken == Token_BACKTICK
            || yytoken == Token_LAMBDA
            || yytoken == Token_LBRACKET
            || yytoken == Token_INTEGER
            || yytoken == Token_MINUS
            || yytoken == Token_LPAREN
            || yytoken == Token_IDENTIFIER
            || yytoken == Token_PLUS
            || yytoken == Token_IMAGNUM)
        {
            TestAst *__node_132 = 0;
            if (!parseTest(&__node_132))
            {
                expectedSymbol(AstNode::TestKind, "test");
                return false;
            }
            (*yynode)->type = __node_132;

            if (yytoken == Token_COMMA)
            {
                if (yytoken != Token_COMMA)
                {
                    expectedToken(yytoken, Token_COMMA, "comma");
                    return false;
                }
                yylex();

                TestAst *__node_133 = 0;
                if (!parseTest(&__node_133))
                {
                    expectedSymbol(AstNode::TestKind, "test");
                    return false;
                }
                (*yynode)->value = __node_133;

                if (yytoken == Token_COMMA)
                {
                    if (yytoken != Token_COMMA)
                    {
                        expectedToken(yytoken, Token_COMMA, "comma");
                        return false;
                    }
                    yylex();

                    TestAst *__node_134 = 0;
                    if (!parseTest(&__node_134))
                    {
                        expectedSymbol(AstNode::TestKind, "test");
                        return false;
                    }
                    (*yynode)->traceback = __node_134;

                }
                else if (true /*epsilon*/)
                {
                }
                else
                {
                    return false;
                }
            }
            else if (true /*epsilon*/)
            {
            }
            else
            {
                return false;
            }
        }
        else if (true /*epsilon*/)
        {
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseReturnStmt(ReturnStmtAst **yynode)
{
    *yynode = create<ReturnStmtAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_RETURN)
    {
        if (yytoken != Token_RETURN)
        {
            expectedToken(yytoken, Token_RETURN, "returns");
            return false;
        }
        yylex();

        if (yytoken == Token_NOT
            || yytoken == Token_LBRACE
            || yytoken == Token_STRINGLITERAL
            || yytoken == Token_FLOAT
            || yytoken == Token_TILDE
            || yytoken == Token_BACKTICK
            || yytoken == Token_LAMBDA
            || yytoken == Token_LBRACKET
            || yytoken == Token_INTEGER
            || yytoken == Token_MINUS
            || yytoken == Token_LPAREN
            || yytoken == Token_IDENTIFIER
            || yytoken == Token_PLUS
            || yytoken == Token_IMAGNUM)
        {
            TestlistAst *__node_135 = 0;
            if (!parseTestlist(&__node_135))
            {
                expectedSymbol(AstNode::TestlistKind, "testlist");
                return false;
            }
            (*yynode)->returnExpr = __node_135;

        }
        else if (true /*epsilon*/)
        {
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseShiftExpr(ShiftExprAst **yynode)
{
    *yynode = create<ShiftExprAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_LBRACE
        || yytoken == Token_STRINGLITERAL
        || yytoken == Token_FLOAT
        || yytoken == Token_TILDE
        || yytoken == Token_BACKTICK
        || yytoken == Token_LBRACKET
        || yytoken == Token_INTEGER
        || yytoken == Token_MINUS
        || yytoken == Token_LPAREN
        || yytoken == Token_IDENTIFIER
        || yytoken == Token_PLUS
        || yytoken == Token_IMAGNUM)
    {
        ArithExprAst *__node_136 = 0;
        if (!parseArithExpr(&__node_136))
        {
            expectedSymbol(AstNode::ArithExprKind, "arithExpr");
            return false;
        }
        (*yynode)->arithExpr = __node_136;

        while (yytoken == Token_LSHIFT
               || yytoken == Token_RSHIFT)
        {
            ShiftOpAst *__node_137 = 0;
            if (!parseShiftOp(&__node_137))
            {
                expectedSymbol(AstNode::ShiftOpKind, "shiftOp");
                return false;
            }
            (*yynode)->shiftOpListSequence = snoc((*yynode)->shiftOpListSequence, __node_137, memoryPool);

            ArithExprAst *__node_138 = 0;
            if (!parseArithExpr(&__node_138))
            {
                expectedSymbol(AstNode::ArithExprKind, "arithExpr");
                return false;
            }
            (*yynode)->arithExprListSequence = snoc((*yynode)->arithExprListSequence, __node_138, memoryPool);

        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseShiftOp(ShiftOpAst **yynode)
{
    *yynode = create<ShiftOpAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_LSHIFT
        || yytoken == Token_RSHIFT)
    {
        if (yytoken == Token_LSHIFT)
        {
            if (yytoken != Token_LSHIFT)
            {
                expectedToken(yytoken, Token_LSHIFT, "lshift");
                return false;
            }
            yylex();

            (*yynode)->shiftOp = PythonParser::LeftShiftOp;
        }
        else if (yytoken == Token_RSHIFT)
        {
            if (yytoken != Token_RSHIFT)
            {
                expectedToken(yytoken, Token_RSHIFT, "rshift");
                return false;
            }
            yylex();

            (*yynode)->shiftOp = PythonParser::RightShiftOp;
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseSimpleStmt(SimpleStmtAst **yynode)
{
    *yynode = create<SimpleStmtAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_FLOAT
        || yytoken == Token_STRINGLITERAL
        || yytoken == Token_PRINT
        || yytoken == Token_YIELD
        || yytoken == Token_EXEC
        || yytoken == Token_MINUS
        || yytoken == Token_GLOBAL
        || yytoken == Token_BACKTICK
        || yytoken == Token_RETURN
        || yytoken == Token_LBRACE
        || yytoken == Token_IMAGNUM
        || yytoken == Token_IDENTIFIER
        || yytoken == Token_IMPORT
        || yytoken == Token_TILDE
        || yytoken == Token_NOT
        || yytoken == Token_BREAK
        || yytoken == Token_FROM
        || yytoken == Token_RAISE
        || yytoken == Token_DEL
        || yytoken == Token_LPAREN
        || yytoken == Token_INTEGER
        || yytoken == Token_PASS
        || yytoken == Token_CONTINUE
        || yytoken == Token_PLUS
        || yytoken == Token_LAMBDA
        || yytoken == Token_ASSERT
        || yytoken == Token_LBRACKET)
    {
        SmallStmtAst *__node_139 = 0;
        if (!parseSmallStmt(&__node_139))
        {
            expectedSymbol(AstNode::SmallStmtKind, "smallStmt");
            return false;
        }
        (*yynode)->smallStmtSequence = snoc((*yynode)->smallStmtSequence, __node_139, memoryPool);

        while (yytoken == Token_SEMICOLON)
        {
            if (yytoken != Token_SEMICOLON)
            {
                expectedToken(yytoken, Token_SEMICOLON, "semicolon");
                return false;
            }
            yylex();

            if ( yytoken == Token_LINEBREAK || yytoken == Token_DEDENT)
            {
                break;
            }
            SmallStmtAst *__node_140 = 0;
            if (!parseSmallStmt(&__node_140))
            {
                expectedSymbol(AstNode::SmallStmtKind, "smallStmt");
                return false;
            }
            (*yynode)->smallStmtSequence = snoc((*yynode)->smallStmtSequence, __node_140, memoryPool);

        }
        if (yytoken != Token_LINEBREAK)
        {
            expectedToken(yytoken, Token_LINEBREAK, "linebreak");
            return false;
        }
        yylex();

    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseSmallStmt(SmallStmtAst **yynode)
{
    *yynode = create<SmallStmtAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_FLOAT
        || yytoken == Token_STRINGLITERAL
        || yytoken == Token_PRINT
        || yytoken == Token_YIELD
        || yytoken == Token_EXEC
        || yytoken == Token_MINUS
        || yytoken == Token_GLOBAL
        || yytoken == Token_BACKTICK
        || yytoken == Token_RETURN
        || yytoken == Token_LBRACE
        || yytoken == Token_IMAGNUM
        || yytoken == Token_IDENTIFIER
        || yytoken == Token_IMPORT
        || yytoken == Token_TILDE
        || yytoken == Token_NOT
        || yytoken == Token_BREAK
        || yytoken == Token_FROM
        || yytoken == Token_RAISE
        || yytoken == Token_DEL
        || yytoken == Token_LPAREN
        || yytoken == Token_INTEGER
        || yytoken == Token_PASS
        || yytoken == Token_CONTINUE
        || yytoken == Token_PLUS
        || yytoken == Token_LAMBDA
        || yytoken == Token_ASSERT
        || yytoken == Token_LBRACKET)
    {
        if (yytoken == Token_NOT
            || yytoken == Token_LBRACE
            || yytoken == Token_STRINGLITERAL
            || yytoken == Token_FLOAT
            || yytoken == Token_TILDE
            || yytoken == Token_BACKTICK
            || yytoken == Token_LAMBDA
            || yytoken == Token_LBRACKET
            || yytoken == Token_INTEGER
            || yytoken == Token_MINUS
            || yytoken == Token_LPAREN
            || yytoken == Token_IDENTIFIER
            || yytoken == Token_PLUS
            || yytoken == Token_IMAGNUM)
        {
            ExprStmtAst *__node_141 = 0;
            if (!parseExprStmt(&__node_141))
            {
                expectedSymbol(AstNode::ExprStmtKind, "exprStmt");
                return false;
            }
            (*yynode)->exprStmt = __node_141;

        }
        else if (yytoken == Token_PRINT)
        {
            PrintStmtAst *__node_142 = 0;
            if (!parsePrintStmt(&__node_142))
            {
                expectedSymbol(AstNode::PrintStmtKind, "printStmt");
                return false;
            }
            (*yynode)->printStmt = __node_142;

        }
        else if (yytoken == Token_DEL)
        {
            DelStmtAst *__node_143 = 0;
            if (!parseDelStmt(&__node_143))
            {
                expectedSymbol(AstNode::DelStmtKind, "delStmt");
                return false;
            }
            (*yynode)->delStmt = __node_143;

        }
        else if (yytoken == Token_PASS)
        {
            PassStmtAst *__node_144 = 0;
            if (!parsePassStmt(&__node_144))
            {
                expectedSymbol(AstNode::PassStmtKind, "passStmt");
                return false;
            }
            (*yynode)->passStmt = __node_144;

        }
        else if (yytoken == Token_RETURN
                 || yytoken == Token_RAISE
                 || yytoken == Token_YIELD
                 || yytoken == Token_BREAK
                 || yytoken == Token_CONTINUE)
        {
            FlowStmtAst *__node_145 = 0;
            if (!parseFlowStmt(&__node_145))
            {
                expectedSymbol(AstNode::FlowStmtKind, "flowStmt");
                return false;
            }
            (*yynode)->flowStmt = __node_145;

        }
        else if (yytoken == Token_IMPORT
                 || yytoken == Token_FROM)
        {
            ImportStmtAst *__node_146 = 0;
            if (!parseImportStmt(&__node_146))
            {
                expectedSymbol(AstNode::ImportStmtKind, "importStmt");
                return false;
            }
            (*yynode)->importStmt = __node_146;

        }
        else if (yytoken == Token_GLOBAL)
        {
            GlobalStmtAst *__node_147 = 0;
            if (!parseGlobalStmt(&__node_147))
            {
                expectedSymbol(AstNode::GlobalStmtKind, "globalStmt");
                return false;
            }
            (*yynode)->globalStmt = __node_147;

        }
        else if (yytoken == Token_EXEC)
        {
            ExecStmtAst *__node_148 = 0;
            if (!parseExecStmt(&__node_148))
            {
                expectedSymbol(AstNode::ExecStmtKind, "execStmt");
                return false;
            }
            (*yynode)->execStmt = __node_148;

        }
        else if (yytoken == Token_ASSERT)
        {
            AssertStmtAst *__node_149 = 0;
            if (!parseAssertStmt(&__node_149))
            {
                expectedSymbol(AstNode::AssertStmtKind, "assertStmt");
                return false;
            }
            (*yynode)->assertStmt = __node_149;

        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseStmt(StmtAst **yynode)
{
    *yynode = create<StmtAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_FLOAT
        || yytoken == Token_STRINGLITERAL
        || yytoken == Token_PRINT
        || yytoken == Token_YIELD
        || yytoken == Token_EXEC
        || yytoken == Token_MINUS
        || yytoken == Token_CLASS
        || yytoken == Token_GLOBAL
        || yytoken == Token_BACKTICK
        || yytoken == Token_RETURN
        || yytoken == Token_LBRACE
        || yytoken == Token_IMAGNUM
        || yytoken == Token_IDENTIFIER
        || yytoken == Token_DEF
        || yytoken == Token_IMPORT
        || yytoken == Token_WHILE
        || yytoken == Token_TILDE
        || yytoken == Token_NOT
        || yytoken == Token_BREAK
        || yytoken == Token_FROM
        || yytoken == Token_RAISE
        || yytoken == Token_DEL
        || yytoken == Token_LPAREN
        || yytoken == Token_INTEGER
        || yytoken == Token_LINEBREAK
        || yytoken == Token_PASS
        || yytoken == Token_CONTINUE
        || yytoken == Token_IF
        || yytoken == Token_PLUS
        || yytoken == Token_TRY
        || yytoken == Token_AT
        || yytoken == Token_LAMBDA
        || yytoken == Token_ASSERT
        || yytoken == Token_LBRACKET
        || yytoken == Token_FOR)
    {
        if (yytoken == Token_FLOAT
            || yytoken == Token_STRINGLITERAL
            || yytoken == Token_PRINT
            || yytoken == Token_YIELD
            || yytoken == Token_EXEC
            || yytoken == Token_MINUS
            || yytoken == Token_GLOBAL
            || yytoken == Token_BACKTICK
            || yytoken == Token_RETURN
            || yytoken == Token_LBRACE
            || yytoken == Token_IMAGNUM
            || yytoken == Token_IDENTIFIER
            || yytoken == Token_IMPORT
            || yytoken == Token_TILDE
            || yytoken == Token_NOT
            || yytoken == Token_BREAK
            || yytoken == Token_FROM
            || yytoken == Token_RAISE
            || yytoken == Token_DEL
            || yytoken == Token_LPAREN
            || yytoken == Token_INTEGER
            || yytoken == Token_PASS
            || yytoken == Token_CONTINUE
            || yytoken == Token_PLUS
            || yytoken == Token_LAMBDA
            || yytoken == Token_ASSERT
            || yytoken == Token_LBRACKET)
        {
            SimpleStmtAst *__node_150 = 0;
            if (!parseSimpleStmt(&__node_150))
            {
                expectedSymbol(AstNode::SimpleStmtKind, "simpleStmt");
                return false;
            }
            (*yynode)->simpleStmt = __node_150;

        }
        else if (yytoken == Token_WHILE
                 || yytoken == Token_FOR
                 || yytoken == Token_CLASS
                 || yytoken == Token_DEF
                 || yytoken == Token_AT
                 || yytoken == Token_TRY
                 || yytoken == Token_IF)
        {
            CompoundStmtAst *__node_151 = 0;
            if (!parseCompoundStmt(&__node_151))
            {
                expectedSymbol(AstNode::CompoundStmtKind, "compoundStmt");
                return false;
            }
            (*yynode)->compoundStmt = __node_151;

        }
        else if (yytoken == Token_LINEBREAK)
        {
            if (yytoken != Token_LINEBREAK)
            {
                expectedToken(yytoken, Token_LINEBREAK, "linebreak");
                return false;
            }
            yylex();

        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseSubscript(SubscriptAst **yynode)
{
    *yynode = create<SubscriptAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_FLOAT
        || yytoken == Token_STRINGLITERAL
        || yytoken == Token_MINUS
        || yytoken == Token_BACKTICK
        || yytoken == Token_LBRACE
        || yytoken == Token_IMAGNUM
        || yytoken == Token_IDENTIFIER
        || yytoken == Token_TILDE
        || yytoken == Token_NOT
        || yytoken == Token_ELLIPSIS
        || yytoken == Token_COLON
        || yytoken == Token_LPAREN
        || yytoken == Token_INTEGER
        || yytoken == Token_PLUS
        || yytoken == Token_LAMBDA
        || yytoken == Token_LBRACKET || yytoken == Token_RBRACKET
        || yytoken == Token_EOF
        || yytoken == Token_COMMA)
    {
        (*yynode)->isEllipsis = false;
        (*yynode)->hasColon = false;
        if (yytoken == Token_ELLIPSIS)
        {
            if (yytoken != Token_ELLIPSIS)
            {
                expectedToken(yytoken, Token_ELLIPSIS, "ellipsis");
                return false;
            }
            yylex();

            (*yynode)->isEllipsis = true;
        }
        else if (yytoken == Token_COLON
                 || yytoken == Token_NOT
                 || yytoken == Token_LBRACE
                 || yytoken == Token_STRINGLITERAL
                 || yytoken == Token_FLOAT
                 || yytoken == Token_TILDE
                 || yytoken == Token_BACKTICK
                 || yytoken == Token_LAMBDA
                 || yytoken == Token_LBRACKET
                 || yytoken == Token_INTEGER
                 || yytoken == Token_MINUS
                 || yytoken == Token_LPAREN
                 || yytoken == Token_IDENTIFIER
                 || yytoken == Token_PLUS
                 || yytoken == Token_IMAGNUM)
        {
            if ((yytoken == Token_NOT
                 || yytoken == Token_LBRACE
                 || yytoken == Token_STRINGLITERAL
                 || yytoken == Token_FLOAT
                 || yytoken == Token_TILDE
                 || yytoken == Token_BACKTICK
                 || yytoken == Token_LAMBDA
                 || yytoken == Token_LBRACKET
                 || yytoken == Token_INTEGER
                 || yytoken == Token_MINUS
                 || yytoken == Token_LPAREN
                 || yytoken == Token_IDENTIFIER
                 || yytoken == Token_PLUS
                 || yytoken == Token_IMAGNUM) && ( yytoken != Token_COLON ))
            {
                TestAst *__node_152 = 0;
                if (!parseTest(&__node_152))
                {
                    expectedSymbol(AstNode::TestKind, "test");
                    return false;
                }
                (*yynode)->begin = __node_152;

            }
            else if (true /*epsilon*/)
            {
            }
            else
            {
                return false;
            }
            if ((true /*epsilon*/) && ( yytoken == Token_RBRACKET || yytoken == Token_COMMA ))
            {
            }
            else if (yytoken == Token_COLON)
            {
                if (yytoken != Token_COLON)
                {
                    expectedToken(yytoken, Token_COLON, "colon");
                    return false;
                }
                yylex();

                (*yynode)->hasColon = true;
                if (yytoken == Token_NOT
                    || yytoken == Token_LBRACE
                    || yytoken == Token_STRINGLITERAL
                    || yytoken == Token_FLOAT
                    || yytoken == Token_TILDE
                    || yytoken == Token_BACKTICK
                    || yytoken == Token_LAMBDA
                    || yytoken == Token_LBRACKET
                    || yytoken == Token_INTEGER
                    || yytoken == Token_MINUS
                    || yytoken == Token_LPAREN
                    || yytoken == Token_IDENTIFIER
                    || yytoken == Token_PLUS
                    || yytoken == Token_IMAGNUM)
                {
                    TestAst *__node_153 = 0;
                    if (!parseTest(&__node_153))
                    {
                        expectedSymbol(AstNode::TestKind, "test");
                        return false;
                    }
                    (*yynode)->end = __node_153;

                }
                else if (true /*epsilon*/)
                {
                }
                else
                {
                    return false;
                }
                if (yytoken == Token_COLON)
                {
                    if (yytoken != Token_COLON)
                    {
                        expectedToken(yytoken, Token_COLON, "colon");
                        return false;
                    }
                    yylex();

                    (*yynode)->hasColon = true;
                    if (yytoken == Token_NOT
                        || yytoken == Token_LBRACE
                        || yytoken == Token_STRINGLITERAL
                        || yytoken == Token_FLOAT
                        || yytoken == Token_TILDE
                        || yytoken == Token_BACKTICK
                        || yytoken == Token_LAMBDA
                        || yytoken == Token_LBRACKET
                        || yytoken == Token_INTEGER
                        || yytoken == Token_MINUS
                        || yytoken == Token_LPAREN
                        || yytoken == Token_IDENTIFIER
                        || yytoken == Token_PLUS
                        || yytoken == Token_IMAGNUM)
                    {
                        TestAst *__node_154 = 0;
                        if (!parseTest(&__node_154))
                        {
                            expectedSymbol(AstNode::TestKind, "test");
                            return false;
                        }
                        (*yynode)->step = __node_154;

                    }
                    else if (true /*epsilon*/)
                    {
                    }
                    else
                    {
                        return false;
                    }
                }
                else if (true /*epsilon*/)
                {
                }
                else
                {
                    return false;
                }
            }
            else
            {
                return false;
            }
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseSubscriptlist(SubscriptlistAst **yynode)
{
    *yynode = create<SubscriptlistAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_FLOAT
        || yytoken == Token_STRINGLITERAL
        || yytoken == Token_MINUS
        || yytoken == Token_BACKTICK
        || yytoken == Token_LBRACE
        || yytoken == Token_IMAGNUM
        || yytoken == Token_IDENTIFIER
        || yytoken == Token_TILDE
        || yytoken == Token_NOT
        || yytoken == Token_ELLIPSIS
        || yytoken == Token_COLON
        || yytoken == Token_COMMA
        || yytoken == Token_LPAREN
        || yytoken == Token_INTEGER
        || yytoken == Token_PLUS
        || yytoken == Token_LAMBDA
        || yytoken == Token_LBRACKET || yytoken == Token_RBRACKET
        || yytoken == Token_EOF)
    {
        SubscriptAst *__node_155 = 0;
        if (!parseSubscript(&__node_155))
        {
            expectedSymbol(AstNode::SubscriptKind, "subscript");
            return false;
        }
        (*yynode)->subscriptSequence = snoc((*yynode)->subscriptSequence, __node_155, memoryPool);

        while (yytoken == Token_COMMA)
        {
            if (yytoken != Token_COMMA)
            {
                expectedToken(yytoken, Token_COMMA, "comma");
                return false;
            }
            yylex();

            (*yynode)->hasComma = true;
            if (yytoken == Token_RBRACKET)
            {
                break;
            }
            SubscriptAst *__node_156 = 0;
            if (!parseSubscript(&__node_156))
            {
                expectedSymbol(AstNode::SubscriptKind, "subscript");
                return false;
            }
            (*yynode)->subscriptSequence = snoc((*yynode)->subscriptSequence, __node_156, memoryPool);

        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseSuite(SuiteAst **yynode)
{
    *yynode = create<SuiteAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_FLOAT
        || yytoken == Token_STRINGLITERAL
        || yytoken == Token_PRINT
        || yytoken == Token_YIELD
        || yytoken == Token_EXEC
        || yytoken == Token_MINUS
        || yytoken == Token_GLOBAL
        || yytoken == Token_BACKTICK
        || yytoken == Token_RETURN
        || yytoken == Token_LBRACE
        || yytoken == Token_IMAGNUM
        || yytoken == Token_IDENTIFIER
        || yytoken == Token_IMPORT
        || yytoken == Token_TILDE
        || yytoken == Token_NOT
        || yytoken == Token_BREAK
        || yytoken == Token_FROM
        || yytoken == Token_RAISE
        || yytoken == Token_DEL
        || yytoken == Token_LPAREN
        || yytoken == Token_INTEGER
        || yytoken == Token_LINEBREAK
        || yytoken == Token_PASS
        || yytoken == Token_CONTINUE
        || yytoken == Token_PLUS
        || yytoken == Token_LAMBDA
        || yytoken == Token_ASSERT
        || yytoken == Token_LBRACKET)
    {
        if (yytoken == Token_FLOAT
            || yytoken == Token_STRINGLITERAL
            || yytoken == Token_PRINT
            || yytoken == Token_YIELD
            || yytoken == Token_EXEC
            || yytoken == Token_MINUS
            || yytoken == Token_GLOBAL
            || yytoken == Token_BACKTICK
            || yytoken == Token_RETURN
            || yytoken == Token_LBRACE
            || yytoken == Token_IMAGNUM
            || yytoken == Token_IDENTIFIER
            || yytoken == Token_IMPORT
            || yytoken == Token_TILDE
            || yytoken == Token_NOT
            || yytoken == Token_BREAK
            || yytoken == Token_FROM
            || yytoken == Token_RAISE
            || yytoken == Token_DEL
            || yytoken == Token_LPAREN
            || yytoken == Token_INTEGER
            || yytoken == Token_PASS
            || yytoken == Token_CONTINUE
            || yytoken == Token_PLUS
            || yytoken == Token_LAMBDA
            || yytoken == Token_ASSERT
            || yytoken == Token_LBRACKET)
        {
            SimpleStmtAst *__node_157 = 0;
            if (!parseSimpleStmt(&__node_157))
            {
                expectedSymbol(AstNode::SimpleStmtKind, "simpleStmt");
                return false;
            }
            (*yynode)->simpleStmt = __node_157;

        }
        else if (yytoken == Token_LINEBREAK)
        {
            do
            {
                if (yytoken != Token_LINEBREAK)
                {
                    expectedToken(yytoken, Token_LINEBREAK, "linebreak");
                    return false;
                }
                yylex();

            }
            while (yytoken == Token_LINEBREAK);
            if (yytoken != Token_INDENT)
            {
                expectedToken(yytoken, Token_INDENT, "indent");
                return false;
            }
            yylex();

            do
            {
                StmtAst *__node_158 = 0;
                if (!parseStmt(&__node_158))
                {
                    expectedSymbol(AstNode::StmtKind, "stmt");
                    return false;
                }
                (*yynode)->stmtSequence = snoc((*yynode)->stmtSequence, __node_158, memoryPool);

            }
            while (yytoken == Token_FLOAT
                   || yytoken == Token_STRINGLITERAL
                   || yytoken == Token_PRINT
                   || yytoken == Token_YIELD
                   || yytoken == Token_EXEC
                   || yytoken == Token_MINUS
                   || yytoken == Token_CLASS
                   || yytoken == Token_GLOBAL
                   || yytoken == Token_BACKTICK
                   || yytoken == Token_RETURN
                   || yytoken == Token_LBRACE
                   || yytoken == Token_IMAGNUM
                   || yytoken == Token_IDENTIFIER
                   || yytoken == Token_DEF
                   || yytoken == Token_IMPORT
                   || yytoken == Token_WHILE
                   || yytoken == Token_TILDE
                   || yytoken == Token_NOT
                   || yytoken == Token_BREAK
                   || yytoken == Token_FROM
                   || yytoken == Token_RAISE
                   || yytoken == Token_DEL
                   || yytoken == Token_LPAREN
                   || yytoken == Token_INTEGER
                   || yytoken == Token_LINEBREAK
                   || yytoken == Token_PASS
                   || yytoken == Token_CONTINUE
                   || yytoken == Token_IF
                   || yytoken == Token_PLUS
                   || yytoken == Token_TRY
                   || yytoken == Token_AT
                   || yytoken == Token_LAMBDA
                   || yytoken == Token_ASSERT
                   || yytoken == Token_LBRACKET
                   || yytoken == Token_FOR);
            if (yytoken != Token_DEDENT)
            {
                expectedToken(yytoken, Token_DEDENT, "dedent");
                return false;
            }
            yylex();

        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseTerm(TermAst **yynode)
{
    *yynode = create<TermAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_LBRACE
        || yytoken == Token_STRINGLITERAL
        || yytoken == Token_FLOAT
        || yytoken == Token_TILDE
        || yytoken == Token_BACKTICK
        || yytoken == Token_LBRACKET
        || yytoken == Token_INTEGER
        || yytoken == Token_MINUS
        || yytoken == Token_LPAREN
        || yytoken == Token_IDENTIFIER
        || yytoken == Token_PLUS
        || yytoken == Token_IMAGNUM)
    {
        FactorAst *__node_159 = 0;
        if (!parseFactor(&__node_159))
        {
            expectedSymbol(AstNode::FactorKind, "factor");
            return false;
        }
        (*yynode)->factor = __node_159;

        if (yytoken == Token_SLASH
            || yytoken == Token_MODULO
            || yytoken == Token_DOUBLESLASH
            || yytoken == Token_STAR)
        {
            do
            {
                TermOpAst *__node_160 = 0;
                if (!parseTermOp(&__node_160))
                {
                    expectedSymbol(AstNode::TermOpKind, "termOp");
                    return false;
                }
                (*yynode)->termOpSequence = snoc((*yynode)->termOpSequence, __node_160, memoryPool);

                FactorAst *__node_161 = 0;
                if (!parseFactor(&__node_161))
                {
                    expectedSymbol(AstNode::FactorKind, "factor");
                    return false;
                }
                (*yynode)->factorsSequence = snoc((*yynode)->factorsSequence, __node_161, memoryPool);

            }
            while (yytoken == Token_SLASH
                   || yytoken == Token_MODULO
                   || yytoken == Token_DOUBLESLASH
                   || yytoken == Token_STAR);
        }
        else if (true /*epsilon*/)
        {
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseTermOp(TermOpAst **yynode)
{
    *yynode = create<TermOpAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_SLASH
        || yytoken == Token_MODULO
        || yytoken == Token_DOUBLESLASH
        || yytoken == Token_STAR)
    {
        if (yytoken == Token_STAR)
        {
            if (yytoken != Token_STAR)
            {
                expectedToken(yytoken, Token_STAR, "star");
                return false;
            }
            yylex();

            (*yynode)->op = PythonParser::StarOp;
        }
        else if (yytoken == Token_SLASH)
        {
            if (yytoken != Token_SLASH)
            {
                expectedToken(yytoken, Token_SLASH, "slash");
                return false;
            }
            yylex();

            (*yynode)->op = PythonParser::SlashOp;
        }
        else if (yytoken == Token_MODULO)
        {
            if (yytoken != Token_MODULO)
            {
                expectedToken(yytoken, Token_MODULO, "modulo");
                return false;
            }
            yylex();

            (*yynode)->op = PythonParser::ModuloOp;
        }
        else if (yytoken == Token_DOUBLESLASH)
        {
            if (yytoken != Token_DOUBLESLASH)
            {
                expectedToken(yytoken, Token_DOUBLESLASH, "doubleslash");
                return false;
            }
            yylex();

            (*yynode)->op = PythonParser::DoubleSlashOp;
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseTest(TestAst **yynode)
{
    *yynode = create<TestAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_NOT
        || yytoken == Token_LBRACE
        || yytoken == Token_STRINGLITERAL
        || yytoken == Token_FLOAT
        || yytoken == Token_TILDE
        || yytoken == Token_BACKTICK
        || yytoken == Token_LAMBDA
        || yytoken == Token_LBRACKET
        || yytoken == Token_INTEGER
        || yytoken == Token_MINUS
        || yytoken == Token_LPAREN
        || yytoken == Token_IDENTIFIER
        || yytoken == Token_PLUS
        || yytoken == Token_IMAGNUM)
    {
        if (yytoken == Token_NOT
            || yytoken == Token_LBRACE
            || yytoken == Token_STRINGLITERAL
            || yytoken == Token_FLOAT
            || yytoken == Token_TILDE
            || yytoken == Token_BACKTICK
            || yytoken == Token_LBRACKET
            || yytoken == Token_INTEGER
            || yytoken == Token_MINUS
            || yytoken == Token_LPAREN
            || yytoken == Token_IDENTIFIER
            || yytoken == Token_PLUS
            || yytoken == Token_IMAGNUM)
        {
            AndTestAst *__node_162 = 0;
            if (!parseAndTest(&__node_162))
            {
                expectedSymbol(AstNode::AndTestKind, "andTest");
                return false;
            }
            (*yynode)->andTestSequence = snoc((*yynode)->andTestSequence, __node_162, memoryPool);

            while (yytoken == Token_OR)
            {
                if (yytoken != Token_OR)
                {
                    expectedToken(yytoken, Token_OR, "or");
                    return false;
                }
                yylex();

                AndTestAst *__node_163 = 0;
                if (!parseAndTest(&__node_163))
                {
                    expectedSymbol(AstNode::AndTestKind, "andTest");
                    return false;
                }
                (*yynode)->andTestSequence = snoc((*yynode)->andTestSequence, __node_163, memoryPool);

            }
        }
        else if (yytoken == Token_LAMBDA)
        {
            LambdaDefAst *__node_164 = 0;
            if (!parseLambdaDef(&__node_164))
            {
                expectedSymbol(AstNode::LambdaDefKind, "lambdaDef");
                return false;
            }
            (*yynode)->lambdaDef = __node_164;

        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseTestlist(TestlistAst **yynode)
{
    *yynode = create<TestlistAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_NOT
        || yytoken == Token_LBRACE
        || yytoken == Token_STRINGLITERAL
        || yytoken == Token_FLOAT
        || yytoken == Token_TILDE
        || yytoken == Token_BACKTICK
        || yytoken == Token_LAMBDA
        || yytoken == Token_LBRACKET
        || yytoken == Token_INTEGER
        || yytoken == Token_MINUS
        || yytoken == Token_LPAREN
        || yytoken == Token_IDENTIFIER
        || yytoken == Token_PLUS
        || yytoken == Token_IMAGNUM)
    {
        TestAst *__node_165 = 0;
        if (!parseTest(&__node_165))
        {
            expectedSymbol(AstNode::TestKind, "test");
            return false;
        }
        (*yynode)->testsSequence = snoc((*yynode)->testsSequence, __node_165, memoryPool);

        while (yytoken == Token_COMMA)
        {
            if (yytoken != Token_COMMA)
            {
                expectedToken(yytoken, Token_COMMA, "comma");
                return false;
            }
            yylex();

            if ( yytoken == Token_COLON || yytoken == Token_SEMICOLON || yytoken == Token_RPAREN || yytoken == Token_LINEBREAK)
            {
                break;
            }
            TestAst *__node_166 = 0;
            if (!parseTest(&__node_166))
            {
                expectedSymbol(AstNode::TestKind, "test");
                return false;
            }
            (*yynode)->testsSequence = snoc((*yynode)->testsSequence, __node_166, memoryPool);

        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseTestlistSafe(TestlistSafeAst **yynode)
{
    *yynode = create<TestlistSafeAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_NOT
        || yytoken == Token_LBRACE
        || yytoken == Token_STRINGLITERAL
        || yytoken == Token_FLOAT
        || yytoken == Token_TILDE
        || yytoken == Token_BACKTICK
        || yytoken == Token_LAMBDA
        || yytoken == Token_LBRACKET
        || yytoken == Token_INTEGER
        || yytoken == Token_MINUS
        || yytoken == Token_LPAREN
        || yytoken == Token_IDENTIFIER
        || yytoken == Token_PLUS
        || yytoken == Token_IMAGNUM)
    {
        TestAst *__node_167 = 0;
        if (!parseTest(&__node_167))
        {
            expectedSymbol(AstNode::TestKind, "test");
            return false;
        }
        (*yynode)->testSequence = snoc((*yynode)->testSequence, __node_167, memoryPool);

        if (yytoken == Token_COMMA)
        {
            do
            {
                if (yytoken != Token_COMMA)
                {
                    expectedToken(yytoken, Token_COMMA, "comma");
                    return false;
                }
                yylex();

                TestAst *__node_168 = 0;
                if (!parseTest(&__node_168))
                {
                    expectedSymbol(AstNode::TestKind, "test");
                    return false;
                }
                (*yynode)->testSequence = snoc((*yynode)->testSequence, __node_168, memoryPool);

            }
            while (yytoken == Token_COMMA);
            if (yytoken == Token_COMMA)
            {
                if (yytoken != Token_COMMA)
                {
                    expectedToken(yytoken, Token_COMMA, "comma");
                    return false;
                }
                yylex();

            }
            else if (true /*epsilon*/)
            {
            }
            else
            {
                return false;
            }
        }
        else if (true /*epsilon*/)
        {
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseTrailer(TrailerAst **yynode)
{
    *yynode = create<TrailerAst>();

    (*yynode)->startToken = tokenStream->index() - 1;
    (*yynode)->trailerDotName = -1;

    if (yytoken == Token_LBRACKET
        || yytoken == Token_LPAREN
        || yytoken == Token_DOT)
    {
        if (yytoken == Token_LPAREN)
        {
            if (yytoken != Token_LPAREN)
            {
                expectedToken(yytoken, Token_LPAREN, "lparen");
                return false;
            }
            yylex();

            if (yytoken == Token_NOT
                || yytoken == Token_LBRACE
                || yytoken == Token_STRINGLITERAL
                || yytoken == Token_FLOAT
                || yytoken == Token_TILDE
                || yytoken == Token_BACKTICK
                || yytoken == Token_LAMBDA
                || yytoken == Token_LBRACKET
                || yytoken == Token_DOUBLESTAR
                || yytoken == Token_INTEGER
                || yytoken == Token_MINUS
                || yytoken == Token_LPAREN
                || yytoken == Token_STAR
                || yytoken == Token_IDENTIFIER
                || yytoken == Token_PLUS
                || yytoken == Token_IMAGNUM)
            {
                ArglistAst *__node_169 = 0;
                if (!parseArglist(&__node_169))
                {
                    expectedSymbol(AstNode::ArglistKind, "arglist");
                    return false;
                }
                (*yynode)->trailerArglist = __node_169;

            }
            else if (true /*epsilon*/)
            {
            }
            else
            {
                return false;
            }
            if (yytoken != Token_RPAREN)
            {
                expectedToken(yytoken, Token_RPAREN, "rparen");
                return false;
            }
            yylex();

        }
        else if (yytoken == Token_LBRACKET)
        {
            if (yytoken != Token_LBRACKET)
            {
                expectedToken(yytoken, Token_LBRACKET, "lbracket");
                return false;
            }
            yylex();

            SubscriptlistAst *__node_170 = 0;
            if (!parseSubscriptlist(&__node_170))
            {
                expectedSymbol(AstNode::SubscriptlistKind, "subscriptlist");
                return false;
            }
            (*yynode)->subscriptlist = __node_170;

            if (yytoken != Token_RBRACKET)
            {
                expectedToken(yytoken, Token_RBRACKET, "rbracket");
                return false;
            }
            yylex();

        }
        else if (yytoken == Token_DOT)
        {
            if (yytoken != Token_DOT)
            {
                expectedToken(yytoken, Token_DOT, "dot");
                return false;
            }
            yylex();

            if (yytoken != Token_IDENTIFIER)
            {
                expectedToken(yytoken, Token_IDENTIFIER, "identifier");
                return false;
            }
            (*yynode)->trailerDotName = tokenStream->index() - 1;
            yylex();

        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseTryStmt(TryStmtAst **yynode)
{
    *yynode = create<TryStmtAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_TRY)
    {
        if (yytoken != Token_TRY)
        {
            expectedToken(yytoken, Token_TRY, "try");
            return false;
        }
        yylex();

        if (yytoken != Token_COLON)
        {
            expectedToken(yytoken, Token_COLON, "colon");
            return false;
        }
        yylex();

        SuiteAst *__node_171 = 0;
        if (!parseSuite(&__node_171))
        {
            expectedSymbol(AstNode::SuiteKind, "suite");
            return false;
        }
        (*yynode)->trySuite = __node_171;

        if (yytoken == Token_EXCEPT)
        {
            do
            {
                ExceptClauseAst *__node_172 = 0;
                if (!parseExceptClause(&__node_172))
                {
                    expectedSymbol(AstNode::ExceptClauseKind, "exceptClause");
                    return false;
                }
                (*yynode)->exceptClauseSequence = snoc((*yynode)->exceptClauseSequence, __node_172, memoryPool);

                if (yytoken != Token_COLON)
                {
                    expectedToken(yytoken, Token_COLON, "colon");
                    return false;
                }
                yylex();

                SuiteAst *__node_173 = 0;
                if (!parseSuite(&__node_173))
                {
                    expectedSymbol(AstNode::SuiteKind, "suite");
                    return false;
                }
                (*yynode)->exceptSuiteSequence = snoc((*yynode)->exceptSuiteSequence, __node_173, memoryPool);

            }
            while (yytoken == Token_EXCEPT);
            if (yytoken == Token_ELSE)
            {
                if (yytoken != Token_ELSE)
                {
                    expectedToken(yytoken, Token_ELSE, "else");
                    return false;
                }
                yylex();

                if (yytoken != Token_COLON)
                {
                    expectedToken(yytoken, Token_COLON, "colon");
                    return false;
                }
                yylex();

                SuiteAst *__node_174 = 0;
                if (!parseSuite(&__node_174))
                {
                    expectedSymbol(AstNode::SuiteKind, "suite");
                    return false;
                }
                (*yynode)->tryElseSuite = __node_174;

            }
            else if (true /*epsilon*/)
            {
            }
            else
            {
                return false;
            }
        }
        else if (yytoken == Token_FINALLY)
        {
            if (yytoken != Token_FINALLY)
            {
                expectedToken(yytoken, Token_FINALLY, "finally");
                return false;
            }
            yylex();

            if (yytoken != Token_COLON)
            {
                expectedToken(yytoken, Token_COLON, "colon");
                return false;
            }
            yylex();

            SuiteAst *__node_175 = 0;
            if (!parseSuite(&__node_175))
            {
                expectedSymbol(AstNode::SuiteKind, "suite");
                return false;
            }
            (*yynode)->finallySuite = __node_175;

        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseVarargslist(VarargslistAst **yynode)
{
    *yynode = create<VarargslistAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_DOUBLESTAR
        || yytoken == Token_LPAREN
        || yytoken == Token_STAR
        || yytoken == Token_IDENTIFIER || yytoken == Token_COLON
        || yytoken == Token_EOF
        || yytoken == Token_RPAREN)
    {
        if (yytoken == Token_LPAREN
            || yytoken == Token_IDENTIFIER)
        {
            FuncDefAst *__node_176 = 0;
            if (!parseFuncDef(&__node_176))
            {
                expectedSymbol(AstNode::FuncDefKind, "funcDef");
                return false;
            }
            (*yynode)->funcDef = __node_176;

        }
        else if (true /*epsilon*/)
        {
        }
        else
        {
            return false;
        }
        if ((yytoken == Token_DOUBLESTAR
             || yytoken == Token_STAR) && ( yytoken != Token_RPAREN  && LA(2).kind == Token_IDENTIFIER))
        {
            FunPosParamAst *__node_177 = 0;
            if (!parseFunPosParam(&__node_177))
            {
                expectedSymbol(AstNode::FunPosParamKind, "funPosParam");
                return false;
            }
            (*yynode)->funPosParam = __node_177;

        }
        else if (true /*epsilon*/)
        {
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseWhileStmt(WhileStmtAst **yynode)
{
    *yynode = create<WhileStmtAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_WHILE)
    {
        if (yytoken != Token_WHILE)
        {
            expectedToken(yytoken, Token_WHILE, "while");
            return false;
        }
        yylex();

        TestAst *__node_178 = 0;
        if (!parseTest(&__node_178))
        {
            expectedSymbol(AstNode::TestKind, "test");
            return false;
        }
        (*yynode)->whileTest = __node_178;

        if (yytoken != Token_COLON)
        {
            expectedToken(yytoken, Token_COLON, "colon");
            return false;
        }
        yylex();

        SuiteAst *__node_179 = 0;
        if (!parseSuite(&__node_179))
        {
            expectedSymbol(AstNode::SuiteKind, "suite");
            return false;
        }
        (*yynode)->whileSuite = __node_179;

        if (yytoken == Token_ELSE)
        {
            if (yytoken != Token_ELSE)
            {
                expectedToken(yytoken, Token_ELSE, "else");
                return false;
            }
            yylex();

            if (yytoken != Token_COLON)
            {
                expectedToken(yytoken, Token_COLON, "colon");
                return false;
            }
            yylex();

            SuiteAst *__node_180 = 0;
            if (!parseSuite(&__node_180))
            {
                expectedSymbol(AstNode::SuiteKind, "suite");
                return false;
            }
            (*yynode)->whileElseSuite = __node_180;

        }
        else if (true /*epsilon*/)
        {
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseXorExpr(XorExprAst **yynode)
{
    *yynode = create<XorExprAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_LBRACE
        || yytoken == Token_STRINGLITERAL
        || yytoken == Token_FLOAT
        || yytoken == Token_TILDE
        || yytoken == Token_BACKTICK
        || yytoken == Token_LBRACKET
        || yytoken == Token_INTEGER
        || yytoken == Token_MINUS
        || yytoken == Token_LPAREN
        || yytoken == Token_IDENTIFIER
        || yytoken == Token_PLUS
        || yytoken == Token_IMAGNUM)
    {
        AndExprAst *__node_181 = 0;
        if (!parseAndExpr(&__node_181))
        {
            expectedSymbol(AstNode::AndExprKind, "andExpr");
            return false;
        }
        (*yynode)->xorExpr = __node_181;

        while (yytoken == Token_BITXOR)
        {
            if (yytoken != Token_BITXOR)
            {
                expectedToken(yytoken, Token_BITXOR, "bitxor");
                return false;
            }
            yylex();

            AndExprAst *__node_182 = 0;
            if (!parseAndExpr(&__node_182))
            {
                expectedSymbol(AstNode::AndExprKind, "andExpr");
                return false;
            }
            (*yynode)->hatXorExprSequence = snoc((*yynode)->hatXorExprSequence, __node_182, memoryPool);

        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseYieldExpr(YieldExprAst **yynode)
{
    *yynode = create<YieldExprAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_YIELD)
    {
        if (yytoken != Token_YIELD)
        {
            expectedToken(yytoken, Token_YIELD, "yield");
            return false;
        }
        yylex();

        if (yytoken == Token_NOT
            || yytoken == Token_LBRACE
            || yytoken == Token_STRINGLITERAL
            || yytoken == Token_FLOAT
            || yytoken == Token_TILDE
            || yytoken == Token_BACKTICK
            || yytoken == Token_LAMBDA
            || yytoken == Token_LBRACKET
            || yytoken == Token_INTEGER
            || yytoken == Token_MINUS
            || yytoken == Token_LPAREN
            || yytoken == Token_IDENTIFIER
            || yytoken == Token_PLUS
            || yytoken == Token_IMAGNUM)
        {
            TestlistAst *__node_183 = 0;
            if (!parseTestlist(&__node_183))
            {
                expectedSymbol(AstNode::TestlistKind, "testlist");
                return false;
            }
            (*yynode)->expr = __node_183;

        }
        else if (true /*epsilon*/)
        {
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}

bool Parser::parseYieldStmt(YieldStmtAst **yynode)
{
    *yynode = create<YieldStmtAst>();

    (*yynode)->startToken = tokenStream->index() - 1;

    if (yytoken == Token_YIELD)
    {
        YieldExprAst *__node_184 = 0;
        if (!parseYieldExpr(&__node_184))
        {
            expectedSymbol(AstNode::YieldExprKind, "yieldExpr");
            return false;
        }
        (*yynode)->yield = __node_184;

    }
    else
    {
        return false;
    }

    (*yynode)->endToken = tokenStream->index() - 1;

    return true;
}


} // end of namespace PythonParser

