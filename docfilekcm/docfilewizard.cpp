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

#include "docfilewizard.h"

#include <QGroupBox>
#include <QFormLayout>
#include <QLabel>
#include <QLineEdit>
#include <QBoxLayout>
#include <QPushButton>
#include <QTabWidget>
#include <QDebug>

#include <KLocalizedString>
#include <KIcon>
#include <KStandardDirs>
#include <KDialog>
#include <KMessageBox>
#include <KProcess>

DocfileWizard::DocfileWizard(QWidget* parent)
    : QDialog(parent)
    , worker(0)
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
    statusField->resize(width(), 200);
    resultField = new QTextEdit();
    resultField->setText(i18n("The process has not been run yet."));
    resultField->setFontFamily("monospace");
    resultField->resize(width(), 200);
    status->setLayout(new QHBoxLayout);
    tabs->addTab(statusField, i18n("Script output"));
    tabs->addTab(resultField, i18n("Results"));
    status->layout()->addWidget(tabs);

    // The run / close buttons
    QHBoxLayout* buttonsLayout = new QHBoxLayout;
    buttonsLayout->setDirection(QBoxLayout::RightToLeft);
    QPushButton* closeButton = new QPushButton(i18n("Close"));
    closeButton->setIcon(KIcon("dialog-close"));
    QPushButton* runButton = new QPushButton(i18n("Generate"));
    runButton->setIcon(KIcon("tools-wizard"));
    buttonsLayout->addWidget(closeButton);
    buttonsLayout->addWidget(runButton);
    buttonsLayout->addItem(new QSpacerItem(0, 0, QSizePolicy::Expanding, QSizePolicy::Expanding));

    // connections
    QObject::connect(closeButton, SIGNAL(clicked(bool)), this, SLOT(close()));
    QObject::connect(moduleField, SIGNAL(textChanged(QString)), this, SLOT(updateOutputFilename(QString)));
    QObject::connect(runButton, SIGNAL(clicked(bool)), this, SLOT(run()));

    // putting it all together
    layout()->addWidget(interpreter);
    layout()->addWidget(module);
    layout()->addWidget(status);
    layout()->addItem(new QSpacerItem(0, 0, QSizePolicy::Expanding, QSizePolicy::Expanding));
    qobject_cast<QVBoxLayout*>(layout())->addLayout(buttonsLayout); // TODO ugh
}

QString DocfileWizard::fileNameForModule(QString moduleName) const
{
    if ( moduleName.isEmpty() ) {
        return moduleName;
    }
    return moduleName.replace('.', '/') + ".py";
}

bool DocfileWizard::run()
{
    if ( worker ) {
        // process already running
        return 0;
    }
    KStandardDirs d;
    QString scriptUrl = d.findResource("data", "kdevpythonsupport/scripts/introspect.py");
    if ( scriptUrl.isEmpty() ) {
        KMessageBox::error(this, i18n("Couldn't find the introspect.py script; check your installation!"));
        return false;
    }
    statusField->clear();
    resultField->clear();
    QString interpreter = interpreterField->text();
    QString module = moduleField->text();
    worker = new QProcess(this);
    QObject::connect(worker, SIGNAL(readyReadStandardError()), this, SLOT(displayScriptOutput()));
    QObject::connect(worker, SIGNAL(readyReadStandardOutput()), this, SLOT(displayScriptOutput()));
    QObject::connect(worker, SIGNAL(finished(int)), this, SLOT(processFinished(int)));
    worker->start(interpreter, QStringList() << scriptUrl << module);
    return true;
}

void DocfileWizard::displayScriptOutput()
{
    qDebug() << "received script output";
    statusField->append(worker->readAllStandardError());
    resultField->append(worker->readAllStandardOutput());
}

void DocfileWizard::processFinished(int)
{
    worker = 0;
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
