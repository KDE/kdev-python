/*****************************************************************************
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
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
#include <duchain.h>
#include <duchainlock.h>
#include <parsesession.h>
#include <topducontext.h>
#include "pythoneditorintegrator.h"
// #include "dumpchain.h"
#include <parsingenvironment.h>
#include <ktexteditor/smartrange.h>
#include <ktexteditor/smartinterface.h>
#include <ktexteditor/document.h>
#include <smartconverter.h>
#include <symboltable.h>

using namespace KDevelop;
using namespace KTextEditor;

namespace Python
{


ContextBuilder::ContextBuilder(ParseSession* session, const KUrl &url)
    :m_editor(new EditorIntegrator(session))
    ,m_session(session)
    ,m_url(url)
    ,m_ownsEditorIntegrator(true)
    ,m_compilingContexts(false)
    ,m_recompiling(false)
    ,m_lastContext(0)
{
    kDebug() << "*********Building Contexts for*******"<<m_url;

}
ContextBuilder::ContextBuilder (EditorIntegrator* editor, const KUrl &url)
    :m_editor(editor)
    ,m_url(url)
    ,m_ownsEditorIntegrator(false)
    ,m_compilingContexts(false)
    ,m_recompiling(false)
    ,m_lastContext(0)
{
    kDebug() << "*********Building Contexts for********"<<m_url;
}


ContextBuilder::~ContextBuilder ()
{
    if (m_ownsEditorIntegrator)
        delete m_editor;
}

TopDUContext* ContextBuilder::buildContexts(Ast* node)
{
    m_compilingContexts = true;
    m_editor->setCurrentUrl( KDevelop::HashedString( m_url.prettyUrl() ) );

    TopDUContext* topLevelContext = 0;
    {
        DUChainWriteLocker lock(DUChain::lock());
        topLevelContext = DUChain::self()->chainForDocument(m_url);
        if( topLevelContext && !topLevelContext->smartRange() && m_editor->smart() )
        {
            lock.unlock();
            SmartConverter conv(m_editor, 0);
            conv.convertDUChain(topLevelContext);
            lock.lock();
        }

        if (topLevelContext)
        {
            kDebug() << "ContextBuilder::buildContexts: recompiling";
            m_recompiling = true;
            if (m_compilingContexts)
            {
                if (m_editor->currentDocument() && m_editor->smart() && topLevelContext->range().textRange() != m_editor->currentDocument()->documentRange())
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
            Q_ASSERT(m_compilingContexts);
            topLevelContext = new TopDUContext(m_editor->currentUrl(), m_editor->currentDocument() ? SimpleRange(m_editor->currentDocument()->documentRange()) : SimpleRange(SimpleCursor(0,0), SimpleCursor(INT_MAX, INT_MAX)));
            topLevelContext->setSmartRange( m_editor->topRange( EditorIntegrator::DefinitionUseChain) , DocumentRangeObject::Own );
            topLevelContext->setType(DUContext::Global);
            DUChain::self()->addDocumentChain(IdentifiedFile( m_url, 0 ), topLevelContext);
        }

        setEncountered(topLevelContext);
        node->context = topLevelContext;
    }
    
    supportBuild(node);
    
    {
        // allDeclarations always returned Zero as it looks for the Total Number Of definitions, as Depicted here.
        // Currently it simply dispalys the localdeclarations in the topcontext,
        // def a():\n\tpass\ndef b():\n\tpass returns 2 Declarations.
        DUChainReadLocker lock(DUChain::lock());
        //foreach(DUContext* context, topLevelContext->childContexts());
        kDebug() << "built top-level context with" << topLevelContext->localDeclarations().count() << "declarations,"<<topLevelContext->localDefinitions().count()<<" Definitions and" << topLevelContext->childContexts().size() << "Child-Contexts";
        if( m_recompiling )
        {
//             DumpChain dump;
//             dump.dump(topLevelContext);
        }
        foreach(DUContext* contexts, topLevelContext->childContexts())
                kDebug()<<"CHILD:"<<contexts->scopeIdentifier(true)<<"Parent:"<<(dynamic_cast<TopDUContext*>(contexts->parentContext()) ? "top-context" : "");
    }
    m_compilingContexts = false;
    return topLevelContext;
}

KDevelop::DUContext* ContextBuilder::buildSubContexts(const KUrl& url, Ast *node, KDevelop::DUContext* parent)
{
    m_compilingContexts = true;
    m_recompiling = false;
    m_editor->setCurrentUrl( HashedString( url.prettyUrl() ) );
    node->context = parent;
    {
        openContext(node->context);
        m_editor->setCurrentRange(m_editor->topRange(EditorIntegrator::DefinitionUseChain ));
        visitNode(node);
        closeContext();
    }
    m_compilingContexts = false;
    if( node->context == parent )
    {
        kDebug() << "Error in ContextBuilder::buildSubContexts(...): du-context was not replaced with new one";
        DUChainWriteLocker lock(DUChain::lock());
        delete node->context;
        node->context = 0;
    }
    return node->context;
}

void ContextBuilder::supportBuild(Ast *node, DUContext* context)
{
    if(!node->context)
    {
        kDebug()<<"No Context Found matching with the node";
    }
    openContext( context ? context : node->context);
    m_editor->setCurrentUrl( currentContext()->url() );
    m_editor->setCurrentRange( currentContext()->smartRange() );
    visitNode(node);
    closeContext();
    Q_ASSERT(m_contextStack.isEmpty());
}

void ContextBuilder::visitClassDefinition( ClassDefinitionAst* node )
{
    kDebug()<<"Visiting Class Declaration";
    openContext(node, DUContext::Class, identifierForName( node->className->identifier ));
    addImportedContexts();
    visitNodeList( node->inheritance );
    visitNodeList(node->classBody);
    closeContext();
}
// void ContextBuilder::visit_import_as_name(import_as_name_ast *node)
// {
//     openContext(node, DUContext::Namespace , identifierForName(node->imported_as));
//     addImportedContexts();
//     closeContext();
// }
// 
// void ContextBuilder::visit_compound_stmt(compound_stmt_ast *node)
// {
//     if(!node->classdef && !node->fucdef && !node->try_stmt)
//     {
//         openContext(node, DUContext::Other);
//         addImportedContexts();
//         default_visitor::visit_compound_stmt(node);
//         closeContext();
//     }
//     else if(node->try_stmt)
//     {
//         QString name = "try";
//         m_identifier = Identifier(name);
//         KDevelop::QualifiedIdentifier x;
//         x.push(m_identifier);
//         openContext(node, DUContext::Other, x);
//         addImportedContexts();
//         default_visitor::visit_compound_stmt(node);
//         closeContext();
//         x.clear();
//     }
//     else
//     {
//         default_visitor::visit_compound_stmt(node);
//     }
// }

void ContextBuilder::visitFunctionDefinition( FunctionDefinitionAst* node )
{
    kDebug() << "building function definition context";
    ClassDefinitionAst* classast = dynamic_cast<ClassDefinitionAst*>( node->parent );
    if( classast ) 
    {
        DUChainReadLocker lock( DUChain::lock() );
        QList<DUContext*> classContexts = currentContext()->findContexts( DUContext::Class, QualifiedIdentifier( classast->context->localScopeIdentifier() ) );
        if( classContexts.count() == 1 )
        {
            m_importedParentContexts.append( classContexts.first() );
        }else if( classContexts.count() > 1 )
        {
            kWarning() << "Multiple class contexts for" << classast->className->identifier << classast->context->localScopeIdentifier() << "shouldn't happen!";
            foreach( DUContext* classContext, classContexts )
            {
                kDebug() << "Context" << classContext->scopeIdentifier( true ) << "range" << classContext->range().textRange() << "in" << classContext->url().str();
            }
        }
    }
    
    visitNodeList( node->decorators );
    if( node->parameters.count() > 0 )
    {
        openContext( node->parameters.first(), node->parameters.last(), DUContext::Other );
        addImportedContexts();
        visitNodeList( node->parameters );
        closeContext();
    }
    openContext( node->functionBody.first(), node->functionBody.last() ,DUContext::Function, identifierForName( node->functionName->identifier ) );
    addImportedContexts();
    visitNodeList( node->functionBody );
    closeContext();
    m_importedParentContexts.clear();
}

// void ContextBuilder::visit_varargslist(varargslist_ast *node)
// {
//     QString name = "arguements";
//     m_identifier = Identifier(name);
//     KDevelop::QualifiedIdentifier x;
//     x.push(m_identifier);
//     openContext(node,DUContext::Other, x);
//     addImportedContexts();
//     default_visitor::visit_varargslist(node);
//     closeContext();
//     x.clear();
// }

void ContextBuilder::openContext(DUContext* newContext)
{
    m_contextStack.push(newContext);
    m_nextContextStack.push(0);
}

DUContext* ContextBuilder::openContext(Ast* rangeNode, DUContext::ContextType type, const QString& identifier)
{
    if (m_compilingContexts)
    {
        DUContext* ret = openContextInternal(m_editor->findRange(rangeNode), type, !identifier.isEmpty() ? identifierForName(identifier) : QualifiedIdentifier());
        rangeNode->context = ret;
        return ret;
    }
    else
    {
        openContext( rangeNode->context );
        m_editor->setCurrentRange(currentContext()->smartRange());
        return currentContext();
    }
}

DUContext* ContextBuilder::openContext(Ast* rangeNode, DUContext::ContextType type, const QualifiedIdentifier& identifier)
{
    if (m_compilingContexts)
    {
        //kDebug() << "Opening ContextInternal";
        DUContext* ret = openContextInternal(m_editor->findRange(rangeNode), type, identifier);
        //kDebug() << "Associating context" ;
        rangeNode->context = ret;
        return ret;
    }
    else
    {
        //kDebug() << "Opening Context associated with node";
        openContext(rangeNode->context);
        m_editor->setCurrentRange(currentContext()->smartRange());
        return currentContext();
    }
}

DUContext* ContextBuilder::openContext(Ast* fromRange, Ast* toRange, DUContext::ContextType type, const QualifiedIdentifier& identifier)
{
    if (m_compilingContexts)
    {
        DUContext* ret = openContextInternal(m_editor->findRange(fromRange, toRange), type, identifier );
        fromRange->context = ret;
        return ret;
    }
    else
    {
        openContext(fromRange->context);
        m_editor->setCurrentRange(currentContext()->smartRange());
        return currentContext();
    }
}

DUContext* ContextBuilder::openContextInternal(const SimpleRange& range, DUContext::ContextType type, const QualifiedIdentifier& identifier)
{
    kDebug() << "OpenContextInternal";
    Q_ASSERT(m_compilingContexts);
    DUContext* ret = 0L;
    {
        DUChainReadLocker readLock(DUChain::lock());
        if (recompiling())
        {
            const QList<DUContext*>& childContexts = currentContext()->childContexts();
            QMutexLocker lock(m_editor->smart() ? m_editor->smart()->smartMutex() : 0);
            SimpleRange translated = range;
            if (m_editor->smart())
                translated = SimpleRange( m_editor->smart()->translateFromRevision( translated.textRange() ) );
            if(!childContexts.count())
                kDebug()<<"------No Child Contexts while Recompiling-----";
            for (; nextContextIndex() < childContexts.count(); ++nextContextIndex())
            {
                DUContext* child = childContexts.at(nextContextIndex());
                if (child->range().start > translated.end && child->smartRange())
                    break;
                if (child->type() == type && child->localScopeIdentifier() == identifier && child->range() == translated)
                {
                    ret = child;
                    readLock.unlock();
                    DUChainWriteLocker writeLock(DUChain::lock());
                    
                    ret->clearImportedParentContexts();
                    m_editor->setCurrentRange(ret->smartRange());
                    break;
                }
            }
        }
        if (!ret)
        {
            readLock.unlock();
            DUChainWriteLocker writeLock(DUChain::lock());
            if(!currentContext())
                kDebug()<<"Current Context is Empty, need to Create a New One";
            ret = new DUContext(m_editor->currentUrl(), SimpleRange(range), m_contextStack.isEmpty() ? 0 : currentContext());
            ret->setSmartRange( m_editor->createRange( range.textRange() ), DocumentRangeObject::Own );
            ret->setType(type);
            if (!identifier.isEmpty())
            {
                ret->setLocalScopeIdentifier(identifier);
                if (type == DUContext::Class)
                    SymbolTable::self()->addContext(ret);
            }
        }
    }
    setEncountered(ret);
    openContext(ret);
    return ret;
}

void ContextBuilder::closeContext()
{
    {
        DUChainWriteLocker lock(DUChain::lock());
        currentContext()->cleanIfNotEncountered(m_encountered, m_compilingContexts);
        setEncountered( currentContext() );
    }
    m_lastContext=currentContext();
    m_contextStack.pop();
    m_nextContextStack.pop();
    m_editor->exitCurrentRange();
}

void ContextBuilder::visitFor( ForAst* node )
{
    kDebug() << "Found for, building context";
    DUContext* forctx = openContext( node->assignedTargets.first(), node->iterable.first(), DUContext::Other );
    visitNodeList( node->assignedTargets );
    visitNodeList( node->iterable );
    closeContext();
    
    m_importedParentContexts = QList<DUContext*>() << forctx;
    if( node->forBody.count() > 0 )
    {
        openContext( node->forBody.first(), node->forBody.last(), DUContext::Other );
        addImportedContexts();
        visitNodeList( node->forBody );
        closeContext();
    }
    if( node->elseBody.count() > 0 )
    {
        openContext( node->elseBody.first(), node->elseBody.last(), DUContext::Other );
        addImportedContexts();
        visitNodeList( node->elseBody );
        closeContext();
    }
    m_importedParentContexts.clear();
}

void ContextBuilder::visitWhile( WhileAst* node )
{
    kDebug() << "Creating contexts for while";
    visitNode(node->condition);
    if( node->whileBody.count() > 0 )
    {
        openContext( node->whileBody.first(), node->whileBody.last(), DUContext::Other );
        addImportedContexts();
        visitNodeList( node->whileBody );
        closeContext();
    } else if( node->elseBody.count() > 0 )
    {
        openContext( node->elseBody.first(), node->elseBody.last(), DUContext::Other );
        addImportedContexts();
        visitNodeList( node->elseBody );
        closeContext();
    }
    m_importedParentContexts.clear();
}

const QualifiedIdentifier ContextBuilder::identifierForName( const QString& name )
{
    m_identifier = Identifier(name);
    m_qidentifier.clear();
    m_qidentifier.push(m_identifier);
    return m_qidentifier;
}

void ContextBuilder::addImportedContexts()
{
    if (m_compilingContexts && !m_importedParentContexts.isEmpty())
    {
        kDebug()<<"Adding Imported Contexts";
        DUChainWriteLocker lock(DUChain::lock());
        foreach (DUContext* imported, m_importedParentContexts)
            currentContext()->addImportedParentContext(imported);

        m_importedParentContexts.clear();
    }
}

}

void Python::ContextBuilder::visitWith( WithAst * node )
{
    kDebug() << "creating contexts for With";
    
    if( node->body.count() > 0 )
    {
        openContext( node->body.first(), node->body.last(), DUContext::Other );
        visitNodeList( node->body );
        closeContext();
    }
}
