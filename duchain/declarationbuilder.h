/*****************************************************************************
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 *   Copyright 2007 Andreas Pakulat <apaku@gmx.de>                           *
 * Copyright 2011-2013 Sven Brauch <svenbrauch@googlemail.com>                *
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
#ifndef DECLARATIONBUILDER_H
#define DECLARATIONBUILDER_H

#include <language/duchain/builders/abstractdeclarationbuilder.h>
#include <language/duchain/classfunctiondeclaration.h>
#include <language/duchain/builders/abstracttypebuilder.h>
#include <interfaces/iproject.h>
#include <interfaces/icore.h>
#include <interfaces/iprojectcontroller.h>

#include "contextbuilder.h"
#include "typebuilder.h"
#include <language/duchain/types/unsuretype.h>

namespace Python
{
    
typedef QPair<QString, TopDUContextPointer> moduleContextTuple;

typedef KDevelop::AbstractDeclarationBuilder<Ast, Identifier, TypeBuilder> DeclarationBuilderBase;

class KDEVPYTHONDUCHAIN_EXPORT DeclarationBuilder: public DeclarationBuilderBase
{
public:
    DeclarationBuilder(PythonEditorIntegrator* editor);
    virtual ~DeclarationBuilder();
    void setPrebuilding(bool arg1);
    virtual ReferencedTopDUContext build(const IndexedString& url, Ast* node, ReferencedTopDUContext updateContext = ReferencedTopDUContext());
    int m_ownPriority;

protected:
    template<class T> T* openDeclaration(Identifier* name, Ast* range, DeclarationFlags flags = NoFlags) {
        T* decl = DeclarationBuilderBase::openDeclaration<T>(name, range, flags);
        decl->setAlwaysForceDirect(true);
        return decl;
    };
    template<class T> T* openDeclaration(const QualifiedIdentifier& id, const RangeInRevision& newRange, DeclarationFlags flags = NoFlags) {
        T* decl = DeclarationBuilderBase::openDeclaration<T>(id, newRange, flags);
        decl->setAlwaysForceDirect(true);
        return decl;
    };
    virtual void closeDeclaration();

    virtual void visitClassDefinition( ClassDefinitionAst* node );
    virtual void visitFunctionDefinition( FunctionDefinitionAst* node );
    virtual void visitAssignment(AssignmentAst* node);
    virtual void visitFor(ForAst* node);
    virtual void visitImport(ImportAst* node);
    virtual void visitImportFrom(ImportFromAst* node);
    virtual void visitArguments(ArgumentsAst* node);
    virtual void visitExceptionHandler(ExceptionHandlerAst* node);
    virtual void visitReturn(ReturnAst* node);
    virtual void visitCode(CodeAst* node);
    virtual void visitCall(CallAst* node);
    virtual void visitWith(WithAst* node);
    virtual void visitYield(YieldAst* node);
    virtual void visitLambda(LambdaAst* node);
    virtual void visitComprehension(ComprehensionAst* node);
    virtual void visitGlobal(GlobalAst* node);
    virtual void visitAssertion(AssertionAst* node);
    virtual void visitIf(IfAst* node);
    
    template<typename T> void visitDecorators(QList<ExpressionAst*> decorators, T* addTo);
    
    QString getDocstring(QList<Ast*> body);
    
    template<typename T> T* visitVariableDeclaration(Python::Ast* node, Declaration* previous = 0, AbstractType::Ptr type = AbstractType::Ptr(0));
    template<typename T> T* visitVariableDeclaration(Identifier* node, Ast* originalAst = 0, Declaration* previous = 0, AbstractType::Ptr type = AbstractType::Ptr(0));
    template<typename T> T* visitVariableDeclaration(Identifier* node, RangeInRevision range, AbstractType::Ptr type = AbstractType::Ptr(0));
    
    enum FitDeclarationType {
        NoTypeRequired,
        InstanceDeclarationType,
        AliasDeclarationType,
        FunctionDeclarationType
    };
    
    template<typename T> QList<Declaration*> reopenFittingDeclaration(QList< Declaration* > declarations, FitDeclarationType mustFitType, RangeInRevision updateRangeTo, Declaration** ok);
    QList<Declaration*> existingDeclarationsForNode(Identifier* node);

    /// Adjust the type of foo in an expression like assert isinstance(fooinstance, Foo)
    /// Does nothing if the given expression isn't of any of the forms
    ///    a) isinstance(fooinstance, Foo)
    ///    b) type(fooinstance) == Foo
    ///    c) fooinstance.__class__ == Foo
    void adjustForTypecheck(ExpressionAst* check);
    /// Helper for the above
    void adjustExpressionsForTypecheck(ExpressionAst* adjust, ExpressionAst* from);
    
    FitDeclarationType kindForType(AbstractType::Ptr type, bool isAlias = false);
    
    /// schedule an object to be deleted when the declaration builder is destroyed
    /// this is used to bypass the automated duchain cleanup for imports
    void scheduleForDeletion(DUChainBase* d, bool doschedule = true);
    
    /// python-specific version of openDeclaration which scans for existing declarations in previous versions of
    /// this top-context in a more intelligent way.
    /// Use this in normal declaratonbuilder code if you can't use visitVariableDeclaration.
    template<typename T> T* eventuallyReopenDeclaration(Python::Identifier* name, Python::Ast* range, FitDeclarationType mustFitType);
    
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
                                               ProblemPointer& problemEncountered, Python::Ast* rangeNode = 0);
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
     * @param rangeNode can be used to override the declarationIdentifier's range, if required. Defaults to 0.
     * @return :Declaration* the top level declaration created
     **/
    Declaration* createDeclarationTree(const QStringList& nameComponents, Identifier* declarationIdentifier,
                                       const ReferencedTopDUContext& innerCtx, Declaration* aliasDeclaration = 0,
                                       const RangeInRevision& range = RangeInRevision::invalid());
    
    /**
     * @brief Find a declaration specified by "foo.bar.baz" in the given top context.
     *
     * @param dottedNameIdentifier string list of module names, starting with the most general one.
     * @param ctx top context to search
     * @return :Declaration* declaration if found, 0 otherwise.
     * 
     * @note The DUChain must not be locked.
     **/
    Declaration* findDeclarationInContext(QStringList dottedNameIdentifier, TopDUContext* ctx) const;
    
    QStack<TopDUContextPointer> m_importContextsForImportStatement;
    DeclarationPointer m_firstAttributeDeclaration;
private:
    QList<DUChainBase*> m_scheduledForDeletion;
    QString buildModuleNameFromNode(ImportFromAst* node, AliasAst* alias, const QString& intermediate);
};

}

#endif
// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
