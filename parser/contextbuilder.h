/*****************************************************************************
 * Copyright (c) 2007 Piyush verma < piyush.verma@gmail.com>                 *
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

namespace Python {
    class LexedFile;
    typedef KSharedPtr<LexedFile> LexedFilePointer;
}

using namespace python;

class ContextBuilder: public python::default_visitor
{

public:
    ContextBuilder(ParseSession* session);
    ParseSession* parseSession() const;
    virtual ~ContextBuilder ();

    KDevelop::TopDUContext* buildContexts();

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

//     virtual void openContext(KDevelop::DUContext* newContext);
// 
//     virtual void closeContext();

    QSet<KDevelop::DUChainBase*> m_encountered;
    QStack<KDevelop::DUContext*> m_contextStack;
    int m_nextContextIndex;

    QStack<int> m_nextContextStack;
    inline int& nextContextIndex() { return m_nextContextStack.top(); }
private:
    ParseSession* m_session;
};

#endif
