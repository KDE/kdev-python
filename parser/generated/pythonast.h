// THIS FILE IS GENERATED
// WARNING! All changes made in this file will be lost!

#ifndef PYTHON_AST_H_INCLUDED
#define PYTHON_AST_H_INCLUDED

#include <QtCore/QList>
#include <kdev-pg-list.h>

#include <parserexport.h>


#include <QtCore/QString>

namespace PythonParser
{
class Lexer;

enum OperatorType
{
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
enum NumericType
{
    IntegerNumeric,
    FloatNumeric,
    ImaginaryNumeric
};
}

namespace PythonParser
{

struct AndExprAst;
struct AndTestAst;
struct ArglistAst;
struct ArgumentAst;
struct ArithExprAst;
struct ArithOpAst;
struct AssertStmtAst;
struct AtomAst;
struct AugassignAst;
struct BreakStmtAst;
struct ClassdefAst;
struct CodeexprAst;
struct CompOpAst;
struct ComparisonAst;
struct CompoundStmtAst;
struct ContinueStmtAst;
struct DecoratorAst;
struct DecoratorsAst;
struct DefparamAst;
struct DelStmtAst;
struct DictmakerAst;
struct DottedAsNameAst;
struct DottedAsNamesAst;
struct DottedNameAst;
struct ExceptClauseAst;
struct ExecStmtAst;
struct ExprAst;
struct ExprStmtAst;
struct ExprlistAst;
struct FactOpAst;
struct FactorAst;
struct FlowStmtAst;
struct ForStmtAst;
struct FpDefAst;
struct FplistAst;
struct FunPosParamAst;
struct FuncDefAst;
struct FuncdeclAst;
struct GenForAst;
struct GenIfAst;
struct GenIterAst;
struct GlobalStmtAst;
struct IfStmtAst;
struct ImportAsNameAst;
struct ImportAsNamesAst;
struct ImportFromAst;
struct ImportNameAst;
struct ImportStmtAst;
struct LambdaDefAst;
struct ListForAst;
struct ListIfAst;
struct ListIterAst;
struct ListMakerTestAst;
struct ListmakerAst;
struct NotTestAst;
struct NumberAst;
struct PassStmtAst;
struct PlainArgumentsListAst;
struct PowerAst;
struct PrintStmtAst;
struct ProjectAst;
struct RaiseStmtAst;
struct ReturnStmtAst;
struct ShiftExprAst;
struct ShiftOpAst;
struct SimpleStmtAst;
struct SliceopAst;
struct SmallStmtAst;
struct StmtAst;
struct SubscriptAst;
struct SubscriptlistAst;
struct SuiteAst;
struct TermAst;
struct TermOpAst;
struct TestAst;
struct TestListGexpAst;
struct TestlistAst;
struct TestlistGexpAst;
struct TestlistSafeAst;
struct TrailerAst;
struct TryStmtAst;
struct VarargslistAst;
struct WhileStmtAst;
struct XorExprAst;
struct YieldStmtAst;


struct KDEVPYTHONPARSER_EXPORT AstNode
{
    enum AstNodeKind
    {
        AndExprKind = 1000,
        AndTestKind = 1001,
        ArglistKind = 1002,
        ArgumentKind = 1003,
        ArithExprKind = 1004,
        ArithOpKind = 1005,
        AssertStmtKind = 1006,
        AtomKind = 1007,
        AugassignKind = 1008,
        BreakStmtKind = 1009,
        ClassdefKind = 1010,
        CodeexprKind = 1011,
        CompOpKind = 1012,
        ComparisonKind = 1013,
        CompoundStmtKind = 1014,
        ContinueStmtKind = 1015,
        DecoratorKind = 1016,
        DecoratorsKind = 1017,
        DefparamKind = 1018,
        DelStmtKind = 1019,
        DictmakerKind = 1020,
        DottedAsNameKind = 1021,
        DottedAsNamesKind = 1022,
        DottedNameKind = 1023,
        ExceptClauseKind = 1024,
        ExecStmtKind = 1025,
        ExprKind = 1026,
        ExprStmtKind = 1027,
        ExprlistKind = 1028,
        FactOpKind = 1029,
        FactorKind = 1030,
        FlowStmtKind = 1031,
        ForStmtKind = 1032,
        FpDefKind = 1033,
        FplistKind = 1034,
        FunPosParamKind = 1035,
        FuncDefKind = 1036,
        FuncdeclKind = 1037,
        GenForKind = 1038,
        GenIfKind = 1039,
        GenIterKind = 1040,
        GlobalStmtKind = 1041,
        IfStmtKind = 1042,
        ImportAsNameKind = 1043,
        ImportAsNamesKind = 1044,
        ImportFromKind = 1045,
        ImportNameKind = 1046,
        ImportStmtKind = 1047,
        LambdaDefKind = 1048,
        ListForKind = 1049,
        ListIfKind = 1050,
        ListIterKind = 1051,
        ListMakerTestKind = 1052,
        ListmakerKind = 1053,
        NotTestKind = 1054,
        NumberKind = 1055,
        PassStmtKind = 1056,
        PlainArgumentsListKind = 1057,
        PowerKind = 1058,
        PrintStmtKind = 1059,
        ProjectKind = 1060,
        RaiseStmtKind = 1061,
        ReturnStmtKind = 1062,
        ShiftExprKind = 1063,
        ShiftOpKind = 1064,
        SimpleStmtKind = 1065,
        SliceopKind = 1066,
        SmallStmtKind = 1067,
        StmtKind = 1068,
        SubscriptKind = 1069,
        SubscriptlistKind = 1070,
        SuiteKind = 1071,
        TermKind = 1072,
        TermOpKind = 1073,
        TestKind = 1074,
        TestListGexpKind = 1075,
        TestlistKind = 1076,
        TestlistGexpKind = 1077,
        TestlistSafeKind = 1078,
        TrailerKind = 1079,
        TryStmtKind = 1080,
        VarargslistKind = 1081,
        WhileStmtKind = 1082,
        XorExprKind = 1083,
        YieldStmtKind = 1084,
        AST_NODE_KIND_COUNT
    };

