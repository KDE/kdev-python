/*
    SPDX-FileCopyrightText: 2012 Sven Brauch svenbrauch @googlemail.com

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef PYASTTEST_H
#define PYASTTEST_H

#include <QtCore/QObject>
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
    explicit PyAstTest(QObject* parent = nullptr);
    void initShell();
    CodeAst::Ptr getAst(QString code);
    void testCode(QString code);
private Q_SLOTS:
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
    void testExceptionHandlers();
    void testCorrectedFuncRanges();
    void testCorrectedFuncRanges_data();
};

}

#endif // PYASTTEST_H
