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

#ifndef ASTPRINTER_H
#define ASTPRINTER_H

#include "astdefaultvisitor.h"
#include "parserexport.h"

namespace Python
{

class KDEVPYTHONPARSER_EXPORT AstPrinter : public AstDefaultVisitor
{
public:
    AstPrinter();
    ~AstPrinter();
    virtual void visitIdentifier( IdentifierAst* ast );
    virtual void visitLiteral( LiteralAst* ast );
    virtual void visitNode( Ast* ast );
    virtual void visitUnaryExpression( UnaryExpressionAst* node );
    virtual void visitBinaryExpression( BinaryExpressionAst* node );
    virtual void visitComparison( ComparisonAst* node );
    virtual void visitEnclosure( EnclosureAst* node );
    virtual void visitAssignment( AssignmentAst* node );
    virtual void visitFromImport( FromImportAst* node );
    virtual void visitArgument( ArgumentAst* node );
    
private:
    QString indentation() const;
    int indent;
};

}

#endif
