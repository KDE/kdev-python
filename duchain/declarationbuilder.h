/*****************************************************************************
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 * Copyright 2007 Andreas Pakulat <apaku@gmx.de>                             *
 * Copyright 2011-2014 Sven Brauch <svenbrauch@googlemail.com>               *
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

#ifndef PYTHON_DECLARATIONBUILDER_H
#define PYTHON_DECLARATIONBUILDER_H

#include <language/duchain/builders/abstracttypebuilder.h>
#include <language/duchain/builders/abstractdeclarationbuilder.h>

#include <QList>

#include "contextbuilder.h"
#include "declarations/functiondeclaration.h"
#include "ast.h"

namespace Python
{

class CorrectionHelper;

typedef KDevelop::AbstractTypeBuilder<Ast, Identifier, ContextBuilder> TypeBuilderBase;

typedef KDevelop::AbstractDeclarationBuilder<Ast, Identifier, TypeBuilderBase> DeclarationBuilderBase;

class KDEVPYTHONDUCHAIN_EXPORT DeclarationBuilder: public DeclarationBuilderBase
{
public:
    DeclarationBuilder(PythonEditorIntegrator* editor, int ownPriority);
    virtual ~DeclarationBuilder();

    /**
     * @brief Entry function, called by KDevPlatform.
     */
    ReferencedTopDUContext build(const IndexedString& url, Ast* node,
                                 ReferencedTopDUContext updateContext = ReferencedTopDUContext()) override;

    /**
     * @brief Set whether the current running pass is the first or the second one.
     * @param prebuilding true if first pass, false if second
     */
    void setPrebuilding(bool prebuilding);

    /**
     * @brief Priority of this parse job.
     */
    int jobPriority() const;

    /**
     * @brief Get the docstring which belongs to the given body
     * @param body Body of statements which is in the documented function or class
     */
    QString getDocstring(QList<Ast*> body) const;

    /**
     * @brief Construct the dotted name of a module from an import ... from ... as statement.
     *
     * @param node the import ... from node
     * @param alias the ... as ... node
     * @param intermediate an additional string to prepend to the module name (dot is added internally)
     */
    QString buildModuleNameFromNode(ImportFromAst* node, AliasAst* alias, const QString& intermediate) const;

    /**
     * @brief Get a list of all module names which were not found while parsing.
     */
    QVector<IndexedString> missingModules() const {
        return m_missingModules;
    }

protected:
    /// AST visitor functions
    void visitClassDefinition(ClassDefinitionAst* node) override;
    void visitFunctionDefinition(FunctionDefinitionAst* node) override;
    void visitAssignment(AssignmentAst* node) override;
    void visitAnnotationAssignment(AnnotationAssignmentAst* node) override;
    void visitFor(ForAst* node) override;
    void visitImport(ImportAst* node) override;
    void visitImportFrom(ImportFromAst* node) override;
    void visitArguments(ArgumentsAst* node) override;
    void visitExceptionHandler(ExceptionHandlerAst* node) override;
    void visitReturn(ReturnAst* node) override;
    void visitCode(CodeAst* node) override;
    void visitCall(CallAst* node) override;
    void visitYield(YieldAst* node) override;
    void visitWithItem(WithItemAst* node) override;
    void visitLambda(LambdaAst* node) override;
    void visitComprehension(ComprehensionAst* node) override;
    void visitGlobal(GlobalAst* node) override;
    void visitAssertion(AssertionAst* node) override;
    void visitIf(IfAst* node) override;
    void visitString(StringAst* node) override;
    void visitNode(Ast* node) override;

protected:
    enum VisitVariableFlags {
        NoVisitVariableFlags = 0x0,
        AbortIfReopenMismatch = 0x1
    };
    /// Visitor helper functions
    template<typename T> T* visitVariableDeclaration(Python::Ast* node, Declaration* previous=nullptr,
                                                     AbstractType::Ptr type = AbstractType::Ptr(),
                                                     VisitVariableFlags flags=NoVisitVariableFlags);
    template<typename T> T* visitVariableDeclaration(Identifier* node, Ast* originalAst = nullptr, Declaration* previous=nullptr,
                                                     AbstractType::Ptr type = AbstractType::Ptr(),
                                                     VisitVariableFlags flags=NoVisitVariableFlags);

