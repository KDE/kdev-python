/*
    SPDX-FileCopyrightText: 2007 Andreas Pakulat <apaku@gmx.de>
    SPDX-FileCopyrightText: 2010-2011 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: LGPL-2.0-or-later
*/

#include "astbuilder.h"
#include "ast.h"

#include <language/duchain/problem.h>
#include <language/duchain/duchain.h>
#include <language/editor/documentrange.h>

#include <memory>

#include "python_header.h"
#include "asttransformer.h"
#include "astdefaultvisitor.h"
#include "rangefixvisitor.h"

#include <QDebug>
#include <QMutexLocker>

#include "parserdebug.h"

using namespace KDevelop;

namespace Python
{

QMutex AstBuilder::pyInitLock;

QString PyUnicodeObjectToQString(PyObject* obj) {
    auto pyObjectCleanup = [](PyObject* o) { if (o) Py_DECREF(o); };
    const auto strOwner = std::unique_ptr<PyObject, decltype(pyObjectCleanup)>(PyObject_Str(obj), pyObjectCleanup);
    const auto str = strOwner.get();

    Py_ssize_t size;
    const char *ptr = PyUnicode_AsUTF8AndSize(str, &size);
    if (!ptr) {
        qCWarning(KDEV_PYTHON_PARSER) << "failed to convert python string to unicode";
        return {};
    }

    return QString::fromUtf8(ptr, size);
}

struct PythonParser : private QMutexLocker<QMutex>
{
    PyObject* m_parser_mod = nullptr;
    PyObject* m_parse_func = nullptr;

    PythonParser(QMutex& lock): QMutexLocker(&lock)
    {
#if PYTHON_VERSION < QT_VERSION_CHECK(3, 12, 0)
        Py_InitializeEx(0);
#else
        PyConfig config;
        PyConfig_InitPythonConfig(&config);
        config.site_import = 0;
        config.install_signal_handlers = 0;
        Py_InitializeFromConfig(&config);
#endif

        Q_ASSERT(Py_IsInitialized());
        m_parser_mod = PyImport_ImportModule("ast");
        Q_ASSERT(m_parser_mod); // parser import error
        m_parse_func = PyObject_GetAttrString(m_parser_mod, "parse");
        Q_ASSERT(m_parse_func); // parser function renamed?
    }

    // Call parser function and return the python ast.Module.
    // NOTE: The caller must DECREF the result
    PyObject* parse(QString const &source, QString const &filename) const
    {
        PyObject* args = PyTuple_New(3);
        PyTuple_SET_ITEM(args, 0, PyUnicode_FromString(source.toUtf8().data()));
        PyTuple_SET_ITEM(args, 1, PyUnicode_FromString(filename.toUtf8().data()));
        PyTuple_SET_ITEM(args, 2, PyUnicode_FromString("exec"));
        PyObject *result = PyObject_CallObject(m_parse_func, args);
        Py_DECREF(args);
        return result;
    }

