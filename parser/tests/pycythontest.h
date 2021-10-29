/*
    SPDX-FileCopyrightText: 2012 Sven Brauch svenbrauch @googlemail.com
    SPDX-FileCopyrightText: 2014 Gregor Vollmer <gregor@celement.de>

    SPDX-License-Identifier: GPL-2.0-or-later
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
    explicit PyCythonTest(QObject* parent = nullptr);
    void initShell();
    CodeAst::Ptr getAst(QString code, const QUrl& filename);

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
