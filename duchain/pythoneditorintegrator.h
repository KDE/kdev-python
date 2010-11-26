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
#ifndef PYTHONEDITORINTEGRATOR_H
#define PYTHONEDITORINTEGRATOR_H

#include <language/editor/editorintegrator.h>
#include "pythonduchainexport.h"

namespace Python
{

class Ast;

class KDEVPYTHONDUCHAIN_EXPORT EditorIntegrator : public KDevelop::EditorIntegrator
{

public:
    EditorIntegrator();

    KTextEditor::Cursor findPosition( Ast* node, Edge edge = BackEdge ) const;

    using KDevelop::EditorIntegrator::createRange;
    KTextEditor::Range findRange( Ast* node, RangeEdge = OuterEdge );
    KTextEditor::Range findRange( Ast* from, Python::Ast* to );

private:
};

}

#endif
// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
