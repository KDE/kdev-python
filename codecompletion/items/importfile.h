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

#ifndef IMPORTFILEITEM_H
#define IMPORTFILEITEM_H

#include <language/codecompletion/abstractincludefilecompletionitem.h>
#include <shell/project.h>

#include "duchain/navigation/navigationwidget.h"

namespace Python {

typedef KDevelop::AbstractIncludeFileCompletionItem<NavigationWidget> IncludeFileItemBase;

class ImportFileItem : public IncludeFileItemBase
{

public:
    ImportFileItem(const KDevelop::IncludeItem& include);
    virtual ~ImportFileItem();
    
    virtual void execute(KTextEditor::Document* document, const KTextEditor::Range& word);
    QString moduleName;
    KDevelop::IProject* fromProject;
};

}

#endif // IMPORTFILEITEM_H