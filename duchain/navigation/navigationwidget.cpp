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

namespace Python {

NavigationWidget::NavigationWidget(KDevelop::DeclarationPointer declaration, KDevelop::TopDUContextPointer topContext, const QString& /* htmlPrefix */, const QString& /* htmlSuffix */)
{
    kDebug() << "Navigation widget for Declaration requested";
    m_topContext = topContext;
    
    initBrowser(400);
    
    DeclarationNavigationContext* context = new DeclarationNavigationContext(declaration, m_topContext);
    m_startContext = context;
    setContext(m_startContext);
    
    m_fullyQualifiedModuleIdentifier = context->m_fullyQualifiedModuleIdentifier;
    kDebug() << "Identifier: " << m_fullyQualifiedModuleIdentifier;
    if ( m_fullyQualifiedModuleIdentifier.length() ) {
        m_documentationWebView = new QWebView(this);
        m_documentationWebView->load(QUrl("http://localhost:1050/" + m_fullyQualifiedModuleIdentifier + ".html"));
        connect( m_documentationWebView, SIGNAL(loadFinished(bool)), SLOT(addDocumentationData(bool)) );
    }
}

void NavigationWidget::addDocumentationData(bool finished)
{
    kDebug() << "Done loading!";
    disconnect(m_documentationWebView, SIGNAL(loadFinished(bool)));
    if ( finished ) {
        QGridLayout* newLayout = new QGridLayout();
        newLayout->setRowMinimumHeight(0, 200);
        newLayout->setColumnMinimumWidth(0, 500);
        newLayout->addWidget(m_documentationWebView);
        layout()->addItem(newLayout);
    }
    else {
        kError() << "Failed to get documentation for " << m_fullyQualifiedModuleIdentifier;
    }
//     QWebElement document = m_documentationWebView->page()->mainFrame()->documentElement();
//     if ( ! document.isNull() ) {
//         kDebug() << " >>> Trying to append documentation... ";
//         kDebug() << document.findFirst("body").tagName();
//         document.findFirst("body").findFirst("div").replace(m_originalHtml);
//     }
//     else {
//         kError() << " !!! Could not append documentation to HTML page received!";
//     }
}

NavigationWidget::NavigationWidget(const KDevelop::IncludeItem& /* includeItem */, KDevelop::TopDUContextPointer /*topContext*/, const QString& /*htmlPrefix*/, const QString& /*htmlSuffix*/)
{

}

}

#include "navigationwidget.moc"