/*****************************************************************************
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 * Copyright 2010-2012 Sven Brauch <svenbrauch@googlemail.com>               *
 *                                                                           *
 * Permission is hereby granted, free of charge, to any person obtaining     *
 * a copy of this software and associated documentation files (the           *
 * "Software"), to deal in the Software without restriction, including       *
 * without limitation the rights to use, copy, modify, merge, publish,       *
 * distribute, sublicense, and/or sell copies of the Software, and to        *
 * permit persons to whom the Software is furnished to do so, subject to     *
 * the following conditions:                                                 *
 *                                                                           *
 * The above copyright notice and this permission notice shall be            *
 * included in all copies or substantial portions of the Software.           *
 *                                                                           *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,           *
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF        *
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND                     *
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE    *
 * LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION    *
 * OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION     *
 * WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.           *
 *****************************************************************************/
#include "usebuilder.h"

#include <ktexteditor/smartrange.h>
#include <ktexteditor/smartinterface.h>

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

void UseBuilder::visitName(NameAst* node)
{
    Declaration* declaration = Helper::declarationForName(node, identifierForNode(node->identifier),
                                                          editorFindRange(node, node), DUContextPointer(currentContext()));
    
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
    ExpressionVisitor v(currentContext(), editor());
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
