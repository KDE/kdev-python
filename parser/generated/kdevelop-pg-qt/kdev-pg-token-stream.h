/*
  This file is part of kdev-pg
  Copyright 2005, 2006 Roberto Raggi <roberto@kdevelop.org>

  Permission to use, copy, modify, distribute, and sell this software and its
  documentation for any purpose is hereby granted without fee, provided that
  the above copyright notice appear in all copies and that both that
  copyright notice and this permission notice appear in supporting
  documentation.

  The above copyright notice and this permission notice shall be included in
  all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
  KDEVELOP TEAM BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN
  AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
  CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
*/

//krazy:exclude-all=inline
#ifndef KDEV_PG_TOKEN_STREAM_H
#define KDEV_PG_TOKEN_STREAM_H

#include <QtCore/QtGlobal>

#include "kdev-pg-location-table.h"

namespace KDevPG
{

class Token {
  public:
    int kind;
    qint64 begin;
    qint64 end;
};
template<class T>
class TokenStreamBase
{
public:
  typedef T Token;
  TokenStreamBase()
    : mTokenBuffer(0),
      mTokenBufferSize(0),
      mIndex(0),
      mTokenCount(0),
      mLocationTable(0)
  {
    reset();
  }

  ~TokenStreamBase()
  {
    if (mTokenBuffer)
      ::free(mTokenBuffer);
    if (mLocationTable)
      delete mLocationTable;
  }

  inline void reset()
  {
    mIndex = 0;
    mTokenCount = 0;
  }

  inline qint64 size() const
  {
    return mTokenCount;
  }

  inline qint64 index() const
  {
    return mIndex;
  }

  inline qint64 tokenIndex() const
  {
    if( mIndex )
      return mIndex - 1;
    return mIndex;
  }

  inline void rewind(qint64 index)
  {
    mIndex = index;
  }

  inline T const &token(qint64 index) const
  {
    return mTokenBuffer[index];
  }

  inline T &token(qint64 index)
  {
    return mTokenBuffer[index];
  }

  inline int nextToken()
  {
    return mTokenBuffer[mIndex++].kind;
  }

  inline T &next()
  {
    if (mTokenCount == mTokenBufferSize)
      {
        if (mTokenBufferSize == 0)
          mTokenBufferSize = 1024;

        mTokenBufferSize <<= 2;

        mTokenBuffer = reinterpret_cast<T*>
          (::realloc(mTokenBuffer, mTokenBufferSize * sizeof(T)));
      }

    return mTokenBuffer[mTokenCount++];
  }

  inline LocationTable *locationTable()
  {
    if (!mLocationTable)
      mLocationTable = new LocationTable();

    return mLocationTable;
  }

  inline void startPosition(qint64 index, qint64 *line, qint64 *column)
  {
    if (!mLocationTable)
      {
        *line = 0; *column = 0;
      }
    else
      mLocationTable->positionAt(token(index).begin, line, column);
  }

  inline void endPosition(qint64 index, qint64 *line, qint64 *column)
  {
    if (!mLocationTable)
      {
        *line = 0; *column = 0;
      }
    else
      mLocationTable->positionAt(token(index).end, line, column);
  }

private:
  T *mTokenBuffer;
  qint64 mTokenBufferSize;
  qint64 mIndex;
  qint64 mTokenCount;
  LocationTable *mLocationTable;

private:
  TokenStreamBase(TokenStreamBase const &other);
  void operator = (TokenStreamBase const &other);
};


class TokenStream : public TokenStreamBase<Token>
{
};


}

#endif // KDEV_PG_TOKEN_STREAM_H

