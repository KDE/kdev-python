/*****************************************************************************
 * Copyright (c) 2007 Andreas Pakulat <apaku@gmx.de>                         *
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 * Copyright (c) 2010-2012 Sven Brauch <svenbrauch@googlemail.com>           *
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
#ifndef PYTHON_PARSEJOB_H
#define PYTHON_PARSEJOB_H

#include "ast.h"

#include <QStringList>

#include <ksharedptr.h>
#include <ktexteditor/range.h>
#include <kdev-pg-memory-pool.h>

#include <language/backgroundparser/parsejob.h>
#include <language/duchain/duchainpointer.h>
#include <language/duchain/topducontext.h>



using namespace KDevelop;

namespace Python
{

class LanguageSupport;

class ParseSession;

class ParseJob : public KDevelop::ParseJob
{
    Q_OBJECT

public:
    enum {
        Rescheduled = KDevelop::TopDUContext::LastFeature
    };
    ParseJob(const IndexedString& url, ILanguageSupport* languageSupport );
    virtual ~ParseJob();

    void setAST( CodeAst* ast );
    virtual CodeAst *ast() const;

    const KTextEditor::Range& textRangeToParse() const;

protected:
    virtual void run();

private:
    CodeAst *m_ast;
    bool m_readFromDisk;
    KDevelop::ReferencedTopDUContext m_duContext;
    KTextEditor::Range m_textRangeToParse;
};

}

#endif
// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
