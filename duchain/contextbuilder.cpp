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
    TopDUContext* top = new TopDUContext(currentDocumentUrl, range, file);
    ReferencedTopDUContext ref(top);
    m_topContext = ref;
    return top;
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

void ContextBuilder::openContextForStatementList( const QList<StatementAst*>& l )
{
    if ( l.count() > 0 )
    {
        Ast* first = l.first();
        Ast* last = l.last();
        openContext(first, RangeInRevision(first->startLine - 1, first->startCol, last->endLine + 1, 10000), DUContext::Other );
        kDebug() << " +++ opening context: " << first->startLine - 1 << ":" << first->startCol << " -- " << last->endLine + 1 << "inf";
        addImportedContexts();
        visitNodeList( l );
        closeContext();
    }
}

void ContextBuilder::visitClassDefinition( ClassDefinitionAst* node )
{
    openContext( node, DUContext::Class, identifierForNode( node->name ) );
    addImportedContexts();
    visitNodeList( node->baseClasses );
    visitNodeList( node->body );
    closeContext();
}

void ContextBuilder::visitArguments(ArgumentsAst* node)
{
    AstDefaultVisitor::visitArguments(node);
}

void ContextBuilder::visitCode(CodeAst* node) {
    AstDefaultVisitor::visitCode(node);
    DUChainWriteLocker lock(DUChain::lock());
    TopDUContext* internal = DUChain::self()->chainForDocument(KUrl("/home/sven/projects/kde4/python/documentation/test.py"));
    if ( internal ) {
        currentContext()->addImportedParentContext(internal);
    }
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
            currentContext()->addImportedParentContext(moduleChain);
        }
    }
    Python::AstDefaultVisitor::visitImport(node);
}

void ContextBuilder::visitFunctionDefinition( FunctionDefinitionAst* node )
{
    kDebug() << " Building function definition context: " << node->name->value;
    ClassDefinitionAst* classast = dynamic_cast<ClassDefinitionAst*>( node->parent );

    if ( classast ) m_importedParentContexts.append( currentContext() );

    visitNodeList( node->decorators );

    if ( node->arguments )
    {
        DUContext* funcctx = openContext( node->arguments, node->arguments, DUContext::Function, identifierForNode( node->name ) );
        addImportedContexts();
        visitNode( node->arguments );
        closeContext();
        m_importedParentContexts.append( funcctx );
    }

    openContextForStatementList( node->body );
    m_importedParentContexts.clear();
}

// void ContextBuilder::visitFor( ForAst* node )
// {
//     DUContext* forctx = openContext( node, KDevelop::DUContext::Other );
//     visitNode(node->target);
//     closeContext();
// 
//     visitNode(node->iterator);
// 
//     m_importedParentContexts = QList<DUContext*>() << forctx;
//     openContextForStatementList( node->body );
//     openContextForStatementList( node->orelse );
//     m_importedParentContexts.clear();
// }

// void ContextBuilder::visitWhile( WhileAst* node )
// {
//     visitNode( node->condition );
//     openContextForStatementList( node->body );
//     openContextForStatementList( node->orelse );
// }

void ContextBuilder::visitWith( WithAst * node )
{
    m_importedParentContexts = QList<DUContext*>() << openContext( node->contextExpression, DUContext::Other );
    visitNode( node->contextExpression );
    closeContext();

    openContextForStatementList( node->body );
    m_importedParentContexts.clear();
}

// void ContextBuilder::visitTry( TryAst* node )
// {
//     kDebug() << "creating contexts for try";
//     openContextForStatementList( node->tryBody );
//     visitNodeList( node->exceptions );
//     openContextForStatementList( node->elseBody );
//     openContextForStatementList( node->finallyBody );
// }

// void ContextBuilder::visitIf( IfAst* node )
// {
//     visitNode( node->condition );
//     openContextForStatementList( node->body );
//     
//     foreach ( StatementAst* current, node->body) {
//         visitNode(current);
//     }
// 
//     openContextForStatementList( node->orelse );
// }

}
