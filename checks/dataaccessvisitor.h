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

#ifndef DATAACCESSVISITOR_H
#define DATAACCESSVISITOR_H

#include "parser/astdefaultvisitor.h"
#include <language/duchain/topducontext.h>
#include <language/checks/dataaccessrepository.h>
#include <pythoneditorintegrator.h>

#include <QExplicitlySharedDataPointer>
#include <memory>

namespace Python {

class DataAccessVisitor : public Python::AstDefaultVisitor
{
public:
    using Access = KDevelop::DataAccess::DataAccessFlag;

    DataAccessVisitor(const KDevelop::ReferencedTopDUContext& top,
                      KDevelop::DataAccessRepository* repo,
                      QExplicitlySharedDataPointer<Python::ParseSession> session);

    virtual void visitNode(Ast* node);

    Access transformFlag(Python::ExpressionAst::Context);
    Access accessForNode(Python::Ast* node);
    virtual void visitAssignment(AssignmentAst* node);

private:
    KDevelop::DataAccessRepository* m_repo;
    const KDevelop::ReferencedTopDUContext m_top;
    std::unique_ptr<PythonEditorIntegrator> m_editorIntegrator;
};

}

#endif // DATAACCESSVISITOR_H
