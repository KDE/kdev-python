/*
    SPDX-FileCopyrightText: 2011 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef KEYWORDITEM_H
#define KEYWORDITEM_H

#include <language/codecompletion/normaldeclarationcompletionitem.h>

using namespace KDevelop;

namespace Python {

class KeywordItem : public NormalDeclarationCompletionItem
{

public:
    enum Flags {
        NoFlags = 0x0,
        ForceLineBeginning = 0x1,
        ImportantItem = 0x2
    };
    KeywordItem(CodeCompletionContext::Ptr context, QString keyword, QString descr, Python::KeywordItem::Flags flags = NoFlags);
    void execute(KTextEditor::View* view, const KTextEditor::Range& word) override;
    QVariant data(const QModelIndex& index, int role, const KDevelop::CodeCompletionModel* model) const override;
private:
    QString m_keyword;
    QString m_description;
    Flags m_flags;
    
};

}

#endif // KEYWORDITEM_H
