/*
    SPDX-FileCopyrightText: 2012 Sven Brauch svenbrauch @googlemail.com

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#include "codehelpers.h"
#include <QStack>
#include <QRegularExpression>

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

CodeHelpers::EndLocation CodeHelpers::endsInside(const QString &code)
{
    bool insideSingleLineComment = false;
    QStringList stringDelimiters;
    stringDelimiters << "\"\"\"" << "\'\'\'" << "'" << "\"";
    QStack<QString> stringStack;
    const int max_len = code.length();
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
        for ( const QString& check : stringDelimiters ) {
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

    if ( ! stringStack.isEmpty() ) {
        return String;
    }
    else if ( insideSingleLineComment ) {
        return Comment;
    }

    return Code;
}

QString CodeHelpers::killStrings(QString stringWithStrings)
{
    QRegularExpression replaceStrings(QStringLiteral("(\".*\"|\'.*\'|\"\"\".*\"\"\"|\'\'\'.*\'\'\')"),
                                      QRegularExpression::InvertedGreedinessOption);
    QString stripped = stringWithStrings.replace(replaceStrings, QStringLiteral("\"S\""));
    return stripped;
}

QString CodeHelpers::expressionUnderCursor(Python::LazyLineFetcher& lineFetcher, KTextEditor::Cursor cursor,
                                           KTextEditor::Cursor& startCursor, bool forceScanExpression)
{
    startCursor = cursor;
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
    QStringList seperatorChars = QStringList() << "," << "=" << ":" << "*" << "-" << "+" << "/" << "%" << "^" << "~";
    QStack<QString> brackets;
    bool lastWasSlice = false;
    int linesFetched = 1;
    QString text;
    bool done = false;
    while ( start != 0 ) {
        while ( start >= 0 ) {
            QChar c = line[start];
            int bracket = closingBrackets.indexOf(c);
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
        linePart = line.mid(start, end-start + 1);
        startCursor.setColumn(start);
    }

    QString expression(linePart + text);
    expression = expression.trimmed();
    return expression;
}

QString CodeHelpers::extractStringUnderCursor(const QString &code, KTextEditor::Range range, KTextEditor::Cursor cursor, int *cursorPositionInString = nullptr)
{
    QPair<QString, QString> beforeAndAfter = splitCodeByCursor(code, range, cursor);

    // TODO is this even necessary?
    if ( endsInside(beforeAndAfter.first) != String ) {
        return QString();
    }

    QStringList quoteCharacters = QStringList() << "\"" << "'";

    // using a stack is probably overkill for this...
    QStack<QString> quotes;
    QString string;

    int start = beforeAndAfter.first.size() - 1;


    while ( start >= 0 ) {
        QChar c = beforeAndAfter.first.at(start);
        int quote = quoteCharacters.indexOf(c);

        // if we've found a quote character and we're either at the beginning of the code or the previous char is not a backslash
        if ( quote != -1 && (start == 0 || (start != 0 && beforeAndAfter.first.at(start - 1) != '\\')) ) {
            if ( endsInside(beforeAndAfter.first.left(start)) != String ) {
                quotes.push(quoteCharacters.at(quote));
                break;
            }
        }

        start--;
    }

    int end = start + 1;

    while ( ! quotes.isEmpty() && end < beforeAndAfter.first.size() + beforeAndAfter.second.size() ) {
        QChar c;
        if (end < beforeAndAfter.first.size()) {
            c = beforeAndAfter.first.at(end);
        }
        else {
            c = beforeAndAfter.second.at(end - beforeAndAfter.first.size());
        }

        if (c == '\\') {
            end += 2;
        }

        if ( quotes.top() == c ) {
            quotes.pop();
        }

        end++;
    }

    string = code.mid(start, end - start);

    if ( cursorPositionInString ) {
        *cursorPositionInString = beforeAndAfter.first.size() - start;
    }

    return string;
}

QPair<QString, QString> CodeHelpers::splitCodeByCursor(const QString &code, KTextEditor::Range range, KTextEditor::Cursor cursor)
{
    QStringList lines = code.split('\n');

    int position = 0;
    bool firstRow = true;
    int startColumn = range.start().column();
    int endColumn;
    for ( int row = range.start().line(), i = 0; row <= cursor.line(); row++, i++ ) {
        if ( row != cursor.line() ) {
            if ( i >= lines.size() ) {
                // something went wrong with the context ranges
                break;
            }
            endColumn = lines.at(i).size();
        }
        else {
            endColumn = cursor.column();
        }

        position += endColumn - startColumn + 1;

        if ( firstRow ) {
            startColumn = 0;
            firstRow = false;
        }
    }

    QString before(code.mid(0, position - 1));
    QString after(code.mid(position - 1, code.size() - position + 1));

    return QPair<QString, QString>(before, after);
}

}
