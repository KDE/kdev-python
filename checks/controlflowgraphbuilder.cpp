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

#include "controlflowgraphbuilder.h"
#include "duchain/helpers.h"
#include <language/checks/controlflownode.h>

namespace Python {

ControlFlowGraphBuilder::ControlFlowGraphBuilder(const KDevelop::ReferencedTopDUContext& top,
                                                 KDevelop::ControlFlowGraph* graph,
                                                 QExplicitlySharedDataPointer<Python::ParseSession> session)
    : m_graph(graph)
    , m_currentNode(nullptr)
    , m_session(session)
    , m_top(top)
    , m_editorIntegrator(new PythonEditorIntegrator(session.data()))
{
}

RangeInRevision ControlFlowGraphBuilder::range(const Ast* node) const
{
    return m_editorIntegrator->findRange(node);
}

RangeInRevision ControlFlowGraphBuilder::range(const Compound& nodelist) const
{
    if ( nodelist.isEmpty() ) {
        return RangeInRevision();
    }
    return m_editorIntegrator->findRange(nodelist.first(), nodelist.last());
}

ControlFlowGraphBuilder::Node* ControlFlowGraphBuilder::createNodeForCompound(const ControlFlowGraphBuilder::Compound& nodelist) const
{
    auto ran = range(nodelist);
    auto node = new Node();
    node->setStartCursor(ran.start);
    node->setEndCursor(ran.end);
    return node;
}
RangeInRevision ControlFlowGraphBuilder::encompass(const RangeInRevision& a, const RangeInRevision& b) const
{
    Q_ASSERT(a.start < b.start);
    return RangeInRevision(a.start, b.end);
}

RangeInRevision ControlFlowGraphBuilder::encompass(const ControlFlowGraphBuilder::Node* a,
                                                   const ControlFlowGraphBuilder::Node* b) const
{
    auto end = b->nodeRange();
    if ( b->nodeRange().isEmpty() ) {
        end = a->nodeRange();
    }
    return RangeInRevision(a->nodeRange().start, end.end);
}

void ControlFlowGraphBuilder::setRangeOnNode(const RangeInRevision& range, ControlFlowGraphBuilder::Node* a) const
{
    a->setStartCursor(range.start);
    a->setEndCursor(range.end);
}

void ControlFlowGraphBuilder::finishWithNode(const Ast* node)
{
    if ( ! node ) {
        return;
    }
    m_currentNode->setEndCursor(range(node).start);
}

void ControlFlowGraphBuilder::setCurrentNode(ControlFlowGraphBuilder::Node* node, const Compound& body)
{
    m_currentCompound = body;
    m_currentNode = node;
}

ControlFlowGraphBuilder::Node* ControlFlowGraphBuilder::resume(const Compound& interrupted_body,
                                                               Ast* continue_after)
{
    auto start = range(continue_after).end;
    auto end = range(interrupted_body).end;
    auto node = new Node();
    node->setStartCursor(start);
    node->setEndCursor(end);
    return node;
}

void ControlFlowGraphBuilder::visitFunctionOrClass(Identifier* name, const Compound& compound)
{
    DUChainReadLocker lock;
    auto pos = range(name).start + CursorInRevision(0, 1);
    auto context = m_top->findContextAt(pos);
    auto d = context->findDeclarationAt(pos);
    auto func = new Node();
    func->setStartCursor(range(compound.first()).start);
    func->setEndCursor(range(compound.last()).end);
    auto body = createNodeForCompound(compound);
    func->setNext(body);
    if ( ! d ) {
        return;
    }
    m_graph->addEntry(d, func);
    setCurrentNode(body, compound);
}

void ControlFlowGraphBuilder::visitFunctionDefinition(Python::FunctionDefinitionAst* node)
{
    visitFunctionOrClass(node->name, node->body);
    Python::AstDefaultVisitor::visitFunctionDefinition(node);
}

void ControlFlowGraphBuilder::visitClassDefinition(ClassDefinitionAst* node)
{
    visitFunctionOrClass(node->name, node->body);
    Python::AstDefaultVisitor::visitClassDefinition(node);
}

void ControlFlowGraphBuilder::visitReturn(ReturnAst* node)
{
    auto ret = new Node();
    m_currentNode->setNext(ret);
    m_graph->addEntry(ret);
    Python::AstDefaultVisitor::visitReturn(node);
}

void ControlFlowGraphBuilder::visitIf(IfAst* node)
{
    finishWithNode(node->body.first());
    auto interrupted = m_currentCompound;

    auto ifexpr = new Node();
    m_currentNode->setNext(ifexpr);
    auto if_ = createNodeForCompound(node->body);
    auto else_ = createNodeForCompound(node->orelse);
    ifexpr->setNext(if_);
    ifexpr->setAlternative(else_);

    setCurrentNode(if_, node->body);
    for ( auto n: node->body ) {
        visitNode(n);
    }
    setCurrentNode(else_, node->orelse);
    for ( auto n: node->orelse ) {
        visitNode(n);
    }

    auto resumed = resume(interrupted, node);
    if_->setNext(resumed);
    else_->setNext(resumed);
    setCurrentNode(resumed, interrupted);
}

void ControlFlowGraphBuilder::visitWhile(WhileAst* node)
{
    finishWithNode(node->body.first());
    auto interrupted = m_currentCompound;

    auto while_ = new Node();
    m_currentNode->setNext(while_);
    auto body = createNodeForCompound(node->body);
    while_->setNext(body);

    setCurrentNode(body, node->body);
    Python::AstDefaultVisitor::visitWhile(node);

    auto resumed = resume(interrupted, node);
    body->setNext(resumed);
    setCurrentNode(resumed, interrupted);
}

void ControlFlowGraphBuilder::visitBreak(BreakAst* node)
{
    auto break_ = new Node();
    m_currentNode->setNext(break_);
    setRangeOnNode(range(node), break_);

    Python::AstDefaultVisitor::visitBreak(node);
}

void ControlFlowGraphBuilder::visitFor(ForAst* node)
{
    finishWithNode(node->body.first());
    auto interrupted = m_currentCompound;

    auto for_ = new Node();
    m_currentNode->setNext(for_);
    auto body = createNodeForCompound(node->body);
    for_->setNext(body);

    setCurrentNode(for_, node->body);
    Python::AstDefaultVisitor::visitFor(node);

    auto resumed = resume(interrupted, node);
    body->setNext(resumed);
    setCurrentNode(resumed, interrupted);
}

void ControlFlowGraphBuilder::visitContinue(ContinueAst* node)
{
    auto continue_ = new Node();
    m_currentNode->setNext(continue_);
    setRangeOnNode(range(node), continue_);

    Python::AstDefaultVisitor::visitContinue(node);
}

}
