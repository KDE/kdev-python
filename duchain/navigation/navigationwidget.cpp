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

NavigationWidget::NavigationWidget(KDevelop::DeclarationPointer declaration, KDevelop::TopDUContextPointer topContext, const QString& htmlPrefix, const QString& htmlSuffix)
{
    kDebug() << "Navigation widget for Declaration requested";
    m_topContext = topContext;
    
    m_startContext = new DeclarationNavigationContext(declaration, m_topContext);
    setContext(m_startContext);
    
    m_originalHtml = m_startContext->html();
    
    m_documentationWebView = new QWebView(this);
    m_documentationWebView->load(QUrl("http://localhost:1050/"));
    connect( m_documentationWebView, SIGNAL(loadFinished(bool)), SLOT(addDocumentationData(bool)) );
    
    QGridLayout* newLayout = new QGridLayout();
    newLayout->setRowMinimumHeight(0, 300);
    newLayout->setColumnMinimumWidth(0, 400);
    newLayout->addWidget(m_documentationWebView);
    layout()->addItem(newLayout);
    
    initBrowser(400);
}

void NavigationWidget::addDocumentationData(bool finished)
{
    kDebug() << "Done loading!";
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

NavigationWidget::NavigationWidget(const KDevelop::IncludeItem& includeItem, KDevelop::TopDUContextPointer topContext, const QString& htmlPrefix, const QString& htmlSuffix)
{

}

}

#include "navigationwidget.moc"