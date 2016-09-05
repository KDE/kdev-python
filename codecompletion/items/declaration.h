/*****************************************************************************
 * Copyright (c) 2011-2016 Sven Brauch <svenbrauch@googlemail.com>           *
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
 *****************************************************************************
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
    virtual QVariant data(const QModelIndex& index, int role, const KDevelop::CodeCompletionModel* model) const override;
    QString shortenedTypeString(KDevelop::DeclarationPointer decl, int desiredTypeLength) const override;

    void setTypeHint(PythonCodeCompletionContext::ItemTypeHint type);
    void addMatchQuality(int add);

    bool createsExpandingWidget() const override
    {
        return true;
    }

    QWidget* createExpandingWidget(const CodeCompletionModel* /*model*/) const override
    {
        return new Python::NavigationWidget(m_declaration, {}, {}, {}, KDevelop::AbstractNavigationWidget::EmbeddableWidget);
    }

protected:
    PythonCodeCompletionContext::ItemTypeHint m_typeHint;
    int m_addMatchQuality;
};

} // namespace Python

#endif
