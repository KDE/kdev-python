/*
    SPDX-FileCopyrightText: 2011-2016 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#include "declaration.h"
#include "duchain/helpers.h"

#include <language/codecompletion/codecompletionmodel.h>
#include <language/codecompletion/codecompletioncontext.h>
#include <language/duchain/types/containertypes.h>
#include <language/duchain/duchainlock.h>
#include <language/duchain/duchain.h>
#include <language/duchain/types/typepointer.h>
#include <language/duchain/classfunctiondeclaration.h>
#include <language/duchain/types/functiontype.h>
#include <language/duchain/types/enumeratortype.h>
#include <language/duchain/duchainutils.h>
#include <language/duchain/aliasdeclaration.h>

using namespace KDevelop;

namespace Python {

PythonDeclarationCompletionItem::PythonDeclarationCompletionItem(DeclarationPointer decl, 
                                                                 QExplicitlySharedDataPointer<CodeCompletionContext> context,
                                                                 int inheritanceDepth)
                               : NormalDeclarationCompletionItem(decl, context, inheritanceDepth)
                               , m_typeHint(PythonCodeCompletionContext::NoHint)
                               , m_addMatchQuality(0)
{
    Q_ASSERT(decl->alwaysForceDirect());
    if ( context ) {
        setTypeHint(static_cast<PythonCodeCompletionContext*>(context.data())->itemTypeHint());
    }
}

void PythonDeclarationCompletionItem::addMatchQuality(int add)
{
    m_addMatchQuality += add;
}

void PythonDeclarationCompletionItem::setTypeHint(PythonCodeCompletionContext::ItemTypeHint type)
{
    m_typeHint = type;
}

QString PythonDeclarationCompletionItem::shortenedTypeString(const KDevelop::DeclarationPointer& decl, int desiredTypeLength) const {
    if ( !decl ) {
        return {};
    }
    auto type = decl->abstractType()->toString();
    if ( type.length() > desiredTypeLength ) {
        return type.left(desiredTypeLength) + QStringLiteral("...");
    }
    return type;
}

QVariant PythonDeclarationCompletionItem::data(const QModelIndex& index, int role, const KDevelop::CodeCompletionModel* model) const
{
    switch ( role ) {
        case KDevelop::CodeCompletionModel::MatchQuality: {
            if ( ! declaration() ) return 0;
            if ( ! model->completionContext()->duContext() ) return 0;
            if ( declaration()->identifier().identifier().str().startsWith(QLatin1Char('_')) ) {
                return 0;
            }
            if ( declaration()->context()->topContext() == Helper::getDocumentationFileContext() ) {
                return 0;
            }
            if (   m_typeHint == PythonCodeCompletionContext::IterableRequested 
                && dynamic_cast<ListType*>(declaration()->abstractType().data()) )
            {
                return 10;
            }
            if ( model->completionContext()->duContext() == declaration()->context() ) {
                return 5 + m_addMatchQuality;
            }
            if ( model->completionContext()->duContext()->topContext() == declaration()->context()->topContext() ) {
                return 3 + m_addMatchQuality;
            }
            return m_addMatchQuality;
        }
        case KDevelop::CodeCompletionModel::BestMatchesCount: {
            return 5;
        }
    }

    QVariant data = KDevelop::NormalDeclarationCompletionItem::data(index, role, model);
    if ( data.canConvert<QString>() ) {
        QString s = data.toString();
        s.replace(QStringLiteral("<unknown>"), QStringLiteral("?"));
        return QVariant(s);
    }
    else if ( data.canConvert<QStringList>() ) {
        QStringList s = data.toStringList();
        s.replaceInStrings(QStringLiteral("<unknown>"), QStringLiteral("?"));
        return QVariant(s);
    }
    else return data;
}

}
