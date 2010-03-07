/*
  This file is part of kdev-pg
  Copyright 2002-2006 Roberto Raggi <roberto@kdevelop.org>
  Copyright 2009 Milian Wolff <mail@milianw.de>

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
#ifndef KDEV_PG_LOCATION_TABLE_H
#define KDEV_PG_LOCATION_TABLE_H

#include <QtCore/QtGlobal>

#include <QtCore/qalgorithms.h>

namespace KDevPG
{

class LocationTable
{
public:
  inline LocationTable(qint64 size = 1024)
    : lines(0), lineCount(0), currentLine(0), lastLine(0)
  {
    resize(size);
    lines[currentLine++] = 0;
  }

  inline ~LocationTable()
  {
    free(lines);
  }

  inline qint64 size() const
  { return lineCount; }

  void resize(qint64 size)
  {
    Q_ASSERT(size > 0);
    lines = (qint64*) ::realloc(lines, sizeof(qint64) * size);
    lineCount = size;
  }

  /**
   * Returns the \a line and \a column of the given \a offset in this table.
   */
  void positionAt(qint64 offset, qint64 *line, qint64 *column) const
  {
    if ( offset < 0 ) {
      // invalid offset
      *line = -1;
      *column = -1;
      return;
    } else if ( offset > lines[currentLine - 1] ) {
      // overflow
      *line = currentLine - 1;
      *column = offset - lines[currentLine - 1];
      return;
    }

    qint64 i = -1;
    // search relative to last line (next line and the one after that)
    if ( lastLine + 1 < currentLine && lines[lastLine] <= offset ) {
      if ( lines[lastLine + 1] > offset ) {
        // last matched line matches again
        i = lastLine;
      } else if ( lastLine + 2 < currentLine && lines[lastLine + 2] > offset ) {
        // next line relative to last matched matches
        i = lastLine + 1;
      }
    }
    if ( i == -1 ) {
      // fallback to binary search
      qint64 *it = qLowerBound(lines, lines + currentLine, offset);
      Q_ASSERT(it != lines + currentLine);

      if (*it != offset) {
        --it;
      }
      *line = it - lines;
      *column = offset - *it;
    } else {
      *line = i;
      *column = offset - lines[i];
    }

    lastLine = *line;
  }

  /**
   * Marks an \a offset as the character before the first one in the next line.
   * The positionAt() function relies on newline() being called properly.
   */
  inline void newline(qint64 offset)
  {
    if (currentLine == lineCount)
      resize(currentLine * 2);

    lines[currentLine++] = offset+1;
  }

  inline qint64 &operator[](int index)
  { return lines[index]; }

protected:
  /// An array of input buffer offsets
  qint64 *lines;
  /// The size of the allocated array
  qint64 lineCount;
  /// The index to the next index in the lines array
  qint64 currentLine;
  /// Last line as found by positionAt
  mutable qint64 lastLine;

private:
  LocationTable(LocationTable const &other);
  void operator=(LocationTable const &other);
};

}

#endif // KDEV_PG_LOCATION_TABLE_H

