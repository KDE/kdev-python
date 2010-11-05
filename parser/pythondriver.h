/* Python Parser Test
 *
 * Copyright 2007 Andreas Pakulat <apaku@gmx.de>
 *
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
 */

#ifndef PYTHONDRIVER_H
#define PYTHONDRIVER_H

#include <QtCore/QString>
#include "parserexport.h"
#include <kurl.h>

#include <language/interfaces/iproblem.h>


namespace KDevPG
{
class MemoryPool;
class TokenStream;
}
namespace Python
{
class CodeAst;
}

namespace Python
{
/**
 * Class to parse a Python source file or a string containing python source code
 */
class KDEVPYTHONPARSER_EXPORT Driver
{
public:
    Driver();
    bool readFile( const QString&, const char* = 0 );
    void setContent( const QString& );
    void setDebug( bool );
    QPair<CodeAst*, bool> parse( Python::CodeAst* ast );
    void setTokenStream( KDevPG::TokenStream* );
    void setMemoryPool( KDevPG::MemoryPool* );
    void setCurrentDocument(KUrl url);
    
    QList<KDevelop::ProblemPointer> m_problems;
    
private:
    QString m_content;
    bool m_debug;
    KDevPG::MemoryPool* m_pool;
    KDevPG::TokenStream* m_tokenstream;
    KUrl m_currentDocument;
};

}

#endif

// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
