/*
    SPDX-FileCopyrightText: 2010-2012 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef PYTHONCODECOMPLETIONWORKER_H
#define PYTHONCODECOMPLETIONWORKER_H

#include "model.h"
#include <language/codecompletion/codecompletionworker.h>
#include <language/codecompletion/codecompletionitem.h>
#include "pythoncompletionexport.h"

namespace Python {

class KDEVPYTHONCOMPLETION_EXPORT PythonCodeCompletionWorker : public KDevelop::CodeCompletionWorker
{
    Q_OBJECT

public:
    PythonCodeCompletionWorker(PythonCodeCompletionModel *parent, const QUrl& document);
    KDevelop::CodeCompletionContext* createCompletionContext(const KDevelop::DUContextPointer& context, const QString& contextText, const QString& followingText, const KDevelop::CursorInRevision& position) const override;
    void updateContextRange(KTextEditor::Range &contextRange, KTextEditor::View *view, const KDevelop::DUContextPointer& context) const override;
    PythonCodeCompletionModel* parent;
};

}

#endif // PYTHONCODECOMPLETIONWORKER_H
