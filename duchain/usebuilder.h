/*
    SPDX-FileCopyrightText: 2007 Piyush verma <piyush.verma@gmail.com>
    SPDX-FileCopyrightText: 2010-2013 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
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
    void visitName(NameAst* node) override;
    void visitCall(CallAst* node) override;
    void visitAttribute(AttributeAst* node) override;
    void visitSubscript(SubscriptAst* node) override;
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
