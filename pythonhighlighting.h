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
#ifndef KDEVPYTHONHIGHLIGHTING_H
#define KDEVPYTHONHIGHLIGHTING_H

#include <QObject>
#include <QHash>
#include <QModelIndex>

#include <language/highlighting/codehighlighting.h>
#include <language/duchain/topducontext.h>

namespace Python
{
    
class Highlighting;

class CodeHighlightingInstance : public KDevelop::CodeHighlightingInstance {
public:
    CodeHighlightingInstance(const Highlighting* highlighting);
    void highlightUse(KDevelop::DUContext* context, int index, const QColor& color) override;
    bool useRainbowColor(KDevelop::Declaration* dec) const override;
private:
    void checkHasBlocks(KDevelop::TopDUContext* top) const;
    mutable bool checked_blocks;
    mutable bool has_blocks;
};

    
class Highlighting : public KDevelop::CodeHighlighting
{
Q_OBJECT
public:
    Highlighting( QObject* parent );
    CodeHighlightingInstance* createInstance() const override;
};
}
#endif
