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
#include <qdir.h>
#include <language/duchain/topducontext.h>
#include <language/interfaces/iproblem.h>

namespace Python
{
    
CodeAst* AstBuilder::parse(KUrl filename)
{
    CodeAst* ast = parseXmlAst(getXmlForFile(filename));
    return ast;
}
    
QString AstBuilder::getXmlForFile(KUrl filename)
{
    QProcess* parser = new QProcess();
    // we call a python script to parse the code for us. It returns an XML string with the AST
    kDebug() << QDir::current();
    parser->start("/usr/bin/env", QStringList() << "python" << "pythonpythonparser.py" << filename.path());
    parser->waitForFinished();
    
    // TODO this is not clean
    if ( parser->exitStatus() != QProcess::NormalExit ) {
        kError() << "Error parsing file: " << parser->errorString();
        return "";
    }
    
    QString result = parser->readAllStandardOutput();
    kDebug() << "XML for " << filename << ":" << result;
    
    if ( ! result.length() ) {
        result = parser->readAllStandardError();
        result.split(":");
        int lineno = result[0].toAscii();
        int colno = result[1].toAscii();
        KDevelop::ProblemPointer p(new KDevelop::Problem());
        p->setFinalLocation(KDevelop::DocumentRange(KDevelop::IndexedString(filename), KDevelop::SimpleRange(lineno, colno, lineno, colno + 1)));
        p->setSource(KDevelop::ProblemData::Disk);
        p->setDescription(result);
        kWarning() << "Parse Error: " << result;
        return "0";
    }
    delete parser;
    return result;
}

CodeAst* AstBuilder::parseXmlAst(QString xml)
{
    Q_ASSERT(xml.length());
    
    if ( xml == "0" ) {
        return 0;
    }
    
    QXmlStreamReader* xmlast = new QXmlStreamReader();
    xmlast->addData(xml);
    
    m_nodeMap.clear();
    
    parseXmlAstNode(xmlast, QXmlStreamReader::Invalid);
    
    populateAst();
    
    CodeAst* codeAst = dynamic_cast<CodeAst*>(m_currentNode);
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
    
    // TODO implent this using QMap/QBinaryFind/enum/parser table
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
    kDebug() << "Stack size: " << m_nodeStack.length();
    return true;
}

template <typename T> T* AstBuilder::resolveNode(const QString& identifier)
{
    int id = identifier.toInt();
    if ( ! id ) return 0;
    return dynamic_cast<T*>(m_nodeMap.value(id));
}

template <typename T> QList<T*> AstBuilder::resolveNodeList(const QString& commaSeperatedIdentifiers)
{
    QList<T*> items;
    QStringList identifiers = commaSeperatedIdentifiers.split(",");
    for ( int i=0; i<identifiers.length(); i++ ) {
        if ( identifiers.at(i).length() ) items << resolveNode<T>(identifiers.at(i));
    }
    return items;
}

Identifier* AstBuilder::createIdentifier(const QString& name, Ast* range)
{
    Identifier* ident = new Identifier(name);
    ident->startCol = range->startCol;
    ident->endCol = range->startCol + name.length() - 1;
    ident->startLine = range->startLine;
    ident->endLine = range->endLine;
    return ident;
}

ExpressionAst::Context AstBuilder::resolveContext(const QString& identifier)
{
    int id = identifier.toInt();
    if ( ! id ) return ExpressionAst::Invalid;
    return m_contextNodeMap.value(id);
}

Ast::BooleanOperationTypes AstBuilder::resolveBooleanOperator(const QString& identifier)
{
    int id = identifier.toInt();
    if ( ! id ) return Ast::BooleanInvalidOperation;
    return m_boolOpNodeMap.value(id);
}

Ast::OperatorTypes AstBuilder::resolveOperator(const QString& identifier)
{
    int id = identifier.toInt();
    if ( ! id ) return Ast::OperatorInvalid;
    return m_opNodeMap.value(id);
}

Ast::UnaryOperatorTypes AstBuilder::resolveUnaryOperator(const QString& identifier)
{
    int id = identifier.toInt();
    if ( ! id ) return Ast::UnaryOperatorInvalid;
    return m_unaryOpNodeMap.value(id);
}

Ast::ComparisonOperatorTypes AstBuilder::resolveComparisonOperator(const QString& identifier)
{
    int id = identifier.toInt();
    if ( ! id ) return Ast::ComparisonOperatorInvalid;
    return m_compOpNodeMap.value(id);
}

QList< Ast::ComparisonOperatorTypes > AstBuilder::resolveComparisonOperatorList(const QString& identifiers)
{
    QList<Ast::ComparisonOperatorTypes> items;
    QList<QString> ids = identifiers.split(",");
    for ( int i=0; i < ids.length(); i++ ) {
        items << resolveComparisonOperator(ids.at(i));
    }
    return items;
}

NameAst* AstBuilder::populateNameAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    NameAst* currentNode = dynamic_cast<NameAst*>(ast);
    currentNode->context = resolveContext(currentAttributes.value("NR_ctx"));
    currentNode->identifier = createIdentifier(currentAttributes.value("id"), currentNode);
    kDebug() << "Processing NameAst" << currentNode->identifier->value;
    return currentNode;
}