    ~PythonParser()
    {
        if (Py_IsInitialized())
        {
            Py_XDECREF(m_parse_func);
            Py_XDECREF(m_parser_mod);
            Py_Finalize();
        }
    }
};

CodeAst::Ptr AstBuilder::parse(const QUrl& filename, QString &contents)
{
    qCDebug(KDEV_PYTHON_PARSER) << " ====> AST     ====>     building abstract syntax tree for " << filename.path();

#if PYTHON_VERSION < QT_VERSION_CHECK(3, 12, 0)
    Py_NoSiteFlag = 1;
#endif

    contents.append(QLatin1Char('\n'));
    
    PythonParser py_parser(pyInitLock);

    PyObject* syntaxtree = py_parser.parse(contents, filename.fileName());

    if ( ! syntaxtree ) {
        qCDebug(KDEV_PYTHON_PARSER) << " ====< parse error, trying to fix";

        PyObject *exception, *value, *backtrace;
        PyErr_Fetch(&exception, &value, &backtrace);
        qCDebug(KDEV_PYTHON_PARSER) << "Error objects: " << exception << value << backtrace;

        if ( ! value ) {
            qCWarning(KDEV_PYTHON_PARSER) << "Internal parser error: exception value is null, aborting";
            return CodeAst::Ptr();
        }
        PyErr_NormalizeException(&exception, &value, &backtrace);

        if ( ! PyObject_IsInstance(value, PyExc_SyntaxError) ) {
            qCWarning(KDEV_PYTHON_PARSER) << "Exception was not a SyntaxError, aborting";
            return CodeAst::Ptr();
        }
        PyObject* errorMessage_str = PyObject_GetAttrString(value, "msg");
        PyObject* linenoobj = PyObject_GetAttrString(value, "lineno");
        PyObject* colnoobj = PyObject_GetAttrString(value, "offset");

        int lineno = PyLong_AsLong(linenoobj) - 1;
        int colno = PyLong_AsLong(colnoobj);

        ProblemPointer p(new Problem());
        KTextEditor::Cursor start(lineno, (colno-4 > 0 ? colno-4 : 0));
        KTextEditor::Cursor end(lineno, (colno+4 > 4 ? colno+4 : 4));
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
        QChar c;
        QChar newline(QLatin1Char('\n'));
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
                if ( contents[emptySince] == QLatin1Char(':') ) {
                    qCDebug(KDEV_PYTHON_PARSER) << indents.length() << emptySinceLine + 1 << indents;
                    if ( indents.length() > emptySinceLine + 1 && indents.at(emptySinceLine) < indents.at(emptySinceLine + 1) ) {
                        qCDebug(KDEV_PYTHON_PARSER) << indents.at(emptySinceLine) << indents.at(emptySinceLine + 1);
                        contents.insert(emptyLinesSince + 1 + indents.at(emptyLinesSinceLine), QStringLiteral("\tpass#"));
                    }
                    else {
                        contents.insert(emptySince + 1, QStringLiteral("\tpass#"));
                    }
                }
                else if ( indents.length() >= currentLine && currentLine > 0 ) {
                    qCDebug(KDEV_PYTHON_PARSER) << indents << currentLine;
                    contents[i+1+indents.at(currentLine - 1)] = QLatin1Char('#');
                    contents.insert(i+1+indents.at(currentLine - 1), QStringLiteral("pass"));
                }
                break;
            }
        }

        syntaxtree = py_parser.parse(contents, filename.fileName());
        // 3rd try: discard everything after the last non-empty line, but only until the next block start
        currentLineBeginning = qMin(contents.length() - 1, currentLineBeginning);
        errline = qMax(0, qMin(indents.length()-1, errline));
        if ( ! syntaxtree ) {
            PyErr_Fetch(&exception, &value, &backtrace);
            qCDebug(KDEV_PYTHON_PARSER) << "Error objects: " << exception << value << backtrace;

            qCWarning(KDEV_PYTHON_PARSER) << "Discarding parts of the code to be parsed because of previous errors";
            qCDebug(KDEV_PYTHON_PARSER) << indents;
            int indentAtError = errline < indents.length() ? indents.at(errline): 0;
            QChar c;
            bool atLineBeginning = true;
            int currentIndent = -1;
            int currentLineBeginning_end = currentLineBeginning;
            int currentLineContentBeginning = currentLineBeginning;
            for ( int i = currentLineBeginning; i < len; i++ ) {
                c = contents.at(i);
                qCDebug(KDEV_PYTHON_PARSER) << c;
                if ( c == QLatin1Char('\n') ) {
                    if ( currentIndent <= indentAtError && currentIndent != -1 ) {
                        qCDebug(KDEV_PYTHON_PARSER) << "Start of error code: " << currentLineBeginning;
                        qCDebug(KDEV_PYTHON_PARSER) << "End of error block (current position): " << currentLineBeginning_end;
                        qCDebug(KDEV_PYTHON_PARSER) << "Length: " << currentLineBeginning_end - currentLineBeginning;
                        qCDebug(KDEV_PYTHON_PARSER) << "indent at error <> current indent:" << indentAtError << "<>" << currentIndent;
//                         contents.remove(currentLineBeginning, currentLineBeginning_end-currentLineBeginning);
                        break;
                    }
                    contents.insert(currentLineContentBeginning - 1, QStringLiteral("pass#"));
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
            syntaxtree = py_parser.parse(contents, filename.fileName());
        }
        if ( ! syntaxtree ) {
            return CodeAst::Ptr(); // everything fails, so we abort.
        }
    }
    QString kind = PyUnicodeObjectToQString(PyObject_Repr(syntaxtree));
    qCDebug(KDEV_PYTHON_PARSER) << "Got syntax tree from python parser:" << kind;

    AstTransformer t;
    t.run(syntaxtree, filename.fileName().replace(QStringLiteral(".py"), QString()));
    Py_DECREF(syntaxtree);

    RangeFixVisitor fixVisitor(contents);
    fixVisitor.visitNode(t.ast);

    return CodeAst::Ptr(t.ast);
}

}

