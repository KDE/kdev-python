/*****************************************************************************
 * Copyright (c) 2013 Sven Brauch <svenbrauch@googlemail.com>                *
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
 *****************************************************************************/

#include "missingincludeitem.h"
#include <language/codecompletion/codecompletionmodel.h>
#include <KTextEditor/Document>
#include <KLocalizedString>

namespace Python {

MissingIncludeItem::MissingIncludeItem(const QString& insertText, const QString& matchText, const QString& removeComponents)
    : m_text(insertText)
    , m_matchText(matchText)
    , m_removeComponents(removeComponents)
{

}

QVariant MissingIncludeItem::data(const QModelIndex& index, int role, const KDevelop::CodeCompletionModel* /*model*/) const
{
    switch ( role ) {
        case Qt::DisplayRole:
            switch ( index.column() ) {
                case KDevelop::CodeCompletionModel::Name:
                    return m_matchText;
                case KDevelop::CodeCompletionModel::Postfix:
                    return "";
                case KDevelop::CodeCompletionModel::Prefix:
                    return i18nc("programming; %1 is a code statement to be added in the editor", "Add \"%1\"", m_text);
                default:
                    return "";
            }
    }
    return QVariant();
}

void MissingIncludeItem::execute(KTextEditor::Document* document, const KTextEditor::Range& word)
{
    kDebug() << "executed with text" << m_text;
    // First, add the import statement to the top of the file
    // FIXME: deal with multi-line comments
    int insertAt = 0;
    for ( int i = 0; i < document->lines(); i++ ) {
        const QString& line = document->line(i);
        if ( line.trimmed().startsWith('#') || line.trimmed().isEmpty() ) {
            continue;
        }

        if (    ( line.startsWith("import") && m_text.startsWith("import") )
             || ( line.startsWith("from") && m_text.startsWith("from") ) )
        {
            insertAt = i;
            break;
        }

        if ( ! line.startsWith("import") && ! line.startsWith("from") ) {
            // non-empty, non-comment, non-import line, so we insert it here; the common
            // situation this occurs in is when there's no imports yet.
            insertAt = i;
            break;
        }
    }

    // Then, eventually replace the text the user was typing
    if ( ! m_removeComponents.isEmpty() ) {
        const KTextEditor::Cursor end = word.end();
        const KTextEditor::Cursor start = end - KTextEditor::Cursor(0, m_removeComponents.length());
        document->replaceText(KTextEditor::Range(start, end), m_matchText);
    }

    // Do this only later, otherwise ranges change
    document->insertLine(qMax(0, insertAt - 1), m_text);
}

}
