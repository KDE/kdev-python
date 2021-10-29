/*
    SPDX-FileCopyrightText: 2014 Gregor Vollmer <gregor@celement.de>

    SPDX-License-Identifier: LGPL-2.0-or-later
*/

#include "cythonsyntaxremover.h"
#include "astdefaultvisitor.h"
#include "codehelpers.h"
#include <QRegExp>

#include <KTextEditor/Range>

#include <QDebug>
#include "parserdebug.h"

using namespace KDevelop;

namespace Python {

// Updates the cursors for all nodes if they fall on a line
// where parts where deleted.
class CythonDeletionFixVisitor : public AstDefaultVisitor {
public:
    CythonDeletionFixVisitor(const QVector<CythonSyntaxRemover::DeletedCode>& deletedRanges)
      : m_deletedRanges() {

        for (const auto& del: deletedRanges) {
            // TODO: Multi-line deletes, handle them, possible?
            if (del.range.start().line() == del.range.end().line()) {
                m_deletedRanges[del.range.start().line()].append(del.range);
            }
        }
        // sort by column for faster access
        for (auto it = m_deletedRanges.begin();
             it !=  m_deletedRanges.end();
             it++) {
            std::sort(it.value().begin(),  it.value().end());
        }
    }

    void visitIdentifier(Identifier* node) override {
        if (node) {
            fixIdentifier(node);
        }
    }

