/***************************************************************************
 *   This file is part of KDevelop                                         *
 *   Copyright (C) 2007 Andreas Pakulat <apaku@gmx.de>                     *
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU Library General Public License as       *
 *   published by the Free Software Foundation; either version 2 of the    *
 *   License, or (at your option) any later version.                       *
 *                                                                         *
 *   This program is distributed in the hope that it will be useful,       *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
 *   GNU General Public License for more details.                          *
 *                                                                         *
 *   You should have received a copy of the GNU Library General Public     *
 *   License along with this program; if not, write to the                 *
 *   Free Software Foundation, Inc.,                                       *
 *   51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.         *
 ***************************************************************************/

#ifndef BUILDNEWASTVISITOR_H
#define BUILDNEWASTVISITOR_H

#include "python_default_visitor.h"

namespace Python
{

class BuildSimpleAstVisitor : default_visitor
{
public:
    virtual void visit_and_expr(and_expr_ast *node);
    virtual void visit_and_test(and_test_ast *node);
    virtual void visit_arg_list(arg_list_ast *node);
    virtual void visit_arglist(arglist_ast *node);
    virtual void visit_argument(argument_ast *node);
    virtual void visit_arith_expr(arith_expr_ast *node);
    virtual void visit_arith_op(arith_op_ast *node);
    virtual void visit_assert_stmt(assert_stmt_ast *node);
    virtual void visit_atom(atom_ast *node);
    virtual void visit_augassign(augassign_ast *node);
    virtual void visit_break_stmt(break_stmt_ast *node);
    virtual void visit_classdef(classdef_ast *node);
    virtual void visit_comp_op(comp_op_ast *node);
    virtual void visit_comparison(comparison_ast *node);
    virtual void visit_compound_stmt(compound_stmt_ast *node);
    virtual void visit_continue_stmt(continue_stmt_ast *node);
    virtual void visit_decorator(decorator_ast *node);
    virtual void visit_decorators(decorators_ast *node);
    virtual void visit_del_stmt(del_stmt_ast *node);
    virtual void visit_dictmaker(dictmaker_ast *node);
    virtual void visit_dotted_as_name(dotted_as_name_ast *node);
    virtual void visit_dotted_as_names(dotted_as_names_ast *node);
    virtual void visit_dotted_name(dotted_name_ast *node);
    virtual void visit_except_clause(except_clause_ast *node);
    virtual void visit_exec_stmt(exec_stmt_ast *node);
    virtual void visit_expr(expr_ast *node);
    virtual void visit_expr_stmt(expr_stmt_ast *node);
    virtual void visit_exprlist(exprlist_ast *node);
    virtual void visit_fact_op(fact_op_ast *node);
    virtual void visit_factor(factor_ast *node);
    virtual void visit_flow_stmt(flow_stmt_ast *node);
    virtual void visit_for_stmt(for_stmt_ast *node);
    virtual void visit_fp_def(fp_def_ast *node);
    virtual void visit_fpdef(fpdef_ast *node);
    virtual void visit_fplist(fplist_ast *node);
    virtual void visit_fun_pos_param(fun_pos_param_ast *node);
    virtual void visit_func_def(func_def_ast *node);
    virtual void visit_funcdef(funcdef_ast *node);
    virtual void visit_gen_for(gen_for_ast *node);
    virtual void visit_gen_if(gen_if_ast *node);
    virtual void visit_gen_iter(gen_iter_ast *node);
    virtual void visit_global_stmt(global_stmt_ast *node);
    virtual void visit_if_stmt(if_stmt_ast *node);
    virtual void visit_import_as_name(import_as_name_ast *node);
    virtual void visit_import_as_names(import_as_names_ast *node);
    virtual void visit_import_from(import_from_ast *node);
    virtual void visit_import_name(import_name_ast *node);
    virtual void visit_import_stmt(import_stmt_ast *node);
    virtual void visit_lambda_def(lambda_def_ast *node);
    virtual void visit_list_for(list_for_ast *node);
    virtual void visit_list_if(list_if_ast *node);
    virtual void visit_list_iter(list_iter_ast *node);
    virtual void visit_list_maker(list_maker_ast *node);
    virtual void visit_listmaker(listmaker_ast *node);
    virtual void visit_not_test(not_test_ast *node);
    virtual void visit_number(number_ast *node);
    virtual void visit_pass_stmt(pass_stmt_ast *node);
    virtual void visit_power(power_ast *node);
    virtual void visit_print_stmt(print_stmt_ast *node);
    virtual void visit_project(project_ast *node);
    virtual void visit_raise_stmt(raise_stmt_ast *node);
    virtual void visit_return_stmt(return_stmt_ast *node);
    virtual void visit_shift_expr(shift_expr_ast *node);
    virtual void visit_shift_op(shift_op_ast *node);
    virtual void visit_simple_stmt(simple_stmt_ast *node);
    virtual void visit_sliceop(sliceop_ast *node);
    virtual void visit_small_stmt(small_stmt_ast *node);
    virtual void visit_stmt(stmt_ast *node);
    virtual void visit_subscript(subscript_ast *node);
    virtual void visit_subscriptlist(subscriptlist_ast *node);
    virtual void visit_suite(suite_ast *node);
    virtual void visit_term(term_ast *node);
    virtual void visit_term_op(term_op_ast *node);
    virtual void visit_test(test_ast *node);
    virtual void visit_test_list_gexp(test_list_gexp_ast *node);
    virtual void visit_testlist(testlist_ast *node);
    virtual void visit_testlist1(testlist1_ast *node);
    virtual void visit_testlist_gexp(testlist_gexp_ast *node);
    virtual void visit_testlist_safe(testlist_safe_ast *node);
    virtual void visit_trailer(trailer_ast *node);
    virtual void visit_try_stmt(try_stmt_ast *node);
    virtual void visit_varargslist(varargslist_ast *node);
    virtual void visit_while_stmt(while_stmt_ast *node);
    virtual void visit_xor_expr(xor_expr_ast *node);
    virtual void visit_yield_stmt(yield_stmt_ast *node);
};

}

#endif

//kate: space-indent on; indent-width 4; replace-tabs on; auto-insert-doxygen on; indent-mode cstyle;
