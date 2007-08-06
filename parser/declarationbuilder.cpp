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

ForwardDeclaration * DeclarationBuilder::openForwardDeclaration(std::size_t name, ast_node * range)
{
    return static_cast<ForwardDeclaration*>(openDeclaration(name, range, false, true));
}

Declaration* DeclarationBuilder::openDefinition(std::size_t name, ast_node* rangeNode, bool isFunction)
{
    kDebug()<< isFunction;
    return openDeclaration(name, rangeNode, isFunction, false, true);
}

void DeclarationBuilder::visit_funcdef(funcdef_ast *node)
{
    kDebug()<<"Opening definiton for function";
    openDefinition(node->func_name, node, true);
    m_functionDefinedStack.push(node->start_token);
    DeclarationBuilderBase::visit_funcdef(node);
    m_functionDefinedStack.pop();
}

void DeclarationBuilder::visit_classdef(classdef_ast *node)
{
    openDefinition(node->class_name, node, false);
    DeclarationBuilderBase::visit_classdef(node);
    closeDeclaration();
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

Declaration* DeclarationBuilder::openDeclaration(std::size_t name, ast_node* rangeNode, bool isFunction, bool isForward, bool isDefinition)
{
    DUChainWriteLocker lock(DUChain::lock());
    Declaration::Scope scope = Declaration::GlobalScope;
    switch (currentContext()->type()) 
    {
        case DUContext::Class:
        scope = Declaration::ClassScope;
        break;
        case DUContext::Function:
        scope = Declaration::FunctionScope;
        default:
        break;
    }
    Range newRange = m_editor->findRange(rangeNode);
    QualifiedIdentifier id;
//     if (name) {
//         TypeSpecifierAST* typeSpecifier = 0; //Additional type-specifier for example the return-type of a cast operator
//         id = identifierForName(name);
//         if( typeSpecifier && id == QualifiedIdentifier("operator{...cast...}") ) {
//         if( typeSpecifier->kind == AST::Kind_SimpleTypeSpecifier )
//             visitSimpleTypeSpecifier( static_cast<SimpleTypeSpecifierAST*>( typeSpecifier ) );
//         }
//     }
    Declaration* declaration = 0;
    if (recompiling())
    {
        QMutexLocker lock(m_editor->smart() ? m_editor->smart()->smartMutex() : 0);
        Range translated = newRange;
        if (m_editor->smart())
            translated = m_editor->smart()->translateFromRevision(translated);
        for (; nextDeclaration() < currentContext()->localDeclarations().count(); ++nextDeclaration()) 
        {
            Declaration* dec = currentContext()->localDeclarations().at(nextDeclaration());
            if (dec->textRange().start() > translated.end() && dec->smartRange()) 
                break;
            if (dec->textRange() == translated && dec->scope() == scope &&
                (id.isEmpty() && dec->identifier().toString().isEmpty()) && dec->isDefinition() == isDefinition)
            {
                if (isForward)
                {
                    if (!dynamic_cast<ForwardDeclaration*>(dec))
                        break;
                }
                else if (isFunction) 
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
                if (currentContext()->type() == DUContext::Class) 
                {
                    ClassMemberDeclaration* classDeclaration = static_cast<ClassMemberDeclaration*>(declaration);
                }
                break;
            }
        }
    }
    if (!declaration)
    {
        Range* prior = m_editor->currentRange();
        Range* range = m_editor->createRange(newRange);
        m_editor->exitCurrentRange();
        Q_ASSERT(m_editor->currentRange() == prior);
        if (isForward)
        {
            declaration = new ForwardDeclaration(range, scope, currentContext());
        }
        else if (isFunction) 
        {
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

        if (isDefinition)
        declaration->setDeclarationIsDefinition(true);
        switch (currentContext()->type()) 
        {
        case DUContext::Global:
        case DUContext::Class:
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
    if(m_lastContext && (m_lastContext->type() == DUContext::Class || m_lastContext->type() == DUContext::Other ) )
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
