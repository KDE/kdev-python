#include "pythoncodecompletioncontext.h"
#include <language/codecompletion/codecompletionitem.h>
#include <language/duchain/duchainpointer.h>
#include <language/codecompletion/normaldeclarationcompletionitem.h>
#include <language/util/includeitem.h>

using namespace KDevelop;

QList<CompletionTreeItemPointer> PythonCodeCompletionContext::completionItems(bool& abort, bool fullCompletion)
{
    QList<CompletionTreeItemPointer> items;
    
    CompletionTreeItem* item = new CompletionTreeItem();
    items << CompletionTreeItemPointer( item );
    
    return items;
}