    int kind;
    qint64 startToken;
    qint64 endToken;
};

struct KDEVPYTHONPARSER_EXPORT AndExprAst: public AstNode
{
    enum { KIND = AndExprKind };

    ShiftExprAst *andExpr;
    const KDevPG::ListNode<ShiftExprAst *> *anddShifExprSequence;
};

struct KDEVPYTHONPARSER_EXPORT AndTestAst: public AstNode
{
    enum { KIND = AndTestKind };

    const KDevPG::ListNode<NotTestAst *> *notTestSequence;
};

struct KDEVPYTHONPARSER_EXPORT ArglistAst: public AstNode
{
    enum { KIND = ArglistKind };

    PlainArgumentsListAst *argListBegin;
    TestAst *arglistStar;
    TestAst *arglistDoublestar;
};

struct KDEVPYTHONPARSER_EXPORT ArgumentAst: public AstNode
{
    enum { KIND = ArgumentKind };

    TestAst *argumentTest;
    TestAst *argumentEqualTest;
    GenForAst *genFor;
};

struct KDEVPYTHONPARSER_EXPORT ArithExprAst: public AstNode
{
    enum { KIND = ArithExprKind };

    TermAst *arithTerm;
    const KDevPG::ListNode<ArithOpAst *> *arithOpListSequence;
    const KDevPG::ListNode<TermAst *> *arithTermListSequence;
};

struct KDEVPYTHONPARSER_EXPORT ArithOpAst: public AstNode
{
    enum { KIND = ArithOpKind };

    PythonParser::OperatorType arithOp;
};

struct KDEVPYTHONPARSER_EXPORT AssertStmtAst: public AstNode
{
    enum { KIND = AssertStmtKind };

    TestAst *assertNotTest;
    TestAst *assertRaiseTest;
};

struct KDEVPYTHONPARSER_EXPORT AtomAst: public AstNode
{
    enum { KIND = AtomKind };

    TestlistGexpAst *testlistGexp;
    ListmakerAst *listmaker;
    DictmakerAst *dictmaker;
    CodeexprAst *codeexpr;
    qint64 atomIdentifierName;
    NumberAst *number;
    const KDevPG::ListNode<qint64 > *stringliteralSequence;
};

struct KDEVPYTHONPARSER_EXPORT AugassignAst: public AstNode
{
    enum { KIND = AugassignKind };

    PythonParser::OperatorType assignOp;
};

struct KDEVPYTHONPARSER_EXPORT BreakStmtAst: public AstNode
{
    enum { KIND = BreakStmtKind };

};

struct KDEVPYTHONPARSER_EXPORT ClassdefAst: public AstNode
{
    enum { KIND = ClassdefKind };

