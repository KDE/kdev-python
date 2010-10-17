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
    QProcess* parser = new QProcess();
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
    
    m_nodeMap.clear();
    
    parseXmlAstNode(xmlast, QXmlStreamReader::Invalid);
    
    Q_ASSERT(false);
}

void AstBuilder::parseXmlAstNode(QXmlStreamReader* xmlast, QXmlStreamReader::TokenType token = QXmlStreamReader::Invalid) {
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
            // Here we can now assemble an actual node with the attributes extracted above
            kDebug() << "Token: " << token << "; " << "Name: " << currentElementName << "; Text: " << currentElementText;
            for ( int i=0; i<currentElementAttributes.length(); i++ ) {
                kDebug() << currentElementAttributes.at(i).name() << currentElementAttributes.at(i).value();
            }
            
            // this will push a parent onto the stack
            parseAstNode(currentElementName, currentElementText, currentElementAttributes);
            
            parseXmlAstNode(xmlast, token);
            
            // now we pop this parent off
            m_nodeStack.removeLast();
        }
        // Everything else (stuff between tags, comments...) is ignored
        else continue;
    }
}

void AstBuilder::parseAstNode(QString name, QString text, const QList< QXmlStreamAttribute >& attributes)
{
    Ast* ast;
    
    QMap<QString, QString> attributeDict;
    
    for ( int i=0; i<attributes.length(); i++ ) {
        attributeDict.insert(attributes.at(i).name().toString(), attributes.at(i).value().toString());
    }
    
    // TODO think about a less explicit way to do this
    // things in the comments are definitely found like this in the XML file
    name = name.toLower();
    if      ( name == "aliasast" ) ast = new AliasAst(m_nodeStack.last()); // aliasAst
    else if ( name == "argumentsast" ) ast = new ArgumentsAst(m_nodeStack.last()); // argumentsAst
    else if ( name == "assertast" ) ast = new AssertionAst(m_nodeStack.last()); // assertAst
    else if ( name == "assignast" ) ast = new AssignmentAst(m_nodeStack.last()); // assignAst
    else if ( name == "attributeast" ) ast = new AttributeAst(m_nodeStack.last()); // attributeAst
    else if ( name == "augassignast" ) ast = new AugmentedAssignmentAst(m_nodeStack.last()); // augassignast
    else if ( name == "binopast" ) ast = new BinaryOperationAst(m_nodeStack.last()); // binOpAst
    else if ( name == "boolopast" ) ast = new BooleanOperationAst(m_nodeStack.last()); // boolOpAst
    else if ( name == "breakast" ) ast = new BreakAst(m_nodeStack.last()); // breakAst
    else if ( name == "callast" ) ast = new CallAst(m_nodeStack.last()); // callAst
    else if ( name == "classdefast" ) ast = new ClassDefinitionAst(m_nodeStack.last()); // classDefAst
    else if ( name == "moduleast" ) ast = new CodeAst(); // moduleAst
    else if ( name == "compareast" ) ast = new CompareAst(m_nodeStack.last()); // compareAst
    else if ( name == "comprehensionast" ) ast = new ComprehensionAst(m_nodeStack.last()); // comprehensionAst
    else if ( name == "continueast" ) ast = new ContinueAst(m_nodeStack.last()); // continueAst
    else if ( name == "deleteast" ) ast = new DeleteAst(m_nodeStack.last()); // deleteAst
    else if ( name == "dictast" ) ast = new DictAst(m_nodeStack.last()); // dictAst
//     else if ( name == "dictionarycomprehensionast" ) ast = new DictionaryComprehensionAst(m_nodeStack.last()); // TODO support this for python 2.7+
    else if ( name == "ellipsisast" ) ast = new EllipsisAst(m_nodeStack.last()); // ellipsisAst
    else if ( name == "excepthandlerast" ) ast = new ExceptionHandlerAst(m_nodeStack.last()); // exceptHandlerAst
    else if ( name == "execast" ) ast = new ExecAst(m_nodeStack.last()); // execAst
    else if ( name == "exprast" ) ast = new ExpressionAst(m_nodeStack.last()); // exprast
    else if ( name == "extsliceast" ) ast = new ExtendedSliceAst(m_nodeStack.last()); // extsliceast
    else if ( name == "forast" ) ast = new ForAst(m_nodeStack.last()); // forAst
    else if ( name == "functiondefast" ) ast = new FunctionDefinitionAst(m_nodeStack.last()); // functionDefAst
//     else if ( name == "generatorexpressionast" ) ast = new GeneratorExpressionAst(m_nodeStack.last()); // TODO check this
    else if ( name == "globalast" ) ast = new GlobalAst(m_nodeStack.last()); // globalAst
    else if ( name == "ifast" ) ast = new IfAst(m_nodeStack.last()); // ifAst
    else if ( name == "ifexpast" ) ast = new IfExpressionAst(m_nodeStack.last()); // ifExpAst
    else if ( name == "importast" ) ast = new ImportAst(m_nodeStack.last()); // importAst
    else if ( name == "importfromast" ) ast = new ImportFromAst(m_nodeStack.last()); // importFromAst
    else if ( name == "indexast" ) ast = new IndexAst(m_nodeStack.last()); // indexAst
    else if ( name == "keywordast" ) ast = new KeywordAst(m_nodeStack.last()); // keywordAst
    else if ( name == "lambdaast" ) ast = new LambdaAst(m_nodeStack.last()); // lambdaAst
    else if ( name == "listast" ) ast = new ListAst(m_nodeStack.last()); // listAst
    else if ( name == "listcompast" ) ast = new ListComprehensionAst(m_nodeStack.last()); // listCompAst
    else if ( name == "nameast" ) ast = new NameAst(m_nodeStack.last()); // nameAst
    else if ( name == "numast" ) ast = new NumberAst(m_nodeStack.last()); // numAst
    else if ( name == "passast" ) ast = new PassAst(m_nodeStack.last());  // passAst
    else if ( name == "printast" ) ast = new PrintAst(m_nodeStack.last()); // printAst
    else if ( name == "raiseast" ) ast = new RaiseAst(m_nodeStack.last());  // raiseAst
//     else if ( name == "reprast" ) ast = new ReprAst(m_nodeStack.last()); // TODO what's this?
    else if ( name == "returnast" ) ast = new ReturnAst(m_nodeStack.last()); // returnAst
//     else if ( name == "setast" ) ast = new SetAst(m_nodeStack.last()); // TODO support this for python 2.7+
//     else if ( name == "setcomprehensionast" ) ast = new SetComprehensionAst(m_nodeStack.last()); // TODO support this for python 2.7+
    else if ( name == "sliceast" ) ast = new SliceAst(m_nodeStack.last()); // sliceAst
    else if ( name == "strast" ) ast = new StringAst(m_nodeStack.last()); // strAst
    else if ( name == "subscriptast" ) ast = new SubscriptAst(m_nodeStack.last()); // subscriptAst
    else if ( name == "tryexceptast" ) ast = new TryExceptAst(m_nodeStack.last()); // tryExceptAst
    else if ( name == "tryfinallyast" ) ast = new TryFinallyAst(m_nodeStack.last()); // tryFinallyAst
    else if ( name == "tupleast" ) ast = new TupleAst(m_nodeStack.last()); // tupleAst
    else if ( name == "unaryopast" ) ast = new UnaryOperationAst(m_nodeStack.last()); // unaryOpAst
    else if ( name == "whileast" ) ast = new WhileAst(m_nodeStack.last()); // whileAst
    else if ( name == "withast" ) ast = new WithAst(m_nodeStack.last()); // withAst
    else if ( name == "yieldast" ) ast = new YieldAst(m_nodeStack.last()); // yieldAst
    else kError() << "Unknown AST type" << name;
    
    m_nodeMap.insert(attributeDict["nodecnt"].toInt(), ast);
    
    m_nodeStack.append(ast);
}

void AstBuilder::populateAst()
{
}
    
}

