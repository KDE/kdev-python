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
#include <KDebug>
#include <KStandardDirs>
#include <KUrl>
#include <KLocale>
#include <QDir>
#include <QTimer>
#include <language/duchain/topducontext.h>
#include <language/interfaces/iproblem.h>
#include <language/duchain/duchain.h>

#include "python_header.h"

#include <interfaces/icore.h>
#include <interfaces/iprojectcontroller.h>
#include <interfaces/iproject.h>

using namespace KDevelop;
extern grammar _PyParser_Grammar;

namespace Python
{

#include "generated.h"

QMutex AstBuilder::pyInitLock;
QString AstBuilder::pyHomeDir = KStandardDirs::locate("data", "");

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

AstBuilder::AstBuilder(KDevPG::MemoryPool* pool)
    : m_pool(pool)
{

}

CodeAst* AstBuilder::parse(KUrl filename, QString& contents)
{
    qDebug() << " ====> AST     ====>     building abstract syntax tree for " << filename.path();
    
    Py_NoSiteFlag = 1;
    
    QPair<QString, int> hacked = fileHeaderHack(contents, filename);
    contents = hacked.first;
    int lineOffset = hacked.second;
    
    AstBuilder::pyInitLock.lock();
    Py_SetPythonHome(AstBuilder::pyHomeDir.toAscii().data());
    kDebug() << "Not initialized, calling init func.";
    Py_Initialize();
    QTimer timer;
    timer.start(1000);
    while ( ! Py_IsInitialized() && timer.isActive() ) {
        kWarning() << "Python doesn't say it is initialized yet, waiting -- should not happen!";
        usleep(100000);
    }
    Q_ASSERT(Py_IsInitialized());
    
    PyArena* arena = PyArena_New();
    Q_ASSERT(arena); // out of memory
    PyCompilerFlags* flags = new PyCompilerFlags();
    flags->cf_flags = 0;
    
    PyObject *exception, *value, *backtrace;
    PyErr_Fetch(&exception, &value, &backtrace);
//     kDebug() << "Errors before starting parser:";
//     PyObject_Print(value, stderr, Py_PRINT_RAW);
//     kDebug();
    mod_ty syntaxtree = PyParser_ASTFromString(contents.toAscii(), "<kdev-editor-contents>", file_input, flags, arena);

    if ( ! syntaxtree ) {
        kWarning() << "DID NOT RECEIVE A SYNTAX TREE -- probably parse error.";
        
        PyErr_Fetch(&exception, &value, &backtrace);
        kDebug() << "Error objects: " << exception << value << backtrace;
        PyObject_Print(value, stderr, Py_PRINT_RAW);
        
        PyObject* errorMessage_str = PyTuple_GetItem(value, 0);
        PyObject* errorDetails_tuple = PyTuple_GetItem(value, 1);
        qDebug() << "Eventual errors while extracting tuple: ";
        PyObject_Print(errorMessage_str, stderr, Py_PRINT_RAW);
       
        if ( ! errorDetails_tuple ) {
            kWarning() << "Error retrieving error message, not displaying, and not doing anything";
            pyInitLock.unlock();
            return 0;
        }
        PyObject* linenoobj = PyTuple_GetItem(errorDetails_tuple, 1);
        errorMessage_str = PyTuple_GetItem(value, 0);
        errorDetails_tuple = PyTuple_GetItem(value, 1);
        PyObject_Print(errorMessage_str, stderr, Py_PRINT_RAW);
        
        PyObject* colnoobj = PyTuple_GetItem(errorDetails_tuple, 2);
        int lineno = PyInt_AsLong(linenoobj) - 1;
        int colno = PyInt_AsLong(colnoobj);
        
        ProblemPointer p(new Problem());
        SimpleCursor start(lineno + lineOffset, (colno-4 > 0 ? colno-4 : 0));
        SimpleCursor end(lineno + lineOffset, (colno+4 > 4 ? colno+4 : 4));
        SimpleRange range(start, end);
        kDebug() << "Problem range: " << range;
        DocumentRange location(IndexedString(filename.path()), range);
        p->setFinalLocation(location);
        p->setDescription(PyString_AsString(PyObject_Str(errorMessage_str)));
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
        
        syntaxtree = PyParser_ASTFromString(contents.toAscii(), "<kdev-editor-contents>", file_input, flags, arena);
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
            syntaxtree = PyParser_ASTFromString(contents.toAscii(), "<kdev-editor-contents>", file_input, flags, arena);
        }
        if ( ! syntaxtree ) {
            PyArena_Free(arena);
            Py_Finalize();
            pyInitLock.unlock();
            return 0; // everything fails, so we abort.
        }
    }
    kDebug() << "Got syntax tree from python parser:" << syntaxtree->kind << Module_kind;

    PythonAstTransformer t(lineOffset, m_pool);
    t.run(syntaxtree, filename.fileName().replace(".py", ""));
    
    PyArena_Free(arena);
    Py_Finalize();
    
    AstBuilder::pyInitLock.unlock();

    return t.ast;
}

}

