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
#include <contextbuilder.h>
#include <duchain.h>
#include <duchainlock.h>
#include <parsesession.h>
#include <topducontext.h>
#include "pythoneditorintegrator.h"
#include <parsingenvironment.h>
#include <ktexteditor/smartrange.h>
#include <ktexteditor/smartinterface.h>
#include <symboltable.h>

using namespace KDevelop;
using namespace python;
using namespace KTextEditor;

ContextBuilder::ContextBuilder(ParseSession* session, const KUrl &url)
    :m_editor(new PythonEditorIntegrator(session))
    ,m_session(session)
    ,m_url(url)
    ,m_compilingContexts(false)
    ,m_recompiling(false)
{
    kDebug() << "=====Building Contexts for===="<<m_url<<endl;

}
ContextBuilder::ContextBuilder (PythonEditorIntegrator* editor, const KUrl &url)
    : m_editor(editor)
    , m_url(url)
    , m_compilingContexts(false)
    , m_recompiling(false)
{
    kDebug() << "=====Building Contexts for===="<<m_url<<endl;
}


ContextBuilder::~ContextBuilder ()
{
}

TopDUContext* ContextBuilder::buildContexts(ast_node* node)
{
    m_compilingContexts = true;
    m_editor->setCurrentUrl(m_url);

    TopDUContext* topLevelContext = 0;
    {
        DUChainWriteLocker lock(DUChain::lock());
        topLevelContext = DUChain::self()->chainForDocument(m_url);
        if (topLevelContext)
        {
            kDebug() << "ContextBuilder::buildContexts: recompiling" << endl;
            m_recompiling = true;
            Q_ASSERT(topLevelContext->textRangePtr());
            if (m_compilingContexts) 
            {
                Q_ASSERT(topLevelContext->textRangePtr());
                if (!topLevelContext->smartRange() && m_editor->smart())
                    topLevelContext->setTextRange(m_editor->topRange(PythonEditorIntegrator::DefinitionUseChain));
            }
        }
        else
        {
            kDebug() << "ContextBuilder::buildContexts: compiling" << endl;
            m_recompiling = false;
            Q_ASSERT(m_compilingContexts);
            Range* range = m_editor->topRange(PythonEditorIntegrator::DefinitionUseChain);
            topLevelContext = new TopDUContext(range);
            topLevelContext->setType(DUContext::Global);
            DUChain::self()->addDocumentChain(IdentifiedFile(m_url,0), topLevelContext);
        }

        setEncountered(topLevelContext);
        m_session->put(node,topLevelContext);
    }
    supportBuild(node);
    {
        DUChainReadLocker lock(DUChain::lock());
        kDebug() << "built top-level context with " << topLevelContext->allDeclarations(KTextEditor::Cursor()).size() << " declarations";
    }
    m_compilingContexts = false;
    return topLevelContext;
}

KDevelop::DUContext* ContextBuilder::buildSubContexts(const KUrl& url, ast_node *node, KDevelop::DUContext* parent) 
{
    m_compilingContexts = true;
    m_recompiling = false;
    m_editor->setCurrentUrl(url);
    m_session->put(node,parent);
    {
        openContext(m_session->get(node));
        m_editor->setCurrentRange(m_editor->topRange(EditorIntegrator::DefinitionUseChain ));
        visit_node (node);
        closeContext();
    }
    m_compilingContexts = false;
    if( m_session->get(node) == parent ) 
    {
        kDebug() << "Error in ContextBuilder::buildSubContexts(...): du-context was not replaced with new one" << endl;
        DUChainWriteLocker lock(DUChain::lock());
        m_session->remove(node);
        m_session->put(node,0);
    }
    return m_session->get(node);
}

void ContextBuilder::supportBuild(ast_node *node, DUContext* context)
{
    openContext( context ? context : m_session->get(node) );
    m_editor->setCurrentUrl(currentContext()->url());
    m_editor->setCurrentRange(currentContext()->textRangePtr());
    visit_node(node);
    closeContext();
    Q_ASSERT(m_contextStack.isEmpty());
}

void ContextBuilder::openContext(DUContext* newContext)
{
    m_contextStack.push(newContext);
    m_nextContextStack.push(0);
}

