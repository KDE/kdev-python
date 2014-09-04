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

#include <malloc.h>

#include <QStringList>
#include <KDebug>
#include <KUrl>
#include <QMutexLocker>
#include <language/duchain/topducontext.h>
#include <language/duchain/problem.h>
#include <language/duchain/duchain.h>

#include "python_header.h"
#include "astdefaultvisitor.h"
#include "cythonsyntaxremover.h"

#include <interfaces/icore.h>
#include <interfaces/iprojectcontroller.h>
#include <interfaces/iproject.h>

using namespace KDevelop;
extern grammar _PyParser_Grammar;

namespace Python
{

// Update the "end" cursors of all nodes in the given tree.
class RangeUpdateVisitor : public AstDefaultVisitor {
public:
    virtual void visitNode(Ast* node) {
        AstDefaultVisitor::visitNode(node);
        if ( node && node->parent ) {
            if ( ( node->parent->endLine <= node->endLine && node->parent->endCol <= node->endCol )
                 || node->parent->endLine < node->endLine )
            {
                node->parent->endLine = node->endLine;
                node->parent->endCol = node->endCol;
            }
        }
    };
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
class RangeFixVisitor : public AstDefaultVisitor {
public:
    RangeFixVisitor(const QString& contents)
        : lines(contents.split('\n')) { }; // TODO can this be \r\n?
    virtual void visitFunctionDefinition(FunctionDefinitionAst* node) {
        cutDefinitionPreamble(node->name, "def");
        AstDefaultVisitor::visitFunctionDefinition(node);
    };
    virtual void visitClassDefinition(ClassDefinitionAst* node) {
        cutDefinitionPreamble(node->name, "class");
        AstDefaultVisitor::visitClassDefinition(node);
    };
    // alias for imports (import foo as bar, baz as bang)
    // no strings, brackets, or whatever are allowed here, so the "parser"
    // can be very straightforward.
    virtual void visitImport(ImportAst* node) {
        AstDefaultVisitor::visitImport(node);
        int aliasIndex = 0;
        foreach ( AliasAst* alias, node->names ) {
            fixAlias(alias->name, alias->asName, node->startLine, aliasIndex);
            aliasIndex += 1;
        }
    };
    // alias for exceptions (except FooBarException as somethingterriblehappened: ...)
    virtual void visitExceptionHandler(ExceptionHandlerAst* node) {
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
            if ( ! lines.at(currentLine).trimmed().startsWith('@') ) {
                // it's not a decorator, so stop skipping lines.
                break;
            }
            currentLine += 1;
        }
        fixNode->startLine = currentLine;
        fixNode->endLine = currentLine;

