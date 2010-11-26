/*****************************************************************************
 * Copyright (c) 2007 Andreas Pakulat <apaku@gmx.de>                         *
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 *                                                                           *
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
 *****************************************************************************/
#ifndef PYTHON_PARSESESSION_H
#define PYTHON_PARSESESSION_H
#include <QtCore/QString>
#include "parserexport.h"

namespace Python
{
    class CodeAst;
    class Ast;

class KDEVPYTHONPARSER_EXPORT ParseSession
{
public:
    ParseSession();
    ~ParseSession();

    void setContents( const QString& contents );
    QString contents() const;

    bool parse( Python::CodeAst** );
private:
    QString m_contents;

};

}

#endif

// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
