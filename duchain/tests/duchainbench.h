/*
    SPDX-FileCopyrightText: 2014 Benjamin Kaiser <benjaminjkaiser@gmail.com>

    SPDX-License-Identifier: MIT
*/

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
    explicit DUChainBench(QObject* parent = nullptr);
    void initShell();
    ~DUChainBench() override;

    KDevelop::ReferencedTopDUContext parse(const QString& code);

    Python::CodeAst::Ptr m_ast;

private Q_SLOTS:
    void benchSimpleStatements();
    void benchSimpleStatements_data();

private:
    QList<KDevelop::TestFile*> createdFiles;
    QDir testDir;
    QTemporaryDir testDirOwner;
};

#endif // DUCHAINBENCH_H
