/*
    SPDX-FileCopyrightText: 2007 Piyush verma <piyush.verma@gmail.com>
    SPDX-FileCopyrightText: 2007 Andreas Pakulat <apaku@gmx.de>
    SPDX-FileCopyrightText: 2011 Sven Brauch <svenbrauch@gmail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
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
