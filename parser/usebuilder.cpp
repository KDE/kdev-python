/* Python Parser Test
 *
 * Copyright 2007 Andreas Pakulat <apaku@gmx.de>
 *
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
 */
#include "usebuilder.h"
#include "pythoneditorintegrator.h"

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
    if (TopDUContext* top = dynamic_cast<TopDUContext*>(m_session->get(node)))
        top->setHasUses(true);
}


ParseSession *UseBuilder::parseSession() const
{
    return m_session;
}
