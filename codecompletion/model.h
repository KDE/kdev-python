/*
    SPDX-FileCopyrightText: 2011 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef PYTHONCODECOMPLETIONMODEL_H
#define PYTHONCODECOMPLETIONMODEL_H
#include "pythoncompletionexport.h"

#include <language/codecompletion/codecompletionmodel.h>
#include <language/duchain/duchainpointer.h>


namespace Python {

class KDEVPYTHONCOMPLETION_EXPORT PythonCodeCompletionModel : public KDevelop::CodeCompletionModel
{
    Q_OBJECT

public:
    PythonCodeCompletionModel(QObject* parent);
    ~PythonCodeCompletionModel() override;
    
    KDevelop::CodeCompletionWorker* createCompletionWorker() override;
    KTextEditor::Range completionRange(KTextEditor::View* view, const KTextEditor::Cursor &position) override;
    bool shouldStartCompletion(KTextEditor::View* view, const QString& inserted,
                               bool userInsertion, const KTextEditor::Cursor& position) override;
    bool shouldAbortCompletion(KTextEditor::View* view, const KTextEditor::Range& range, const QString& currentCompletion) override;
    QString filterString(KTextEditor::View *view, const KTextEditor::Range &range, const KTextEditor::Cursor &position) override;

    QUrl m_currentDocument;
};

}

#endif // PYTHONCODECOMPLETIONMODEL_H
