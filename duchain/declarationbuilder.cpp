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

#include <language/duchain/definition.h>
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
        : ContextBuilder()
{
    kDebug() << "Building Declarations";
}

DeclarationBuilder::DeclarationBuilder( EditorIntegrator* editor )
        : ContextBuilder( editor )
{
    kDebug() << "Building Declarations";
}

DeclarationBuilder:: ~DeclarationBuilder()
{
}

TopDUContext* DeclarationBuilder::buildDeclarations( const KUrl& url, Ast* node, const KDevelop::TopDUContextPointer& updateContext )
{
    TopDUContext* top = buildContexts( url, node, updateContext );
    Q_ASSERT( m_functionDefinedStack.isEmpty() );
    return top;
}

DUContext* DeclarationBuilder::buildSubDeclarations( const KUrl& url, Ast* node, KDevelop::DUContext* parent )
{
    DUContext* top = buildSubContexts( url, node, parent );
    Q_ASSERT( m_functionDefinedStack.isEmpty() );
    return top;
}

Declaration* DeclarationBuilder::openDefinition( IdentifierAst* name, Ast* rangeNode, bool isFunction )
{
    return openDeclaration( name, rangeNode, isFunction, true );
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
    DeclarationType* ret = new DeclarationType( m_editor->currentUrl(), range, ( KDevelop::Declaration::Scope )scope, currentContext() );
    ret->setSmartRange( smartRange );
    return ret;
}

Declaration* DeclarationBuilder::openDeclaration( IdentifierAst* name, Ast* range, bool isFunction, bool isDefinition, const Identifier& customName )
{
    kDebug() << "Is Function:" << isFunction;
    DUChainWriteLocker lock( DUChain::lock() );

    if ( isFunction && !m_functionDefinedStack.isEmpty() )
        isDefinition |= ( bool )m_functionDefinedStack.top();

    Declaration::Scope scope = Declaration::GlobalScope;

    switch ( currentContext()->type() )
    {

        case DUContext::Class:
            kDebug() << "In a Class Context";
            scope = Declaration::ClassScope;
            break;

        case DUContext::Function:
            kDebug() << "In a Function Context";
            scope = Declaration::FunctionScope;
            break;

        default:
            break;
    }

    SimpleRange newRange = m_editor->findRange( name ? name : range );

    QualifiedIdentifier id;

    if ( name )
    {
        id = identifierForName( name );
    }
    else
    {
        id = QualifiedIdentifier( customName );
    }

    Identifier lastId;

    if ( !id.isEmpty() )
        lastId = id.last();

    Declaration* declaration = 0;

    if ( recompiling() )
    {
        QMutexLocker lock( m_editor->smart() ? m_editor->smart()->smartMutex() : 0 );
        SimpleRange translated = newRange;

        if ( m_editor->smart() )
            translated = SimpleRange( m_editor->smart()->translateFromRevision( translated.textRange() ) );

        foreach( Declaration* dec, currentContext()->allLocalDeclarations( lastId ) )
        {
            if ( wasEncountered( dec ) )
            {
                continue;
            }

            if ( dec->range() == translated &&
                    dec->scope() == scope &&
                    ( ( id.isEmpty() && dec->identifier().toString().isEmpty() ) || ( !id.isEmpty() && lastId == dec->identifier() ) ) &&
                    dec->isDefinition() == isDefinition
               )
            {
                if ( isFunction )
                {
                    if ( scope == Declaration::ClassScope )
                    {
                        if ( !dynamic_cast<ClassFunctionDeclaration*>( dec ) )
                            continue;
                    }
                    else if ( !dynamic_cast<AbstractFunctionDeclaration*>( dec ) )
                    {
                        continue;
                    }
                }
                else if ( scope == Declaration::ClassScope )
                {
                    if ( !dynamic_cast<ClassMemberDeclaration*>( dec ) )
                        continue;
                }

                declaration = dec;

                break;
            }
        }
    }

    if ( !declaration )
    {
        //kDebug()<<"No Declarations";
        SmartRange* prior = m_editor->currentRange();
        SmartRange* range = m_editor->createRange( newRange.textRange() );
        m_editor->exitCurrentRange();
        //(range->start() != range->end());
        Q_ASSERT( m_editor->currentRange() == prior );

        if ( isFunction )
        {
            //kDebug()<<"Is a Function";
            if ( scope == Declaration::ClassScope )
            {
                declaration = specialDeclaration<ClassFunctionDeclaration>( range, newRange );
            }
            else
            {
                declaration = specialDeclaration<FunctionDeclaration>( range, newRange, scope );
            }

            if ( !m_functionDefinedStack.isEmpty() )
                declaration->setDeclarationIsDefinition( m_functionDefinedStack.top() );
        }
        else if ( scope == Declaration::ClassScope )
        {
            declaration = specialDeclaration<ClassMemberDeclaration>( range, newRange );
        }
        else
        {
            declaration = specialDeclaration<Declaration>( range, newRange, scope );
        }

        declaration->setIdentifier( id.last() );
        declaration->setDeclarationIsDefinition( isDefinition );

        switch ( currentContext()->type() )
        {

            case DUContext::Global:

            case DUContext::Class:
                kDebug() << "Found Declaration::Class Context";
                SymbolTable::self()->addDeclaration( declaration );
                break;

            default:
                break;
        }
    }

    setEncountered( declaration );

    m_declarationStack.push( declaration );
    return declaration;
}

