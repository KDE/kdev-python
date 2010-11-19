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
    
    static QString shortDescription(KDevelop::Declaration* declaration) { return "<b>Test</b>"; };
    static QString shortDescription(const KDevelop::IncludeItem& includeItem) { return "<b>Test</b>"; };
    
    QWebView* m_documentationWebView;
};

}

#endif // NAVIGATIONWIDGET_H