/*****************************************************************************
 * Copyright 2010 Miquel Canes Gonzalez <miquelcanes@gmail.com>              *
 * Copyright 2011-2014 Sven Brauch <svenbrauch@googlemail.com>               *
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

#ifndef EXPRESSIONVISITOR_H
#define EXPRESSIONVISITOR_H

#include <QHash>
#include <KLocalizedString>

#include <language/duchain/types/abstracttype.h>
#include <language/duchain/types/integraltype.h>
#include <language/duchain/types/typesystemdata.h>
#include <language/duchain/types/typeregister.h>
#include <language/duchain/types/containertypes.h>
#include <language/duchain/duchainpointer.h>
#include <language/duchain/declaration.h>
#include <language/duchain/types/structuretype.h>
#include <language/duchain/classdeclaration.h>
#include <language/duchain/functiondeclaration.h>
#include <language/duchain/builders/dynamiclanguageexpressionvisitor.h>

#include "astdefaultvisitor.h"
#include "pythonduchainexport.h"
#include "pythoneditorintegrator.h"

#include "duchain/declarations/functiondeclaration.h"
#include "duchain/helpers.h"

using namespace KDevelop;
class Identifier;

namespace Python
{

typedef DUChainPointer<FunctionDeclaration> FunctionDeclarationPointer;

class KDEVPYTHONDUCHAIN_EXPORT ExpressionVisitor : public AstDefaultVisitor, public DynamicLanguageExpressionVisitor
{
public:
    ExpressionVisitor(const KDevelop::DUContext* ctx);
    /// Use this to construct the expression-visitor recursively
    ExpressionVisitor(Python::ExpressionVisitor* parent, const DUContext* overrideContext=nullptr);

    void visitBinaryOperation(BinaryOperationAst* node) override;
    void visitUnaryOperation(UnaryOperationAst* node) override;
    void visitBooleanOperation(BooleanOperationAst* node) override;
    void visitCompare(CompareAst* node) override;

    void visitString(StringAst* node) override;
    void visitBytes(BytesAst* node) override;
    void visitFormattedValue(FormattedValueAst * node) override;
    void visitJoinedString(JoinedStringAst* node) override;
    void visitNumber(NumberAst* node) override;
    void visitName(NameAst* node) override;
    void visitList(ListAst* node) override;
    void visitDict(DictAst* node) override;
    void visitSet(SetAst* node) override;
    void visitSubscript(SubscriptAst* node) override;
    void visitCall(CallAst* node) override;
    void visitAttribute(AttributeAst* node) override;
    void visitTuple(TupleAst* node) override;
    void visitLambda(LambdaAst* node) override;
    void visitListComprehension(ListComprehensionAst* node) override;
    void visitDictionaryComprehension(DictionaryComprehensionAst* node) override;
    void visitSetComprehension(SetComprehensionAst* node) override;
    void visitIfExpression(IfExpressionAst* node) override;
    void visitNameConstant(NameConstantAst* node) override;
    void visitAssignmentExpression(AssignmentExpressionAst* node) override;

    /**
     * @brief Checks for magic docstrings that override a call's return type.
     *
     * @param node The node to visit.
     * @param normalType The return type as determined without docstrings.
     * @param docstring Docstring of the function.
     */
    AbstractType::Ptr docstringTypeOverride(CallAst* node, const AbstractType::Ptr normalType,
                                              const QString& docstring);

    bool isAlias() const {
        return m_isAlias;
    }

    void enableGlobalSearching() {
        m_forceGlobalSearching = true;
    }

    void enableUnknownNameReporting() {
        m_reportUnknownNames = true;
    }

    void scanUntil(const CursorInRevision& end) {
        m_scanUntilCursor = end;
    }

    QSet<QString> unknownNames() const {
        return m_unknownNames;
    }

    template<typename T>
    static TypePtr<T> typeObjectForIntegralType(const QString& typeDescriptor) {
        auto context = Helper::getDocumentationFileContext();
        if ( ! context ) {
            AbstractType::Ptr null;
            return null.cast<T>();
        }
        auto decls = context->findDeclarations(QualifiedIdentifier(typeDescriptor));
        auto decl = decls.isEmpty() ? nullptr : dynamic_cast<Declaration*>(decls.first());
        auto type = decl ? decl->abstractType() : AbstractType::Ptr();
        return type.cast<T>();
    }

private:
    AbstractType::Ptr fromBinaryOperator(AbstractType::Ptr lhs, AbstractType::Ptr rhs, const QString& op);
    AbstractType::Ptr encounterPreprocess(AbstractType::Ptr type, bool merge=false);
    void encounter(AbstractType::Ptr type, DeclarationPointer declaration=DeclarationPointer(), bool alias=false);

    void addUnknownName(const QString& name);

    AbstractType::Ptr encounterPreprocess(AbstractType::Ptr type) override;

    void setLastIsAlias(bool alias) {
        m_isAlias = alias;
    }

private:
    /// tells whether the returned declaration is an alias
    bool m_isAlias = false;
    /// used by code completion to disable range checks on declaration searches
    bool m_forceGlobalSearching = false;
    /// used by code completion to detect unknown NameAst elements in expressions
    bool m_reportUnknownNames = false;
    CursorInRevision m_scanUntilCursor = CursorInRevision::invalid();
    static QHash<NameConstantAst::NameConstantTypes, KDevelop::AbstractType::Ptr> m_defaultTypes;
    QSet<QString> m_unknownNames;
};

}

#endif // EXPRESSIONVISITOR_H
