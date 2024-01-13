/*
    SPDX-FileCopyrightText: 2013 Sven Brauch <svenbrauch@gmail.com>

    SPDX-License-Identifier: GPL-2.0-only OR GPL-3.0-only OR LicenseRef-KDE-Accepted-GPL
*/

#include "docfilewizard.h"
#include "docfilemanagerwidget.h"

#include <QGroupBox>
#include <QFormLayout>
#include <QLabel>
#include <QLineEdit>
#include <QBoxLayout>
#include <QPushButton>
#include <QTabWidget>
#include <QScrollBar>
#include <QDebug>
#include <QDir>
#include <QStandardPaths>

#include <KLocalizedString>
#include <KMessageBox>
#include <KProcess>
#include <interfaces/icore.h>
#include <interfaces/iproject.h>
#include <interfaces/iprojectcontroller.h>
#include <project/projectmodel.h>
#include <util/path.h>

DocfileWizard::DocfileWizard(const QString& workingDirectory, QWidget* parent)
    : QDialog(parent)
    , worker(nullptr)
    , workingDirectory(workingDirectory)
{
    setLayout(new QVBoxLayout);

    // The interpreter group box
    QGroupBox* interpreter = new QGroupBox;
    interpreter->setTitle(i18n("Configure the Python interpreter to use"));
    QFormLayout* interpreterLayout = new QFormLayout;
    interpreterField = new QLineEdit("python");
    interpreterLayout->addRow(new QLabel(i18n("Python executable")), interpreterField);
    interpreter->setLayout(interpreterLayout);

    // The module + output file group box
    QGroupBox* module = new QGroupBox;
    module->setTitle(i18n("Select a python module to generate documentation for"));
    QFormLayout* moduleLayout = new QFormLayout;
    moduleField = new QLineEdit;
    moduleLayout->addRow(new QLabel(i18nc("refers to selecting a python module to perform some operation on",
                                          "Target module (e.g. \"math\")")), moduleField);
    outputFilenameField = new QLineEdit;
    moduleLayout->addRow(new QLabel(i18n("Output filename")), outputFilenameField);
    module->setLayout(moduleLayout);

    // Status group box
    QGroupBox* status = new QGroupBox;
    QTabWidget* tabs = new QTabWidget;
    status->setTitle(i18n("Status and output"));
    statusField = new QTextEdit();
    statusField->setText(i18n("The process has not been run yet."));
    statusField->setFontFamily("monospace");
    statusField->setLineWrapMode(QTextEdit::NoWrap);
    statusField->setReadOnly(true);
    statusField->setAcceptRichText(false);
    resultField = new QTextEdit();
    resultField->setText(i18n("The process has not been run yet."));
    resultField->setFontFamily("monospace");
    resultField->setLineWrapMode(QTextEdit::NoWrap);
    resultField->setReadOnly(true);
    resultField->setAcceptRichText(false);
    status->setLayout(new QHBoxLayout);
    tabs->addTab(statusField, i18n("Script output"));
    tabs->addTab(resultField, i18n("Results"));
    status->layout()->addWidget(tabs);

    // The run / close buttons
    QHBoxLayout* buttonsLayout = new QHBoxLayout;
    buttonsLayout->setDirection(QBoxLayout::RightToLeft);
    QPushButton* closeButton = new QPushButton(i18n("Close"));
    closeButton->setIcon(QIcon::fromTheme("dialog-close"));
    saveButton = new QPushButton(i18n("Save and close"));
    saveButton->setEnabled(false);
    saveButton->setIcon(QIcon::fromTheme("dialog-ok-apply"));
    runButton = new QPushButton(i18n("Generate"));
    runButton->setDefault(true);
    runButton->setIcon(QIcon::fromTheme("tools-wizard"));
    buttonsLayout->addWidget(closeButton);
    buttonsLayout->addWidget(runButton);
    buttonsLayout->addWidget(saveButton);
    buttonsLayout->addItem(new QSpacerItem(0, 0, QSizePolicy::Expanding, QSizePolicy::Expanding));

    // connections
    QObject::connect(closeButton, &QAbstractButton::clicked, this, &QWidget::close);
    QObject::connect(saveButton, &QAbstractButton::clicked, this, &DocfileWizard::saveAndClose);
    QObject::connect(moduleField, &QLineEdit::textChanged, this, &DocfileWizard::updateOutputFilename);
    QObject::connect(runButton, &QAbstractButton::clicked, this, &DocfileWizard::run);

    // putting it all together
    layout()->addWidget(interpreter);
    layout()->addWidget(module);
    layout()->addWidget(status);
    layout()->addItem(new QSpacerItem(0, 0, QSizePolicy::Expanding, QSizePolicy::Expanding));
    qobject_cast<QVBoxLayout*>(layout())->addLayout(buttonsLayout); // TODO ugh

    resize(640, 480);
}

const QString DocfileWizard::wasSavedAs() const
{
    return savedAs;
}

