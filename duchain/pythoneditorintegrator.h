/*****************************************************************************
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 * Copyright 2011-2012 Sven Brauch <svenbrauch@googlemail.com>               *
 *                                                                           *
 * This program is free software; you can redistribute it and/or             *
 * modify it under the terms of the GNU General Public License as            *
 * published by the Free Software Foundation; either version 2 of            *
 * the License, or (at your option) any later version.                       *
 *                                                                           *
 * This program is distributed in the hope that it will be useful,           *
 * but WITHOUT ANY WARRANTY; without even the implied warranty of            *
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             *
 * GNU General Public License for more details.                              *
 *                                                                           *
 * You should have received a copy of the GNU General Public License         *
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.     *
 *****************************************************************************
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
