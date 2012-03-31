/*
    This file is part of kdev-python, the python language plugin for KDevelop
    Copyright (C) 2012  Sven Brauch svenbrauch@googlemail.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/


#include "codehelpers.h"
#include <QStack>

namespace Python {
    

FileIndentInformation::FileIndentInformation(const QStringList& lines)
{
    initialize(lines);
}

void FileIndentInformation::initialize(const QStringList& lines)
{
    for ( int atLine = 0; atLine < lines.length(); atLine++ ) {
        const QString& currentLine = lines.at(atLine);
        const int currentLength = currentLine.length();
        bool lineIsNonempty = false;
        for ( int indent = 0; indent < currentLength; indent++ ) {
            if ( ! currentLine.at(indent).isSpace() ) {
                m_indents.append(indent);
                lineIsNonempty = true;
                break;
            }
        }
        if ( ! lineIsNonempty ) {
            m_indents.append(currentLine.length());
        }
    }
}

FileIndentInformation::FileIndentInformation(const QString& data)
{
    initialize(data.split('\n'));
}

FileIndentInformation::FileIndentInformation(const QByteArray& data)
{
    initialize(QString(data.data()).split('\n'));
}

FileIndentInformation::FileIndentInformation(KTextEditor::Document* document)
{
    QStringList lines;
    for ( int i = 0; i < document->lines(); i++ ) {
        lines << document->line(i);
    }
    initialize(lines);
}

int FileIndentInformation::indentForLine(int line) const
{
    return m_indents.at(line);
}

int FileIndentInformation::nextChange(int line, ChangeTypes type, ScanDirection direction) const
{
    kDebug() << "scanning:" << line << m_indents;
    line = qMin(line, m_indents.length() - 1);
    line = qMax(line, 0);
    kDebug() << "capped:" << line;
    const int currentIndent = m_indents.at(line);
    const int length = m_indents.length();
    const char scandir = direction == Forward ? 1 : -1;
    int atIndent = 0;
    do {
        if ( line >= length - 1 || line < 0 ) {
           break;
        }
        line += scandir;
        atIndent = m_indents.at(line);
    } while ( type == Indent ? atIndent <= currentIndent :
              type == Dedent ? atIndent >= currentIndent :
                               atIndent == currentIndent );
    kDebug() << "result: " << line;
    return line;
}

CodeHelpers::CodeHelpers()
{
    
}

QString CodeHelpers::expressionUnderCursor(Python::LazyLineFetcher& lineFetcher, KTextEditor::Cursor cursor)
{
    QString line = lineFetcher.fetchLine(cursor.line());
    int index = cursor.column();
    QChar c = line[index];
    if ( ! c.isLetterOrNumber() && c != '_' ) {
        return QString();
    }

    int end = index;
    for (; end < line.size(); ++end)
    {
        QChar c = line[end];
        if ( ! ( c.isLetterOrNumber() || c == '_' ) ) {
            break;
        }
    }
    int start = index;
    QStringList openingBrackets = QStringList() << "(" << "[" << "{" << "\"" << "'";
    QStringList closingBrackets = QStringList() << ")" << "]" << "}" << "\"" << "'";
    QStringList sliceChars = QStringList() << "." << "(" << "["; // chars which are allowed to be preceded by a space
    QStack<QString> brackets;
    bool lastWasSlice = false;
    while ( start > 0 ) {
        QChar c = line[start];
        int bracket = closingBrackets.indexOf(c);
        kDebug() << bracket << c;
        if ( ! brackets.isEmpty() && brackets.top() == c ) {
            brackets.pop();
        }
        else if ( bracket != -1 ) {
            brackets.push(openingBrackets.at(bracket));
        }
        else if ( openingBrackets.contains(c) ) {
            start += 1;
            break;
        }
        
        if ( brackets.isEmpty() && c.isSpace() && ! lastWasSlice ) {
            start += 1;
            break;
        }
        
        if ( sliceChars.contains(c) ) {
            lastWasSlice = true;
        }
        else {
            lastWasSlice = false;
        }
        start--;
    }
    if ( ! ( start < end ) ) {
        return QString();
    }

    QString expression(line.mid(start, end-start));
    expression = expression.trimmed();
    kDebug() << "expression found:" << expression;
    return expression;
}

}