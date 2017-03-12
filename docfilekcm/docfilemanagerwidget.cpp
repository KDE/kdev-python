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
#include "docfilewizard.h"
#include <interfaces/idocumentcontroller.h>
#include <interfaces/icore.h>

#include <QBoxLayout>
#include <QFileSystemModel>
#include <QDialogButtonBox>
#include <QTreeView>
#include <QPushButton>
#include <QSplitter>
#include <QLabel>
#include <QTextEdit>
#include <QUrl>
#include <QDebug>
#include <QTemporaryFile>
#include <QStandardPaths>
#include <QDesktopServices>
#include <QIcon>
#include <QUrl>

#include <KMessageBox>
#include <KLocalizedString>
#include <KTextEditor/Document>

DocfileManagerWidget::DocfileManagerWidget(QWidget* parent)
    : QWidget(parent)
{
    QString dir = docfilePath();
    if ( dir.isEmpty() ) {
        KMessageBox::error(this, i18n("Failed to find a valid data directory for kdevpythonsupport."));
        return;
    }

    // construct the tree view which displays the currently installed files
    QFileSystemModel* model = new QFileSystemModel(this);
    model->setRootPath(dir);
    filesTreeView = new QTreeView;
    filesTreeView->setSelectionMode(QAbstractItemView::MultiSelection);
    filesTreeView->setModel(model);
    filesTreeView->setRootIndex(model->index(dir));

    // construct the buttons for up/download
    QVBoxLayout* buttonsLayout = new QVBoxLayout;
    QPushButton* generateButton = new QPushButton(i18n("Generate..."));
    generateButton->setIcon(QIcon::fromTheme("tools-wizard"));
    QPushButton* importButton = new QPushButton(i18n("Import From Editor"));
    importButton->setToolTip(i18n("Copy the contents of the active editor window "
                                  "to a new file in the documentation directory"));
    buttonsLayout->addWidget(generateButton);
    buttonsLayout->addWidget(importButton);
    QObject::connect(generateButton, &QAbstractButton::clicked, this, &DocfileManagerWidget::runWizard);
    QObject::connect(importButton, &QAbstractButton::clicked, this, &DocfileManagerWidget::copyEditorContents);

    // construct the buttons for the remaining actions
    QFrame* separator = new QFrame();
    separator->setFrameShape(QFrame::HLine);
    QFrame* separator2 = new QFrame();
    separator2->setFrameShape(QFrame::HLine);
    QPushButton* openFileManagerButton = new QPushButton(i18n("Open File Manager"));
    QPushButton* openTextEditorButton = new QPushButton(i18nc("Edit selected files", "Edit selected"));
    QPushButton* searchPathsButton = new QPushButton(i18n("Search Paths..."));
    buttonsLayout->addWidget(separator);
    buttonsLayout->addWidget(openFileManagerButton);
    buttonsLayout->addWidget(openTextEditorButton);
    buttonsLayout->addWidget(separator2);
    buttonsLayout->addWidget(searchPathsButton);
    QObject::connect(openFileManagerButton, &QAbstractButton::clicked, this, &DocfileManagerWidget::openDocfilePath);
    QObject::connect(openTextEditorButton, &QAbstractButton::clicked, this, &DocfileManagerWidget::openSelectedInTextEditor);
    QObject::connect(searchPathsButton, &QAbstractButton::clicked, this, &DocfileManagerWidget::showSearchPaths);

    buttonsLayout->addItem(new QSpacerItem(0, 0, QSizePolicy::Expanding, QSizePolicy::Expanding));

    // arrange the results nicely around a splitter
    QSplitter* splitter = new QSplitter;
    QWidget* w = new QWidget;
    w->setLayout(buttonsLayout);
    splitter->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
    splitter->addWidget(filesTreeView);
    splitter->addWidget(w);
    splitter->setSizes(QList<int>() << 800 << 100);

    setLayout(new QVBoxLayout);
    layout()->addWidget(splitter);
}

