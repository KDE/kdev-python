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
#ifndef CONTEXTBUILDER_H
#define CONTEXTBUILDER_H

#include "python_default_visitor.h"

#include <QSet>
#include <QHash>
#include <identifier.h>
#include <ducontext.h>
#include <ksharedptr.h>

namespace KDevelop
{
    class DUChain;
    class KDevelop::DUChainBase;
    class DUContext;
    class TopDUContext;
}

class PythonEditorIntegrator;
class ParseSession;

namespace Python 
{
    class LexedFile;
    typedef KSharedPtr<LexedFile> LexedFilePointer;
}

using namespace python;

class ContextBuilder: public python::default_visitor
{

public:
    ContextBuilder(ParseSession* session, const KUrl &url);
    ContextBuilder(PythonEditorIntegrator* editor, const KUrl &url);
    virtual ~ContextBuilder ();

    ParseSession* parseSession() const;

    KDevelop::TopDUContext* buildContexts(ast_node* node);
    KDevelop::DUContext* buildSubContexts(const KUrl& url, ast_node *node, KDevelop::DUContext* parent = 0);
    void supportBuild(ast_node *node, KDevelop::DUContext* context = 0);
protected:
    inline KDevelop::DUContext* currentContext() { return m_contextStack.top(); }

    void setEncountered( KDevelop::DUChainBase* item )
    {
        m_encountered.insert(item);
    }

    bool wasEncountered( KDevelop::DUChainBase* item )
    {
        return m_encountered.contains(item);
    }


    virtual void openContext(KDevelop::DUContext* newContext);
    virtual void closeContext();
    PythonEditorIntegrator* m_editor;
    inline bool recompiling() const { return m_recompiling; }

    QSet<KDevelop::DUChainBase*> m_encountered;
    QStack<KDevelop::DUContext*> m_contextStack;
    int m_nextContextIndex;

    KDevelop::QualifiedIdentifier identifierForName(std::size_t id);

    KDevelop::DUContext* openContext(ast_node* range, KDevelop::DUContext::ContextType type, const KDevelop::QualifiedIdentifier& identifier);
    KDevelop::DUContext* openContext(ast_node* range, KDevelop::DUContext::ContextType type, std::size_t identifier = 0);
    KDevelop::DUContext* openContext(ast_node* fromRange, ast_node* toRange, KDevelop::DUContext::ContextType type, std::size_t identifier = 0);
    KDevelop::DUContext* openContextInternal(const KTextEditor::Range& range, KDevelop::DUContext::ContextType type, const KDevelop::QualifiedIdentifier& identifier);

    virtual void visit_funcdef(funcdef_ast *node);
    //virtual void visit_name(name_ast *node);
    virtual void visit_classdef(classdef_ast *node);
    /*virtual void visit_for_stmt(for_stmt_ast *node);
    virtual void visit_while_stmt(while_stmt_ast *node);*/

private:
    ParseSession* m_session;
    KUrl m_url;
    bool m_compilingContexts: 1;
    bool m_recompiling : 1;

    QStack<int> m_nextContextStack;
    inline int& nextContextIndex() { return m_nextContextStack.top(); }
    KDevelop::Identifier m_identifier;
    KDevelop::QualifiedIdentifier m_qidentifier;
    QList<KDevelop::DUContext*> m_importedParentContexts;

};


#endif