DUContext* ContextBuilder::openContext(ast_node* rangeNode, DUContext::ContextType type, std::size_t identifier)
{
    if (m_compilingContexts) 
    {
        DUContext* ret = openContextInternal(m_editor->findRange(rangeNode), type, identifier ? identifierForName(identifier) : QualifiedIdentifier());
        m_session->put(rangeNode,ret);
        return ret;
    }
    else
    {
        openContext(m_session->get(rangeNode));
        m_editor->setCurrentRange(currentContext()->textRangePtr());
        return currentContext();
    }
}

DUContext* ContextBuilder::openContext(ast_node* rangeNode, DUContext::ContextType type, const QualifiedIdentifier& identifier)
{
    if (m_compilingContexts) 
    {
        DUContext* ret = openContextInternal(m_editor->findRange(rangeNode), type, identifier);
        m_session->put(rangeNode,ret);
        return ret;
    }
    else 
    {
        openContext(m_session->get(rangeNode));
        m_editor->setCurrentRange(currentContext()->textRangePtr());
        return currentContext();
    }
}

DUContext* ContextBuilder::openContext(ast_node* fromRange, ast_node* toRange, DUContext::ContextType type, std::size_t identifier)
{
    if (m_compilingContexts) 
    {
        DUContext* ret = openContextInternal(m_editor->findRange(fromRange, toRange), type, identifier ? identifierForName(identifier) : QualifiedIdentifier());
        m_session->put(fromRange,ret);
        return ret;
    }
    else 
    {
        openContext(m_session->get(fromRange));
        m_editor->setCurrentRange(currentContext()->textRangePtr());
        return currentContext();
    }
}

DUContext* ContextBuilder::openContextInternal(const Range& range, DUContext::ContextType type, const QualifiedIdentifier& identifier)
{
    Q_ASSERT(m_compilingContexts);
    DUContext* ret = 0L;
    {
        DUChainReadLocker readLock(DUChain::lock());
        if (recompiling())
        {
            const QList<DUContext*>& childContexts = currentContext()->childContexts();
            Range translated = range;
            if (m_editor->smart())
                translated = m_editor->smart()->translateFromRevision(translated);
            for (; nextContextIndex() < childContexts.count(); ++nextContextIndex()) 
            {
                DUContext* child = childContexts.at(nextContextIndex());
                if (child->textRange().start() > translated.end() && child->smartRange())
                break;
                if (child->type() == type && child->localScopeIdentifier() == identifier && child->textRange() == translated) 
                {
                    ret = child;
                    readLock.unlock();
                    DUChainWriteLocker writeLock(DUChain::lock());
                    ret->clearNamespaceAliases();
                    ret->clearImportedParentContexts();
                    m_editor->setCurrentRange(ret->textRangePtr());
                    break;
                }
            }
        }
        if (!ret) 
        {
            readLock.unlock();
            DUChainWriteLocker writeLock(DUChain::lock());
            ret = new DUContext(m_editor->createRange(range), m_contextStack.isEmpty() ? 0 : currentContext());
            ret->setType(type);
            if (!identifier.isEmpty()) 
            {
                ret->setLocalScopeIdentifier(identifier);
                if (type == DUContext::Class || type == DUContext::Namespace)
                SymbolTable::self()->addContext(ret);
            }
        }
    }
    setEncountered(ret);
    openContext(ret);
    return ret;
}

void ContextBuilder::closeContext()
{
    {
        DUChainWriteLocker lock(DUChain::lock());
        currentContext()->cleanIfNotEncountered(m_encountered, m_compilingContexts);
        setEncountered( currentContext() );
    }
    m_contextStack.pop();
    m_nextContextStack.pop();
    m_editor->exitCurrentRange();
}

void ContextBuilder::visit_funcdef(funcdef_ast *node)
{
    if(m_compilingContexts && node->func_name && node->fun_suite)
    {
        QualifiedIdentifier functionName = identifierForName(node->func_name);
        DUChainReadLocker lock(DUChain::lock());
        QList<DUContext*> functionContext = currentContext()->findContexts(DUContext::Function, functionName);

    }
}

ParseSession *ContextBuilder::parseSession() const
{
    return m_session;
}

QualifiedIdentifier ContextBuilder::identifierForName(std::size_t id)
{
    QString name;
    name = m_editor->tokenToString(id);
    m_identifier = Identifier(name);
    m_qidentifier.push(m_identifier);
    return m_qidentifier;
}
