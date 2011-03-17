/*
 * This file is part of KDevelop
 * Copyright 2011 by Sven Brauch
 */

#include <language/codecompletion/codecompletionmodel.h>
#include <language/duchain/duchainutils.h>

#include <KTextEditor/View>
#include <KTextEditor/Document>

#include "implementfunctioncompletionitem.h"

using namespace KDevelop;
using namespace KTextEditor;

namespace Python {

ImplementFunctionCompletionItem::ImplementFunctionCompletionItem(const QString& name, const QString& arguments, const QString& writeArguments, const QString& previousIndent)
    : m_arguments(arguments), m_writeArguments(writeArguments), m_name(name), m_previousIndent(previousIndent)
{
    
}

void ImplementFunctionCompletionItem::execute(KTextEditor::Document* document, const KTextEditor::Range& word)
{
    const QString finalText = m_name + "(" + m_writeArguments + "):";
    document->replaceText(word, finalText);
    document->insertLine(word.start().line() + 1, m_previousIndent + "\t"); // 4 spaces is indentation for python. everyone does it like this. you must, too.
    if ( View* view = document->activeView() ) {
        view->setCursorPosition(Cursor(word.end().line() + 1, m_previousIndent.length() + 4));
    }
}

QVariant ImplementFunctionCompletionItem::data(const QModelIndex& index, int role, const KDevelop::CodeCompletionModel* model) const
{
    switch ( role ) {
        case Qt::DisplayRole:
            switch ( index.column() ) {
                case KDevelop::CodeCompletionModel::Name:
                    return m_name + "(" + m_arguments + ")";
                case KDevelop::CodeCompletionModel::Postfix:
                    return "";
                case KDevelop::CodeCompletionModel::Prefix:
                    return "implement method";
                default:
                    return "";
            }
        case Qt::DecorationRole:
            if( index.column() == KDevelop::CodeCompletionModel::Icon ) {
                KDevelop::CodeCompletionModel::CompletionProperties p(KDevelop::CodeCompletionModel::Function);
                return DUChainUtils::iconForProperties(p);
            }
        default: return CompletionTreeItem::data(index, role, model);
    }
}

} // namespace Python