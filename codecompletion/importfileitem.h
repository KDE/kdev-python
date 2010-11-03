#ifndef IMPORTFILEITEM_H
#define IMPORTFILEITEM_H

#include <language/codecompletion/abstractincludefilecompletionitem.h>
#include "navigationwidget.h"
#include <shell/project.h>

namespace Python {

typedef KDevelop::AbstractIncludeFileCompletionItem<NavigationWidget> IncludeFileItemBase;

class ImportFileItem : public IncludeFileItemBase
{

public:
    ImportFileItem(const KDevelop::IncludeItem& include);
    virtual ~ImportFileItem();
    
    virtual void execute(KTextEditor::Document* document, const KTextEditor::Range& word);
    QString moduleName;
    KDevelop::IProject* fromProject;
};

}

#endif // IMPORTFILEITEM_H