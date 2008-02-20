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


ContextBuilder::ContextBuilder()
        : m_editor( new EditorIntegrator )
        , m_ownsEditorIntegrator( true )
        , m_compilingContexts( false )
        , m_recompiling( false )
        , m_lastContext( 0 )
{

}

ContextBuilder::ContextBuilder( EditorIntegrator* editor )
        : m_editor( editor )
        , m_ownsEditorIntegrator( false )
        , m_compilingContexts( false )
        , m_recompiling( false )
        , m_lastContext( 0 )
{
}


ContextBuilder::~ContextBuilder()
{
    if ( m_ownsEditorIntegrator )
        delete m_editor;
}

TopDUContext* ContextBuilder::buildContexts( const KUrl& url, Ast* node, const TopDUContextPointer& updateContext )
{
    m_compilingContexts = true;
    m_editor->setCurrentUrl( KDevelop::HashedString( url.prettyUrl() ) );

    TopDUContext* topLevelContext = 0;
    {
        DUChainWriteLocker lock( DUChain::lock() );
        topLevelContext = updateContext.data();

        if ( topLevelContext && !topLevelContext->smartRange() && m_editor->smart() )
        {
            lock.unlock();
            smartenContext( topLevelContext );
            lock.lock();
            topLevelContext = updateContext.data();
        }

        if ( topLevelContext && topLevelContext->smartRange() )
        {
            if ( topLevelContext->smartRange()->parentRange() )
            {
                //Top range must not have a parent, else something is wrong with the structure
                kDebug() << *topLevelContext->smartRange() << "has a parent" << *topLevelContext->smartRange()->parentRange();
                Q_ASSERT( false );
            }
        }

        if ( topLevelContext )
        {
            kDebug() << "ContextBuilder::buildContexts: recompiling";
            m_recompiling = true;

            if ( m_compilingContexts )
            {
                if ( m_editor->currentDocument() && m_editor->smart() && topLevelContext->range().textRange() != m_editor->currentDocument()->documentRange() )
                {
                    topLevelContext->setRange( SimpleRange( m_editor->currentDocument()->documentRange() ) );
                    kDebug() << "WARNING: Top-level context has Changed Ranges.";
                }
            }
        }
        else
        {
            kDebug() << "ContextBuilder::buildContexts: compiling";
            m_recompiling = false;
            Q_ASSERT( m_compilingContexts );
            topLevelContext = new TopDUContext( m_editor->currentUrl(), m_editor->currentDocument() ? SimpleRange( m_editor->currentDocument()->documentRange() ) : SimpleRange( SimpleCursor( 0, 0 ), SimpleCursor( INT_MAX, INT_MAX ) ) );
            topLevelContext->setSmartRange( m_editor->topRange( EditorIntegrator::DefinitionUseChain ) , DocumentRangeObject::Own );
            topLevelContext->setType( DUContext::Global );
            DUChain::self()->addDocumentChain( IdentifiedFile( url, 0 ), topLevelContext );
        }

        setEncountered( topLevelContext );

        node->context = topLevelContext;
    }

    supportBuild( node );

    if ( m_editor->currentDocument() && m_editor->smart() && topLevelContext->range().textRange() != m_editor->currentDocument()->documentRange() )
    {
        kDebug() << "WARNING: top level context has wrong size:" << topLevelContext->range().textRange() << "should be:" << m_editor->currentDocument()->documentRange();
        topLevelContext->setRange( m_editor->currentDocument()->documentRange() );
    }
    
    {
        DUChainReadLocker lock( DUChain::lock() );
        //foreach(DUContext* context, topLevelContext->childContexts());
        kDebug() << "built top-level context with" << topLevelContext->localDeclarations().count() << "declarations," << topLevelContext->localDefinitions().count() << " Definitions and" << topLevelContext->childContexts().size() << "Child-Contexts";

        if ( m_recompiling )
        {
            DumpChain dump;
            dump.dump( topLevelContext );
        }

        foreach( DUContext* contexts, topLevelContext->childContexts() )
            kDebug() << "CHILD:" << contexts->scopeIdentifier( true ) << "Parent:" << ( dynamic_cast<TopDUContext*>( contexts->parentContext() ) ? "top-context" : "" );
    }

    m_compilingContexts = false;
    return topLevelContext;
}

