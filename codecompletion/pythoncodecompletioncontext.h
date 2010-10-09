#ifndef PYTHONCODECOMPLETIONCONTEXT_H
#define PYTHONCODECOMPLETIONCONTEXT_H

#include <language/codecompletion/codecompletioncontext.h>


class PythonCodeCompletionContext : public KDevelop::CodeCompletionContext
{

public:
    virtual QList< KDevelop::CompletionTreeItemPointer > completionItems(bool& abort, bool fullCompletion = true);
};

#endif // PYTHONCODECOMPLETIONCONTEXT_H
