/*****************************************************************************
 * Copyright (c) 2011 Sven Brauch <svenbrauch@googlemail.com>                *
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
