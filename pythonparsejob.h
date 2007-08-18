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
#ifndef PARSEJOB_H
#define PARSEJOB_H

#include <parsejob.h>
#include "python_ast.h"

#include <QStringList>

#include <ksharedptr.h>
#include <ktexteditor/range.h>

#include <duchainpointer.h>

class PythonLanguageSupport;

class ParseSession;

using namespace python;

namespace KDevelop {
    class TopDUContext;
}

namespace Python {
    class LexedFile;
}

typedef QList<KDevelop::TopDUContext*> ImportedFileList;

class PythonParseJob : public KDevelop::ParseJob
{
    Q_OBJECT
public:
    PythonParseJob( const KUrl &url, PythonLanguageSupport* parent);
    virtual ~PythonParseJob();

    void setAST(project_ast* ast);
    virtual project_ast *AST() const;

    void setDUChain(KDevelop::TopDUContext* duChain);
    virtual KDevelop::TopDUContext* duChain() const;

    const KTextEditor::Range& textRangeToParse() const;

    void setUpdatingContext( const KDevelop::TopDUContextPointer& context );
    KDevelop::TopDUContextPointer updatingContext() const;

    PythonLanguageSupport* python() const;
    ParseSession* parseSession() const;
    bool wasReadFromDisk() const;
    void setLexedFile( Python::LexedFile* file );
    Python::LexedFile* lexedFile();

protected:
    virtual void run();
private:
    ParseSession *m_session;
    project_ast *m_AST;
    bool m_readFromDisk;
    KDevelop::TopDUContext* m_duContext;
    KUrl m_url;
    KDevelop::TopDUContextPointer m_updatingContext;
    KTextEditor::Range m_textRangeToParse;
};

#endif
