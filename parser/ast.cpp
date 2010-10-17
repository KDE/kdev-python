/***************************************************************************
 *   This file is part of KDevelop                                         *
 *   Copyright 2007 Andreas Pakulat <apaku@gmx.de>                         *
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

namespace Python
{

// We never need actual constructors for AST nodes, but it seems to be required, at least for some platforms
// so we provide pseudo implementations
// there's nothing happening here, don't bother reading the code
    
Ast::Ast( Ast* parent, Ast::AstType type ) : parent(parent), astType( type ) { }
Ast::~Ast() { }
Identifier::Identifier(QString value) : value(value) { }
FunctionDefinitionAst::FunctionDefinitionAst(Ast* parent, Ast::AstType type): StatementAst(parent, type) { }
AssignmentAst::AssignmentAst(Ast* parent, Ast::AstType type): StatementAst(parent, type) { }
PrintAst::PrintAst(Ast* parent, Ast::AstType type): StatementAst(parent, type) { }
AttributeAst::AttributeAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, type) { }
CallAst::CallAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, type) { }
NameAst::NameAst(Ast* parent, Ast::AstType type): ExpressionAst(parent, type) { }
PassAst::PassAst(Ast* parent, Ast::AstType type): StatementAst(parent, type) { }
ArgumentsAst::ArgumentsAst(Ast* parent, Ast::AstType type): Ast(parent, type) { }
ExpressionAst::ExpressionAst(Ast* parent, Ast::AstType type): Ast(parent, type) { }
KeywordAst::KeywordAst(Ast* parent, Ast::AstType type): Ast(parent, type) { }
StatementAst::StatementAst(Ast* parent, Ast::AstType type): Ast(parent, type) { }


}


#include "pythonast.h"