ClassDefinitionAst* AstBuilder::populateClassDefinitonAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    ClassDefinitionAst* currentNode = dynamic_cast<ClassDefinitionAst*>(ast);
    currentNode->baseClasses = resolveNodeList<ExpressionAst>(currentAttributes.value("NRLST_bases"));
    currentNode->body = resolveNodeList<StatementAst>(currentAttributes.value("NRLST_body"));
    currentNode->decorators = resolveNodeList<ExpressionAst>(currentAttributes.value("NRLST_decorator_list"));
    currentNode->name = createIdentifier(currentAttributes.value("name"), currentNode);
    currentNode->name->startCol += 6; // TODO fix this! ;D
    currentNode->name->endCol += 6;
    return currentNode;
}

FunctionDefinitionAst* AstBuilder::populateFunctionDefinitionAst(Ast* ast, const stringDictionary& currentAttributes)
{
    FunctionDefinitionAst* currentNode = dynamic_cast<FunctionDefinitionAst*>(ast);
    currentNode->arguments = resolveNode<ArgumentsAst>(currentAttributes.value("NR_args"));
    currentNode->body = resolveNodeList<StatementAst>(currentAttributes.value("NRLST_body"));
    currentNode->decorators = resolveNodeList<NameAst>(currentAttributes.value("NRLST_decorator_list"));
    currentNode->name = createIdentifier(currentAttributes.value("name"), currentNode);
    currentNode->name->startCol += 4; // TODO fix this! ;D
    currentNode->name->endCol += 4;
    return currentNode;
}

AssignmentAst* AstBuilder::populateAssignmentAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    AssignmentAst* currentNode = dynamic_cast<AssignmentAst*>(ast);
    currentNode->value = resolveNode<ExpressionAst>(currentAttributes.value("NR_value"));
    currentNode->targets = resolveNodeList<ExpressionAst>(currentAttributes.value("NRLST_targets"));
    return currentNode;
}

CodeAst* AstBuilder::populateCodeAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    CodeAst* currentNode = dynamic_cast<CodeAst*>(ast);
    currentNode->body = resolveNodeList<StatementAst>(currentAttributes.value("NRLST_body"));
    return currentNode;
}

DeleteAst* AstBuilder::populateDeleteAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    DeleteAst* currentNode = dynamic_cast<DeleteAst*>(ast);
    currentNode->targets = resolveNodeList<ExpressionAst>(currentAttributes.value("NRLST_targets"));
    return currentNode;
}

ForAst* AstBuilder::populateForAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    ForAst* currentNode = dynamic_cast<ForAst*>(ast);
    currentNode->body = resolveNodeList<StatementAst>(currentAttributes.value("NRLST_body"));
    currentNode->orelse = resolveNodeList<StatementAst>(currentAttributes.value("NRLST_orelse"));
    currentNode->iterator = resolveNode<ExpressionAst>(currentAttributes.value("NR_iter"));
    currentNode->target = resolveNode<ExpressionAst>(currentAttributes.value("NR_target"));
    return currentNode;
}

PrintAst* AstBuilder::populatePrintAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    PrintAst* currentNode = dynamic_cast<PrintAst*>(ast);
    currentNode->destination = resolveNode<ExpressionAst>(currentAttributes.value("NR_dest"));
    currentNode->newline = currentAttributes.value("nl") == "True" ? true : false;
    currentNode->values = resolveNodeList<ExpressionAst>(currentAttributes.value("NRLST_values"));
    return currentNode;
}

