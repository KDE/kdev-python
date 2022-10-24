#pragma once
#include "python_header.h"

namespace Python
{

#define Py_GRAMMAR_GET(mod, name) \
    ast_##name = PyObject_GetAttrString(mod, #name); \
    Q_ASSERT(ast_##name)

class Grammar {
public:
    // https://docs.python.org/3/library/ast.html#abstract-grammar
    // mod
    PyObject* ast_mod;
    PyObject* ast_Module;
    PyObject* ast_Interactive;
    PyObject* ast_Expression;
    PyObject* ast_FunctionType;

    // stmt
    PyObject* ast_stmt;
    PyObject* ast_FunctionDef;
    PyObject* ast_AsyncFunctionDef;
    PyObject* ast_ClassDef;
    PyObject* ast_Return;
    PyObject* ast_Delete;
    PyObject* ast_Assign;
    PyObject* ast_AugAssign;
    PyObject* ast_AnnAssign;
    PyObject* ast_For;
    PyObject* ast_AsyncFor;
    PyObject* ast_While;
    PyObject* ast_If;
    PyObject* ast_With;
    PyObject* ast_AsyncWith;
    PyObject* ast_Match;
    PyObject* ast_Raise;
    PyObject* ast_Try;
    PyObject* ast_Assert;
    PyObject* ast_Import;
    PyObject* ast_ImportFrom;
    PyObject* ast_Global;
    PyObject* ast_Nonlocal;
    PyObject* ast_Pass;
    PyObject* ast_Break;
    PyObject* ast_Continue;

    // expr
    PyObject* ast_expr;
    PyObject* ast_Expr;
    PyObject* ast_BoolOp;
    PyObject* ast_NamedExpr;
    PyObject* ast_BinOp;
    PyObject* ast_UnaryOp;
    PyObject* ast_Lambda;
    PyObject* ast_IfExp;
    PyObject* ast_Dict;
    PyObject* ast_Set;
    PyObject* ast_ListComp;
    PyObject* ast_SetComp;
    PyObject* ast_DictComp;
    PyObject* ast_GeneratorExp;
    PyObject* ast_Await;
    PyObject* ast_Yield;
    PyObject* ast_YieldFrom;
    PyObject* ast_Compare;
    PyObject* ast_Call;
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 6, 0)
    PyObject* ast_FormattedValue;
#endif
    PyObject* ast_JoinedStr;
    PyObject* ast_Constant;
    PyObject* ast_Attribute;
    PyObject* ast_Subscript;
    PyObject* ast_Starred;
    PyObject* ast_Name;
    PyObject* ast_List;
    PyObject* ast_Tuple;
    PyObject* ast_Slice;

    // expr_context
    PyObject* ast_expr_context;
    PyObject* ast_Load;
    PyObject* ast_Store;
    PyObject* ast_Del;

    // boolop
    PyObject* ast_boolop;
    PyObject* ast_And;
    PyObject* ast_Or;

    // operator
    PyObject* ast_operator;
    PyObject* ast_Add;
    PyObject* ast_Sub;
    PyObject* ast_Mult;
    PyObject* ast_MatMult;
    PyObject* ast_Div;
    PyObject* ast_Mod;
    PyObject* ast_Pow;
    PyObject* ast_LShift;
    PyObject* ast_RShift;
    PyObject* ast_BitOr;
    PyObject* ast_BitXor;
    PyObject* ast_BitAnd;
    PyObject* ast_FloorDiv;

    // unaryop
    PyObject* ast_unaryop;
    PyObject* ast_Invert;
    PyObject* ast_Not;
    PyObject* ast_UAdd;
    PyObject* ast_USub;

    // cmpop
    PyObject* ast_cmpop;
    PyObject* ast_Eq;
    PyObject* ast_NotEq;
    PyObject* ast_Lt;
    PyObject* ast_LtE;
    PyObject* ast_Gt;
    PyObject* ast_GtE;
    PyObject* ast_Is;
    PyObject* ast_IsNot;
    PyObject* ast_In;
    PyObject* ast_NotIn;

    // comprehension
    PyObject* ast_comprehension;

    // excepthandler
    PyObject* ast_excepthandler;
    PyObject* ast_ExceptHandler;

    // arguments
    PyObject* ast_arguments;

    // arg
    PyObject* ast_arg;

    // keyword
    PyObject* ast_keyword;

    // alias
    PyObject* ast_alias;

    // withitem
    PyObject* ast_withitem;

#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 10, 0)
    // match_case
    PyObject* ast_match_case;

    // pattern
    PyObject* ast_pattern;
    PyObject* ast_MatchValue;
    PyObject* ast_MatchSingleton;
    PyObject* ast_MatchSequence;
    PyObject* ast_MatchMapping;
    PyObject* ast_MatchClass;
    PyObject* ast_MatchStar;
    PyObject* ast_MatchAs;
    PyObject* ast_MatchOr;
#endif

    // type_ignore
    PyObject* ast_type_ignore;
    PyObject* ast_TypeIgnore;

#if PYTHON_VERSION < QT_VERSION_CHECK(3, 8, 0)
    // Missing in 3.8+
    PyObject* ast_Num;
    PyObject* ast_Str;
    PyObject* ast_Bytes;
#endif

    Grammar() {
        PyObject* mod = PyImport_ImportModule("ast");

        Py_GRAMMAR_GET(mod, mod);
        Py_GRAMMAR_GET(mod, Module);
        Py_GRAMMAR_GET(mod, Interactive);
        Py_GRAMMAR_GET(mod, Expression);
        Py_GRAMMAR_GET(mod, FunctionType);

        Py_GRAMMAR_GET(mod, stmt);
        Py_GRAMMAR_GET(mod, FunctionDef);
        Py_GRAMMAR_GET(mod, AsyncFunctionDef);
        Py_GRAMMAR_GET(mod, ClassDef);
        Py_GRAMMAR_GET(mod, Return);
        Py_GRAMMAR_GET(mod, Delete);
        Py_GRAMMAR_GET(mod, Assign);
        Py_GRAMMAR_GET(mod, AugAssign);
        Py_GRAMMAR_GET(mod, AnnAssign);
        Py_GRAMMAR_GET(mod, For);
        Py_GRAMMAR_GET(mod, AsyncFor);
        Py_GRAMMAR_GET(mod, While);
        Py_GRAMMAR_GET(mod, If);
        Py_GRAMMAR_GET(mod, With);
        Py_GRAMMAR_GET(mod, AsyncWith);
        Py_GRAMMAR_GET(mod, Match);
        Py_GRAMMAR_GET(mod, Raise);
        Py_GRAMMAR_GET(mod, Try);
        Py_GRAMMAR_GET(mod, Assert);
        Py_GRAMMAR_GET(mod, Import);
        Py_GRAMMAR_GET(mod, ImportFrom);
        Py_GRAMMAR_GET(mod, Global);
        Py_GRAMMAR_GET(mod, Nonlocal);
        Py_GRAMMAR_GET(mod, Pass);
        Py_GRAMMAR_GET(mod, Break);
        Py_GRAMMAR_GET(mod, Continue);

        Py_GRAMMAR_GET(mod, expr);
        Py_GRAMMAR_GET(mod, Expr);
        Py_GRAMMAR_GET(mod, BoolOp);
        Py_GRAMMAR_GET(mod, NamedExpr);
        Py_GRAMMAR_GET(mod, BinOp);
        Py_GRAMMAR_GET(mod, UnaryOp);
        Py_GRAMMAR_GET(mod, Lambda);
        Py_GRAMMAR_GET(mod, IfExp);
        Py_GRAMMAR_GET(mod, Dict);
        Py_GRAMMAR_GET(mod, Set);
        Py_GRAMMAR_GET(mod, ListComp);
        Py_GRAMMAR_GET(mod, SetComp);
        Py_GRAMMAR_GET(mod, DictComp);
        Py_GRAMMAR_GET(mod, GeneratorExp);
        Py_GRAMMAR_GET(mod, Await);
        Py_GRAMMAR_GET(mod, Yield);
        Py_GRAMMAR_GET(mod, YieldFrom);
        Py_GRAMMAR_GET(mod, Compare);
        Py_GRAMMAR_GET(mod, Call);
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 6, 0)
        Py_GRAMMAR_GET(mod, FormattedValue);
#endif
        Py_GRAMMAR_GET(mod, JoinedStr);
        Py_GRAMMAR_GET(mod, Constant);
        Py_GRAMMAR_GET(mod, Attribute);
        Py_GRAMMAR_GET(mod, Subscript);
        Py_GRAMMAR_GET(mod, Starred);
        Py_GRAMMAR_GET(mod, Name);
        Py_GRAMMAR_GET(mod, List);
        Py_GRAMMAR_GET(mod, Tuple);
        Py_GRAMMAR_GET(mod, Slice);

        Py_GRAMMAR_GET(mod, expr_context);
        Py_GRAMMAR_GET(mod, Load);
        Py_GRAMMAR_GET(mod, Store);
        Py_GRAMMAR_GET(mod, Del);

        Py_GRAMMAR_GET(mod, boolop);
        Py_GRAMMAR_GET(mod, And);
        Py_GRAMMAR_GET(mod, Or);

        Py_GRAMMAR_GET(mod, operator);
        Py_GRAMMAR_GET(mod, Add);
        Py_GRAMMAR_GET(mod, Sub);
        Py_GRAMMAR_GET(mod, Mult);
        Py_GRAMMAR_GET(mod, MatMult);
        Py_GRAMMAR_GET(mod, Div);
        Py_GRAMMAR_GET(mod, Mod);
        Py_GRAMMAR_GET(mod, Pow);
        Py_GRAMMAR_GET(mod, LShift);
        Py_GRAMMAR_GET(mod, RShift);
        Py_GRAMMAR_GET(mod, BitOr);
        Py_GRAMMAR_GET(mod, BitXor);
        Py_GRAMMAR_GET(mod, BitAnd);
        Py_GRAMMAR_GET(mod, FloorDiv);

        Py_GRAMMAR_GET(mod, unaryop);
        Py_GRAMMAR_GET(mod, Invert);
        Py_GRAMMAR_GET(mod, Not);
        Py_GRAMMAR_GET(mod, UAdd);
        Py_GRAMMAR_GET(mod, USub);

        Py_GRAMMAR_GET(mod, cmpop);
        Py_GRAMMAR_GET(mod, Eq);
        Py_GRAMMAR_GET(mod, NotEq);
        Py_GRAMMAR_GET(mod, Lt);
        Py_GRAMMAR_GET(mod, LtE);
        Py_GRAMMAR_GET(mod, Gt);
        Py_GRAMMAR_GET(mod, GtE);
        Py_GRAMMAR_GET(mod, Is);
        Py_GRAMMAR_GET(mod, IsNot);
        Py_GRAMMAR_GET(mod, In);
        Py_GRAMMAR_GET(mod, NotIn);

        Py_GRAMMAR_GET(mod, comprehension);

        Py_GRAMMAR_GET(mod, excepthandler);
        Py_GRAMMAR_GET(mod, ExceptHandler);

        Py_GRAMMAR_GET(mod, arguments);
        Py_GRAMMAR_GET(mod, arg);
        Py_GRAMMAR_GET(mod, keyword);
        Py_GRAMMAR_GET(mod, alias);
        Py_GRAMMAR_GET(mod, withitem);

#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 10, 0)
        Py_GRAMMAR_GET(mod, match_case);
        Py_GRAMMAR_GET(mod, pattern);
        Py_GRAMMAR_GET(mod, MatchValue);
        Py_GRAMMAR_GET(mod, MatchSingleton);
        Py_GRAMMAR_GET(mod, MatchSequence);
        Py_GRAMMAR_GET(mod, MatchMapping);
        Py_GRAMMAR_GET(mod, MatchClass);
        Py_GRAMMAR_GET(mod, MatchStar);
        Py_GRAMMAR_GET(mod, MatchAs);
        Py_GRAMMAR_GET(mod, MatchOr);
#endif
        Py_GRAMMAR_GET(mod, type_ignore);
        Py_GRAMMAR_GET(mod, TypeIgnore);

#if PYTHON_VERSION < QT_VERSION_CHECK(3, 8, 0)
        Py_GRAMMAR_GET(mod, Num);
        Py_GRAMMAR_GET(mod, Str);
        Py_GRAMMAR_GET(mod, Bytes);
#endif

        Py_DECREF(mod);
    }

