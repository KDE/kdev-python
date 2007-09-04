#ifndef TYPEBUILDER_H
#define TYPEBUILDER_H

#include "contextbuilder.h"
#include <typesystem.h>
#include <declaration.h>
#include "pythonduchainbuilderexport.h"

class ClassType;
class FunctionType;

typedef ContextBuilder TypeBuilderBase;

class KDEVPYTHONDUCHAINBUILDER_EXPORT TypeBuilder: public TypeBuilderBase
{
public:
    TypeBuilder(ParseSession* session, const KUrl &url);
    TypeBuilder(PythonEditorIntegrator* editor, const KUrl &url);
    virtual void supportBuild(ast_node *node, KDevelop::DUContext* context = 0);
    const QList< KDevelop::AbstractType::Ptr >& topTypes() const;
    KDevelop::DUContext* searchContext() ;
    KDevelop::AbstractType::Ptr lastType() const;
    void setLastType(KDevelop::AbstractType::Ptr ptr);
private:
    QStack<KDevelop::AbstractType::Ptr> m_typeStack;
};

#endif
