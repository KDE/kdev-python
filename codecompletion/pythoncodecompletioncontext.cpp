/*
 * This file is part of KDevelop
 * Copyright 2010 Sven Brauch <svenbrauch@googlemail.com>
 * Licensed under the GNU GPL
 * */

#include <qprocess.h>
#include <QtCore/QRegExp>

#include <language/duchain/duchainpointer.h>
#include <language/duchain/declaration.h>
#include <language/duchain/functiondeclaration.h>
#include <language/codecompletion/codecompletionitem.h>
#include <language/codecompletion/normaldeclarationcompletionitem.h>
#include <language/codecompletion/abstractincludefilecompletionitem.h>
#include <language/codecompletion/codecompletionitem.h>
#include <language/util/includeitem.h>

#include <interfaces/icore.h>
#include <interfaces/iprojectcontroller.h>
#include <interfaces/iproject.h>
#include <project/projectmodel.h>

#include "keyworditem.h"
#include "pythoncodecompletionworker.h"
#include "astbuilder.h"
#include "expressionvisitor.h"
#include "navigation/navigationwidget.h"
#include "importfileitem.h"
#include "functiondeclarationcompletionitem.h"
#include "pythoncodecompletioncontext.h"
#include "pythoneditorintegrator.h"
#include "duchain/declarationbuilder.h"

using namespace KTextEditor;
using namespace KDevelop;

