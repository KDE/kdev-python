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
    
    // TODO this is not clean
    if ( parser->exitStatus() != QProcess::NormalExit ) {
        kError() << "Error parsing file: " << parser->errorString();
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
    
    populateAst();
    
    CodeAst* codeAst = dynamic_cast<CodeAst*>(m_currentNode);
    if ( ! codeAst ) 
        Q_ASSERT(codeAst);
    return codeAst;
}

void AstBuilder::parseXmlAstNode(QXmlStreamReader* xmlast, QXmlStreamReader::TokenType token = QXmlStreamReader::Invalid) {
    bool nodeAdded = false;
    
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
            
            // Skip the document root element
            if ( currentElementName == "pythonast" ) {
                parseXmlAstNode(xmlast, token);
                continue;
            }
            
            kDebug() << "Token: " << token << "; " << "Name: " << currentElementName << "; Text: " << currentElementText;
            for ( int i=0; i<currentElementAttributes.length(); i++ ) {
                kDebug() << currentElementAttributes.at(i).name() << currentElementAttributes.at(i).value();
            }
            
            // this will push a parent onto the stack
            nodeAdded = parseAstNode(currentElementName, currentElementText, currentElementAttributes);
            if ( ! nodeAdded ) continue;
            
            parseXmlAstNode(xmlast, token);
            
            // now we pop this parent off
            m_currentNode = m_nodeStack.last();
            m_nodeStack.removeLast();
        }
        // Everything else (stuff between tags, comments...) is ignored
        else continue;
    }
}

bool AstBuilder::parseAstNode(QString name, QString text, const QList< QXmlStreamAttribute >& attributes)
{
    Ast* ast;
    
    QMap<QString, QString> attributeDict;
    
    for ( int i=0; i<attributes.length(); i++ ) {
        kDebug() << "Added attribute: " << attributes.at(i).name().toString() << attributes.at(i).value().toString();
        attributeDict.insert(attributes.at(i).name().toString(), attributes.at(i).value().toString());
    }
    
    int node_id = attributeDict["nodecnt"].toInt();
    
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
    else {
        // assemble AST primitives
        // TODO revert the order, better performance
        if      ( name == "loadast" ) m_contextNodeMap.insert(node_id, ExpressionAst::Load);
        else if ( name == "storeast") m_contextNodeMap.insert(node_id, ExpressionAst::Store);
        else if ( name == "deleteast" ) m_contextNodeMap.insert(node_id, ExpressionAst::Delete);
        else if ( name == "augassignast" ) m_contextNodeMap.insert(node_id, ExpressionAst::AugStore);
        
        else if ( name == "addast" ) m_opNodeMap.insert(node_id, Ast::OperatorAdd);
        else if ( name == "subast" ) m_opNodeMap.insert(node_id, Ast::OperatorSub);
        else if ( name == "multast" ) m_opNodeMap.insert(node_id, Ast::OperatorMult);
        else if ( name == "divast" ) m_opNodeMap.insert(node_id, Ast::OperatorDiv);
        else if ( name == "modast" ) m_opNodeMap.insert(node_id, Ast::OperatorMod);
        else if ( name == "bitxorast" ) m_opNodeMap.insert(node_id, Ast::OperatorBitwiseXor);
        else if ( name == "bitandast" ) m_opNodeMap.insert(node_id, Ast::OperatorBitwiseAnd);
        else if ( name == "bitorast" ) m_opNodeMap.insert(node_id, Ast::OperatorBitwiseOr);
        else if ( name == "powast" ) m_opNodeMap.insert(node_id, Ast::OperatorPow);
        else if ( name == "rshiftast" ) m_opNodeMap.insert(node_id, Ast::OperatorRightShift);
        else if ( name == "lshiftast" ) m_opNodeMap.insert(node_id, Ast::OperatorLeftShift);
        
        else if ( name == "notast" ) m_unaryOpNodeMap.insert(node_id, Ast::UnaryOperatorNot);
        else if ( name == "uaddast" ) m_unaryOpNodeMap.insert(node_id, Ast::UnaryOperatorAdd);
        else if ( name == "usubast" ) m_unaryOpNodeMap.insert(node_id, Ast::UnaryOperatorSub);
        else if ( name == "invertast" ) m_unaryOpNodeMap.insert(node_id, Ast::UnaryOperatorInvert);
        
        else if ( name == "eqast" ) m_compOpNodeMap.insert(node_id, Ast::ComparisonOperatorEquals);
        else if ( name == "noteqast" ) m_compOpNodeMap.insert(node_id, Ast::ComparisonOperatorNotEquals);
        else if ( name == "ltast" ) m_compOpNodeMap.insert(node_id, Ast::ComparisonOperatorLessThan);
        else if ( name == "lteast" ) m_compOpNodeMap.insert(node_id, Ast::ComparisonOperatorLessThanEqual);
        else if ( name == "gtast" ) m_compOpNodeMap.insert(node_id, Ast::ComparisonOperatorGreaterThan);
        else if ( name == "gteast" ) m_compOpNodeMap.insert(node_id, Ast::ComparisonOperatorGreaterThanEqual);
        else if ( name == "isast" ) m_compOpNodeMap.insert(node_id, Ast::ComparisonOperatorIs);
        else if ( name == "isnotast" ) m_compOpNodeMap.insert(node_id, Ast::ComparisonOperatorIsNot);
        else if ( name == "inast" ) m_compOpNodeMap.insert(node_id, Ast::ComparisonOperatorIn);
        else if ( name == "notinast" ) m_compOpNodeMap.insert(node_id, Ast::ComparisonOperatorNotIn);
        
        else if ( name == "andast" ) m_boolOpNodeMap.insert(node_id, Ast::BooleanAnd);
        else if ( name == "orast" ) m_boolOpNodeMap.insert(node_id, Ast::BooleanOr);
        else {
            kWarning() << "Unknown AST type" << name;
        }
        // we did not push a node onto the stack, so we return false
        return false;
    }
    
    m_nodeMap.insert(node_id, ast);
    m_attributeStore.insert(node_id, attributeDict);
    
    m_nodeStack.append(ast);
    return true;
}

