/*
    SPDX-FileCopyrightText: 2011 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef IMPORTFILEITEM_H
#define IMPORTFILEITEM_H

#include <language/codecompletion/abstractincludefilecompletionitem.h>
#include <shell/project.h>

#include "duchain/navigation/navigationwidget.h"

namespace Python {

typedef KDevelop::AbstractIncludeFileCompletionItem<NavigationWidget> IncludeFileItemBase;

class ImportFileItem : public IncludeFileItemBase
{

public:
    ImportFileItem(const KDevelop::IncludeItem& include);
    ~ImportFileItem() override;
    
    void execute(KTextEditor::View* view, const KTextEditor::Range& word) override;
    QString moduleName;
    KDevelop::IProject* fromProject;
};

}

#endif // IMPORTFILEITEM_H
