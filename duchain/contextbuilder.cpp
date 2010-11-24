/*****************************************************************************
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 *   Copyright 2007 Andreas Pakulat <apaku@gmx.de>                           *
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
#include "contextbuilder.h"
// #include <language/duchain/language.h>
#include <language/duchain/duchainlock.h>
#include <language/duchain/topducontext.h>
#include <language/duchain/parsingenvironment.h>
#include <ktexteditor/smartrange.h>
#include <ktexteditor/smartinterface.h>
#include <ktexteditor/document.h>
#include "pythoneditorintegrator.h"
#include "dumpchain.h"
#include <language/editor/rangeinrevision.h>
#include <interfaces/foregroundlock.h>
#include <pythonparsejob.h>
#include <interfaces/icore.h>
#include <interfaces/idocumentcontroller.h>
#include <interfaces/iprojectcontroller.h>
#include <project/projectmodel.h>
#include <interfaces/iproject.h>
#include "usebuilder.h"
#include "pythonducontext.h"

using namespace KDevelop;

using namespace KTextEditor;

Python::PythonEditorIntegrator* Python::ContextBuilder::m_editor;

namespace Python
{
    
TopDUContext* ParseJob::m_internalFunctions;

PythonEditorIntegrator* ContextBuilder::editor() const
{
    return ContextBuilder::m_editor;
}

TopDUContext* ContextBuilder::newTopContext(const RangeInRevision& range, ParsingEnvironmentFile* file) 
{
    IndexedString currentDocumentUrl = ContextBuilder::m_editor->parseSession()->currentDocument();
    kDebug() << currentDocumentUrl.str();
    
    if ( !file ) {
        file = new ParsingEnvironmentFile(currentDocumentUrl);
        file->setLanguage(IndexedString("python"));
    }
    TopDUContext* top = new PythonDUContext<TopDUContext>(currentDocumentUrl, range, file);
    ReferencedTopDUContext ref(top);
    m_topContext = ref;
    return top;
}

DUContext* ContextBuilder::newContext(const RangeInRevision& range)
{
    return new PythonDUContext<DUContext>(range, currentContext());
}

void ContextBuilder::setEditor(PythonEditorIntegrator* editor)
{
    //m_identifierCompiler = new IdentifierCompiler(editor->parseSession());
    ContextBuilder::m_editor = editor;
}

void ContextBuilder::setEditor(ParseSession* session)
{
    PythonEditorIntegrator* e = new PythonEditorIntegrator(/*session*/);
    //m_identifierCompiler = new IdentifierCompiler(e->parseSession());
    setEditor(e);
}

void ContextBuilder::startVisiting( Ast* node )
{
    visitNode( node );
}

void ContextBuilder::setContextOnNode( Ast* node, DUContext* context )
{
    node->context = context;
}

DUContext* ContextBuilder::contextFromNode( Ast* node )
{
    return node->context;
}

RangeInRevision ContextBuilder::editorFindRange( Ast* fromNode, Ast* toNode )
{
    return editor()->findRange(fromNode, toNode);
}

QualifiedIdentifier ContextBuilder::identifierForNode( Python::Identifier* node )
{
    return QualifiedIdentifier( node->value );
}

void ContextBuilder::addImportedContexts()
{
    if ( compilingContexts() && !m_importedParentContexts.isEmpty() )
    {
        DUChainWriteLocker lock( DUChain::lock() );
        foreach( DUContext* imported, m_importedParentContexts )
            currentContext()->addImportedParentContext( imported );

        m_importedParentContexts.clear();
    }
}

void ContextBuilder::openContextForStatementList( const QList<Ast*>& l, DUContext::ContextType type)
{
    if ( l.count() > 0 )
    {
        Ast* first = l.first();
        Ast* last = l.last();
        Q_ASSERT(first->hasUsefulRangeInformation); // TODO remove this
        RangeInRevision range(RangeInRevision(first->startLine - 1, first->startCol, last->endLine + 1, 10000));
        DUContext* rangectx = openContext(first, range, DUContext::Other );
        kDebug() << " +++ opening context (stmlist): " << range.castToSimpleRange();
        addImportedContexts();
        visitNodeList( l );
        closeContext();
        kDebug() << " --- closed context (stmlist): line " << rangectx->range().castToSimpleRange();
    }
}

void ContextBuilder::visitAttribute(AttributeAst* node)
{
    Python::AstDefaultVisitor::visitAttribute(node);
}

void ContextBuilder::visitClassDefinition( ClassDefinitionAst* node )
{
    RangeInRevision range(node->body.first()->startLine, node->body.first()->startCol, node->body.last()->endLine, node->body.last()->endCol + 100000);
    openContext( node, range, DUContext::Class, identifierForNode( node->name ) );
    kDebug() << " +++ opening CLASS context: " << range.castToSimpleRange();
    addImportedContexts();
    Python::AstDefaultVisitor::visitClassDefinition(node);
    closeContext();
    kDebug() << " --- closing CLASS context: " << range.castToSimpleRange();
}

