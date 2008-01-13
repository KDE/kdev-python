// THIS FILE IS GENERATED
// WARNING! All changes made in this file will be lost!

#ifndef PYTHON_H_INCLUDED
#define PYTHON_H_INCLUDED

#include "pythonast.h"
#include <kdev-pg-memory-pool.h>
#include <kdev-pg-allocator.h>
#include <kdev-pg-token-stream.h>

#include <parserexport.h>
namespace PythonParser
{

class KDEVPYTHONPARSER_EXPORT Parser
{
public:
    typedef KDevPG::TokenStream::Token Token;
    KDevPG::TokenStream *tokenStream;
    int yytoken;

    inline Token LA(qint64 k = 1) const
    {
        return tokenStream->token(tokenStream->index() - 1 + k - 1);
    }
    inline int yylex()
    {
        return (yytoken = tokenStream->nextToken());
    }
    inline void rewind(qint64 index)
    {
        tokenStream->rewind(index);
        yylex();
    }

// token stream
    void setTokenStream(KDevPG::TokenStream *s)
    {
        tokenStream = s;
    }

// error handling
    void expectedSymbol(int kind, const QString& name);
    void expectedToken(int kind, qint64 token, const QString& name);

    bool mBlockErrors;
    inline bool blockErrors(bool block)
    {
        bool previous = mBlockErrors;
        mBlockErrors = block;
        return previous;
    }

// memory pool
    typedef KDevPG::MemoryPool memoryPoolType;

    KDevPG::MemoryPool *memoryPool;
    void setMemoryPool(KDevPG::MemoryPool *p)
    {
        memoryPool = p;
    }
    template <class T>
    inline T *create()
    {
        T *node = new (memoryPool->allocate(sizeof(T))) T();
        node->kind = T::KIND;
        return node;
    }

    enum TokenType
    {
        Token_AND = 1000,
        Token_ANDEQ = 1001,
        Token_AS = 1002,
        Token_ASSERT = 1003,
        Token_AT = 1004,
        Token_BACKTICK = 1005,
        Token_BITAND = 1006,
        Token_BITOR = 1007,
        Token_BITXOR = 1008,
        Token_BREAK = 1009,
        Token_CLASS = 1010,
        Token_COLON = 1011,
        Token_COMMA = 1012,
        Token_CONTINUE = 1013,
        Token_DEDENT = 1014,
        Token_DEF = 1015,
        Token_DEL = 1016,
        Token_DOT = 1017,
        Token_DOUBLESLASH = 1018,
        Token_DOUBLESLASHEQ = 1019,
        Token_DOUBLESTAR = 1020,
        Token_DOUBLESTAREQ = 1021,
        Token_ELIF = 1022,
        Token_ELLIPSIS = 1023,
        Token_ELSE = 1024,
        Token_EOF = 1025,
        Token_EQUAL = 1026,
        Token_EXCEPT = 1027,
        Token_EXEC = 1028,
        Token_FINALLY = 1029,
        Token_FLOAT = 1030,
        Token_FOR = 1031,
        Token_FROM = 1032,
        Token_GLOBAL = 1033,
        Token_GREATER = 1034,
        Token_GREATEREQ = 1035,
        Token_IDENTIFIER = 1036,
        Token_IF = 1037,
        Token_IMAGNUM = 1038,
        Token_IMPORT = 1039,
        Token_IN = 1040,
        Token_INDENT = 1041,
        Token_INTEGER = 1042,
        Token_INVALID = 1043,
        Token_IS = 1044,
        Token_ISEQUAL = 1045,
        Token_LAMBDA = 1046,
        Token_LBRACE = 1047,
        Token_LBRACKET = 1048,
        Token_LESS = 1049,
        Token_LESSEQ = 1050,
        Token_LINEBREAK = 1051,
        Token_LPAREN = 1052,
        Token_LSHIFT = 1053,
        Token_LSHIFTEQ = 1054,
        Token_MINUS = 1055,
        Token_MINUSEQ = 1056,
        Token_MODULO = 1057,
        Token_MODULOEQ = 1058,
        Token_NOT = 1059,
        Token_OR = 1060,
        Token_OREQ = 1061,
        Token_PASS = 1062,
        Token_PLUS = 1063,
        Token_PLUSEQ = 1064,
        Token_PRINT = 1065,
        Token_RAISE = 1066,
        Token_RBRACE = 1067,
        Token_RBRACKET = 1068,
        Token_RETURN = 1069,
        Token_RPAREN = 1070,
        Token_RSHIFT = 1071,
        Token_RSHIFTEQ = 1072,
        Token_SEMICOLON = 1073,
        Token_SLASH = 1074,
        Token_SLASHEQ = 1075,
        Token_STAR = 1076,
        Token_STAREQ = 1077,
        Token_STRINGLITERAL = 1078,
        Token_TILDE = 1079,
        Token_TILDEEQ = 1080,
        Token_TRY = 1081,
        Token_UNEQUAL = 1082,
        Token_WHILE = 1083,
        Token_YIELD = 1084,
        TokenTypeSize
    }; // TokenType

// user defined declarations:
public:

    /**
     * Transform the raw input into tokens.
     * When this method returns, the parser's token stream has been filled
     * and any parse_*() method can be called.
     */
    void tokenize( const QString& contents );

