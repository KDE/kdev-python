#include "navigationwidget.h"
#include <language/duchain/navigation/abstractnavigationwidget.h>
#include <language/util/includeitem.h>

NavigationWidget::NavigationWidget()
{

}

NavigationWidget::NavigationWidget(KDevelop::DeclarationPointer declaration, KDevelop::TopDUContextPointer topContext, const QString& htmlPrefix, const QString& htmlSuffix)
{
    kDebug() << "Navigation widget requested";
}

NavigationWidget::NavigationWidget(const KDevelop::IncludeItem& includeItem, KDevelop::TopDUContextPointer topContext)
{

}

#include "navigationwidget.moc"
