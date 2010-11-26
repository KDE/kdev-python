/*****************************************************************************
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 *   Copyright 2007 Andreas Pakulat <apaku@gmx.de>                           *
 *                                                                           *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
 * 02110-1301, USA.
 *****************************************************************************/
#ifndef CONTEXTBUILDER_H
#define CONTEXTBUILDER_H

#include "astdefaultvisitor.h"

#include <language/duchain/builders/abstractcontextbuilder.h>

#include "pythonduchainexport.h"

namespace Python
{

class EditorIntegrator;
class ParseSession;

typedef KDevelop::AbstractContextBuilder<Ast, IdentifierAst> ContextBuilderBase;

class KDEVPYTHONDUCHAIN_EXPORT ContextBuilder: public ContextBuilderBase, public Python::AstDefaultVisitor
{
public:
    void setEditor(EditorIntegrator* editor);
    void setEditor(ParseSession* session);

protected:
    EditorIntegrator* editor() const;

    virtual void startVisiting( Ast* node );
    virtual void setContextOnNode( Ast* node, KDevelop::DUContext* context );
    virtual KDevelop::DUContext* contextFromNode( Ast* node );
    virtual KTextEditor::Range editorFindRange( Ast* fromNode, Ast* toNode );
    virtual KDevelop::QualifiedIdentifier identifierForNode( IdentifierAst* node );

    void addImportedContexts();

    virtual void visitFunctionDefinition( FunctionDefinitionAst* );
    virtual void visitClassDefinition( ClassDefinitionAst* );
    virtual void visitFor( ForAst* node );
    virtual void visitWith( WithAst* node );
    virtual void visitWhile( WhileAst* node );
    virtual void visitIf( IfAst* node );
    virtual void visitTry( TryAst* node );

    template <typename T> void visitNodeList( const QList<T*>& l )
    {
        typename QList<T*>::ConstIterator it, end = l.end();

        for ( it = l.begin(); it != end; ++it )
        {
            visitNode(( *it ) );
        }
    }

private:
    void openContextForStatementList( const QList<StatementAst*>& );

    QList<KDevelop::DUContext*> m_importedParentContexts;
};

}

#endif
