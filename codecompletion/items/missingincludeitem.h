/*****************************************************************************
 * Copyright (c) 2013 Sven Brauch <svenbrauch@googlemail.com>                *
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
 *****************************************************************************/

#ifndef PYTHON_MISSINGINCLUDEITEM_H
#define PYTHON_MISSINGINCLUDEITEM_H

#include "navigation/navigationwidget.h"
#include <language/codecompletion/codecompletionitem.h>

namespace Python {

/// Class for adding an import. Will figure out where to add it by itself.
class MissingIncludeItem : public KDevelop::CompletionTreeItem {
public:
    MissingIncludeItem(const QString& insertText, const QString& matchText, const QString& removeComponents=QString());
    virtual void execute(KTextEditor::View* view, const KTextEditor::Range& word) override;
    virtual QVariant data(const QModelIndex& index, int role, const KDevelop::CodeCompletionModel* model) const override;

private:
    const QString m_text;
    const QString m_matchText;
    const QString m_removeComponents;
};

}

#endif // MISSINGINCLUDEITEM_H
