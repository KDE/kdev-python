/*****************************************************************************
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
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
#include "dumpchain.h"
#include "pythoneditorintegrator.h"

#include <language/duchain/types/identifiedtype.h>
#include <language/duchain/ducontext.h>
#include <language/duchain/topducontext.h>
#include <language/duchain/declaration.h>
#include <language/duchain/duchainpointer.h>
#include <language/duchain/use.h>

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
    kDebug() << QString( indent*2, ' ' ) << (imported ? "==import==> Context " : "New Context ") << context->scopeIdentifier(true) << context->transformFromLocalRevision(context->range()) << " " << context << " " << (dynamic_cast<TopDUContext*>(context) ? "top-context" : "");
    if (!imported)
    {
        foreach (Declaration* dec, context->localDeclarations())
        {
            kDebug() << QString( (indent+1)*2, ' ' ) << "Declaration: " << dec->toString() << " [" << dec->qualifiedIdentifier() << "]  "<< dec << "(internal ctx" << dec->internalContext() << ")" << context->transformFromLocalRevision(dec->range()) << ", "<< ( dec->isDefinition() ? "definition, " : "declaration, " ) << dec->uses().count() << "use(s)";
            for( QMap<IndexedString, QList<RangeInRevision> >::const_iterator it = dec->uses().constBegin(); it != dec->uses().constEnd(); ++it )
            {
                kDebug() << QString((indent+1)*2, ' ') << "File:" << it.key().str();
                foreach(const RangeInRevision& r, it.value())
                {
                    kDebug() << QString((indent+2)*2, ' ') << "Use:" << context->transformFromLocalRevision(r);
                }
            }
        }
    }
    ++indent;
    if (!imported)
    {
        foreach (const DUContext::Import& parent, context->importedParentContexts())
        {
            dump(parent.context(dynamic_cast<TopDUContext*>(context)), true);
        }
        foreach (DUContext* child, context->childContexts())
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