void DeclarationBuilder::eventuallyAssignInternalContext()
{
    if ( m_lastContext )
    {
        DUChainWriteLocker lock( DUChain::lock() );

        if ( dynamic_cast<ClassFunctionDeclaration*>( currentDeclaration() ) )
            Q_ASSERT( !static_cast<ClassFunctionDeclaration*>( currentDeclaration() )->isConstructor() || currentDeclaration()->context()->type() == DUContext::Class );

        if ( m_lastContext && ( m_lastContext->type() == DUContext::Class || m_lastContext->type() == DUContext::Other || m_lastContext->type() == DUContext::Function ) )
        {
            if ( !m_lastContext->owner() || ( !wasEncountered( m_lastContext->owner() ) ) )   //if the context is already internalContext of another declaration, leave it alone
            {
                currentDeclaration()->setInternalContext( m_lastContext );

                if ( currentDeclaration()->range().start >= currentDeclaration()->range().end )
                    kDebug() << "Warning: Range was invalidated";

                m_lastContext = 0;
            }
        }
    }
}

void DeclarationBuilder::closeDeclaration()
{
    if ( m_lastContext )
    {
        currentDeclaration()->setKind( Declaration::Type );
    }

    eventuallyAssignInternalContext();

    m_declarationStack.pop();
}

void DeclarationBuilder::abortDeclaration()
{
    m_declarationStack.pop();
}

void DeclarationBuilder::openContext( DUContext * newContext )
{
    ContextBuilder::openContext( newContext );
}

void DeclarationBuilder::closeContext()
{
    ContextBuilder::closeContext();
}


KDevelop::Declaration* DeclarationBuilder::currentDeclaration() const
{
    return m_declarationStack.top();
}

int& DeclarationBuilder::nextDeclaration()
{
    return m_nextDeclarationStack.top();
}

void DeclarationBuilder::visitClassDefinition( ClassDefinitionAst* node )
{
    kDebug() << "opening class definition";
    ContextBuilder::visitClassDefinition( node );
    openDefinition( node->className, node );
    eventuallyAssignInternalContext();
    closeDeclaration();
}

void DeclarationBuilder::visitFunctionDefinition( FunctionDefinitionAst* node )
{
    kDebug() << "opening function definition";
    openDeclaration( node->functionName, node, true, true );
    ContextBuilder::visitFunctionDefinition( node );
    closeDeclaration();
}

}

