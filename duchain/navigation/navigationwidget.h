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

#ifndef NAVIGATIONWIDGET_H
#define NAVIGATIONWIDGET_H

#include <language/duchain/navigation/abstractnavigationwidget.h>
#include <language/util/includeitem.h>
#include "pythonduchainexport.h"
#include <QWebView>

namespace Python {

class KDEVPYTHONDUCHAIN_EXPORT NavigationWidget : public KDevelop::AbstractNavigationWidget
{
Q_OBJECT

public slots:
    void addDocumentationData(bool finished);

public:
    NavigationWidget(KDevelop::DeclarationPointer declaration, KDevelop::TopDUContextPointer topContext, const QString& htmlPrefix = QString(), const QString& htmlSuffix = QString());
    NavigationWidget(const KDevelop::IncludeItem& includeItem, KDevelop::TopDUContextPointer topContext, const QString& htmlPrefix = QString(), const QString& htmlSuffix = QString());
    
    static QString shortDescription(KDevelop::Declaration* /*declaration*/) { return "<b>Test</b>"; };
    static QString shortDescription(const KDevelop::IncludeItem& /*includeItem*/) { return "<b>Test</b>"; };
    
    QWebView* m_documentationWebView;
    QString m_originalHtml;
    QString m_fullyQualifiedModuleIdentifier;
};

}

#endif // NAVIGATIONWIDGET_H