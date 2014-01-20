/*****************************************************************************
 * Copyright (c) 2011 Sven Brauch <svenbrauch@googlemail.com>                *
 *                                                                           *
 * This program is free software; you can redistribute it and/or             *
 * modify it under the terms of the GNU General Public License as            *
 * published by the Free Software Foundation; either version 2 of            *
 * the License, or (at your option) any later version.                       *
 *                                                                           *           
 * This program is distributed in the hope that it will be useful,           *
 * but WITHOUT ANY WARRANTY; without even the implied warranty of            *
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             *
 * GNU General Public License for more details.                              *
 *                                                                           *   
 * You should have received a copy of the GNU General Public License         *
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.     *
 *****************************************************************************
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

void KeywordItem::execute(Document* document, const Range& word)
{
    if ( m_flags & ForceLineBeginning ) {
        Range newRange(Cursor(word.start().line(), 0), word.end());
        document->replaceText(newRange, m_keyword);
    }
    else {
        document->replaceText(word, m_keyword);
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
            return QVariant(kw.replace("\n", ""));
        }
        else if ( index.column() == KTextEditor::CodeCompletionModel::Prefix ) {
            return QVariant(m_description);
        }
        else {
            return QVariant("");
        }
        break;
    case KTextEditor::CodeCompletionModel::ItemSelected:
        return QVariant("");
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
