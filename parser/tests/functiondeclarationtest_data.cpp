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

CodeAst* simpleFunctionSingleParam()
{
    CodeAst* ast = new CodeAst();
    ast->start = 0;
    ast->startLine = 0;
    ast->startCol = 0;
    ast->end = -1;
    ast->endLine = -1;
    ast->endCol = -1;
    FunctionDefinitionAst* funast = new FunctionDefinitionAst( ast );
    funast->startLine = 0;
    funast->endLine = 1;
    funast->start = 0;
    funast->startCol = 0;
    funast->endCol = 6;
    funast->end = 16;
    IdentifierAst* idast = new IdentifierAst( funast );
    idast->startLine = 0;
    idast->startCol = 4;
    idast->start = 4;
    idast->endLine = 0;
    idast->endCol = 6;
    idast->end = 6;
    idast->identifier = "foo";
    funast->functionName = idast;
    StatementAst* pass = new StatementAst( funast, Ast::PassAst );
    pass->startLine = 1;
    pass->startCol = 2;
    pass->start = 13;
    pass->end = 16;
    pass->endLine = 1;
    pass->endCol = 5;
    funast->functionBody << pass;
    ast->statements << funast;
    return ast;
}

CodeAst* simpleFunctionNoParams()
{
    CodeAst* ast = new CodeAst();
    ast->start = 0;
    ast->startLine = 0;
    ast->startCol = 0;
    ast->end = -1;
    ast->endLine = -1;
    ast->endCol = -1;
    FunctionDefinitionAst* funast = new FunctionDefinitionAst( ast );
    funast->startLine = 0;
    funast->endLine = 1;
    funast->start = 0;
    funast->startCol = 0;
    funast->endCol = 6;
    funast->end = 16;
    IdentifierAst* idast = new IdentifierAst( funast );
    idast->startLine = 0;
    idast->startCol = 4;
    idast->start = 4;
    idast->endLine = 0;
    idast->endCol = 6;
    idast->end = 6;
    idast->identifier = "foo";
    funast->functionName = idast;
    DefaultParameterAst* param = new DefaultParameterAst( funast );
    param->start = 9;
    param->startLine = 0;
    param->startCol = 9;
    param->endLine = 0;
    param->endCol = 10;
    param->end = 10;
    IdentifierParameterPartAst* idparam = new IdentifierParameterPartAst( param );
    idparam->start = 9;
    idparam->startLine = 0;
    idparam->startCol = 9;
    idparam->endLine = 0;
    idparam->endCol = 10;
    idparam->end = 10;
    IdentifierAst* paramname = new IdentifierAst( idparam );
    paramname->start = 9;
    paramname->startLine = 0;
    paramname->startCol = 9;
    paramname->endLine = 0;
    paramname->endCol = 10;
    paramname->end = 10;
    
    idparam->name = paramname;
    param->name = idparam;
    
    funast->parameters << param;
    
    StatementAst* pass = new StatementAst( funast, Ast::PassAst );
    pass->startLine = 1;
    pass->startCol = 2;
    pass->start = 13;
    pass->end = 16;
    pass->endLine = 1;
    pass->endCol = 5;
    funast->functionBody << pass;
    ast->statements << funast;
    return ast;
}
