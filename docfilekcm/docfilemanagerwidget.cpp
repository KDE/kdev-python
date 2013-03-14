/*
 * This file is part of kdev-python
 * Copyright 2013  Sven Brauch <svenbrauch@gmail.com>
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License as
 * published by the Free Software Foundation; either version 2 of
 * the License or (at your option) version 3 or any later version
 * accepted by the membership of KDE e.V. (or its successor approved
 * by the membership of KDE e.V.), which shall act as a proxy
 * defined in Section 14 of version 3 of the license.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 */

#include "docfilemanagerwidget.h"
#include "kcm_docfiles.h"

#include <QBoxLayout>
#include <QFileSystemModel>
#include <QTreeView>
#include <QPushButton>
#include <QSplitter>
#include <QLabel>
#include <QTextEdit>
#include <QUrl>
#include <QDebug>

#include <KStandardDirs>
#include <KMessageBox>
#include <KLocalizedString>

DocfileManagerWidget::DocfileManagerWidget(QWidget* parent, DocfilesKCModule* kcmodule)
    : QWidget(parent)
{
    // The directories will be found most-local-first, so using the first one is good.
    KStandardDirs d;
    QStringList dirs = d.findDirs("data", "kdevpythonsupport/documentation_files");
    if ( dirs.isEmpty() ) {
        KMessageBox::error(this, i18n("Failed to find a valid data directory for kdevpythonsupport."));
        return;
    }

    // construct the tree view which displays the currently installed files
    QFileSystemModel *model = new QFileSystemModel;
    model->setRootPath(dirs.first());
    filesTreeView = new QTreeView;
    filesTreeView->setSelectionMode(QAbstractItemView::MultiSelection);
    filesTreeView->setModel(model);
    filesTreeView->setRootIndex(model->index(dirs.first()));

    // construct the buttons for up/download
    QVBoxLayout* buttonsLayout = new QVBoxLayout;
    QPushButton* ghnsButton = new QPushButton(i18n("Download new"));
    ghnsButton->setIcon(KIcon("get-hot-new-stuff"));
    QPushButton* generateButton = new QPushButton(i18n("Generate..."));
    generateButton->setIcon(KIcon("tools-wizard"));
    QPushButton* uploadButton = new QPushButton(i18n("Share selected"));
    uploadButton->setIcon(KIcon("applications-internet")); // TODO better icon semantically
    buttonsLayout->addWidget(ghnsButton);
    buttonsLayout->addWidget(generateButton);
    buttonsLayout->addWidget(uploadButton);
    buttonsLayout->addItem(new QSpacerItem(0, 0, QSizePolicy::Expanding, QSizePolicy::Expanding));
    QObject::connect(ghnsButton, SIGNAL(clicked(bool)), kcmodule, SLOT(showGHNSDialog()));
    QObject::connect(generateButton, SIGNAL(clicked(bool)), kcmodule, SLOT(runWizard()));
    QObject::connect(uploadButton, SIGNAL(clicked(bool)), kcmodule, SLOT(uploadSelected()));

    // arrange the results nicely around a splitter
    QSplitter* splitter = new QSplitter;
    QWidget* w = new QWidget;
    w->setLayout(buttonsLayout);
    splitter->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
    splitter->addWidget(filesTreeView);
    splitter->addWidget(w);
    splitter->setSizes(QList<int>() << 800 << 100);

    setLayout(new QHBoxLayout);
    layout()->addWidget(splitter);
}

const QList<QUrl> DocfileManagerWidget::selectedItems() const
{
    const QModelIndexList items = filesTreeView->selectionModel()->selectedRows();
    QList<QUrl> urls;
    const QFileSystemModel* fsmodel = qobject_cast<QFileSystemModel*>(filesTreeView->model());
    foreach ( const QModelIndex& index, items ) {
        urls << QUrl(fsmodel->filePath(index));
    }
    return urls;
}
