/*****************************************************************************
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 * Copyright 2010-2013 Sven Brauch <svenbrauch@googlemail.com>               *
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
#ifndef USEBUILDER_H
#define USEBUILDER_H

#include "contextbuilder.h"
#include "pythonduchainexport.h"
#include "pythoneditorintegrator.h"
#include "ast.h"

#include <language/duchain/builders/abstractusebuilder.h>

#include <QStack>

namespace Python {

class ParseSession;

typedef KDevelop::AbstractUseBuilder<Ast, Identifier, ContextBuilder> UseBuilderBase;

class KDEVPYTHONDUCHAIN_EXPORT UseBuilder: public UseBuilderBase
{
public:
    /// vector of names to ignore since they were unknown imports
    UseBuilder(PythonEditorIntegrator *editor, QVector<IndexedString> ignoreVariables);
    ParseSession* parseSession() const;

protected:
    virtual void visitName(NameAst* node);
    virtual void visitCall(CallAst* node);
    virtual void visitAttribute(AttributeAst* node);
    virtual void visitSubscript(SubscriptAst* node);
private:
    ParseSession* m_session;
    inline int& nextUseIndex()
    {
        return m_nextUseStack.top();
    }
    QStack<int> m_nextUseStack;
    bool m_errorReportingEnabled;
    inline void disableErrorReporting() {
        m_errorReportingEnabled = false;
    };
    inline void enableErrorReporting() {
        m_errorReportingEnabled = true;
    };
    DUContext* contextAtOrCurrent(const CursorInRevision& pos);
    // Add a use for `method` immediately after `value`.
    void useHiddenMethod(ExpressionAst* value, Declaration* method);

    QVector<IndexedString> m_ignoreVariables;
};

}

#endif
// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