protected:
    /**
     * @brief Applies docstring hints, such as "addsType"
     * @param node the called function
     * @param function the declaration which belongs to @p node
     *
     * Used for example in a = []; a.append(3) to set the type of a to "list of int".
     */
    void applyDocstringHints(CallAst* node, Python::FunctionDeclaration::Ptr function);

    /**
     * @brief Try to deduce types of function arguments from a call and stores it in the duchain
     * @param node the called function or class (i.e. constructor)
     * @param called the declaration which belongs to @p node
     *
     * Used for example in def f(x): pass; a = f(3) to set the type of x to "int"
     */
    void addArgumentTypeHints(CallAst* node, DeclarationPointer called);

    /**
     * @brief Adjust the type of foo in an expression like assert isinstance(fooinstance, Foo)
     * Does nothing if the given expression isn't of any of the forms
     *    a) isinstance(fooinstance, Foo)
     *    b) type(fooinstance) == Foo */
    void adjustForTypecheck(ExpressionAst* check, bool useUnsure);
    /// Helper for the above
    void adjustExpressionsForTypecheck(ExpressionAst* adjust, ExpressionAst* from, bool useUnsure);

    /// Represents a single source type in a tuple assignment.
    struct SourceType {
        AbstractType::Ptr type;
        DeclarationPointer declaration;
        bool isAlias;
    };

    /** @brief If sourceType is a container that can be unpacked into outTypes, do so. */
    void tryUnpackType(AbstractType::Ptr sourceType, QVector<AbstractType::Ptr>& outTypes, int starred);

    /**
      * @brief Handle a variable assignment to @p name and give it the type @p element.
      */
    void assignToName(NameAst* name, const SourceType& element);

    /**
     * @brief Handle assignment to subscript @p subscript with rhs type @p element.
     */
    void assignToSubscript(SubscriptAst* subscript, const SourceType& element);

    /**
     * @brief Handle assignment to an attribute @p attribute with rhs type @p element.
     */
    void assignToAttribute(AttributeAst* attribute, const SourceType& element);

    /**
     * @brief Handle assignment to a target @p target with rhs type @p element.
     */
    void assignToTuple(TupleAst* tuple, const SourceType& element);

    /**
     * @brief Handle assignment to a target @p target with rhs type @p element.
     */
    void assignToUnknown(ExpressionAst* target, const AbstractType::Ptr type);
    void assignToUnknown(ExpressionAst* target, const SourceType& element);

    /**
     * @brief Find all existing declarations for the identifier @p node
     */
    QList<Declaration*> existingDeclarationsForNode(Identifier* node);

    enum FitDeclarationType {
        NoTypeRequired,
        InstanceDeclarationType,
        AliasDeclarationType,
        FunctionDeclarationType
    };
    FitDeclarationType kindForType(AbstractType::Ptr type, bool isAlias = false);

    /**
     * @brief schedule an object to be deleted when the declaration builder is destroyed
     * this is used to bypass the automated duchain cleanup for imports */
    void scheduleForDeletion(DUChainBase* d, bool doschedule = true);

    /**
     * @brief python-specific version of openDeclaration which scans for existing declarations in previous versions of
     *        this top-context in a more intelligent way.
     * Use this in normal declaratonbuilder code if you can't use visitVariableDeclaration. */
    template<typename T> T* eventuallyReopenDeclaration(Python::Identifier* name, Python::Ast* range,
                                                        FitDeclarationType mustFitType);

    template<typename T> QList<Declaration*> reopenFittingDeclaration(QList<Declaration*> declarations,
                                                                      FitDeclarationType mustFitType,
                                                                      RangeInRevision updateRangeTo, Declaration** ok);

    /**
     * @brief Create a declaration for an import statement.
     *
     * @param dottedName The dotted name of the module, like "random.randint".
     * @param declarationIdentifier provides the name and range
     * @param rangeNode can be used to override the declarationIdentifier's range, if required. Defaults to 0.
     * @param createProblem whether or not to create DUChain problems Defaults to CreateProblems.
     * @return :Declaration* the declaration created, or 0 if none was found.
     **/
    Declaration* createModuleImportDeclaration(QString dottedName, QString declarationName, Python::Identifier* declarationIdentifier,
                                               ProblemPointer& problemEncountered, Python::Ast* rangeNode = nullptr);
    /**
     * @brief Create a tree of declarations for the specified list.
     * Give the list ["foo","bar","baz"], and you'll get a declaration "foo" containing "bar" in its internal context,
     * "bar" containing "baz" etc.
     * This is used in import handling.
     * This function automatically updates existing declaration trees to the maximum level possible! Thus,
     * if you call this with ["foo", "bar"], then ["foo", "baz"], "baz" will be added to "foo".
     *
     * @warning The DUChain must not be locked when this is called.
     *
     * @param nameComponents the list of names to create declarations for
     * @param declarationIdentifier provides the name and range
     * @param innerCtx the internalContext() to set on the last created declaration. Either this or aliasDeclaration must be provided!
     * @param aliasDeclaration the declaration to alias with the last created declaration
     * @param range can be used to override the declarationIdentifier's range, if required. Defaults to an invalid range.
     * @return :Declaration* the top level declaration created
     **/
    Declaration* createDeclarationTree(const QStringList& nameComponents, Identifier* declarationIdentifier,
                                       const ReferencedTopDUContext& innerCtx, Declaration* aliasDeclaration = nullptr,
                                       const RangeInRevision& range = RangeInRevision::invalid());

    /**
     * @brief Find a declaration specified by "foo.bar.baz" in the given top context.
     *
     * @param dottedNameIdentifier string list of module names, starting with the most general one.
     * @param ctx top context to search
     * @return :Declaration* declaration if found, 0 otherwise.
     *
     * This will traverse nested classes and properties until the list of passed names is exhausted.
     * @warning The DUChain must not be locked.
     **/
    Declaration* findDeclarationInContext(QStringList dottedNameIdentifier, TopDUContext* ctx) const;

private:
    template<class T> T* openDeclaration(Identifier* name, Ast* range, DeclarationFlags flags = NoFlags)
    {
        T* decl = DeclarationBuilderBase::openDeclaration<T>(name, range, flags);
        decl->setAlwaysForceDirect(true);
        return decl;
    };
    template<class T> T* openDeclaration(const QualifiedIdentifier& id, const RangeInRevision& newRange,
                                         DeclarationFlags flags = NoFlags)
    {
        T* decl = DeclarationBuilderBase::openDeclaration<T>(id, newRange, flags);
        decl->setAlwaysForceDirect(true);
        return decl;
    };
    void closeDeclaration() override;

private:
    /// HACK: List of items to delete after parsing finishes, to work around the built-in cleanup logic
    QList<DUChainBase*> m_scheduledForDeletion;
    QScopedPointer<CorrectionHelper> m_correctionHelper;
    int m_ownPriority = 0;
    QVector<StructureType::Ptr> m_currentClassTypes;
    // missing modules, for not reporting them as unknown variables
    QVector<IndexedString> m_missingModules;

    StringAst* m_lastComment = nullptr;
};

}

#endif
// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
