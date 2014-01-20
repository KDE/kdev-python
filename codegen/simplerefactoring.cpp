/***************************************************************************
 *   This file is part of KDevelop                                         *
 *   Copyright 2012 Sven Brauch <svenbrauch@googlemail.com>                *
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

#include "simplerefactoring.h"
#include <helpers.h>
#include <language/codegen/documentchangeset.h>
#include <language/duchain/navigation/useswidget.h>
#include <language/duchain/navigation/abstractnavigationwidget.h>

#include <interfaces/idocumentcontroller.h>
#include <interfaces/iuicontroller.h>

#include <language/duchain/duchainlock.h>
#include <language/duchain/duchainutils.h>
#include <language/duchain/functiondefinition.h>
#include <language/interfaces/codecontext.h>
#include <language/duchain/navigation/usescollector.h>
#include <language/duchain/use.h>

#include <KParts/MainWindow>

#include <interfaces/contextmenuextension.h>
#include <interfaces/idocument.h>
#include <interfaces/icore.h>
#include <QAction>
#include <QTabWidget>
#include <QLabel>
#include <QBoxLayout>
#include <QLineEdit>
#include <QPushButton>
#include <KLocalizedString>
#include <KIcon>
#include <KTextEditor/Document>
#include <KMessageBox>
#include <QLabel>

#include "duchain/helpers.h"

using namespace KDevelop;

namespace Python {
    
class SimpleRefactoringCollector : public KDevelop::UsesWidget::UsesWidgetCollector {
    public:
    SimpleRefactoringCollector(IndexedDeclaration decl) : UsesWidgetCollector(decl) {
        setCollectConstructors(true);
        setCollectDefinitions(true);
        setCollectOverloads(true);
    }

    virtual void processUses(KDevelop::ReferencedTopDUContext topContext) {
        if ( topContext == Helper::getDocumentationFileContext() ) {
            return;
        }
        m_allUsingContexts << IndexedTopDUContext(topContext.data());
        UsesWidgetCollector::processUses(topContext);
    }

    QVector<IndexedTopDUContext> m_allUsingContexts;
};
 
void SimpleRefactoring::doContextMenu(KDevelop::ContextMenuExtension& extension, KDevelop::Context* context)
{
    if ( DeclarationContext* declContext = dynamic_cast<DeclarationContext*>(context) ) {
        qRegisterMetaType<KDevelop::IndexedDeclaration>("KDevelop::IndexedDeclaration");

        DUChainReadLocker lock;

        Declaration* declaration = declContext->declaration().data();

        if ( declaration ) {
            QFileInfo finfo(declaration->topContext()->url().str());
            if ( declaration->topContext() == Helper::getDocumentationFileContext() ) {
                kDebug() << "in doc file, not offering rename action";
                return;
            }
            if (finfo.isWritable()) {
                QAction* action = new QAction(i18n("Rename \"%1\"...", declaration->qualifiedIdentifier().toString()), 0);
                action->setData(QVariant::fromValue(IndexedDeclaration(declaration)));
                action->setIcon(KIcon("edit-rename"));
                connect(action, SIGNAL(triggered(bool)), this, SLOT(executeRenameAction()));

                extension.addAction(ContextMenuExtension::RefactorGroup, action);
            }
        }
    }
}

void SimpleRefactoring::executeRenameAction()
{
    QAction* action = qobject_cast<QAction*>(sender());
    if ( action ) {
        IndexedDeclaration decl = action->data().value<IndexedDeclaration>();
        if ( ! decl.isValid() ) {
            decl = Helper::declarationUnderCursor();
        }
        startInteractiveRename(decl);
    }
    else {
        kWarning() << "strange problem";
    }    
}

SimpleRefactoring& SimpleRefactoring::self()
{
    static SimpleRefactoring ret;
    return ret;
}


DocumentChangeSet::ChangeResult applyChangesToDeclarations(QString oldName, QString newName, DocumentChangeSet& changes, QList<IndexedDeclaration> declarations) {
    foreach ( const IndexedDeclaration &decl, declarations ) {
        if(!decl.data()) {
            continue;
        }
        TopDUContext* top = decl.data()->topContext();
        if ( decl.data()->range().isEmpty() ) {
            kDebug() << "found empty declaration";
        }
        DocumentChangeSet::ChangeResult result = changes.addChange(DocumentChange(top->url(), decl.data()->rangeInCurrentRevision(), oldName, newName));
        if ( ! result ) {
            return result;
        }
    }
    return DocumentChangeSet::ChangeResult(true);
}

DocumentChangeSet::ChangeResult applyChanges(QString oldName, QString newName, DocumentChangeSet& changes, DUContext* context, int usedDeclarationIndex) {
    if ( usedDeclarationIndex == std::numeric_limits<int>::max() )
        return DocumentChangeSet::ChangeResult(true);

    for ( int a = 0; a < context->usesCount(); ++a ) {
        const Use& use(context->uses()[a]);
        if ( use.m_declarationIndex != usedDeclarationIndex )
            continue;
        if ( use.m_range.isEmpty() ) {
            kDebug() << "found empty use";
            continue;
        }
        DocumentChangeSet::ChangeResult result = changes.addChange(DocumentChange(context->url(), context->transformFromLocalRevision(use.m_range), oldName, newName));
        if ( ! result ) {
            return result;
        }
    }

    foreach(DUContext* child, context->childContexts()) {
        DocumentChangeSet::ChangeResult result = applyChanges(oldName, newName, changes, child, usedDeclarationIndex);
        if ( ! result ) {
            return result;
        }
    }
    return DocumentChangeSet::ChangeResult(true);
}

void SimpleRefactoring::startInteractiveRename(KDevelop::IndexedDeclaration decl)
{
    DUChainReadLocker lock(DUChain::lock());

    Declaration* declaration = decl.data();
    if ( ! declaration ) {
        KMessageBox::error(ICore::self()->uiController()->activeMainWindow(), i18n("No declaration under cursor"));
        return;
    }
    QFileInfo info(declaration->topContext()->url().str());
    if ( ! info.isWritable() ) {
        KMessageBox::error(ICore::self()->uiController()->activeMainWindow(),
                        i18n("Declaration is located in non-writeable file %1.", declaration->topContext()->url().str()));
        return;
    }
    
    if( ! declaration )
        return;

    ///Step 1: Allow the user to specify a replacement name, and allow him to see all uses
    QString originalName = declaration->identifier().identifier().str();
    QString replacementName;

    // Since we don't yet know what the text should be replaced with, we just collect the top-contexts to process
    SimpleRefactoringCollector* collector = new SimpleRefactoringCollector(decl);

    QPointer<QDialog> dialog = new QDialog();

    QTabWidget tabWidget;

    UsesWidget uses(declaration, collector);

    QWidget* navigationWidget = declaration->context()->createNavigationWidget(declaration);
    AbstractNavigationWidget* abstractNavigationWidget = dynamic_cast<AbstractNavigationWidget*>(navigationWidget);

    if ( abstractNavigationWidget ) { //So the context-links work
        connect(&uses, SIGNAL(navigateDeclaration(KDevelop::IndexedDeclaration)), abstractNavigationWidget, SLOT(navigateDeclaration(KDevelop::IndexedDeclaration)));
    }

    QVBoxLayout verticalLayout;
    QHBoxLayout actionsLayout;
    dialog->setLayout(&verticalLayout);
    dialog->setWindowTitle(i18n("Rename %1", declaration->toString()));

    QLabel newNameLabel(i18n("New name:"));
    actionsLayout.addWidget(&newNameLabel);

    QLineEdit edit(declaration->identifier().identifier().str());
    newNameLabel.setBuddy(&edit);

    actionsLayout.addWidget(&edit);
    edit.setText(originalName);
    edit.setFocus();
    edit.selectAll();
    QPushButton goButton(i18n("Rename"));
    goButton.setToolTip(i18n("Note: All overloaded functions, overloads, forward-declarations, etc. will be renamed too"));
    actionsLayout.addWidget(&goButton);
    connect(&goButton, SIGNAL(clicked(bool)), dialog, SLOT(accept()));

    QPushButton cancelButton(i18n("Cancel"));
    actionsLayout.addWidget(&cancelButton);
    verticalLayout.addLayout(&actionsLayout);

    tabWidget.addTab(&uses, i18n("Uses"));
    if ( navigationWidget ) {
        tabWidget.addTab(navigationWidget, i18n("Declaration Info"));
    }

    verticalLayout.addWidget(&tabWidget);

    connect(&cancelButton, SIGNAL(clicked(bool)), dialog, SLOT(reject()));

    lock.unlock();
    dialog->resize(750, 550);

    if ( dialog->exec() != QDialog::Accepted ) {
        kDebug() << "stopped";
        return;
    }
    //It would be nicer to scope this, but then "uses" would not survive

    replacementName = edit.text();


    if ( replacementName == originalName || replacementName.isEmpty() ) {
        return;
    }

    DocumentChangeSet changes;
    lock.lock();
    foreach(const KDevelop::IndexedTopDUContext &collected, collector->m_allUsingContexts) {
        QSet<int> hadIndices;
        foreach(const IndexedDeclaration &decl, collector->declarations()) {
        uint usedDeclarationIndex = collected.data()->indexForUsedDeclaration(decl.data(), false);
        if ( hadIndices.contains(usedDeclarationIndex) ) {
            continue;
        }
        hadIndices.insert(usedDeclarationIndex);
        DocumentChangeSet::ChangeResult result = applyChanges(originalName, replacementName, changes, collected.data(), usedDeclarationIndex);
        if(!result) {
            KMessageBox::error(0, i18n("Applying changes failed: %1", result.m_failureReason));
            return;
        }
        }
    }

    DocumentChangeSet::ChangeResult result = applyChangesToDeclarations(originalName, replacementName, changes, collector->declarations());
    if(!result) {
        KMessageBox::error(0, i18n("Applying changes failed: %1", result.m_failureReason));
        return;
    }

    ///We have to ignore failed changes for now, since uses of a constructor or of operator() may be created on "(" parens
    changes.setReplacementPolicy(DocumentChangeSet::IgnoreFailedChange);
    result = changes.applyAllChanges();
    if(!result) {
        KMessageBox::error(0, i18n("Applying changes failed: %1", result.m_failureReason));
        return;
    }
}
    
}
