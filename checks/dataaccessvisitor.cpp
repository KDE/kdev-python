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

#include "dataaccessvisitor.h"

namespace Python {

DataAccessVisitor::DataAccessVisitor(const KDevelop::ReferencedTopDUContext& top,
                                     KDevelop::DataAccessRepository* repo,
                                     QExplicitlySharedDataPointer<Python::ParseSession> session)
    : m_top(top)
    , m_repo(repo)
    , m_editorIntegrator(new Python::PythonEditorIntegrator(session.data()))
{
}

DataAccessVisitor::Access DataAccessVisitor::transformFlag(ExpressionAst::Context context)
{
    if ( context == ExpressionAst::AugLoad || context == ExpressionAst::Load ) {
        return DataAccess::Read;
    }
    if ( context == ExpressionAst::AugStore || context == ExpressionAst::Store ) {
        return DataAccess::Write;
    }
    if ( context == ExpressionAst::Parameter ) {
        // TODO
        return DataAccess::Read;
    }
    return DataAccess::None;
}

void DataAccessVisitor::visitAssignment(AssignmentAst* node)
{
    // make sure rhs is visited first
    visitNode(node->value);
    foreach (ExpressionAst* expression, node->targets) {
        visitNode(expression);
    };
}

DataAccessVisitor::Access DataAccessVisitor::accessForNode(Ast* node)
{
    static QSet<Python::Ast::AstType> types;
    if ( types.isEmpty() ) {
        types << Python::Ast::NameAstType << Python::Ast::AttributeAstType << Python::Ast::SubscriptAstType
              << Python::Ast::ListAstType << Python::Ast::TupleAstType;
    }

    if ( node->isExpression() ) {
        auto expr = static_cast<ExpressionAst*>(node);
        if ( expr->belongsToCall ) {
            return Access::Call;
        }
    }

    auto context = Access::None;
    if ( types.contains(node->astType) ) {
        auto flag = ExpressionAst::Invalid;
        switch ( node->astType ) {
            case Ast::NameAstType: flag = static_cast<NameAst*>(node)->context; break;
            case Ast::AttributeAstType: flag = static_cast<AttributeAst*>(node)->context; break;
            case Ast::SubscriptAstType: flag = static_cast<SubscriptAst*>(node)->context; break;
            case Ast::ListAstType: flag = static_cast<ListAst*>(node)->context; break;
            case Ast::TupleAstType: flag = static_cast<TupleAst*>(node)->context; break;
            default: Q_ASSERT(false);
        }
        context = transformFlag(flag);
    }
    return context;
}

void DataAccessVisitor::visitNode(Ast* node)
{
    if ( ! node ) {
        return;
    }
    auto pos = m_editorIntegrator->findPosition(node, PythonEditorIntegrator::FrontEdge);
    auto kind = accessForNode(node);
    if ( kind != DataAccess::None ) {
        m_repo->addModification(pos, kind);
    }
    Python::AstVisitor::visitNode(node);
}

}
