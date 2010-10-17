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

#ifndef ASTBUILDER_H
#define ASTBUILDER_H

#include <QtCore/QStack>

#include "ast.h"
#include <kurl.h>
#include <QDomDocument>
#include "kdebug.h"
#include "QXmlStreamReader"

namespace PythonParser
{
    class Parser;
    class AstNode;
}

namespace Python
{
    class Ast;
    class CodeAst;


class AstBuilder
{
    
public:
    CodeAst* parse(KUrl filename);
private:
    CodeAst* parseXmlAst(QString xml);
    QString getXmlForFile(KUrl filename);
    void parseXmlAstNode(QXmlStreamReader* xmlast, QXmlStreamReader::TokenType token);
    void parseAstNode(QString name, QString text, const QList<QXmlStreamAttribute>& attributes);
    
    QList<Ast*> m_nodeStack;
    
    template <typename ASTType> ASTType* createAst(QDomElement* startEnd = 0) {
        ASTType* ast = new ASTType();
        if ( startEnd ) {
            kDebug() << "would set start end now";
        }
    }
    
    QMap<int, Ast*> m_nodeMap;
    QStack<Ast*> m_astStack;
    
    void populateAst();
};

}

#endif