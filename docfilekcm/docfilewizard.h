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
    DocfileWizard(const QString& workingDirectory, QWidget* parent = 0);
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

public slots:
    // Calls python to actually generate the docfile
    bool run();
    void updateOutputFilename(const QString& newModuleName);
    void processScriptOutput();
    void processFinished(int);
    void saveAndClose();
};

#endif // DOCFILEWIZARD_H
