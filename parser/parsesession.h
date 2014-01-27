/*****************************************************************************
 * Copyright (c) 2007 Andreas Pakulat <apaku@gmx.de>                         *
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
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
#ifndef PYTHON_PARSESESSION_H
#define PYTHON_PARSESESSION_H
#include <QtCore/QString>
#include "parserexport.h"
#include <language/duchain/indexedstring.h>
#include <language/duchain/duchainpointer.h>
#include <language/duchain/problem.h>
#include <language/editor/simplecursor.h>
#include <language/editor/documentrange.h>
#include "ast.h"
#include "kurl.h"
#include <kdev-pg-memory-pool.h>
#include "astdefaultvisitor.h"

#include <language/interfaces/iastcontainer.h>
#include <language/editor/rangeinrevision.h>
#include <language/editor/modificationrevision.h>

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
    ~ParseSession();

    void setContents( const QString& contents );
    QString contents() const;
    
    KDevPG::MemoryPool* m_pool;
    
    void setCurrentDocument(const IndexedString& url);
    IndexedString currentDocument();

    QPair<CodeAst::Ptr, bool> parse();
    
    QList<KDevelop::ProblemPointer> m_problems;
    
    const ModificationRevision& futureModificationRevision() const;
    void setFutureModificationRevision(const ModificationRevision& revision);
    
    void mapAstUse(Ast* node, const SimpleUse& use)
    {
        Q_UNUSED(node);
        Q_UNUSED(use);
    }
    
    CodeAst::Ptr ast;
    
private:
    QString m_contents;
    KDevelop::IndexedString m_currentDocument;
    ModificationRevision m_futureModificationRevision;

};

}

#endif

// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
