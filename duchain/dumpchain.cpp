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
#include "dumpchain.h"
#include "pythoneditorintegrator.h"
#include "parsesession.h"

#include <identifiedtype.h>
#include <ducontext.h>
#include <topducontext.h>
#include <declaration.h>
#include <definition.h>
#include <duchainpointer.h>
#include <use.h>

using namespace KDevelop;

static char const * const names[] = {
    0,
    "ClassDeclaration",
    "FunctionDeclaration"
};

DumpChain::DumpChain()
    : m_editor(0)
{
}

void DumpChain::dump( ast_node* node, ParseSession* session)
{
    delete m_editor;
    m_editor = 0;
    if (session)
        m_editor = new PythonEditorIntegrator(session);
    visit_node(node);
}

void DumpChain::dump( DUContext * context, bool imported )
{
    if(context)
        kDebug()<<(imported ? "==import==> Context " : "New Context ") << context->scopeIdentifier(true) << context->textRange() << " " << (dynamic_cast<TopDUContext*>(context) ? "top-context" : "");
    if( !context )
        return;
    if (!imported)
    {
        if(!context->localDeclarations().count())
            kDebug()<<"No Declarations in the context";
        foreach (Declaration* dec, context->localDeclarations())
        {
            kDebug()<<dec->toString()<<" ["<<dec->qualifiedIdentifier()<< "]  "<<dec->textRange()<< ", "<< (dec->isDefinition() ? "defined, " : (dec->definition() ? "" : "no definition, "));
            if (dec->definition())
                kDebug()<<"Definition: " << dec->definition()->textRange() << endl;
        }
    }
    if (!imported)
    {
        foreach (DUContextPointer parent, context->importedParentContexts())
        {
            kDebug()<<"===Dumping Parent Contexts===";
            dump(parent.data(), true);
        }
        foreach (DUContext* child, context->childContexts())
        {
            kDebug()<<"===Dumping Child Contexts===";
            dump(child);
        }
    }
}

void DumpChain::visit_node(ast_node *node)
{
    if (node)
        if (m_editor)
        {
            QString nodeText;
            for( std::size_t a = node->start_token; a != node->end_token; a++ )
            {
                kdev_pg_token_stream::token_type const &tok( m_editor->parseSession()->tokenStream()->token((int) a) );
                if( !nodeText.isEmpty() )
                    nodeText += ' ';
                nodeText += m_editor->parseSession()->tokenText(tok.begin, tok.end);
            }
            if( !nodeText.isEmpty() ) nodeText = "\"" + nodeText + "\"";
            kDebug() <<names[node->kind]
              << "[(" << node->start_token << ") " << m_editor->findPosition(node->start_token, PythonEditorIntegrator::FrontEdge) << /*", "
              << m_editor->findPosition(node->end_token, CppEditorIntegrator::FrontEdge) <<*/ "] " << nodeText << endl;
        }
        else
            kDebug() << names[node->kind] << "[" << node->start_token << ", " << node->end_token << "]" << endl;
    //DefaultVisitor::visit(node);

    if (node)
        if (m_editor)
            kDebug() << names[node->kind]
              << "[("  << node->end_token << ") "/*<< m_editor->findPosition(node->start_token, CppEditorIntegrator::FrontEdge) << ", "*/
              << m_editor->findPosition(node->end_token, PythonEditorIntegrator::FrontEdge) << "]" << endl;
        else
            kDebug() << names[node->kind]
              << "[" << node->start_token << ", " << node->end_token << ']' << endl;
}

DumpChain::~ DumpChain( )
{
    delete m_editor;
}
// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
