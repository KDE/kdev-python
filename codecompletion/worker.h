/*****************************************************************************
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

#ifndef PYTHONCODECOMPLETIONWORKER_H
#define PYTHONCODECOMPLETIONWORKER_H

#include "model.h"
#include <language/codecompletion/codecompletionworker.h>
#include <language/codecompletion/codecompletionitem.h>
#include "pythoncompletionexport.h"

namespace Python {

class KDEVPYTHONCOMPLETION_EXPORT PythonCodeCompletionWorker : public KDevelop::CodeCompletionWorker
{

public:
    PythonCodeCompletionWorker(PythonCodeCompletionModel *parent, const QUrl& document);
    virtual KDevelop::CodeCompletionContext* createCompletionContext(KDevelop::DUContextPointer context, const QString& contextText, const QString& followingText, const KDevelop::CursorInRevision& position) const;
    virtual void updateContextRange(KTextEditor::Range &contextRange, KTextEditor::View *view, KDevelop::DUContextPointer context) const;
    PythonCodeCompletionModel* parent;
};

}

#endif // PYTHONCODECOMPLETIONWORKER_H
