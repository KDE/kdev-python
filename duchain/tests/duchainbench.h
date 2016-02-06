/*****************************************************************************
 * Copyright 2014 Benjamin Kaiser <benjaminjkaiser@gmail.com>                *
 *                                                                           *
 * Permission is hereby granted, free of charge, to any person obtaining     *
 * a copy of this software and associated documentation files (the           *
 * "Software"), to deal in the Software without restriction, including       *
 * without limitation the rights to use, copy, modify, merge, publish,       *
 * distribute, sublicense, and/or sell copies of the Software, and to        *
 * permit persons to whom the Software is furnished to do so, subject to     *
 * the following conditions:                                                 *
 *                                                                           *
 * The above copyright notice and this permission notice shall be            *
 * included in all copies or substantial portions of the Software.           *
 *                                                                           *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,           *
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF        *
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND                     *
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE    *
 * LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION    *
 * OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION     *
 * WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.           *
 *****************************************************************************/

#ifndef PY_DUCHAINBENCH_H
#define PY_DUCHAINBENCH_H

#include <QObject>
#include <QTemporaryDir>
#include "ast.h"
#include <serialization/indexedstring.h>
#include <language/duchain/topducontext.h>
#include <tests/testfile.h>

namespace KDevelop {
    class TopDUContext;
    class ReferencedTopDUContext;
}

using namespace KDevelop;

class DUChainBench : public QObject
{
    Q_OBJECT
public:
    explicit DUChainBench(QObject* parent = 0);
    void initShell();
    virtual ~DUChainBench();

    KDevelop::ReferencedTopDUContext parse(const QString& code);

    Python::CodeAst::Ptr m_ast;

private slots:
    void benchSimpleStatements();
    void benchSimpleStatements_data();

private:
    QList<KDevelop::TestFile*> createdFiles;
    QDir testDir;
    QTemporaryDir testDirOwner;
};

#endif // DUCHAINBENCH_H
