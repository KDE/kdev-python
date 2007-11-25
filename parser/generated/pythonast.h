// THIS FILE IS GENERATED
// WARNING! All changes made in this file will be lost!

#ifndef PYTHON_AST_H_INCLUDED
#define PYTHON_AST_H_INCLUDED

#include <QtCore/QList>
#include <kdev-pg-list.h>

#include <parserexport.h>


#include <QtCore/QString>

namespace Python
{
class Lexer;

enum shift_operator_enum
{
    op_lshift,
    op_rshift
};
enum arith_operator_enum
{
    op_plus,
    op_minus
};
enum term_operator_enum
{
    op_star,
    op_slash,
    op_modulo,
    op_doubleslash
};
enum factor_operator_enum
{
    op_factor_plus,
    op_factor_minus,
    op_factor_tilde
};
enum augassign_eq_enum
{
    eq_plus,
    eq_minus,
    eq_star,
    eq_slash,
    eq_modulo,
    eq_and,
    eq_or,
    eq_tilde,
    eq_lshift,
    eq_rshift,
    eq_doublestar,
    eq_doubleslash
};
enum comp_operator_enum
{
    op_less,
    op_greater,
    op_isequal,
    op_greatereq,
    op_lesseq,
    op_unequal,
    op_in,
    op_not_in,
    op_is,
    op_is_not
};
enum num_type_enum
{
    type_int,
    type_float,
    type_imagnum
};
}

