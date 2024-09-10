/*
    SPDX-FileCopyrightText: 2013 Sven Brauch <svenbrauch@gmail.com>

    SPDX-License-Identifier: GPL-2.0-only OR GPL-3.0-only OR LicenseRef-KDE-Accepted-GPL
*/

#ifndef DOCFILEWIZARD_H
#define DOCFILEWIZARD_H

#include <QWidget>
#include <QDialog>
#include <QLineEdit>
#include <QTextEdit>
#include <QFile>
#include <KProcess>

class DocfileWizard : public QDialog
{
Q_OBJECT
public:
    DocfileWizard(const QString& workingDirectory, QWidget* parent = nullptr);
    QString fileNameForModule(QString moduleName) const;
    void setModuleName(const QString& moduleName);
    // Returns the path the file was saved as when exiting the dialog,
    // or an empty string if the file was not saved.
    const QString wasSavedAs() const;

private:
    QLineEdit* interpreterField;
    QLineEdit* moduleField;
    QLineEdit* outputFilenameField;
    QTextEdit* statusField;
    QTextEdit* resultField;
    // used for deciding whether to auto-update the output filename text field
    QString previousModuleName;
    QProcess* worker;
    QFile outputFile;
    QString savedAs;
    const QString workingDirectory;

    QPushButton* runButton;
    QPushButton* saveButton;

public Q_SLOTS:
    // Calls python to actually generate the docfile
    bool run();
    void updateOutputFilename(const QString& newModuleName);
    void processScriptOutput();
    void processFinished(int, QProcess::ExitStatus);
    void saveAndClose();
};

#endif // DOCFILEWIZARD_H
