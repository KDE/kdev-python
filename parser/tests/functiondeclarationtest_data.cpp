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

#include "ast.h"

using namespace Python;

static void initAst( Ast* ast, qint64 s, qint64 sL, qint64 sC, qint64 e, qint64 eL, qint64 eC )
{
    ast->start = s;
    ast->startLine = sL;
    ast->startCol = sC;
    ast->end = e;
    ast->endLine = eL;
    ast->endCol = eC;
}

template <typename T> T* createAstNode( qint64 start, qint64 startLine, qint64 startCol,
                                        qint64 end, qint64 endLine, qint64 endCol,
                                        Ast::AstType type, Ast* parent )
{
    T* ast = new T( parent, type );
    initAst( ast, start, startLine, startCol, end, endLine, endCol );
    return ast;
}

template <typename T> T* createAstNode( qint64 start, qint64 startLine, qint64 startCol,
                                        qint64 end, qint64 endLine, qint64 endCol )
{
    T* ast = new T();
    initAst( ast, start, startLine, startCol, end, endLine, endCol );
    return ast;
}

template <typename T> T* createAstNode( qint64 start, qint64 startLine, qint64 startCol,
                                        qint64 end, qint64 endLine, qint64 endCol,
                                        Ast* parent )
{
    T* ast = new T( parent );
    initAst( ast, start, startLine, startCol, end, endLine, endCol );
    return ast;
}

template <typename T> T* createAstFrom( Ast* parent )
{
    return createAstNode<T>( parent->start, parent->startLine, parent->startCol, parent->end, parent->endLine, parent->endCol, parent );
}

CodeAst* simpleFunctionSingleParam()
{
    CodeAst* ast = createAstNode<CodeAst>( 0, 0, 0, -1, -1, -1 );
    FunctionDefinitionAst* funast = createAstNode<FunctionDefinitionAst>( 0, 0, 0, -1, -1, -1, ast );
    IdentifierAst* idast = createAstNode<IdentifierAst>( 4, 0, 4, 6, 0, 6, funast );
    idast->identifier = "foo";
    funast->functionName = idast;
    
    DefaultParameterAst* param = createAstNode<DefaultParameterAst>( 9, 0, 9, 11, 0, 11, funast );
    IdentifierParameterPartAst* idparam = createAstFrom<IdentifierParameterPartAst>( param );
    IdentifierAst* paramname = createAstNode<IdentifierAst>( 9, 0, 9, 9, 0, 9, idparam );
    paramname->identifier = "a";
    
    idparam->name = paramname;
    param->name = idparam;
    funast->parameters << param;
    
    StatementAst* pass = createAstNode<StatementAst>( 16, 1, 2, 20, 1, 6, Ast::PassAst, funast );
    funast->functionBody << pass;
    ast->statements << funast;
    return ast;
}

CodeAst* simpleFunctionNoParams()
{
    CodeAst* ast = createAstNode<CodeAst>( 0, 0, 0, -1, -1, -1 );
    FunctionDefinitionAst* funast = createAstNode<FunctionDefinitionAst>( 0, 0, 0, -1, -1, -1, ast );
    IdentifierAst* idast = createAstNode<IdentifierAst>( 4, 0, 4, 6, 0, 6, funast );
    idast->identifier = "foo";
    funast->functionName = idast;
    
    StatementAst* pass = createAstNode<StatementAst>( 13, 1, 2, 17, 1, 6, Ast::PassAst, funast );
    pass->astType = Ast::PassAst;
    
    funast->functionBody << pass;
    ast->statements << funast;
    return ast;
}

CodeAst* simpleFunctionDefaultParam()
{
    CodeAst* ast = createAstNode<CodeAst>( 0, 0, 0, -1, -1, -1 );
    FunctionDefinitionAst* funast = createAstNode<FunctionDefinitionAst>( 0, 0, 0, -1, -1, -1, ast );
    IdentifierAst* idast = createAstNode<IdentifierAst>( 4, 0, 4, 6, 0, 6, funast );
    idast->identifier = "foo";
    funast->functionName = idast;
    DefaultParameterAst* param = createAstNode<DefaultParameterAst>( 9, 0, 9, 17, 0, 17, funast );
    IdentifierParameterPartAst* idparam = createAstNode<IdentifierParameterPartAst>( 9, 0, 9, 10, 0, 10, param );
    IdentifierAst* paramname = createAstNode<IdentifierAst>( 9, 0, 9, 9, 0, 9, idparam );
    paramname->identifier = "a";
    
    AtomAst* atom = createAstNode<AtomAst>( 11, 0, 11, 17, 0, 17, param );
    
    LiteralAst* lit = createAstNode<LiteralAst>( 11, 0, 11, 17, 0, 17, atom );
    lit->literalType = LiteralAst::String;
    lit->value = "'bar'";
    
    atom->literal = lit;
    param->value = atom;
    
    idparam->name = paramname;
    param->name = idparam;
    funast->parameters << param;
    
    StatementAst* pass = createAstNode<StatementAst>( 22, 1, 2, 26, 1, 6, Ast::PassAst, funast );
    pass->astType = Ast::PassAst;
    
    funast->functionBody << pass;
    ast->statements << funast;
    return ast;
}

CodeAst* simpleFunctionListParam()
{
    CodeAst* ast = createAstNode<CodeAst>( 0, 0, 0, -1, -1, -1 );
    FunctionDefinitionAst* funast = createAstNode<FunctionDefinitionAst>( 0, 0, 0, -1, -1, -1, ast );
    IdentifierAst* idast = createAstNode<IdentifierAst>( 4, 0, 4, 6, 0, 6, funast );
    idast->identifier = "foo";
    funast->functionName = idast;
    
    ListParameterAst* param = createAstNode<ListParameterAst>( 9, 0, 9, 14, 0, 14, funast );
    IdentifierAst* paramname = createAstNode<IdentifierAst>( 10, 0, 10, 12, 0, 12, param );
    paramname->identifier = "bar";
    
    param->name = paramname;
    
    funast->parameters << param;
    
    StatementAst* pass = createAstNode<StatementAst>( 19, 1, 2, 23, 1, 6, Ast::PassAst, funast );
    pass->astType = Ast::PassAst;
    
    funast->functionBody << pass;
    ast->statements << funast;
    return ast;
}
