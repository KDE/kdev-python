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
#ifndef CONTEXTBUILDER_H
#define CONTEXTBUILDER_H

#include "astdefaultvisitor.h"

#include <QSet>
#include <QHash>
#include <QList>
#include <language/duchain/identifier.h>
#include <language/duchain/duchainpointer.h>
#include <language/duchain/ducontext.h>
#include <ksharedptr.h>

#include "pythonduchainexport.h"

namespace KDevelop
{
class DUChain;
class DUChainBase;
class DUContext;
class TopDUContext;
}

namespace Python
{

class EditorIntegrator;

class KDEVPYTHONDUCHAIN_EXPORT ContextBuilder: public Python::AstDefaultVisitor
{

public:
    ContextBuilder();
    ContextBuilder( EditorIntegrator* editor );
    virtual ~ContextBuilder();

    KDevelop::TopDUContext* buildContexts( const KUrl& url, Ast* node, const KDevelop::TopDUContextPointer& updateContext = KDevelop::TopDUContextPointer() );
    KDevelop::DUContext* buildSubContexts( const KUrl& url, Ast* node, KDevelop::DUContext* parent = 0 );
    void supportBuild( Ast *node, KDevelop::DUContext* context = 0 );
    
protected:
    void smartenContext( KDevelop::TopDUContext* topLevelContext );
    KDevelop::DUContext* currentContext();

    void setEncountered( KDevelop::DUChainBase* item );

    bool wasEncountered( KDevelop::DUChainBase* item );


    virtual void openContext( KDevelop::DUContext* newContext );
    virtual void closeContext();
    bool recompiling() const;

    QSet<KDevelop::DUChainBase*> m_encountered;
    QStack<KDevelop::DUContext*> m_contextStack;
    int m_nextContextIndex;

    const KDevelop::QualifiedIdentifier identifierForName( IdentifierAst* );

    KDevelop::DUContext* openContext( Ast* range, KDevelop::DUContext::ContextType type, const KDevelop::QualifiedIdentifier& identifier );
    KDevelop::DUContext* openContext( Ast* range, KDevelop::DUContext::ContextType type, IdentifierAst* = 0 );
    KDevelop::DUContext* openContext( Ast* fromRange, Ast* toRange, KDevelop::DUContext::ContextType type, const KDevelop::QualifiedIdentifier& identifier = KDevelop::QualifiedIdentifier() );
    KDevelop::DUContext* openContextInternal( const KDevelop::SimpleRange& range, KDevelop::DUContext::ContextType type, const KDevelop::QualifiedIdentifier& identifier );

    virtual void visitFunctionDefinition( FunctionDefinitionAst* );
    virtual void visitClassDefinition( ClassDefinitionAst* );
    virtual void visitFor( ForAst* node );
    virtual void visitWith( WithAst* node );
    virtual void visitWhile( WhileAst* node );
    virtual void visitIf( IfAst* node );
    virtual void visitTry( TryAst* node );
    void addImportedContexts();

    template <typename T> void visitNodeList( const QList<T*>& l )
    {
        typename QList<T*>::ConstIterator it, end = l.end();

        for ( it = l.begin(); it != end; ++it )
        {
            visitNode(( *it ) );
        }
    }

protected:
    EditorIntegrator* m_editor;
    
    bool m_ownsEditorIntegrator: 1;
    
    bool m_compilingContexts: 1;
    
    bool m_recompiling : 1;

    QStack<int> m_nextContextStack;
    int& nextContextIndex();

    KDevelop::Identifier m_identifier;
    KDevelop::QualifiedIdentifier m_qidentifier;

    KDevelop::DUContext* m_lastContext;

    QList<KDevelop::DUContext*> m_importedParentContexts;

private:
    void openContextForStatementList( const QList<StatementAst*>& );
};

}

#endif
