#ifndef DUMPCHAIN_H
#define DUMPCHAIN_H

#include "python_default_visitor.h"

class ParseSession;
class PythonEditorIntegrator;

namespace KDevelop
{
    class DUContext;
}

using namespace python;

class DumpChain: public default_visitor
{
public:
    DumpChain();
    virtual ~DumpChain();
    void dump(ast_node *node, ParseSession* session = 0);
    void dump(KDevelop::DUContext* context, bool imported = false);
    virtual void visit_node(ast_node *node);
    ParseSession* parseSession() const;

private:
    ParseSession* m_session;
    PythonEditorIntegrator* m_editor;
};

#endif