ReturnAst* AstBuilder::populateReturnAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    ReturnAst* currentNode = dynamic_cast<ReturnAst*>(ast);
    currentNode->value = resolveNode<ExpressionAst>(currentAttributes.value("NR_value"));
    return currentNode;
}

IfAst* AstBuilder::populateIfAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    IfAst* currentNode = dynamic_cast<IfAst*>(ast);
    currentNode->body = resolveNodeList<StatementAst>(currentAttributes.value("NRLST_body"));
    currentNode->condition = resolveNode<ExpressionAst>(currentAttributes.value("NR_test"));
    currentNode->orelse = resolveNodeList<StatementAst>(currentAttributes.value("NRLST_orelse"));
    return currentNode;
}

BooleanOperationAst* AstBuilder::populateBooleanOperationAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    BooleanOperationAst* currentNode = dynamic_cast<BooleanOperationAst*>(ast);
    currentNode->values = resolveNodeList<ExpressionAst>(currentAttributes.value("NRLST_values"));
    currentNode->type = resolveBooleanOperator(currentAttributes.value("NR_op"));
    return currentNode;
}

CallAst* AstBuilder::populateCallAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    CallAst* currentNode = dynamic_cast<CallAst*>(ast);
    currentNode->arguments = resolveNodeList<ExpressionAst>(currentAttributes.value("NRLST_args"));
    currentNode->function = resolveNode<ExpressionAst>(currentAttributes.value("NR_func"));
    currentNode->keywordArguments = resolveNode<ExpressionAst>(currentAttributes.value("NR_kwargs"));
    currentNode->keywords = resolveNodeList<KeywordAst>(currentAttributes.value("NRLST_keywords"));
    currentNode->starArguments = resolveNode<ExpressionAst>(currentAttributes.value("NR_starargs"));
    return currentNode;
}

LambdaAst* AstBuilder::populateLambdaAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    LambdaAst* currentNode = dynamic_cast<LambdaAst*>(ast);
    currentNode->arguments = resolveNode<ArgumentsAst>(currentAttributes.value("NR_args"));
    currentNode->body = resolveNode<ExpressionAst>(currentAttributes.value("NR_body"));
    return currentNode;
}

WhileAst* AstBuilder::populateWhileAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    WhileAst* currentNode = dynamic_cast<WhileAst*>(ast);
    currentNode->body = resolveNodeList<StatementAst>(currentAttributes.value("NRLST_body"));
    currentNode->orelse = resolveNodeList<StatementAst>(currentAttributes.value("NRLST_orelse"));
    currentNode->condition = resolveNode<ExpressionAst>(currentAttributes.value("NR_test"));
    return currentNode;
}

DictAst* AstBuilder::populateDictAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    DictAst* currentNode = dynamic_cast<DictAst*>(ast);
    currentNode->keys = resolveNodeList<ExpressionAst>(currentAttributes.value("NRLST_keys"));
    currentNode->values = resolveNodeList<ExpressionAst>(currentAttributes.value("NRLST_values"));
    return currentNode;
}

ListAst* AstBuilder::populateListAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    ListAst* currentNode = dynamic_cast<ListAst*>(ast);
    currentNode->elements = resolveNodeList<ExpressionAst>(currentAttributes.value("NRLST_elts"));
    currentNode->context = resolveContext(currentAttributes.value("NR_ctx"));
    return currentNode;
}

TupleAst* AstBuilder::populateTupleAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    TupleAst* currentNode = dynamic_cast<TupleAst*>(ast);
    currentNode->context = resolveContext(currentAttributes.value("NR_ctx"));
    currentNode->elements = resolveNodeList<ExpressionAst>(currentAttributes.value("NRLST_elts"));
    return currentNode;
}

AugmentedAssignmentAst* AstBuilder::populateAugmentedAssignmentAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    AugmentedAssignmentAst* currentNode = dynamic_cast<AugmentedAssignmentAst*>(ast);
    currentNode->op = resolveOperator(currentAttributes.value("NR_op"));
    currentNode->target = resolveNode<ExpressionAst>(currentAttributes.value("NR_target"));
    currentNode->value = resolveNode<ExpressionAst>(currentAttributes.value("NR_value"));
    return currentNode;
}