KDevelop::DUContext* ContextBuilder::buildSubContexts( const KUrl& url, Ast *node, KDevelop::DUContext* parent )
{
//     m_compilingContexts = true;
//     m_recompiling = false;
    m_editor->setCurrentUrl( HashedString( url.prettyUrl() ) );
    node->context = parent;
    {
        openContext( node->context );
        m_editor->setCurrentRange( m_editor->topRange( EditorIntegrator::DefinitionUseChain ) );
        visitNode( node );
        closeContext();
    }

    m_compilingContexts = false;

    if ( node->context == parent )
    {
        kDebug() << "Error in ContextBuilder::buildSubContexts(...): du-context was not replaced with new one";
        DUChainWriteLocker lock( DUChain::lock() );
        delete node->context;
        node->context = 0;
    }

    return node->context;
}

void ContextBuilder::supportBuild( Ast *node, DUContext* context )
{
    if( !context )
    {
        context = node->context;
    }
    
    if( TopDUContext* topLevelContext = dynamic_cast<TopDUContext*>( context ) )
    {
        smartenContext( topLevelContext );
    }

    openContext( context ? context : node->context );

    m_editor->setCurrentUrl( currentContext()->url() );
    m_editor->setCurrentRange( currentContext()->smartRange() );
    visitNode( node );
    closeContext();
    Q_ASSERT( m_contextStack.isEmpty() );
}

void ContextBuilder::openContext( DUContext* newContext )
{
    m_contextStack.push( newContext );
    m_nextContextStack.push( 0 );
}

DUContext* ContextBuilder::openContext( Ast* rangeNode, DUContext::ContextType type, IdentifierAst* identifier )
{
    if ( m_compilingContexts )
    {
        DUContext* ret = openContextInternal( m_editor->findRange( rangeNode ), type, identifier ? identifierForName( identifier ) : QualifiedIdentifier() );
        rangeNode->context = ret;
        return ret;
    }
    else
    {
        openContext( rangeNode->context );
        m_editor->setCurrentRange( currentContext()->smartRange() );
        return currentContext();
    }
}

DUContext* ContextBuilder::openContext( Ast* rangeNode, DUContext::ContextType type, const QualifiedIdentifier& identifier )
{
    if ( m_compilingContexts )
    {
        //kDebug() << "Opening ContextInternal";
        DUContext* ret = openContextInternal( m_editor->findRange( rangeNode ), type, identifier );
        //kDebug() << "Associating context" ;
        rangeNode->context = ret;
        return ret;
    }
    else
    {
        //kDebug() << "Opening Context associated with node";
        openContext( rangeNode->context );
        m_editor->setCurrentRange( currentContext()->smartRange() );
        return currentContext();
    }
}

DUContext* ContextBuilder::openContext( Ast* fromRange, Ast* toRange, DUContext::ContextType type, const QualifiedIdentifier& identifier )
{
    if ( m_compilingContexts )
    {
        DUContext* ret = openContextInternal( m_editor->findRange( fromRange, toRange ), type, identifier );
        fromRange->context = ret;
        return ret;
    }
    else
    {
        openContext( fromRange->context );
        m_editor->setCurrentRange( currentContext()->smartRange() );
        return currentContext();
    }
}

