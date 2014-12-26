/*****************************************************************************
 * Copyright (c) 2013 Atanas Gospodinov <atanas.r.gospodinov@gmail.com>      *
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
    virtual void execute(KTextEditor::View* view, const KTextEditor::Range& word) override;
    virtual QVariant data(const QModelIndex& index, int role, const KDevelop::CodeCompletionModel* model) const;

private:
    ReplacementVariable m_variable;
    QString m_description;
    bool m_hasEditableFields;
    KTextEditor::Range m_position;
};

}

#endif // REPLACEMENTVARIABLE_H
