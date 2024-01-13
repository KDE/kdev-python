/*
    SPDX-FileCopyrightText: 2011-2012 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef PYCOMPLETIONTEST_H
#define PYCOMPLETIONTEST_H

#include <QObject>

#include <language/editor/cursorinrevision.h>
#include <language/codecompletion/codecompletioncontext.h>

#include "codecompletion/model.h"

using namespace KDevelop;

namespace Python {

struct CompletionParameters {
    DUContextPointer contextAtCursor;
    QString snip;
    QString remaining;
    CursorInRevision cursorAt;
};

class PyCompletionTest : public QObject
{
    Q_OBJECT
    public:
        explicit PyCompletionTest(QObject* parent = nullptr);
        void initShell();
        
        const QList<CompletionTreeItem*> invokeCompletionOn(const QString& initCode, const QString& invokeCode);
        const CompletionParameters prepareCompletion(const QString& initCode, const QString& invokeCode);
        const QList<CompletionTreeItem*> runCompletion(const CompletionParameters data);

        bool containsItemForDeclarationNamed(const QList< CompletionTreeItem* > items, QString itemName);
        // convenience function
        bool declarationInCompletionList(const QString& initCode, const QString& invokeCode, QString itemName);
        // convenience function
        bool completionListIsEmpty(const QString& initCode, const QString& invokeCode);
        // convenience function
        bool containsItemStartingWith(const QList< CompletionTreeItem* > items, const QString& itemName);
        // convenience function
        bool itemInCompletionList(const QString& initCode, const QString& invokeCode, QString itemName);
        
    private Q_SLOTS:
        void testIntegralTypesImmediate();
        void testIntegralTypesImmediate_data();
        void testIntegralExpressionsDifferentContexts();
        void testIntegralExpressionsDifferentContexts_data();
        void testNoCompletionInCommentsOrStrings();
        void testNoCompletionInCommentsOrStrings_data();
        void testImplementMethodCompletion();
        void testImplementMethodCompletion_data();
        void testExceptionCompletion();
        void testGeneratorCompletion();
        void testInheritanceCompletion();
        void testImportCompletion();
        void testImportCompletion_data();
        void testNoImplicitMagicFunctions();
        void testExpressionParser();
        void testExpressionParser_data();
        void testExpressionParserMisc();
        void testCompletionAfterQuotes();
        void testCompletionAfterQuotes_data();
        void testIgnoreCommentSignsInStringLiterals();
        void testIdentifierMatching();
        void testAutoBrackets();
        void testAddImportCompletion();
        void testAddImportCompletion_data();
        void testFunctionDeclarationCompletion();
        void testFunctionDeclarationCompletion_data();
        void testCompletionScopes();
        void testCompletionScopes_data();
        void testStringFormattingCompletion();
        void testStringFormattingCompletion_data();
        void testStringFormatter();
        void testStringFormatter_data();
        // benchmarks
        void completionBenchTest();
        void completionBenchTest_data();
    private:
        QList<CompletionTreeItemPointer> m_ptrs;

};

}
#endif
