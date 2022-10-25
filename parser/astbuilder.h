/*
    SPDX-FileCopyrightText: 2007 Andreas Pakulat <apaku@gmx.de>
    SPDX-FileCopyrightText: 2010-2011 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: LGPL-2.0-or-later
*/

#ifndef ASTBUILDER_H
#define ASTBUILDER_H

#include "ast.h"
#include "parserexport.h"

#include <QUrl>
#include "astdefaultvisitor.h"

#include <language/duchain/topducontext.h>

typedef struct _object PyObject;

namespace PythonParser
{
    class Parser;
    class AstNode;
}

namespace Python
{
class Ast;
class CodeAst;

QString PyUnicodeObjectToQString(PyObject* obj);

class KDEVPYTHONPARSER_EXPORT AstBuilder
{
public:
    CodeAst::Ptr parse(const QUrl& filename, QString &contents);
    QList<KDevelop::ProblemPointer> m_problems;
private:
    static QMutex pyInitLock;
};

}

#endif
