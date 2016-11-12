/*****************************************************************************
 * Copyright (c) 2007 Andreas Pakulat <apaku@gmx.de>                         *
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 *                                                                           *
 * This program is free software; you can redistribute it and/or             *
 * modify it under the terms of the GNU General Public License as            *
 * published by the Free Software Foundation; either version 2 of            *
 * the License, or (at your option) any later version.                       *
 *                                                                           *
 * This program is distributed in the hope that it will be useful,           *
 * but WITHOUT ANY WARRANTY; without even the implied warranty of            *
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             *
 * GNU General Public License for more details.                              *
 *                                                                           *
 * You should have received a copy of the GNU General Public License         *
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.     *
 *****************************************************************************
 */

#ifndef KDEVPYTHONLANGUAGESUPPORT_H
#define KDEVPYTHONLANGUAGESUPPORT_H

#include <interfaces/iplugin.h>
#include <interfaces/ilanguagecheck.h>
#include <interfaces/ilanguagecheckprovider.h>
#include <language/interfaces/ilanguagesupport.h>
#include <QtCore/QVariant>

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

class LanguageSupport
    : public KDevelop::IPlugin
    , public KDevelop::ILanguageSupport
    , public KDevelop::ILanguageCheckProvider
{
    Q_OBJECT
    Q_INTERFACES( KDevelop::ILanguageSupport )
    Q_INTERFACES( KDevelop::ILanguageCheckProvider )

public:
    LanguageSupport( QObject *parent, const QVariantList& args = QVariantList() );
    ~LanguageSupport() override;
    /*Name Of the Language*/
    QString name() const override;
    /*Parsejob used by background parser to parse given Url*/
    KDevelop::ParseJob *createParseJob( const KDevelop::IndexedString &url ) override;
    /*the code highlighter*/
    KDevelop::ICodeHighlighting* codeHighlighting() const override;
    KDevelop::BasicRefactoring* refactoring() const override;
    
    KDevelop::ContextMenuExtension contextMenuExtension(KDevelop::Context* context) override;
    
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

public slots:
    void documentOpened(KDevelop::IDocument*);

private:
    Highlighting* m_highlighting;
    Refactoring *m_refactoring;
    static LanguageSupport* m_self;
};

}

#endif

