#ifndef PYTHONCODECOMPLETIONWORKER_H
#define PYTHONCODECOMPLETIONWORKER_H

#include "pythoncodecompletionmodel.h"
#include <language/codecompletion/codecompletionworker.h>
#include <language/codecompletion/codecompletionitem.h>
#include "pythoncompletionexport.h"

namespace Python {

class KDEVPYTHONCOMPLETION_EXPORT PythonCodeCompletionWorker : public KDevelop::CodeCompletionWorker
{

public:
    PythonCodeCompletionWorker(PythonCodeCompletionModel *parent);
    virtual KDevelop::CodeCompletionContext* createCompletionContext(KDevelop::DUContextPointer context, const QString& contextText, const QString& followingText, const KDevelop::CursorInRevision& position) const;
};

#endif // PYTHONCODECOMPLETIONWORKER_H

}