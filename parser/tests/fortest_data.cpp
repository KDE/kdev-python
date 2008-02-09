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

CodeAst* simpleForLoop()
{
    CodeAst* ast = createAstNode<CodeAst>( 0, 0, 0, 22, 2, 0 );
    ForAst* forast = createAstNode<ForAst>( 0, 0, 0, 22, 2, 0, ast );
    
    IdentifierTargetAst* target = createAstNode<IdentifierTargetAst>( 4, 0, 4, 4, 0, 4, forast );
    IdentifierAst* idast = createAstNode<IdentifierAst>( 4, 0, 4, 4, 0, 4, target );
    idast->identifier = "i";
    target->identifier = idast;
    forast->assignedTargets << target;
    
    AtomAst* atom = createAstNode<AtomAst>( 9, 0, 9, 12, 0, 12, forast );
    idast = createAstNode<IdentifierAst>( 9, 0, 9, 12, 0, 12, atom );
    idast->identifier = "list";
    atom->identifier = idast;
    forast->iterable << atom;
    
    StatementAst* pass = createAstNode<StatementAst>( 17, 1, 2, 20, 1, 5, Ast::PassAst, forast );
    forast->forBody << pass;
    ast->statements << forast;
    return ast;

}

