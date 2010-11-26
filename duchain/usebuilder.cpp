/*****************************************************************************
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 *                                                                           *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
 * 02110-1301, USA.
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
// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