namespace Python {

QList<CompletionTreeItemPointer> PythonCodeCompletionContext::completionItems(bool& abort, bool fullCompletion)
{
    if ( abort ) 
        return QList<CompletionTreeItemPointer>();
    
    QList<CompletionTreeItemPointer> items;
    DUChainReadLocker lock(DUChain::lock());
    
    if ( m_operation == PythonCodeCompletionContext::NoCompletion ) {
            
    }
    else if ( m_operation == PythonCodeCompletionContext::ImportFileCompletion ) {
        kDebug() << "Preparing to do autocompletion for import...";
        m_maxFolderScanDepth = 1;
        foreach ( ImportFileItem* item, includeFileItems(getSearchPaths(m_workingOnDocument)) ) {
            Q_ASSERT(item);
            item->includeItem.name = QString(item->moduleName + " (from " + KUrl::relativeUrl(m_workingOnDocument, item->includeItem.basePath) + ")");
            items << CompletionTreeItemPointer( item );
        }
    }
    else if ( m_operation == PythonCodeCompletionContext::ImportSubCompletion ) {
        foreach ( ImportFileItem* item, includeFileItemsForSubmodule(m_subForModule) ) {
            Q_ASSERT(item);
            item->includeItem.name = QString(item->moduleName + " (from " + KUrl::relativeUrl(m_workingOnDocument, item->includeItem.basePath) + ")");
            items << CompletionTreeItemPointer( item );
        }
    }
    else if ( m_operation == PythonCodeCompletionContext::MemberAccessCompletion ) {
        AstBuilder* builder = new AstBuilder();
        CodeAst* tmpAst = builder->parse(KUrl(), m_guessTypeOfExpression);
        if ( tmpAst ) {
            PythonEditorIntegrator* ed = new PythonEditorIntegrator();
            ExpressionVisitor* v = new ExpressionVisitor(m_context.data(), ed);
            v->visitCode(tmpAst);
            if ( v->lastType() ) {
                kDebug() << v->lastType()->toString();
                items = getCompletionItemsForType(v->lastType());
            }
            else {
                kWarning() << "Did not receive a type from expression visitor! Not offering autocompletion.";
            }
        }
        else {
            kWarning() << "Completion requested for syntactically invalid expression, not offering anything";
        }
    }
    else {
        // it's stupid to display a 3-letter completion item on manually invoked code completion and makes everything look crowded
        if ( m_operation == PythonCodeCompletionContext::NewStatementCompletion && ! fullCompletion ) {
            QStringList keywordItems;
            keywordItems << "def" << "class" << "lambda" << "global" << "print" << "import" << "from" << "while" << "for";
            foreach ( const QString& current, keywordItems ) {
                items << CompletionTreeItemPointer(new KeywordItem(KDevelop::CodeCompletionContext::Ptr(this), current));
            }
        }
        if ( abort ) {
            return QList<CompletionTreeItemPointer>();
        }
        QList<DeclarationDepthPair> declarations = m_duContext->allDeclarations(m_position, m_duContext->topContext());
        items.append(declarationListToItemList(declarations));
    }
    
    m_searchingForModule.clear();
    m_subForModule.clear();
    
    return items;
}

QList<CompletionTreeItemPointer> PythonCodeCompletionContext::declarationListToItemList(QList<DeclarationDepthPair> declarations, int maxDepth)
{
    QList<CompletionTreeItemPointer> items;
    
    DeclarationPointer currentDeclaration;
    int count = declarations.length();
    for ( int i = 0; i < count; i++ ) {
        if ( maxDepth && maxDepth > declarations.at(i).second ) {
            kDebug() << "Skipped completion item because of its depth";
            continue;
        }
        currentDeclaration = DeclarationPointer(declarations.at(i).first);
        
        kDebug() << "Adding item: " << currentDeclaration.data()->identifier().identifier().str();
        NormalDeclarationCompletionItem* item;
        if ( currentDeclaration.data()->abstractType() && currentDeclaration.data()->abstractType().constData()->whichType() == AbstractType::TypeFunction ) {
            kDebug() << "Adding function declaration item";
            item = new FunctionDeclarationCompletionItem(currentDeclaration);
        }
        else {
            item = new NormalDeclarationCompletionItem(currentDeclaration, KDevelop::CodeCompletionContext::Ptr(this));
        }
        kDebug() << item->declaration().data()->identifier().identifier().str();
        items << CompletionTreeItemPointer(item);
    }
    return items;
}

QList<CompletionTreeItemPointer> PythonCodeCompletionContext::getCompletionItemsForType(AbstractType::Ptr type)
{
    if ( type->whichType() == AbstractType::TypeStructure ) {
        // find properties of class declaration
        TypePtr<StructureType> cls = StructureType::Ptr::dynamicCast(type);
        kDebug() << "Finding completion items for class type";
        QList<DeclarationDepthPair> declarations = cls->internalContext(m_context->topContext())->allDeclarations(CursorInRevision::invalid(), m_context->topContext(), false);
        return declarationListToItemList(declarations);
    }
    
    if ( type->whichType() == AbstractType::TypeIntegral ) {
        kDebug() << "Finding completion items for integral type";
    }
    
    QList<CompletionTreeItemPointer> items;
    return items;
}

QList< ImportFileItem* > PythonCodeCompletionContext::includeFileItemsForSubmodule(QString submodule)
{
    QList<ImportFileItem*> items;
    QList<KUrl> searchPaths = getSearchPaths(m_workingOnDocument);
    QStringList subdirs = submodule.split(".");
    QList<KUrl> foundPaths;
    
    // this is a bit tricky. We need to find every path formed like /.../foo/bar for
    // a query string ("submodule" variable) like foo.bar
    // we also need paths like /foo.py, because then bar is probably a module in that file.
    // Thus, we first generate a list of possible paths, then match them against those which actually exist
    // and then gather all the items in those paths.
    
    foreach (KUrl currentPath, searchPaths) {
        bool exists = true;
        kDebug() << "Searching: " << currentPath;
        foreach ( QString subdir, subdirs ) {
            exists = currentPath.cd(subdir);
            kDebug() << currentPath;
            if ( ! exists ) break;
        }
        if ( exists ) {
            foundPaths.append(currentPath);
            kDebug() << "Found path: exists";
        }
    }
    return includeFileItems(foundPaths);
}

QList<ImportFileItem*> PythonCodeCompletionContext::includeFileItems(QList<KUrl> searchPaths) {
    QList<ImportFileItem*> items;
    
    kDebug() << "Gathering include file autocompletions...";
    
    foreach (KUrl currentPath, searchPaths) {
        kDebug() << "Processing path: " << currentPath;
        QDir currentDir(currentPath.path());
        QFileInfoList files = currentDir.entryInfoList();
        foreach (QFileInfo file, files) {
            kDebug() << "Scanning file: " << file.absoluteFilePath();
            if ( file.fileName() == "." || file.fileName() == ".." ) continue;
            if ( file.fileName().endsWith(".py") || file.fileName().endsWith(".pyc") || file.isDir() ) {
                IncludeItem includeItem;
                includeItem.basePath = file.baseName();
                includeItem.name = file.fileName();
                includeItem.isDirectory = file.isDir();
                ImportFileItem* item = new ImportFileItem(includeItem);
                item->moduleName = file.fileName().replace(".pyc", "").replace(".pyo", "").replace(".py", "");
                items.append(item);
                kDebug() << "FOUND: " << file.absoluteFilePath();
            }
        }
    }
    
    return items;
}

PythonCodeCompletionContext::PythonCodeCompletionContext(DUContextPointer context, const QString& text, const KDevelop::CursorInRevision& position, 
                                                         int depth, const PythonCodeCompletionWorker* parent): CodeCompletionContext(context, text, position, depth),
                                                         parent(parent), m_context(context)
{
    m_workingOnDocument = parent->parent->m_currentDocument;
    QString currentLine = "\n" + text.split("\n").last(); // we'll only look at the last line, as 99% of python statements are limited to one line
    kDebug() << "Doing auto-completion context scan for: " << currentLine;
    
    QRegExp importsub("(.*)\n[\\s]*from(.*)import[\\s]*$");
    importsub.setMinimal(true);
    bool is_importSub = importsub.exactMatch(currentLine);
    QRegExp importsub2("(.*)\n[\\s]*(from(.*)|import(.*))\\.$");
    importsub2.setMinimal(true);
    bool is_importSub2 = importsub2.exactMatch(currentLine);
    if ( is_importSub || is_importSub2 ) {
        QStringList for_module_match;
        if ( is_importSub ) for_module_match = importsub.capturedTexts();
        else for_module_match = importsub2.capturedTexts();
        
        kDebug() << for_module_match;
        
        QString for_module;
        if ( is_importSub ) for_module = for_module_match.last().replace(" ", "");
        else for_module = for_module_match[3].replace(" ", "");
            
        kDebug() << "Matching against module name: " << for_module_match;
        m_operation = PythonCodeCompletionContext::ImportSubCompletion;
        m_subForModule = for_module;
        kDebug() << "submodule: " << for_module;
        return;
    }
    
    QRegExp newStatementCompletion("(.*)\n[\\s]*$");
    newStatementCompletion.setMinimal(true);
    bool isNewStatementCompletion = newStatementCompletion.exactMatch(currentLine);
    if ( isNewStatementCompletion ) {
        m_operation = PythonCodeCompletionContext::NewStatementCompletion;
        return;
    }
    
    QRegExp importfile("(.*)\n[\\s]*import[\\s]*$");
    importfile.setMinimal(true);
    bool is_importfile = importfile.exactMatch(currentLine);
    QRegExp fromimport("(.*)\n[\\s]*from[\\s]*$");
    fromimport.setMinimal(true);
    bool is_fromimport = fromimport.exactMatch(currentLine);
    if ( is_importfile || is_fromimport ) {
        kDebug() << "Autocompletion type: import completion";
        m_operation = PythonCodeCompletionContext::ImportFileCompletion;
        return;
    }
    
    QRegExp attributeAccess(".*\n[\\s]*(.*\\.)*$");
    attributeAccess.setMinimal(true);
    bool is_attributeAccess = attributeAccess.exactMatch(currentLine);
    if ( is_attributeAccess ) {
        QStringList expr = currentLine.split(".");
        expr.removeAll("");
        m_guessTypeOfExpression = expr.join(".");
        m_guessTypeOfExpression.replace(QRegExp("\"(.*)\""), "\"STRING\"").replace(QRegExp("(.*)\n[\\s]*"), "");
        kDebug() << "Guess type of this expression: " << m_guessTypeOfExpression;
        m_operation = PythonCodeCompletionContext::MemberAccessCompletion;
        return;
    }
    
    QRegExp noCompletionPossible("(.*)\n[\\s]*(class|def)[\\s]*$");
    noCompletionPossible.setMinimal(true);
    bool is_noCompletionPossible = noCompletionPossible.exactMatch(currentLine);
    if ( is_noCompletionPossible ) {
        m_operation = PythonCodeCompletionContext::NoCompletion;
        return;
    }
    
    QRegExp memberaccess("");
    kDebug() << "Is import file: " << is_importfile;
//     Q_ASSERT(false);
}


}
