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
    KeywordItem(KDevelop::CodeCompletionContext::Ptr context, QString keyword, Flags flags = NoFlags);
    virtual void execute(KTextEditor::Document* document, const KTextEditor::Range& word);
    virtual QVariant data(const QModelIndex& index, int role, const KDevelop::CodeCompletionModel* model) const;
private:
    QString m_keyword;
    Flags m_flags;
    
};

}

#endif // KEYWORDITEM_H
