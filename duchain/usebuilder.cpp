/*****************************************************************************
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 * Copyright 2010-2011 Sven Brauch <svenbrauch@googlemail.com>               *
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
    keywords << "None" << "True" << "False" << "__name__";
    
    Q_ASSERT(node->identifier);
    Q_ASSERT(node->hasUsefulRangeInformation); // TODO remove this!
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
    
    /// debug
    kDebug() << " Registering use for " << node->identifier->value << " at " << useRange.castToSimpleRange() << "with dec" << declaration;
    {
        DUChainReadLocker lock(DUChain::lock());
        Q_ASSERT( ! declaration || declaration->alwaysForceDirect() );
    }
    /// end debug
    UseBuilderBase::newUse(node, useRange, DeclarationPointer(declaration));
//     kDebug() << "USE FOUND:" << topContext()->findUseAt(useRange.start) << "for declaration" << declaration->toString();
}

void UseBuilder::visitListComprehension(ListComprehensionAst* node)
{
    // TODO fix this properly
    // due to duchain limitations, we currently cannot declare the "x"
    // in "[x for x in range(3)]" properly. Thus, it's always reported as an error;
    // we at least avoid this here, so it's displayed in plain black with no
    // language support whatsoever.
    disableErrorReporting();
    AstDefaultVisitor::visitListComprehension(node);
    enableErrorReporting();
}

void UseBuilder::visitDictionaryComprehension(DictionaryComprehensionAst* node)
{
    disableErrorReporting();
    AstDefaultVisitor::visitDictionaryComprehension(node);
    enableErrorReporting();
}

void UseBuilder::visitGeneratorExpression(GeneratorExpressionAst* node)
{
    disableErrorReporting();
    Python::AstDefaultVisitor::visitGeneratorExpression(node);
    enableErrorReporting();
}

void UseBuilder::visitAttribute(AttributeAst* node)
{
    ExpressionVisitor v(currentContext(), editor());
    kDebug() << "VisitAttribute start";
    UseBuilderBase::visitAttribute(node);
    kDebug() << "Visit Attribute base end";
    
    v.visitNode(node);
    
    RangeInRevision useRange(node->attribute->startLine, node->attribute->startCol, node->attribute->endLine, node->attribute->endCol + 1);
    
    DUChainWriteLocker lock(DUChain::lock());
    DeclarationPointer declaration = v.lastDeclaration();
    if ( declaration && declaration->range() == useRange ) return;
    if ( ! declaration && v.shouldBeKnown() ) {
        KDevelop::Problem *p = new KDevelop::Problem();
        p->setFinalLocation(DocumentRange(currentlyParsedDocument(), useRange.castToSimpleRange())); // TODO ok?
        p->setSource(KDevelop::ProblemData::SemanticAnalysis);
        p->setSeverity(KDevelop::ProblemData::Hint);
        p->setDescription(i18n("Attribute \"%1\" not found on accessed object", node->attribute->value));
        ProblemPointer ptr(p);
        topContext()->addProblem(ptr);
    }
    UseBuilderBase::newUse(node, useRange, declaration);
//     currentContext()->findUseAt();
}


ParseSession *UseBuilder::parseSession() const
{
    return m_session;
}

}
// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
