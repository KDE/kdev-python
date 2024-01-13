/*
    SPDX-FileCopyrightText: 2013 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: LGPL-2.0-or-later
*/

#ifndef CORRECTIONFILEGENERATOR_H
#define CORRECTIONFILEGENERATOR_H

#include <QCache>
#include <QStringList>

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

public Q_SLOTS:
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
    QString m_filePath;
    /// The last known-valid contents of the document
    QStringList m_oldContents;
    /// The current contents of the document to be written to disk later
    QStringList m_code;

    QScopedPointer<FileIndentInformation> m_fileIndents;

    static const int DEFAULT_INDENT_LEVEL = 4;
};

class CorrectionAssistant : public QDialog
{
    Q_OBJECT
public:
    CorrectionAssistant(KDevelop::IndexedDeclaration declaration, CorrectionFileGenerator::HintType hintType,
                        QWidget *parent = nullptr);

    KDevelop::IndexedDeclaration declaration() const;
    CorrectionFileGenerator::HintType hintType() const;

private:
    KDevelop::IndexedDeclaration m_declaration;
    CorrectionFileGenerator::HintType m_hintType;
};

} // namespace python

#endif // CORRECTIONFILEGENERATOR_H
