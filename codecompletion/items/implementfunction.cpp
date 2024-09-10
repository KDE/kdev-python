/*
    SPDX-FileCopyrightText: 2011 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#include "implementfunction.h"

#include <language/codecompletion/codecompletionmodel.h>
#include <language/duchain/duchainutils.h>
#include <interfaces/icore.h>
#include <interfaces/isession.h>
#include <interfaces/idocumentcontroller.h>

#include <KTextEditor/View>
#include <KTextEditor/Document>
#include <KTextEditor/Editor>

#include <QIcon>

using namespace KDevelop;
using namespace KTextEditor;

namespace Python {

ImplementFunctionCompletionItem::ImplementFunctionCompletionItem(const QString& name, const QStringList& arguments, const QString& previousIndent)
    : m_arguments(arguments), m_name(name), m_previousIndent(previousIndent)
{
    
}

void ImplementFunctionCompletionItem::execute(KTextEditor::View* view, const KTextEditor::Range& word)
{
    auto document = view->document();
    const QString finalText = m_name + QStringLiteral("(") + m_arguments.join(QStringLiteral(", ")) + QStringLiteral("):");
    document->replaceText(word, finalText);
    // 4 spaces is indentation for python. everyone does it like this. you must, too.
    // TODO use kate settings
    document->insertLine(word.start().line() + 1, m_previousIndent + QStringLiteral("    "));
    if ( View* view = ICore::self()->documentController()->activeTextDocumentView() ) {
        view->setCursorPosition(Cursor(word.end().line() + 1, m_previousIndent.length() + 4));
    }
}

QVariant ImplementFunctionCompletionItem::data(const QModelIndex& index, int role, const KDevelop::CodeCompletionModel* model) const
{
    switch ( role ) {
        case KDevelop::CodeCompletionModel::MatchQuality: {
            return QVariant(m_name.startsWith(QStringLiteral("__")) ? 0 : 10);
        }
        case KDevelop::CodeCompletionModel::BestMatchesCount: {
            return QVariant(5);
        }
        case Qt::DisplayRole:
            switch ( index.column() ) {
                case KDevelop::CodeCompletionModel::Name:
                    return QVariant(m_name + QStringLiteral("(") + m_arguments.join(QStringLiteral(", ")) + QStringLiteral(")"));
                case KDevelop::CodeCompletionModel::Postfix:
                    return QVariant(QString());
                case KDevelop::CodeCompletionModel::Prefix:
                    return QVariant(QStringLiteral("Override method"));
                default:
                    return QVariant(QString());
            }
        case Qt::DecorationRole:
            if( index.column() == KDevelop::CodeCompletionModel::Icon ) {
                KDevelop::CodeCompletionModel::CompletionProperties p(KDevelop::CodeCompletionModel::Function);
                return DUChainUtils::iconForProperties(p);
            }
            // Fall through
        default: return CompletionTreeItem::data(index, role, model);
    }
}

} // namespace Python
