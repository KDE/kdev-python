/*
 * This file is part of KDevelop
 * Copyright 2010 Sven Brauch <svenbrauch@googlemail.com>
 * Licensed under the GNU GPL
 * */

#include "pythoncodecompletioncontext.h"

#include <language/codecompletion/normaldeclarationcompletionitem.h>
#include <language/codecompletion/abstractincludefilecompletionitem.h>
#include <language/codecompletion/codecompletionitem.h>
#include <language/util/includeitem.h>

#include <language/duchain/duchainpointer.h>
#include <language/duchain/declaration.h>

#include "navigation/navigationwidget.h"
#include "importfileitem.h"
#include "functiondeclarationcompletionitem.h"

#include <qprocess.h>
#include <interfaces/icore.h>
#include <interfaces/iprojectcontroller.h>
#include <interfaces/iproject.h>
#include <project/projectmodel.h>
#include <QtCore/QRegExp>

#include <language/duchain/functiondeclaration.h>
#include <language/codecompletion/codecompletionitem.h>
#include "keyworditem.h"

using namespace KDevelop;

typedef QPair<Declaration*, int> DeclarationDepthPair;

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
        m_maxFolderScanDepth = 1;
        foreach ( ImportFileItem* item, includeFileItems() ) {
            item->includeItem.name = QString(item->moduleName + " (from " + KUrl::relativeUrl(item->fromProject->folder(), item->includeItem.basePath) + ")");
            items << CompletionTreeItemPointer( item );
        }
    }
    else if ( m_operation == PythonCodeCompletionContext::ImportSubCompletion ) {
        kDebug() << "Stuff found for completion: " << findFilesForName(m_subForModule);
        foreach ( ImportFileItem* item, findFilesForName(m_subForModule) ) {
            item->includeItem.name = QString(item->moduleName + " (from " + KUrl::relativeUrl(item->fromProject->folder(), item->includeItem.basePath) + ")");
            items << CompletionTreeItemPointer( item );
        }
    }
    else if ( m_operation == PythonCodeCompletionContext::MemberAccessCompletion ) {
        // we don't have type support, so we cannot support completing mebers yet. But we can at least prevent kdevelop from opening a pointless
        // popup with completion items you don't want
    }
    else {
        // it's stupid to display a 3-letter completion item on manually invoked code completion and makes everything look crowded
        if ( m_operation == PythonCodeCompletionContext::NewStatementCompletion && ! fullCompletion ) {
            QStringList keywordItems;
            keywordItems << "def" << "class" << "lambda" << "global" << "print";
            foreach ( const QString& current, keywordItems ) {
                items << CompletionTreeItemPointer(new KeywordItem(KDevelop::CodeCompletionContext::Ptr(this), current));
            }
        }
        if ( abort ) {
            return QList<CompletionTreeItemPointer>();
        }
        QList<DeclarationDepthPair> declarations = m_duContext->allDeclarations(m_position, m_duContext->topContext());
        
        DeclarationPointer currentDeclaration;
        int count = declarations.length();
        for ( int i = 0; i < count; i++ ) {
            if ( abort ) {
                return items;
            }
            currentDeclaration = DeclarationPointer(declarations.at(i).first);
//             if ( currentDeclaration.data()->rangeInCurrentRevision().start > m_position.castToSimpleCursor() ) continue;
            
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
    }
    
    m_searchingForModule.clear();
    m_subForModule.clear();
    
    return items;
}

QList< ImportFileItem* > PythonCodeCompletionContext::findFilesForName(const QString& name)
{
    kDebug() << "Name: " << name;
    QStringList resolvedName = name.split(".");
    m_maxFolderScanDepth = resolvedName.length() + 1;
    m_searchingForModule = resolvedName;
    return includeFileItems();
}

QList<ImportFileItem*> PythonCodeCompletionContext::includeFileItems() {
    QList<ImportFileItem*> items;
    foreach  (IProject* project, ICore::self()->projectController()->projects() ) {
        foreach ( KDevelop::ProjectFolderItem* folder, project->foldersForUrl( KUrl(project->folder().url()) ) ) {
            m_folderStack.push(folder);
            items << fileItemsForFolder(folder, project);
            m_folderStack.pop();
        }
    }
    return items;
}

