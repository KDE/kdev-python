#ifndef KEYWORDITEM_H
#define KEYWORDITEM_H

#include <language/codecompletion/normaldeclarationcompletionitem.h>

using namespace KDevelop;

namespace Python {

class KeywordItem : public NormalDeclarationCompletionItem
{

public:
    KeywordItem(KDevelop::CodeCompletionContext::Ptr context, QString keyword);
    virtual void execute ( KTextEditor::Document* document, const KTextEditor::Range& word );
    virtual QVariant data ( const QModelIndex& index, int role, const KDevelop::CodeCompletionModel* model ) const;
    QString m_keyword;
};

}

#endif // KEYWORDITEM_H
