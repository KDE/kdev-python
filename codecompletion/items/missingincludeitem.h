/*
    SPDX-FileCopyrightText: 2013 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef PYTHON_MISSINGINCLUDEITEM_H
#define PYTHON_MISSINGINCLUDEITEM_H

#include "navigation/navigationwidget.h"
#include <language/codecompletion/codecompletionitem.h>

namespace Python {

/// Class for adding an import. Will figure out where to add it by itself.
class MissingIncludeItem : public KDevelop::CompletionTreeItem {
public:
    MissingIncludeItem(const QString& insertText, const QString& matchText, const QString& removeComponents=QString());
    void execute(KTextEditor::View* view, const KTextEditor::Range& word) override;
    QVariant data(const QModelIndex& index, int role, const KDevelop::CodeCompletionModel* model) const override;

private:
    const QString m_text;
    const QString m_matchText;
    const QString m_removeComponents;
};

}

#endif // MISSINGINCLUDEITEM_H
