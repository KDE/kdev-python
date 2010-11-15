#include "navigationwidget.h"
#include "declarationnavigationcontext.h"

namespace Python {

NavigationWidget::NavigationWidget(KDevelop::DeclarationPointer declaration, KDevelop::TopDUContextPointer topContext, const QString& htmlPrefix, const QString& htmlSuffix)
{
    kDebug() << "Navigation widget for Declaration requested";
    m_topContext = topContext;
    
    initBrowser(400);
    
    m_startContext = new DeclarationNavigationContext(declaration, m_topContext);
    setContext(m_startContext);
}

NavigationWidget::NavigationWidget(const KDevelop::IncludeItem& includeItem, KDevelop::TopDUContextPointer topContext, const QString& htmlPrefix, const QString& htmlSuffix)
{

}

}