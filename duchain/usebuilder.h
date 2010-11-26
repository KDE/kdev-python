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
#ifndef USEBUILDER_H
#define USEBUILDER_H

#include "contextbuilder.h"
#include "pythonduchainexport.h"

class ParseSession;

typedef ContextBuilder UseBuilderBase;

class KDEVPYTHONDUCHAIN_EXPORT UseBuilder: public UseBuilderBase
{
public:
    UseBuilder(ParseSession* session, const KUrl &url);
    UseBuilder(PythonEditorIntegrator* editor, const KUrl &url);
    ParseSession* parseSession() const;
    void buildUses(ast_node *node);
    virtual void openContext(KDevelop::DUContext* newContext);
    virtual void closeContext();
private:
    ParseSession* m_session;
    void newUse(std::size_t name,ast_node* rangenode);
    inline int& nextUseIndex()
    {
        return m_nextUseStack.top();
    }
    QStack<int> m_nextUseStack;
};

#endif
// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
