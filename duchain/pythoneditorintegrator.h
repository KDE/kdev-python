/*****************************************************************************
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 * Copyright 2011-2012 Sven Brauch <svenbrauch@googlemail.com>               *
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
#ifndef PYTHONEDITORINTEGRATOR_H
#define PYTHONEDITORINTEGRATOR_H

#include "pythonduchainexport.h"
#include <language/editor/documentrange.h>
#include "parsesession.h"
#include <codehelpers.h>

namespace Python
{

class Ast;

class KDEVPYTHONDUCHAIN_EXPORT PythonEditorIntegrator
{

public:
    PythonEditorIntegrator(ParseSession* session);
    ~PythonEditorIntegrator();
    
    ParseSession* parseSession() const;

    enum Edge {
        FrontEdge,
        BackEdge
    };

    enum RangeEdge {
        InnerEdge,
        OuterEdge
    };

    CursorInRevision findPosition( Python::Ast* node, Python::PythonEditorIntegrator::Edge edge = BackEdge ) const;

    RangeInRevision findRange( Python::Ast* node, Python::PythonEditorIntegrator::RangeEdge edge = OuterEdge) const;
    RangeInRevision findRange( Python::Ast* from, Python::Ast* to) const;
    inline FileIndentInformation* indent() const {
        return m_indentInformationCache;
    }
private:
    ParseSession* m_session;
    FileIndentInformation* m_indentInformationCache;
};

}

#endif
// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
