/*
    SPDX-FileCopyrightText: 2010-2014 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#include "model.h"

#include <KTextEditor/View>
#include <KTextEditor/Document>
#include <KTextEditor/CodeCompletionModelControllerInterface>

#include <QDebug>
#include "codecompletiondebug.h"

#include "context.h"
#include "worker.h"

namespace Python {

PythonCodeCompletionModel::PythonCodeCompletionModel(QObject* parent)
    : CodeCompletionModel(parent)
{
    // This avoids flickering of the completion-list when full code-completion mode is used
    setForceWaitForModel(true);
}

PythonCodeCompletionModel::~PythonCodeCompletionModel() { }

bool PythonCodeCompletionModel::shouldStartCompletion(KTextEditor::View* view, const QString& inserted,
                                                bool userInsertion, const KTextEditor::Cursor& position)
{
    QList<QString> words;
    words << "for" << "raise" << "except" << "in";
    for ( const QString& word : words ) {
        if ( view->document()->line(position.line()).mid(0, position.column()).endsWith(word + " ") ) {
            return true;
        }
    }
    // shebang / encoding lines
    if ( view->document()->line(position.line()).mid(0, position.column()).endsWith("#") && 
         position.line() < 2 )
    {
        return true;
    }

    // we're probably dealing with string formatting completion
    // is there any other case where this condition is true?
    if ( ! userInsertion && inserted.startsWith('{') ) {
        return true;
    }

    return KDevelop::CodeCompletionModel::shouldStartCompletion(view, inserted, userInsertion, position);
}

bool PythonCodeCompletionModel::shouldAbortCompletion(KTextEditor::View* view, const KTextEditor::Range& range, const QString& currentCompletion)
{
    const QString text = view->document()->text(range);
    if ( completionContext() ) {
        auto context = static_cast<PythonCodeCompletionContext*>(completionContext().data());
        if ( context->completionContextType() == PythonCodeCompletionContext::StringFormattingCompletion ) {
            if ( text.endsWith('"') || text.endsWith("'") || text.endsWith(' ') ) {
                return true;
            }
        }
    }
    return KTextEditor::CodeCompletionModelControllerInterface::shouldAbortCompletion(view, range, currentCompletion);
}

QString PythonCodeCompletionModel::filterString(KTextEditor::View *view, const KTextEditor::Range &range, const KTextEditor::Cursor &position)
{
    // TODO The completion context may be null, so we need to check it first. This might a bug.
    if ( completionContext() ) {
        auto context = static_cast<PythonCodeCompletionContext*>(completionContext().data());
        if (context->completionContextType() == PythonCodeCompletionContext::StringFormattingCompletion) {
           return QString();
        }
    }
    return CodeCompletionModel::filterString(view, range, position);
}

KTextEditor::Range PythonCodeCompletionModel::completionRange(KTextEditor::View* view, const KTextEditor::Cursor& position)
{
    m_currentDocument = view->document()->url();
    return KTextEditor::CodeCompletionModelControllerInterface::completionRange(view, position);
}

KDevelop::CodeCompletionWorker* PythonCodeCompletionModel::createCompletionWorker()
{
    return new PythonCodeCompletionWorker(this, m_currentDocument);
}

}

#include "moc_model.cpp"
