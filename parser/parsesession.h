/*
    SPDX-FileCopyrightText: 2007 Andreas Pakulat <apaku@gmx.de>
    SPDX-FileCopyrightText: 2007 Piyush verma <piyush.verma@gmail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef PYTHON_PARSESESSION_H
#define PYTHON_PARSESESSION_H

#include <QString>

#include "parserexport.h"
#include <language/duchain/duchainpointer.h>
#include <language/duchain/problem.h>
#include <language/editor/documentrange.h>

#include <language/interfaces/iastcontainer.h>
#include <language/editor/rangeinrevision.h>
#include <language/editor/modificationrevision.h>

#include "ast.h"
#include "astdefaultvisitor.h"

using namespace KDevelop;

typedef QPair<KDevelop::DUContextPointer, KDevelop::RangeInRevision> SimpleUse;

namespace Python
{
class CodeAst;
class Ast;

class KDEVPYTHONPARSER_EXPORT ParseSession : public IAstContainer
{
public:
    ParseSession();
    ~ParseSession() override;

    void setContents( const QString& contents );
    QString contents() const;
    
    void setCurrentDocument(const IndexedString& url);
    IndexedString currentDocument();

    QPair<CodeAst::Ptr, bool> parse();
    
    QList<KDevelop::ProblemPointer> m_problems;
    
    const ModificationRevision& futureModificationRevision() const;
    void setFutureModificationRevision(const ModificationRevision& revision);
    
    CodeAst::Ptr ast;
    
private:
    QString m_contents;
    KDevelop::IndexedString m_currentDocument;
    ModificationRevision m_futureModificationRevision;

};

}

#endif

// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