    void fixIdentifier(Identifier* name) {
        if (!m_deletedRanges.contains(name->startLine)) {
            return;
        }
        for (auto range: m_deletedRanges[name->startLine]) {
            if (name->startCol >= range.start().column()) {
                name->startCol += range.end().column() - range.start().column();
                if (name->startLine == name->endLine) {
                    name->endCol += range.end().column() - range.start().column();
                }
            }
            else {
                break;
            }
        }
    }


private:
    // Key is the line number of the ranges to delete.
    QMap<int, QVector<KTextEditor::Range>> m_deletedRanges;
};


QString CythonSyntaxRemover::stripCythonSyntax(const QString& code)
{
    if (!m_strippedCode.isEmpty()) {
        return m_strippedCode;
    }
    m_code = code.split("\n");

    // Search through code line by line and try to detect
    // Cython specific syntax. Delete these syntax elements and
    // remember the deleted positions.
    // Check every line quickly for hints that Cython syntax
    // is used and then find the correct replacement via
    // regular expressions.
    for (m_offset.setPosition(0, 0);
         m_offset.line() < m_code.length();
         m_offset.setLine(m_offset.line()+1), m_offset.setColumn(0)) {
        QString& line = m_code[m_offset.line()];
        if (fixFunctionDefinitions(line)) continue;
        if (fixExtensionClasses(line)) continue;
        if (fixVariableTypes(line)) continue;
        if (fixCimports(line)) continue;
        if (fixCtypedefs(line)) continue;
    }
    return m_strippedCode = m_code.join("\n");
}

bool CythonSyntaxRemover::fixFunctionDefinitions(QString& line)
{
    // Regular Expression Explanation
    // find a line looking roughly like:
    //   XXdef RETURN_TYPE FunctionName(
    //   XXdef FunctionName(
    // A typical Cython function definition.
    // Warning: Matches extension class definitions, too!
    static QRegExp regexp_cdef_function("^\\s*((def|cdef|cpdef)\\s+([\\.a-zA-Z0-9_]+\\**\\s+)?)[a-zA-Z0-9_]+\\s*\\(");
    if (regexp_cdef_function.indexIn(line) != -1) {
        auto wholeMatch = regexp_cdef_function.cap(0);
        auto definition = regexp_cdef_function.cap(2);
        auto definitionPos = regexp_cdef_function.pos(2);
        auto returnType = regexp_cdef_function.cap(3);
        auto returnTypePos = regexp_cdef_function.pos(3);
        if (returnType == QString("class")) {
            // if the "return type" is class, the regexp falsely detected
            // a class definition for a derived class.
            return false;
        }
        qCDebug(KDEV_PYTHON_PARSER) << "Function, replace" << definition
            << "and remove return type: " << returnType;
        // from the beginning of the argument list (open paren),
        // replace type specifiers (if available).
        m_offset.setColumn(wholeMatch.length());
        qCDebug(KDEV_PYTHON_PARSER) << "Regex ended at offset" << m_offset;
        auto types = getArgumentListTypes();
        for (int i = types.size()-1; i >= 0; i--) {
            auto range = types[i];
            qCDebug(KDEV_PYTHON_PARSER) << "Replace" << range.start().line() << ":" << range.start().column() << " to " << range.end().line() << ":" << range.end().column() << m_code[range.start().line()].mid(range.start().column(), range.end().column() - range.start().column());
            QString white = QString(" ").repeated(range.end().column() - range.start().column());
            m_code[range.start().line()].replace(range.start().column(), white.length(), white);
        }
        // Find range of syntax for return values in case an exception occurs
        // Syntax: "cdef foo(bar) except (EXPRESSION,*):"
        auto start = m_offset;
        while (m_code[m_offset.line()][m_offset.column()] != ':') {
            m_offset.setColumn(m_offset.column() + 1);
            if (m_offset.column() >= m_code.at(m_offset.line()).length()) {
                m_offset.setLine(m_offset.line()+1);
                m_offset.setColumn(0);
                if(m_offset.line() >= m_code.length()) {
                    m_offset.setLine(m_code.length() - 1);
                    m_offset.setColumn(m_code[m_offset.line()].length() - 1);
                    break;
                }
            }
        }
        // replace the exception definition
        if (start.line() == m_offset.line() && start.column() < m_offset.column()) {
            auto exceptionDefLen = m_offset.column() - start.column();
            auto exceptionDef = m_code.at(m_offset.line()).mid(start.column(), exceptionDefLen);
            if(exceptionDef.indexOf(QString("except")) != -1) {
                m_deletions.append(DeletedCode{exceptionDef, {start, m_offset}});
                m_code[start.line()].remove(start.column(), exceptionDefLen);
            }
            else {
                // probably the closing ":" was not typed yet, recover m_offset
                m_offset = start;
            }
        }
        // replace multiline expression...
        else if (start.line() < m_offset.line()) {
            auto pos = start;
            QString exceptionDef;
            bool foundExceptKeyword = false;
            for (; pos.line() < m_offset.line() && pos.line() < m_code.length(); pos.setLine(pos.line()+1), pos.setColumn(0)) {
                QString& curLine = m_code[pos.line()];
                exceptionDef.append(curLine.mid(pos.column(), curLine.length() - pos.column()));
                // replace with ":" if there is an offset to start of line. This is the
                // case for the first line
                qCDebug(KDEV_PYTHON_PARSER) << "foundExceptKeyword?" << foundExceptKeyword << "curLine.indexOf(\"except\")" << curLine.indexOf("except");
                if(foundExceptKeyword || curLine.indexOf("except") != -1) {
                    foundExceptKeyword = true;
                    curLine.replace(pos.column(), curLine.length() - pos.column(),
                                    pos.column() ? QStringLiteral(":") : QString());
                }
                else {
                    // first line of "exception def" did not contain except
                    // keyword, probably the closing : was not typed.
                    // Recover m_offset
                    m_offset = start;
                    break;
                }
            }
            if(foundExceptKeyword) {
                QString& curLine = m_code[m_offset.line()];
                // remove one more char than offset points to, we don't want to keep
                // the : in the multiline case
                m_offset.setColumn(m_offset.column() + 1);
                exceptionDef.append(curLine.mid(0, m_offset.column()));
                curLine.remove(0,  m_offset.column());
                m_deletions.append(DeletedCode{exceptionDef, {start, m_offset}});
            }
        }
        // if a return type was specified, delete it from code
        if (returnTypePos != -1) {
            auto delrange = KTextEditor::Range(start.line(), returnTypePos,
                                               start.line(), returnTypePos + returnType.length());
            m_deletions.append(DeletedCode{returnType, delrange});
            line.remove(returnTypePos,
                        returnType.length());
        }
        // if the keyword is not def (but cdef, cpdef ...),  replace it
        if (definition != QString("def")) {
            auto delrange = KTextEditor::Range(start.line(), definitionPos,
                                               start.line(), definitionPos + definition.length()-3);
            m_deletions.append(DeletedCode{definition, delrange});
            line.replace(definitionPos,
                        definition.length(),
                        "def");
        }
        return true;
    }
    return false;
}

bool CythonSyntaxRemover::fixExtensionClasses(QString& line)
{
    // Regular Expression Explanation
    // Matches an extension class definition
    //   cdef class ClassName
    static QRegExp regexp_cdef_class("^\\s*(cdef\\s+)class");
    if (regexp_cdef_class.indexIn(line) != -1) {
        auto definition = regexp_cdef_class.cap(1);
        auto definition_pos = regexp_cdef_class.pos(1);
        qCDebug(KDEV_PYTHON_PARSER) << "Extension class, remove " << definition;
        auto delrange = KTextEditor::Range(m_offset.line(), definition_pos,
                                           m_offset.line(), definition_pos+definition.length());
        m_deletions.append(DeletedCode{regexp_cdef_class.cap(1), delrange});
        line.remove(definition_pos,
                    definition.length());
        return true;
    }
    return false;
}

bool CythonSyntaxRemover::fixVariableTypes(QString& line)
{
    // Regular Expression Explanation
    // Matches a variable type specification
    //   cdef TYPE VarName
    //   cdef TYPE Var1, Var2, [...]
    // TODO: Handle cases such as
    //   cdef TYPE Var1=0, Var2=4
    static QRegExp regexp_cdef_variable("^(\\s*)cdef\\s+[\\.a-zA-Z0-9_]+(\\[[^\\]]+\\])?\\s*\\**\\s*[a-zA-Z0-9_]+\\s*(,\\s*[a-zA-Z0-9_]+\\s*)*");
    if (regexp_cdef_variable.indexIn(line) != -1) {
        qCDebug(KDEV_PYTHON_PARSER) << "Variable cdef -> pass";
        auto delrange = KTextEditor::Range(m_offset.line(), 0,
                                           m_offset.line(), line.length()-regexp_cdef_variable.cap(1).length()-4);
        m_deletions.append(DeletedCode{line, delrange});
        line = regexp_cdef_variable.cap(1);
        line += QString("pass");
        return false;
    }
    return false;
}

bool CythonSyntaxRemover::fixCimports(QString& line)
{
    // Regular Expression Explanation
    // ... self explanatory
    static QRegExp regexp_cimport_a("^from .+ cimport");
    static QRegExp regexp_cimport_b("^cimport");
    regexp_cimport_a.setMinimal(true);
    if (regexp_cimport_a.indexIn(line) != -1 ||
        regexp_cimport_b.indexIn(line) != -1) {
        auto delrange = KTextEditor::Range(m_offset.line(), 0, m_offset.line(), line.length());
        m_deletions.append(DeletedCode{line, delrange});
        line.clear();
        return true;
    }
    return false;
}

bool CythonSyntaxRemover::fixCtypedefs(QString& line)
{
    // Regular Expression Explanation
    // remove lines starting with
    //   ctypedef
    // until a hash # is reached
    static QRegExp regexp_ctypedef("^(\\s*ctypedef\\s+[^#]+)");
    if (regexp_ctypedef.indexIn(line) != -1) {
        line.remove(regexp_ctypedef.pos(1),
                    regexp_ctypedef.cap(1).length());
        auto typeDef = regexp_ctypedef.cap(1);
        auto typeDefPos = regexp_ctypedef.pos(1);
        auto delrange = KTextEditor::Range(m_offset.line(), typeDefPos,
        m_offset.line(), regexp_ctypedef.pos(1) + typeDef.length());
        m_deletions.append(DeletedCode{typeDef, delrange});
        return true;
    }
    return false;
}

QVector<KTextEditor::Range> CythonSyntaxRemover::getArgumentListTypes()
{
    QVector<KTextEditor::Range> type_specifiers;
    auto token_list(getArgumentListTokens());
    // if there are consecutive IDs, the first ID is the type specifier
    for (int i = 0; i < token_list.size()-1; i++) {
        if (token_list.at(i).type == TOKEN_ID &&
            token_list.at(i+1).type == TOKEN_ID) {
            type_specifiers.append(token_list[i].range);
        }
    }
    return type_specifiers;
}

QVector<CythonSyntaxRemover::Token> CythonSyntaxRemover::getArgumentListTokens()
{
    auto range = KTextEditor::Range(m_offset, m_offset);
    QVector<CythonSyntaxRemover::Token> token_list;
    bool stop_tokenizer = false;
    while (!stop_tokenizer) {
        // did we reach end of line?
        // continue to next line until we hit non-empty line
        while (m_offset.column() >= m_code[m_offset.line()].length()) {
            if (m_offset.line() >= m_code.length()-1) {
                break;
            }
            m_offset.setColumn(0);
            m_offset.setLine(m_offset.line() + 1);
            range.setStart(m_offset);
            range.setEnd(m_offset);
        }
        QChar c = m_code.at(m_offset.line()).at(m_offset.column());
        m_offset.setColumn(m_offset.column() + 1);
        if (c.isSpace()) {
            range.setStart(m_offset);
            range.setEnd(m_offset);
        }
        else if (c == '=') {
            range.setEnd(range.end() + KTextEditor::Cursor(0, 1));
            int open_paren_count = 0;
            bool in_string = false;
            // while there are open parenthesis or if we are in
            // string mode and the current character does not terminate
            // the token, consume!
            c = m_code.at(m_offset.line()).at(m_offset.column());
            m_offset.setColumn(m_offset.column() + 1);
            while (open_paren_count > 0 || in_string ||
                   !(c == ',' || c == ')')) {
                if (m_offset.column() >= m_code.at(m_offset.line()).length()) {
                    if (m_offset.line() >= m_code.length()) {
                        m_offset.setColumn(m_offset.column() - 1);
                        break;
                    }
                    m_offset.setLine(m_offset.line() + 1);
                    m_offset.setColumn(0);
                }
                range.setEnd(m_offset);
                // TODO: Support for """ """ multiline strings.
                // Maybe implicitly contained?
                if (c == '"') {
                    if (in_string && m_offset.column() >= 2)
                        in_string = (m_code.at(m_offset.line()).at(m_offset.column()-2) == '\\');
                    else
                        in_string = !in_string;
                }
                else if (!in_string && c == '(')
                    open_paren_count++;
                else if (!in_string && c == ')')
                    open_paren_count--;
                c = m_code.at(m_offset.line()).at(m_offset.column());
                m_offset.setColumn(m_offset.column() + 1);
            }
            m_offset.setColumn(m_offset.column() - 1);
            range.setEnd(m_offset);
            token_list.append({TOKEN_DEFAULT_ARGUMENT, range});
            range.setStart(range.end());
        }
        else if (c == ',') {
            range.setEnd(m_offset);
            token_list.append({TOKEN_COMMA, range});
            range.setStart(range.end());
        }
        else if (c == ')') {
            stop_tokenizer = true;
            range.setEnd(m_offset);
            token_list.append({TOKEN_END, range});
            range.setStart(range.end());
        }
        else {
            int open_bracket_count = 0;
            c = m_code.at(m_offset.line()).at(m_offset.column());
            m_offset.setColumn(m_offset.column()+1);
            // stop consuming the input if there are no closing
            // square brackets left and the current character is
            // whitespace, =,  ,, ) or the end of line.
            while ((!c.isSpace()
                    && m_offset.column() < m_code.at(m_offset.line()).length()
                    && c != ')' && c != ',' && c != '=') || open_bracket_count > 0) {
                if (c == '[') {
                    open_bracket_count++;
                }
                else if (c == ']') {
                    open_bracket_count--;
                }
                c = m_code.at(m_offset.line()).at(m_offset.column());
                m_offset.setColumn(m_offset.column() + 1);
            }
            m_offset.setColumn(m_offset.column() - 1);
            range.setEnd(m_offset);
            token_list.append({TOKEN_ID, range});
            range.setStart(range.end());
        }
    }
    return token_list;
}

void CythonSyntaxRemover::fixAstRanges(CodeAst* ast)
{
    if (!m_deletions.isEmpty()) {
        CythonDeletionFixVisitor visit(m_deletions);
        visit.visitNode(ast);
    }
}


}
