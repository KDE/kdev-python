/*
    SPDX-FileCopyrightText: 2014 Gregor Vollmer <gregor@celement.de>

    SPDX-License-Identifier: LGPL-2.0-or-later
*/

#ifndef CYTHONSYNTAXREMOVER_H
#define CYTHONSYNTAXREMOVER_H


#include "parserexport.h"
#include <QString>
#include <QStringList>
#include <KTextEditor/Range>

namespace Python {

class CodeAst;

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
        KTextEditor::Range range;
    };

    struct DeletedCode {
        QString code;
        KTextEditor::Range range;
    };

    QString stripCythonSyntax(const QString& code);
    void fixAstRanges(CodeAst* ast);

private:
    bool fixFunctionDefinitions(QString& line);
    bool fixExtensionClasses(QString& line);
    bool fixVariableTypes(QString& line);
    bool fixCimports(QString& line);
    bool fixCtypedefs(QString& line);

    QVector<KTextEditor::Range> getArgumentListTypes();
    QVector<Token> getArgumentListTokens();

    QStringList m_code;
    QString m_strippedCode;
    KTextEditor::Cursor m_offset;
    QVector<DeletedCode> m_deletions;
};

}

#endif // CYTHONSYNTAXREMOVER_H
