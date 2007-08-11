#include "dumpchain.h"
#include "pythoneditorintegrator.h"
#include "parsesession.h"

#include <identifiedtype.h>
#include <ducontext.h>
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

void DumpChain::visit_node(ast_node *node)
{
    if (node)
        if (m_editor)
        {
            QString nodeText;
            for( std::size_t a = node->start_token; a != node->end_token; a++ ) 
            {
                parser::token_type const &tok( m_editor->parseSession()->token_stream->token((int) a) );
                if( !nodeText.isEmpty() )
                    nodeText += ' ';
                //nodeText += QByteArray( tok.text+tok.position, tok.size );
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

void DumpChain::dump( DUContext * context, bool imported )
{
    if( !context )
        return;
    if (!imported) 
    {
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
            dump(parent.data(), true);
        }
        foreach (DUContext* child, context->childContexts())
            dump(child);
    }
}