    qint64 className;
    TestlistAst *testlist;
    SuiteAst *classSuite;
};

struct KDEVPYTHONPARSER_EXPORT CodeexprAst: public AstNode
{
    enum { KIND = CodeexprKind };

    const KDevPG::ListNode<TestAst *> *testSequence;
};

struct KDEVPYTHONPARSER_EXPORT CompOpAst: public AstNode
{
    enum { KIND = CompOpKind };

    PythonParser::OperatorType compOp;
};

struct KDEVPYTHONPARSER_EXPORT ComparisonAst: public AstNode
{
    enum { KIND = ComparisonKind };

    ExprAst *compExpr;
    const KDevPG::ListNode<CompOpAst *> *compOpSequence;
    const KDevPG::ListNode<ExprAst *> *compOpExprSequence;
};

struct KDEVPYTHONPARSER_EXPORT CompoundStmtAst: public AstNode
{
    enum { KIND = CompoundStmtKind };

    IfStmtAst *ifStmt;
    WhileStmtAst *whileStmt;
    ForStmtAst *forStmt;
    TryStmtAst *tryStmt;
    FuncdeclAst *funcdecl;
    ClassdefAst *classdef;
};

struct KDEVPYTHONPARSER_EXPORT ContinueStmtAst: public AstNode
{
    enum { KIND = ContinueStmtKind };

};

struct KDEVPYTHONPARSER_EXPORT DecoratorAst: public AstNode
{
    enum { KIND = DecoratorKind };

    DottedNameAst *decoratorName;
    ArglistAst *arguments;
};

struct KDEVPYTHONPARSER_EXPORT DecoratorsAst: public AstNode
{
    enum { KIND = DecoratorsKind };

    const KDevPG::ListNode<DecoratorAst *> *decoratorSequence;
};

struct KDEVPYTHONPARSER_EXPORT DefparamAst: public AstNode
{
    enum { KIND = DefparamKind };

    FplistAst *fplist;
};

struct KDEVPYTHONPARSER_EXPORT DelStmtAst: public AstNode
{
    enum { KIND = DelStmtKind };

    ExprlistAst *delList;
};

struct KDEVPYTHONPARSER_EXPORT DictmakerAst: public AstNode
{
    enum { KIND = DictmakerKind };

    const KDevPG::ListNode<TestAst *> *keyListSequence;
    const KDevPG::ListNode<TestAst *> *valueListSequence;
};

struct KDEVPYTHONPARSER_EXPORT DottedAsNameAst: public AstNode
{
    enum { KIND = DottedAsNameKind };

    DottedNameAst *importDottedName;
    qint64 importedAs;
};

struct KDEVPYTHONPARSER_EXPORT DottedAsNamesAst: public AstNode
{
    enum { KIND = DottedAsNamesKind };

    const KDevPG::ListNode<DottedAsNameAst *> *dottedAsNameSequence;
};

struct KDEVPYTHONPARSER_EXPORT DottedNameAst: public AstNode
{
    enum { KIND = DottedNameKind };

    const KDevPG::ListNode<qint64 > *dottedNameSequence;
};

struct KDEVPYTHONPARSER_EXPORT ExceptClauseAst: public AstNode
{
    enum { KIND = ExceptClauseKind };

    TestAst *exceptTest;
    TestAst *exceptTargetTest;
};

struct KDEVPYTHONPARSER_EXPORT ExecStmtAst: public AstNode
{
    enum { KIND = ExecStmtKind };

    ExprAst *execCode;
    TestAst *globalDictExec;
    TestAst *localDictExec;
};

struct KDEVPYTHONPARSER_EXPORT ExprAst: public AstNode
{
    enum { KIND = ExprKind };

    XorExprAst *expr;
    const KDevPG::ListNode<XorExprAst *> *orrExprSequence;
};

struct KDEVPYTHONPARSER_EXPORT ExprStmtAst: public AstNode
{
    enum { KIND = ExprStmtKind };

    TestlistAst *testlist;
    AugassignAst *augassign;
    TestlistAst *anugassignTestlist;
    const KDevPG::ListNode<TestlistAst *> *equalTestlistSequence;
};

struct KDEVPYTHONPARSER_EXPORT ExprlistAst: public AstNode
{
    enum { KIND = ExprlistKind };

    const KDevPG::ListNode<ExprAst *> *exprSequence;
    const KDevPG::ListNode<ExprAst *> *exprlistSequence;
};

struct KDEVPYTHONPARSER_EXPORT FactOpAst: public AstNode
{
    enum { KIND = FactOpKind };

