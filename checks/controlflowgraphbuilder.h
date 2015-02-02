/*****************************************************************************
 * Copyright (c) 2014 Sven Brauch <svenbrauch@gmail.com>                     *
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

#ifndef CONTROLFLOWGRAPHBUILDER_H
#define CONTROLFLOWGRAPHBUILDER_H

#include "parser/astdefaultvisitor.h"
#include <parsesession.h>
#include <pythoneditorintegrator.h>

#include <language/checks/controlflowgraph.h>
#include <language/checks/controlflownode.h>
#include <language/duchain/topducontext.h>

#include <memory>
#include <QExplicitlySharedDataPointer>

namespace Python {

class ControlFlowGraphBuilder : public Python::AstDefaultVisitor
{
public:
    using Node = KDevelop::ControlFlowNode;
    using Compound = QList<Ast*>;

    ControlFlowGraphBuilder(const KDevelop::ReferencedTopDUContext& top, KDevelop::ControlFlowGraph* graph,
                            QExplicitlySharedDataPointer<Python::ParseSession> session);

    virtual void visitFunctionDefinition(Python::FunctionDefinitionAst* node);
    virtual void visitReturn(ReturnAst* node);
    virtual void visitIf(IfAst* node);
    virtual void visitWhile(WhileAst* node);
    virtual void visitBreak(BreakAst* node);
    virtual void visitContinue(ContinueAst* node);
    virtual void visitFor(ForAst* node);
    virtual void visitClassDefinition(ClassDefinitionAst* node);

    void visitFunctionOrClass(Identifier* name, const Compound& body);

    RangeInRevision range(const Ast* node) const;
    RangeInRevision range(const Compound& nodelist) const;

    RangeInRevision encompass(const RangeInRevision& a, const RangeInRevision& b) const;
    RangeInRevision encompass(const Node* a, const Node* b) const;

    void setRangeOnNode(const RangeInRevision& range, Node* a) const;

    Node* createNodeForCompound(const Compound& nodelist) const;

    void finishWithNode(const Ast* node);
    void setCurrentNode(Node* node, const Compound& body);
    Node* resume(const Compound& interrupted_body, Ast* continue_after);

private:
    KDevelop::ControlFlowGraph* m_graph;
    const KDevelop::ReferencedTopDUContext m_top;
    const QExplicitlySharedDataPointer<Python::ParseSession> m_session;
    std::unique_ptr<Python::PythonEditorIntegrator> m_editorIntegrator;

    KDevelop::ControlFlowNode* m_currentNode;
    Compound m_currentCompound;
};

}

#endif // CONTROLFLOWGRAPHBUILDER_H
