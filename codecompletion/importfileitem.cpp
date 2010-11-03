#include "importfileitem.h"
#include <ktexteditor/document.h>
#include <language/codecompletion/abstractincludefilecompletionitem.h>

using namespace KDevelop;

namespace Python {
    
ImportFileItem::ImportFileItem(const KDevelop::IncludeItem& include): AbstractIncludeFileCompletionItem< NavigationWidget >(include)
{
    
}

ImportFileItem::~ImportFileItem()
{

}

void ImportFileItem::execute(KTextEditor::Document* document, const KTextEditor::Range& word)
{
    kDebug() << "ImportFileItem executed";
    document->replaceText(word, moduleName);
}


}