    PythonParser::OperatorType facOp;
};

struct KDEVPYTHONPARSER_EXPORT FactorAst: public AstNode
{
    enum { KIND = FactorKind };

    FactOpAst *factOp;
    FactorAst *factor;
    PowerAst *power;
};

struct KDEVPYTHONPARSER_EXPORT FlowStmtAst: public AstNode
{
    enum { KIND = FlowStmtKind };

    BreakStmtAst *breakStmt;
    ContinueStmtAst *continueStmt;
    ReturnStmtAst *returnStmt;
    RaiseStmtAst *raiseStmt;
    YieldStmtAst *yieldStmt;
};

struct KDEVPYTHONPARSER_EXPORT ForStmtAst: public AstNode
{
    enum { KIND = ForStmtKind };

    ExprlistAst *forExpr;
    TestlistAst *forTestlist;
    SuiteAst *forSuite;
    SuiteAst *forElseSuite;
};

struct KDEVPYTHONPARSER_EXPORT FpDefAst: public AstNode
{
    enum { KIND = FpDefKind };

    DefparamAst *defparam;
    TestAst *fpDefTest;
};

struct KDEVPYTHONPARSER_EXPORT FplistAst: public AstNode
{
    enum { KIND = FplistKind };

    const KDevPG::ListNode<DefparamAst *> *fplistFpdefSequence;
};

struct KDEVPYTHONPARSER_EXPORT FunPosParamAst: public AstNode
{
    enum { KIND = FunPosParamKind };

    qint64 starId;
    qint64 doubleStarId;
};

struct KDEVPYTHONPARSER_EXPORT FuncDefAst: public AstNode
{
    enum { KIND = FuncDefKind };

    const KDevPG::ListNode<FpDefAst *> *fpDefSequence;
};

struct KDEVPYTHONPARSER_EXPORT FuncdeclAst: public AstNode
{
    enum { KIND = FuncdeclKind };

    DecoratorsAst *decorators;
    qint64 funcName;
    VarargslistAst *funArgs;
    SuiteAst *funSuite;
};

struct KDEVPYTHONPARSER_EXPORT GenForAst: public AstNode
{
    enum { KIND = GenForKind };

    ExprlistAst *exprlist;
    TestAst *test;
    GenIterAst *genIter;
};

struct KDEVPYTHONPARSER_EXPORT GenIfAst: public AstNode
{
    enum { KIND = GenIfKind };

    TestAst *test;
    GenIterAst *genIter;
};

struct KDEVPYTHONPARSER_EXPORT GenIterAst: public AstNode
{
    enum { KIND = GenIterKind };

    GenForAst *genFor;
    GenIfAst *genIf;
};

struct KDEVPYTHONPARSER_EXPORT GlobalStmtAst: public AstNode
{
    enum { KIND = GlobalStmtKind };

    const KDevPG::ListNode<qint64 > *globalNameSequence;
};

struct KDEVPYTHONPARSER_EXPORT IfStmtAst: public AstNode
{
    enum { KIND = IfStmtKind };

    TestAst *ifTest;
    SuiteAst *ifSuite;
    const KDevPG::ListNode<TestAst *> *elifTestSequence;
    const KDevPG::ListNode<SuiteAst *> *elifSuiteSequence;
    SuiteAst *ifElseSuite;
};

struct KDEVPYTHONPARSER_EXPORT ImportAsNameAst: public AstNode
{
    enum { KIND = ImportAsNameKind };

    qint64 importedName;
    qint64 importedAs;
};

struct KDEVPYTHONPARSER_EXPORT ImportAsNamesAst: public AstNode
{
    enum { KIND = ImportAsNamesKind };

    const KDevPG::ListNode<ImportAsNameAst *> *importAsNameSequence;
};

struct KDEVPYTHONPARSER_EXPORT ImportFromAst: public AstNode
{
    enum { KIND = ImportFromKind };

    DottedNameAst *importFromName;
    ImportAsNamesAst *importAsNames;
};

struct KDEVPYTHONPARSER_EXPORT ImportNameAst: public AstNode
{
    enum { KIND = ImportNameKind };

    DottedAsNamesAst *importName;
};

struct KDEVPYTHONPARSER_EXPORT ImportStmtAst: public AstNode
{
    enum { KIND = ImportStmtKind };

    ImportNameAst *importImport;
    ImportFromAst *importFrom;
};

struct KDEVPYTHONPARSER_EXPORT LambdaDefAst: public AstNode
{
    enum { KIND = LambdaDefKind };

