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
#include "usebuilder.h"
#include "pythoneditorintegrator.h"

#include <ktexteditor/smartrange.h>
#include <ktexteditor/smartinterface.h>

#include <declaration.h>
#include <use.h>
#include <topducontext.h>
#include <duchain.h>
#include <duchainlock.h>
#include <parsesession.h>

using namespace KTextEditor;
using namespace KDevelop;

UseBuilder::UseBuilder (ParseSession* session, const KUrl &url)
    : UseBuilderBase(session, url)
    , m_session(session)
{
}

UseBuilder::UseBuilder (PythonEditorIntegrator* editor, const KUrl &url)
    : UseBuilderBase(editor,url)
{
}

void UseBuilder::buildUses(ast_node *node)
{
    supportBuild(node);
    if (TopDUContext* top = dynamic_cast<TopDUContext*>(m_session->getNode(node)))
        top->setHasUses(true);
}

void UseBuilder::newUse(std::size_t name, ast_node* rangenode)
{
    //CPP calls it with a NameAst* name, But python doesnt have NameAST* and
    //Long cannot be used to find a Range so, a additional parameter rangenode is being passed.
    Range newRange = m_editor->findRange(rangenode);
    QualifiedIdentifier id = identifierForName(name);

    DUChainWriteLocker lock(DUChain::lock());
    QList<Declaration*> declarations = currentContext()->findDeclarations(id, newRange.start());
    foreach (Declaration* declaration, declarations)
        if (!declaration->isForwardDeclaration())
        {
            declarations.clear();
            declarations.append(declaration);
            break;
        }
    Use* ret = 0;
    if (recompiling())
    {
        const QList<Use*>& uses = currentContext()->uses();
        QMutexLocker smartLock(m_editor->smart() ? m_editor->smart()->smartMutex() : 0);
        Range translated = newRange;
        if (m_editor->smart())
        translated = m_editor->smart()->translateFromRevision(translated);
        for (; nextUseIndex() < uses.count(); ++nextUseIndex())
        {
            Use* use = uses.at(nextUseIndex());
            if (use->textRange().start() > translated.end() && use->smartRange() )
                break;
            if (use->textRange() == translated &&
                ((!use->declaration() && declarations.isEmpty()) ||
                (declarations.count() == 1 && use->declaration() == declarations.first())))
            {
                ret = use;
                break;
            }
        }
    }
    if (!ret)
    {
        Range* prior = m_editor->currentRange();
        Range* use = m_editor->createRange(newRange);
        m_editor->exitCurrentRange();
        Q_ASSERT(m_editor->currentRange() == prior);
        Use* newUse = new Use(use, currentContext());
        setEncountered(newUse);
        if (declarations.count())
            declarations.first()->addUse(newUse);
        else
            currentContext()->addOrphanUse(newUse);
    }
}

void UseBuilder::openContext(DUContext * newContext)
{
  UseBuilderBase::openContext(newContext);
  m_nextUseStack.push(0);
}

void UseBuilder::closeContext()
{
  UseBuilderBase::closeContext();
  m_nextUseStack.pop();
}


ParseSession *UseBuilder::parseSession() const
{
    return m_session;
}
// kate: space-indent on; indent-width 4; tab-width: 4; replace-tabs on; auto-insert-doxygen on
