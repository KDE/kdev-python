#include "pythoncodecompletionworker.h"
#include "pythoncodecompletionmodel.h"

PythonCodeCompletionWorker::PythonCodeCompletionWorker(PythonCodeCompletionModel *parent)
    : KDevelop::CodeCompletionWorker(parent)
{

}

KDevelop::CodeCompletionContext* PythonCodeCompletionWorker::createCompletionContext(KDevelop::DUContextPointer context, const QString& contextText, const QString& followingText, const KDevelop::CursorInRevision& position) const
{
    return KDevelop::CodeCompletionWorker::createCompletionContext(context, contextText, followingText, position);
}
