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

#include "astvisitor.h"

namespace Python
{
    
AstVisitor::AstVisitor() { }
AstVisitor::~AstVisitor() { }


void AstVisitor::visitNode(Ast* node)
{
    if ( ! node ) return;
    switch ( node->astType ) {
        case Ast::ArgumentsAstType:             AstVisitor::visitArguments(dynamic_cast<ArgumentsAst*>(node)); break;
        case Ast::AssignmentAstType:            AstVisitor::visitAssignment(dynamic_cast<AssignmentAst*>(node)); break;
        case Ast::AttributeAstType:             AstVisitor::visitAttribute(dynamic_cast<AttributeAst*>(node)); break;
        case Ast::CallAstType:                  AstVisitor::visitCall(dynamic_cast<CallAst*>(node)); break;
        case Ast::FunctionDefinitionAstType:    AstVisitor::visitFunctionDefinition(dynamic_cast<FunctionDefinitionAst*>(node)); break;
        case Ast::KeywordAstType:               AstVisitor::visitKeyword(dynamic_cast<KeywordAst*>(node)); break;
        case Ast::NameAstType:                  AstVisitor::visitName(dynamic_cast<NameAst*>(node)); break;
        case Ast::PassAstType:                  AstVisitor::visitPass(dynamic_cast<PassAst*>(node)); break;
        case Ast::PrintAstType:                 AstVisitor::visitPrint(dynamic_cast<PrintAst*>(node)); break;
        case Ast::ExpressionAstType:            break;
    }
}

}
