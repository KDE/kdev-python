/*
    SPDX-FileCopyrightText: 2011 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef IMPLEMENTFUNCTIONCOMPLETIONITEM_H
#define IMPLEMENTFUNCTIONCOMPLETIONITEM_H

#include <language/codecompletion/codecompletionitem.h>
#include <QStringList>

using namespace KDevelop;

namespace Python {

class ImplementFunctionCompletionItem : public CompletionTreeItem
{
public:
    ImplementFunctionCompletionItem(const QString& name, const QStringList& arguments, const QString& previousIndent);
    void execute(KTextEditor::View* view, const KTextEditor::Range& word) override;
    QVariant data(const QModelIndex& index, int role, const CodeCompletionModel* model) const override;

private:
    QStringList m_arguments;
    QString m_name;
    QString m_previousIndent;
};

} // namespace Python

#endif // IMPLEMENTFUNCTIONCOMPLETIONITEM_H