        // cut away the "def" / "class"
        int currentColumn = -1;
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
            if ( lineData.midRef(currentColumn, defKeyword.size()) == defKeyword ) {
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
#ifdef Q_OS_WIN32
    // If you want to make this work on windows, take care to check Py_UNICODE_WIDE (see below)
    // not sure if this always works
    // not sure either why the "linux" version below wouldn't work on windows
    return QString::fromWCharArray((wchar_t*)PyUnicode_AS_DATA(PyObject_Str(obj)));
#else
    uint* data = (uint*) PyUnicode_AS_DATA(PyObject_Str(obj));
#ifdef Py_UNICODE_WIDE
    return QString::fromUcs4(data);
#else
    return QString::fromUcs2(data);
#endif // Py_UNICODE_WIDE
#endif // windows
}

QPair<QString, int> fileHeaderHack(QString& contents, const KUrl& filename)
{
    IProject* proj = ICore::self()->projectController()->findProjectForUrl(filename);
    // the file is not in a project, don't apply hack
    if ( ! proj ) {
        return QPair<QString, int>(contents, 0);
    }
    const KUrl headerFileUrl = proj->folder().path(KUrl::AddTrailingSlash) + ".kdev_python_header";
    QFile headerFile(headerFileUrl.path());
    QString headerFileContents;
    if ( headerFile.exists() ) {
        headerFile.open(QIODevice::ReadOnly);
        headerFileContents = headerFile.readAll();
        headerFile.close();
        kDebug() << "Found header file, applying hack";
        int insertAt = 0;
        bool endOfCommentsReached = false;
        bool commentSignEncountered = false;
//         bool atLineBeginning = true;
        int lastLineBeginning = 0;
        int newlineCount = 0;
        int l = contents.length();
        do {
            if ( insertAt >= l ) {
                kDebug() << "File consist only of comments, not applying hack";
                return QPair<QString, int>(contents, 0);
            }
            if ( contents.at(insertAt) == '#' ) {
                commentSignEncountered = true;
            }
            if ( not contents.at(insertAt).isSpace() ) {
//                 atLineBeginning = false;
                if ( not commentSignEncountered ) {
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
        } while ( not endOfCommentsReached );
        kDebug() << "Inserting contents at char" << lastLineBeginning << "of file";
        contents = contents.left(lastLineBeginning) 
                   + "\n" + headerFileContents + "\n#\n" 
                   + contents.right(contents.length() - lastLineBeginning);
        kDebug() << contents;
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

CodeAst::Ptr AstBuilder::parse(KUrl filename, QString &contents)
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
        kDebug() << filename.fileName() << "is probably Cython file.";
        contents = cythonSyntaxRemover.stripCythonSyntax(contents);
    }

    mod_ty syntaxtree = PyParser_ASTFromString(contents.toUtf8().data(), "<kdev-editor-contents>", file_input, &flags, arena);

    if ( ! syntaxtree ) {
        qDebug() << " ====< parse error, trying to fix";
        
        PyErr_Fetch(&exception, &value, &backtrace);
        kDebug() << "Error objects: " << exception << value << backtrace;
        PyObject_Print(value, stderr, Py_PRINT_RAW);
        
        PyObject* errorMessage_str = PyTuple_GetItem(value, 0);
        PyObject* errorDetails_tuple = PyTuple_GetItem(value, 1);
        qDebug() << "Eventual errors while extracting tuple: ";
        PyObject_Print(errorMessage_str, stderr, Py_PRINT_RAW);
       
        if ( ! errorDetails_tuple ) {
            kWarning() << "Error retrieving error message, not displaying, and not doing anything";
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
        kDebug() << "Problem range: " << range;
        DocumentRange location(IndexedString(filename.path()), range);
        p->setFinalLocation(location);
        p->setDescription(PyUnicodeObjectToQString(errorMessage_str));
        p->setSource(ProblemData::Parser);
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
                    kDebug() << indents.length() << emptySinceLine + 1 << indents;
                    if ( indents.length() > emptySinceLine + 1 && indents.at(emptySinceLine) < indents.at(emptySinceLine + 1) ) {
                        kDebug() << indents.at(emptySinceLine) << indents.at(emptySinceLine + 1);
                        contents.insert(emptyLinesSince + 1 + indents.at(emptyLinesSinceLine), "\tpass#");
                    }
                    else {
                        contents.insert(emptySince + 1, "\tpass#");
                    }
                }
                else if ( indents.length() >= currentLine && currentLine > 0 ) {
                    kDebug() << indents << currentLine;
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
            kWarning() << "Discarding parts of the code to be parsed because of previous errors";
            kDebug() << indents;
            int indentAtError = indents.at(errline);
            QChar c;
            bool atLineBeginning = true;
            int currentIndent = -1;
            int currentLineBeginning_end = currentLineBeginning;
            int currentLineContentBeginning = currentLineBeginning;
            for ( int i = currentLineBeginning; i < len; i++ ) {
                c = contents.at(i);
                kDebug() << c;
                if ( c == '\n' ) {
                    if ( currentIndent <= indentAtError && currentIndent != -1 ) {
                        kDebug() << "Start of error code: " << currentLineBeginning;
                        kDebug() << "End of error block (current position): " << currentLineBeginning_end;
                        kDebug() << "Length: " << currentLineBeginning_end - currentLineBeginning;
                        kDebug() << "indent at error <> current indent:" << indentAtError << "<>" << currentIndent;
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
            kDebug() << "This is what is left: " << contents;
            syntaxtree = PyParser_ASTFromString(contents.toUtf8(), "<kdev-editor-contents>", file_input, &flags, arena);
        }
        if ( ! syntaxtree ) {
            return CodeAst::Ptr(); // everything fails, so we abort.
        }
    }
    kDebug() << "Got syntax tree from python parser:" << syntaxtree->kind << Module_kind;

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

