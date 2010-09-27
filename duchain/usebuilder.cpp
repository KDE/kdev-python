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

#include <language/duchain/declaration.h>
#include <language/duchain/use.h>
#include <language/duchain/topducontext.h>
#include <language/duchain/duchain.h>
#include <language/duchain/duchainlock.h>
#include <parsesession.h>
#include <usebuilder.h>

using namespace KTextEditor;
using namespace KDevelop;

namespace Python {

UseBuilder::UseBuilder (PythonEditorIntegrator* editor)
{
}

void UseBuilder::buildUses(Ast *node)
{
    supportBuild(node);
//     if (TopDUContext* top = dynamic_cast<TopDUContext*>(m_session->getNode(node)))
//         top->setHasUses(true);
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

}
// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
