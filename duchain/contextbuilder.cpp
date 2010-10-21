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
#include <contextbuilder.h>
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

using namespace KDevelop;

using namespace KTextEditor;

namespace Python
{

PythonEditorIntegrator* ContextBuilder::editor() const
{
//     return static_cast<EditorIntegrator*>(ContextBuilderBase::editor());
    return m_editor;
}

TopDUContext* ContextBuilder::newTopContext(const RangeInRevision& range, ParsingEnvironmentFile* file) 
{
    IndexedString currentDocumentUrl = m_editor->parseSession()->currentDocument();
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
    m_editor = editor;
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
        kDebug() << "Adding Imported Contexts";
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
        openContext( l.first(), l.last(), DUContext::Other );
        addImportedContexts();
        visitNodeList( l );
        closeContext();
    }
}

void ContextBuilder::visitClassDefinition( ClassDefinitionAst* node )
{
    kDebug() << "Visiting Class Declaration";
    openContext( node, DUContext::Class, identifierForNode( node->name ) );
    addImportedContexts();
    visitNodeList( node->baseClasses );
    visitNodeList( node->body );
    closeContext();
}

void ContextBuilder::visitFunctionDefinition( FunctionDefinitionAst* node )
{
    kDebug() << "building function definition context";
    kDebug() << node->startLine;
    ClassDefinitionAst* classast = dynamic_cast<ClassDefinitionAst*>( node->parent );

    if ( classast )
    {
//         DUChainReadLocker lock( DUChain::lock() );
//         QList<DUContext*> classContexts = currentContext()->findContexts( DUContext::Class, QualifiedIdentifier( classast->context->localScopeIdentifier(). ) );

//         if ( classContexts.count() != 1 )
//         {
//             m_importedParentContexts.append( classContexts.first() );
               m_importedParentContexts.append( currentContext() );
//         }

//         if ( classContexts.count() > 1 )
//         {
//             kWarning() << "Multiple class contexts for" << classast->className->identifier << classast->context->localScopeIdentifier() << "shouldn't happen!";
//             foreach( DUContext* classContext, classContexts )
//             {
//                 kDebug() << "Context" << classContext->scopeIdentifier( true ) << "range" << classContext->range().textRange() << "in" << classContext->url().str();
//             }
//         }
    }

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

void ContextBuilder::visitFor( ForAst* node )
{
    kDebug() << "Found for, building context";
    DUContext* forctx = openContext( node, KDevelop::DUContext::Other );
    visitNode(node->target);
    closeContext();

    visitNode(node->iterator);

    m_importedParentContexts = QList<DUContext*>() << forctx;
    openContextForStatementList( node->body );
    openContextForStatementList( node->orelse );
    m_importedParentContexts.clear();
}

void ContextBuilder::visitWhile( WhileAst* node )
{
    kDebug() << "Creating contexts for while";
    visitNode( node->condition );
    openContextForStatementList( node->body );
    openContextForStatementList( node->orelse );
}

void ContextBuilder::visitWith( WithAst * node )
{
    kDebug() << "creating contexts for With";

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

void ContextBuilder::visitIf( IfAst* node )
{
    kDebug() << "creating contexts for if";
    visitNode( node->condition );
    openContextForStatementList( node->body );
    
    QList <Python::StatementAst* >::const_iterator it, end = node->body.constEnd();

    for ( it = node->body.begin(); it != end; ++it )
    {
        visitNode(*it);
    }

    openContextForStatementList( node->orelse );
}

}
