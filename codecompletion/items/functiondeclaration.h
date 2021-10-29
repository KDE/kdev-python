/*
    SPDX-FileCopyrightText: 2011 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef FUNCTIONDECLARATIONCOMPLETIONITEM_H
#define FUNCTIONDECLARATIONCOMPLETIONITEM_H

#include <language/codecompletion/normaldeclarationcompletionitem.h>
#include <language/duchain/functiondeclaration.h>

#include "declaration.h"

using namespace KDevelop;

namespace Python {

class FunctionDeclarationCompletionItem : public Python::PythonDeclarationCompletionItem
{

public:
    FunctionDeclarationCompletionItem(DeclarationPointer decl, KDevelop::CodeCompletionContext::Ptr context);
    ~FunctionDeclarationCompletionItem() override;
    int argumentHintDepth() const override;
    virtual int atArgument() const;
    void setAtArgument(int d);
    void setDepth(int d);
    void setDoNotCall(bool doNotCall);

    QVariant data(const QModelIndex& index, int role, const CodeCompletionModel* model) const override;
    void executed(KTextEditor::View* view, const KTextEditor::Range& word) override;
private:
    int m_atArgument;
    int m_depth;
    // indicates that no parentheses should be added when executing this item,
    // e.g. for import completion or inheritance
    bool m_doNotCall;
};

}

#endif // FUNCTIONDECLARATIONCOMPLETIONITEM_H
