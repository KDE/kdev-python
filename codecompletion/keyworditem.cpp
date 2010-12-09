#include "keyworditem.h"
#include <language/duchain/ducontext.h>
#include <KTextEditor/View>
#include <KTextEditor/Document>
#include <KTextEditor/CodeCompletionModel>
#include <language/codecompletion/codecompletionmodel.h>

using namespace KDevelop;
using namespace KTextEditor;

namespace Python {

Python::KeywordItem::KeywordItem(KDevelop::CodeCompletionContext::Ptr context, QString keyword) : NormalDeclarationCompletionItem ( DeclarationPointer(), context, 0 )
{
    m_keyword = keyword;
}

void Python::KeywordItem::execute ( KTextEditor::Document* document, const KTextEditor::Range& word )
{
    document->replaceText(word, m_keyword);
}

QVariant KeywordItem::data ( const QModelIndex& index, int role, const KDevelop::CodeCompletionModel* model ) const
{
    switch (role) {
    case KDevelop::CodeCompletionModel::IsExpandable:
        return QVariant(false);
    case Qt::DisplayRole:
        if (index.column() == KTextEditor::CodeCompletionModel::Name) {
            return QVariant(m_keyword);
        } else {
            return QVariant("");
        }
        break;
    case KTextEditor::CodeCompletionModel::ItemSelected:
        return QVariant("");
    case KTextEditor::CodeCompletionModel::InheritanceDepth:
        return QVariant(0);
    default:
        //pass
        break;
    }

    return NormalDeclarationCompletionItem::data(index, role, model);
}

}
