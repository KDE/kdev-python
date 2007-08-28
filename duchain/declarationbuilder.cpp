/*****************************************************************************
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
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

#include <definition.h>
#include <symboltable.h>
#include <forwarddeclaration.h>
#include <duchain.h>
#include <duchainlock.h>
#include "parsesession.h"
#include "pythoneditorintegrator.h"
#include "functiondeclaration.h"
#include "classfunctiondeclaration.h"


using namespace KTextEditor;
using namespace KDevelop;
using namespace python;


DeclarationBuilder::DeclarationBuilder (ParseSession* session, const KUrl &url):DeclarationBuilderBase(session,url)
{
    kDebug()<<"Building Declarations";
}
DeclarationBuilder::DeclarationBuilder (PythonEditorIntegrator* editor, const KUrl &url):DeclarationBuilderBase(editor,url)
{
    kDebug()<<"Building Declarations";
}

DeclarationBuilder:: ~DeclarationBuilder()
{
}

TopDUContext* DeclarationBuilder::buildDeclarations(ast_node *node)
{
    TopDUContext* top = buildContexts(node);
    Q_ASSERT(m_functionDefinedStack.isEmpty());
    return top;
}
DUContext* DeclarationBuilder::buildSubDeclarations(const KUrl& url, ast_node *node, KDevelop::DUContext* parent) {
    DUContext* top = buildSubContexts(url, node, parent);
    Q_ASSERT(m_functionDefinedStack.isEmpty());
    return top;
}

Declaration* DeclarationBuilder::openDefinition(std::size_t name, ast_node* rangeNode, bool isFunction)
{
    return openDeclaration(name, rangeNode, isFunction);
}

void DeclarationBuilder::visit_funcdef(funcdef_ast *node)
{
    //kDebug()<<"Opening definiton for function";
    openDefinition(node->func_name, node, true);
    DeclarationBuilderBase::visit_funcdef(node);
}

void DeclarationBuilder::visit_classdef(classdef_ast *node)
{
    openDefinition(node->class_name, node);
    DeclarationBuilderBase::visit_classdef(node);
    //closeDeclaration();
}

void DeclarationBuilder::visit_fun_pos_param(fun_pos_param_ast *node)
{
    if(node->star_id)
        openDefinition(node->star_id,node,false);
    if(node->double_star_id)
        openDefinition(node->double_star_id,node,false);
    DeclarationBuilderBase::visit_fun_pos_param(node);
}

void DeclarationBuilder::visit_atom(atom_ast *node)
{
    if(node->atom_identifier_name)
    {
        DUChainWriteLocker lock(DUChain::lock());
        QList<Declaration*> decls = currentContext()->findDeclarations(identifierForName(node->atom_identifier_name), m_editor->findPosition(node->start_token, KDevelop::EditorIntegrator::FrontEdge) );
        if(!decls.count())
        {
            openDefinition(node->atom_identifier_name, node, false);
        }
    }
    DeclarationBuilderBase::visit_atom(node);
}

template<class DeclarationType>
DeclarationType* DeclarationBuilder::specialDeclaration( KTextEditor::Range* range )
{
    return new DeclarationType(range, currentContext());
}

template<class DeclarationType>
DeclarationType* DeclarationBuilder::specialDeclaration( KTextEditor::Range* range, int scope )
{
    return new DeclarationType(range, (KDevelop::Declaration::Scope)scope, currentContext());
}

Declaration* DeclarationBuilder::openDeclaration(std::size_t name, ast_node* rangeNode, bool isFunction)
{
    //kDebug()<<"Is Function:"<<isFunction;
    DUChainWriteLocker lock(DUChain::lock());
    Declaration::Scope scope;
    switch (currentContext()->type())
    {
        case DUContext::Class:
            //kDebug()<<"In a Class Context";
            scope = Declaration::ClassScope;
            break;
        case DUContext::Function:
            //kDebug()<<"In a Function Context";
            scope = Declaration::FunctionScope;
            break;
        case DUContext::Global:
            //kDebug()<<"Context is of type Global";
            scope = Declaration::GlobalScope;
            break;
        default:
            kDebug()<<"Context is Neithea Class Nor a Function";
            break;
    }
    Range newRange = m_editor->findRange(rangeNode);

    QualifiedIdentifier id;
    id = identifierForName(name);
    Identifier lastId;
    if( !id.isEmpty() )
        lastId = id.last();
    Declaration* declaration = 0;
    if (recompiling())
    {
//         kDebug()<<"Is Function While Recompiling:"<<isFunction;
        //dec->isDefinition() == true;
        QMutexLocker lock(m_editor->smart() ? m_editor->smart()->smartMutex() : 0);
        Range translated = newRange;
        if (m_editor->smart())
            translated = m_editor->smart()->translateFromRevision(translated);
        Q_ASSERT(translated.start() != translated.end());
        kDebug()<<"Recompiling:"<<currentContext()->localDeclarations().count()<<"declarations found.";
        for (; nextDeclaration() < currentContext()->localDeclarations().count(); ++nextDeclaration()) 
        {
            Declaration* dec = currentContext()->localDeclarations().at(nextDeclaration());
//             if (dec->textRange().start() > translated.end() && dec->smartRange())
//                 break;
            if (dec->textRange() == translated &&
          dec->scope() == scope &&
          ((id.isEmpty() && dec->identifier().toString().isEmpty()) || (!id.isEmpty() && lastId == dec->identifier())))
            {
                if (isFunction)
                {
                    if (scope == Declaration::ClassScope)
                    {
                        if (!dynamic_cast<ClassFunctionDeclaration*>(dec))
                            break;
                    }
                    else if (!dynamic_cast<AbstractFunctionDeclaration*>(dec))
                    {
                        break;
                    }
                }
                else if (scope == Declaration::ClassScope) 
                {
                    if (!dynamic_cast<ClassMemberDeclaration*>(dec))
                        break;
                }
                declaration = dec;
                break;
            }
        }
    }
    if (!declaration)
    {
        //kDebug()<<"No Declarations";
        Range* prior = m_editor->currentRange();
        Range* range = m_editor->createRange(newRange);
        m_editor->exitCurrentRange();
        //(range->start() != range->end());
        Q_ASSERT(m_editor->currentRange() == prior);
        if (isFunction)
        {
            //kDebug()<<"Is a Function";
            if (scope == Declaration::ClassScope)
            {
                declaration = specialDeclaration<ClassFunctionDeclaration>( range );
            }
            else
            {
                declaration = specialDeclaration<FunctionDeclaration>(range, scope );
            }
            if (!m_functionDefinedStack.isEmpty())
                declaration->setDeclarationIsDefinition(m_functionDefinedStack.top());
        }
        else if (scope == Declaration::ClassScope) 
        {
            declaration = specialDeclaration<ClassMemberDeclaration>(range );
        }
        else
        {
            declaration = specialDeclaration<Declaration>(range, scope );
        }
        if(name)
        {
            declaration->setIdentifier(id.last());
        }

        declaration->setDeclarationIsDefinition(true);

        switch (currentContext()->type())
        {
        case DUContext::Global:
            kDebug()<<"Found Declaration::Global Context";
            SymbolTable::self()->addDeclaration(declaration);
            break;
        case DUContext::Class:
            kDebug()<<"Found Declaration::Class Context";
            SymbolTable::self()->addDeclaration(declaration);
            break;
        case DUContext::Function:
            kDebug()<<"Found Declaration::Function Context";
            SymbolTable::self()->addDeclaration(declaration);
            break;
        default:
            break;
        }
    }
    setEncountered(declaration);
    m_declarationStack.push(declaration);
    return declaration;
}

void DeclarationBuilder::closeDeclaration()
{
    if (m_lastContext)
    {
        DUChainWriteLocker lock(DUChain::lock());
        currentDeclaration()->setKind(Declaration::Type);
    }
    if(m_lastContext && (m_lastContext->type() == DUContext::Class || m_lastContext->type() == DUContext::Other || m_lastContext->type() == DUContext::Function) )
    {
        currentDeclaration()->setInternalContext(m_lastContext);
        m_lastContext = 0;
    }
    m_declarationStack.pop();
}

void DeclarationBuilder::abortDeclaration()
{
    m_declarationStack.pop();
}

void DeclarationBuilder::openContext(DUContext * newContext)
{
  DeclarationBuilderBase::openContext(newContext);

  m_nextDeclarationStack.push(0);
}

void DeclarationBuilder::closeContext()
{
  DeclarationBuilderBase::closeContext();
  m_nextDeclarationStack.pop();
}
