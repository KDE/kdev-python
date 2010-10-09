#include "pythoncodecompletionmodel.h"
#include "pythoncodecompletionworker.h"
#include "ktexteditor/view.h"

namespace Python {

PythonCodeCompletionModel::PythonCodeCompletionModel(QObject* parent)
    : CodeCompletionModel(parent)
{

}

PythonCodeCompletionModel::~PythonCodeCompletionModel() { }


KTextEditor::Range PythonCodeCompletionModel::completionRange(KTextEditor::View* view, const KTextEditor::Cursor& position)
{
    return KTextEditor::CodeCompletionModelControllerInterface3::completionRange(view, position);
}

KDevelop::CodeCompletionWorker* PythonCodeCompletionModel::createCompletionWorker()
{
    return new PythonCodeCompletionWorker(this);
}

}