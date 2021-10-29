/*
    SPDX-FileCopyrightText: 2011-2016 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef PYTHONDECLARATIONCOMPLETIONITEM_H
#define PYTHONDECLARATIONCOMPLETIONITEM_H

#include <language/codecompletion/normaldeclarationcompletionitem.h>
#include <language/codecompletion/codecompletioncontext.h>
#include <language/codecompletion/codecompletionmodel.h>
#include "codecompletion/context.h"

namespace Python {

class PythonDeclarationCompletionItem : public KDevelop::NormalDeclarationCompletionItem {
public:
    PythonDeclarationCompletionItem(KDevelop::DeclarationPointer decl = KDevelop::DeclarationPointer(), 
                                    QExplicitlySharedDataPointer<KDevelop::CodeCompletionContext> context = QExplicitlySharedDataPointer<KDevelop::CodeCompletionContext>(), 
                                    int inheritanceDepth = 0);
    QVariant data(const QModelIndex& index, int role, const KDevelop::CodeCompletionModel* model) const override;
    QString shortenedTypeString(const KDevelop::DeclarationPointer& decl, int desiredTypeLength) const override;

    void setTypeHint(PythonCodeCompletionContext::ItemTypeHint type);
    void addMatchQuality(int add);

    bool createsExpandingWidget() const override
    {
        return true;
    }

    QWidget* createExpandingWidget(const CodeCompletionModel* /*model*/) const override
    {
        return new Python::NavigationWidget(m_declaration, {}, KDevelop::AbstractNavigationWidget::EmbeddableWidget);
    }

protected:
    PythonCodeCompletionContext::ItemTypeHint m_typeHint;
    int m_addMatchQuality;
};

} // namespace Python

#endif