    ~Grammar() {
        Py_XDECREF(ast_Module);
        Py_XDECREF(ast_Interactive);
        Py_XDECREF(ast_Expression);
        Py_XDECREF(ast_FunctionType);

        Py_XDECREF(ast_stmt);
        Py_XDECREF(ast_FunctionDef);
        Py_XDECREF(ast_AsyncFunctionDef);
        Py_XDECREF(ast_ClassDef);
        Py_XDECREF(ast_Return);
        Py_XDECREF(ast_Delete);
        Py_XDECREF(ast_Assign);
        Py_XDECREF(ast_AugAssign);
        Py_XDECREF(ast_AnnAssign);
        Py_XDECREF(ast_For);
        Py_XDECREF(ast_AsyncFor);
        Py_XDECREF(ast_While);
        Py_XDECREF(ast_If);
        Py_XDECREF(ast_With);
        Py_XDECREF(ast_AsyncWith);
        Py_XDECREF(ast_Match);
        Py_XDECREF(ast_Raise);
        Py_XDECREF(ast_Try);
        Py_XDECREF(ast_Assert);
        Py_XDECREF(ast_Import);
        Py_XDECREF(ast_ImportFrom);
        Py_XDECREF(ast_Global);
        Py_XDECREF(ast_Nonlocal);
        Py_XDECREF(ast_Pass);
        Py_XDECREF(ast_Break);
        Py_XDECREF(ast_Continue);

        Py_XDECREF(ast_expr);
        Py_XDECREF(ast_Expr);
        Py_XDECREF(ast_BoolOp);
        Py_XDECREF(ast_NamedExpr);
        Py_XDECREF(ast_BinOp);
        Py_XDECREF(ast_UnaryOp);
        Py_XDECREF(ast_Lambda);
        Py_XDECREF(ast_IfExp);
        Py_XDECREF(ast_Dict);
        Py_XDECREF(ast_Set);
        Py_XDECREF(ast_ListComp);
        Py_XDECREF(ast_SetComp);
        Py_XDECREF(ast_DictComp);
        Py_XDECREF(ast_GeneratorExp);
        Py_XDECREF(ast_Await);
        Py_XDECREF(ast_Yield);
        Py_XDECREF(ast_YieldFrom);
        Py_XDECREF(ast_Compare);
        Py_XDECREF(ast_Call);
#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 6, 0)
        Py_XDECREF(ast_FormattedValue);
#endif
        Py_XDECREF(ast_JoinedStr);
        Py_XDECREF(ast_Constant);
        Py_XDECREF(ast_Attribute);
        Py_XDECREF(ast_Subscript);
        Py_XDECREF(ast_Starred);
        Py_XDECREF(ast_Name);
        Py_XDECREF(ast_List);
        Py_XDECREF(ast_Tuple);
        Py_XDECREF(ast_Slice);

        Py_XDECREF(ast_expr_context);
        Py_XDECREF(ast_Load);
        Py_XDECREF(ast_Store);
        Py_XDECREF(ast_Del);

        Py_XDECREF(ast_boolop);
        Py_XDECREF(ast_And);
        Py_XDECREF(ast_Or);

        Py_XDECREF(ast_operator);
        Py_XDECREF(ast_Add);
        Py_XDECREF(ast_Sub);
        Py_XDECREF(ast_Mult);
        Py_XDECREF(ast_MatMult);
        Py_XDECREF(ast_Div);
        Py_XDECREF(ast_Mod);
        Py_XDECREF(ast_Pow);
        Py_XDECREF(ast_LShift);
        Py_XDECREF(ast_RShift);
        Py_XDECREF(ast_BitOr);
        Py_XDECREF(ast_BitXor);
        Py_XDECREF(ast_BitAnd);
        Py_XDECREF(ast_FloorDiv);

        Py_XDECREF(ast_unaryop);
        Py_XDECREF(ast_Invert);
        Py_XDECREF(ast_Not);
        Py_XDECREF(ast_UAdd);
        Py_XDECREF(ast_USub);

        Py_XDECREF(ast_cmpop);
        Py_XDECREF(ast_Eq);
        Py_XDECREF(ast_NotEq);
        Py_XDECREF(ast_Lt);
        Py_XDECREF(ast_LtE);
        Py_XDECREF(ast_Gt);
        Py_XDECREF(ast_GtE);
        Py_XDECREF(ast_Is);
        Py_XDECREF(ast_IsNot);
        Py_XDECREF(ast_In);
        Py_XDECREF(ast_NotIn);

        Py_XDECREF(ast_comprehension);

        Py_XDECREF(ast_excepthandler);
        Py_XDECREF(ast_ExceptHandler);

        Py_XDECREF(ast_arguments);
        Py_XDECREF(ast_arg);
        Py_XDECREF(ast_keyword);
        Py_XDECREF(ast_alias);
        Py_XDECREF(ast_withitem);

#if PYTHON_VERSION >= QT_VERSION_CHECK(3, 10, 0)
        Py_XDECREF(ast_match_case);
        Py_XDECREF(ast_pattern);
        Py_XDECREF(ast_MatchValue);
        Py_XDECREF(ast_MatchSingleton);
        Py_XDECREF(ast_MatchSequence);
        Py_XDECREF(ast_MatchMapping);
        Py_XDECREF(ast_MatchClass);
        Py_XDECREF(ast_MatchStar);
        Py_XDECREF(ast_MatchAs);
        Py_XDECREF(ast_MatchOr);
#endif

        Py_XDECREF(ast_type_ignore);
        Py_XDECREF(ast_TypeIgnore);
#if PYTHON_VERSION < QT_VERSION_CHECK(3, 8, 0)
        Py_XDECREF(ast_Num);
        Py_XDECREF(ast_Str);
        Py_XDECREF(ast_Bytes);
#endif
    }
};

#undef Py_GRAMMAR_GET

} // end namespace Python