void ContextBuilder::visitArguments(ArgumentsAst* node)
{
    AstDefaultVisitor::visitArguments(node);
}

void ContextBuilder::visitCode(CodeAst* node) {
    DUChainWriteLocker lock(DUChain::lock());
    TopDUContext* internal = DUChain::self()->chainForDocument(KUrl("/home/sven/projects/kde4/python/documentation/test.py"));
    if ( internal ) {
        currentContext()->addImportedParentContext(internal);
    }
    AstDefaultVisitor::visitCode(node);
}

KUrl ContextBuilder::findModulePath(const QString& name)
{
    QStringList modulePath = name.split(".");
    
    KUrl currentPath = currentContext()->url().toUrl();
    Q_ASSERT(currentPath.url().length());
    kDebug() << " >>>>>>>>> Got URL: " << currentPath.upUrl().url(KUrl::RemoveTrailingSlash);
    
    IProject* currentProject = ICore::self()->projectController()->findProjectForUrl(currentPath);
    if ( ! currentProject ) {
        kError() << "Cannot import module contexts without a project opened.";
        return KUrl();
    }
    
    // easiest case: current directory
    KUrl filename(currentPath.directory(KUrl::AppendTrailingSlash) + modulePath.first() + ".py");
    kDebug() << "filename url: " << filename;
    if ( currentProject->filesForUrl(filename).length() > 0 ) {
        ProjectFileItem* result = currentProject->filesForUrl(filename).first();
        kDebug() << "Found! " << result->url();
        return result->url();
    }
    
    return KUrl();
}

void ContextBuilder::visitImportFrom(ImportFromAst* node)
{
    Python::AstDefaultVisitor::visitImportFrom(node);
}

void ContextBuilder::visitImport(ImportAst* node)
{
    foreach ( AliasAst* name, node->names ) {
        // for "import ... as", use the as thingy, use the module name otherwise
        Identifier* variableDeclarationName = name->asName ? name->asName->identifier : name->name;
        
        KUrl moduleFilePath = findModulePath(name->name->value);
        if ( ! moduleFilePath.isValid() ) continue;
        else {
            DUChainWriteLocker lock(DUChain::lock());
            TopDUContext* moduleChain = DUChain::self()->chainForDocument(KUrl(moduleFilePath));
            contextsForModules.insert(name->name->value, TopDUContextPointer(moduleChain));
            kDebug() << "Added " << name->name->value << " to the module chain map";
//             currentContext()->addImportedParentContext(moduleChain);
        }
    }
    Python::AstDefaultVisitor::visitImport(node);
}

void ContextBuilder::visitFunctionDefinition( FunctionDefinitionAst* node )
{
    kDebug() << " Building function definition context: " << node->name->value;
    DUChainWriteLocker lock(DUChain::lock());
    
    visitNodeList( node->decorators );
    
    Ast* first = node->body.first();
    Ast* last = node->body.last();
    Q_ASSERT(first->hasUsefulRangeInformation); // TODO remove this
    RangeInRevision range(RangeInRevision(first->startLine, first->startCol, last->endLine, last->endCol + 100000));
    
    if ( node->arguments && node->arguments->arguments.length() )
    {
        int sline, eline, scol, ecol;
        sline = node->arguments->arguments.first()->startLine;
        eline = node->arguments->arguments.last()->endLine;
        scol = node->arguments->arguments.first()->startCol;
        ecol = node->arguments->arguments.last()->endCol;
        
        RangeInRevision range(sline, scol, eline, ecol+100000);
        Q_ASSERT(range.isValid());
        DUContext* funcctx = openContext( node->arguments, range, DUContext::Function);
        kDebug() << funcctx;
        kDebug() << " +++ opening FUNCTION ARGUMENTS context: " << funcctx->range().castToSimpleRange();
        visitNode( node->arguments );
        closeContext();
        m_importedParentContexts.append( funcctx );
    }
    
    DUContext* ctx = openContext(first, range, DUContext::Function, identifierForNode( node->name ) );
    kDebug() << " +++ opening context (function definition): " << range.castToSimpleRange();
    addImportedContexts();
    
    visitNodeList(node->body);
    
    closeContext();
    kDebug() << " --- closed context (function definition): " << ctx->range().castToSimpleRange();
}

void ContextBuilder::visitWith( WithAst * node )
{
    m_importedParentContexts = QList<DUContext*>() << openContext( node->contextExpression, DUContext::Other );
    kDebug() << " +++ opening context: " << node->startLine - 1 << ":" << node->startCol << " -- " << node->endLine + 1 << "inf";
    visitNode( node->contextExpression );
    closeContext();

    openContextForStatementList( node->body );
    m_importedParentContexts.clear();
}

}
