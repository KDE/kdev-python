/*
    SPDX-FileCopyrightText: 2011 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#include "importfile.h"

#include <KTextEditor/Document>
#include <KTextEditor/View>
#include <language/codecompletion/abstractincludefilecompletionitem.h>

#include "duchain/navigation/navigationwidget.h"

#include <QDebug>
#include "codecompletiondebug.h"

using namespace KDevelop;

namespace Python {
    
ImportFileItem::ImportFileItem(const KDevelop::IncludeItem& include): AbstractIncludeFileCompletionItem< NavigationWidget >(include)
{
    
}

ImportFileItem::~ImportFileItem()
{

}

void ImportFileItem::execute(KTextEditor::View* view, const KTextEditor::Range& word)
{
    qCDebug(KDEV_PYTHON_CODECOMPLETION) << "ImportFileItem executed";
    view->document()->replaceText(word, moduleName);
}


}
