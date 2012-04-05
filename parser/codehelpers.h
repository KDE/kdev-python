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
        static QString expressionUnderCursor(LazyLineFetcher& lineFetcher, KTextEditor::Cursor cursor);
    };
}

#endif // CODEHELPERS_H

class C;
