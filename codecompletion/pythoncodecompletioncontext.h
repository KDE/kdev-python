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

#ifndef PYTHONCODECOMPLETIONCONTEXT_H
#define PYTHONCODECOMPLETIONCONTEXT_H

#include <language/codecompletion/codecompletioncontext.h>
#include <language/duchain/duchainpointer.h>
#include <qstack.h>

#include "importfileitem.h"
#include "pythoncodecompletionworker.h"
#include "pythoncompletionexport.h"

using namespace KDevelop;

namespace KDevelop {
    class IProject;
    class ProjectFolderItem;
}

namespace Python {
    
typedef QPair<Declaration*, int> DeclarationDepthPair;

class KDEVPYTHONCOMPLETION_EXPORT PythonCodeCompletionContext : public KDevelop::CodeCompletionContext
{
public:
    enum CompletionContextType {
        ImportFileCompletion,
        MemberAccessCompletion,
        DefaultCompletion,
        ImportSubCompletion,
        NoCompletion,
        NewStatementCompletion,
        DefineCompletion
    };
    
    PythonCodeCompletionContext(DUContextPointer context, const QString& text, const KDevelop::CursorInRevision& position, int depth, const PythonCodeCompletionWorker* parent);
    virtual QList< KDevelop::CompletionTreeItemPointer > completionItems(bool& abort, bool fullCompletion = true);
    QList<ImportFileItem*> includeFileItems(QList<KUrl> searchPaths);
    QList<ImportFileItem*> includeFileItemsForSubmodule(QString submodule);
    QList<CompletionTreeItemPointer> getCompletionItemsForType(AbstractType::Ptr type, DeclarationPointer declaration);
    QList<CompletionTreeItemPointer> declarationListToItemList(QList<DeclarationDepthPair> declarations, int maxDepth = 0);
    
    CompletionContextType m_operation;
    QStack<ProjectFolderItem*> m_folderStack;
    int m_maxFolderScanDepth;
    QStringList m_searchingForModule;
    QString m_subForModule;
    const PythonCodeCompletionWorker* parent;
    KUrl m_workingOnDocument;
    QString m_guessTypeOfExpression;
    QString m_indent;
    
    DUContextPointer m_context;
    
private:
    bool m_dontAddMe;
};

}

#endif // PYTHONCODECOMPLETIONCONTEXT_H
