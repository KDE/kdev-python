/*****************************************************************************
 * Copyright (c) 2010-2011 Sven Brauch <svenbrauch@googlemail.com>           *
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

#include "pythoncodecompletionworker.h"
#include "pythoncodecompletionmodel.h"
#include "pythoncodecompletioncontext.h"
#include <language/duchain/declaration.h>
#include <KLocalizedString>


namespace Python {

PythonCodeCompletionWorker::PythonCodeCompletionWorker(PythonCodeCompletionModel *parent, KUrl /*document*/)
    : KDevelop::CodeCompletionWorker(parent), parent(parent)
{

}

KDevelop::CodeCompletionContext* PythonCodeCompletionWorker::createCompletionContext(KDevelop::DUContextPointer context, const QString& contextText, const QString& /*followingText*/, const KDevelop::CursorInRevision& position) const
{
    PythonCodeCompletionContext* completionContext = new PythonCodeCompletionContext(context, contextText, position, 0, this);
    return completionContext;
}

QList< KSharedPtr< CompletionTreeElement > > PythonCodeCompletionWorker::computeGroups(QList< CompletionTreeItemPointer > items, KSharedPtr< CodeCompletionContext > completionContext)
{
    QList< KSharedPtr<CompletionTreeElement> > tree;
    CompletionCustomGroupNode* localDeclarations = new CompletionCustomGroupNode(i18n("Local declarations"));
    CompletionCustomGroupNode* globalDeclarations = new CompletionCustomGroupNode(i18n("Global or imported declarations"));
    CompletionCustomGroupNode* stuff = new CompletionCustomGroupNode(i18n("Other suggestions"));
    
    int currentIndex = 0;
    foreach (CompletionTreeItemPointer currentItem, items) {
        KSharedPtr<CompletionTreeElement> currentElement(dynamic_cast<CompletionTreeElement*>(currentItem.data()));
        Declaration* currentDeclaration = currentItem->declaration().data();
        if ( currentDeclaration ) {
            if ( items.lastIndexOf(currentItem) != currentIndex )
                continue;
            if ( currentDeclaration->context() == completionContext.data()->duContext() ) {
                localDeclarations->appendChild(currentElement);
            }
            else {
                globalDeclarations->appendChild(currentElement);
            }
        }
        else {
            stuff->appendChild(currentElement);
        }
        currentIndex += 1;
    }
    
    if ( localDeclarations->children.length() )
        tree << KSharedPtr<CompletionTreeElement>(static_cast<CompletionTreeElement*>(localDeclarations));
    if ( globalDeclarations->children.length() )
        tree << KSharedPtr<CompletionTreeElement>(static_cast<CompletionTreeElement*>(globalDeclarations));
    if ( stuff->children.length() )
        tree << KSharedPtr<CompletionTreeElement>(static_cast<CompletionTreeElement*>(stuff));
    return tree;
}


}