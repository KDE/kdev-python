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


#ifndef CODEHELPERS_H
#define CODEHELPERS_H
#include <QString>
#include <QStringList>
#include <KTextEditor/Document>
#include "parserexport.h"

namespace Python {
    
// helper class that lazy fetches lines from a document, for performance gain
class KDEVPYTHONPARSER_EXPORT LazyLineFetcher {
public:
    virtual QString fetchLine(int lineno) = 0;
    virtual ~LazyLineFetcher() { };
};

class KDEVPYTHONPARSER_EXPORT TrivialLazyLineFetcher : public LazyLineFetcher {
public:
    TrivialLazyLineFetcher(QStringList lines) : m_lines(lines) { }
    virtual QString fetchLine(int lineno) {
        return m_lines.at(lineno);
    };
private:
    QStringList m_lines;
};

class KDEVPYTHONPARSER_EXPORT TextDocumentLazyLineFetcher : public LazyLineFetcher {
public:
    TextDocumentLazyLineFetcher(KTextEditor::Document* d) :
      m_document(d) { };
    QString fetchLine(int lineno) {
        return m_document->line(lineno);
    };
private:
    KTextEditor::Document* m_document;
};

class KDEVPYTHONPARSER_EXPORT FileIndentInformation {
public:
    FileIndentInformation(const QStringList& lines);
    FileIndentInformation(KTextEditor::Document* document);
    FileIndentInformation(const QByteArray& data);
    FileIndentInformation(const QString& data);
    
    enum ScanDirection {
        Forward,
        Backward
    };
    
    enum ChangeTypes {
        Indent,
        Dedent,
        AnyChange
    };
    
    int indentForLine(int line) const;
    int linesCount() const;
    int nextChange(int line, ChangeTypes type, ScanDirection direction = Forward) const;
private:
    QList<int> m_indents;
    void initialize(const QStringList& lines);
};

class KDEVPYTHONPARSER_EXPORT CodeHelpers
{
    public:
        enum EndLocation {
            Code,
            String,
            Comment
        };

        CodeHelpers();
        /**
         * @brief Get the python expression at the specified cursor.
         *
         * @param lineFetcher An object which is used to get lines from the document
         * @param cursor where to search for the expression
         * @param forceScanExpression Start scanning even if the first char is non-alphanumeric. Defaults to false.
         * @return QString the expression which was found, as string.
         **/
        static QString expressionUnderCursor(LazyLineFetcher& lineFetcher, KTextEditor::Cursor cursor,
                                             KTextEditor::Cursor& start, bool forceScanExpression = false);
        
        /**
         * @brief Replaces all quoted strings with "S" in the given expression.
         * TODO this does not work correctly, I think.
         * 
         * @param stringWithStrings some python code which may contain strings
         * @return QString the input code, with all strings replaced by "S", so 'foo("fancy\"\"\"''__/string")' -> 'foo("S")'
         **/
        static QString killStrings(QString stringWithStrings);
        
        /**
         * @brief Check whether the given code ends inside a comment.
         **/
        static EndLocation endsInside(const QString &code);

        /**
         * @brief Extracts the string which is under the cursor, if one is present
         *
         * @param code the code, which to scan
         * @param range the range in the document, which contains this code
         * @param cursor the location of the cursor in the document
         * @param cursorPositionInString optional return value, which is set to
         *        the relative position of the cursor inside the string
         * @return The string under the cursor, or an empty string if none is available.
         */
        static QString extractStringUnderCursor(const QString &code, KTextEditor::Range range, KTextEditor::Cursor cursor, int *cursorPositionInString);

        /**
         * @brief Splits the given code, which is assumed to be contained in
         *        the range provided range, in two pieces: before and after the
         *        cursor.
         * @param code some code to split
         * @param range the range in the document, which contains this code
         * @param cursor the location of the cursor in the document
         * @return A pair of strings, containing the code and the code after
         *         the cursor
         */
        static QPair<QString, QString> splitCodeByCursor(const QString &code, KTextEditor::Range range, KTextEditor::Cursor cursor);
};
}

#endif // CODEHELPERS_H

class C;
