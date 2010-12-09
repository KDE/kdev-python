#ifndef PYTHONCODECOMPLETIONCONTEXT_H
#define PYTHONCODECOMPLETIONCONTEXT_H

#include <language/codecompletion/codecompletioncontext.h>
#include "pythoncompletionexport.h"
#include <language/duchain/duchainpointer.h>
#include <qstack.h>
#include <importfileitem.h>

using namespace KDevelop;

namespace KDevelop {
    class IProject;
    class ProjectFolderItem;
}

namespace Python {

class KDEVPYTHONCOMPLETION_EXPORT PythonCodeCompletionContext : public KDevelop::CodeCompletionContext
{
public:
    enum CompletionContextType {
        ImportFileCompletion,
        MemberAccessCompletion,
        DefaultCompletion,
        ImportSubCompletion,
        NoCompletion,
        NewStatementCompletion
    };
    
    PythonCodeCompletionContext(DUContextPointer context, const QString& text, const KDevelop::CursorInRevision& position, int depth);
    virtual QList< KDevelop::CompletionTreeItemPointer > completionItems(bool& abort, bool fullCompletion = true);
    QList<ImportFileItem*> includeFileItems();
    QList<ImportFileItem*> fileItemsForFolder(KDevelop::ProjectFolderItem* folder, KDevelop::IProject* project);
    QList<ImportFileItem*> findFilesForName(const QString& name);
    
    CompletionContextType m_operation;
    QStack<ProjectFolderItem*> m_folderStack;
    int m_maxFolderScanDepth;
    QStringList m_searchingForModule;
    QString m_subForModule;
    
private:
    bool m_dontAddMe;
};

}

#endif // PYTHONCODECOMPLETIONCONTEXT_H
