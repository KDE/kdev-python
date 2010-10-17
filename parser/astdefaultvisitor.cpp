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

#include "astdefaultvisitor.h"

namespace Python
{

AstDefaultVisitor::AstDefaultVisitor() : AstVisitor() { }
AstDefaultVisitor::~AstDefaultVisitor() { }

// The Ast "ends" here, those dont have child nodes
// note that Identifier is not a node in this Ast
void AstDefaultVisitor::visitName(NameAst* node) { }
void AstDefaultVisitor::visitPass(StatementAst* node) { }


void AstDefaultVisitor::visitCode(CodeAst* node)
{
    foreach (StatementAst* statement, node->body) {
        visitNode(statement);
    }
}

void AstDefaultVisitor::visitAssignment(AssignmentAst* node)
{
    foreach (ExpressionAst* expression, node->targets) {
        visitNode(expression);
    };
    visitNode(node->value);
}

void AstDefaultVisitor::visitPrint(PrintAst* node)
{
    visitNode(node->destination);
    foreach (ExpressionAst* expression, node->values) {
        visitNode(expression);
    }
}

void AstDefaultVisitor::visitCall(CallAst* node)
{
    visitNode(node->function);
    visitNode(node->keywordArguments);
    visitNode(node->starArguments);
    foreach (ExpressionAst* argument, node->arguments) {
        visitNode(node->arguments);
    }
    visitNode(node->arguments);
}

void AstDefaultVisitor::visitFunctionDefinition(FunctionDefinitionAst* node)
{
    visitNode(node->arguments);
}

void AstDefaultVisitor::visitAttribute(AttributeAst* node)
{
    visitNode(node->value);
}

void AstDefaultVisitor::visitKeyword(KeywordAst* node)
{
    visitNode(node->value);
}

void AstDefaultVisitor::visitArguments(ArgumentsAst* node)
{
    foreach (ExpressionAst* expression, node->arguments) {
        visitNode(expression);
    }
}

}