namespace Python
{

struct And_exprAst;
struct And_testAst;
struct Arg_listAst;
struct ArglistAst;
struct ArgumentAst;
struct Arith_exprAst;
struct Arith_opAst;
struct Assert_stmtAst;
struct AtomAst;
struct AugassignAst;
struct Break_stmtAst;
struct ClassdefAst;
struct Comp_opAst;
struct ComparisonAst;
struct Compound_stmtAst;
struct Continue_stmtAst;
struct DecoratorAst;
struct DecoratorsAst;
struct Del_stmtAst;
struct DictmakerAst;
struct Dotted_as_nameAst;
struct Dotted_as_namesAst;
struct Dotted_nameAst;
struct Except_clauseAst;
struct Exec_stmtAst;
struct ExprAst;
struct Expr_stmtAst;
struct ExprlistAst;
struct Fact_opAst;
struct FactorAst;
struct Flow_stmtAst;
struct For_stmtAst;
struct Fp_defAst;
struct FpdefAst;
struct FplistAst;
struct Fun_pos_paramAst;
struct Func_defAst;
struct FuncdefAst;
struct Gen_forAst;
struct Gen_ifAst;
struct Gen_iterAst;
struct Global_stmtAst;
struct If_stmtAst;
struct Import_as_nameAst;
struct Import_as_namesAst;
struct Import_fromAst;
struct Import_nameAst;
struct Import_stmtAst;
struct Lambda_defAst;
struct List_forAst;
struct List_ifAst;
struct List_iterAst;
struct List_makerAst;
struct ListmakerAst;
struct Not_testAst;
struct NumberAst;
struct Pass_stmtAst;
struct PowerAst;
struct Print_stmtAst;
struct ProjectAst;
struct Raise_stmtAst;
struct Return_stmtAst;
struct Shift_exprAst;
struct Shift_opAst;
struct Simple_stmtAst;
struct SliceopAst;
struct Small_stmtAst;
struct StmtAst;
struct SubscriptAst;
struct SubscriptlistAst;
struct SuiteAst;
struct TermAst;
struct Term_opAst;
struct TestAst;
struct Test_list_gexpAst;
struct TestlistAst;
struct Testlist1Ast;
struct Testlist_gexpAst;
struct Testlist_safeAst;
struct TrailerAst;
struct Try_stmtAst;
struct VarargslistAst;
struct While_stmtAst;
struct Xor_exprAst;
struct Yield_stmtAst;


struct KDEVPYTHONPARSER_EXPORT AstNode
{
    enum AstNodeKind
    {
        And_exprKind = 1000,
        And_testKind = 1001,
        Arg_listKind = 1002,
        ArglistKind = 1003,
        ArgumentKind = 1004,
        Arith_exprKind = 1005,
        Arith_opKind = 1006,
        Assert_stmtKind = 1007,
        AtomKind = 1008,
        AugassignKind = 1009,
        Break_stmtKind = 1010,
        ClassdefKind = 1011,
        Comp_opKind = 1012,
        ComparisonKind = 1013,
        Compound_stmtKind = 1014,
        Continue_stmtKind = 1015,
        DecoratorKind = 1016,
        DecoratorsKind = 1017,
        Del_stmtKind = 1018,
        DictmakerKind = 1019,
        Dotted_as_nameKind = 1020,
        Dotted_as_namesKind = 1021,
        Dotted_nameKind = 1022,
        Except_clauseKind = 1023,
        Exec_stmtKind = 1024,
        ExprKind = 1025,
        Expr_stmtKind = 1026,
        ExprlistKind = 1027,
        Fact_opKind = 1028,
        FactorKind = 1029,
        Flow_stmtKind = 1030,
        For_stmtKind = 1031,
        Fp_defKind = 1032,
        FpdefKind = 1033,
        FplistKind = 1034,
        Fun_pos_paramKind = 1035,
        Func_defKind = 1036,
        FuncdefKind = 1037,
        Gen_forKind = 1038,
        Gen_ifKind = 1039,
        Gen_iterKind = 1040,
        Global_stmtKind = 1041,
        If_stmtKind = 1042,
        Import_as_nameKind = 1043,
        Import_as_namesKind = 1044,
        Import_fromKind = 1045,
        Import_nameKind = 1046,
        Import_stmtKind = 1047,
        Lambda_defKind = 1048,
        List_forKind = 1049,
        List_ifKind = 1050,
        List_iterKind = 1051,
        List_makerKind = 1052,
        ListmakerKind = 1053,
        Not_testKind = 1054,
        NumberKind = 1055,
        Pass_stmtKind = 1056,
        PowerKind = 1057,
        Print_stmtKind = 1058,
        ProjectKind = 1059,
        Raise_stmtKind = 1060,
        Return_stmtKind = 1061,
        Shift_exprKind = 1062,
        Shift_opKind = 1063,
        Simple_stmtKind = 1064,
        SliceopKind = 1065,
        Small_stmtKind = 1066,
        StmtKind = 1067,
        SubscriptKind = 1068,
        SubscriptlistKind = 1069,
        SuiteKind = 1070,
        TermKind = 1071,
        Term_opKind = 1072,
        TestKind = 1073,
        Test_list_gexpKind = 1074,
        TestlistKind = 1075,
        Testlist1Kind = 1076,
        Testlist_gexpKind = 1077,
        Testlist_safeKind = 1078,
        TrailerKind = 1079,
        Try_stmtKind = 1080,
        VarargslistKind = 1081,
        While_stmtKind = 1082,
        Xor_exprKind = 1083,
        Yield_stmtKind = 1084,
        AST_NODE_KIND_COUNT
    };

    int kind;
    qint64 startToken;
    qint64 endToken;
};

struct KDEVPYTHONPARSER_EXPORT And_exprAst: public AstNode
{
    enum { KIND = And_exprKind };

    Shift_exprAst *and_expr;
    const KDevPG::ListNode<Shift_exprAst *> *andd_shif_exprSequence;
};

struct KDEVPYTHONPARSER_EXPORT And_testAst: public AstNode
{
    enum { KIND = And_testKind };

    const KDevPG::ListNode<Not_testAst *> *not_testSequence;
};

struct KDEVPYTHONPARSER_EXPORT Arg_listAst: public AstNode
{
    enum { KIND = Arg_listKind };

    const KDevPG::ListNode<ArgumentAst *> *argumentSequence;
};

struct KDEVPYTHONPARSER_EXPORT ArglistAst: public AstNode
{
    enum { KIND = ArglistKind };

