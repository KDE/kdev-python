#include "pythoncodecompletioncontext.h"
#include <language/codecompletion/codecompletionitem.h>
#include <language/duchain/duchainpointer.h>
#include <language/codecompletion/normaldeclarationcompletionitem.h>
#include <language/util/includeitem.h>
#include <language/codecompletion/abstractincludefilecompletionitem.h>
#include "navigationwidget.h"
#include "importfileitem.h"

using namespace KDevelop;

namespace Python {

QList<CompletionTreeItemPointer> PythonCodeCompletionContext::completionItems(bool& abort, bool fullCompletion)
{
    QList<CompletionTreeItemPointer> items;
    
    kDebug() << "Adding testing item to completion list";
    
    IncludeItem item;
    item.name = "Foo";
    items << CompletionTreeItemPointer( new ImportFileItem(item) );
    
    return items;
}

PythonCodeCompletionContext::PythonCodeCompletionContext(DUContextPointer context, const QString& text, const KDevelop::CursorInRevision& position, int depth): CodeCompletionContext(context, text, position, depth)
{

}


}