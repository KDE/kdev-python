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

#include "importfile.h"

#include <KTextEditor/Document>
#include <KTextEditor/View>
#include <language/codecompletion/abstractincludefilecompletionitem.h>

#include "duchain/navigation/navigationwidget.h"

#include <QDebug>
#include "codecompletiondebug.h"

using namespace KDevelop;

namespace Python {
    
ImportFileItem::ImportFileItem(const KDevelop::IncludeItem& include): AbstractIncludeFileCompletionItem< NavigationWidget >(include)
{
    
}

ImportFileItem::~ImportFileItem()
{

}

void ImportFileItem::execute(KTextEditor::View* view, const KTextEditor::Range& word)
{
    qCDebug(KDEV_PYTHON_CODECOMPLETION) << "ImportFileItem executed";
    view->document()->replaceText(word, moduleName);
}


}