QList<ImportFileItem*> PythonCodeCompletionContext::fileItemsForFolder(KDevelop::ProjectFolderItem* folder, IProject* project)
{
    kDebug() << " +++++ Processing folder: " << folder->folderName();
    kDebug() << "current folder stack count " << m_folderStack.count();
    if ( ! folder ) {
        m_dontAddMe = true;
        return QList<ImportFileItem*>();
    }
    bool continue_recursion = true;
    bool do_recursion = true;
    
    kDebug() << m_maxFolderScanDepth << m_folderStack.count() << m_searchingForModule;
    
    if ( m_maxFolderScanDepth - 1 < m_folderStack.count() ) continue_recursion = false; // we dont offer foo.bar.baz.bang.bar if there's only one dot in the address by now
    
    if ( m_searchingForModule.length() > 0 && folder->url() != project->folder().url() ) {
        if ( m_searchingForModule.length() >= m_folderStack.count() && m_searchingForModule.at(m_folderStack.count() - 2) != folder->folderName() ) {
            kDebug() << "Skip: " << m_searchingForModule.at(m_folderStack.count() - 2) << m_searchingForModule << m_folderStack.count() - 2 << folder->folderName();
            m_dontAddMe = true;
            return QList<ImportFileItem*>();
        }
        else if ( m_searchingForModule.at(m_folderStack.count() - 2) != folder->folderName() ) {
            m_dontAddMe = true;
            return QList<ImportFileItem*>();
        }
        kDebug() << "USE: " << m_searchingForModule.at(m_folderStack.count() - 2) << m_searchingForModule << m_folderStack << folder->folderName();
    }
    
    kDebug() << " >>>>> For directory " << folder->folderName() << " : " << "doing recursion: " << do_recursion << "; continuing downwards: " << continue_recursion;
    
    QList<ImportFileItem*> items;
    foreach ( KDevelop::ProjectFolderItem* folder, folder->folderList() ) {
        if ( ! folder ) continue;
        m_folderStack.push(folder);
        if ( continue_recursion ) {
            kDebug() << "Scanning for include items: " << folder->folderName();
            items << fileItemsForFolder(folder, project);
            if ( m_dontAddMe ) {
                m_dontAddMe = false;
                m_folderStack.pop();
                continue;
            }
        }
        
        // only add items when at right level
        if ( m_searchingForModule.length() != 0 && m_maxFolderScanDepth != m_folderStack.count() ) {
            kDebug() << "CONTINUE: " << m_maxFolderScanDepth << m_folderStack.count();
            if ( m_searchingForModule.length() < m_folderStack.count() ) do_recursion = false; // don't add items from here, we're too deep 
            else {
                // we're not yet deep enough, so don't even add the folder
                m_folderStack.pop();
                continue;
            }
        }
        else {
            kDebug() << "ADD: " << m_maxFolderScanDepth << m_folderStack.count();
            kDebug() << "adding files and folders from directory " << folder->folderName();
        }
        
        // Add the folder
        IncludeItem* folderItem = new IncludeItem();
        folderItem->basePath = folder->url();
        folderItem->isDirectory = true;
        ImportFileItem* importFolderItem = new ImportFileItem(*folderItem);
        importFolderItem->fromProject = project;
        importFolderItem->moduleName = folder->folderName();
        items << importFolderItem;
        
        if ( continue_recursion && do_recursion ) {
            // Add all sub-items and folders
            foreach ( ProjectFileItem* file, folder->fileList() ) {
                if ( ! file->fileName().endsWith(".py") || file->fileName() == "__init__.py" ) continue;
                IncludeItem* item = new IncludeItem();
                item->basePath = folder->url();
                ImportFileItem* importItem = new ImportFileItem(*item);
                importItem->moduleName = file->fileName().replace(".py", "");
                importItem->fromProject = project;
                items << importItem;
            }
        }
        m_folderStack.pop();
    }
    return items;
}

PythonCodeCompletionContext::PythonCodeCompletionContext(DUContextPointer context, const QString& text, const KDevelop::CursorInRevision& position, 
                                                         int depth): CodeCompletionContext(context, text, position, depth)
{
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
        m_operation = PythonCodeCompletionContext::ImportFileCompletion;
        return;
    }
    
    QRegExp attributeAccess("(.*)\n[\\s]*(.*)\\.$");
    attributeAccess.setMinimal(true);
    bool is_attributeAccess = attributeAccess.exactMatch(currentLine);
    if ( is_attributeAccess ) {
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
