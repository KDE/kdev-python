#include "pythoncodecompletioncontext.h"

#include <language/codecompletion/codecompletionitem.h>
#include <language/codecompletion/normaldeclarationcompletionitem.h>
#include <language/codecompletion/abstractincludefilecompletionitem.h>
#include <language/util/includeitem.h>

#include <language/duchain/duchainpointer.h>
#include <language/duchain/declaration.h>

#include "navigationwidget.h"
#include "importfileitem.h"
#include <qprocess.h>
#include <interfaces/icore.h>
#include <interfaces/iprojectcontroller.h>
#include <interfaces/iproject.h>
#include <project/projectmodel.h>
#include <QtCore/QRegExp>

using namespace KDevelop;

typedef QPair<Declaration*, int> DeclarationDepthPair;

namespace Python {

QList<CompletionTreeItemPointer> PythonCodeCompletionContext::completionItems(bool& abort, bool fullCompletion)
{
    QList<CompletionTreeItemPointer> items;
    
    
    if ( m_operation == PythonCodeCompletionContext::ImportFileCompletion ) {
        m_maxFolderScanDepth = 1;
        foreach ( ImportFileItem* item, includeFileItems() ) {
            item->includeItem.name = QString(item->moduleName + " (from " + KUrl::relativeUrl(item->fromProject->folder(), item->includeItem.basePath) + ")");
            items << CompletionTreeItemPointer( item );
        }
    }
    else {
        QList<DeclarationDepthPair> declarations = m_duContext->allDeclarations(CursorInRevision::invalid(), m_duContext->topContext());
        
        Declaration* currentDeclaration;
        int count = declarations.length();
        for ( int i = 0; i < count; i++ ) {
            currentDeclaration = declarations.at(i).first;
            DeclarationPointer ptr(currentDeclaration);
            items << CompletionTreeItemPointer( new NormalDeclarationCompletionItem(ptr) );
        }
    }
    
    return items;
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
    if ( ! folder ) return QList<ImportFileItem*>();
    if ( m_maxFolderScanDepth < m_folderStack.count() ) return QList<ImportFileItem*>();
    QList<ImportFileItem*> items;
    foreach ( KDevelop::ProjectFolderItem* folder, folder->folderList() ) {
        if ( ! folder ) continue;
        m_folderStack.push(folder);
        kDebug() << "Scanning for include items: " << folder->folderName();
        items << fileItemsForFolder(folder, project);
        
        // Add the folder
        IncludeItem* folderItem = new IncludeItem();
        folderItem->basePath = m_folderStack.top()->url();
        folderItem->isDirectory = true;
        ImportFileItem* importFolderItem = new ImportFileItem(*folderItem);
        importFolderItem->fromProject = project;
        importFolderItem->moduleName = folder->folderName();
        items << importFolderItem;
        
        // Add all sub-items and folders
        foreach ( ProjectFileItem* file, folder->fileList() ) {
            if ( ! file->fileName().endsWith(".py") || file->fileName() == "__init__.py" ) continue;
            IncludeItem* item = new IncludeItem();
            item->basePath = m_folderStack.top()->url();
            ImportFileItem* importItem = new ImportFileItem(*item);
            importItem->moduleName = file->fileName().replace(".py", "");
            importItem->fromProject = project;
            items << importItem;
        }
        m_folderStack.pop();
    }
    return items;
}

PythonCodeCompletionContext::PythonCodeCompletionContext(DUContextPointer context, const QString& text, const KDevelop::CursorInRevision& position, int depth): CodeCompletionContext(context, text, position, depth)
{
    kDebug() << text;
    QRegExp importfile("(.*)[\\s]*import[\\s]$");
    importfile.setMinimal(true);
    QRegExp memberaccess("");
    bool is_importfile = importfile.exactMatch(text);
    if ( is_importfile ) m_operation = PythonCodeCompletionContext::ImportFileCompletion;
    kDebug() << "Is import file: " << is_importfile;
//     Q_ASSERT(false);
}


}