RaiseAst* AstBuilder::populateRaiseAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    RaiseAst* currentNode = dynamic_cast<RaiseAst*>(ast);
    currentNode->type = resolveNode<ExpressionAst>(currentAttributes.value("NR_type"));
    return currentNode;
}

TryExceptAst* AstBuilder::populateTryExceptAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    TryExceptAst* currentNode = dynamic_cast<TryExceptAst*>(ast);
    currentNode->body = resolveNodeList<StatementAst>(currentAttributes.value("NRLST_body"));
    currentNode->handlers = resolveNodeList<ExceptionHandlerAst>(currentAttributes.value("NRLST_handlers"));
    currentNode->orelse = resolveNodeList<StatementAst>(currentAttributes.value("NRLST_orelse"));
    return currentNode;
}

TryFinallyAst* AstBuilder::populateTryFinallyAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    TryFinallyAst* currentNode = dynamic_cast<TryFinallyAst*>(ast);
    currentNode->body = resolveNodeList<StatementAst>(currentAttributes.value("NRLST_body"));
    currentNode->finalbody = resolveNodeList<StatementAst>(currentAttributes.value("NRLST_finalbody"));
    return currentNode;
}

AssertionAst* AstBuilder::populateAssertionAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    AssertionAst* currentNode = dynamic_cast<AssertionAst*>(ast);
    currentNode->condition = resolveNode<ExpressionAst>(currentAttributes.value("NR_test"));
    currentNode->message = resolveNode<ExpressionAst>(currentAttributes.value("NR_msg"));
    return currentNode;
}

BinaryOperationAst* AstBuilder::populateBinaryOperationAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    BinaryOperationAst* currentNode = dynamic_cast<BinaryOperationAst*>(ast);
    currentNode->rhs = resolveNode<ExpressionAst>(currentAttributes.value("NR_right"));
    currentNode->lhs = resolveNode<ExpressionAst>(currentAttributes.value("NR_left"));
    currentNode->type = resolveOperator(currentAttributes.value("NR_op"));
    return currentNode;
}

ImportAst* AstBuilder::populateImportAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    ImportAst* currentNode = dynamic_cast<ImportAst*>(ast);
    currentNode->names = resolveNodeList<AliasAst>(currentAttributes.value("NRLST_names"));
    return currentNode;
}

ImportFromAst* AstBuilder::populateImportFromAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    ImportFromAst* currentNode = dynamic_cast<ImportFromAst*>(ast);
    currentNode->level = currentAttributes.value("level").toInt();
    currentNode->module = createIdentifier(currentAttributes.value("module"), currentNode);
    currentNode->names = resolveNodeList<AliasAst>(currentAttributes.value("NRLST_names"));
    return currentNode;
}

AliasAst* AstBuilder::populateAliasAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    AliasAst* currentNode = dynamic_cast<AliasAst*>(ast);
    currentNode->asName = resolveNode<NameAst>(currentAttributes.value("NR_asname"));
    currentNode->name = createIdentifier(currentAttributes.value("name"), currentNode);
    return currentNode;
}

GlobalAst* AstBuilder::populateGlobalAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    GlobalAst* currentNode = dynamic_cast<GlobalAst*>(ast);
//     currentNode->names = resolveNodeList<Identifier>(currentAttributes.value("NRLST_names")); // TODO the parser does not write this correctly! also, need to fix resolve<Identifier>
    return currentNode;
}

UnaryOperationAst* AstBuilder::populateUnaryOperationAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    UnaryOperationAst* currentNode = dynamic_cast<UnaryOperationAst*>(ast);
    currentNode->operand = resolveNode<ExpressionAst>(currentAttributes.value("NR_operand"));
    currentNode->type = resolveUnaryOperator(currentAttributes.value("NR_op"));
    return currentNode;
}

IfExpressionAst* AstBuilder::populateIfExpressionAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    IfExpressionAst* currentNode = dynamic_cast<IfExpressionAst*>(ast);
    currentNode->body = resolveNode<ExpressionAst>(currentAttributes.value("NR_body"));
    currentNode->orelse = resolveNode<ExpressionAst>(currentAttributes.value("NR_orelse"));
    currentNode->condition = resolveNode<ExpressionAst>(currentAttributes.value("NR_test"));
    return currentNode;
}

