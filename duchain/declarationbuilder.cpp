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
#include "declarationbuilder.h"

#include <QByteArray>

#include <ktexteditor/smartrange.h>
#include <ktexteditor/smartinterface.h>

#include <language/duchain/symboltable.h>
#include <language/duchain/functiondeclaration.h>
#include <language/duchain/classfunctiondeclaration.h>
#include <language/duchain/duchain.h>
#include <language/duchain/duchainlock.h>

#include "pythoneditorintegrator.h"


using namespace KTextEditor;

using namespace KDevelop;

namespace Python
{


DeclarationBuilder::DeclarationBuilder()
        : DeclarationBuilderBase()
{
    kDebug() << "Building Declarations";
}

DeclarationBuilder::DeclarationBuilder( EditorIntegrator* editor )
        : DeclarationBuilderBase( )
{
    setEditor(editor);
    kDebug() << "Building Declarations";
}

DeclarationBuilder:: ~DeclarationBuilder()
{
}

template<class DeclarationType>
DeclarationType* DeclarationBuilder::specialDeclaration( KTextEditor::SmartRange* smartRange,
        const KDevelop::SimpleRange& range )
{
    DeclarationType* ret = new DeclarationType( m_editor->currentUrl(), range, currentContext() );
    ret->setSmartRange( smartRange );
    return ret;
}

template<class DeclarationType>
DeclarationType* DeclarationBuilder::specialDeclaration( KTextEditor::SmartRange* smartRange,
        const KDevelop::SimpleRange& range,
        int scope )
{
    DeclarationType* ret = new DeclarationType( m_editor->currentUrl(), range, currentContext() );
    ret->setSmartRange( smartRange );
    return ret;
}

void DeclarationBuilder::closeDeclaration()
{
    if ( lastContext() )
    {
        currentDeclaration()->setKind( Declaration::Type );
    }

    eventuallyAssignInternalContext();

    DeclarationBuilderBase::closeDeclaration();
}

void DeclarationBuilder::visitClassDefinition( ClassDefinitionAst* node )
{
    kDebug() << "opening class definition";
    ContextBuilder::visitClassDefinition( node );
    openDeclaration<Declaration>( node->className, node );
    eventuallyAssignInternalContext();
    closeDeclaration();
}

void DeclarationBuilder::visitFunctionDefinition( FunctionDefinitionAst* node )
{
    kDebug() << "opening function definition";
    openDeclaration<FunctionDeclaration>( node->functionName, node );
    ContextBuilder::visitFunctionDefinition( node );
    closeDeclaration();
}

void DeclarationBuilder::visitLambda( LambdaAst* node )
{
    kDebug() << "opening lambda def";
    openDeclaration<FunctionDeclaration>( QualifiedIdentifier( "lambda" ), SimpleRange(editorFindRange(node, node)) );
    ContextBuilder::visitLambda( node );
    closeDeclaration();
}

void DeclarationBuilder::visitDefaultParameter( DefaultParameterAst* node )
{
    ContextBuilder::visitDefaultParameter( node );
    AbstractFunctionDeclaration* function = currentDeclaration<AbstractFunctionDeclaration>();

    if( function )
    {
        if( node->value )
        {
            //Not sure what to do here, C++ simply adds the source code as default parameter, but that doesn't sound sane...
        }
        //simple case, we have an identifier parameter
        if( node->name->astType == Ast::IdentifierParameterPartAst )
        {
        } else if( node->name->astType == Ast::ListParameterPartAst )
        {
            //complex case, a sublist, what to do??
        }
    }
}

}

