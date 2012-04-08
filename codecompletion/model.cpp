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

#include "model.h"

#include <KTextEditor/View>
#include <KTextEditor/Document>

#include "worker.h"

namespace Python {

PythonCodeCompletionModel::PythonCodeCompletionModel(QObject* parent)
    : CodeCompletionModel(parent)
{
    // This avoids flickering of the completion-list when full code-completion mode is used
    setForceWaitForModel(true);
}

PythonCodeCompletionModel::~PythonCodeCompletionModel() { }

bool PythonCodeCompletionModel::shouldStartCompletion(KTextEditor::View* view, const QString& inserted,
                                                bool userInsertion, const KTextEditor::Cursor& position)
{
    QList<QString> words;
    words << "for" << "raise" << "except";
    foreach ( const QString& word, words ) {
        if ( view->document()->line(position.line()).mid(0, position.column()).endsWith(word + " ") ) {
            return true;
        }
    }
    // shebang / encoding lines
    if ( view->document()->line(position.line()).mid(0, position.column()).endsWith("#") && 
         position.line() < 2 )
    {
        return true;
    }
    return KDevelop::CodeCompletionModel::shouldStartCompletion(view, inserted, userInsertion, position);
}

KTextEditor::Range PythonCodeCompletionModel::completionRange(KTextEditor::View* view, const KTextEditor::Cursor& position)
{
    m_currentDocument = view->document()->url();
    kWarning() << "Current document: " << m_currentDocument;
    return KTextEditor::CodeCompletionModelControllerInterface3::completionRange(view, position);
}

KDevelop::CodeCompletionWorker* PythonCodeCompletionModel::createCompletionWorker()
{
    return new PythonCodeCompletionWorker(this, m_currentDocument);
}

}