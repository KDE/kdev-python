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
#include "usebuilder.h"

#include <QDebug>
#include "duchaindebug.h"

#include <language/duchain/declaration.h>
#include <language/duchain/use.h>
#include <language/duchain/topducontext.h>
#include <language/duchain/duchain.h>
#include <language/duchain/duchainlock.h>
#include <language/duchain/types/structuretype.h>

#include "parsesession.h"
#include "pythoneditorintegrator.h"
#include "ast.h"
#include "expressionvisitor.h"
#include "helpers.h"

using namespace KTextEditor;
using namespace KDevelop;

namespace Python {

UseBuilder::UseBuilder(PythonEditorIntegrator* editor, QVector<IndexedString> ignoreVariables)
    : UseBuilderBase()
    , m_errorReportingEnabled(true)
    , m_ignoreVariables(ignoreVariables)
{
    setEditor(editor);
}

DUContext* UseBuilder::contextAtOrCurrent(const CursorInRevision& pos)
{
    DUContext* context = 0;
    {
        DUChainReadLocker lock;
        context = topContext()->findContextAt(pos, true);
    }
    if ( ! context ) {
        context = currentContext();
    }
    return context;
}

void UseBuilder::useHiddenMethod(ExpressionAst* value, IndexedIdentifier method) {
    DUContext* context = contextAtOrCurrent(editorFindPositionSafe(value));
    ExpressionVisitor v(context);
    v.visitNode(value);
    RangeInRevision useRange;
    // TODO fixme! this does not necessarily use the opening bracket as it should
    useRange.start = CursorInRevision(value->endLine, value->endCol + 1);
    useRange.end = CursorInRevision(value->endLine, value->endCol + 2);
    DUChainReadLocker lock;
    auto function = Helper::accessAttribute(v.lastType(), method, context->topContext());
    lock.unlock();
    if ( function && function->isFunctionDeclaration() ) {
        UseBuilderBase::newUse(value, useRange, DeclarationPointer(function));
    }
}

void UseBuilder::visitName(NameAst* node)
{
    DUContext* context = contextAtOrCurrent(editorFindPositionSafe(node));
    Declaration* declaration = Helper::declarationForName(identifierForNode(node->identifier),
                                                          editorFindRange(node, node),
                                                          DUChainPointer<const DUContext>(context));

    static const QStringList keywords = {"None", "True", "False"};

    Q_ASSERT(node->identifier);
    RangeInRevision useRange = rangeForNode(node->identifier, true);

    if ( declaration && declaration->range() == useRange ) return;

    if ( ! declaration && ! keywords.contains(node->identifier->value) && m_errorReportingEnabled ) {
        if ( ! m_ignoreVariables.contains(IndexedString(node->identifier->value)) ) {
            KDevelop::Problem *p = new KDevelop::Problem();
            p->setFinalLocation(DocumentRange(currentlyParsedDocument(), useRange.castToSimpleRange())); // TODO ok?
            p->setSource(KDevelop::IProblem::SemanticAnalysis);
            p->setSeverity(KDevelop::IProblem::Hint);
            p->setDescription(i18n("Undefined variable: %1", node->identifier->value));
            {
                DUChainWriteLocker wlock(DUChain::lock());
                ProblemPointer ptr(p);
                topContext()->addProblem(ptr);
            }
        }
    }
    UseBuilderBase::newUse(node, useRange, DeclarationPointer(declaration));
}

void UseBuilder::visitCall(CallAst* node)
{
    UseBuilderBase::visitCall(node);
    DUContext* context = contextAtOrCurrent(editorFindPositionSafe(node));
    ExpressionVisitor v(context);
    v.visitNode(node->function);
    if ( auto classType = v.lastType().cast<StructureType>() ) {
        DUChainReadLocker lock;
        // This is either __init__() or __call__(): `a = Foo()` or `b = a()`.
        auto function = Helper::functionForCalled(classType->declaration(topContext()), v.isAlias());
        lock.unlock();
        RangeInRevision openingParenRange;
        // TODO fixme! this does not necessarily use the opening bracket as it should
        openingParenRange.start = CursorInRevision(node->endLine, node->endCol + 1);
        openingParenRange.end = CursorInRevision(node->endLine, node->endCol + 2);
        UseBuilderBase::newUse(node, openingParenRange, DeclarationPointer(function.declaration));
    }
}

void UseBuilder::visitAttribute(AttributeAst* node)
{
    qCDebug(KDEV_PYTHON_DUCHAIN) << "VisitAttribute start";
    UseBuilderBase::visitAttribute(node);
    qCDebug(KDEV_PYTHON_DUCHAIN) << "Visit Attribute base end";

    DUContext* context = contextAtOrCurrent(editorFindPositionSafe(node));
    ExpressionVisitor v(context);
    v.visitNode(node);
    RangeInRevision useRange(node->attribute->startLine, node->attribute->startCol,
                             node->attribute->endLine, node->attribute->endCol + 1);
    
    DeclarationPointer declaration = v.lastDeclaration();
    DUChainWriteLocker wlock;
    if ( declaration && declaration->range() == useRange ) {
        // this is the declaration, don't build a use for it
        return;
    }
    if ( ! declaration && v.isConfident() && ( ! v.lastType() || Helper::isUsefulType(v.lastType()) ) ) {
        KDevelop::Problem *p = new KDevelop::Problem();
        p->setFinalLocation(DocumentRange(currentlyParsedDocument(), useRange.castToSimpleRange()));
        p->setSource(KDevelop::IProblem::SemanticAnalysis);
        p->setSeverity(KDevelop::IProblem::Hint);
        p->setDescription(i18n("Attribute \"%1\" not found on accessed object", node->attribute->value));
        ProblemPointer ptr(p);
        topContext()->addProblem(ptr);
    }
    UseBuilderBase::newUse(node, useRange, declaration);
}

void UseBuilder::visitSubscript(SubscriptAst* node) {
    UseBuilderBase::visitSubscript(node);
    static const IndexedIdentifier getitemIdentifier(KDevelop::Identifier("__getitem__"));
    static const IndexedIdentifier setitemIdentifier(KDevelop::Identifier("__setitem__"));
    bool isAugTarget = (node->parent->astType == Ast::AugmentedAssignmentAstType &&
                        static_cast<AugmentedAssignmentAst*>(node->parent)->target == node);
    // e.g `a[0] += 2` uses both __getitem__ and __setitem__.
    if (isAugTarget || node->context == ExpressionAst::Context::Load) {
        useHiddenMethod(node->value, getitemIdentifier);
    }
    if ( node->context == ExpressionAst::Context::Store ) {
        useHiddenMethod(node->value, setitemIdentifier);
    }
}

ParseSession *UseBuilder::parseSession() const
{
    return m_session;
}

}
// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
