/*
    SPDX-FileCopyrightText: 2013-2015 Sven Brauch <mail@svenbrauch.de>
    SPDX-FileCopyrightText: 2016-2017 Francis Herne <mail@flherne.uk>

    SPDX-License-Identifier: LGPL-2.0-or-later
*/

#include "rangefixvisitor.h"

namespace Python {

class NextAstFindVisitor : public AstDefaultVisitor {
public:
    KTextEditor::Cursor findNext(Python::Ast* node) {
        m_root = node;
        auto parent = node;
        while ( parent->parent && parent->parent->isExpression() ) {
            parent = parent->parent;
        }
        visitNode(parent);

        while ( ! m_next.isValid() && parent->parent ) {
            // no next expression found in that statement, advance to the next statement
            parent = parent->parent;
            visitNode(parent);
        }

        return m_next;
    };
    void visitNode(Python::Ast* node) override {
        if ( ! node ) {
            return;
        }
        AstDefaultVisitor::visitNode(node);
        if ( node->start() > m_root->start() && ! node->isChildOf(m_root) ) {
            m_next = (m_next < node->start() && m_next.isValid()) ? m_next : node->start();
        }
    }

private:
    KTextEditor::Cursor m_next{-1, -1};
    Ast* m_root;
};


//BEGIN RangeFixVisitor
void RangeFixVisitor::visitNode(Ast* node) {
    AstDefaultVisitor::visitNode(node);
    if ( node && node->parent && node->parent->astType != Ast::AttributeAstType ) {
        if ( ( node->parent->endLine <= node->endLine && node->parent->endCol <= node->endCol )
                || node->parent->endLine < node->endLine )
        {
            node->parent->endLine = node->endLine;
            node->parent->endCol = node->endCol;
        }
    }
};

void RangeFixVisitor::visitCode(CodeAst* node) {
    node->startLine = node->startCol = 0;
    AstDefaultVisitor::visitCode(node);
}

void RangeFixVisitor::visitFunctionDefinition(FunctionDefinitionAst* node) {
    cutDefinitionPreamble(node->name, node->async ? QStringLiteral("asyncdef") : QStringLiteral("def"));
    AstDefaultVisitor::visitFunctionDefinition(node);
};

void RangeFixVisitor::visitClassDefinition(ClassDefinitionAst* node) {
    cutDefinitionPreamble(node->name, QStringLiteral("class"));
    AstDefaultVisitor::visitClassDefinition(node);
};

void RangeFixVisitor::visitAttribute(AttributeAst* node) {
    // Work around the weird way to count columns in Python's AST module.

    // Find where the next expression (of any kind) behind this one starts
    NextAstFindVisitor v;
    auto next_start = v.findNext(node);
    if ( ! next_start.isValid() ) {
        // use end of document as reference
        next_start = {static_cast<int>(lines.size() - 1), static_cast<int>(lines.last().size() - 1)};
    }

    // take only the portion of the line up to that next expression
    auto endLine = next_start.line();
    auto endCol = next_start.column();
    if ( ! (next_start > node->start()) ) {
        endLine = node->startLine;
        endCol = -1;
    }

    const QString& name(node->attribute->value);

    QString line;
    for ( int n = node->startLine,
                pos = node->value->endCol + 1,
                dotFound = false,
                nameFound = false;
            n <= endLine; ++n, pos = 0 ) {
        line = lines.at(n);
        if ( n == endLine && endCol != -1 ) {
            // Never look at the next expression.
            line = line.left(endCol);
        }
        if ( !dotFound ) {
            // The real attr name can never be before a dot.
            // Nor can the start of a comment.
            // (Don't be misled by `foo["bar"].bar` or `foo["#"].bar`)
            pos = line.indexOf(QLatin1Char('.'), pos);
            if ( pos == -1 ) continue;
            dotFound = true;
        }
        if ( !nameFound ) {
            // Track if the attr name has appeared at least once.
            // This helps avoid RangeFixVisitor::interpreting '#'s in strings as comments -
            //   there can never be a comment before the real attr name.
            pos = line.indexOf(name, pos + 1);
            if ( pos == -1 ) continue;
            nameFound = true;
        }
        if ( dotFound && nameFound &&
                (pos = line.indexOf(QLatin1Char('#'), pos + name.length())) != -1) {
            // Remove the comment after a '#' iff we're certain it can't
            //  be inside a string literal (e.g. `foo["#"].bar`).
            line = line.left(pos);
        }
        // Take the last occurrence, any others are in string literals.
        pos = line.lastIndexOf(name);
        if ( pos != -1 ) {
            node->startLine = n;
            node->startCol = pos;
        }
        // N.B. we do this for all lines, the last non-comment occurrence
        //  is the real one.
    }
    // This fails (only, AFAIK) in a very limited case:
    // If the value expression (`foo` in `foo.bar`) contains a dot, the
    //   attr name, _and_ a hash in that order (may not be consecutive),
    //   and the hash is on the same line as the real attr name,
    //   we wrongly interpret the hash as the start of a comment.
    // e.g `foo["...barrier#"].bar` will highlight part of the string.

    node->endLine = node->startLine;
    node->endCol = node->startCol + name.length() - 1;
    node->attribute->copyRange(node);

    AstDefaultVisitor::visitAttribute(node);
};

// alias for imports (import foo as bar, baz as bang)
// no strings, brackets, or whatever are allowed here, so the "parser"
// can be very straightforward.
void RangeFixVisitor::visitImport(ImportAst* node) {
    AstDefaultVisitor::visitImport(node);
    int aliasIndex = 0;
    for ( AliasAst* alias: node->names ) {
        fixAlias(alias->name, alias->asName, node->startLine, aliasIndex);
        aliasIndex += 1;
    }
};

// alias for exceptions (except FooBarException as somethingterriblehappened: ...)
void RangeFixVisitor::visitExceptionHandler(ExceptionHandlerAst* node) {
    AstDefaultVisitor::visitExceptionHandler(node);
    if ( ! node->name ) {
        return;
    }
    const QString& line = lines.at(node->startLine);
    const int end = line.size() - 1;
    int back = backtrackDottedName(line, end);
    node->name->startCol = end - back;
    node->name->endCol = end;
}

void RangeFixVisitor::visitString(Python::StringAst* node) {
    AstDefaultVisitor::visitString(node);
    auto match = findString.match(lines.at(node->startLine), node->startCol);
    if ( match.capturedLength() > 0 ) {
        node->endCol += match.capturedLength() - 1; // Ranges are inclusive.
    }
}
void RangeFixVisitor::visitBytes(Python::BytesAst* node) {
    AstDefaultVisitor::visitBytes(node);
    auto match = findString.match(lines.at(node->startLine), node->startCol + 1);
    if ( match.capturedLength() > 0 ) {
        node->endCol += match.capturedLength(); // -1 then +1, because of the 'b'.
    }
}
void RangeFixVisitor::visitFormattedValue(Python::FormattedValueAst * node) {
    AstDefaultVisitor::visitFormattedValue(node);
    auto match = findString.match(lines.at(node->startLine), node->startCol + 1);
    if ( match.capturedLength() > 0 ) {
        node->endCol += match.capturedLength();
    }
}

void RangeFixVisitor::visitNumber(Python::NumberAst* node) {
    AstDefaultVisitor::visitNumber(node);
    auto match = findNumber.match(lines.at(node->startLine), node->startCol);
    if ( match.capturedLength() > 0 ) {
        node->endCol += match.capturedLength() - 1; // Ranges are inclusive.
    }
}

// Add one column after the last child to cover the closing bracket: `[1,2,3]`
// TODO This is still wrong if the last child is followed by parens or whitespace.
// endCol matters most in single-line expressions, so this isn't a huge problem.
void RangeFixVisitor::visitSubscript(Python::SubscriptAst* node) {
    AstDefaultVisitor::visitSubscript(node);
    node->endCol++;
}
void RangeFixVisitor::visitComprehension(Python::ComprehensionAst* node) {
    AstDefaultVisitor::visitComprehension(node);
    node->endCol++;
}
void RangeFixVisitor::visitList(Python::ListAst* node) {
    AstDefaultVisitor::visitList(node);
    node->endCol++;
}
void RangeFixVisitor::visitTuple(Python::TupleAst* node) {
    AstDefaultVisitor::visitTuple(node);
    node->endCol++;
}

// skip the decorators and the "def" at the beginning
// of a class or function declaration and modify @arg node
// example:
//  @decorate(foo)
//  @decorate(bar)
//  class myclass(parent): pass
// before: start of class->name is [0, 0]
// after: start of class->name is [2, 5]
// line continuation characters are not supported,
// because code needing those in this case is not worth being supported.
void RangeFixVisitor::cutDefinitionPreamble(Ast* fixNode, const QString& defKeyword) {
    if ( ! fixNode ) {
        return;
    }
    int currentLine = fixNode->startLine;

    // cut away decorators
    while ( currentLine < lines.size() ) {
        if ( lines.at(currentLine).trimmed().remove(QLatin1Char(' ')).remove(QLatin1Char('\t')).startsWith(defKeyword) ) {
            // it's not a decorator, so stop skipping lines.
            break;
        }
        currentLine += 1;
    }
//         qDebug() << "FIX:" << fixNode->range();
    fixNode->startLine = currentLine;
    fixNode->endLine = currentLine;
//         qDebug() << "FIXED:" << fixNode->range() << fixNode->astType;

    // cut away the "def" / "class"
    int currentColumn = -1;
    if ( currentLine > lines.size() ) {
        // whops?
        return;
    }
    const QString& lineData = lines.at(currentLine);
    bool keywordFound = false;
    while ( currentColumn < lineData.size() - 1 ) {
        currentColumn += 1;
        if ( lineData.at(currentColumn).isSpace() ) {
            // skip space at the beginning of the line
            continue;
        }
        else if ( keywordFound ) {
            // if the "def" / "class" was already found, and the current char is
            // non space, then this is indeed the start of the identifier we're looking for.
            break;
        }
        else {
            keywordFound = true;
            currentColumn += defKeyword.size();
        }
    }
    const int previousLength = fixNode->endCol - fixNode->startCol;
    fixNode->startCol = currentColumn;
    fixNode->endCol = currentColumn + previousLength;
};

int RangeFixVisitor::backtrackDottedName(const QString& data, const int start) {
    bool haveDot = true;
    bool previousWasSpace = true;
    for ( int i = start - 1; i >= 0; i-- ) {
        if ( data.at(i).isSpace() ) {
            previousWasSpace = true;
            continue;
        }
        if ( data.at(i) == QLatin1Char(':') ) {
            // excepthandler
            continue;
        }
        if ( data.at(i) == QLatin1Char('.') ) {
            haveDot = true;
        }
        else if ( haveDot ) {
            haveDot = false;
            previousWasSpace = false;
            continue;
        }
        if ( previousWasSpace && ! haveDot ) {
            return start-i-2;
        }
        previousWasSpace = false;
    }
    return 0;
}

void RangeFixVisitor::fixAlias(Ast* dotted, Ast* asname, const int startLine, int aliasIndex) {
    if ( ! asname && ! dotted ) {
        return;
    }
    QString line = lines.at(startLine);
    int lineno = startLine;
    for ( int i = 0; i < line.size(); i++ ) {
        const QChar& current = line.at(i);
        if ( current == QLatin1Char('\\') ) {
            // line continuation character
            // splitting like "import foo as \ \n bar" is not supported.
            lineno += 1;
            line = lines.at(lineno);
            i = 0;
            continue;
        }
        if ( current == QLatin1Char(',') ) {
            if ( aliasIndex == 0 ) {
                // nothing found, continue below
                line = line.left(i);
                break;
            }
            // next alias expression
            aliasIndex -= 1;
        }
        if ( i > line.length() - 3 ) {
            continue;
        }
        if ( current.isSpace() && line.mid(i+1).startsWith(QStringLiteral("as")) && ( line.at(i+3).isSpace() || line.at(i+3) == QLatin1Char('\\') ) ) {
            // there's an "as"
            if ( aliasIndex == 0 ) {
                // it's the one we're looking for
                // find the expression
                if ( dotted ) {
                    int dottedNameLength = backtrackDottedName(line, i);
                    dotted->startLine = lineno;
                    dotted->endLine = lineno;
                    dotted->startCol = i-dottedNameLength;
                    dotted->endCol = i;
                }
                // find the asname
                if ( asname ) {
                    bool atStart = true;
                    int textStart = i+3;
                    for ( int j = i+3; j < line.size(); j++ ) {
                        if ( atStart && ! line.at(j).isSpace() ) {
                            atStart = false;
                            textStart = j;
                        }
                        if ( ! atStart && ( line.at(j).isSpace() || j == line.size() - 1 ) ) {
                            // found it
                            asname->startLine = lineno;
                            asname->endLine = lineno;
                            asname->startCol = textStart - 1;
                            asname->endCol = j;
                        }
                    }
                }
                return;
            }
        }
    }
    // no "as" found, use last dotted name in line
    const int end = line.size() - whitespaceAtEnd(line);
    int back = backtrackDottedName(line, end);
    dotted->startLine = lineno;
    dotted->endLine = lineno;
    dotted->startCol = end - back;
    dotted->endCol = end;
};

int RangeFixVisitor::whitespaceAtEnd(const QString& line) {
    for ( int i = 0; i < line.size(); i++ ) {
        if ( ! line.at(line.size() - i - 1).isSpace() ) {
            return i;
        }
    }
    return 0;
};

// FIXME This doesn't work for triple-quoted strings
//  (it gives length 2, which is no worse than before).
const QRegularExpression RangeFixVisitor::findString(QStringLiteral("\\G(['\"]).*?(?<!\\\\)\\g1"));
// Looser than the real spec, but since we know there *is* a valid number it finds the end ok.
const QRegularExpression RangeFixVisitor::findNumber(QStringLiteral("\\G(?:[\\d_\\.bjoxBJOX]|[eE][+-]?)*"));

}
