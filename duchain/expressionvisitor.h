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
#include <language/duchain/functiondeclaration.h>
#include <language/duchain/builders/dynamiclanguageexpressionvisitor.h>

#include "astdefaultvisitor.h"
#include "pythonduchainexport.h"
#include "pythoneditorintegrator.h"

#include "duchain/declarations/classdeclaration.h"
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

    virtual void visitBinaryOperation(BinaryOperationAst* node);
    virtual void visitUnaryOperation(UnaryOperationAst* node);
    virtual void visitBooleanOperation(BooleanOperationAst* node);
    virtual void visitCompare(CompareAst* node);

    virtual void visitString(StringAst* node);
    virtual void visitBytes(BytesAst* node);
    virtual void visitNumber(NumberAst* node);
    virtual void visitName(NameAst* node);
    virtual void visitList(ListAst* node);
    virtual void visitDict(DictAst* node);
    virtual void visitSet(SetAst* node);
    virtual void visitSubscript(SubscriptAst* node);
    virtual void visitCall(CallAst* node);
    virtual void visitAttribute(AttributeAst* node);
    virtual void visitTuple(TupleAst* node);
    virtual void visitListComprehension(ListComprehensionAst* node);
    virtual void visitDictionaryComprehension(DictionaryComprehensionAst* node);
    virtual void visitSetComprehension(SetComprehensionAst* node);
    virtual void visitIfExpression(IfExpressionAst* node);
    virtual void visitNameConstant(NameConstantAst* node);

    /**
     * @brief Checks the decorators of the given function declaration.
     *
     * @param node The node to visit
     * @param funcDecl The call's function declaration, if any
     * @param classDecl The call's class declaration, if any
     * @param isConstructor whether a constructor is being called
     */
    void checkForDecorators(CallAst* node, Python::FunctionDeclaration* funcDecl,
                            Python::ClassDeclaration* classDecl, bool isConstructor);

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
        auto decls = Helper::getDocumentationFileContext()->findDeclarations(QualifiedIdentifier(typeDescriptor));
        auto decl = decls.isEmpty() ? nullptr : dynamic_cast<Declaration*>(decls.first());
        auto type = decl ? decl->abstractType() : AbstractType::Ptr();
        return type.cast<T>();
    }

private:
    AbstractType::Ptr fromBinaryOperator(AbstractType::Ptr lhs, AbstractType::Ptr rhs, const QString& op);
    AbstractType::Ptr encounterPreprocess(AbstractType::Ptr type, bool merge=false);
    void encounter(AbstractType::Ptr type, DeclarationPointer declaration=DeclarationPointer(), bool alias=false);

    void addUnknownName(const QString& name);

    virtual AbstractType::Ptr encounterPreprocess(AbstractType::Ptr type);

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