void DocfileManagerWidget::showSearchPaths()
{
    QStringList dirs = QStandardPaths::locateAll(QStandardPaths::GenericDataLocation, "kdevpythonsupport/documentation_files", QStandardPaths::LocateDirectory);
    QLabel* dirsMessageLabel = new QLabel(i18nc("displays a list of search paths below",
                                                "Paths searched for documentation by kdev-python (in this order):"));
    QTextEdit* paths = new QTextEdit;
    paths->setPlainText(dirs.join("\n"));
    paths->setReadOnly(true);

    QDialog* message = new QDialog(this);
    message->setLayout(new QVBoxLayout);
    message->layout()->addWidget(dirsMessageLabel);
    message->layout()->addWidget(paths);
    QWidget* closeWidget = new QWidget;
    QPushButton* closeButton = new QPushButton("Close");
    closeWidget->setLayout(new QHBoxLayout);
    closeWidget->layout()->addItem(new QSpacerItem(1, 1, QSizePolicy::Expanding, QSizePolicy::Expanding));
    closeWidget->layout()->addWidget(closeButton);
    message->layout()->addWidget(closeWidget);

    QObject::connect(closeButton, &QAbstractButton::clicked, message, &QWidget::close);
    message->resize(600, 200);
    message->exec();
}

void DocfileManagerWidget::openDocfilePath()
{
    if ( QDir(docfilePath()).exists() ) {
        QDesktopServices::openUrl(QUrl::fromLocalFile(docfilePath()));
    }
}

void DocfileManagerWidget::copyEditorContents()
{
    KDevelop::IDocumentController* documentController = KDevelop::ICore::self()->documentController();
    if ( documentController->activeDocument() ) {
        if ( KTextEditor::Document* doc = documentController->activeDocument()->textDocument() ) {
            auto dialog = new QDialog(this);
            auto buttonbox = new QDialogButtonBox(QDialogButtonBox::Ok | QDialogButtonBox::Cancel, dialog);
            connect(buttonbox->button(QDialogButtonBox::Ok), &QPushButton::clicked,
                    dialog, &QDialog::accept);
            connect(buttonbox->button(QDialogButtonBox::Cancel), &QPushButton::clicked,
                    dialog, &QDialog::reject);
            dialog->setLayout(new QVBoxLayout);
            dialog->layout()->addWidget(new QLabel(i18n("Enter a relative target path to copy %1 to:", doc->url().path())));
            QLineEdit* lineEdit = new QLineEdit;
            lineEdit->setText(doc->documentName());
            dialog->layout()->addWidget(lineEdit);
            dialog->layout()->addWidget(new QLabel(i18n("This path must match what you use in Python to import "
                                                          "this module. For example, enter \"numpy/fft.py\" for numpy.fft")));
            dialog->layout()->addWidget(new QLabel(i18n("After copying, you will be editing the new document.")));
            dialog->layout()->addWidget(buttonbox);
            if ( dialog->exec() == QDialog::Accepted ) {
                auto target = QUrl::fromLocalFile(docfilePath() + "/" + lineEdit->text());
                // TODO QUrl: cleanPath?
                QDir d(target.url());
                if ( ! d.exists() ) {
                    d.mkpath(d.absolutePath());
                }
                doc->saveAs(target);
            }
        }
    }
}

void DocfileManagerWidget::openSelectedInTextEditor()
{
    const QList<QUrl> selected = selectedItems();
    if ( selected.isEmpty() ) {
        KMessageBox::information(this, i18n("Please select at least one file from the list for editing."));
    }
    foreach ( const QUrl& item, selected ) {
        KDevelop::ICore::self()->documentController()->openDocument(item);
    }
}

QString DocfileManagerWidget::docfilePath()
{
    // finds a local directory which is contained in the dirs searched by the parser, code
    // and creates it if it doesn't exist
    QString path = QStandardPaths::writableLocation(QStandardPaths::GenericDataLocation) + "/" + "kdevpythonsupport/documentation_files/";
    QDir dir(path);
    dir.mkpath(path);
    return path;
}

const QList<QUrl> DocfileManagerWidget::selectedItems() const
{
    const QModelIndexList items = filesTreeView->selectionModel()->selectedRows();
    QList<QUrl> urls;
    const QFileSystemModel* fsmodel = qobject_cast<QFileSystemModel*>(filesTreeView->model());
    foreach ( const QModelIndex& index, items ) {
        urls << QUrl::fromLocalFile(fsmodel->filePath(index));
    }
    return urls;
}

void DocfileManagerWidget::runWizard()
{
    DocfileWizard wizard(docfilePath(), this);
    wizard.exec();
}
