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
#include <language/codecompletion/normaldeclarationcompletionitem.h>
#include <language/duchain/declaration.h>
#include <language/duchain/functiondeclaration.h>

#include <KTextEditor/View>
#include <KTextEditor/Document>

#include "functiondeclarationcompletionitem.h"
#include "navigation/navigationwidget.h"
#include "pythondeclarationcompletionitem.h"

#include <language/codecompletion/codecompletionmodel.h>
#include <language/duchain/types/functiontype.h>
#include "helpers.h"

using namespace KDevelop;
using namespace KTextEditor;

namespace Python {

FunctionDeclarationCompletionItem::FunctionDeclarationCompletionItem(DeclarationPointer decl) : PythonDeclarationCompletionItem(decl), m_argumentHintDepth(0) { }

int FunctionDeclarationCompletionItem::argumentHintDepth() const
{
    return m_argumentHintDepth;
}

void FunctionDeclarationCompletionItem::setArgumentHintDepth(int d)
{
    m_argumentHintDepth = d;
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
                if ( argumentHintDepth() ) {
                    createArgumentList(dec, ret, &highlight, argumentHintDepth());
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
    DUChainPointer<FunctionDeclaration> decl = declaration().dynamicCast<FunctionDeclaration>();
    if ( ! decl.data() ) {
        kError() << "ERROR: could not get declaration data, not executing completion item!";
        return;
    }
    kDebug() << "declaration data: " << decl.data();
    const QString suffix = "()";
    int skip = 2; // place cursor behind bracktes
    if ( decl.data()->type<FunctionType>()->arguments().length() != 0 ) {
        skip = 1; // place cursor in brackets if there's parameters
    }
    document->replaceText(word, decl.data()->identifier().toString() + suffix);
    if ( View* view = document->activeView() ) {
        view->setCursorPosition( Cursor(word.end().line(), word.end().column() + skip) );
    }
}

FunctionDeclarationCompletionItem::~FunctionDeclarationCompletionItem() { }

}