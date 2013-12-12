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

#include <QCache>
#include <QStringList>
#include <KDialog>

#include <interfaces/context.h>
#include <interfaces/contextmenuextension.h>
#include <language/duchain/types/abstracttype.h>
#include <language/duchain/declaration.h>
#include <language/duchain/duchain.h>

#include "parser/codehelpers.h"

#include "ui_correctionwidget.h"

namespace Python {

class CorrectionFileGenerator;

class TypeCorrection : public QObject
{
    Q_OBJECT
public:
    static TypeCorrection& self();
    void doContextMenu(KDevelop::ContextMenuExtension& extension, KDevelop::Context* context);

public slots:
    void executeSpecifyTypeAction();
    void accepted();

private:
    TypeCorrection();

    QScopedPointer<Ui::CorrectionWidget> m_ui;
};

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
        FunctionType,
        MemberFunctionType
    };

    void addHint(const QString& typeCode, const QStringList &modules, KDevelop::Declaration* forDeclaration, HintType hintType);

private:
    /// Find the given structure as far as it exists, and return the line number
    /// where more stuff can be added.
    /// You can pass an empty string for class or function, or both.
    int findStructureFor(const QString& klass, const QString& function);

    /// Create an empty structure part, such as
    /// class class_identifierSuffix:\n    pass
    QString createStructurePart(const QString& identifierSuffix, StructureType type);

    /// Checks if the syntax of the created file is still valid.
    bool checkForValidSyntax();

private:
    /// The file which is being modified by this object
    QFile m_file;
    /// The last known-valid contents of the document
    QStringList m_oldContents;
    /// The current contents of the document to be written to disk later
    QStringList m_code;

    QScopedPointer<FileIndentInformation> m_fileIndents;

    static const int DEFAULT_INDENT_LEVEL = 4;
};

class CorrectionAssistant : public KDialog
{
    Q_OBJECT
public:
    CorrectionAssistant(KDevelop::IndexedDeclaration declaration, CorrectionFileGenerator::HintType hintType, QWidget *parent = 0);

    KDevelop::IndexedDeclaration declaration() const;
    CorrectionFileGenerator::HintType hintType() const;

private:
    KDevelop::IndexedDeclaration m_declaration;
    CorrectionFileGenerator::HintType m_hintType;
};

} // namespace python

#endif // CORRECTIONFILEGENERATOR_H
