#include "parsesession.h"
#include <kdebug.h>
#include "kdev-pg-memory-pool.h"
#include "kdev-pg-token-stream.h"

ParseSession::ParseSession()
        : memory_pool( new parser::memory_pool_type )
        , token_stream( new parser::token_stream_type )
{
}
ParseSession::~ParseSession()
{
    delete memory_pool;
    delete token_stream;
}
void ParseSession::positionAt( std::size_t offset, int *line, int *column ) const
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
