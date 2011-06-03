#include "navigationwidget.h"
#include "declarationnavigationcontext.h"
#include <qlayout.h>
#include <QWebView>
#include <QUrl>
#include <QWebFrame>
#include <QWebElement>
#include <qboxlayout.h>
#include <qpushbutton.h>
#include <QObject>

#include <QtNetwork>

#include <QProcess>

#include "parser/parserConfig.h"
#include <QThread>

#include <QTimer>

namespace Python {

NavigationWidget::NavigationWidget(KDevelop::DeclarationPointer declaration, KDevelop::TopDUContextPointer topContext, const QString& /* htmlPrefix */, const QString& /* htmlSuffix */)
{
    kDebug() << "Navigation widget for Declaration requested";
    m_topContext = topContext;
    
    initBrowser(400);
    
    DeclarationNavigationContext* context = new DeclarationNavigationContext(declaration, m_topContext);
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