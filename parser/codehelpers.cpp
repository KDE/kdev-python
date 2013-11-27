/*
    This file is part of kdev-python, the python language plugin for KDevelop
    Copyright (C) 2012  Sven Brauch svenbrauch@googlemail.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 2 of the License, or
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
    m_indents.clear();
    for ( int atLine = 0; atLine < lines.length(); atLine++ ) {
        const QString& currentLine = lines.at(atLine);
        const int currentLength = currentLine.length();
        bool lineIsEmpty = true;
        for ( int indent = 0; indent < currentLength; indent++ ) {
            if ( ! currentLine.at(indent).isSpace() ) {
                m_indents.append(indent);
                lineIsEmpty = false;
                break;
            }
        }
        if ( lineIsEmpty ) {
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

int FileIndentInformation::linesCount() const
{
    return m_indents.length();
}

int FileIndentInformation::nextChange(int line, ChangeTypes type, ScanDirection direction) const
{
    line = qMin(line, m_indents.length() - 1);
    line = qMax(line, 0);
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
    return line;
}

CodeHelpers::CodeHelpers()
{
    
}

bool CodeHelpers::endsInside(const QString &code, CodeHelpers::EndLocation location)
{
    bool insideSingleLineComment = false;
    QStringList stringDelimiters;
    stringDelimiters << "\"\"\"" << "\'\'\'" << "'" << "\"";
    QStack<QString> stringStack;
    const int max_len = code.length();
    kDebug() << "Checking for comment line:" << code;
    for ( int atChar = 0; atChar < max_len; atChar++ ) {
        const QChar c = code.at(atChar);
        if ( c == ' ' || c.isLetterOrNumber() ) {
            continue;
        }
        if ( stringStack.isEmpty() && c == '#' ) {
            insideSingleLineComment = true;
            continue;
        }
        if ( c == '\n' ) {
            insideSingleLineComment = false;
            continue;
        }
        if ( insideSingleLineComment ) {
            // don't count string delimiters in a comment line
            continue;
        }
        if ( c != '"' && c != '\'' && c != '\\' ) {
            continue;
        }
        QStringRef t;
        if ( max_len - atChar > 2 ) {
            t = code.midRef(atChar, 3);
        }
        foreach ( const QString& check, stringDelimiters ) {
            if ( t != check && ! ( check.size() == 1 && c == check.at(0) ) ) {
                continue;
            }
            if ( stringStack.isEmpty() ) {
                stringStack.push(check);
                atChar += check.length() - 1;
                break;
            }
            else if ( stringStack.top() == check ) {
                stringStack.pop();
                atChar += check.length() - 1;
                break;
            }
        }
        if ( c == '\\' ) {
            atChar ++;
            continue;
        }
    }

    if (location == String) {
        return ! stringStack.isEmpty();
    }
    else {
        return insideSingleLineComment;
    }
}

QString CodeHelpers::killStrings(QString stringWithStrings)
{
    QRegExp replaceStrings("(\".*\"|\'.*\'|\"\"\".*\"\"\"|\'\'\'.*\'\'\')");
    replaceStrings.setMinimal(true);
    QString stripped = stringWithStrings.replace(replaceStrings, "\"S\"");
    return stripped;
}

QString CodeHelpers::expressionUnderCursor(Python::LazyLineFetcher& lineFetcher, KTextEditor::Cursor cursor, bool forceScanExpression)
{
    QString line = lineFetcher.fetchLine(cursor.line());
    int index = cursor.column();
    QChar c = line[index];
    
    int end = index;
    // This flag is used by codecompletion (in contrast to the debugger)
    if ( ! forceScanExpression ) {
        if ( ! c.isLetterOrNumber() && c != '_' ) {
            return QString();
        }
    }
    for (; end < line.size(); ++end)
    {
        QChar c = line[end];
        if ( ! ( c.isLetterOrNumber() || c == '_' ) ) {
            if ( ! forceScanExpression ) end--;
            break;
        }
    }
    int start = index;
    QStringList openingBrackets = QStringList() << "(" << "[" << "{" << "\"" << "'";
    QStringList closingBrackets = QStringList() << ")" << "]" << "}" << "\"" << "'";
    QStringList sliceChars = QStringList() << "." << "(" << "["; // chars which are allowed to be preceded by a space
    QStringList seperatorChars = QStringList() << "," << "=" << ":";
    QStack<QString> brackets;
    bool lastWasSlice = false;
    int linesFetched = 1;
    QString text;
    bool done = false;
    while ( start != 0 ) {
        while ( start >= 0 ) {
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
                done = true;
                break;
            }
            
            if ( brackets.isEmpty() && ( (c.isSpace() && ! lastWasSlice) || seperatorChars.contains(c) ) ) {
                done = true;
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
        if ( done ) {
            break;
        }
        if ( cursor.line() < linesFetched ) {
            break;
        }
        if ( brackets.isEmpty() && ! lineFetcher.fetchLine(cursor.line() - linesFetched).trimmed().endsWith('\\') ) {
            // break at newline without previous backslash
            break;
        }
        // store this line for multi-line expressions
        if ( linesFetched != 1 ) {
            text.prepend(line);
        }
        else {
            text.prepend(line.mid(0, end));
        }
        line.clear();
        while ( line.isEmpty() && cursor.line() >= linesFetched ) {
            line = lineFetcher.fetchLine(cursor.line() - linesFetched);
            linesFetched++;
            start = line.length() - 1;
        }
    }
    start = qMax(0, start);
    QString linePart;
    if ( start > end ) {
        linePart = QString();
    }
    else {
        kDebug() << line << start << end << end-start << line.length();
        linePart = line.mid(start, end-start + 1);
    }

    QString expression(linePart + text);
    expression = expression.trimmed();
    kDebug() << "expression found:" << expression;
    return expression;
}

}
