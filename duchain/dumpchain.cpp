/*****************************************************************************
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 *                                                                           *
 * Permission is hereby granted, free of charge, to any person obtaining     *
 * a copy of this software and associated documentation files (the           *
 * "Software"), to deal in the Software without rekDebug()iction, including       *
 * without limitation the rights to use, copy, modify, merge, publish,       *
 * dikDebug()ibute, sublicense, and/or sell copies of the Software, and to        *
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

#include <language/duchain/identifiedtype.h>
#include <language/duchain/ducontext.h>
#include <language/duchain/topducontext.h>
#include <language/duchain/declaration.h>
#include <language/duchain/definition.h>
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
    kDebug() << QString( indent*2, ' ' ) << (imported ? "==import==> Context " : "New Context ") << context->scopeIdentifier(true) << context->range().textRange() << " " << context << " " << (dynamic_cast<TopDUContext*>(context) ? "top-context" : "");
    if (!imported)
    {
        foreach (Declaration* dec, context->localDeclarations())
        {
            kDebug() << QString( (indent+1)*2, ' ' ) << "Declaration: " << dec->toString() << " [" << dec->qualifiedIdentifier() << "]  "<< dec << "(internal ctx" << dec->internalContext() << ")" << dec->range().textRange() << ", "<< ( dec->isDefinition() ? "defined, " : ( dec->definition() ? "" : "no definition, ") ) << dec->uses().count() << "use(s)";
            if (dec->definition())
                kDebug() << QString( (indent+1)*2, ' ' ) << "Definition: " << dec->definition()->range().textRange() << endl;
            foreach( Use* use, dec->uses() )
            {
                kDebug() << QString((indent+1)*2, ' ') << "Use:" << use->range().textRange();
            }
        }
    }
    ++indent;
    if (!imported)
    {
        foreach (DUContextPointer parent, context->importedParentContexts())
        {
            dump(parent.data(), true);
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
