/*
    SPDX-FileCopyrightText: 2013-2015 Sven Brauch <mail@svenbrauch.de>
    SPDX-FileCopyrightText: 2016-2017 Francis Herne <mail@flherne.uk>

    SPDX-License-Identifier: LGPL-2.0-or-later
*/

#ifndef RANGEFIXVISITOR_H
#define RANGEFIXVISITOR_H

#include <QRegularExpression>

#include "astdefaultvisitor.h"

namespace Python {

/**
 * This visitor attempts to give each AST node the correct range,
 *  with workarounds for unset or incorrect (for our purposes) ranges
 *  that are supplied by the CPython parser.
 */
class KDEVPYTHONPARSER_NO_EXPORT RangeFixVisitor : public AstDefaultVisitor {
public:
    RangeFixVisitor(const QString& contents) : lines(contents.split(QLatin1Char('\n'))) {};
    void visitNode(Ast* node) override;
    void visitCode(Python::CodeAst* node) override;
    void visitFunctionDefinition(FunctionDefinitionAst* node) override;
    void visitClassDefinition(ClassDefinitionAst* node) override;
    void visitAttribute(AttributeAst* node) override;
    void visitImport(ImportAst* node) override;
    void visitExceptionHandler(ExceptionHandlerAst* node) override;
    void visitString(Python::StringAst* node) override;
    void visitBytes(Python::BytesAst* node) override;
    void visitFormattedValue(Python::FormattedValueAst * node) override;
    void visitNumber(Python::NumberAst* node) override;
    void visitSubscript(Python::SubscriptAst* node) override;
    void visitComprehension(Python::ComprehensionAst* node) override;
    void visitList(Python::ListAst* node) override;
    void visitTuple(Python::TupleAst* node) override;

private:
    void cutDefinitionPreamble(Ast* fixNode, const QString& defKeyword);
    int backtrackDottedName(const QString& data, const int start);
    void fixAlias(Ast* dotted, Ast* asname, const int startLine, int aliasIndex);
    int whitespaceAtEnd(const QString& line);

    const QStringList lines;
    QVector<KTextEditor::Cursor> dots;
    KTextEditor::Cursor attributeStart;
    static const QRegularExpression findString;
    static const QRegularExpression findNumber;
};

}

#endif // RANGEFIXVISITOR_H
