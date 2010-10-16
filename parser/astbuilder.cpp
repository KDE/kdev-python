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

#include "astbuilder.h"

#include <QStringList>

#include "pythonparser.h"
#include "ast.h"

#include <kdebug.h>
#include <QProcess>
#include <QDomDocument>
#include "kurl.h"
#include <qxmlstream.h>
#include <QXmlStreamReader>

namespace Python
{
    
CodeAst* AstBuilder::parse(KUrl filename)
{
    return parseXmlAst(getXmlForFile(filename));
}
    
QString AstBuilder::getXmlForFile(KUrl filename)
{
    QProcess *parser = new QProcess();
    // we call a python script to parse the code for us. It returns an XML string with the AST
    parser->start("/home/sven/projects/kde4/python/pythonpythonparser.py", QStringList(filename.path())); // TODO fix this
    parser->waitForFinished();
    
    if ( parser->error() ) {
        kError() << parser->errorString();
        return "";
    }
    
    QString result = parser->readAllStandardOutput();
    kDebug() << "XML for " << filename << ":" << result;
    delete parser;
    return result;
}

CodeAst* AstBuilder::parseXmlAst(QString xml)
{
    QXmlStreamReader* xmlast = new QXmlStreamReader();
    xmlast->addData(xml);
    m_nodeMap = new QMap<int, Ast*>;
    
    parseXmlAstNode(xmlast, QXmlStreamReader::Invalid);
    
    Q_ASSERT(false);
}

void AstBuilder::parseXmlAstNode(QXmlStreamReader* xmlast, QXmlStreamReader::TokenType token) {
    while ( ! xmlast->atEnd() && ! xmlast->hasError() ) {
        // Advance to the next (first) token
        QXmlStreamReader::TokenType token = xmlast->readNext();
        
        // Store everything we need later into local variables
        QString currentElementName = xmlast->name().toString(); 
        QString currentElementText = xmlast->text().toString();
        QList<QXmlStreamAttribute> currentElementAttributes = xmlast->attributes().toList();
        
        // We ignore startDocument and EndDocument
        if ( token == QXmlStreamReader::StartDocument || token == QXmlStreamReader::EndDocument ) {
            continue;
        }
        // We recursively continue parsing if we find another element
        else if ( token == QXmlStreamReader::StartElement ) {
            parseXmlAstNode(xmlast, token);
        }
        // Everything else (stuff between tags, comments...) is ignored
        else continue;
        
        // Here we can now assemble an actual node with the attributes extracted above
        kDebug() << "Token: " << token << "; " << "Name: " << currentElementName << "; Text: " << currentElementText;
        for ( int i=0; i<currentElementAttributes.length(); i++ ) {
            kDebug() << currentElementAttributes.at(i).name() << currentElementAttributes.at(i).value();
        }
        
        parseAstNode(currentElementName, currentElementText, currentElementAttributes);
    }
}

void AstBuilder::parseAstNode(QString name, QString text, const QList< QXmlStreamAttribute >& attributes)
{
    Ast* ast;
    switch ( name ) {
        case "AssignAst":   ast = createAssignmentAst(name, text, attributes); break;
        case "NameAst":     ast = createIdentifierAst(name, text, attributes); break;
        case "StoreAst":    break;
        default:            kError() << "Unknown AST type" << name;
    }
}
    
}

