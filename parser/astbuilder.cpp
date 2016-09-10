/***************************************************************************
 *   This file is part of KDevelop                                         *
 *   Copyright 2007 Andreas Pakulat <apaku@gmx.de>                         *
 *   Copyright 2010-2011 Sven Brauch <svenbrauch@googlemail.com>           *
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

#include "astbuilder.h"
#include "ast.h"

#include <QStringList>
#include <QStack>
#include <QMutexLocker>
#include <language/duchain/topducontext.h>
#include <language/duchain/problem.h>
#include <language/duchain/duchain.h>

#include <memory>

#include "python_header.h"
#include "astdefaultvisitor.h"
#include "cythonsyntaxremover.h"

#include <interfaces/icore.h>
#include <interfaces/iprojectcontroller.h>
#include <interfaces/iproject.h>
#include <util/path.h>

#include <QDebug>
#include "parserdebug.h"

using namespace KDevelop;
extern grammar _PyParser_Grammar;

namespace Python
{

// Update the "end" cursors of all nodes in the given tree.
class RangeUpdateVisitor : public AstDefaultVisitor {
public:
    void visitNode(Ast* node) override {
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
};

class NextAstFindVisitor : public AstDefaultVisitor {
public:
    KTextEditor::Cursor findNext(Python::Ast* node) {
        m_root = node;
        auto parent = node;
        while ( parent && parent->parent && parent->parent->isExpression() ) {
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

// This class is used to fix some of the remaining issues
// with the ranges of objects obtained from the python parser.
// Issues addressed are:
//  1) decorators and "def" / "class" statements for classes / functions
//  2) ranges of aliases
// Both issues are easy to correct since the possible syntax is very restricted
// (no bracket matching, no strings, no nesting, ...)
// For the aliases, fortunately only imports and excepthandlers are affected;
// the "with" statement, which has more complicated syntax, provides
// the necessary information already.
//  3) attribute rangees
// Not so easy, but when starting from the end of the expression it works okay
class RangeFixVisitor : public AstDefaultVisitor {
public:
    RangeFixVisitor(const QString& contents)
        : lines(contents.split('\n')) { };
    void visitFunctionDefinition(FunctionDefinitionAst* node) override {
        cutDefinitionPreamble(node->name, node->async ? "asyncdef" : "def");
        AstDefaultVisitor::visitFunctionDefinition(node);
    };
    void visitClassDefinition(ClassDefinitionAst* node) override {
        cutDefinitionPreamble(node->name, "class");
        AstDefaultVisitor::visitClassDefinition(node);
    };

    void visitAttribute(AttributeAst* node) override {
        // Work around the weird way to count columns in Python's AST module.

        // Find where the next expression (of any kind) behind this one starts
        NextAstFindVisitor v;
        auto next_start = v.findNext(node);
        if ( ! next_start.isValid() ) {
            // use end of document as reference
            next_start = {lines.size() - 1, lines.last().size() - 1};
        }

        // take only the portion of the line up to that next expression
        QString line = lines.at(node->startLine);
        auto lineno = next_start.line();
        auto colno = next_start.column();
        if ( ! (next_start > node->start()) ) {
            colno = -1;
            lineno = node->startLine;
        }
        do {
            line = lines.at(lineno);
            if ( colno != -1 ) {
                line = line.left(colno);
            }
            colno = -1;
            lineno -= 1;
            // eventually go to previous line for multi-line expressions
        } while ( ! line.contains(node->attribute->value) && lineno >= 0 );

        node->startLine = lineno + 1;
        node->endLine = node->startLine;
        // now, just take the last occurrence of the value.
        // it is guaranteed that this is the right one, otherwise
        // that portion of the line would have been cut off above.
        node->startCol = line.lastIndexOf(node->attribute->value);
        node->endCol = node->startCol + node->attribute->value.length() - 1;
        node->attribute->copyRange(node);

        AstDefaultVisitor::visitAttribute(node);
    };

    // alias for imports (import foo as bar, baz as bang)
    // no strings, brackets, or whatever are allowed here, so the "parser"
    // can be very straightforward.
    void visitImport(ImportAst* node) override {
        AstDefaultVisitor::visitImport(node);
        int aliasIndex = 0;
        foreach ( AliasAst* alias, node->names ) {
            fixAlias(alias->name, alias->asName, node->startLine, aliasIndex);
            aliasIndex += 1;
        }
    };

    // alias for exceptions (except FooBarException as somethingterriblehappened: ...)
    void visitExceptionHandler(ExceptionHandlerAst* node) override {
        AstDefaultVisitor::visitExceptionHandler(node);
        if ( ! node->name ) {
            return;
        }
        const QString& line = lines.at(node->startLine);
        const int end = line.count() - 1;
        int back = backtrackDottedName(line, end);
        node->name->startCol = end - back;
        node->name->endCol = end;
    }

private:
    const QStringList lines;
    QVector<KTextEditor::Cursor> dots;
    KTextEditor::Cursor attributeStart;


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
    void cutDefinitionPreamble(Ast* fixNode, const QString& defKeyword) {
        if ( ! fixNode ) {
            return;
        }
        int currentLine = fixNode->startLine;

        // cut away decorators
        while ( currentLine < lines.size() ) {
            if ( lines.at(currentLine).trimmed().remove(' ').remove('\t').startsWith(defKeyword) ) {
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

    int backtrackDottedName(const QString& data, const int start) {
        bool haveDot = true;
        bool previousWasSpace = true;
        for ( int i = start - 1; i >= 0; i-- ) {
            if ( data.at(i).isSpace() ) {
                previousWasSpace = true;
                continue;
            }
            if ( data.at(i) == ':' ) {
                // excepthandler
                continue;
            }
            if ( data.at(i) == '.' ) {
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

    void fixAlias(Ast* dotted, Ast* asname, const int startLine, int aliasIndex) {
        if ( ! asname && ! dotted ) {
            return;
        }
        QString line = lines.at(startLine);
        int lineno = startLine;
        for ( int i = 0; i < line.size(); i++ ) {
            const QChar& current = line.at(i);
            if ( current == '\\' ) {
                // line continuation character
                // splitting like "import foo as \ \n bar" is not supported.
                lineno += 1;
                line = lines.at(lineno);
                i = 0;
                continue;
            }
            if ( current == ',' ) {
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
            if ( current.isSpace() && line.mid(i+1).startsWith("as") && ( line.at(i+3).isSpace() || line.at(i+3) == '\\' ) ) {
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
        const int end = line.count() - whitespaceAtEnd(line);
        int back = backtrackDottedName(line, end);
        dotted->startLine = lineno;
        dotted->endLine = lineno;
        dotted->startCol = end - back;
        dotted->endCol = end;
    };

    int whitespaceAtEnd(const QString& line) {
        for ( int i = 0; i <= line.size(); i++ ) {
            if ( ! line.at(line.size() - i - 1).isSpace() ) {
                return i;
            }
        }
        return 0;
    };
};

#include "generated.h"

QMutex AstBuilder::pyInitLock;

QString PyUnicodeObjectToQString(PyObject* obj) {
    auto pyObjectCleanup = [](PyObject* o) { if (o) Py_DECREF(o); };
    const auto strOwner = std::unique_ptr<PyObject, decltype(pyObjectCleanup)>(PyObject_Str(obj), pyObjectCleanup);
    const auto str = strOwner.get();
    if (PyUnicode_READY(str) < 0) {
        qWarning("PyUnicode_READY(%p) returned false!", (void*)str);
        return QString();
    }
    const auto length = PyUnicode_GET_LENGTH(str);
    switch(PyUnicode_KIND(str)) {
        case PyUnicode_1BYTE_KIND:
            return QString::fromLatin1((const char*)PyUnicode_1BYTE_DATA(str), length);
        case PyUnicode_2BYTE_KIND:
            return QString::fromUtf16(PyUnicode_2BYTE_DATA(str), length);
        case PyUnicode_4BYTE_KIND:
            return QString::fromUcs4(PyUnicode_4BYTE_DATA(str), length);
        case PyUnicode_WCHAR_KIND:
            qWarning("PyUnicode_KIND(%p) returned PyUnicode_WCHAR_KIND, this should not happen!", (void*)str);
            return QString::fromWCharArray(PyUnicode_AS_UNICODE(str), length);
    }
    Q_UNREACHABLE();
}

QPair<QString, int> fileHeaderHack(QString& contents, const QUrl& filename)
{
    IProject* proj = ICore::self()->projectController()->findProjectForUrl(filename);
    // the file is not in a project, don't apply hack
    if ( ! proj ) {
        return QPair<QString, int>(contents, 0);
    }
    const QUrl headerFileUrl = QUrl::fromLocalFile(proj->path().path() + "/.kdev_python_header");
    QFile headerFile(headerFileUrl.path());
    QString headerFileContents;
    if ( headerFile.exists() ) {
        headerFile.open(QIODevice::ReadOnly);
        headerFileContents = headerFile.readAll();
        headerFile.close();
        qCDebug(KDEV_PYTHON_PARSER) << "Found header file, applying hack";
        int insertAt = 0;
        bool endOfCommentsReached = false;
        bool commentSignEncountered = false;
//         bool atLineBeginning = true;
        int lastLineBeginning = 0;
        int newlineCount = 0;
        int l = contents.length();
        do {
            if ( insertAt >= l ) {
                qCDebug(KDEV_PYTHON_PARSER) << "File consist only of comments, not applying hack";
                return QPair<QString, int>(contents, 0);
            }
            if ( contents.at(insertAt) == '#' ) {
                commentSignEncountered = true;
            }
            if ( !contents.at(insertAt).isSpace() ) {
//                 atLineBeginning = false;
                if ( !commentSignEncountered ) {
                    endOfCommentsReached = true;
                }
            }
            if ( contents.at(insertAt) == '\n' ) {
//                 atLineBeginning = true;
                commentSignEncountered = false;
                lastLineBeginning = insertAt;
                newlineCount += 1;
            }
            if ( newlineCount == 2 ) {
                endOfCommentsReached = true;
            }
            insertAt += 1;
        } while ( !endOfCommentsReached );
        qCDebug(KDEV_PYTHON_PARSER) << "Inserting contents at char" << lastLineBeginning << "of file";
        contents = contents.left(lastLineBeginning) 
                   + "\n" + headerFileContents + "\n#\n" 
                   + contents.right(contents.length() - lastLineBeginning);
        qCDebug(KDEV_PYTHON_PARSER) << contents;
        return QPair<QString, int>(contents, - ( headerFileContents.count('\n') + 3 ));
    }
    else {
        return QPair<QString, int>(contents, 0);
    }
}

namespace {
struct PythonInitializer : private QMutexLocker {
    PythonInitializer(QMutex& pyInitLock):
        QMutexLocker(&pyInitLock), arena(0)
    {
            Py_InitializeEx(0);
            Q_ASSERT(Py_IsInitialized());

            arena = PyArena_New();
            Q_ASSERT(arena); // out of memory
    }
    ~PythonInitializer()
    {
        if (arena)
            PyArena_Free(arena);
        if (Py_IsInitialized())
            Py_Finalize();
    }
    PyArena* arena;
};
}

CodeAst::Ptr AstBuilder::parse(const QUrl& filename, QString &contents)
{
    qDebug() << " ====> AST     ====>     building abstract syntax tree for " << filename.path();
    
    Py_NoSiteFlag = 1;
    
    contents.append('\n');
    
    QPair<QString, int> hacked = fileHeaderHack(contents, filename);
    contents = hacked.first;
    int lineOffset = hacked.second;

    PythonInitializer pyIniter(pyInitLock);
    PyArena* arena = pyIniter.arena;

    PyCompilerFlags flags = {PyCF_SOURCE_IS_UTF8 | PyCF_IGNORE_COOKIE};

    PyObject *exception, *value, *backtrace;
    PyErr_Fetch(&exception, &value, &backtrace);

    CythonSyntaxRemover cythonSyntaxRemover;

    if (filename.fileName().endsWith(".pyx", Qt::CaseInsensitive)) {
        qCDebug(KDEV_PYTHON_PARSER) << filename.fileName() << "is probably Cython file.";
        contents = cythonSyntaxRemover.stripCythonSyntax(contents);
    }

    mod_ty syntaxtree = PyParser_ASTFromString(contents.toUtf8().data(), "<kdev-editor-contents>", file_input, &flags, arena);

    if ( ! syntaxtree ) {
        qDebug() << " ====< parse error, trying to fix";
        
        PyErr_Fetch(&exception, &value, &backtrace);
        qCDebug(KDEV_PYTHON_PARSER) << "Error objects: " << exception << value << backtrace;

        if ( ! value ) {
            qCWarning(KDEV_PYTHON_PARSER) << "Internal parser error: exception value is null, aborting";
            return CodeAst::Ptr();
        }

        PyObject_Print(value, stderr, Py_PRINT_RAW);
        
        PyObject* errorMessage_str = PyTuple_GetItem(value, 0);
        PyObject* errorDetails_tuple = PyTuple_GetItem(value, 1);
       
        if ( ! errorDetails_tuple ) {
            qCWarning(KDEV_PYTHON_PARSER) << "Error retrieving error message, not displaying, and not doing anything";
            return CodeAst::Ptr();
        }
        PyObject* linenoobj = PyTuple_GetItem(errorDetails_tuple, 1);
        errorMessage_str = PyTuple_GetItem(value, 0);
        errorDetails_tuple = PyTuple_GetItem(value, 1);
        PyObject_Print(errorMessage_str, stderr, Py_PRINT_RAW);
        
        PyObject* colnoobj = PyTuple_GetItem(errorDetails_tuple, 2);
        int lineno = PyLong_AsLong(linenoobj) - 1;
        int colno = PyLong_AsLong(colnoobj);
        
        ProblemPointer p(new Problem());
        KTextEditor::Cursor start(lineno + lineOffset, (colno-4 > 0 ? colno-4 : 0));
        KTextEditor::Cursor end(lineno + lineOffset, (colno+4 > 4 ? colno+4 : 4));
        KTextEditor::Range range(start, end);
        qCDebug(KDEV_PYTHON_PARSER) << "Problem range: " << range;
        DocumentRange location(IndexedString(filename.path()), range);
        p->setFinalLocation(location);
        p->setDescription(PyUnicodeObjectToQString(errorMessage_str));
        p->setSource(IProblem::Parser);
        m_problems.append(p);
        
        // try to recover.
        // Currently the following is tired:
        // * If the last non-space char before the error reported was ":", it's most likely an indent error.
        //   The common easy-to-fix and annoying indent error is "for item in foo: <EOF>". In that case, just add "pass" after the ":" token.
        // * If it's not, we will just comment the line with the error, fixing problems like "foo = <EOF>".
        // * If both fails, everything including the first non-empty line before the one with the error will be deleted.
        int len = contents.length();
        int currentLine = 0;
        QString currentLineContents;
        QChar c;
        QChar newline('\n');
        int emptySince = 0; int emptySinceLine = 0; int emptyLinesSince = 0; int emptyLinesSinceLine = 0;
        unsigned short currentLineIndent = 0;
        bool atLineBeginning = true;
        QList<unsigned short> indents;
        int errline = qMax(0, lineno);
        int currentLineBeginning = 0;
        for ( int i = 0; i < len; i++ ) {
            c = contents.at(i);
            if ( ! c.isSpace() ) {
                emptySince = i;
                emptySinceLine = currentLine;
                atLineBeginning = false;
                if ( indents.length() <= currentLine ) indents.append(currentLineIndent);
            }
            else if ( c == newline ) {
                if ( currentLine == errline ) {
                    atLineBeginning = false;
                }
                else {
                    currentLine += 1;
                    currentLineBeginning = i+1;
                    // this line has had content, so reset the "empty lines since" counter
                    if ( ! atLineBeginning ) {
//                         lastNonemptyLineBeginning = emptyLinesSince;
                        emptyLinesSince = i;
                        emptyLinesSinceLine = currentLine;
                    }
                    atLineBeginning = true;
                    if ( indents.length() <= currentLine ) indents.append(currentLineIndent);
                    currentLineIndent = 0;
                }
            }
            else if ( atLineBeginning ) {
                currentLineIndent += 1;
            }
            
            if ( currentLine == errline && ! atLineBeginning ) {
                // if the last non-empty char before the error opens a new block, it's likely an "empty block" problem
                // we can easily fix that by adding in a "pass" statement. However, we want to add that in the next line, if possible
                // so context ranges for autocompletion stay intact.
                if ( contents[emptySince] == QChar(':') ) {
                    qCDebug(KDEV_PYTHON_PARSER) << indents.length() << emptySinceLine + 1 << indents;
                    if ( indents.length() > emptySinceLine + 1 && indents.at(emptySinceLine) < indents.at(emptySinceLine + 1) ) {
                        qCDebug(KDEV_PYTHON_PARSER) << indents.at(emptySinceLine) << indents.at(emptySinceLine + 1);
                        contents.insert(emptyLinesSince + 1 + indents.at(emptyLinesSinceLine), "\tpass#");
                    }
                    else {
                        contents.insert(emptySince + 1, "\tpass#");
                    }
                }
                else if ( indents.length() >= currentLine && currentLine > 0 ) {
                    qCDebug(KDEV_PYTHON_PARSER) << indents << currentLine;
                    contents[i+1+indents.at(currentLine - 1)] = QChar('#');
                    contents.insert(i+1+indents.at(currentLine - 1), "pass");
                }
                break;
            }
        }

        syntaxtree = PyParser_ASTFromString(contents.toUtf8(), "<kdev-editor-contents>", file_input, &flags, arena);
        // 3rd try: discard everything after the last non-empty line, but only until the next block start
        currentLineBeginning = qMin(contents.length() - 1, currentLineBeginning);
        errline = qMax(0, qMin(indents.length()-1, errline));
        if ( ! syntaxtree ) {
            qCWarning(KDEV_PYTHON_PARSER) << "Discarding parts of the code to be parsed because of previous errors";
            qCDebug(KDEV_PYTHON_PARSER) << indents;
            int indentAtError = indents.at(errline);
            QChar c;
            bool atLineBeginning = true;
            int currentIndent = -1;
            int currentLineBeginning_end = currentLineBeginning;
            int currentLineContentBeginning = currentLineBeginning;
            for ( int i = currentLineBeginning; i < len; i++ ) {
                c = contents.at(i);
                qCDebug(KDEV_PYTHON_PARSER) << c;
                if ( c == '\n' ) {
                    if ( currentIndent <= indentAtError && currentIndent != -1 ) {
                        qCDebug(KDEV_PYTHON_PARSER) << "Start of error code: " << currentLineBeginning;
                        qCDebug(KDEV_PYTHON_PARSER) << "End of error block (current position): " << currentLineBeginning_end;
                        qCDebug(KDEV_PYTHON_PARSER) << "Length: " << currentLineBeginning_end - currentLineBeginning;
                        qCDebug(KDEV_PYTHON_PARSER) << "indent at error <> current indent:" << indentAtError << "<>" << currentIndent;
//                         contents.remove(currentLineBeginning, currentLineBeginning_end-currentLineBeginning);
                        break;
                    }
                    contents.insert(currentLineContentBeginning - 1, "pass#");
                    i += 5;
                    i = qMin(i, contents.length());
                    len = contents.length();
                    atLineBeginning = true;
                    currentIndent = 0;
                    currentLineBeginning_end = i + 1;
                    currentLineContentBeginning = i + 1;
                    continue;
                }
                if ( ! c.isSpace() && atLineBeginning ) {
                    currentLineContentBeginning = i;
                    atLineBeginning = false;
                }
                if ( c.isSpace() && atLineBeginning ) currentIndent += 1;
            }
            qCDebug(KDEV_PYTHON_PARSER) << "This is what is left: " << contents;
            syntaxtree = PyParser_ASTFromString(contents.toUtf8(), "<kdev-editor-contents>", file_input, &flags, arena);
        }
        if ( ! syntaxtree ) {
            return CodeAst::Ptr(); // everything fails, so we abort.
        }
    }
    qCDebug(KDEV_PYTHON_PARSER) << "Got syntax tree from python parser:" << syntaxtree->kind << Module_kind;

    PythonAstTransformer t(lineOffset);
    t.run(syntaxtree, filename.fileName().replace(".py", ""));
    
    RangeFixVisitor fixVisitor(contents);
    fixVisitor.visitNode(t.ast);
    
    RangeUpdateVisitor updateVisitor;
    updateVisitor.visitNode(t.ast);

    cythonSyntaxRemover.fixAstRanges(t.ast);

    return CodeAst::Ptr(t.ast);
}

}

