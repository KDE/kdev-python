/***************************************************************************
 *   This file is part of KDevelop                                         *
 *   Copyright 2008 Andreas Pakulat <apaku@gmx.de>                         *
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

#include "datahelper.h"

using namespace Python;

CodeAst* simpleFunctionSingleParam()
{
    CodeAst* ast = createAstNode<CodeAst>( 0, 0, 0, 21, 2, 0 );
    FunctionDefinitionAst* funast = createAstNode<FunctionDefinitionAst>( 0, 0, 0, 21, 2, 0, ast );
    IdentifierAst* idast = createAstNode<IdentifierAst>( 4, 0, 4, 6, 0, 6, funast );
    idast->identifier = "foo";
    funast->functionName = idast;
    
    DefaultParameterAst* param = createAstNode<DefaultParameterAst>( 9, 0, 9, 9, 0, 9, funast );
    IdentifierParameterPartAst* idparam = createAstFrom<IdentifierParameterPartAst>( param );
    IdentifierAst* paramname = createAstNode<IdentifierAst>( 9, 0, 9, 9, 0, 9, idparam );
    paramname->identifier = "a";
    
    idparam->name = paramname;
    param->name = idparam;
    funast->parameters << param;
    
    StatementAst* pass = createAstNode<StatementAst>( 16, 1, 2, 19, 1, 5, Ast::PassAst, funast );
    funast->functionBody << pass;
    ast->statements << funast;
    return ast;
}

CodeAst* simpleFunctionNoParams()
{
    CodeAst* ast = createAstNode<CodeAst>( 0, 0, 0, 18, 2, 0 );
    FunctionDefinitionAst* funast = createAstNode<FunctionDefinitionAst>( 0, 0, 0, 18, 2, 0, ast );
    IdentifierAst* idast = createAstNode<IdentifierAst>( 4, 0, 4, 6, 0, 6, funast );
    idast->identifier = "foo";
    funast->functionName = idast;
    
    StatementAst* pass = createAstNode<StatementAst>( 13, 1, 2, 16, 1, 5, Ast::PassAst, funast );
    pass->astType = Ast::PassAst;
    
    funast->functionBody << pass;
    ast->statements << funast;
    return ast;
}

CodeAst* simpleFunctionDefaultParam()
{
    CodeAst* ast = createAstNode<CodeAst>( 0, 0, 0, 27, 2, 0 );
    FunctionDefinitionAst* funast = createAstNode<FunctionDefinitionAst>( 0, 0, 0, 27, 2, 0, ast );
    IdentifierAst* idast = createAstNode<IdentifierAst>( 4, 0, 4, 6, 0, 6, funast );
    idast->identifier = "foo";
    funast->functionName = idast;
    DefaultParameterAst* param = createAstNode<DefaultParameterAst>( 9, 0, 9, 15, 0, 15, funast );
    IdentifierParameterPartAst* idparam = createAstNode<IdentifierParameterPartAst>( 9, 0, 9, 9, 0, 9, param );
    IdentifierAst* paramname = createAstNode<IdentifierAst>( 9, 0, 9, 9, 0, 9, idparam );
    paramname->identifier = "a";
    
    AtomAst* atom = createAstNode<AtomAst>( 11, 0, 11, 15, 0, 15, param );
    
    LiteralAst* lit = createAstNode<LiteralAst>( 11, 0, 11, 15, 0, 15, atom );
    lit->literalType = LiteralAst::String;
    lit->value = "'bar'";
    
    atom->literal = lit;
    param->value = atom;
    
    idparam->name = paramname;
    param->name = idparam;
    funast->parameters << param;
    
    StatementAst* pass = createAstNode<StatementAst>( 22, 1, 2, 25, 1, 5, Ast::PassAst, funast );
    pass->astType = Ast::PassAst;
    
    funast->functionBody << pass;
    ast->statements << funast;
    return ast;
}

CodeAst* simpleFunctionListParam()
{
    CodeAst* ast = createAstNode<CodeAst>( 0, 0, 0, 24, 2, 0 );
    FunctionDefinitionAst* funast = createAstNode<FunctionDefinitionAst>( 0, 0, 0, 24, 2, 0, ast );
    IdentifierAst* idast = createAstNode<IdentifierAst>( 4, 0, 4, 6, 0, 6, funast );
    idast->identifier = "foo";
    funast->functionName = idast;
    
    ListParameterAst* param = createAstNode<ListParameterAst>( 9, 0, 9, 12, 0, 12, funast );
    IdentifierAst* paramname = createAstNode<IdentifierAst>( 10, 0, 10, 12, 0, 12, param );
    paramname->identifier = "bar";
    
    param->name = paramname;
    
    funast->parameters << param;
    
    StatementAst* pass = createAstNode<StatementAst>( 19, 1, 2, 22, 1, 5, Ast::PassAst, funast );
    pass->astType = Ast::PassAst;
    
    funast->functionBody << pass;
    ast->statements << funast;
    return ast;
}


CodeAst* simpleFunctionDictParam()
{
    CodeAst* ast = createAstNode<CodeAst>( 0, 0, 0, 25, 2, 0 );
    FunctionDefinitionAst* funast = createAstNode<FunctionDefinitionAst>( 0, 0, 0, 25, 2, 0, ast );
    IdentifierAst* idast = createAstNode<IdentifierAst>( 4, 0, 4, 6, 0, 6, funast );
    idast->identifier = "foo";
    funast->functionName = idast;
    
    DictionaryParameterAst* param = createAstNode<DictionaryParameterAst>( 9, 0, 9, 13, 0, 13, funast );
    IdentifierAst* paramname = createAstNode<IdentifierAst>( 11, 0, 11, 13, 0, 13, param );
    paramname->identifier = "bar";
    
    param->name = paramname;
    
    funast->parameters << param;
    
    StatementAst* pass = createAstNode<StatementAst>( 20, 1, 2, 23, 1, 5, Ast::PassAst, funast );
    pass->astType = Ast::PassAst;
    
    funast->functionBody << pass;
    ast->statements << funast;
    return ast;
}

CodeAst* simpleFunctionTwoParam()
{
    CodeAst* ast = createAstNode<CodeAst>( 0, 0, 0, 24, 2, 0 );
    FunctionDefinitionAst* funast = createAstNode<FunctionDefinitionAst>( 0, 0, 0, 24, 2, 0, ast );
    IdentifierAst* idast = createAstNode<IdentifierAst>( 4, 0, 4, 6, 0, 6, funast );
    idast->identifier = "foo";
    funast->functionName = idast;
    
    DefaultParameterAst* param = createAstNode<DefaultParameterAst>( 9, 0, 9, 9, 0, 9, funast );
    IdentifierParameterPartAst* idparam = createAstFrom<IdentifierParameterPartAst>( param );
    IdentifierAst* paramname = createAstNode<IdentifierAst>( 9, 0, 9, 9, 0, 9, idparam );
    paramname->identifier = "a";
    
    idparam->name = paramname;
    param->name = idparam;
    funast->parameters << param;
    
    param = createAstNode<DefaultParameterAst>( 12, 0, 12, 12, 0, 12, funast );
    idparam = createAstFrom<IdentifierParameterPartAst>( param );
    paramname = createAstNode<IdentifierAst>( 12, 0, 12, 12, 0, 12, idparam );
    paramname->identifier = "b";
    
    idparam->name = paramname;
    param->name = idparam;
    funast->parameters << param;
    
    StatementAst* pass = createAstNode<StatementAst>( 19, 1, 2, 22, 1, 5, Ast::PassAst, funast );
    funast->functionBody << pass;
    ast->statements << funast;
    return ast;
}

CodeAst* simpleFunctionTwoLongParam()
{
    CodeAst* ast = createAstNode<CodeAst>( 0, 0, 0, 31, 2, 0 );
    FunctionDefinitionAst* funast = createAstNode<FunctionDefinitionAst>( 0, 0, 0, 31, 2, 0, ast );
    IdentifierAst* idast = createAstNode<IdentifierAst>( 4, 0, 4, 6, 0, 6, funast );
    idast->identifier = "foo";
    funast->functionName = idast;
    
    DefaultParameterAst* param = createAstNode<DefaultParameterAst>( 9, 0, 9, 13, 0, 13, funast );
    IdentifierParameterPartAst* idparam = createAstFrom<IdentifierParameterPartAst>( param );
    IdentifierAst* paramname = createAstNode<IdentifierAst>( 9, 0, 9, 13, 0, 13, idparam );
    paramname->identifier = "alpha";
    
    idparam->name = paramname;
    param->name = idparam;
    funast->parameters << param;
    
    param = createAstNode<DefaultParameterAst>( 16, 0, 16, 19, 0, 19, funast );
    idparam = createAstFrom<IdentifierParameterPartAst>( param );
    paramname = createAstNode<IdentifierAst>( 16, 0, 16, 19, 0, 19, idparam );
    paramname->identifier = "beta";
    
    idparam->name = paramname;
    param->name = idparam;
    funast->parameters << param;
    
    StatementAst* pass = createAstNode<StatementAst>( 26, 1, 2, 29, 1, 5, Ast::PassAst, funast );
    funast->functionBody << pass;
    ast->statements << funast;
    return ast;
}

CodeAst* simpleFunctionListAndDictParam()
{
    CodeAst* ast = createAstNode<CodeAst>( 0, 0, 0, 30, 2, 0 );
    FunctionDefinitionAst* funast = createAstNode<FunctionDefinitionAst>( 0, 0, 0, 30, 2, 0, ast );
    IdentifierAst* idast = createAstNode<IdentifierAst>( 4, 0, 4, 6, 0, 6, funast );
    idast->identifier = "foo";
    funast->functionName = idast;
    
    DefaultParameterAst* param = createAstNode<DefaultParameterAst>( 9, 0, 9, 9, 0, 9, funast );
    IdentifierParameterPartAst* idparam = createAstFrom<IdentifierParameterPartAst>( param );
    IdentifierAst* paramname = createAstNode<IdentifierAst>( 9, 0, 9, 9, 0, 9, idparam );
    paramname->identifier = "a";
    
    idparam->name = paramname;
    param->name = idparam;
    funast->parameters << param;
    
    ListParameterAst* lparam = createAstNode<ListParameterAst>( 12, 0, 12, 13, 0, 13, funast );
    paramname = createAstNode<IdentifierAst>( 13, 0, 13, 13, 0, 13, lparam );
    paramname->identifier = "b";
    
    lparam->name = paramname;
    funast->parameters << lparam;
    
    DictionaryParameterAst* dparam = createAstNode<DictionaryParameterAst>( 16, 0, 16, 18, 0, 18, funast );
    paramname = createAstNode<IdentifierAst>( 18, 0, 18, 18, 0, 18, dparam );
    paramname->identifier = "c";
    
    dparam->name = paramname;
    funast->parameters << dparam;
    
    StatementAst* pass = createAstNode<StatementAst>( 25, 1, 2, 28, 1, 5, Ast::PassAst, funast );
    funast->functionBody << pass;
    ast->statements << funast;
    return ast;
}

CodeAst* simpleFunctionCombinedDictParam()
{
    CodeAst* ast = createAstNode<CodeAst>( 0, 0, 0, 26, 2, 0 );
    FunctionDefinitionAst* funast = createAstNode<FunctionDefinitionAst>( 0, 0, 0, 26, 2, 0, ast );
    IdentifierAst* idast = createAstNode<IdentifierAst>( 4, 0, 4, 6, 0, 6, funast );
    idast->identifier = "foo";
    funast->functionName = idast;
    
    DefaultParameterAst* param = createAstNode<DefaultParameterAst>( 9, 0, 9, 9, 0, 9, funast );
    IdentifierParameterPartAst* idparam = createAstFrom<IdentifierParameterPartAst>( param );
    IdentifierAst* paramname = createAstNode<IdentifierAst>( 9, 0, 9, 9, 0, 9, idparam );
    paramname->identifier = "a";
    
    idparam->name = paramname;
    param->name = idparam;
    funast->parameters << param;
    
    DictionaryParameterAst* dparam = createAstNode<DictionaryParameterAst>( 12, 0, 12, 14, 0, 14, funast );
    paramname = createAstNode<IdentifierAst>( 14, 0, 14, 14, 0, 14, dparam );
    paramname->identifier = "b";
    
    dparam->name = paramname;
    funast->parameters << dparam;
    
    StatementAst* pass = createAstNode<StatementAst>( 21, 1, 2, 24, 1, 5, Ast::PassAst, funast );
    funast->functionBody << pass;
    ast->statements << funast;
    return ast;
}

CodeAst* simpleFunctionCombinedListParam()
{
    CodeAst* ast = createAstNode<CodeAst>( 0, 0, 0, 25, 2, 0 );
    FunctionDefinitionAst* funast = createAstNode<FunctionDefinitionAst>( 0, 0, 0, 25, 2, 0, ast );
    IdentifierAst* idast = createAstNode<IdentifierAst>( 4, 0, 4, 6, 0, 6, funast );
    idast->identifier = "foo";
    funast->functionName = idast;
    
    DefaultParameterAst* param = createAstNode<DefaultParameterAst>( 9, 0, 9, 9, 0, 9, funast );
    IdentifierParameterPartAst* idparam = createAstFrom<IdentifierParameterPartAst>( param );
    IdentifierAst* paramname = createAstNode<IdentifierAst>( 9, 0, 9, 9, 0, 9, idparam );
    paramname->identifier = "a";
    
    idparam->name = paramname;
    param->name = idparam;
    funast->parameters << param;
    
    ListParameterAst* lparam = createAstNode<ListParameterAst>( 12, 0, 12, 13, 0, 13, funast );
    paramname = createAstNode<IdentifierAst>( 13, 0, 13, 13, 0, 13, lparam );
    paramname->identifier = "b";
    
    lparam->name = paramname;
    funast->parameters << lparam;
    
    StatementAst* pass = createAstNode<StatementAst>( 20, 1, 2, 23, 1, 5, Ast::PassAst, funast );
    funast->functionBody << pass;
    ast->statements << funast;
    return ast;
}
