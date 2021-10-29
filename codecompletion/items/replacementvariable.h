/*
    SPDX-FileCopyrightText: 2013 Atanas Gospodinov <atanas.r.gospodinov@gmail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef REPLACEMENTVARIABLE_H
#define REPLACEMENTVARIABLE_H

#include <language/codecompletion/normaldeclarationcompletionitem.h>

#include "codecompletion/helpers.h"

using namespace KDevelop;

namespace Python {

class ReplacementVariableItem : public CompletionTreeItem
{
public:
    ReplacementVariableItem(const ReplacementVariable &variable, const QString &description, bool hasEditableFields, KTextEditor::Range position = KTextEditor::Range::invalid());
    void execute(KTextEditor::View* view, const KTextEditor::Range& word) override;
    QVariant data(const QModelIndex& index, int role, const KDevelop::CodeCompletionModel* model) const override;

private:
    ReplacementVariable m_variable;
    QString m_description;
    bool m_hasEditableFields;
    KTextEditor::Range m_position;
};

}

#endif // REPLACEMENTVARIABLE_H
