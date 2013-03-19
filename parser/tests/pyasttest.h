/*
    This file is part of kdev-python, the python language plugin for KDevelop
    Copyright (C) 2012  Sven Brauch svenbrauch@googlemail.com

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


#ifndef PYASTTEST_H
#define PYASTTEST_H

#include <QtCore/QObject>
#include <kdev-pg-memory-pool.h>
#include <ast.h>

namespace KDevelop {
    class TopDUContext;
    class ReferencedTopDUContext;
}

namespace Python {

class PyAstTest : public QObject
{
Q_OBJECT
public:
    explicit PyAstTest(QObject* parent = 0);
    void initShell();
    CodeAst* getAst(QString code);
    void testCode(QString code);
private slots:
    void testClass();
    void testStatements();
    void testStatements_data();
    void testExpressions();
    void testExpressions_data();
    void testSlices();
    void testSlices_data();
    void testOther();
    void testOther_data();
    void testNewPython3();
    void testNewPython3_data();
private:
    KDevPG::MemoryPool* m_pool;
};

}

#endif // PYASTTEST_H
