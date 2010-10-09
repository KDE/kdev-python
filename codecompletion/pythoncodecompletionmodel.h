#ifndef PYTHONCODECOMPLETIONMODEL_H
#define PYTHONCODECOMPLETIONMODEL_H

#include <language/codecompletion/codecompletionmodel.h>
#include <language/duchain/duchainpointer.h>
#include "pythoncompletionexport.h"

class KDEVPYTHONCOMPLETION_EXPORT PythonCodeCompletionModel : public KDevelop::CodeCompletionModel
{

public:
    PythonCodeCompletionModel(QObject* parent);
    virtual ~PythonCodeCompletionModel();
    
    virtual KDevelop::CodeCompletionWorker* createCompletionWorker();
    KTextEditor::Range completionRange(KTextEditor::View* view, const KTextEditor::Cursor &position); 
};

#endif // PYTHONCODECOMPLETIONMODEL_H
