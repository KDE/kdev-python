/*****************************************************************************
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 *                                                                           *
 * Permission is hereby granted, free of charge, to any person obtaining     *
 * a copy of this software and associated documentation files (the           *
 * "Software"), to deal in the Software without restriction, including       *
 * without limitation the rights to use, copy, modify, merge, publish,       *
 * distribute, sublicense, and/or sell copies of the Software, and to        *
 * permit persons to whom the Software is furnished to do so, subject to     *
 * the following conditions:                                                 *
 *                                                                           *
 * The above copyright notice and this permission notice shall be            *
 * included in all copies or substantial portions of the Software.           *
 *                                                                           *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,           *
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF        *
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND                     *
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE    *
 * LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION    *
 * OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION     *
 * WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.           *
 *****************************************************************************/
#ifndef DECLARATIONBUILDER_H
#define DECLARATIONBUILDER_H

#include <declaration.h>
#include <classfunctiondeclaration.h>
#include "contextbuilder.h"


namespace KDevelop
{
    class Declaration;
}

typedef ContextBuilder DeclarationBuilderBase;

using namespace python;
using namespace KDevelop;

class DeclarationBuilder: public DeclarationBuilderBase
{
public:
    DeclarationBuilder(ParseSession* session, const KUrl &url);
    DeclarationBuilder(PythonEditorIntegrator* editor, const KUrl &url);
    KDevelop::TopDUContext* buildDeclarations(ast_node *node,QList<KDevelop::DUContext*>* includes = 0);
    KDevelop::DUContext* buildSubDeclarations(const KUrl& url, ast_node *node, KDevelop::DUContext* parent = 0);
    virtual void visit_classdef(classdef_ast *node);
    virtual void visit_funcdef(funcdef_ast *node);
    virtual void openContext(KDevelop::DUContext* newContext);
    virtual void closeContext();
private:
    KDevelop::ForwardDeclaration* openForwardDeclaration(std::size_t name, ast_node* range);
    KDevelop::Declaration* openDeclaration(std::size_t name, ast_node* range, bool isFunction = false, bool isForward = false, bool isDefinition = false);
    KDevelop::Declaration* openDefinition(std::size_t name, ast_node* range, bool isFunction = false);
    void closeDeclaration();
    void abortDeclaration();
    inline bool hasCurrentDeclaration() const
    {
        return !m_declarationStack.isEmpty();
    }
    inline KDevelop::Declaration* currentDeclaration() const
    {
        return m_declarationStack.top();
    }
    template<class DeclarationType>
    inline DeclarationType* currentDeclaration() const
    {
        return dynamic_cast<DeclarationType*>(m_declarationStack.top());
    }
    inline KDevelop::Declaration::AccessPolicy currentAccessPolicy()
    {
        return m_accessPolicyStack.top();
    }
    inline void setAccessPolicy(KDevelop::Declaration::AccessPolicy policy)
    {
        m_accessPolicyStack.top() = policy;
    }
    template<class DeclarationType>
    DeclarationType* specialDeclaration( KTextEditor::Range* range );
    template<class DeclarationType>
    DeclarationType* specialDeclaration( KTextEditor::Range* range, int scope );
    inline int& nextDeclaration()
    {
        return m_nextDeclarationStack.top();
    }
    QStack<KDevelop::Declaration*> m_declarationStack;
    QStack<KDevelop::Declaration::AccessPolicy> m_accessPolicyStack;
    QStack<int> m_nextDeclarationStack;
    QStack<std::size_t> m_functionDefinedStack;
    bool m_inTypedef;
};
#endif