    Arg_listAst *arg_list;
    TestAst *arglist_star;
    TestAst *arglist_doublestar;
};

struct KDEVPYTHONPARSER_EXPORT ArgumentAst: public AstNode
{
    enum { KIND = ArgumentKind };

    TestAst *argument_test;
    TestAst *argument_equal_test;
    Gen_forAst *gen_for;
};

struct KDEVPYTHONPARSER_EXPORT Arith_exprAst: public AstNode
{
    enum { KIND = Arith_exprKind };

    TermAst *arith_term;
    const KDevPG::ListNode<Arith_opAst *> *arith_op_listSequence;
    const KDevPG::ListNode<TermAst *> *arith_term_listSequence;
};

struct KDEVPYTHONPARSER_EXPORT Arith_opAst: public AstNode
{
    enum { KIND = Arith_opKind };

    Python::arith_operator_enum arith_operator;
};

struct KDEVPYTHONPARSER_EXPORT Assert_stmtAst: public AstNode
{
    enum { KIND = Assert_stmtKind };

    TestAst *assert_not_test;
    TestAst *assert_raise_test;
};

struct KDEVPYTHONPARSER_EXPORT AtomAst: public AstNode
{
    enum { KIND = AtomKind };

    Testlist_gexpAst *testlist_gexp;
    ListmakerAst *listmaker;
    DictmakerAst *dictmaker;
    Testlist1Ast *testlist1;
    qint64 atom_identifier_name;
    NumberAst *number;
    const KDevPG::ListNode<qint64 > *stringliteralSequence;
};

struct KDEVPYTHONPARSER_EXPORT AugassignAst: public AstNode
{
    enum { KIND = AugassignKind };

    Python::augassign_eq_enum augassign_eq;
};

struct KDEVPYTHONPARSER_EXPORT Break_stmtAst: public AstNode
{
    enum { KIND = Break_stmtKind };

};

struct KDEVPYTHONPARSER_EXPORT ClassdefAst: public AstNode
{
    enum { KIND = ClassdefKind };

    qint64 class_name;
    TestlistAst *testlist;
    SuiteAst *class_suite;
};

struct KDEVPYTHONPARSER_EXPORT Comp_opAst: public AstNode
{
    enum { KIND = Comp_opKind };

    Python::comp_operator_enum comp_operator;
};

struct KDEVPYTHONPARSER_EXPORT ComparisonAst: public AstNode
{
    enum { KIND = ComparisonKind };

    ExprAst *comp_expr;
    const KDevPG::ListNode<Comp_opAst *> *comp_opSequence;
    const KDevPG::ListNode<ExprAst *> *comp_op_exprSequence;
};

struct KDEVPYTHONPARSER_EXPORT Compound_stmtAst: public AstNode
{
    enum { KIND = Compound_stmtKind };

    If_stmtAst *if_stmt;
    While_stmtAst *while_stmt;
    For_stmtAst *for_stmt;
    Try_stmtAst *try_stmt;
    FuncdefAst *fucdef;
    ClassdefAst *classdef;
};

struct KDEVPYTHONPARSER_EXPORT Continue_stmtAst: public AstNode
{
    enum { KIND = Continue_stmtKind };

};

struct KDEVPYTHONPARSER_EXPORT DecoratorAst: public AstNode
{
    enum { KIND = DecoratorKind };

    Dotted_nameAst *decorator_name;
    ArglistAst *arguments;
};

struct KDEVPYTHONPARSER_EXPORT DecoratorsAst: public AstNode
{
    enum { KIND = DecoratorsKind };

    const KDevPG::ListNode<DecoratorAst *> *decoratorSequence;
};

struct KDEVPYTHONPARSER_EXPORT Del_stmtAst: public AstNode
{
    enum { KIND = Del_stmtKind };

