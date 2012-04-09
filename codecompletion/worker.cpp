/*****************************************************************************
 * Copyright (c) 2010-2011 Sven Brauch <svenbrauch@googlemail.com>           *
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

#include "worker.h"
#include "model.h"
#include "context.h"
#include <language/duchain/declaration.h>
#include <KLocalizedString>


namespace Python {

PythonCodeCompletionWorker::PythonCodeCompletionWorker(PythonCodeCompletionModel *parent, KUrl /*document*/)
    : KDevelop::CodeCompletionWorker(parent), parent(parent)
{

}

KDevelop::CodeCompletionContext* PythonCodeCompletionWorker::createCompletionContext(KDevelop::DUContextPointer context, const QString& contextText, const QString& /*followingText*/, const KDevelop::CursorInRevision& position) const
{
    PythonCodeCompletionContext* completionContext = new PythonCodeCompletionContext(context, contextText, position, 0, this);
    return completionContext;
}


}