/*****************************************************************************
 * Copyright (c) 2007 Andreas Pakulat <apaku@gmx.de>                         *
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 * Copyright (c) 2010-2012 Sven Brauch <svenbrauch@googlemail.com>           *
 *                                                                           *
 * This program is free software; you can redistribute it and/or             *
 * modify it under the terms of the GNU General Public License as            *
 * published by the Free Software Foundation; either version 2 of            *
 * the License, or (at your option) any later version.                       *
 *                                                                           *
 * This program is distributed in the hope that it will be useful,           *
 * but WITHOUT ANY WARRANTY; without even the implied warranty of            *
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             *
 * GNU General Public License for more details.                              *
 *                                                                           *
 * You should have received a copy of the GNU General Public License         *
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.     *
 *****************************************************************************
 */
#ifndef PYTHON_PARSEJOB_H
#define PYTHON_PARSEJOB_H

#include "ast.h"

#include <QStringList>

#include <QExplicitlySharedDataPointer>
#include <ktexteditor/range.h>
#include <astdefaultvisitor.h>

#include <language/backgroundparser/parsejob.h>
#include <language/duchain/duchainpointer.h>
#include <language/duchain/topducontext.h>

using namespace KDevelop;

namespace Python
{

class ParseSession;
class LanguageSupport;

class ParseJob : public KDevelop::ParseJob
{
    Q_OBJECT

public:
    enum {
        Rescheduled = (KDevelop::TopDUContext::LastFeature << 1),
        PEP8Checking = (KDevelop::TopDUContext::LastFeature << 2)
    };
    ParseJob(const IndexedString& url, ILanguageSupport* languageSupport );
    virtual ~ParseJob();

    virtual CodeAst* ast() const;
    bool wasReadFromDisk() const;
    static void eventuallyDoPEP8Checking(const IndexedString document, TopDUContext* topContext);

    virtual ControlFlowGraph* controlFlowGraph();
    virtual DataAccessRepository* dataAccessInformation();

protected:
    virtual void run(ThreadWeaver::JobPointer self, ThreadWeaver::Thread* thread) override;

private:
    QList<QUrl> m_cachedCustomIncludes;
    CodeAst::Ptr m_ast;
    bool m_readFromDisk;
    KDevelop::ReferencedTopDUContext m_duContext;
    KTextEditor::Range m_textRangeToParse;
    QExplicitlySharedDataPointer<ParseSession> m_currentSession;
};

}

#endif
// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
