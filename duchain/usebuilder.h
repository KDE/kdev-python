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
#ifndef USEBUILDER_H
#define USEBUILDER_H

#include "contextbuilder.h"
#include "pythonduchainexport.h"
#include "pythoneditorintegrator.h"
#include "ast.h"

#include <language/duchain/builders/abstractusebuilder.h>

namespace Python {

class ParseSession;

typedef KDevelop::AbstractUseBuilder<Ast, Identifier, ContextBuilder> UseBuilderBase;

class KDEVPYTHONDUCHAIN_EXPORT UseBuilder: public UseBuilderBase
{
public:
    UseBuilder(PythonEditorIntegrator *editor);
    ParseSession* parseSession() const;

protected:
    virtual void visitName(NameAst* node);
    virtual void visitAttribute(AttributeAst* node);
private:
    ParseSession* m_session;
    PythonEditorIntegrator* m_editor;
    inline int& nextUseIndex()
    {
        return m_nextUseStack.top();
    }
    QStack<int> m_nextUseStack;
};

}

#endif
// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
