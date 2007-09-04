#include "typebuilder.h"
#include "pythoneditorintegrator.h"
#include "parsesession.h"
#include <ducontext.h>
#include <duchain.h>

using namespace KDevelop;
TypeBuilder::TypeBuilder(ParseSession* session, const KUrl &url)
  : TypeBuilderBase(session, url)
{
}

TypeBuilder::TypeBuilder(PythonEditorIntegrator * editor, const KUrl &url)
  : TypeBuilderBase(editor,url)
{
}

void TypeBuilder::supportBuild(ast_node *node, DUContext* context)
{
    TypeBuilderBase::supportBuild(node, context);
    Q_ASSERT(m_typeStack.isEmpty());
}
