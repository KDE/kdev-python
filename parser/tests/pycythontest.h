/*
    This file is part of kdev-python, the python language plugin for KDevelop
    Copyright (C) 2012  Sven Brauch svenbrauch@googlemail.com
    Copyright (C) 2014  Gregor Vollmer <gregor@celement.de>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/


#ifndef PYCYTHONTEST_H
#define PYCYTHONTEST_H

#include <QtCore/QObject>
#include "ast.h"

namespace KDevelop {
    class TopDUContext;
    class ReferencedTopDUContext;
}

namespace Python {

class AstBuilder;

class PyCythonTest : public QObject
{
Q_OBJECT
public:
    explicit PyCythonTest(QObject* parent = 0);
    void initShell();
    CodeAst::Ptr getAst(QString code, KUrl filename);

private:
    QSharedPointer<AstBuilder> m_builder;

private slots:
    void testCythonReplacement();
    void testCythonReplacement_data();
    void testCythonRanges();
    void testCythonRanges_data();
};

}

#endif // PYCYTHONTEST_H