DUContext* ContextBuilder::openContextInternal( const SimpleRange& range, DUContext::ContextType type, const QualifiedIdentifier& identifier )
{
    kDebug() << "OpenContextInternal";
    Q_ASSERT( m_compilingContexts );
    DUContext* ret = 0L;
    {
        DUChainReadLocker readLock( DUChain::lock() );

        if ( recompiling() )
        {
            const QList<DUContext*>& childContexts = currentContext()->childContexts();
            QMutexLocker lock( m_editor->smart() ? m_editor->smart()->smartMutex() : 0 );
            SimpleRange translated = range;

            if ( m_editor->smart() )
                translated = SimpleRange( m_editor->smart()->translateFromRevision( translated.textRange() ) );

            if ( !childContexts.count() )
                kDebug() << "------No Child Contexts while Recompiling-----";

            for ( ; nextContextIndex() < childContexts.count(); ++nextContextIndex() )
            {
                DUContext* child = childContexts.at( nextContextIndex() );

                if ( child->range().start > translated.end && child->smartRange() )
                    break;

                if ( child->type() == type && child->localScopeIdentifier() == identifier && child->range() == translated )
                {
                    ret = child;
                    readLock.unlock();
                    DUChainWriteLocker writeLock( DUChain::lock() );

                    ret->clearImportedParentContexts();
                    m_editor->setCurrentRange( ret->smartRange() );
                    break;
                }
            }
        }

        if ( !ret )
        {
            readLock.unlock();
            DUChainWriteLocker writeLock( DUChain::lock() );

            if ( !currentContext() )
                kDebug() << "Current Context is Empty, need to Create a New One";

            ret = new DUContext( m_editor->currentUrl(), SimpleRange( range ), m_contextStack.isEmpty() ? 0 : currentContext() );

            ret->setSmartRange( m_editor->createRange( range.textRange() ), DocumentRangeObject::Own );

            ret->setType( type );

            if ( !identifier.isEmpty() )
            {
                ret->setLocalScopeIdentifier( identifier );

                if ( type == DUContext::Class )
                    SymbolTable::self()->addContext( ret );
            }
        }
    }

    setEncountered( ret );
    openContext( ret );
    return ret;
}

void ContextBuilder::closeContext()
{
    {
        DUChainWriteLocker lock( DUChain::lock() );
        currentContext()->cleanIfNotEncountered( m_encountered, m_compilingContexts );
        setEncountered( currentContext() );
    }

    m_lastContext = currentContext();
    m_contextStack.pop();
    m_nextContextStack.pop();
    m_editor->exitCurrentRange();
}

const QualifiedIdentifier ContextBuilder::identifierForName( IdentifierAst* name )
{
    m_identifier = Identifier( name->identifier );
    m_qidentifier.clear();
    m_qidentifier.push( m_identifier );
    return m_qidentifier;
}

void ContextBuilder::addImportedContexts()
{
    if ( m_compilingContexts && !m_importedParentContexts.isEmpty() )
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

void ContextBuilder::setEncountered( KDevelop::DUChainBase* item )
{
    m_encountered.insert( item );
}

bool ContextBuilder::wasEncountered( KDevelop::DUChainBase* item )
{
    return m_encountered.contains( item );
}

KDevelop::DUContext * ContextBuilder::currentContext( )
{
    return m_contextStack.top();
}

bool ContextBuilder::recompiling( ) const
{
    return m_recompiling;
}

int& ContextBuilder::nextContextIndex()
{
    return m_nextContextStack.top();
}

void ContextBuilder::smartenContext( TopDUContext* topLevelContext )
{
    if ( topLevelContext && !topLevelContext->smartRange() && m_editor->smart() )
    {
        SmartConverter conv( m_editor, 0 );
        conv.convertDUChain( topLevelContext );
    }
}

void ContextBuilder::visitClassDefinition( ClassDefinitionAst* node )
{
    kDebug() << "Visiting Class Declaration";
    openContext( node, DUContext::Class, identifierForName( node->className ) );
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
        DUContext* funcctx = openContext( node->parameters.first(), node->parameters.last(), DUContext::Function, identifierForName( node->functionName ) );
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
