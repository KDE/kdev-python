/*****************************************************************************
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 * Copyright 2007 Andreas Pakulat <apaku@gmx.de>                             *
 * Copyright (c) 2010-2014 Sven Brauch <svenbrauch@googlemail.com>           *
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
#ifndef PYTHON_CONTEXTBUILDER_H
#define PYTHON_CONTEXTBUILDER_H

#include "astdefaultvisitor.h"

#include <language/duchain/builders/abstractcontextbuilder.h>
#include <language/editor/rangeinrevision.h>
#include <language/duchain/topducontext.h>

#include "pythonduchainexport.h"

using namespace KDevelop;

namespace Python
{

class PythonEditorIntegrator;
class FileIndentInformation;

typedef KDevelop::AbstractContextBuilder<Ast, Identifier> ContextBuilderBase;

/**
 * @brief The context builder, which calculates the scopes in a file.
 *
 * For practical reasons, some building of scopes also happens
 * in the declaration builder.
 */
class KDEVPYTHONDUCHAIN_EXPORT ContextBuilder: public ContextBuilderBase, public Python::AstDefaultVisitor
{
public:
    ContextBuilder() = default;

    /**
     * @brief Entry function called by KDevPlatform API.
     */
    ReferencedTopDUContext build(const KDevelop::IndexedString& url, Ast* node,
                                         ReferencedTopDUContext updateContext = ReferencedTopDUContext()) override;

    /**
     * @brief Set the editor integrator.
     */
    void setEditor(PythonEditorIntegrator* editor);

    /**
     * @brief Set the modification revision which will be created by this builder.
     */
    void setFutureModificationRevision(const ModificationRevision& rev);

    /**
     * @brief Get the editor integrator.
     */
    PythonEditorIntegrator* editor() const;

    /**
     * @brief Find the URL which would be imported by the dotted name @p name.
     *
     * @param name a dotted name, such as PyQt4.QtCore.QWidget
     * @param currentDocument the current document, for resolving relative imports
     * @return QPair< QUrl, QStringList > the URL if found, and a list of components from
     *  the end of the name which were not yet consumed
     */
    static QPair<QUrl, QStringList> findModulePath(const QString& name, const QUrl& currentDocument);

    /**
     * @brief Get the range which encompasses the given @p node.
     * @param moveRight true to make the range longer by one character
     */
    static RangeInRevision rangeForNode(Ast* node, bool moveRight);

    /**
     * @brief Get the range of @p identifier.
     * @param moveRight true to make the range longer by one character
     */
    static RangeInRevision rangeForNode(Identifier* identifier, bool moveRight);

    /**
     * @brief Find the range of a comprehension.
     * @param node Comprehension to find the range of, e.g. a ListComprehensionAst.
     */
    RangeInRevision comprehensionRange(Ast* node);

    /**
     * @brief Calculate the range of the arguments context of the given @p node.
     * @return Range the argument list of this function encompasses.
     */
    RangeInRevision rangeForArgumentsContext(Python::FunctionDefinitionAst* node);

    /**
     * @brief Add @p module to the list of unresolved imports in this builder.
     */
    void addUnresolvedImport(const IndexedString& module);

    /**
     * @brief Retrieve a list of imports not resolved by this builder pass.
     */
    QList<IndexedString> unresolvedImports() const;

public:
    // ugly because this collides with currentDocument(), but we have to use it;
    // for some reason the UseBuilder does not have m_url set, and it's private (not even protected) to AbstractContextBuilder.
    // so at least keep this consistent within the plugin and use this everywhere.
    // maybe we can remove this hack later. TODO maybe change something in kdevplatform, or maybe we're doing something wrong here?
    IndexedString currentlyParsedDocument() const;
    void setCurrentlyParsedDocument(const IndexedString& document);

protected:
    /**
     * @brief Create a new top context and set it as this builder's active context.
     *
     * @param range Range to encompass
     * @return KDevelop::TopDUContext* weak pointer to the created top context.
     */
    TopDUContext* newTopContext(const RangeInRevision& range, ParsingEnvironmentFile* file) override;

    /**
     * @brief Create a new context.
     * Overridden to create instances of Python's specialized DUContext.
     */
    KDevelop::DUContext* newContext(const KDevelop::RangeInRevision& range) override;

protected:
    // AST visitor functions
    void visitFunctionDefinition( FunctionDefinitionAst* ) override;
    void visitClassDefinition( ClassDefinitionAst* ) override;
    void visitCode(CodeAst* node) override;
    void visitListComprehension(ListComprehensionAst* node) override;
    void visitDictionaryComprehension(DictionaryComprehensionAst* node) override;
    void visitGeneratorExpression(GeneratorExpressionAst* node) override;
    void visitComprehensionCommon(Ast* node);

    void startVisiting(Ast* node) override;
    KDevelop::RangeInRevision editorFindRange(Ast* fromNode, Ast* toNode) override;
    virtual KDevelop::CursorInRevision editorFindPositionSafe(Ast* node);
    virtual KDevelop::CursorInRevision startPos(Ast* node);
    KDevelop::QualifiedIdentifier identifierForNode(Identifier* node) override;

    /**
     * @brief Set @p context as the context of @p node.
     * The context is stored inside the AST itself.
     */
    void setContextOnNode(Ast* node, KDevelop::DUContext* context) override;

    /**
     * @brief Get the context set on @p node as previously set by @ref setContextOnNode.
     */
    KDevelop::DUContext* contextFromNode(Ast* node) override;

    /**
     * @brief Add the saved list of contexts to import to the current context, and clear it.
     */
    void addImportedContexts();

    // helpers which need to be called separately from DeclarationBuilder
    virtual void visitFunctionArguments(FunctionDefinitionAst* node);
    virtual void visitFunctionBody(FunctionDefinitionAst* node);
    void openContextForClassDefinition(ClassDefinitionAst* node);

protected:
    // those functions can be used if you want to do something to a context you are in,
    // but which is not the current one. Example: You want to add a variable to a class context,
    // but the current context is inside that class context (method declaration, ...)
    bool contextAlreadyOpen(DUContextPointer context);
    void activateAlreadyOpenedContext(DUContextPointer context);
    void closeAlreadyOpenedContext(DUContextPointer context);
    QList<DUContextPointer> m_temporarilyClosedContexts;

protected:
    // true if the first of the two performed passes is currently active
    bool m_prebuilding = false;

    // List of imports which were encountered, but could not be resolved
    QList<IndexedString> m_unresolvedImports;

    // The ModificationRevision this context will be valid for
    ModificationRevision m_futureModificationRevision;

    IndexedString m_currentlyParsedDocument;

private:
    // The top-context being built.
    ReferencedTopDUContext m_topContext;
    PythonEditorIntegrator* m_editor = nullptr;
    QList<KDevelop::DUContext*> m_importedParentContexts;
    QSharedPointer<FileIndentInformation> m_indentInformationCache;
};

}

#endif
