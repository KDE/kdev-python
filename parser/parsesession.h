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
#include <QtCore/QString>
#include <QtCore/QHash>
#include "parserexport.h"

class LexedFile;
namespace Python
{
    class project_ast;
    class ast_node;
}

class kdev_pg_token_stream;
class kdev_pg_memory_pool;

namespace KDevelop
{
    class DUContext;
}

class KDEVPYTHONPARSER_EXPORT ParseSession
{
public:
    ParseSession();
    ~ParseSession();

    void positionAt( std::size_t offset, std::size_t *line, std::size_t *column ) const;
    void setContents( const QString& contents );
    QString contents() const;

    void putNode( Python::ast_node* ast_node, KDevelop::DUContext* topducontext );
    void removeNode( Python::ast_node* ast_node );
    KDevelop::DUContext* getNode( Python::ast_node* ast_node );

    bool parse( Python::project_ast** );
    QString tokenText( std::size_t, std::size_t);
    kdev_pg_token_stream* tokenStream() const;
private:
    QHash<Python::ast_node*, KDevelop::DUContext*> m_nodeHash;
    QString m_contents;
    kdev_pg_memory_pool* m_memoryPool;
    kdev_pg_token_stream* m_tokenStream;

};

#endif

// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
