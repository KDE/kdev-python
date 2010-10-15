#ifndef IMPORTFILEITEM_H
#define IMPORTFILEITEM_H

#include <language/codecompletion/abstractincludefilecompletionitem.h>
#include "navigationwidget.h"

namespace Python {

typedef KDevelop::AbstractIncludeFileCompletionItem<NavigationWidget> IncludeFileItemBase;

class ImportFileItem : public IncludeFileItemBase
{

public:
    ImportFileItem(const KDevelop::IncludeItem& include)
        : IncludeFileItemBase(include) {};
    virtual ~ImportFileItem();
    
    virtual void execute(KTextEditor::Document* document, const KTextEditor::Range& word);
};

#endif // IMPORTFILEITEM_H

}