template <typename T> T* AstBuilder::resolveNode(const QString& identifier)
{
    return dynamic_cast<T*>(m_nodeMap[identifier.toInt()]);
}

template <typename T> QList<T*> AstBuilder::resolveNodeList(const QString& commaSeperatedIdentifiers)
{
    QList<T*> items;
    QStringList identifiers = commaSeperatedIdentifiers.split(",");
    for ( int i=0; i<identifiers.length(); i++ ) {
        items << resolveNode<T>(identifiers.at(i));
    }
    return items;
}

FunctionDefinitionAst* AstBuilder::populateFunctionDefinitionAst(Ast* ast, const stringDictionary& currentAttributes)
{
    FunctionDefinitionAst* currentNode = dynamic_cast<FunctionDefinitionAst*>(ast);
    currentNode->arguments = resolveNode<ArgumentsAst>(currentAttributes.value("NR_args"));
    currentNode->body = resolveNodeList<StatementAst>(currentAttributes.value("NRLST_body"));
    currentNode->decorators = resolveNodeList<NameAst>(currentAttributes.value("NRLST_decorator_list"));
    currentNode->name = new Identifier(currentAttributes.value("name"));
    kDebug() << "Found function definition, name: " << currentAttributes.value("name");
    return currentNode;
}

void AstBuilder::populateAst()
{
    Ast* currentAbstractNode;
    Ast* currentNode;
    stringDictionary currentAttributes;
    QMapIterator<int, Ast*> i(m_nodeMap);
    while ( i.hasNext() ) {
        i.next();
        currentAbstractNode = i.value();
        currentAttributes = m_attributeStore.value(i.key());
        
        kDebug() << "Processing AST node ID " << i.key();
        kDebug() << "Amount of attributes: " << currentAttributes.size();
        
        stringDictionary::const_iterator i = currentAttributes.begin();
        while ( i != currentAttributes.end() ) {
            kDebug() << i.key() << i.value();
            ++i;
        }
        
        switch ( currentAbstractNode->astType ) {
            case Ast::CodeAstType:                                  break;
            case Ast::FunctionDefinitionAstType:                    populateFunctionDefinitionAst(currentAbstractNode, currentAttributes); break;
            case Ast::ClassDefinitionAstType:                       break;
            case Ast::ReturnAstType:                                break;
            case Ast::DeleteAstType:                                break;
            case Ast::AssignmentAstType:                            break;
            case Ast::AugmentedAssignmentAstType:                   break;
            case Ast::ForAstType:                                   break;
            case Ast::WhileAstType:                                 break;
            case Ast::IfAstType:                                    break;
            case Ast::WithAstType:                                  break;
            case Ast::RaiseAstType:                                 break;
            case Ast::TryExceptAstType:                             break;
            case Ast::TryFinallyAstType:                            break;
            case Ast::AssertionAstType:                             break;
            case Ast::ImportAstType:                                break;
            case Ast::ImportFromAstType:                            break;
            case Ast::ExecAstType:                                  break;
            case Ast::GlobalAstType:                                break;
            case Ast::BreakAstType:                                 break;
            case Ast::ContinueAstType:                              break;
            case Ast::PrintAstType:                                 break;
            case Ast::PassAstType:                                  break;
            case Ast::BooleanOperationAstType:                      break;
            case Ast::BinaryOperationAstType:                       break;
            case Ast::UnaryOperationAstType:                        break;
            case Ast::LambdaAstType:                                break;
            case Ast::IfExpressionAstType:                          break;
            case Ast::DictAstType:                                  break;
            case Ast::SetAstType:                                   break;
            case Ast::ListComprehensionAstType:                     break;
            case Ast::SetComprehensionAstType:                      break;
            case Ast::DictionaryComprehensionAstType:               break;
            case Ast::GeneratorExpressionAstType:                   break;
            case Ast::CompareAstType:                               break;
            case Ast::ReprAstType:                                  break;
            case Ast::NumberAstType:                                break;
            case Ast::StringAstType:                                break;
            case Ast::YieldAstType:                                 break;
            case Ast::NameAstType:                                  break;
            case Ast::CallAstType:                                  break;
            case Ast::AttributeAstType:                             break;
            case Ast::SubscriptAstType:                             break;
            case Ast::ListAstType:                                  break;
            case Ast::TupleAstType:                                 break;
            case Ast::EllipsisAstType:                              break;
            case Ast::SliceAstType:                                 break;
            case Ast::ExtendedSliceAstType:                         break;
            case Ast::IndexAstType:                                 break;
            case Ast::ArgumentsAstType:                             break;
            case Ast::KeywordAstType:                               break;
            case Ast::ComprehensionAstType:                         break;
            case Ast::ExceptionHandlerAstType:                      break;
            case Ast::AliasAstType:                                 break;
            case Ast::ExpressionAstType:                            break;
            case Ast::StatementAstType:                             break;
        }
    }
}
    
}

