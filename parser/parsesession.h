#ifndef PYTHON_PARSESESSION_H
#define PYTHON_PARSESESSION_H
#include <QtCore/QByteArray>

#include <python_parser.h>

using namespace python;

class ParseSession
{
public:
    ParseSession();
    ~ParseSession();

    void positionAt( std::size_t offset, int *line, int *column ) const;
    void setContents( const QByteArray& contents );
    const char *contents() const;
    std::size_t size() const;
    parser::memory_pool_type *memory_pool;
    parser::token_stream_type *token_stream;
private:
    QByteArray m_contents;

};

#endif
