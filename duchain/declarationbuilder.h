/*****************************************************************************
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 *   Copyright 2007 Andreas Pakulat <apaku@gmx.de>                           *
 * Copyright 2011 Sven Brauch <svenbrauch@googlemail.com>                    *
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
    DeclarationBuilder();
    DeclarationBuilder( PythonEditorIntegrator* editor );
    virtual ~DeclarationBuilder();
    void setPrebuilding(bool arg1);
    virtual ReferencedTopDUContext build(const IndexedString& url, Ast* node, ReferencedTopDUContext updateContext = ReferencedTopDUContext());

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
    virtual void visitListComprehension(ListComprehensionAst* node);
    
    template<typename T> void visitDecorators(QList<ExpressionAst*> decorators, T* addTo);
    
    QString getDocstring(QList<Ast*> body);
    
    template<typename T> T* visitVariableDeclaration(Python::Ast* node, Declaration* previous = 0);
    template<typename T> T* visitVariableDeclaration(Identifier* node, Ast* originalAst = 0, Declaration* previous = 0);
    template<typename T> T* visitVariableDeclaration(Identifier* node, RangeInRevision range);
    
    Declaration* createModuleImportDeclaration( QString dottedName, Python::Identifier* declarationIdentifier, Python::Ast* rangeNode = 0);
    
    /**
     * @brief Find a declaration specified by "foo.bar.baz" in the given top context.
     *
     * @param dottedNameIdentifier string list of module names, starting with the most general one.
     * @param ctx top context to search
     * @return :Declaration* declaration if found, 0x0 otherwise.
     * 
     * @note The DUChain must not be locked.
     **/
    Declaration* findDeclarationInContext(QStringList dottedNameIdentifier, TopDUContext* ctx) const;
    
    QStack<TopDUContextPointer> m_importContextsForImportStatement;
    DeclarationPointer m_firstAttributeDeclaration;
    bool m_prebuilding;
private:
    int& nextDeclaration();
};

}

#endif
// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
