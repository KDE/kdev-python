/*
    SPDX-FileCopyrightText: 2007 Piyush verma <piyush.verma@gmail.com>

    SPDX-License-Identifier: MIT
*/

#include "dumpchain.h"
#include "pythoneditorintegrator.h"

#include <language/duchain/types/identifiedtype.h>
#include <language/duchain/ducontext.h>
#include <language/duchain/topducontext.h>
#include <language/duchain/declaration.h>
#include <language/duchain/duchainpointer.h>
#include <language/duchain/use.h>

#include <QDebug>
#include "duchaindebug.h"

using namespace KDevelop;

namespace Python {


DumpChain::DumpChain()
    : indent(0)
{
}

void DumpChain::dump( DUContext * context, bool imported )
{
    if( !context )
        return;
    qCDebug(KDEV_PYTHON_DUCHAIN) << QString( indent*2, QLatin1Char(' ') ) << (imported ? "==import==> Context " : "New Context ") << context->scopeIdentifier(true) << context->transformFromLocalRevision(context->range()) << " " << context << " " << (dynamic_cast<TopDUContext*>(context) ? "top-context" : "");
    if (!imported)
    {
        for (Declaration* dec : context->localDeclarations())
        {
            const auto uses = dec->uses();
            qCDebug(KDEV_PYTHON_DUCHAIN) << QString( (indent+1)*2, QLatin1Char(' ') ) << "Declaration: " << dec->toString() << " [" << dec->qualifiedIdentifier() << "]  "<< dec << "(internal ctx" << dec->internalContext() << ")" << context->transformFromLocalRevision(dec->range()) << ", "<< ( dec->isDefinition() ? "definition, " : "declaration, " ) << uses.count() << "use(s)";
            for (auto it = uses.constBegin(); it != uses.constEnd(); ++it)
            {
                qCDebug(KDEV_PYTHON_DUCHAIN) << QString((indent+1)*2, QLatin1Char(' ')) << "File:" << it.key().str();
                for (const RangeInRevision& r : it.value())
                {
                    qCDebug(KDEV_PYTHON_DUCHAIN) << QString((indent+2)*2, QLatin1Char(' ')) << "Use:" << context->transformFromLocalRevision(r);
                }
            }
        }
    }
    ++indent;
    if (!imported)
    {
        for (const DUContext::Import& parent : context->importedParentContexts())
        {
            dump(parent.context(dynamic_cast<TopDUContext*>(context)), true);
        }
        for (DUContext* child : context->childContexts())
        {
            dump(child);
        }
    }
    --indent;
}

DumpChain::~ DumpChain( )
{
}

}
