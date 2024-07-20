/*
    SPDX-FileCopyrightText: 2007 Andreas Pakulat <apaku@gmx.de>
    SPDX-FileCopyrightText: 2007 Piyush verma <piyush.verma@gmail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
 */

#ifndef KDEVPYTHONLANGUAGESUPPORT_H
#define KDEVPYTHONLANGUAGESUPPORT_H

#include <interfaces/iplugin.h>
#include <interfaces/ilanguagecheck.h>
#include <interfaces/ilanguagecheckprovider.h>
#include <language/interfaces/ilanguagesupport.h>
#include <language/duchain/topducontext.h>

#include <QVariant>
#include <QProcess>

namespace KDevelop
{
class ParseJob;
class IDocument;
class ICodeHighlighting;
}

namespace Python
{

class Highlighting;
class Refactoring;
class StyleChecking;

class LanguageSupport
    : public KDevelop::IPlugin
    , public KDevelop::ILanguageSupport
    , public KDevelop::ILanguageCheckProvider
{
    Q_OBJECT
    Q_INTERFACES( KDevelop::ILanguageSupport )
    Q_INTERFACES( KDevelop::ILanguageCheckProvider )

public:
    LanguageSupport(QObject* parent, const KPluginMetaData& metaData, const QVariantList& args = QVariantList());
    ~LanguageSupport() override;
    /*Name Of the Language*/
    QString name() const override;
    /*Parsejob used by background parser to parse given Url*/
    KDevelop::ParseJob *createParseJob( const KDevelop::IndexedString &url ) override;
    /*the code highlighter*/
    KDevelop::ICodeHighlighting* codeHighlighting() const override;
    KDevelop::BasicRefactoring* refactoring() const override;
    
    KDevelop::ContextMenuExtension contextMenuExtension(KDevelop::Context* context, QWidget* parent) override;
    
    static LanguageSupport* self();

    int suggestedReparseDelayForChange(KTextEditor::Document* doc, const KTextEditor::Range& changedRange,
                                       const QString & changedText, bool removal) const override;
    
    KDevelop::SourceFormatterItemList sourceFormatterItems() const override;

    /// Tells whether this plugin is enabled for the given file.
    static bool enabledForFile(const QUrl& url);

    QList<KDevelop::ILanguageCheck*> providedChecks() override;

    int configPages() const override;
    KDevelop::ConfigPage* configPage(int number, QWidget* parent) override;

    int perProjectConfigPages() const override;
    KDevelop::ConfigPage* perProjectConfigPage(int number, const KDevelop::ProjectConfigOptions& options, QWidget* parent) override;

public Q_SLOTS:
    void documentOpened(KDevelop::IDocument*);
    void updateStyleChecking(KDevelop::ReferencedTopDUContext top);

private:
    Highlighting* m_highlighting;
    Refactoring* m_refactoring;
    StyleChecking* m_styleChecking;
    static LanguageSupport* m_self;
};

}

#endif

