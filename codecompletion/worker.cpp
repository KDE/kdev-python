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
#include "codehelpers.h"
#include <KTextEditor/View>

#include <QDebug>
#include "codecompletiondebug.h"

namespace Python {

PythonCodeCompletionWorker::PythonCodeCompletionWorker(PythonCodeCompletionModel *parent, const QUrl& /*document*/)
    : KDevelop::CodeCompletionWorker(parent), parent(parent)
{

}



KDevelop::CodeCompletionContext* PythonCodeCompletionWorker::createCompletionContext(KDevelop::DUContextPointer context,
                                                                                     const QString& contextText,
                                                                                     const QString& followingText,
                                                                                     const KDevelop::CursorInRevision& position) const
{
    PythonCodeCompletionContext* completionContext = new PythonCodeCompletionContext(
        context, contextText, followingText, position, 0, this
    );
    return completionContext;
}

void PythonCodeCompletionWorker::updateContextRange(KTextEditor::Range &contextRange, KTextEditor::View *view, KDevelop::DUContextPointer context) const
{
    if ( CodeHelpers::endsInside(view->document()->text(contextRange)) == CodeHelpers::String ) {
        qCDebug(KDEV_PYTHON_CODECOMPLETION) << "we're dealing with string completion. extend the range";
        contextRange = context->rangeInCurrentRevision();
    }
}


}
