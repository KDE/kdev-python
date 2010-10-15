#ifndef NAVIGATIONWIDGET_H
#define NAVIGATIONWIDGET_H

#include <language/duchain/navigation/abstractnavigationwidget.h>
#include "pythonduchainexport.h"
#include <language/util/includeitem.h>

class KDEVPYTHONDUCHAIN_EXPORT NavigationWidget : public KDevelop::AbstractNavigationWidget
{
Q_OBJECT
public:
    NavigationWidget();
    NavigationWidget(KDevelop::DeclarationPointer declaration, KDevelop::TopDUContextPointer topContext, const QString& htmlPrefix = QString(), const QString& htmlSuffix = QString());
    NavigationWidget(const KDevelop::IncludeItem& includeItem, KDevelop::TopDUContextPointer topContext);
    
    static QString shortDescription(KDevelop::Declaration* declaration) { return "<b>Test</b>"; };
    static QString shortDescription(const KDevelop::IncludeItem& includeItem) { return "<b>Test</b>"; };
};

#endif // NAVIGATIONWIDGET_H
