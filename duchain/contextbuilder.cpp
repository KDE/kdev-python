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
#include <language/duchain/duchain.h>
#include <language/duchain/duchainlock.h>
#include <language/duchain/topducontext.h>
#include <language/duchain/parsingenvironment.h>
#include <ktexteditor/smartrange.h>
#include <ktexteditor/smartinterface.h>
#include <ktexteditor/document.h>
#include <language/duchain/smartconverter.h>
#include <language/duchain/symboltable.h>
#include "pythoneditorintegrator.h"
#include "dumpchain.h"

using namespace KDevelop;

using namespace KTextEditor;

namespace Python
{

EditorIntegrator* ContextBuilder::editor() const
{
    return static_cast<EditorIntegrator*>(ContextBuilderBase::editor());
}

void ContextBuilder::setEditor(EditorIntegrator* editor)
{
    //m_identifierCompiler = new IdentifierCompiler(editor->parseSession());
    ContextBuilderBase::setEditor(editor, false);
}

void ContextBuilder::setEditor(ParseSession* session)
{
    EditorIntegrator* e = new EditorIntegrator(/*session*/);
    //m_identifierCompiler = new IdentifierCompiler(e->parseSession());
    ContextBuilderBase::setEditor(e, true);
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

KTextEditor::Range ContextBuilder::editorFindRange( Ast* fromNode, Ast* toNode )
{
    return editor()->findRange(fromNode, toNode);
}

QualifiedIdentifier ContextBuilder::identifierForNode( IdentifierAst* node )
{
    return QualifiedIdentifier( node->identifier );
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
    openContext( node, DUContext::Class, identifierForNode( node->className ) );
    addImportedContexts();
    visitNodeList( node->inheritance );
    visitNodeList( node->classBody );
    closeContext();
}

void ContextBuilder::visitFunctionDefinition( FunctionDefinitionAst* node )
{
    kDebug() << "building function definition context";
    ClassDefinitionAst* classast = dynamic_cast<ClassDefinitionAst*>( node->parent );

    if ( classast )
    {
        DUChainReadLocker lock( DUChain::lock() );
        QList<DUContext*> classContexts = currentContext()->findContexts( DUContext::Class, QualifiedIdentifier( classast->context->localScopeIdentifier() ) );

        if ( classContexts.count() != 1 )
        {
            m_importedParentContexts.append( classContexts.first() );
        }

        if ( classContexts.count() > 1 )
        {
            kWarning() << "Multiple class contexts for" << classast->className->identifier << classast->context->localScopeIdentifier() << "shouldn't happen!";
            foreach( DUContext* classContext, classContexts )
            {
                kDebug() << "Context" << classContext->scopeIdentifier( true ) << "range" << classContext->range().textRange() << "in" << classContext->url().str();
            }
        }
    }

    visitNodeList( node->decorators );

    if ( node->parameters.count() > 0 )
    {
        DUContext* funcctx = openContext( node->parameters.first(), node->parameters.last(), DUContext::Function, identifierForNode( node->functionName ) );
        addImportedContexts();
        visitNodeList( node->parameters );
        closeContext();
        m_importedParentContexts.append( funcctx );
    }

    openContextForStatementList( node->functionBody );
    m_importedParentContexts.clear();
}

void ContextBuilder::visitFor( ForAst* node )
{
    kDebug() << "Found for, building context";
    DUContext* forctx = openContext( node->assignedTargets.first(), node->assignedTargets.last(), DUContext::Other );
    visitNodeList( node->assignedTargets );
    closeContext();

    visitNodeList( node->iterable );

    m_importedParentContexts = QList<DUContext*>() << forctx;
    openContextForStatementList( node->forBody );
    openContextForStatementList( node->elseBody );
    m_importedParentContexts.clear();
}

void ContextBuilder::visitWhile( WhileAst* node )
{
    kDebug() << "Creating contexts for while";
    visitNode( node->condition );
    openContextForStatementList( node->whileBody );
    openContextForStatementList( node->elseBody );
}

void ContextBuilder::visitWith( WithAst * node )
{
    kDebug() << "creating contexts for With";

    m_importedParentContexts = QList<DUContext*>() << openContext( node->name, DUContext::Other );
    visitNode( node->name );
    closeContext();

    openContextForStatementList( node->body );
    m_importedParentContexts.clear();
}

void ContextBuilder::visitTry( TryAst* node )
{
    kDebug() << "creating contexts for try";
    openContextForStatementList( node->tryBody );
    visitNodeList( node->exceptions );
    openContextForStatementList( node->elseBody );
    openContextForStatementList( node->finallyBody );
}

void ContextBuilder::visitIf( IfAst* node )
{
    kDebug() << "creating contexts for if";
    visitNode( node->ifCondition );
    openContextForStatementList( node->ifBody );
    QList< QPair< ExpressionAst*, QList<StatementAst*> > >::ConstIterator it, end = node->elseIfBodies.end();

    for ( it = node->elseIfBodies.begin(); it != end; ++it )
    {
        visitNode( ( *it ).first );
        openContextForStatementList( ( *it ).second );
    }

    openContextForStatementList( node->elseBody );
}

}
