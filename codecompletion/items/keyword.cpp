/*
    SPDX-FileCopyrightText: 2011-2014 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#include "keyword.h"

#include <KTextEditor/View>
#include <KTextEditor/Document>
#include <KTextEditor/CodeCompletionModel>

#include <language/duchain/ducontext.h>
#include <language/codecompletion/codecompletionmodel.h>

using namespace KDevelop;
using namespace KTextEditor;

namespace Python {

KeywordItem::KeywordItem(KDevelop::CodeCompletionContext::Ptr context, QString keyword, QString descr, Flags flags)
    : NormalDeclarationCompletionItem (DeclarationPointer(), context, 0)
    , m_description(descr)
    , m_flags(flags)
{
    m_keyword = keyword;
}

void KeywordItem::execute(View* view, const Range& word)
{
    if ( m_flags & ForceLineBeginning ) {
        Range newRange(Cursor(word.start().line(), 0), word.end());
        view->document()->replaceText(newRange, m_keyword);
    }
    else {
        view->document()->replaceText(word, m_keyword);
    }
}

QVariant KeywordItem::data ( const QModelIndex& index, int role, const KDevelop::CodeCompletionModel* model ) const
{
    switch (role) {
    case KDevelop::CodeCompletionModel::IsExpandable:
        return QVariant(false);
    case Qt::DisplayRole:
        if (index.column() == KTextEditor::CodeCompletionModel::Name) {
            QString kw = m_keyword;
            return QVariant(kw.replace(QStringLiteral("\n"), QString()));
        }
        else if ( index.column() == KTextEditor::CodeCompletionModel::Prefix ) {
            return QVariant(m_description);
        }
        else {
            return QVariant(QString());
        }
        break;
    case KTextEditor::CodeCompletionModel::ItemSelected:
        return QVariant(QString());
    case KTextEditor::CodeCompletionModel::InheritanceDepth:
        return QVariant(0);
    case KDevelop::CodeCompletionModel::BestMatchesCount:
        return 5;
    case KDevelop::CodeCompletionModel::MatchQuality:
        if ( m_flags & ImportantItem ) {
            return 10;
        }
        return 0; // most keyword items are not that great for completion
    default:
        //pass
        break;
    }

    return NormalDeclarationCompletionItem::data(index, role, model);
}

}
