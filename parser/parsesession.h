/*****************************************************************************
 * Copyright (c) 2007 Andreas Pakulat <apaku@gmx.de>                         *
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 *                                                                           *
 * Permission is hereby granted, free of charge, to any person obtaining     *
 * a copy of this software and associated documentation files (the           *
 * "Software"), to deal in the Software without restriction, including       *
 * without limitation the rights to use, copy, modify, merge, publish,       *
 * distribute, sublicense, and/or sell copies of the Software, and to        *
 * permit persons to whom the Software is furnished to do so, subject to     *
 * the following conditions:                                                 *
 *                                                                           *
 * The above copyright notice and this permission notice shall be            *
 * included in all copies or substantial portions of the Software.           *
 *                                                                           *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,           *
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF        *
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND                     *
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE    *
 * LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION    *
 * OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION     *
 * WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.           *
 *****************************************************************************/
#ifndef PYTHON_PARSESESSION_H
#define PYTHON_PARSESESSION_H
#include <QtCore/QString>
#include "parserexport.h"
#include <language/duchain/indexedstring.h>
#include <language/duchain/duchainpointer.h>
#include <language/editor/simplecursor.h>
#include <language/editor/documentrange.h>
#include "ast.h"
#include "kurl.h"

#include <language/interfaces/iproblem.h>
#include <language/editor/rangeinrevision.h>

using namespace KDevelop;

typedef QPair<KDevelop::DUContextPointer, KDevelop::RangeInRevision> SimpleUse;

namespace Python
{
    class CodeAst;
    class Ast;

class KDEVPYTHONPARSER_EXPORT ParseSession
{
public:
    ParseSession();
    ~ParseSession();

    void setContents( const QString& contents );
    QString contents() const;
    
    void setCurrentDocument(KUrl& filename);
    IndexedString currentDocument();

    QPair<CodeAst*, bool> parse( Python::CodeAst* ast );
    
    QList<KDevelop::ProblemPointer> m_problems;
    
    void mapAstUse(Ast* node, const SimpleUse& use)
    {
        Q_UNUSED(node);
        Q_UNUSED(use);
    }
    
private:
    QString m_contents;
    KDevelop::IndexedString m_currentDocument;

};

}

#endif

// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
