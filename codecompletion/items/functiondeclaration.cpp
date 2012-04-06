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
#include <language/duchain/functiondeclaration.h>
#include <language/codecompletion/codecompletionmodel.h>
#include <language/duchain/types/functiontype.h>
#include <language/duchain/aliasdeclaration.h>

#include <KTextEditor/View>
#include <KTextEditor/Document>

#include "duchain/navigation/navigationwidget.h"
#include "codecompletion/helpers.h"
#include "declaration.h"


using namespace KDevelop;
using namespace KTextEditor;

namespace Python {

FunctionDeclarationCompletionItem::FunctionDeclarationCompletionItem(DeclarationPointer decl) 
    : PythonDeclarationCompletionItem(decl), m_atArgument(-1) { }

int FunctionDeclarationCompletionItem::atArgument() const
{
    return m_atArgument;
}

void FunctionDeclarationCompletionItem::setAtArgument(int d)
{
    m_atArgument = d;
}

int FunctionDeclarationCompletionItem::argumentHintDepth() const
{
    return m_atArgument >= 0;
}

QVariant FunctionDeclarationCompletionItem::data(const QModelIndex& index, int role, const KDevelop::CodeCompletionModel* model) const
{
    FunctionDeclaration* dec = dynamic_cast<FunctionDeclaration*>(m_declaration.data());
    DUChainReadLocker lock(DUChain::lock());
    switch ( role ) {
        case Qt::DisplayRole: {
            if ( index.column() == KDevelop::CodeCompletionModel::Arguments ) {
                if ( ! dec ) return QVariant();
                if (FunctionType::Ptr functionType = dec->type<FunctionType>()) {
                    QString ret;
                    createArgumentList(dec, ret, 0);
                    return ret.replace("__kdevpythondocumentation_builtin_", "");
                }
            }
        }
        case KDevelop::CodeCompletionModel::HighlightingMethod: {
            if ( index.column() == KDevelop::CodeCompletionModel::Arguments )
                return QVariant(KDevelop::CodeCompletionModel::CustomHighlighting);
            break;
        }
        case KDevelop::CodeCompletionModel::CustomHighlight: {
            if ( index.column() == KDevelop::CodeCompletionModel::Arguments ) {
                if ( ! dec ) return QVariant();
                QString ret;
                QList<QVariant> highlight;
                if ( atArgument() ) {
                    createArgumentList(dec, ret, &highlight, atArgument());
                }
                else {
                    createArgumentList(dec, ret, 0);
                }
                return QVariant(highlight);
            }
        }
    }
    return Python::PythonDeclarationCompletionItem::data(index, role, model);
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
    kDebug() << "declaration data: " << fdecl.data();
    const QString suffix = "()";
    int skip = 2; // place cursor behind bracktes
    if ( fdecl.data()->type<FunctionType>()->arguments().length() != 0 ) {
        skip = 1; // place cursor in brackets if there's parameters
    }
    document->replaceText(word, decl.data()->identifier().toString() + suffix);
    if ( View* view = document->activeView() ) {
        view->setCursorPosition( Cursor(word.end().line(), word.end().column() + skip) );
    }
}

FunctionDeclarationCompletionItem::~FunctionDeclarationCompletionItem() { }

}