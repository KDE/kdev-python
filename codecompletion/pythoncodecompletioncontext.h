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
    
    PythonCodeCompletionContext(DUContextPointer context, const QString& text, const KDevelop::CursorInRevision& position, int depth, KUrl document);
    virtual QList< KDevelop::CompletionTreeItemPointer > completionItems(bool& abort, bool fullCompletion = true);
    QList<ImportFileItem*> includeFileItems();
    
    CompletionContextType m_operation;
    QStack<ProjectFolderItem*> m_folderStack;
    int m_maxFolderScanDepth;
    QStringList m_searchingForModule;
    QString m_subForModule;
    KUrl m_workingOnDocument;
    
private:
    bool m_dontAddMe;
};

}

#endif // PYTHONCODECOMPLETIONCONTEXT_H
