/*
    SPDX-FileCopyrightText: 2007 Piyush verma <piyush.verma@gmail.com>
    SPDX-FileCopyrightText: 2007 Andreas Pakulat <apaku@gmx.de>
    SPDX-FileCopyrightText: 2011 Sven Brauch <svenbrauch@gmail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#include "pythonhighlighting.h"

#include <language/duchain/declaration.h>
#include <language/duchain/types/abstracttype.h>

using namespace KDevelop;

namespace Python
{

Highlighting::Highlighting( QObject * parent )
       : KDevelop::CodeHighlighting(parent)
{
    
}

void CodeHighlightingInstance::highlightUse(KDevelop::DUContext* context, int index, const QColor& color)
{
    KDevelop::CodeHighlightingInstance::highlightUse(context, index, color);
}

CodeHighlightingInstance::CodeHighlightingInstance(const Highlighting* highlighting)
    : KDevelop::CodeHighlightingInstance(highlighting),
      checked_blocks(false),
      has_blocks(false)
{
}

bool CodeHighlightingInstance::useRainbowColor(KDevelop::Declaration* dec) const
{
    if (dec->context()->type() == DUContext::Other) {
        // Normal non-toplevel variable, comprehension variable or lambda parameter.
        return true;
    }
    if ( ! checked_blocks ) {
        checkHasBlocks(dec->topContext());
    }
    // no functions/classes in file and it's a normal variable and in the top level
    if ( ! has_blocks && ! dec->internalContext() && dec->context() == dec->topContext() ) {
        return true;
    }
    return KDevelop::CodeHighlightingInstance::useRainbowColor(dec);
}

void CodeHighlightingInstance::checkHasBlocks(TopDUContext* top) const
{
    QVector<Declaration*> declarations = top->localDeclarations();
    for ( int i = 0; i < declarations.size(); i++ ) {
        if ( declarations.at(i)->internalContext() ) {
           has_blocks = true;
           break;
        }
    }
    checked_blocks = true;
}

CodeHighlightingInstance* Highlighting::createInstance() const
{
    return new CodeHighlightingInstance(this);
}

}

