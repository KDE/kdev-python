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
    virtual ~FunctionDeclarationCompletionItem();
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
