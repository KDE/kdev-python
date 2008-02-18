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
#ifndef DECLARATIONBUILDER_H
#define DECLARATIONBUILDER_H

#include <language/duchain/declaration.h>
#include <language/duchain/classfunctiondeclaration.h>
#include "contextbuilder.h"
#include "pythonduchainexport.h"


namespace KDevelop
{

class Declaration;
}

namespace Python
{

class KDEVPYTHONDUCHAIN_EXPORT DeclarationBuilder: public ContextBuilder
{

public:
    DeclarationBuilder();
    DeclarationBuilder( EditorIntegrator* editor );
    virtual ~DeclarationBuilder();
    KDevelop::TopDUContext* buildDeclarations( const KUrl& url, Ast* node, 
                                               const KDevelop::TopDUContextPointer& updateContext 
                                                       = KDevelop::TopDUContextPointer() );
    KDevelop::DUContext* buildSubDeclarations( const KUrl& url, Ast* node, 
                                               KDevelop::DUContext* parent = 0 );
    KDevelop::Declaration* currentDeclaration() const;

protected:
    virtual void openContext( KDevelop::DUContext* newContext );
    virtual void closeContext();

    virtual void visitClassDefinition( ClassDefinitionAst* node );

private:
    KDevelop::Declaration* openDeclaration( IdentifierAst* name, Ast* range, 
                                             bool isFunction = false, 
                                             bool isDefinition = false, 
                                             const KDevelop::Identifier& customName 
                                                     = KDevelop::Identifier() );
    KDevelop::Declaration* openDefinition( IdentifierAst* name, Ast* range, 
                                           bool isFunction = false );
    void closeDeclaration();
    void abortDeclaration();
    void eventuallyAssignInternalContext();

    template<class DeclarationType>
    inline DeclarationType* currentDeclaration() const
    {
        return dynamic_cast<DeclarationType*>( m_declarationStack.top() );
    }

    template<class DeclarationType>
    DeclarationType* specialDeclaration( KTextEditor::SmartRange* smartRange,
                                         const KDevelop::SimpleRange& range );

    template<class DeclarationType>
    DeclarationType* specialDeclaration( KTextEditor::SmartRange* smartRange,
                                         const KDevelop::SimpleRange& range,
                                         int scope );

    int& nextDeclaration();

    QStack<KDevelop::Declaration*> m_declarationStack;
    QStack<int> m_nextDeclarationStack;
    QStack<std::size_t> m_functionDefinedStack;
};

}

#endif
// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
