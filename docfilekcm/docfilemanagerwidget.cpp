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
#include <QTreeView>
#include <QPushButton>
#include <QSplitter>
#include <QLabel>
#include <QTextEdit>
#include <QUrl>
#include <QDebug>
#include <QTemporaryFile>

#include <KStandardDirs>
#include <KMessageBox>
#include <KLocalizedString>
#include <KMimeType>
#include <KRun>
#include <KNS3/DownloadDialog>
#include <KStandardDirs>
#include <knewstuff3/uploaddialog.h>
#include <KTar>
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
    QFileSystemModel *model = new QFileSystemModel;
    model->setRootPath(dir);
    filesTreeView = new QTreeView;
    filesTreeView->setSelectionMode(QAbstractItemView::MultiSelection);
    filesTreeView->setModel(model);
    filesTreeView->setRootIndex(model->index(dir));

    // construct the buttons for up/download
    QVBoxLayout* buttonsLayout = new QVBoxLayout;
    QPushButton* ghnsButton = new QPushButton(i18n("Download new"));
    ghnsButton->setIcon(KIcon("get-hot-new-stuff"));
    QPushButton* generateButton = new QPushButton(i18n("Generate..."));
    generateButton->setIcon(KIcon("tools-wizard"));
    QPushButton* uploadButton = new QPushButton(i18n("Share selected"));
    uploadButton->setIcon(KIcon("applications-internet")); // TODO better icon semantically
    QPushButton* importButton = new QPushButton(i18n("Import from editor"));
    importButton->setToolTip(i18n("Copy the contents of the active editor window "
                                  "to a new file in the documentation directory"));
    importButton->setIcon(KIcon("edit-copy"));
    buttonsLayout->addWidget(ghnsButton);
    buttonsLayout->addWidget(uploadButton);
    buttonsLayout->addWidget(generateButton);
    buttonsLayout->addWidget(importButton);
    QObject::connect(ghnsButton, SIGNAL(clicked(bool)), this, SLOT(showGHNSDialog()));
    QObject::connect(generateButton, SIGNAL(clicked(bool)), this, SLOT(runWizard()));
    QObject::connect(uploadButton, SIGNAL(clicked(bool)), this, SLOT(uploadSelected()));
    QObject::connect(importButton, SIGNAL(clicked(bool)), this, SLOT(copyEditorContents()));

    // construct the buttons for the remaining actions
    QFrame* separator = new QFrame();
    separator->setFrameShape(QFrame::HLine);
    QPushButton* openFileManagerButton = new QPushButton(i18n("Open file manager"));
    openFileManagerButton->setIcon(KIcon("system-file-manager"));
    QPushButton* openTextEditorButton = new QPushButton(i18nc("Edit selected files", "Edit selected"));
    openTextEditorButton->setIcon(KIcon("kate"));
    buttonsLayout->addWidget(separator);
    buttonsLayout->addWidget(openFileManagerButton);
    buttonsLayout->addWidget(openTextEditorButton);
    QObject::connect(openFileManagerButton, SIGNAL(clicked(bool)), this, SLOT(openDocfilePath()));
    QObject::connect(openTextEditorButton, SIGNAL(clicked(bool)), this, SLOT(openSelectedInTextEditor()));

    buttonsLayout->addItem(new QSpacerItem(0, 0, QSizePolicy::Expanding, QSizePolicy::Expanding));

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

void DocfileManagerWidget::openDocfilePath()
{
    KUrl docfileDirectory(docfilePath());
    KRun::runUrl(docfileDirectory, KMimeType::findByUrl(docfileDirectory)->name(), this);
}

void DocfileManagerWidget::copyEditorContents()
{
    KDevelop::IDocumentController* documentController = KDevelop::ICore::self()->documentController();
    if ( documentController->activeDocument() ) {
        if ( KTextEditor::Document* doc = documentController->activeDocument()->textDocument() ) {
            KDialog* dialog = new KDialog(this);
            dialog->setButtons(KDialog::Ok | KDialog::Cancel);
            QWidget* contents = new QWidget;
            contents->setLayout(new QVBoxLayout);
            contents->layout()->addWidget(new QLabel(i18n("Enter a relative target path to copy %1 to:", doc->url().path())));
            QLineEdit* lineEdit = new QLineEdit;
            lineEdit->setText(doc->documentName());
            contents->layout()->addWidget(lineEdit);
            contents->layout()->addWidget(new QLabel(i18n("This path must match what you use in Python to import "
                                                          "this module. For example, enter \"numpy/fft.py\" for numpy.fft")));
            contents->layout()->addWidget(new QLabel(i18n("After copying, you will be editing the new document.")));
            dialog->setMainWidget(contents);
            if ( dialog->exec() == KDialog::Accepted ) {
                KUrl target = KUrl(docfilePath() + "/" + lineEdit->text());
                target.cleanPath(KUrl::SimplifyDirSeparators);
                doc->saveAs(target);
            }
        }
    }
}

void DocfileManagerWidget::openSelectedInTextEditor()
{
    const QList<QUrl> selected = selectedItems();
    foreach ( const QUrl& item, selected ) {
        KUrl fullUrl(item);
        fullUrl.setProtocol("file"); // TODO isn't there a more elegant solution for this?
        KDevelop::ICore::self()->documentController()->openDocument(fullUrl);
    }
}

QString DocfileManagerWidget::docfilePath()
{
    // The directories will be found most-local-first, so using the first one is good.
    KStandardDirs d;
    QStringList paths = d.findDirs("data", "kdevpythonsupport/documentation_files");
    if ( paths.isEmpty() ) {
        return QString::null;
    }
    return paths.first();
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

void DocfileManagerWidget::runWizard()
{
    DocfileWizard wizard(this);
    wizard.resize(640, 480);
    wizard.exec();
}

void DocfileManagerWidget::showGHNSDialog()
{
    KStandardDirs d;
    QString knsrc = d.findResource("config", "kdev_python_docfiles.knsrc");
    KNS3::DownloadDialog dialog(knsrc, this);
    dialog.exec();
}

QTemporaryFile* DocfileManagerWidget::makeArchive(const QList< QUrl >& urls) const
{
    // we need this path to remove it from the path the file should have in the tar archive
    QString base = docfilePath();
    QTemporaryFile* tempfile = new QTemporaryFile("kdevpython_upload_XXXXXX.tar");
    tempfile->open();
    KTar t(tempfile);
    t.open(QIODevice::WriteOnly);
    foreach ( const QUrl& url, urls ) {
        QFileInfo info(url.path());
        const QString pathInArchive = "./" + url.path().remove(0, base.length());
        if ( info.isDir() ) {
            t.addLocalDirectory(url.path(), pathInArchive);
        }
        else {
            t.addLocalFile(url.path(), pathInArchive);
        }
    }
    t.close();
    return tempfile;
}

void DocfileManagerWidget::uploadSelected()
{
    KStandardDirs d;
    QString knsrc = d.findResource("config", "kdev_python_docfiles.knsrc");
    KNS3::UploadDialog dialog(knsrc, this);
    QList<QUrl> selected = selectedItems();
    // TODO don't if there's only one file
    QTemporaryFile* uploadFile = makeArchive(selected);
    qDebug() << "setting upload file name:" << uploadFile->fileName();
    dialog.setUploadFile(uploadFile->fileName());
    dialog.exec();
    // frees memory and deletes the file, too
    delete uploadFile;
}
