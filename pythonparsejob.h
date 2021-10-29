/*
    SPDX-FileCopyrightText: 2007 Andreas Pakulat <apaku@gmx.de>
    SPDX-FileCopyrightText: 2007 Piyush verma <piyush.verma@gmail.com>
    SPDX-FileCopyrightText: 2010-2012 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
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
    ~ParseJob() override;

    virtual CodeAst* ast() const;
    bool wasReadFromDisk() const;
    void eventuallyDoPEP8Checking(TopDUContext* topContext);

    ControlFlowGraph* controlFlowGraph() override;
    DataAccessRepository* dataAccessInformation() override;

protected:
    void run(ThreadWeaver::JobPointer self, ThreadWeaver::Thread* thread) override;

private:
    QVector<QUrl> m_cachedCustomIncludes;
    CodeAst::Ptr m_ast;
    bool m_readFromDisk;
    KDevelop::ReferencedTopDUContext m_duContext;
    KTextEditor::Range m_textRangeToParse;
    QExplicitlySharedDataPointer<ParseSession> m_currentSession;
};

}

#endif
// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
