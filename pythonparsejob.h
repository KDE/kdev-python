/*****************************************************************************
 * Copyright (c) 2007 Andreas Pakulat <apaku@gmx.de>                         *
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 *                                                                           *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
 * 02110-1301, USA.
 *****************************************************************************/
#ifndef PYTHON_PARSEJOB_H
#define PYTHON_PARSEJOB_H

#include <language/backgroundparser/parsejob.h>
#include "ast.h"

#include <QStringList>

#include <ksharedptr.h>
#include <ktexteditor/range.h>

#include <language/duchain/duchainpointer.h>


namespace KDevelop
{

class TopDUContext;
}

namespace Python
{

class LanguageSupport;

class ParseSession;

class ParseJob : public KDevelop::ParseJob
{
    Q_OBJECT

public:
    ParseJob( const KUrl &url, LanguageSupport* parent );
    virtual ~ParseJob();

    void setAST( CodeAst* ast );
    virtual CodeAst *ast() const;

    const KTextEditor::Range& textRangeToParse() const;

    LanguageSupport* python() const;
    ParseSession* parseSession() const;
    bool wasReadFromDisk() const;

protected:
    virtual void run();

private:
    ParseSession *m_session;
    CodeAst *m_ast;
    bool m_readFromDisk;
    KDevelop::TopDUContext* m_duContext;
    KUrl m_url;
    KTextEditor::Range m_textRangeToParse;
};

}

#endif
// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
