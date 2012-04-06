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

Python::KeywordItem::KeywordItem(KDevelop::CodeCompletionContext::Ptr context, QString keyword, Flags flags)
    : NormalDeclarationCompletionItem (DeclarationPointer(), context, 0),
    m_flags(flags)
{
    m_keyword = keyword;
}

void Python::KeywordItem::execute(KTextEditor::Document* document, const KTextEditor::Range& word)
{
    if ( m_flags == ForceLineBeginning ) {
        KTextEditor::Range newRange(KTextEditor::Cursor(word.start().line(), 0), word.end());
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