ListComprehensionAst* AstBuilder::populateListComprehensionAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    ListComprehensionAst* currentNode = dynamic_cast<ListComprehensionAst*>(ast);
    currentNode->generators = resolveNodeList<ComprehensionAst>(currentAttributes.value("NRLST_generators"));
    currentNode->element = resolveNode<ExpressionAst>(currentAttributes.value("NR_elt"));
    return currentNode;
}

WithAst* AstBuilder::populateWithAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    WithAst* currentNode = dynamic_cast<WithAst*>(ast);
    currentNode->body = resolveNodeList<StatementAst>(currentAttributes.value("NRLST_body"));
    currentNode->contextExpression = resolveNode<ExpressionAst>(currentAttributes.value("NR_context_expr"));
    currentNode->optionalVars = resolveNode<ExpressionAst>(currentAttributes.value("NR_optional_vars"));
    return currentNode;
}

ComprehensionAst* AstBuilder::populateComprehensionAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    ComprehensionAst* currentNode = dynamic_cast<ComprehensionAst*>(ast);
    currentNode->conditions = resolveNodeList<ExpressionAst>(currentAttributes.value("NRLST_ifs"));
    currentNode->iterator = resolveNode<ExpressionAst>(currentAttributes.value("NR_iter"));
    currentNode->target = resolveNode<ExpressionAst>(currentAttributes.value("NR_target"));
    return currentNode;
}

CompareAst* AstBuilder::populateCompareAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    CompareAst* currentNode = dynamic_cast<CompareAst*>(ast);
    currentNode->comparands = resolveNodeList<ExpressionAst>(currentAttributes.value("NRLST_comparators"));
    currentNode->operators = resolveComparisonOperatorList(currentAttributes.value("NRLST_ops"));
    currentNode->leftmostElement = resolveNode<ExpressionAst>(currentAttributes.value("NR_left"));
    return currentNode;
}

NumberAst* AstBuilder::populateNumberAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    NumberAst* currentNode = dynamic_cast<NumberAst*>(ast);
    currentNode->value = currentAttributes.value("n"); // save this as a QString to aviod problems with python number formats like 3j+2 (complex), 3L, 3.35, etc.
    return currentNode;
}

StringAst* AstBuilder::populateStringAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    StringAst* currentNode = dynamic_cast<StringAst*>(ast);
    currentNode->value = currentAttributes.value("s");
    return currentNode;
}

AttributeAst* AstBuilder::populateAttributeAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    AttributeAst* currentNode = dynamic_cast<AttributeAst*>(ast);
    currentNode->value = resolveNode<ExpressionAst>(currentAttributes.value("NR_value"));
    currentNode->attribute = createIdentifier(currentAttributes.value("attr"), currentNode);
    currentNode->context = resolveContext(currentAttributes.value("NR_ctx"));
    return currentNode;
}

SubscriptAst* AstBuilder::populateSubscriptAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    SubscriptAst* currentNode = dynamic_cast<SubscriptAst*>(ast);
    currentNode->context = resolveContext("NR_ctx");
    currentNode->slice = resolveNode<SliceAst>(currentAttributes.value("NR_slice"));
    currentNode->value = resolveNode<ExpressionAst>(currentAttributes.value("NR_value"));
    return currentNode;
}

SliceAst* AstBuilder::populateSliceAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    SliceAst* currentNode = dynamic_cast<SliceAst*>(ast);
    currentNode->lower = resolveNode<ExpressionAst>(currentAttributes.value("NR_lower"));
    currentNode->upper = resolveNode<ExpressionAst>(currentAttributes.value("NR_upper"));
    currentNode->step = resolveNode<ExpressionAst>(currentAttributes.value("NR_step"));
    return currentNode;
}

ArgumentsAst* AstBuilder::populateArgumentsAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    ArgumentsAst* currentNode = dynamic_cast<ArgumentsAst*>(ast);
    currentNode->arguments = resolveNodeList<ExpressionAst>(currentAttributes.value("NRLST_args"));
    currentNode->defaultValues = resolveNodeList<ExpressionAst>(currentAttributes.value("NRLST_defaults"));
    currentNode->kwarg = createIdentifier(currentAttributes.value("kwarg"), currentNode);
    currentNode->vararg = createIdentifier(currentAttributes.value("paramstar"), currentNode);
    return currentNode;
}

