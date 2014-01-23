/*****************************************************************************
 * Copyright (c) 2011 Sven Brauch <svenbrauch@googlemail.com>                *
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

#include "functiondeclaration.h"

#include <language/codecompletion/normaldeclarationcompletionitem.h>
#include <language/codecompletion/codecompletionmodel.h>
#include <language/duchain/types/functiontype.h>
#include <language/duchain/aliasdeclaration.h>

#include <KTextEditor/View>
#include <KTextEditor/Document>
#include <KLocalizedString>

#include "duchain/navigation/navigationwidget.h"
#include "types/variablelengthcontainer.h"
#include "codecompletion/helpers.h"
#include "declaration.h"
#include "declarations/functiondeclaration.h"
#include "duchain/helpers.h"


using namespace KDevelop;
using namespace KTextEditor;

namespace Python {

FunctionDeclarationCompletionItem::FunctionDeclarationCompletionItem(DeclarationPointer decl, CodeCompletionContext::Ptr context) 
    : PythonDeclarationCompletionItem(decl, context)
    , m_atArgument(-1)
    , m_depth(0)
    , m_isImportItem(false)
{

}

int FunctionDeclarationCompletionItem::atArgument() const
{
    return m_atArgument;
}

void FunctionDeclarationCompletionItem::setDepth(int d)
{
    m_depth = d;
}

void FunctionDeclarationCompletionItem::setAtArgument(int d)
{
    m_atArgument = d;
}

int FunctionDeclarationCompletionItem::argumentHintDepth() const
{
    return m_depth;
}

QVariant FunctionDeclarationCompletionItem::data(const QModelIndex& index, int role, const KDevelop::CodeCompletionModel* model) const
{
    switch ( role ) {
        case Qt::DisplayRole: {
            if ( index.column() == KDevelop::CodeCompletionModel::Arguments ) {
                DUChainReadLocker lock;
                if ( Declaration* dec = dynamic_cast<FunctionDeclaration*>(m_declaration.data()) ) {
                    if (FunctionType::Ptr functionType = dec->type<FunctionType>()) {
                        QString ret;
                        createArgumentList(dec, ret, 0, 0, false);
                        return ret.replace("__kdevpythondocumentation_builtin_", "");
                    }
                }
                 return QVariant();
            }
            if ( index.column() == KDevelop::CodeCompletionModel::Prefix ) {
                DUChainReadLocker lock;
                if ( Declaration* dec = dynamic_cast<FunctionDeclaration*>(m_declaration.data()) ) {
                    if ( FunctionType::Ptr type = dec->type<FunctionType>() ) {
                        return i18n("function") + " -> " + type->returnType()->toString().replace("__kdevpythondocumentation_builtin_", "");
                    }
                }
                return QVariant();
            }
            break;
        }
        case KDevelop::CodeCompletionModel::HighlightingMethod: {
            if ( index.column() == KDevelop::CodeCompletionModel::Arguments )
                return QVariant(KDevelop::CodeCompletionModel::CustomHighlighting);
            break;
        }
        case KDevelop::CodeCompletionModel::CustomHighlight: {
            if ( index.column() == KDevelop::CodeCompletionModel::Arguments ) {
                QList<QVariant> highlight;
                QString ret;
                DUChainReadLocker lock;
                if ( Declaration* dec = dynamic_cast<FunctionDeclaration*>(m_declaration.data()) ) {
                    if ( atArgument() ) {
                        createArgumentList(dec, ret, &highlight, atArgument(), false);
                    }
                    else {
                        createArgumentList(dec, ret, 0, 0, false);
                    }
                }
                return QVariant(highlight);
            }
        }
        case KDevelop::CodeCompletionModel::MatchQuality: {
            DUChainReadLocker lock;
            if ( Declaration* dec = dynamic_cast<FunctionDeclaration*>(m_declaration.data()) ) {
                if ( m_typeHint == PythonCodeCompletionContext::IterableRequested
                     && dec->type<FunctionType>()
                     && dynamic_cast<VariableLengthContainer*>(dec->type<FunctionType>()->returnType().unsafeData()) )
                {
                    return 2 + PythonDeclarationCompletionItem::data(index, role, model).toInt();
                }
            }
            return PythonDeclarationCompletionItem::data(index, role, model);
        }
    }
    return Python::PythonDeclarationCompletionItem::data(index, role, model);
}

void FunctionDeclarationCompletionItem::setIsImportItem(bool isImportItem)
{
    m_isImportItem = isImportItem;
}

void FunctionDeclarationCompletionItem::executed(KTextEditor::Document* document, const KTextEditor::Range& word)
{
    kDebug() << "FunctionDeclarationCompletionItem executed";
    DeclarationPointer decl(declaration());
    DUChainPointer<FunctionDeclaration> fdecl;
    AliasDeclaration* alias = dynamic_cast<AliasDeclaration*>(decl.data());
    if ( alias ) {
        DUChainReadLocker lock(DUChain::lock());
        fdecl = dynamic_cast<FunctionDeclaration*>(alias->aliasedDeclaration().declaration());
    }
    else {
        fdecl = decl.dynamicCast<FunctionDeclaration>();
    }
    if ( ! fdecl.data() || ! fdecl.dynamicCast<FunctionDeclaration>() ) {
        kError() << "ERROR: could not get declaration data, not executing completion item!";
        return;
    }
    QString suffix = "()";
    KTextEditor::Range checkSuffix(word.end().line(), word.end().column(), word.end().line(), word.end().column() + 2);
    if ( m_isImportItem || document->text(checkSuffix) == "()"
         || Helper::findDecoratorByName(fdecl.data(), QLatin1String("property")) )
    {
        // don't insert brackets if they're already there,
        // or if the item is an import item.
        suffix = "";
    }
    // place cursor behind bracktes by default
    int skip = 2;
    if ( fdecl.data()->type<FunctionType>()->arguments().length() != 0 ) {
        // place cursor in brackets if there's parameters
        skip = 1;
    }
    document->replaceText(word, decl.data()->identifier().toString() + suffix);
    if ( View* view = document->activeView() ) {
        view->setCursorPosition( Cursor(word.end().line(), word.end().column() + skip) );
    }
}

FunctionDeclarationCompletionItem::~FunctionDeclarationCompletionItem() { }

}
