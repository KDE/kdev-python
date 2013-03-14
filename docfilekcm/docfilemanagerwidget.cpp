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

#include <QBoxLayout>
#include <QFileSystemModel>
#include <QTreeView>
#include <QUrl>
#include <QDebug>

#include <KStandardDirs>
#include <KMessageBox>
#include <KLocalizedString>

DocfileManagerWidget::DocfileManagerWidget(QWidget* parent)
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
    QTreeView *tree = new QTreeView(this);
    tree->setSelectionMode(QAbstractItemView::MultiSelection);
    tree->setModel(model);
    tree->setRootIndex(model->index(dirs.first()));

    // construct the buttons for up/download
    // TODO

    QHBoxLayout* layout = new QHBoxLayout(this);
    layout->addWidget(tree);
    setLayout(layout);
}
