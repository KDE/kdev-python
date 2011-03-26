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

using namespace KDevelop;

namespace Python {

class FunctionDeclarationCompletionItem : public KDevelop::NormalDeclarationCompletionItem
{

public:
    FunctionDeclarationCompletionItem(DeclarationPointer decl);
    virtual ~FunctionDeclarationCompletionItem();
    virtual int argumentHintDepth() const;
    void setArgumentHintDepth(int d);
    
    virtual QVariant data(const QModelIndex& index, int role, const CodeCompletionModel* model) const;
    
    virtual void executed(KTextEditor::Document* document, const KTextEditor::Range& word);
private:
    int m_argumentHintDepth;
};

}

#endif // FUNCTIONDECLARATIONCOMPLETIONITEM_H