    ExprlistAst *del_list;
};

struct KDEVPYTHONPARSER_EXPORT DictmakerAst: public AstNode
{
    enum { KIND = DictmakerKind };

    const KDevPG::ListNode<TestAst *> *key_listSequence;
    const KDevPG::ListNode<TestAst *> *value_listSequence;
};

struct KDEVPYTHONPARSER_EXPORT Dotted_as_nameAst: public AstNode
{
    enum { KIND = Dotted_as_nameKind };

    Dotted_nameAst *import_dotted_name;
    qint64 imported_as;
};

struct KDEVPYTHONPARSER_EXPORT Dotted_as_namesAst: public AstNode
{
    enum { KIND = Dotted_as_namesKind };

    const KDevPG::ListNode<Dotted_as_nameAst *> *dotted_as_nameSequence;
};

struct KDEVPYTHONPARSER_EXPORT Dotted_nameAst: public AstNode
{
    enum { KIND = Dotted_nameKind };

    qint64 dotted_name;
};

struct KDEVPYTHONPARSER_EXPORT Except_clauseAst: public AstNode
{
    enum { KIND = Except_clauseKind };

    TestAst *except_test;
    TestAst *except_target_test;
};

struct KDEVPYTHONPARSER_EXPORT Exec_stmtAst: public AstNode
{
    enum { KIND = Exec_stmtKind };

    ExprAst *exec_code;
    TestAst *global_dict_exec;
    TestAst *local_dict_exec;
};

struct KDEVPYTHONPARSER_EXPORT ExprAst: public AstNode
{
    enum { KIND = ExprKind };

    Xor_exprAst *expr;
    const KDevPG::ListNode<Xor_exprAst *> *orr_exprSequence;
};

struct KDEVPYTHONPARSER_EXPORT Expr_stmtAst: public AstNode
{
    enum { KIND = Expr_stmtKind };

    TestlistAst *testlist;
    AugassignAst *augassign;
    TestlistAst *anugassign_testlist;
    const KDevPG::ListNode<TestlistAst *> *equal_testlistSequence;
};

struct KDEVPYTHONPARSER_EXPORT ExprlistAst: public AstNode
{
    enum { KIND = ExprlistKind };

    const KDevPG::ListNode<ExprAst *> *exprSequence;
    const KDevPG::ListNode<ExprAst *> *exprlistSequence;
};

struct KDEVPYTHONPARSER_EXPORT Fact_opAst: public AstNode
{
    enum { KIND = Fact_opKind };

    Python::factor_operator_enum factor_operator;
};

struct KDEVPYTHONPARSER_EXPORT FactorAst: public AstNode
{
    enum { KIND = FactorKind };

    Fact_opAst *fact_op;
    FactorAst *factor;
    PowerAst *power;
};

struct KDEVPYTHONPARSER_EXPORT Flow_stmtAst: public AstNode
{
    enum { KIND = Flow_stmtKind };

    Break_stmtAst *break_stmt;
    Continue_stmtAst *continue_stmt;
    Return_stmtAst *return_stmt;
    Raise_stmtAst *raise_stmt;
    Yield_stmtAst *yield_stmt;
};

struct KDEVPYTHONPARSER_EXPORT For_stmtAst: public AstNode
{
    enum { KIND = For_stmtKind };

    ExprlistAst *for_expr;
    TestlistAst *for_testlist;
    SuiteAst *for_suite;
    SuiteAst *for_else_suite;
};

struct KDEVPYTHONPARSER_EXPORT Fp_defAst: public AstNode
{
    enum { KIND = Fp_defKind };

    FpdefAst *fpdef;
    TestAst *fp_def_test;
};

struct KDEVPYTHONPARSER_EXPORT FpdefAst: public AstNode
{
    enum { KIND = FpdefKind };

    FplistAst *fplist;
};

struct KDEVPYTHONPARSER_EXPORT FplistAst: public AstNode
{
    enum { KIND = FplistKind };

