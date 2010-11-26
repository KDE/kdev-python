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
#include "pythoneditorintegrator.h"
#include <ktexteditor/document.h>
#include <ktexteditor/smartrange.h>
#include <ktexteditor/smartinterface.h>

#include <language/editor/documentrange.h>
#include <language/editor/documentrangeobject.h>

#include "ast.h"

using namespace KTextEditor;

namespace Python
{

EditorIntegrator::EditorIntegrator()
{
}

Cursor EditorIntegrator::findPosition( Ast* node , Edge edge ) const
{
    if ( edge == BackEdge )
    {
        // Apparently KTE expects a range to go until _after_ the last character that should be included
        // however the parser calculates endCol as the index _before_ the last included character, so adjust here
        return Cursor( node->endLine, node->endCol+1 );
    }else
    {
        return Cursor( node->startLine, node->startCol );
    }
}

Range EditorIntegrator::findRange( Ast * node, RangeEdge edge )
{
    Q_UNUSED( edge );
    kDebug() << "Finding Range ==================";
    return Range( findPosition( node, FrontEdge ), findPosition( node, BackEdge ) );
}

Range EditorIntegrator::findRange( Ast* from, Ast* to )
{
    return Range( findPosition( from, FrontEdge ), findPosition( to, BackEdge ) );
}

}
