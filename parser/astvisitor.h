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

#ifndef PYTHONASTVISITOR_H
#define PYTHONASTVISITOR_H

#include "ast.h"
#include "parserexport.h"

namespace Python
{

class KDEVPYTHONPARSER_EXPORT AstVisitor
{
public:
    virtual ~AstVisitor() {}

    typedef void (AstVisitor::*visitFunc)(Ast *);
    
    void visitNode(Ast* node);

    virtual void visitCode(CodeAst* node);
    virtual void visitFunctionDefinition(FunctionDefinitionAst* node);
    virtual void visitPrint(PrintAst* node);
    virtual void visitAssignment(AssignmentAst* node);
    virtual void visitCall(CallAst* node);
    virtual void visitPass(StatementAst* node);
    virtual void visitName(NameAst* node);
    virtual void visitAttribute(AttributeAst* node);
    virtual void visitKeyword(KeywordAst* node);
    virtual void visitArguments(ArgumentsAst* node);
};
}

#endif
