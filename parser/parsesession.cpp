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
//#include "python_parser.h"

ParseSession::ParseSession()
        : memory_pool( new parser::memory_pool_type )
        , token_stream( new parser::token_stream_type )
        , m_parser( new parser)
{
}
ParseSession::~ParseSession()
{
    delete memory_pool;
    delete token_stream;
}
void ParseSession::positionAt( std::size_t offset, std::size_t *line, std::size_t *column ) const
{
    token_stream->location_table()->position_at( offset, line, column );
}

std::size_t ParseSession::size() const
{
    return m_contents.size();
}

const char *ParseSession::contents() const
{
    return m_contents.constData();
}

void ParseSession::setContents( const QByteArray & contents )
{
    m_contents = contents;
}

parser *ParseSession::Parser() const
{
    return m_parser;
}