    VarargslistAst *lambdaVarargslist;
    TestAst *lambdaTest;
};

struct KDEVPYTHONPARSER_EXPORT ListForAst: public AstNode
{
    enum { KIND = ListForKind };

    ExprlistAst *exprlist;
    TestlistSafeAst *testlistSafe;
    ListIterAst *listIter;
};

struct KDEVPYTHONPARSER_EXPORT ListIfAst: public AstNode
{
    enum { KIND = ListIfKind };

    TestAst *test;
    ListIterAst *listIter;
};

struct KDEVPYTHONPARSER_EXPORT ListIterAst: public AstNode
{
    enum { KIND = ListIterKind };

    ListForAst *listFor;
    ListIfAst *listIf;
};

struct KDEVPYTHONPARSER_EXPORT ListMakerTestAst: public AstNode
{
    enum { KIND = ListMakerTestKind };

    const KDevPG::ListNode<TestAst *> *listTestSequence;
};

struct KDEVPYTHONPARSER_EXPORT ListmakerAst: public AstNode
{
    enum { KIND = ListmakerKind };

    ListMakerTestAst *listMakerTest;
    ListForAst *listFor;
};

struct KDEVPYTHONPARSER_EXPORT NotTestAst: public AstNode
{
    enum { KIND = NotTestKind };

    NotTestAst *notTest;
    ComparisonAst *comparison;
};

struct KDEVPYTHONPARSER_EXPORT NumberAst: public AstNode
{
    enum { KIND = NumberKind };

    PythonParser::NumericType numType;
};

struct KDEVPYTHONPARSER_EXPORT PassStmtAst: public AstNode
{
    enum { KIND = PassStmtKind };

};

struct KDEVPYTHONPARSER_EXPORT PlainArgumentsListAst: public AstNode
{
    enum { KIND = PlainArgumentsListKind };

    const KDevPG::ListNode<ArgumentAst *> *argumentSequence;
};

struct KDEVPYTHONPARSER_EXPORT PowerAst: public AstNode
{
    enum { KIND = PowerKind };

    AtomAst *atom;
    const KDevPG::ListNode<TrailerAst *> *trailerSequence;
    FactorAst *factor;
};

struct KDEVPYTHONPARSER_EXPORT PrintStmtAst: public AstNode
{
    enum { KIND = PrintStmtKind };

    const KDevPG::ListNode<TestAst *> *printArgsSequence;
    const KDevPG::ListNode<TestAst *> *rshiftArgsSequence;
};

struct KDEVPYTHONPARSER_EXPORT ProjectAst: public AstNode
{
    enum { KIND = ProjectKind };

    const KDevPG::ListNode<StmtAst *> *stmtSequence;
};

struct KDEVPYTHONPARSER_EXPORT RaiseStmtAst: public AstNode
{
    enum { KIND = RaiseStmtKind };

    TestAst *type;
    TestAst *value;
    TestAst *traceback;
};

struct KDEVPYTHONPARSER_EXPORT ReturnStmtAst: public AstNode
{
    enum { KIND = ReturnStmtKind };

    TestlistAst *returnExpr;
};

struct KDEVPYTHONPARSER_EXPORT ShiftExprAst: public AstNode
{
    enum { KIND = ShiftExprKind };

    ArithExprAst *arithExpr;
    const KDevPG::ListNode<ShiftOpAst *> *shiftOpListSequence;
    const KDevPG::ListNode<ArithExprAst *> *arithExprListSequence;
};

struct KDEVPYTHONPARSER_EXPORT ShiftOpAst: public AstNode
{
    enum { KIND = ShiftOpKind };

    PythonParser::OperatorType shiftOp;
};

struct KDEVPYTHONPARSER_EXPORT SimpleStmtAst: public AstNode
{
    enum { KIND = SimpleStmtKind };

    const KDevPG::ListNode<SmallStmtAst *> *smallStmtSequence;
};

struct KDEVPYTHONPARSER_EXPORT SliceopAst: public AstNode
{
    enum { KIND = SliceopKind };

    TestAst *sliceTest;
};

struct KDEVPYTHONPARSER_EXPORT SmallStmtAst: public AstNode
{
    enum { KIND = SmallStmtKind };

