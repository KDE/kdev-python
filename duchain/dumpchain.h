/*
    SPDX-FileCopyrightText: 2007 Piyush verma <piyush.verma@gmail.com>

    SPDX-License-Identifier: MIT
*/

#ifndef DUMPCHAIN_H
#define DUMPCHAIN_H

#include <QTextStream>

#include "astdefaultvisitor.h"
#include "pythonduchainexport.h"


namespace KDevelop
{
    class DUContext;
}

namespace Python
{
    
class ParseSession;
class PythonEditorIntegrator;

class KDEVPYTHONDUCHAIN_EXPORT DumpChain
{
public:
    DumpChain();
    virtual ~DumpChain();
    void dump(const KDevelop::DUContext* context, bool imported = false);

private:
    int indent;
};

}

#endif
// kate: space-indent on; indent-width 4; tab-width 4; replace-tabs on; auto-insert-doxygen on
