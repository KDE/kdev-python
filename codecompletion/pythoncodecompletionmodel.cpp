/*
 * This file is part of KDevelop
 * Copyright 2010 Sven Brauch <svenbrauch@googlemail.com>
 * Licensed under the GNU GPL
 * */

#include "pythoncodecompletionmodel.h"
#include "pythoncodecompletionworker.h"
#include "ktexteditor/view.h"
#include <KTextEditor/Document>

namespace Python {

PythonCodeCompletionModel::PythonCodeCompletionModel(QObject* parent)
    : CodeCompletionModel(parent)
{

}

PythonCodeCompletionModel::~PythonCodeCompletionModel() { }


KTextEditor::Range PythonCodeCompletionModel::completionRange(KTextEditor::View* view, const KTextEditor::Cursor& position)
{
    m_currentDocument = view->document()->url();
    return KTextEditor::CodeCompletionModelControllerInterface3::completionRange(view, position);
}

KDevelop::CodeCompletionWorker* PythonCodeCompletionModel::createCompletionWorker()
{
    PythonCodeCompletionWorker* w = new PythonCodeCompletionWorker(this);
    w->m_workingOnDocument = m_currentDocument;
    return w;
}

}