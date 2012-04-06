/*****************************************************************************
 * This file is part of KDevelop
 * Copyright (c) 2011-2012 Sven Brauch <svenbrauch@googlemail.com>           *
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


#ifndef PYCOMPLETIONHELPERS_H
#define PYCOMPLETIONHELPERS_H

#include <language/duchain/declaration.h>

#include <QString>
#include <QList>
#include <QVariant>

#include "pythoncompletionexport.h"

using namespace KDevelop;

namespace Python {

void createArgumentList(Declaration* dec, QString& ret, QList<QVariant>* highlighting, int atArg = 0);

class KDEVPYTHONCOMPLETION_EXPORT ExpressionParser {
public:
    ExpressionParser(QString code);
    
    enum Status {
        InvalidStatus,
        NothingFound,
        ExpressionFound,
        CommaFound,
        CallFound,
        InitializerFound,
        FromFound,
        PrintFound,
        MemberAccessFound,
        ImportFound,
        GeneratorFound,
        RaiseFound
    };
    
    QString popExpression(Status* status);
    QString getRemainingCode();
    QString getScannedCode();
    QString skipUntilStatus(Status requestedStatus, bool* ok, int* expressionsSkipped = 0);
    void reset();
    int trailingWhitespace();
    
private:
    QString m_code;
    int m_cursorPositionInString;
};

}

#endif