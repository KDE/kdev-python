/*****************************************************************************
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 * Copyright (c) 2007 Andreas Pakulat <apaku@gmx.de>                         *
 * Copyright (c) 2011 Sven Brauch <svenbrauch@gmail.com>                     *
 *                                                                           *
 * This program is free software; you can redistribute it and/or             *
 * modify it under the terms of the GNU General Public License as            *
 * published by the Free Software Foundation; either version 2 of            *
 * the License, or (at your option) any later version.                       *
 *                                                                           *
 * This program is distributed in the hope that it will be useful,           *
 * but WITHOUT ANY WARRANTY; without even the implied warranty of            *
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             *
 * GNU General Public License for more details.                              *
 *                                                                           *
 * You should have received a copy of the GNU General Public License         *
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.     *
 *****************************************************************************
 */
#include "pythonhighlighting.h"

#include <language/duchain/declaration.h>
#include <language/duchain/types/abstracttype.h>
#include <language/duchain/declaration.h>

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

