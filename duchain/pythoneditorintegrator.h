/*
    SPDX-FileCopyrightText: 2007 Piyush verma <piyush.verma@gmail.com>
    SPDX-FileCopyrightText: 2011-2012 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

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

    CursorInRevision findPosition( const Python::Ast* node, Python::PythonEditorIntegrator::Edge edge = BackEdge ) const;

    RangeInRevision findRange(const Python::Ast* node, Python::PythonEditorIntegrator::RangeEdge edge = OuterEdge) const;
    RangeInRevision findRange(const Python::Ast* from, const Python::Ast* to) const;
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