    const KDevPG::ListNode<FpdefAst *> *fplist_fpdefSequence;
};

struct KDEVPYTHONPARSER_EXPORT Fun_pos_paramAst: public AstNode
{
    enum { KIND = Fun_pos_paramKind };

    qint64 star_id;
    qint64 double_star_id;
};

struct KDEVPYTHONPARSER_EXPORT Func_defAst: public AstNode
{
    enum { KIND = Func_defKind };

    const KDevPG::ListNode<Fp_defAst *> *fp_defSequence;
};

struct KDEVPYTHONPARSER_EXPORT FuncdefAst: public AstNode
{
    enum { KIND = FuncdefKind };

    DecoratorsAst *decorators;
    qint64 func_name;
    VarargslistAst *fun_args;
    SuiteAst *fun_suite;
};

struct KDEVPYTHONPARSER_EXPORT Gen_forAst: public AstNode
{
    enum { KIND = Gen_forKind };

    ExprlistAst *exprlist;
    TestAst *test;
    Gen_iterAst *gen_iter;
};

struct KDEVPYTHONPARSER_EXPORT Gen_ifAst: public AstNode
{
    enum { KIND = Gen_ifKind };

    TestAst *test;
    Gen_iterAst *gen_iter;
};

struct KDEVPYTHONPARSER_EXPORT Gen_iterAst: public AstNode
{
    enum { KIND = Gen_iterKind };

    Gen_forAst *gen_for;
    Gen_ifAst *gen_if;
};

struct KDEVPYTHONPARSER_EXPORT Global_stmtAst: public AstNode
{
    enum { KIND = Global_stmtKind };

    const KDevPG::ListNode<qint64 > *global_nameSequence;
};

struct KDEVPYTHONPARSER_EXPORT If_stmtAst: public AstNode
{
    enum { KIND = If_stmtKind };

    const KDevPG::ListNode<TestAst *> *if_testSequence;
    SuiteAst *if_suite;
    const KDevPG::ListNode<TestAst *> *elif_testSequence;
    const KDevPG::ListNode<SuiteAst *> *elif_suiteSequence;
    SuiteAst *if_else_suite;
};

struct KDEVPYTHONPARSER_EXPORT Import_as_nameAst: public AstNode
{
    enum { KIND = Import_as_nameKind };

    qint64 imported_name;
    qint64 imported_as;
};

struct KDEVPYTHONPARSER_EXPORT Import_as_namesAst: public AstNode
{
    enum { KIND = Import_as_namesKind };

    const KDevPG::ListNode<Import_as_nameAst *> *import_as_nameSequence;
};

struct KDEVPYTHONPARSER_EXPORT Import_fromAst: public AstNode
{
    enum { KIND = Import_fromKind };

    Dotted_nameAst *import_from_name;
    Import_as_namesAst *import_as_names;
    Import_as_namesAst *import_from_as_name;
};

struct KDEVPYTHONPARSER_EXPORT Import_nameAst: public AstNode
{
    enum { KIND = Import_nameKind };

    Dotted_as_namesAst *import_name;
};

struct KDEVPYTHONPARSER_EXPORT Import_stmtAst: public AstNode
{
    enum { KIND = Import_stmtKind };

    Import_nameAst *import_import;
    Import_fromAst *import_from;
};

struct KDEVPYTHONPARSER_EXPORT Lambda_defAst: public AstNode
{
    enum { KIND = Lambda_defKind };

    VarargslistAst *lambda_varargslist;
    TestAst *lambda_test;
};

struct KDEVPYTHONPARSER_EXPORT List_forAst: public AstNode
{
    enum { KIND = List_forKind };

    ExprlistAst *exprlist;
    Testlist_safeAst *testlist_safe;
    List_iterAst *list_iter;
};

struct KDEVPYTHONPARSER_EXPORT List_ifAst: public AstNode
{
    enum { KIND = List_ifKind };

    TestAst *test;
    List_iterAst *list_iter;
};

struct KDEVPYTHONPARSER_EXPORT List_iterAst: public AstNode
{
    enum { KIND = List_iterKind };

