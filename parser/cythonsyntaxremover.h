/***************************************************************************
 *   This file is part of KDevelop                                         *
 *   Copyright 2014 Gregor Vollmer <gregor@celement.de>                    *
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU Library General Public License as       *
 *   published by the Free Software Foundation; either version 2 of the    *
 *   License, or (at your option) any later version.                       *
 *                                                                         *
 *   This program is distributed in the hope that it will be useful,       *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
 *   GNU General Public License for more details.                          *
 *                                                                         *
 *   You should have received a copy of the GNU Library General Public     *
 *   License along with this program; if not, write to the                 *
 *   Free Software Foundation, Inc.,                                       *
 *   51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.         *
 ***************************************************************************/


#ifndef CYTHONSYNTAXREMOVER_H
#define CYTHONSYNTAXREMOVER_H


#include "parserexport.h"
#include <QString>
#include <QStringList>
#include <language/editor/simplerange.h>


namespace Python {

class CodeAst;
class FileIndentInformation;

// Parse code in a pyx file and remove Cython specific syntax.
// The results can be to used to build the Python AST.
// This class then can be used to fix the identifier ranges
// in the AST to recognize the removed code parts.
class KDEVPYTHONPARSER_EXPORT CythonSyntaxRemover {

public:
    enum TOKEN_TYPE {
        NO_TOKEN,
        TOKEN_ID,
        TOKEN_COMMA,
        TOKEN_END,
        TOKEN_DEFAULT_ARGUMENT
    };

    struct Token {
        TOKEN_TYPE type;
        KDevelop::SimpleRange range;
    };

    struct DeletedCode {
        QString code;
        KDevelop::SimpleRange range;
    };

    QString stripCythonSyntax(const QString& code);
    void fixAstRanges(CodeAst* ast);

private:
    bool fixFunctionDefinitions(QString& line);
    bool fixExtensionClasses(QString& line);
    bool fixVariableTypes(QString& line);
    bool fixCdefBlocks(QString& line);
    bool fixCimports(QString& line);
    bool fixCtypedefs(QString& line);
    bool fixCompileTimeStatements(QString& line);

    QVector<KDevelop::SimpleRange> getArgumentListTypes();
    QVector<Token> getArgumentListTokens();

    QStringList m_code;
    QString m_strippedCode;
    KDevelop::SimpleCursor m_offset;
    QVector<DeletedCode> m_deletions;
    QScopedPointer<FileIndentInformation> m_indents;
};

}

#endif // CYTHONSYNTAXREMOVER_H
