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

#include "astprinter.h"

#include <kdebug.h>

namespace Python
{

static QString names[] = {
"Argument",
"Assert",
"Assignment",
"Atom",
"AttributeReference",
"AttributeReferenceTarget",
"BinaryExpression",
"BooleanNotOperation",
"BooleanAndOperation",
"BooleanOrOperation",
"Break",
"Call",
"ClassDefinition",
"Code",
"Comparison",
"ConditionalExpression",
"Continue",
"Decorator",
"DefaultParameter",
"Del",
"Dictionary",
"DictionaryParameter",
"EllipsisSliceItem",
"Enclosure",
"Except",
"Exec",
"ExpressionSliceItem",
"ExpressionStatement",
"ExtendedSlice",
"For",
"FromImport",
"FunctionDefinition",
"Generator",
"GeneratorFor",
"GeneratorIf",
"Global",
"Identifier",
"IdentifierParameterPart",
"IdentifierTarget",
"If",
"Lambda",
"List",
"ListFor",
"ListIf",
"ListParameter",
"ListParameterPart",
"ListTarget",
"Literal",
"Pass",
"PlainImport",
"Print",
"ProperSliceItem",
"Raise",
"Return",
"SimpleSlice",
"SliceTarget",
"StarImport",
"Subscript",
"SubscriptTarget",
"TupleTarget",
"Try",
"UnaryExpression",
"While",
"With",
"Yield",
};

AstPrinter::AstPrinter()
    : AstDefaultVisitor(), indent( 0 )
{
}

AstPrinter::~AstPrinter()
{
}

void AstPrinter::visitNode( Ast* node )
{
    if( node )
    {
        kDebug() << indentation() + "\\ " + names[node->astType] + "[(" + QString::number( node->start ) + ")]";
        ++indent;
    }
    AstDefaultVisitor::visitNode( node );
    if(node)
    {
        --indent;
        kDebug() << indentation() + "/ " + names[node->astType] + "[(" + QString::number( node->end ) + ")]";
    }
}

QString AstPrinter::indentation() const
{
    QString s;
    for( int a = 0; a < indent; a++ )
        s += "| ";
    return s;
}

void AstPrinter::visitIdentifier( IdentifierAst * ast )
{
    kDebug() << indentation() + "  Identifier ==" << ast->identifier;
}

void AstPrinter::visitLiteral( LiteralAst * ast )
{
    kDebug() << indentation() + "  literal type ==" << ast->literalType;
    kDebug() << indentation() + "  Literal ==" << ast->value;
}

void AstPrinter::visitArgument( ArgumentAst* node )
{
    kDebug() << indentation() + "  ArgumentType ==" << node->argumentType;
    AstDefaultVisitor::visitArgument( node );
}

void AstPrinter::visitFromImport( FromImportAst* node )
{
    kDebug() << indentation() + "  leading dots ==" << node->numLeadingDots;
    AstDefaultVisitor::visitFromImport( node );
}

void AstPrinter::visitAssignment( AssignmentAst* node )
{
    QList<QPair<QList<TargetAst*>, AssignmentAst::OpType > >::const_iterator it;
    QList<QPair<QList<TargetAst*>, AssignmentAst::OpType > >::const_iterator end;
    it = node->targets.begin();
    end = node->targets.end();
    for( ; it != end; ++it )
    {
        QList<TargetAst*> tl = (*it).first;
        foreach( TargetAst* t, tl )
        {
            visitNode( t );
        }
        kDebug() << indentation() + "  op type ==" << (*it).second;
    }
    
    foreach( ExpressionAst* e, node->value )
    {
        visitNode( e );
    }
    visitNode( node->yieldValue );
}

void AstPrinter::visitEnclosure( EnclosureAst* node )
{
    kDebug() << indentation() + "  enclosure type ==" << node->encType;
    AstDefaultVisitor::visitEnclosure( node );
}

void AstPrinter::visitComparison( ComparisonAst* node )
{
    visitNode( node->firstComparator );
    QList< QPair< ComparisonAst::ComparisonOperator, ExpressionAst*> >::iterator it;
    QList< QPair< ComparisonAst::ComparisonOperator, ExpressionAst*> >::iterator end = node->comparatorList.end();
    for( it = node->comparatorList.begin(); it != end; ++it )
    {
        kDebug() << indentation() + "  comparison type" << (*it).first;
        visitNode( (*it).second );
    }
}

void AstPrinter::visitBinaryExpression( BinaryExpressionAst* node )
{
    kDebug() << indentation() + "  binary op ==" << node->opType;
    AstDefaultVisitor::visitBinaryExpression( node );
}

void AstPrinter::visitUnaryExpression( UnaryExpressionAst* node )
{
    kDebug() << indentation() + "  binary op ==" << node->opType;
    AstDefaultVisitor::visitUnaryExpression( node );
}

}
