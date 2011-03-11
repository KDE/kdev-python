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
    PythonCodeCompletionWorker(PythonCodeCompletionModel *parent, KUrl document);
    virtual KDevelop::CodeCompletionContext* createCompletionContext(KDevelop::DUContextPointer context, const QString& contextText, const QString& followingText, const KDevelop::CursorInRevision& position) const;
    PythonCodeCompletionModel* parent;
};

}

#endif // PYTHONCODECOMPLETIONWORKER_H