ExceptionHandlerAst* AstBuilder::populateExceptionHandlerAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    ExceptionHandlerAst* currentNode = dynamic_cast<ExceptionHandlerAst*>(ast);
    currentNode->body = resolveNodeList<StatementAst>(currentAttributes.value("NRLST_body"));
    currentNode->name = resolveNode<ExpressionAst>(currentAttributes.value("NR_name"));
    currentNode->type = resolveNode<ExpressionAst>(currentAttributes.value("NR_type"));
    return currentNode;
}

IndexAst* AstBuilder::populateIndexAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    IndexAst* currentNode = dynamic_cast<IndexAst*>(ast);
    currentNode->value = resolveNode<ExpressionAst>(currentAttributes.value("NR_value"));
    return currentNode;
}

KeywordAst* AstBuilder::populateKeywordAst(Ast* ast, const Python::stringDictionary& currentAttributes)
{
    KeywordAst* currentNode = dynamic_cast<KeywordAst*>(ast);
    currentNode->argumentName = createIdentifier(currentAttributes.value("arg"), currentNode);
    currentNode->value = resolveNode<ExpressionAst>(currentAttributes.value("NR_value"));
    return currentNode;
}

void AstBuilder::populateAst()
{
    Ast* currentAbstractNode;
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
        
        int startLine = currentAttributes.value("lineno").toInt() - 1; // start = 0 <> start = 1
        currentAbstractNode->startLine = startLine;
        currentAbstractNode->endLine = startLine;
        int startCol = currentAttributes.value("col_offset").toInt();
        currentAbstractNode->startCol = startCol;
        currentAbstractNode->endCol = startCol + 100; // TODO fix this ;p
        
        if ( ! currentAbstractNode->startLine && currentAbstractNode->parent ) {
            currentAbstractNode->startLine = currentAbstractNode->parent->startLine;
            currentAbstractNode->endLine = currentAbstractNode->parent->endLine;
            currentAbstractNode->startCol = currentAbstractNode->parent->startCol;
            currentAbstractNode->endCol = currentAbstractNode->parent->endCol;
        }
        
        switch ( currentAbstractNode->astType ) {
            case Ast::CodeAstType:                                  currentAbstractNode = populateCodeAst(currentAbstractNode, currentAttributes); break;
            case Ast::FunctionDefinitionAstType:                    currentAbstractNode = populateFunctionDefinitionAst(currentAbstractNode, currentAttributes); break;
            case Ast::ClassDefinitionAstType:                       currentAbstractNode = populateClassDefinitonAst(currentAbstractNode, currentAttributes); break;
            case Ast::ReturnAstType:                                currentAbstractNode = populateReturnAst(currentAbstractNode, currentAttributes); break;
            case Ast::DeleteAstType:                                currentAbstractNode = populateDeleteAst(currentAbstractNode, currentAttributes); break;
            case Ast::AssignmentAstType:                            currentAbstractNode = populateAssignmentAst(currentAbstractNode, currentAttributes); break;
            case Ast::AugmentedAssignmentAstType:                   currentAbstractNode = populateAugmentedAssignmentAst(currentAbstractNode, currentAttributes); break;
            case Ast::ForAstType:                                   currentAbstractNode = populateForAst(currentAbstractNode, currentAttributes); break;
            case Ast::WhileAstType:                                 currentAbstractNode = populateWhileAst(currentAbstractNode, currentAttributes); break;
            case Ast::IfAstType:                                    currentAbstractNode = populateIfAst(currentAbstractNode, currentAttributes); break;
            case Ast::WithAstType:                                  currentAbstractNode = populateWithAst(currentAbstractNode, currentAttributes); break;
            case Ast::RaiseAstType:                                 currentAbstractNode = populateRaiseAst(currentAbstractNode, currentAttributes); break;
            case Ast::TryExceptAstType:                             currentAbstractNode = populateTryExceptAst(currentAbstractNode, currentAttributes); break;
            case Ast::TryFinallyAstType:                            currentAbstractNode = populateTryFinallyAst(currentAbstractNode, currentAttributes); break;
            case Ast::AssertionAstType:                             currentAbstractNode = populateAssertionAst(currentAbstractNode, currentAttributes); break;
            case Ast::ImportAstType:                                currentAbstractNode = populateImportAst(currentAbstractNode, currentAttributes); break;
            case Ast::ImportFromAstType:                            currentAbstractNode = populateImportFromAst(currentAbstractNode, currentAttributes); break;
//             case Ast::ExecAstType:                                  break; // TODO support this? or better not? :]
            case Ast::GlobalAstType:                                currentAbstractNode = populateGlobalAst(currentAbstractNode, currentAttributes); break;
            case Ast::BreakAstType:                                 break; // ok
            case Ast::ContinueAstType:                              break; // ok
            case Ast::PrintAstType:                                 currentAbstractNode = populatePrintAst(currentAbstractNode, currentAttributes); break;
            case Ast::PassAstType:                                  break; // ok
            case Ast::BooleanOperationAstType:                      currentAbstractNode = populateBooleanOperationAst(currentAbstractNode, currentAttributes); break;
            case Ast::BinaryOperationAstType:                       currentAbstractNode = populateBinaryOperationAst(currentAbstractNode, currentAttributes); break;
            case Ast::UnaryOperationAstType:                        currentAbstractNode = populateUnaryOperationAst(currentAbstractNode, currentAttributes); break;
            case Ast::LambdaAstType:                                currentAbstractNode = populateLambdaAst(currentAbstractNode, currentAttributes); break;
            case Ast::IfExpressionAstType:                          currentAbstractNode = populateIfExpressionAst(currentAbstractNode, currentAttributes); break;
            case Ast::DictAstType:                                  currentAbstractNode = populateDictAst(currentAbstractNode, currentAttributes); break;
//             case Ast::SetAstType:                                   break; // TODO support this (read about sets)
            case Ast::ListComprehensionAstType:                     currentAbstractNode = populateListComprehensionAst(currentAbstractNode, currentAttributes); break;
//             case Ast::SetComprehensionAstType:                      break; // TODO support this
//             case Ast::DictionaryComprehensionAstType:               break; // TODO fix this for python 2.7+
//             case Ast::GeneratorExpressionAstType:                   break; // TODO read about this
            case Ast::CompareAstType:                               currentAbstractNode = populateCompareAst(currentAbstractNode, currentAttributes); break;
//             case Ast::ReprAstType:                                  break; // TODO support this
            case Ast::NumberAstType:                                currentAbstractNode = populateNumberAst(currentAbstractNode, currentAttributes); break;
            case Ast::StringAstType:                                currentAbstractNode = populateStringAst(currentAbstractNode, currentAttributes); break;
//             case Ast::YieldAstType:                                 break; // TODO TODO
            case Ast::NameAstType:                                  currentAbstractNode = populateNameAst(currentAbstractNode, currentAttributes); break;
            case Ast::CallAstType:                                  currentAbstractNode = populateCallAst(currentAbstractNode, currentAttributes); break;
            case Ast::AttributeAstType:                             currentAbstractNode = populateAttributeAst(currentAbstractNode, currentAttributes); break;
            case Ast::SubscriptAstType:                             currentAbstractNode = populateSubscriptAst(currentAbstractNode, currentAttributes); break;
            case Ast::ListAstType:                                  currentAbstractNode = populateListAst(currentAbstractNode, currentAttributes); break;
            case Ast::TupleAstType:                                 currentAbstractNode = populateTupleAst(currentAbstractNode, currentAttributes); break;
//             case Ast::EllipsisAstType:                              break; // TODO TODO
            case Ast::SliceAstType:                                 currentAbstractNode = populateSliceAst(currentAbstractNode, currentAttributes); break;
//             case Ast::ExtendedSliceAstType:                         break; // TODO TODO
            case Ast::IndexAstType:                                 currentAbstractNode = populateIndexAst(currentAbstractNode, currentAttributes); break;
            case Ast::ArgumentsAstType:                             currentAbstractNode = populateArgumentsAst(currentAbstractNode, currentAttributes); break;
            case Ast::KeywordAstType:                               currentAbstractNode = populateKeywordAst(currentAbstractNode, currentAttributes); break;
            case Ast::ComprehensionAstType:                         currentAbstractNode = populateComprehensionAst(currentAbstractNode, currentAttributes); break;
            case Ast::ExceptionHandlerAstType:                      currentAbstractNode = populateExceptionHandlerAst(currentAbstractNode, currentAttributes); break;
            case Ast::AliasAstType:                                 currentAbstractNode = populateAliasAst(currentAbstractNode, currentAttributes); break;
            case Ast::ExpressionAstType:                            break; // ok
            case Ast::StatementAstType:                             break; // ok
        }
    }
}
    
}

