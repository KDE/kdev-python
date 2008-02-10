/*****************************************************************************
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 *                                                                           *
 * Permission is hereby granted, free of charge, to any person obtaining     *
 * a copy of this software and associated documentation files (the           *
 * "Software"), to deal in the Software without rekDebug()iction, including       *
 * without limitation the rights to use, copy, modify, merge, publish,       *
 * dikDebug()ibute, sublicense, and/or sell copies of the Software, and to        *
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

namespace Python {

static char const * const names[] = {
    0,
    "ClassDeclaration",
    "FunctionDeclaration"
};

DumpChain::DumpChain()
    : m_editor(0)
{
}

void DumpChain::dump( Ast* node, ParseSession* session)
{
    delete m_editor;
    m_editor = 0;
    if (session)
        m_editor = new EditorIntegrator(session);
    visitNode(node);
}

void DumpChain::dump( DUContext * context, bool imported )
{
    if(context)
        kDebug() << (imported ? "==import==> Context " : "New Context ") << context->scopeIdentifier(true) << context->range().textRange() << " " << (dynamic_cast<TopDUContext*>(context) ? "top-context" : "");
    if( !context )
        return;
    if (!imported)
    {
        if(!context->localDeclarations().count())
            kDebug() <<"No Declarations in the context";
        foreach (Declaration* dec, context->localDeclarations())
        {
            kDebug() <<dec->toString()<<" ["<<dec->qualifiedIdentifier()<< "]  "<<dec->range().textRange() << ", "<< (dec->isDefinition() ? "defined, " : (dec->definition() ? "" : "no definition, "));
            if (dec->definition())
                kDebug() <<"Definition: " << dec->definition()->range().textRange() << endl;
        }
    }
    if (!imported)
    {
        foreach (DUContextPointer parent, context->importedParentContexts())
        {
            kDebug() <<"===Dumping Parent Contexts===";
            dump(parent.data(), true);
        }
        foreach (DUContext* child, context->childContexts())
        {
            kDebug() <<"===Dumping Child Contexts===";
            dump(child);
        }
    }
}

void DumpChain::visitNode(Ast *node)
{
    if (node)
        if (m_editor)
        {
            QString nodeText;
            kDebug() << names[node->astType]
              << "[(" << node->start << ") " << m_editor->findPosition( node, EditorIntegrator::FrontEdge) << ", "
              << m_editor->findPosition( node , EditorIntegrator::BackEdge ) << "] ";
        }
        else
            kDebug() << names[node->astType] << "[" << node->start << ", " << node->end << "]";
    
    AstDefaultVisitor::visitNode(node);
    
    if (node)
        if (m_editor)
            kDebug() << names[node->astType]
              << "[("  << node->end << ") " << m_editor->findPosition(node, EditorIntegrator::FrontEdge) << ", "
              << m_editor->findPosition( node, EditorIntegrator::BackEdge ) << "]" << endl;
        else
            kDebug() << names[node->astType]
              << "[" << node->start << ", " << node->end << ']' << endl;
}

DumpChain::~ DumpChain( )
{
    delete m_editor;
}

}