    List_forAst *list_for;
    List_ifAst *list_if;
};

struct KDEVPYTHONPARSER_EXPORT List_makerAst: public AstNode
{
    enum { KIND = List_makerKind };

    const KDevPG::ListNode<TestAst *> *list_testSequence;
};

struct KDEVPYTHONPARSER_EXPORT ListmakerAst: public AstNode
{
    enum { KIND = ListmakerKind };

    List_makerAst *list_maker;
    List_forAst *list_for;
};

struct KDEVPYTHONPARSER_EXPORT Not_testAst: public AstNode
{
    enum { KIND = Not_testKind };

    Not_testAst *not_test;
    ComparisonAst *comparison;
};

struct KDEVPYTHONPARSER_EXPORT NumberAst: public AstNode
{
    enum { KIND = NumberKind };

    Python::num_type_enum num_type;
};

struct KDEVPYTHONPARSER_EXPORT Pass_stmtAst: public AstNode
{
    enum { KIND = Pass_stmtKind };

};

struct KDEVPYTHONPARSER_EXPORT PowerAst: public AstNode
{
    enum { KIND = PowerKind };

    AtomAst *atom;
    const KDevPG::ListNode<TrailerAst *> *trailerSequence;
    FactorAst *factor;
};

struct KDEVPYTHONPARSER_EXPORT Print_stmtAst: public AstNode
{
    enum { KIND = Print_stmtKind };

    const KDevPG::ListNode<TestAst *> *print_argsSequence;
    const KDevPG::ListNode<TestAst *> *rshift_argsSequence;
};

struct KDEVPYTHONPARSER_EXPORT ProjectAst: public AstNode
{
    enum { KIND = ProjectKind };

    const KDevPG::ListNode<StmtAst *> *stmtSequence;
};

struct KDEVPYTHONPARSER_EXPORT Raise_stmtAst: public AstNode
{
    enum { KIND = Raise_stmtKind };

    TestAst *type;
    TestAst *value;
    TestAst *traceback;
};

struct KDEVPYTHONPARSER_EXPORT Return_stmtAst: public AstNode
{
    enum { KIND = Return_stmtKind };

    TestlistAst *return_expr;
};

struct KDEVPYTHONPARSER_EXPORT Shift_exprAst: public AstNode
{
    enum { KIND = Shift_exprKind };

    Arith_exprAst *arith_expr;
    const KDevPG::ListNode<Shift_opAst *> *shift_op_listSequence;
    const KDevPG::ListNode<Arith_exprAst *> *arith_expr_listSequence;
};

struct KDEVPYTHONPARSER_EXPORT Shift_opAst: public AstNode
{
    enum { KIND = Shift_opKind };

    Python::shift_operator_enum shift_operator;
};

struct KDEVPYTHONPARSER_EXPORT Simple_stmtAst: public AstNode
{
    enum { KIND = Simple_stmtKind };

    const KDevPG::ListNode<Small_stmtAst *> *small_stmtSequence;
};

struct KDEVPYTHONPARSER_EXPORT SliceopAst: public AstNode
{
    enum { KIND = SliceopKind };

    TestAst *slice_test;
};

struct KDEVPYTHONPARSER_EXPORT Small_stmtAst: public AstNode
{
    enum { KIND = Small_stmtKind };

    Expr_stmtAst *expr_stmt;
    Print_stmtAst *print_stmt;
    Del_stmtAst *del_stmt;
    Pass_stmtAst *pass_stmt;
    Flow_stmtAst *flow_stmt;
    Import_stmtAst *import_stmt;
    Global_stmtAst *global_stmt;
    Exec_stmtAst *exec_stmt;
    Assert_stmtAst *assert_stmt;
};

struct KDEVPYTHONPARSER_EXPORT StmtAst: public AstNode
{
    enum { KIND = StmtKind };