    enum ProblemType
    {
        Error,
        Warning,
        Info
    };
    void reportProblem( Parser::ProblemType type, const QString& message );
    QString tokenText(qint64 begin, qint64 end);
    void setDebug(bool debug);


private:

    QString mContents;
    bool mDebug;


public:
    Parser()
    {
        memoryPool = 0;
        tokenStream = 0;
        yytoken = Token_EOF;
        mBlockErrors = false;
    }

    virtual ~Parser() {}

    bool parseAndExpr(AndExprAst **yynode);
    bool parseAndTest(AndTestAst **yynode);
    bool parseArglist(ArglistAst **yynode);
    bool parseArgument(ArgumentAst **yynode);
    bool parseArithExpr(ArithExprAst **yynode);
    bool parseArithOp(ArithOpAst **yynode);
    bool parseAssertStmt(AssertStmtAst **yynode);
    bool parseAtom(AtomAst **yynode);
    bool parseAugassign(AugassignAst **yynode);
    bool parseBreakStmt(BreakStmtAst **yynode);
    bool parseClassdef(ClassdefAst **yynode);
    bool parseCodeexpr(CodeexprAst **yynode);
    bool parseCompOp(CompOpAst **yynode);
    bool parseComparison(ComparisonAst **yynode);
    bool parseCompoundStmt(CompoundStmtAst **yynode);
    bool parseContinueStmt(ContinueStmtAst **yynode);
    bool parseDecorator(DecoratorAst **yynode);
    bool parseDecorators(DecoratorsAst **yynode);
    bool parseDefparam(DefparamAst **yynode);
    bool parseDelStmt(DelStmtAst **yynode);
    bool parseDictmaker(DictmakerAst **yynode);
    bool parseDottedAsName(DottedAsNameAst **yynode);
    bool parseDottedAsNames(DottedAsNamesAst **yynode);
    bool parseDottedName(DottedNameAst **yynode);
    bool parseExceptClause(ExceptClauseAst **yynode);
    bool parseExecStmt(ExecStmtAst **yynode);
    bool parseExpr(ExprAst **yynode);
    bool parseExprStmt(ExprStmtAst **yynode);
    bool parseExprlist(ExprlistAst **yynode);
    bool parseFactOp(FactOpAst **yynode);
    bool parseFactor(FactorAst **yynode);
    bool parseFlowStmt(FlowStmtAst **yynode);
    bool parseForStmt(ForStmtAst **yynode);
    bool parseFpDef(FpDefAst **yynode);
    bool parseFplist(FplistAst **yynode);
    bool parseFunPosParam(FunPosParamAst **yynode);
    bool parseFuncDef(FuncDefAst **yynode);
    bool parseFuncdecl(FuncdeclAst **yynode);
    bool parseGenFor(GenForAst **yynode);
    bool parseGenIf(GenIfAst **yynode);
    bool parseGenIter(GenIterAst **yynode);
    bool parseGlobalStmt(GlobalStmtAst **yynode);
    bool parseIfStmt(IfStmtAst **yynode);
    bool parseImportAsName(ImportAsNameAst **yynode);
    bool parseImportAsNames(ImportAsNamesAst **yynode);
    bool parseImportFrom(ImportFromAst **yynode);
    bool parseImportName(ImportNameAst **yynode);
    bool parseImportStmt(ImportStmtAst **yynode);
    bool parseLambdaDef(LambdaDefAst **yynode);
    bool parseListFor(ListForAst **yynode);
    bool parseListIf(ListIfAst **yynode);
    bool parseListIter(ListIterAst **yynode);
    bool parseListMakerTest(ListMakerTestAst **yynode);
    bool parseListmaker(ListmakerAst **yynode);
    bool parseNotTest(NotTestAst **yynode);
    bool parseNumber(NumberAst **yynode);
    bool parsePassStmt(PassStmtAst **yynode);
    bool parsePlainArgumentsList(PlainArgumentsListAst **yynode);
    bool parsePower(PowerAst **yynode);
    bool parsePrintStmt(PrintStmtAst **yynode);
    bool parseProject(ProjectAst **yynode);
    bool parseRaiseStmt(RaiseStmtAst **yynode);
    bool parseReturnStmt(ReturnStmtAst **yynode);
    bool parseShiftExpr(ShiftExprAst **yynode);
    bool parseShiftOp(ShiftOpAst **yynode);
    bool parseSimpleStmt(SimpleStmtAst **yynode);
    bool parseSmallStmt(SmallStmtAst **yynode);
    bool parseStmt(StmtAst **yynode);
    bool parseSubscript(SubscriptAst **yynode);
    bool parseSubscriptlist(SubscriptlistAst **yynode);
    bool parseSuite(SuiteAst **yynode);
    bool parseTerm(TermAst **yynode);
    bool parseTermOp(TermOpAst **yynode);
    bool parseTest(TestAst **yynode);
    bool parseTestlist(TestlistAst **yynode);
    bool parseTestlistSafe(TestlistSafeAst **yynode);
    bool parseTrailer(TrailerAst **yynode);
    bool parseTryStmt(TryStmtAst **yynode);
    bool parseVarargslist(VarargslistAst **yynode);
    bool parseWhileStmt(WhileStmtAst **yynode);
    bool parseXorExpr(XorExprAst **yynode);
    bool parseYieldExpr(YieldExprAst **yynode);
    bool parseYieldStmt(YieldStmtAst **yynode);
};

} // end of namespace PythonParser

#endif

