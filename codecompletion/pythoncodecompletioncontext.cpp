#include "pythoncodecompletioncontext.h"

#include <language/codecompletion/codecompletionitem.h>
#include <language/codecompletion/normaldeclarationcompletionitem.h>
#include <language/codecompletion/abstractincludefilecompletionitem.h>
#include <language/util/includeitem.h>

#include <language/duchain/duchainpointer.h>
#include <language/duchain/declaration.h>

#include "navigationwidget.h"
#include "importfileitem.h"

using namespace KDevelop;

typedef QPair<Declaration*, int> DeclarationDepthPair;

namespace Python {

QList<CompletionTreeItemPointer> PythonCodeCompletionContext::completionItems(bool& abort, bool fullCompletion)
{
    QList<CompletionTreeItemPointer> items;
    
    QList<DeclarationDepthPair> declarations = m_duContext->allDeclarations(CursorInRevision::invalid(), m_duContext->topContext());
    
    Declaration* currentDeclaration;
    int count = declarations.length();
    for ( int i = 0; i < count; i++ ) {
        currentDeclaration = declarations.at(i).first;
        DeclarationPointer ptr(currentDeclaration);
        items << CompletionTreeItemPointer( new NormalDeclarationCompletionItem(ptr) );
    }
    
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