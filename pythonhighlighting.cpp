/*****************************************************************************
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 * Copyright (c) 2007 Andreas Pakulat <apaku@gmx.de>                         *
 * Copyright (c) 2011 Sven Brauch <svenbrauch@gmail.com>                     *
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
#include "pythonhighlighting.h"

namespace Python
{

Highlighting::Highlighting( QObject * parent )
       : KDevelop::CodeHighlighting(parent)
{
    
}

void CodeHighlightingInstance::highlightUse(KDevelop::DUContext* context, int index, const QColor& color)
{
    if ( context->localScopeIdentifier() == KDevelop::QualifiedIdentifier("__kdevpythonlanguagesupport_import_helper") ) {
        KDevelop::CodeHighlightingInstance::highlightUse(context, index, QColor(70, 180, 20));
    }
    else {
        KDevelop::CodeHighlightingInstance::highlightUse(context, index, color);
    }
}

CodeHighlightingInstance::CodeHighlightingInstance(const Highlighting* highlighting)
    : KDevelop::CodeHighlightingInstance(highlighting)
{
}

CodeHighlightingInstance* Highlighting::createInstance() const
{
    return new CodeHighlightingInstance(this);
}

}

#include "pythonhighlighting.moc"
