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

#include <language/duchain/builders/abstractcontextbuilder.h>
#include <language/editor/rangeinrevision.h>
#include <language/duchain/topducontext.h>

#include "pythonduchainexport.h"
#include "pythonducontext.h"

using namespace KDevelop;

namespace Python
{
    
typedef QPair<QString, TopDUContextPointer> moduleContextTuple;

class PythonEditorIntegrator;
class ParseSession;

typedef KDevelop::AbstractContextBuilder<Ast, Identifier> ContextBuilderBase;

class KDEVPYTHONDUCHAIN_EXPORT ContextBuilder: public ContextBuilderBase, public Python::AstDefaultVisitor
{
public:
    void setEditor(PythonEditorIntegrator* editor);
    void setEditor(ParseSession* session);
    
    KUrl findModulePath(const QString& name);

protected:
    PythonEditorIntegrator* editor() const;

    virtual void startVisiting( Ast* node );
    virtual void setContextOnNode( Ast* node, KDevelop::DUContext* context );
    virtual KDevelop::DUContext* contextFromNode( Ast* node );
    virtual KDevelop::RangeInRevision editorFindRange( Ast* fromNode, Ast* toNode );
    virtual KDevelop::QualifiedIdentifier identifierForNode( Identifier* node );

    void addImportedContexts();

    virtual void visitFunctionDefinition( FunctionDefinitionAst* );
    virtual void visitClassDefinition( ClassDefinitionAst* );
//     virtual void visitFor( ForAst* node );
    virtual void visitWith( WithAst* node );
//     virtual void visitWhile( WhileAst* node );
//     virtual void visitIf( IfAst* node );
    virtual void visitArguments(ArgumentsAst* node);
    virtual void visitCode(CodeAst* node);
    virtual void visitImport(ImportAst* node);
    virtual void visitImportFrom(ImportFromAst* node);
    
    DUContext* openSafeContext( Python::Ast* node, RangeInRevision& range, DUContext::ContextType type, Python::Identifier* identifier = 0 );
    
    QMap<QString, TopDUContextPointer> contextsForModules;

    static PythonEditorIntegrator* m_editor;
    
    TopDUContext* newTopContext(const RangeInRevision& range, ParsingEnvironmentFile* file);
    virtual KDevelop::DUContext* newContext(const KDevelop::RangeInRevision& range);

    template <typename T> void visitNodeList( const QList<T*>& l )
    {
        typename QList<T*>::ConstIterator it, end = l.end();

        for ( it = l.begin(); it != end; ++it )
        {
            visitNode(( *it ) );
        }
    }
    
    bool m_mapAst;
    ReferencedTopDUContext m_topContext;

private:
    void openContextForStatementList( const QList<Ast*>&, DUContext::ContextType type = DUContext::Other);

    QList<KDevelop::DUContext*> m_importedParentContexts;
};

}

#endif
