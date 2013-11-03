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

#include <KUrl>

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

UseBuilder::UseBuilder (PythonEditorIntegrator* editor) : UseBuilderBase(), m_errorReportingEnabled(true)
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

void UseBuilder::visitName(NameAst* node)
{
    DUContext* context = contextAtOrCurrent(editorFindPositionSafe(node));
    Declaration* declaration = Helper::declarationForName(node, identifierForNode(node->identifier),
                                                          editorFindRange(node, node), DUContextPointer(context));
    
    QStringList keywords;
    keywords << "None" << "True" << "False" << "print";
    
    Q_ASSERT(node->identifier);
    RangeInRevision useRange = rangeForNode(node->identifier, true);
    
    if ( declaration && declaration->range() == useRange ) return;
    
    if ( ! declaration && ! keywords.contains(node->identifier->value) && m_errorReportingEnabled ) {
        KDevelop::Problem *p = new KDevelop::Problem();
        p->setFinalLocation(DocumentRange(currentlyParsedDocument(), useRange.castToSimpleRange())); // TODO ok?
        p->setSource(KDevelop::ProblemData::SemanticAnalysis);
        p->setSeverity(KDevelop::ProblemData::Hint);
        p->setDescription(i18n("Undefined variable: %1", node->identifier->value));
        {
            DUChainWriteLocker wlock(DUChain::lock());
            ProblemPointer ptr(p);
            topContext()->addProblem(ptr);
        }
    }
    
    if ( declaration && declaration->abstractType() && declaration->abstractType()->whichType() == AbstractType::TypeStructure ) {
        if ( node->belongsToCall ) {
            DUChainReadLocker lock;
            QPair< Python::FunctionDeclarationPointer, bool > constructor = Helper::
                             functionDeclarationForCalledDeclaration(DeclarationPointer(declaration));
            lock.unlock();
            bool isConstructor = constructor.second;
            if ( isConstructor ) {
                RangeInRevision constructorRange;
                // TODO fixme! this does not necessarily use the opening bracket as it should
                constructorRange.start = CursorInRevision(node->endLine, node->endCol + 1);
                constructorRange.end = CursorInRevision(node->endLine, node->endCol + 2);
                UseBuilderBase::newUse(node, constructorRange, DeclarationPointer(constructor.first));
            }
        }
    }
    
    UseBuilderBase::newUse(node, useRange, DeclarationPointer(declaration));
}

void UseBuilder::visitAttribute(AttributeAst* node)
{
    DUContext* context = contextAtOrCurrent(editorFindPositionSafe(node));
    ExpressionVisitor v(context);
    kDebug() << "VisitAttribute start";
    UseBuilderBase::visitAttribute(node);
    kDebug() << "Visit Attribute base end";
    
    v.visitNode(node);
    
    RangeInRevision useRange(node->attribute->startLine, node->attribute->startCol, node->attribute->endLine, node->attribute->endCol + 1);
    
    DeclarationPointer declaration = v.lastDeclaration();
    DUChainWriteLocker wlock(DUChain::lock());
    if ( declaration && declaration->range() == useRange ) return;
    if ( ! declaration && v.shouldBeKnown() && ( ! v.lastType() or Helper::isUsefulType(v.lastType()) ) ) {
        KDevelop::Problem *p = new KDevelop::Problem();
        p->setFinalLocation(DocumentRange(currentlyParsedDocument(), useRange.castToSimpleRange())); // TODO ok?
        p->setSource(KDevelop::ProblemData::SemanticAnalysis);
        p->setSeverity(KDevelop::ProblemData::Hint);
        p->setDescription(i18n("Attribute \"%1\" not found on accessed object", node->attribute->value));
        ProblemPointer ptr(p);
        topContext()->addProblem(ptr);
    }
    UseBuilderBase::newUse(node, useRange, declaration);
}


ParseSession *UseBuilder::parseSession() const
{
    return m_session;
}

}
// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
