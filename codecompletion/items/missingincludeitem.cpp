/*
    SPDX-FileCopyrightText: 2013 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#include "missingincludeitem.h"

#include <language/codecompletion/codecompletionmodel.h>

#include <KTextEditor/Document>
#include <KTextEditor/View>

#include <KLocalizedString>
#include <QDebug>
#include "codecompletiondebug.h"

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
                    return QString();
                case KDevelop::CodeCompletionModel::Prefix:
                    return i18nc("programming; %1 is a code statement to be added in the editor", "Add \"%1\"", m_text);
                default:
                    return QString();
            }
    }
    return QVariant();
}

void MissingIncludeItem::execute(KTextEditor::View* view, const KTextEditor::Range& word)
{
    qCDebug(KDEV_PYTHON_CODECOMPLETION) << "executed with text" << m_text;
    // First, add the import statement to the top of the file
    // FIXME: deal with multi-line comments
    int insertAt = 0;
    for ( int i = 0; i < view->document()->lines(); i++ ) {
        const QString& line = view->document()->line(i);
        if ( line.trimmed().startsWith(QLatin1Char('#')) || line.trimmed().isEmpty() ) {
            continue;
        }

        if (    ( line.startsWith(QStringLiteral("import")) && m_text.startsWith(QStringLiteral("import")) )
             || ( line.startsWith(QStringLiteral("from")) && m_text.startsWith(QStringLiteral("from")) ) )
        {
            insertAt = i;
            break;
        }

        if ( ! line.startsWith(QStringLiteral("import")) && ! line.startsWith(QStringLiteral("from")) ) {
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
        view->document()->replaceText(KTextEditor::Range(start, end), m_matchText);
    }

    // Do this only later, otherwise ranges change
    view->document()->insertLine(qMax(0, insertAt - 1), m_text);
}

}
