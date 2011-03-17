/*
 * This file is part of KDevelop
 * Copyright 2011 by Sven Brauch
 */

#ifndef IMPLEMENTFUNCTIONCOMPLETIONITEM_H
#define IMPLEMENTFUNCTIONCOMPLETIONITEM_H

#include <language/codecompletion/codecompletionitem.h>
#include <QStringList>

using namespace KDevelop;

namespace Python {

class ImplementFunctionCompletionItem : public CompletionTreeItem
{
public:
    ImplementFunctionCompletionItem(const QString& name, const QString& arguments, const QString& writeArguments, const QString& previousIndent);
    virtual void execute(KTextEditor::Document* document, const KTextEditor::Range& word);
    virtual QVariant data(const QModelIndex& index, int role, const CodeCompletionModel* model) const;

private:
    QString m_arguments; // displayed
    QString m_writeArguments; // written to the file on execute
    QString m_name;
    QString m_previousIndent;
};

} // namespace Python

#endif // IMPLEMENTFUNCTIONCOMPLETIONITEM_H
