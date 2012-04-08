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

#include "declaration.h"
#include "duchain/helpers.h"

#include <language/codecompletion/codecompletionmodel.h>
#include <language/codecompletion/codecompletioncontext.h>
#include <language/duchain/duchainlock.h>
#include <language/duchain/duchain.h>
#include <language/duchain/classfunctiondeclaration.h>
#include <language/duchain/types/functiontype.h>
#include <language/duchain/types/enumeratortype.h>
#include <language/duchain/duchainutils.h>
#include <language/duchain/aliasdeclaration.h>

using namespace KDevelop;

namespace Python {

PythonDeclarationCompletionItem::PythonDeclarationCompletionItem(DeclarationPointer decl, KSharedPtr< CodeCompletionContext > context, int inheritanceDepth)
                               : NormalDeclarationCompletionItem(decl, context, inheritanceDepth)
{
    Q_ASSERT(decl->alwaysForceDirect());
}

    
QVariant Python::PythonDeclarationCompletionItem::data(const QModelIndex& index, int role, const KDevelop::CodeCompletionModel* model) const
{
    QVariant data = KDevelop::NormalDeclarationCompletionItem::data(index, role, model);
    
    switch ( role ) {
        case KDevelop::CodeCompletionModel::MatchQuality: {
            if ( ! declaration() ) return 0;
            if ( declaration()->identifier().identifier().str().startsWith('_') ) {
                return 0;
            }
            if ( declaration()->context()->topContext() == Helper::getDocumentationFileContext() ) {
                return 0;
            }
            if ( model->completionContext()->duContext() == declaration()->context() ) {
                return 5;
            }
            if ( model->completionContext()->duContext()->topContext() == declaration()->context()->topContext() ) {
                return 3;
            }
            return 0;
        }
        case KDevelop::CodeCompletionModel::BestMatchesCount: {
            return 5;
        }
    }
    
    // this looks a bit hackish; still, this is the sort of stuff I think it's not worth doing clean, as the clean way
    // does not really provide objective advantages (except for being clean) and is definitely way more difficult to implement
    if ( data.canConvert<QString>() ) {
        QString s = data.toString();
        s.replace("__kdevpythondocumentation_builtin_", "").replace("<unknown>", "?");
        return QVariant(s);
    }
    else if ( data.canConvert<QStringList>() ) {
        QStringList s = data.toStringList();
        s.replaceInStrings("__kdevpythondocumentation_builtin_", "").replaceInStrings("<unknown>", "?");
        return QVariant(s);
    }
    else return data;
}

}