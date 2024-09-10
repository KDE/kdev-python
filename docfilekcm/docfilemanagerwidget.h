/*
    SPDX-FileCopyrightText: 2013 Sven Brauch <svenbrauch@gmail.com>

    SPDX-License-Identifier: GPL-2.0-only OR GPL-3.0-only OR LicenseRef-KDE-Accepted-GPL
*/

#ifndef DOCFILEMANAGERWIDGET_H
#define DOCFILEMANAGERWIDGET_H

#include <QWidget>
#include <QTreeView>
#include <QUrl>
#include <QTemporaryFile>

class DocfileManagerWidget : public QWidget
{
Q_OBJECT
public:
    DocfileManagerWidget(QWidget* parent);
    const QList<QUrl> selectedItems() const;
    static QString docfilePath();

public Q_SLOTS:
    void openDocfilePath();
    void openSelectedInTextEditor();
    void runWizard();
    void copyEditorContents();
    void showSearchPaths();

private:
    QTreeView* filesTreeView;
};

#endif // DOCFILEMANAGERWIDGET_H
