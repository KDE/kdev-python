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


#ifndef CODEHELPERS_H
#define CODEHELPERS_H
#include <QString>
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
    int nextChange(int line, ChangeTypes type, ScanDirection direction = Forward) const;
private:
    QList<int> m_indents;
    void initialize(const QStringList& lines);
};

class KDEVPYTHONPARSER_EXPORT CodeHelpers
{
    public:
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
                                             bool forceScanExpression = false);
        
        /**
         * @brief Replaces all quoted strings with "S" in the given expression.
         * TODO this does not work correctly, I think.
         * 
         * @param stringWithStrings some python code which may contain strings
         * @return QString the input code, with all strings replaced by "S", so 'foo("fancy\"\"\"''__/string")' -> 'foo("S")'
         **/
        static QString killStrings(QString stringWithStrings);
        
        /**
         * @brief Check whether the given code ends inside a comment or string literal.
         **/
        static bool endsInsideCommend(const QString& code);
    };
}

#endif // CODEHELPERS_H

class C;
