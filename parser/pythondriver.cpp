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

#include <QtCore/QFile>
#include <QtCore/QDebug>
#include <QtCore/QTextStream>
#include <QtCore/QTextCodec>

#include "astbuilder.h"

#include <language/duchain/duchain.h>
#include <language/duchain/topducontext.h>


using namespace KDevelop;

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

void Driver::setCurrentDocument(KUrl url)
{
    m_currentDocument = url;
}

QPair<CodeAst*, bool> Driver::parse( Python::CodeAst* /* ast */)
{
    AstBuilder pythonparser;
    QPair<CodeAst*, bool> matched;
    matched.first = pythonparser.parse(m_currentDocument, m_content);
    matched.second = matched.first ? true : false; // check wether an AST was returned and react accordingly
    
    m_problems = pythonparser.m_problems;
    
    if( matched.second )
    {
        kDebug() << "Sucessfully parsed";
    }else
    {
        matched.first = 0;
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
