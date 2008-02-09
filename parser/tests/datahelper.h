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

#ifndef DATAHELPER_H
#define DATAHELPER_H

#include "ast.h"
#include "pythondriver.h"
#include "testvisitor.h"

static void doTest( const QString& project, Python::CodeAst* expected )
{
    Python::Driver d;
    Python::CodeAst* result;
    d.setContent( project );
//     d.setDebug( true );
    d.parse( &result );
    TestVisitor tv;
    tv.setExpected( expected );
    tv.visitCode( result );
}

static void initAst( Python::Ast* ast, qint64 s, qint64 sL, qint64 sC, qint64 e, qint64 eL, qint64 eC )
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
                                        Python::Ast::AstType type, Python::Ast* parent )
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
                                        Python::Ast* parent )
{
    T* ast = new T( parent );
    initAst( ast, start, startLine, startCol, end, endLine, endCol );
    return ast;
}

template <typename T> T* createAstFrom( Python::Ast* parent )
{
    return createAstNode<T>( parent->start, parent->startLine, parent->startCol, parent->end, parent->endLine, parent->endCol, parent );
}



#endif
