#include "navigationwidget.h"
#include "declarationnavigationcontext.h"
#include "parser/parserConfig.h"

#include <QUrl>
#include <QObject>

#include <language/duchain/aliasdeclaration.h>

using namespace KDevelop;

namespace Python {

NavigationWidget::NavigationWidget(KDevelop::DeclarationPointer declaration, KDevelop::TopDUContextPointer topContext, const QString& /* htmlPrefix */, const QString& /* htmlSuffix */)
{
    kDebug() << "Navigation widget for Declaration requested";
    
    AliasDeclaration* alias = dynamic_cast<AliasDeclaration*>(declaration.data());
    DeclarationPointer realDeclaration;
    if ( alias ) {
        kDebug() << "is alias declaration";
        DUChainReadLocker lock(DUChain::lock());
        realDeclaration = DeclarationPointer(alias->aliasedDeclaration().declaration());
    }
    else {
        realDeclaration = declaration;
    }
    
    m_topContext = topContext;
    
    initBrowser(400);
    
    DeclarationNavigationContext* context = new DeclarationNavigationContext(realDeclaration, m_topContext);
    m_startContext = context;
    setContext(m_startContext);
}

void NavigationWidget::addDocumentationData(bool finished)
{
}

NavigationWidget::NavigationWidget(const KDevelop::IncludeItem& /* includeItem */, KDevelop::TopDUContextPointer /*topContext*/, const QString& /*htmlPrefix*/, const QString& /*htmlSuffix*/)
{

}

}

#include "navigationwidget.moc"