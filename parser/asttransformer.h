#pragma once
#include "kdevpythonversion.h"
#include "python_grammar.h"

namespace Python
{

class PyObjectRef {
public:
    PyObjectRef(PyObject* py_obj): obj(py_obj) {}
    operator PyObject*() const {
        return obj;
    }
    ~PyObjectRef() {
        Py_XDECREF(obj);
        obj = nullptr;
    }
    PyObject* obj = nullptr;
};


class AstTransformer {
public:
    CodeAst* ast;
    Grammar grammar;

    AstTransformer() {}

    void run(PyObject *syntaxtree, QString moduleName) {
        ast = static_cast<CodeAst*>(visitModuleNode(syntaxtree, nullptr));
        ast->name = new Identifier(moduleName);
    }
    // Shift lines by some fixed amount
    inline int tline(int line) {
        if ( line == -99999 ) {
            // don't touch the marker
            return -99999;
        }
        return line - 1;
    };

    template <class T>
    T getattr(PyObject *obj, const char *attr) const {
        return getattr<T>(obj, attr);
    }

public:
    Ast* visitNode(PyObject* node, Ast* parent);
    template<typename K> QList<K*> visitNodeList(PyObject* node, Ast* parent);
    Ast* visitModuleNode(PyObject* node, Ast* parent);
    Ast* visitStmtNode(PyObject* node, Ast* parent);
    Ast* visitExprNode(PyObject* node, Ast* parent);
    Ast* visitComprehensionNode(PyObject* node, Ast* parent);
    Ast* visitExceptHandlerNode(PyObject* node, Ast* parent);
    Ast* visitArgumentsNode(PyObject* node, Ast* parent);
    Ast* visitArgNode(PyObject* node, Ast* parent);
    Ast* visitKeywordNode(PyObject* node, Ast* parent);
    Ast* visitAliasNode(PyObject* node, Ast* parent);
    Ast* visitWithItemNode(PyObject* node, Ast* parent);
    Ast* visitSliceNode(PyObject* node, Ast* parent);

};

} // namespace Python

