/*****************************************************************************
 * Copyright (c) 2007 Andreas Pakulat <apaku@gmx.de>                         *
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
#include "parsesession.h"

#include "kdev-pg-memory-pool.h"
#include "kdev-pg-token-stream.h"
#include "pythondriver.h"
#include <ducontext.h>

ParseSession::ParseSession()
        : m_memoryPool( new KDevPG::MemoryPool )
        , m_tokenStream( new KDevPG::TokenStream )
{
}
ParseSession::~ParseSession()
{
    delete m_memoryPool;
    delete m_tokenStream;
}
void ParseSession::positionAt( qint64 offset, qint64 *line, qint64 *column ) const
{
    m_tokenStream->locationTable()->positionAt( offset, line, column );
}

void ParseSession::putNode( PythonParser::AstNode* ast_node, KDevelop::DUContext* topducontext )
{
    m_nodeHash[ast_node] = topducontext;
}
KDevelop::DUContext* ParseSession::getNode( PythonParser::AstNode* ast_node )
{
    return m_nodeHash[ast_node];
}
void ParseSession::removeNode( PythonParser::AstNode* ast_node )
{
    m_nodeHash.remove(ast_node);
}
QString ParseSession::contents() const
{
    return m_contents;
}

void ParseSession::setContents( const QString& contents )
{
    m_contents = contents;
}

bool ParseSession::parse( PythonParser::ProjectAst** ast )
{
    Python::Driver d;
    d.setTokenStream( m_tokenStream );
    d.setMemoryPool( m_memoryPool );
    d.setContent( m_contents );
    return d.parse( ast );
}

QString ParseSession::tokenText( qint64 begin, qint64 end )
{
    return m_contents.mid(begin,end-begin+1);
}


KDevPG::TokenStream* ParseSession::tokenStream() const
{
    return m_tokenStream;
}

