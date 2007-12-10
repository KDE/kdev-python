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

AstVisitor::visitFunc _S_parser_table[] =  {

    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitArgument),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitArithmeticExpression),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitAssert),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitAssignment),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitAtom),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitAttributeReference),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitBinaryExpression),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitBooleanNotOperation),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitBooleanAndOperation),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitBooleanOrOperation),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitCall),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitClassDefinition),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitCode),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitComparison),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitConditionalExpression),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitDecorator),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitDefaultParameter),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitDel),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitDictionary),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitDictionaryParameter),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitEllipsisSlice),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitEnclosure),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitExcept),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitExec),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitExpression),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitExpressionSlice),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitExpressionStatement),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitExtendedSlice),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitFor),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitFromImport),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitFunctionDefinition),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitGenerator),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitGeneratorFor),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitGeneratorIf),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitGlobal),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitIdentifierParameterPart),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitIf),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitImport),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitLambda),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitList),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitListFor),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitListIf),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitListParameter),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitListParameterPart),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitParameter),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitParameterPart),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitPlainImport),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitPrimary),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitPrint),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitProperSliceItem),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitRaise),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitReturn),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitSimpleSlice),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitSlice),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitSliceItem),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitStarImport),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitStatement),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitSubscript),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitTarget),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitTry),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitUnaryExpression),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitWhile),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitWith),
    reinterpret_cast<AstVisitor::visitFunc>(&AstVisitor::visitYield),


};

void AstVisitor::visitNode( Ast* node )
{
    if  (node)
          (this->*_S_parser_table[node->astType])(node);
}

}