    ExprStmtAst *exprStmt;
    PrintStmtAst *printStmt;
    DelStmtAst *delStmt;
    PassStmtAst *passStmt;
    FlowStmtAst *flowStmt;
    ImportStmtAst *importStmt;
    GlobalStmtAst *globalStmt;
    ExecStmtAst *execStmt;
    AssertStmtAst *assertStmt;
};

struct KDEVPYTHONPARSER_EXPORT StmtAst: public AstNode
{
    enum { KIND = StmtKind };

    SimpleStmtAst *simpleStmt;
    CompoundStmtAst *compoundStmt;
};

struct KDEVPYTHONPARSER_EXPORT SubscriptAst: public AstNode
{
    enum { KIND = SubscriptKind };

    qint64 subcriptEllipsis;
    TestAst *subTest;
    TestAst *subColonTest;
    SliceopAst *sliceop;
};

struct KDEVPYTHONPARSER_EXPORT SubscriptlistAst: public AstNode
{
    enum { KIND = SubscriptlistKind };

    const KDevPG::ListNode<SubscriptAst *> *subscriptSequence;
};

struct KDEVPYTHONPARSER_EXPORT SuiteAst: public AstNode
{
    enum { KIND = SuiteKind };

    SimpleStmtAst *simpleStmt;
    const KDevPG::ListNode<StmtAst *> *stmtSequence;
};

struct KDEVPYTHONPARSER_EXPORT TermAst: public AstNode
{
    enum { KIND = TermKind };

    FactorAst *factor;
    const KDevPG::ListNode<TermOpAst *> *termOpListSequence;
    const KDevPG::ListNode<FactorAst *> *factorListSequence;
};

struct KDEVPYTHONPARSER_EXPORT TermOpAst: public AstNode
{
    enum { KIND = TermOpKind };

    PythonParser::OperatorType termOp;
};

struct KDEVPYTHONPARSER_EXPORT TestAst: public AstNode
{
    enum { KIND = TestKind };

    const KDevPG::ListNode<AndTestAst *> *andTestSequence;
    LambdaDefAst *lambdaDef;
};

struct KDEVPYTHONPARSER_EXPORT TestListGexpAst: public AstNode
{
    enum { KIND = TestListGexpKind };

    const KDevPG::ListNode<TestAst *> *testSequence;
};

struct KDEVPYTHONPARSER_EXPORT TestlistAst: public AstNode
{
    enum { KIND = TestlistKind };

    const KDevPG::ListNode<TestAst *> *testSequence;
    const KDevPG::ListNode<TestAst *> *testlistSequence;
};

struct KDEVPYTHONPARSER_EXPORT TestlistGexpAst: public AstNode
{
    enum { KIND = TestlistGexpKind };

    TestListGexpAst *testListGexp;
    GenForAst *genFor;
};

struct KDEVPYTHONPARSER_EXPORT TestlistSafeAst: public AstNode
{
    enum { KIND = TestlistSafeKind };

    const KDevPG::ListNode<TestAst *> *testSequence;
};

struct KDEVPYTHONPARSER_EXPORT TrailerAst: public AstNode
{
    enum { KIND = TrailerKind };

    ArglistAst *trailerArglist;
    SubscriptlistAst *subscriptlist;
    qint64 tarilerDotName;
};

struct KDEVPYTHONPARSER_EXPORT TryStmtAst: public AstNode
{
    enum { KIND = TryStmtKind };

    SuiteAst *trySuite;
    const KDevPG::ListNode<ExceptClauseAst *> *exceptClauseSequence;
    const KDevPG::ListNode<SuiteAst *> *exceptSuiteSequence;
    SuiteAst *tryElseSuite;
    SuiteAst *finallySuite;
};

struct KDEVPYTHONPARSER_EXPORT VarargslistAst: public AstNode
{
    enum { KIND = VarargslistKind };

    FuncDefAst *funcDef;
    FunPosParamAst *funPosParam;
};

struct KDEVPYTHONPARSER_EXPORT WhileStmtAst: public AstNode
{
    enum { KIND = WhileStmtKind };

    TestAst *whileTest;
    SuiteAst *whileSuite;
    SuiteAst *whileElseSuite;
};

struct KDEVPYTHONPARSER_EXPORT XorExprAst: public AstNode
{
    enum { KIND = XorExprKind };

    AndExprAst *xorExpr;
    const KDevPG::ListNode<AndExprAst *> *hatXorExprSequence;
};

struct KDEVPYTHONPARSER_EXPORT YieldStmtAst: public AstNode
{
    enum { KIND = YieldStmtKind };

    TestlistAst *yieldExpr;
};



} // end of namespace PythonParser

#endif