QString DocfileWizard::fileNameForModule(QString moduleName) const
{
    if ( moduleName.isEmpty() ) {
        return moduleName;
    }
    return moduleName.replace('.', '/') + ".py";
}

void DocfileWizard::setModuleName(const QString& moduleName)
{
    moduleField->setText(moduleName);
}

bool DocfileWizard::run()
{
    // validate input data, setup and program state
    if ( worker ) {
        // process already running
        return false;
    }
    QString scriptUrl = QStandardPaths::locate(QStandardPaths::GenericDataLocation, "kdevpythonsupport/scripts/introspect.py");
    if ( scriptUrl.isEmpty() ) {
        KMessageBox::error(this, i18n("Couldn't find the introspect.py script; check your installation!"));
        return false;
    }
    if ( workingDirectory.isEmpty() ) {
        KMessageBox::error(this, i18n("Couldn't find a valid kdev-python data directory; check your installation!"));
        return false;
    }
    QString outputFilename = outputFilenameField->text();
    if ( outputFilename.contains("..") ) {
        // protect the user from writing outside the data directory accidentally
        KMessageBox::error(this, i18n("Invalid output filename"));
        return false;
    }

    runButton->setEnabled(false);

    // clean output from previous script runs; since the fields are set to readonly,
    // no user data will be lost
    statusField->clear();
    resultField->clear();

    // set up the process and connect relevant slots
    QString interpreter = interpreterField->text();
    QString module = moduleField->text();
    worker = new QProcess(this);
    QObject::connect(worker, &QProcess::readyReadStandardError, this, &DocfileWizard::processScriptOutput);
    QObject::connect(worker, &QProcess::readyReadStandardOutput, this, &DocfileWizard::processScriptOutput);
    QObject::connect(worker, QOverload<int, QProcess::ExitStatus>::of(&QProcess::finished), this, &DocfileWizard::processFinished);

    // can never have too many slashes
    outputFile.setFileName(workingDirectory + "/" + outputFilename);
    
    QList<KDevelop::IProject*> projs = KDevelop::ICore::self()->projectController()->projects();
    QStringList args;
    args << scriptUrl;
    for (const KDevelop::IProject* proj : projs)
    {
        if ( proj )
            args << proj->path().toLocalFile();
    }
    args << module;
    worker->start(interpreter, args);
    return true;
}

void DocfileWizard::saveAndClose()
{
    bool mayWrite = true;
    if ( outputFile.exists() ) {
        mayWrite = KMessageBox::questionYesNo(this, i18n("The output file <br/>%1<br/> already exists, "
                                                         "do you want to overwrite it?",
                                                          outputFile.fileName())) == KMessageBox::Yes;
    }
    if ( mayWrite ) {
        auto url = QUrl::fromLocalFile(outputFile.fileName());
        Q_ASSERT(url.isLocalFile());
        auto basePath = url.url(QUrl::RemoveFilename | QUrl::PreferLocalFile);

        // should have been done previously
        Q_ASSERT(QDir(basePath).exists());
        if ( ! QDir(basePath).exists() ) {
            QDir(basePath).mkpath(basePath);
        }
        outputFile.open(QIODevice::WriteOnly);
        QString header = "\"\"\"" + i18n("This file contains auto-generated documentation extracted\n"
                                         "from python run-time information. It is analyzed by KDevelop\n"
                                         "to offer features such as code-completion and syntax highlighting.\n"
                                         "If you discover errors in KDevelop's support for this module,\n"
                                         "you can edit this file to correct the errors, e.g. you can add\n"
                                         "additional return statements to functions to control the return\n"
                                         "type to be used for that function by the analyzer.\n"
                                         "Make sure to keep a copy of your changes so you don't accidentally\n"
                                         "overwrite them by re-generating the file.\n") + "\"\"\"\n\n";
        outputFile.write(header.toUtf8() + resultField->toPlainText().toUtf8());
        outputFile.close();
        savedAs = outputFile.fileName();
        close();
    }
}

void DocfileWizard::processScriptOutput()
{
    statusField->insertPlainText(worker->readAllStandardError());
    resultField->insertPlainText(worker->readAllStandardOutput());
    QScrollBar* scrollbar = statusField->verticalScrollBar();
    scrollbar->setValue(scrollbar->maximum());
}

void DocfileWizard::processFinished(int, QProcess::ExitStatus)
{
    worker = nullptr;
    runButton->setEnabled(true);
    saveButton->setEnabled(true);
}

void DocfileWizard::updateOutputFilename(const QString& newModuleName)
{
    QString newFileName = fileNameForModule(newModuleName);
    if ( fileNameForModule(previousModuleName) == outputFilenameField->text() ) {
        // the user didn't edit the field, or edited it to what it is anyways, so update the text
        // otherwise, do nothing.
        outputFilenameField->setText(newFileName);
    }
    previousModuleName = newModuleName;
}

#include "moc_docfilewizard.cpp"
