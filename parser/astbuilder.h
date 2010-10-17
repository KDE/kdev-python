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

typedef QMap<QString, QString> stringDictionary;

class AstBuilder
{
    
public:
    CodeAst* parse(KUrl filename);
private:
    CodeAst* parseXmlAst(QString xml);
    QString getXmlForFile(KUrl filename);
    void parseXmlAstNode(QXmlStreamReader* xmlast, QXmlStreamReader::TokenType token);
    bool parseAstNode(QString name, QString text, const QList<QXmlStreamAttribute>& attributes);
    
    QList<Ast*> m_nodeStack;
    
    // one map for regular ast nodes, and the others for primitive nodes of different types
    QMap<int, Ast*> m_nodeMap;
    QMap<int, ExpressionAst::Context> m_contextNodeMap;
    QMap<int, Ast::BooleanOperationTypes> m_boolOpNodeMap;
    QMap<int, Ast::ComparisonOperatorTypes> m_compOpNodeMap;
    QMap<int, Ast::OperatorTypes> m_opNodeMap;
    QMap<int, Ast::UnaryOperatorTypes> m_unaryOpNodeMap;
    
    QStack<Ast*> m_astStack;
    QMap<int, stringDictionary> m_attributeStore;
    Ast* m_currentNode;
    
    void populateAst();
    
    template<typename T> QList<T*> resolveNodeList(const QString& commaSeperatedIdentifiers);
    template<typename T> T* resolveNode(const QString& identifier);
    
    FunctionDefinitionAst* populateFunctionDefinitionAst(Ast* ast, const stringDictionary& currentAttributes);
};

}

#endif