/***************************************************************************
 *   This file is part of KDevelop                                         *
 *   Copyright 2013 Sven Brauch <svenbrauch@googlemail.com>                *
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU Library General Public License as       *
 *   published by the Free Software Foundation; either version 2 of the    *
 *   License, or (at your option) any later version.                       *
 *                                                                         *
 *   This program is distributed in the hope that it will be useful,       *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
 *   GNU General Public License for more details.                          *
 *                                                                         *
 *   You should have received a copy of the GNU Library General Public     *
 *   License along with this program; if not, write to the                 *
 *   Free Software Foundation, Inc.,                                       *
 *   51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.         *
 ***************************************************************************/

#ifndef CORRECTIONFILEGENERATOR_H
#define CORRECTIONFILEGENERATOR_H

#include <QStringList>
#include <KDialog>

#include <language/duchain/types/abstracttype.h>
#include <language/duchain/duchain.h>

#include "ui_correctionwidget.h"

class Declaration;

namespace Python {

class CorrectionFileGenerator
{
public:
    CorrectionFileGenerator(const QString& filePath);

    enum HintType {
        FunctionReturnHint,
        LocalVariableHint
    };

    enum StructureType {
        ClassType,
        FunctionType
    };

    void addHint(const QString& identifier, const QString& typeCode, const QString& addImportCode,
                 Declaration* forDeclaration, HintType hintType);

private:
    /// Find the given structure as far as it exists, and return the line number
    /// where more stuff can be added.
    /// You can pass an empty string for class or function, or both.
    int findStructureFor(const QString& klass, const QString& function);

    /// Create an empty structure part at the given line number, such as
    /// class class_identifierSuffix:\n    pass
    /// Returns the line number where more stuff can be added.
    int createStructurePart(const QString& identifierSuffix, StructureType type, int lineno);

    /// Checks if the syntax of the created file is still valid.
    bool checkForValidSyntax();

    /// Write the new contents (from m_code) to disk.
    void snyc();

private:
    /// Absolute path to the file which is being modified by this object
    const QString m_filePath;
    /// The last known-valid contents of the document
    QString m_oldContents;
    /// The current contents of the document to be written to disk later
    QString m_code;
};

class CorrectionAssistant : public KDialog {
Q_OBJECT
public:
    CorrectionAssistant(QWidget* parent = 0);

public slots:
    void accepted();

private:
    /// Generate the "import" statement needed for the given type instantiation
    QString findImportCode(const QString& typedCode) const;

private:
    QScopedPointer<CorrectionFileGenerator> m_generator;
};

} // namespace python

#endif // CORRECTIONFILEGENERATOR_H
