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
    : KDevelop::CodeHighlightingInstance(highlighting)
{
}

bool CodeHighlightingInstance::useRainbowColor(KDevelop::Declaration* dec) const
{
    return KDevelop::CodeHighlightingInstance::useRainbowColor(dec);
}

CodeHighlightingInstance* Highlighting::createInstance() const
{
    return new CodeHighlightingInstance(this);
}

}

#include "pythonhighlighting.moc"
