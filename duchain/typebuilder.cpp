/*****************************************************************************
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 * Copyright (c) 2012 Sven Brauch <svenbrauch@gmail.com>                     *
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
#include "typebuilder.h"
#include "pythoneditorintegrator.h"
#include "parsesession.h"
#include <ducontext.h>
#include <duchain.h>

using namespace KDevelop;
TypeBuilder::TypeBuilder(ParseSession* session, const QUrl& url)
  : TypeBuilderBase(session, url)
{
}

TypeBuilder::TypeBuilder(PythonEditorIntegrator * editor, const QUrl& url)
  : TypeBuilderBase(editor, url)
{
}

void TypeBuilder::supportBuild(ast_node *node, DUContext* context)
{
    TypeBuilderBase::supportBuild(node, context);
}
