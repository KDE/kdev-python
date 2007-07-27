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

            if (m_compilingContexts) {
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
            //DUChain::self()->addDocumentChain(IdentifiedFile(m_url,0), topLevelContext);
        }

        setEncountered(topLevelContext);
        m_session->put(node,topLevelContext);
    }
}

ParseSession *ContextBuilder::parseSession() const
{
    return m_session;
}