    Simple_stmtAst *simple_stmt;
    Compound_stmtAst *compound_stmt;
};

struct KDEVPYTHONPARSER_EXPORT SubscriptAst: public AstNode
{
    enum { KIND = SubscriptKind };

    qint64 subcript_ellipsis;
    TestAst *sub_test;
    TestAst *sub_colon_test;
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

    Simple_stmtAst *simple_stmt;
    const KDevPG::ListNode<StmtAst *> *stmtSequence;
};

struct KDEVPYTHONPARSER_EXPORT TermAst: public AstNode
{
    enum { KIND = TermKind };

    FactorAst *factor;
    const KDevPG::ListNode<Term_opAst *> *term_op_listSequence;
    const KDevPG::ListNode<FactorAst *> *factor_listSequence;
};

struct KDEVPYTHONPARSER_EXPORT Term_opAst: public AstNode
{
    enum { KIND = Term_opKind };

    Python::term_operator_enum term_operator;
};

struct KDEVPYTHONPARSER_EXPORT TestAst: public AstNode
{
    enum { KIND = TestKind };

    const KDevPG::ListNode<And_testAst *> *and_testSequence;
    Lambda_defAst *lambda_def;
};

struct KDEVPYTHONPARSER_EXPORT Test_list_gexpAst: public AstNode
{
    enum { KIND = Test_list_gexpKind };

    const KDevPG::ListNode<TestAst *> *testSequence;
};

struct KDEVPYTHONPARSER_EXPORT TestlistAst: public AstNode
{
    enum { KIND = TestlistKind };

    const KDevPG::ListNode<TestAst *> *testSequence;
    const KDevPG::ListNode<TestAst *> *testlistSequence;
};

struct KDEVPYTHONPARSER_EXPORT Testlist1Ast: public AstNode
{
    enum { KIND = Testlist1Kind };

    const KDevPG::ListNode<TestAst *> *testSequence;
};

struct KDEVPYTHONPARSER_EXPORT Testlist_gexpAst: public AstNode
{
    enum { KIND = Testlist_gexpKind };

    Test_list_gexpAst *test_list_gexp;
    Gen_forAst *gen_for;
};

struct KDEVPYTHONPARSER_EXPORT Testlist_safeAst: public AstNode
{
    enum { KIND = Testlist_safeKind };

    const KDevPG::ListNode<TestAst *> *testSequence;
};

struct KDEVPYTHONPARSER_EXPORT TrailerAst: public AstNode
{
    enum { KIND = TrailerKind };

    ArglistAst *trailer_arglist;
    SubscriptlistAst *subscriptlist;
    qint64 tariler_dot_name;
};

struct KDEVPYTHONPARSER_EXPORT Try_stmtAst: public AstNode
{
    enum { KIND = Try_stmtKind };

    SuiteAst *try_suite;
    const KDevPG::ListNode<Except_clauseAst *> *except_clauseSequence;
    const KDevPG::ListNode<SuiteAst *> *except_suiteSequence;
    SuiteAst *try_else_suite;
    SuiteAst *finally_suite;
};

struct KDEVPYTHONPARSER_EXPORT VarargslistAst: public AstNode
{
    enum { KIND = VarargslistKind };

    Func_defAst *func_def;
    Fun_pos_paramAst *fun_pos_param;
};

struct KDEVPYTHONPARSER_EXPORT While_stmtAst: public AstNode
{
    enum { KIND = While_stmtKind };

    TestAst *while_test;
    SuiteAst *while_suite;
    SuiteAst *while_else_suite;
};

struct KDEVPYTHONPARSER_EXPORT Xor_exprAst: public AstNode
{
    enum { KIND = Xor_exprKind };

    And_exprAst *xor_expr;
    const KDevPG::ListNode<And_exprAst *> *hat_xor_exprSequence;
};

struct KDEVPYTHONPARSER_EXPORT Yield_stmtAst: public AstNode
{
    enum { KIND = Yield_stmtKind };

    TestlistAst *yield_expr;
};



} // end of namespace Python

#endif

