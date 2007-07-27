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
#ifndef PYTHON_PARSESESSION_H
#define PYTHON_PARSESESSION_H
#include <QtCore/QByteArray>
#include <python_parser.h>
#include <ksharedptr.h>
#include <ktexteditor/cursor.h>
#include <ducontext.h>
class LexedFile;
namespace python
{
    class parser;
}

using namespace python;

class ParseSession
{
public:
    ParseSession();
    ~ParseSession();

    parser* Parser() const;

    void positionAt( std::size_t offset, std::size_t *line, std::size_t *column ) const;
    void setContents( const QByteArray& contents );
    const char *contents() const;
    std::size_t size() const;
    parser::memory_pool_type *memory_pool;
    parser::token_stream_type *token_stream;
    parser* m_parser;
    void put(ast_node* ast_node, KDevelop::DUContext* topducontext);

private:
    QHash<ast_node*, KDevelop::DUContext*> ducontext;
    QByteArray m_contents;

};

#endif
