/*****************************************************************************
 * Copyright (c) 2011-2013 Sven Brauch <svenbrauch@googlemail.com>           *
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
#include <kdev-pg-memory-pool.h>
#include <QStack>

#include <QObject>

#include "items/importfile.h"
#include "worker.h"
#include "pythoncompletionexport.h"
#include "helpers.h"
#include "types/unsuretype.h"

using namespace KDevelop;

namespace KDevelop {
    class IProject;
    class ProjectFolderItem;
}

namespace Python {
    
typedef QPair<Declaration*, int> DeclarationDepthPair;

/**
 * @brief Represents a single pair of directory and remaining identifiers, for include completion.
 * 
 * In the directory, the functions in PythonCodeCompletionContext try to resolve the remaining
 * identifiers. If the identifier list is empty, the __init__.py file will be read.
 **/
class IncludeSearchTarget {
public:
    IncludeSearchTarget(KUrl d_, QStringList r_) : directory(d_), remainingIdentifiers(r_) {
        directory.cleanPath();
    };
    KUrl directory;
    QStringList remainingIdentifiers;
};

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
        DefineCompletion,
        ShebangLineCompletion,
        FunctionCallCompletion,
        InheritanceCompletion,
        RaiseExceptionCompletion,
        GeneratorVariableCompletion,
        StringFormattingCompletion
    };
    
    enum ItemTypeHint {
        NoHint,
        IterableRequested
    };
    
    PythonCodeCompletionContext(DUContextPointer context, const QString& text, const QString& followingText,
                                const KDevelop::CursorInRevision& position,
                                int depth, const PythonCodeCompletionWorker* parent);

    CompletionContextType completionContextType();

    ItemTypeHint itemTypeHint();

    /**
     * @brief The "interface method" which returns all the completion items to kdevelop.
     **/
    virtual QList< KDevelop::CompletionTreeItemPointer > completionItems(bool& abort, bool fullCompletion = true);

    virtual QList< CompletionTreeElementPointer > ungroupedElements();
    
    /**
     * @brief Get all possible items matching the specified dot-seperated search string.
     **/
    QList<CompletionTreeItemPointer> includeItemsForSubmodule(QString submodule);
    
    /**
     * @brief Get all include items for the given target list.
     **/
    QList< CompletionTreeItemPointer > findIncludeItems(IncludeSearchTarget);
    /**
     * @brief Get all include items for the given single target.
     **/
    QList< CompletionTreeItemPointer > findIncludeItems(QList< Python::IncludeSearchTarget > items);
    
    /**
     * @brief Get all contexts to list declarations from for the given item.
     **/
    DUContext* internalContextForDeclaration(TopDUContext* topContext, QStringList remainingIdentifiers);
    
    /**
     * @brief Get all items that are attributes of the given type. @param type might be any type.
     **/
    QList<CompletionTreeItemPointer> getCompletionItemsForType(AbstractType::Ptr type);
    /**
     * @brief Get all items that are attributes of the given type. @param type must be non-unsure.
     **/
    QList<CompletionTreeItemPointer> getCompletionItemsForOneType(AbstractType::Ptr type);
    
    /**
     * @brief Convert the given list of declarations to a list of include-items.
     * Convenience function.
     **/
    QList<CompletionTreeItemPointer> declarationListToItemList(QList<DeclarationDepthPair> declarations, int maxDepth = 0);
    QList<CompletionTreeItemPointer> declarationListToItemList(QList<Declaration*> declarations);
    
private:
    /// This constructor is only used for recursive calltips
    PythonCodeCompletionContext(DUContextPointer context, const QString& remainingText,
                                QString calledFunction, int depth, int alreadyGivenParameters, CodeCompletionContext* child);
    void summonParentForEventualCall(TokenList tokens, const QString& text);
    /// Get possible "add import..." items for an expression.
    QList< CompletionTreeItemPointer > getMissingIncludeItems(QString forString);
    void eventuallyAddGroup(QString name, int priority, QList<CompletionTreeItemPointer> items);

private:
    /// Item generating functions
    using ItemList = QList<CompletionTreeItemPointer>;
    ItemList shebangItems();
    ItemList generatorItems();
    ItemList functionCallItems();
    ItemList defineItems();
    ItemList raiseItems();
    ItemList importFileItems();
    ItemList inheritanceItems();
    ItemList memberAccessItems();
    ItemList stringFormattingItems();
    ItemList keywordItems();
    ItemList classMemberInitItems();

private:
    CompletionContextType m_operation;
    ItemTypeHint m_itemTypeHint;
    QStack<ProjectFolderItem*> m_folderStack;
    int m_maxFolderScanDepth;
    QStringList m_searchingForModule;
    QString m_searchImportItemsInModule;
    KUrl m_workingOnDocument;
    
    CodeCompletionContext* m_child;
    
    QString m_guessTypeOfExpression;
    QString m_followingText;
    
    QString m_indent;
    KDevelop::CursorInRevision m_position;
    
    QString m_calledFunction;
    int m_alreadyGivenParametersCount;

    QString m_matchAgainst;

    bool m_fullCompletion;

    QList<CompletionTreeElementPointer> m_storedGroups;
};

}

#endif // PYTHONCODECOMPLETIONCONTEXT_H
