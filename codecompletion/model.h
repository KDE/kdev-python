/*****************************************************************************
 * Copyright (c) 2011 Sven Brauch <svenbrauch@googlemail.com>                *
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

#ifndef PYTHONCODECOMPLETIONMODEL_H
#define PYTHONCODECOMPLETIONMODEL_H
#include "pythoncompletionexport.h"

#include <language/codecompletion/codecompletionmodel.h>
#include <language/duchain/duchainpointer.h>
#include <KUrl>


namespace Python {

class KDEVPYTHONCOMPLETION_EXPORT PythonCodeCompletionModel : public KDevelop::CodeCompletionModel
{

public:
    PythonCodeCompletionModel(QObject* parent);
    virtual ~PythonCodeCompletionModel();
    
    virtual KDevelop::CodeCompletionWorker* createCompletionWorker();
    KTextEditor::Range completionRange(KTextEditor::View* view, const KTextEditor::Cursor &position);
    bool shouldStartCompletion(KTextEditor::View* view, const QString& inserted,
                                                     bool userInsertion, const KTextEditor::Cursor& position);
    QString filterString(KTextEditor::View *view, const KTextEditor::Range &range, const KTextEditor::Cursor &position);

    KUrl m_currentDocument;
};

}

#endif // PYTHONCODECOMPLETIONMODEL_H
