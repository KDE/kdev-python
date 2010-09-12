/* Python Parser Test
 *
 * Copyright 2007 Andreas Pakulat <apaku@gmx.de>
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
 * 02110-1301, USA.
 */


#include "pythondriver.h"
#include "pythonparser.h"

#include <QtCore/QFile>
#include <QtCore/QDebug>
#include <QtCore/QTextStream>
#include <QtCore/QTextCodec>

#include "astbuilder.h"

namespace Python
{

Driver::Driver()
    : m_debug(false), m_pool(0), m_tokenstream(0)
{
}

bool Driver::readFile( const QString& filename, const char* codec )
{
    QFile f(filename);
    if( !f.open( QIODevice::ReadOnly | QIODevice::Text ) )
    {
        kDebug() << "Couldn't open project file:" << filename;
        return false;
    }
    QTextStream s(&f);
    if( codec )
        s.setCodec( QTextCodec::codecForName(codec) );
    m_content = s.readAll();
    return true;
}
void Driver::setContent( const QString& content )
{
    m_content = content;
}
void Driver::setDebug( bool debug )
{
    m_debug = debug;
}

bool Driver::parse( Python::CodeAst** ast )
{
    if(!m_tokenstream)
        m_tokenstream = new KDevPG::TokenStream();
    if(!m_pool)
        m_pool = new KDevPG::MemoryPool();

    PythonParser::Parser pythonparser;
    pythonparser.setTokenStream( m_tokenstream );
    pythonparser.setMemoryPool( m_pool );
    pythonparser.setDebug( m_debug );

    pythonparser.tokenize(m_content);
    PythonParser::ProjectAst* srcast;
    bool matched = pythonparser.parseProject( &srcast );
    if( matched )
    {
        kDebug() << "Sucessfully parsed";
//         if( m_debug )
//         {
//             PythonParser::DebugVisitor d( pythonparser.tokenStream );
//             d.visitProject(*srcast);
//         }
        Python::AstBuilder builder(&pythonparser);
        builder.visitProject( srcast );
        int len = builder.mNodeStack.count();
        for ( int i = 0; i < len ; i++ ) {
            Ast* dbg_ast = builder.mNodeStack.at(i);
            kDebug() << dbg_ast->astType;
        }
        *ast = builder.codeAst();
        
    }else
    {
        *ast = 0;
        pythonparser.expectedSymbol(PythonParser::AstNode::ProjectKind, "project");
        kDebug() << "Couldn't parse content";
    }
    return matched;
}


void Driver::setTokenStream( KDevPG::TokenStream* ts )
{
    m_tokenstream = ts;
}

void Driver::setMemoryPool( KDevPG::MemoryPool* pool )
{
    m_pool = pool;
}

}

// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
