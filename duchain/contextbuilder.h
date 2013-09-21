/*****************************************************************************
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 * Copyright 2007 Andreas Pakulat <apaku@gmx.de>                             *
 * Copyright (c) 2010-2013 Sven Brauch <svenbrauch@googlemail.com>           *
 *                                                                           *
 * This program is free software; you can redistribute it and/or             *
 * modify it under the terms of the GNU General Public License as            *
 * published by the Free Software Foundation; either version 2 of            *
 * the License, or (at your option) any later version.                       *
 *                                                                           *
 * This program is distributed in the hope that it will be useful,           *
 * but WITHOUT ANY WARRANTY; without even the implied warranty of            *
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             *
 * GNU General Public License for more details.                              *
 *                                                                           *
 * You should have received a copy of the GNU General Public License         *
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.     *
 *****************************************************************************
 */
#ifndef CONTEXTBUILDER_H
#define CONTEXTBUILDER_H

#include "astdefaultvisitor.h"

#include <language/duchain/builders/abstractcontextbuilder.h>
#include <language/editor/rangeinrevision.h>
#include <language/duchain/topducontext.h>

#include "codehelpers.h"
#include "pythonduchainexport.h"
#include "pythonducontext.h"
#include "pythoneditorintegrator.h"

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
    ContextBuilder();
    virtual ReferencedTopDUContext build(const KDevelop::IndexedString& url, Ast* node,
                                         ReferencedTopDUContext updateContext = ReferencedTopDUContext());

    void setEditor(PythonEditorIntegrator* editor);
    void setEditor(ParseSession* session);
    
    // those functions can be used if you want to do something to a context you are in,
    // but which is not the current one. Example: You want to add a variable to a class context,
    // but the current context is inside that class context (method declaration, ...)
    bool contextAlreayOpen(DUContextPointer context);
    void activateAlreadyOpenedContext(DUContextPointer context);
    void closeAlreadyOpenedContext(DUContextPointer context);
    QList<DUContextPointer> m_temporarilyClosedContexts;

    static QPair<KUrl, QStringList> findModulePath(const QString& name, const KUrl& currentDocument);
    
    // ugly because this collides with currentDocument(), but we have to use it;
    // for some reason the UseBuilder does not have m_url set, and it's private (not even protected) to AbstractContextBuilder.
    // so at least keep this consistent within the plugin and use this everywhere.
    // maybe we can remove this hack later. TODO maybe change something in kdevplatform, or maybe we're doing something wrong here?
    IndexedString currentlyParsedDocument() const;
    IndexedString m_currentlyParsedDocument;
    QList<IndexedString> m_unresolvedImports;
    static RangeInRevision rangeForNode(Ast* node, bool moveRight);
    static RangeInRevision rangeForNode(Identifier* node, bool moveRight);
    static SimpleRange simpleRangeForNode(Python::Ast* node, bool moveRight);
    ModificationRevision m_futureModificationRevision;
    bool m_prebuilding;

protected:
    PythonEditorIntegrator* editor() const;

    virtual void startVisiting( Ast* node );
    virtual void setContextOnNode( Ast* node, KDevelop::DUContext* context );
    virtual KDevelop::DUContext* contextFromNode( Ast* node );
    virtual KDevelop::RangeInRevision editorFindRange( Ast* fromNode, Ast* toNode );
    virtual KDevelop::CursorInRevision editorFindPositionSafe(Ast* node);
    virtual KDevelop::CursorInRevision startPos(Ast* node);
    virtual KDevelop::QualifiedIdentifier identifierForNode(Identifier* node);
    
    void addImportedContexts();

    virtual void visitFunctionDefinition( FunctionDefinitionAst* );
    virtual void visitClassDefinition( ClassDefinitionAst* );
    virtual void visitCode(CodeAst* node);
    virtual void visitLambda(LambdaAst* node);
    virtual void visitListComprehension(ListComprehensionAst* node);
    virtual void visitDictionaryComprehension(DictionaryComprehensionAst* node);
    virtual void visitGeneratorExpression(GeneratorExpressionAst* node);
    
    void visitComprehensionCommon(Ast* node);
    
    // helpers, because they need to be called seperately from DeclarationBuilder... well
    virtual void visitFunctionArguments(FunctionDefinitionAst* node);
    virtual void visitFunctionBody(FunctionDefinitionAst* node);
    void openContextForFunctionBody(FunctionDefinitionAst* node);
    void openContextForClassDefinition(ClassDefinitionAst* node);
    
    RangeInRevision rangeForArgumentsContext( Python::FunctionDefinitionAst* node);
    
    DUContext* openSafeContext( Python::Ast* node, RangeInRevision& range, DUContext::ContextType type, Python::Identifier* identifier = 0 );
    
    QMap<QString, ReferencedTopDUContext> contextsForModules;

    PythonEditorIntegrator* m_editor;
    
    TopDUContext* newTopContext(const RangeInRevision& range, ParsingEnvironmentFile* file);
    virtual KDevelop::DUContext* newContext(const KDevelop::RangeInRevision& range);

    template <typename T> void visitNodeList( const QList<T*>& l ) {
        foreach ( T* node, l ) {
            visitNode(node);
        }
    }
    
    bool m_mapAst;
    ReferencedTopDUContext m_topContext;
    DUContextPointer m_moduleContext;
    TopDUContextPointer m_builtinFunctionsContext;
    DUContextPointer m_mostRecentArgumentsContext;
    RangeInRevision m_lastGeneratorRange;

private:
    void openContextForStatementList( const QList<Ast*>&, DUContext::ContextType type = DUContext::Other);
    bool m_isScheduledForReparsing;
    RangeInRevision comprehensionRange(Ast* node);

    QList<KDevelop::DUContext*> m_importedParentContexts;
    QSharedPointer<FileIndentInformation> m_indentInformationCache;
};

}

#endif
