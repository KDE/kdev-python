/*****************************************************************************
 *   Copyright 2011-2012 Sven Brauch <svenbrauch@googlemail.com>             *
 *                                                                           *
 *   This program is free software: you can redistribute it and/or modify    *
 *   it under the terms of the GNU General Public License as published by    *
 *   the Free Software Foundation, either version 3 of the License, or       *
 *   (at your option) any later version.                                     *
 *                                                                           *
 *   This program is distributed in the hope that it will be useful,         *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of          *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           *
 *   GNU General Public License for more details.                            *
 *                                                                           *
 *   You should have received a copy of the GNU General Public License       *
 *   along with this program.  If not, see <http://www.gnu.org/licenses/>    *
 *****************************************************************************/

#ifndef PYCOMPLETIONTEST_H
#define PYCOMPLETIONTEST_H

#include <QtCore/QObject>
#include <language/editor/cursorinrevision.h>
#include <language/codecompletion/codecompletioncontext.h>

using namespace KDevelop;

namespace Python {

class PyCompletionTest : public QObject
{
    Q_OBJECT
    public:
        explicit PyCompletionTest(QObject* parent = 0);
        void initShell();
        
        QList<CompletionTreeItemPointer> invokeCompletionOn(const QString& code,
                                                            CursorInRevision cursorAt = CursorInRevision::invalid());
        bool containsItemForDeclarationNamed(QList<CompletionTreeItemPointer> items, QString itemName);
        
    private slots:
        void testIntegralTypesImmediate();
    
};

}
#endif