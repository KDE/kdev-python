#include "pythonducontext.h"

#include <language/duchain/topducontext.h>
#include <language/duchain/topducontextdata.h>
#include <language/duchain/duchainregister.h>
#include <language/duchain/duchainpointer.h>

#include "navigation/navigationwidget.h"

using namespace KDevelop;

namespace Python {

REGISTER_DUCHAIN_ITEM_WITH_DATA(PythonTopDUContext, TopDUContextData);

REGISTER_DUCHAIN_ITEM_WITH_DATA(PythonNormalDUContext, DUContextData);

template<>
QWidget* PythonTopDUContext::createNavigationWidget(Declaration* decl, TopDUContext* topContext, const QString& htmlPrefix, const QString& htmlSuffix) const {
    if ( ! decl ) return 0;
    return new NavigationWidget(DeclarationPointer(decl), TopDUContextPointer(topContext), htmlPrefix, htmlSuffix);
}

template<>
QWidget* PythonNormalDUContext::createNavigationWidget(Declaration* decl, TopDUContext* topContext, const QString& htmlPrefix, const QString& htmlSuffix) const {
    if ( ! decl ) return 0;
    return new NavigationWidget(DeclarationPointer(decl), TopDUContextPointer(topContext), htmlPrefix, htmlSuffix);
}

}
