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
    
    QMap<QString, QString> attributeDict;
    
    for ( int i=0; i<attributes.length(); i++ ) {
        attributeDict.insert(attributes.at(i).name().toString(), attributes.at(i).value().toString());
    }
    
    // TODO think about a less explicit way to do this
    // things in the comments are definitely found like this in the XML file
    name = name.toLower();
    if      ( name == "aliasast" ) ast = new AliasAst(); // aliasAst
    else if ( name == "argumentsast" ) ast = new ArgumentsAst(); // argumentsAst
    else if ( name == "assertast" ) ast = new AssertionAst(); // assertAst
    else if ( name == "assignast" ) ast = new AssignmentAst(); // assignAst
    else if ( name == "attributeast" ) ast = new AttributeAst(); // attributeAst
    else if ( name == "augassignast" ) ast = new AugmentedAssignmentAst(); // augassignast
    else if ( name == "binopast" ) ast = new BinaryOperationAst(); // binOpAst
    else if ( name == "boolopast" ) ast = new BooleanOperationAst(); // boolOpAst
    else if ( name == "breakast" ) ast = new BreakAst(); // breakAst
    else if ( name == "callast" ) ast = new CallAst(); // callAst
    else if ( name == "classdefast" ) ast = new ClassDefinitionAst(); // classDefAst
    else if ( name == "moduleast" ) ast = new CodeAst(); // moduleAst
    else if ( name == "compareast" ) ast = new CompareAst(); // compareAst
    else if ( name == "comprehensionast" ) ast = new ComprehensionAst(); // comprehensionAst
    else if ( name == "continueast" ) ast = new ContinueAst(); // continueAst
    else if ( name == "deleteast" ) ast = new DeleteAst(); // deleteAst
    else if ( name == "dictast" ) ast = new DictAst(); // dictAst
//     else if ( name == "dictionarycomprehensionast" ) ast = new DictionaryComprehensionAst(); // TODO support this for python 2.7+
    else if ( name == "ellipsisast" ) ast = new EllipsisAst(); // ellipsisAst
    else if ( name == "excepthandlerast" ) ast = new ExceptionHandlerAst(); // exceptHandlerAst
    else if ( name == "execast" ) ast = new ExecAst(); // execAst
    else if ( name == "exprast" ) ast = new ExpressionAst(); // exprast
    else if ( name == "extsliceast" ) ast = new ExtendedSliceAst(); // extsliceast
    else if ( name == "forast" ) ast = new ForAst(); // forAst
    else if ( name == "functiondefast" ) ast = new FunctionDefinitionAst(); // functionDefAst
//     else if ( name == "generatorexpressionast" ) ast = new GeneratorExpressionAst(); // TODO check this
    else if ( name == "globalast" ) ast = new GlobalAst(); // globalAst
    else if ( name == "ifast" ) ast = new IfAst(); // ifAst
    else if ( name == "ifexpast" ) ast = new IfExpressionAst(); // ifExpAst
    else if ( name == "importast" ) ast = new ImportAst(); // importAst
    else if ( name == "importfromast" ) ast = new ImportFromAst(); // importFromAst
    else if ( name == "indexast" ) ast = new IndexAst(); // indexAst
    else if ( name == "keywordast" ) ast = new KeywordAst(); // keywordAst
    else if ( name == "lambdaast" ) ast = new LambdaAst(); // lambdaAst
    else if ( name == "listast" ) ast = new ListAst(); // listAst
    else if ( name == "listcompast" ) ast = new ListComprehensionAst(); // listCompAst
    else if ( name == "nameast" ) ast = new NameAst(); // nameAst
    else if ( name == "numast" ) ast = new NumberAst(); // numAst
    else if ( name == "passast" ) ast = new PassAst();  // passAst
    else if ( name == "printast" ) ast = new PrintAst(); // printAst
    else if ( name == "raiseast" ) ast = new RaiseAst();  // raiseAst
//     else if ( name == "reprast" ) ast = new ReprAst(); // TODO what's this?
    else if ( name == "returnast" ) ast = new ReturnAst(); // returnAst
//     else if ( name == "setast" ) ast = new SetAst(); // TODO support this for python 2.7+
//     else if ( name == "setcomprehensionast" ) ast = new SetComprehensionAst(); // TODO support this for python 2.7+
    else if ( name == "sliceast" ) ast = new SliceAst(); // sliceAst
    else if ( name == "strast" ) ast = new StringAst(); // strAst
    else if ( name == "subscriptast" ) ast = new SubscriptAst(); // subscriptAst
    else if ( name == "tryexceptast" ) ast = new TryExceptAst(); // tryExceptAst
    else if ( name == "tryfinallyast" ) ast = new TryFinallyAst(); // tryFinallyAst
    else if ( name == "tupleast" ) ast = new TupleAst(); // tupleAst
    else if ( name == "unaryopast" ) ast = new UnaryOperationAst(); // unaryOpAst
    else if ( name == "whileast" ) ast = new WhileAst(); // whileAst
    else if ( name == "withast" ) ast = new WithAst(); // withAst
    else if ( name == "yieldast" ) ast = new YieldAst(); // yieldAst
    else kError() << "Unknown AST type" << name;
    
    m_nodeMap.insert(attributeDict["nodecnt"], ast);
    
}

void AstBuilder::populateAst()
{
}
    
}

