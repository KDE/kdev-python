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
#ifndef TYPEBUILDER_H
#define TYPEBUILDER_H

#include "contextbuilder.h"
#include <typesystem.h>
#include <declaration.h>
#include "pythonduchainexport.h"

class ClassType;
class FunctionType;

typedef ContextBuilder TypeBuilderBase;

class KDEVPYTHONDUCHAIN_EXPORT TypeBuilder: public TypeBuilderBase
{
public:
    TypeBuilder(ParseSession* session, const KUrl &url);
    TypeBuilder(PythonEditorIntegrator* editor, const KUrl &url);
    virtual void supportBuild(ast_node *node, KDevelop::DUContext* context = 0);
    const QList< KDevelop::AbstractType::Ptr >& topTypes() const;
    KDevelop::DUContext* searchContext() ;
    KDevelop::AbstractType::Ptr lastType() const;
    void setLastType(KDevelop::AbstractType::Ptr ptr);
private:
    QStack<KDevelop::AbstractType::Ptr> m_typeStack;
};

#endif
