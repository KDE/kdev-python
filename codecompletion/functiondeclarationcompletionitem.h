#ifndef FUNCTIONDECLARATIONCOMPLETIONITEM_H
#define FUNCTIONDECLARATIONCOMPLETIONITEM_H

#include <language/codecompletion/normaldeclarationcompletionitem.h>
#include <language/duchain/functiondeclaration.h>

using namespace KDevelop;

namespace Python {

class FunctionDeclarationCompletionItem : public KDevelop::NormalDeclarationCompletionItem
{

public:
    FunctionDeclarationCompletionItem(DeclarationPointer decl);
    virtual ~FunctionDeclarationCompletionItem();
    
    virtual void executed(KTextEditor::Document* document, const KTextEditor::Range& word);
};

}

#endif // FUNCTIONDECLARATIONCOMPLETIONITEM_H
