
#include <language/codecompletion/normaldeclarationcompletionitem.h>
#include <language/duchain/declaration.h>
#include <language/duchain/functiondeclaration.h>

#include <KTextEditor/View>
#include <KTextEditor/Document>

#include "functiondeclarationcompletionitem.h"
#include "navigation/navigationwidget.h"

using namespace KDevelop;
using namespace KTextEditor;

namespace Python {

FunctionDeclarationCompletionItem::FunctionDeclarationCompletionItem(DeclarationPointer decl) : NormalDeclarationCompletionItem(decl) { }

void FunctionDeclarationCompletionItem::executed(KTextEditor::Document* document, const KTextEditor::Range& word)
{
    kDebug() << "FunctionDeclarationCompletionItem executed";
    DUChainPointer<FunctionDeclaration> decl = declaration().dynamicCast<FunctionDeclaration>();
    if ( ! decl.data() ) {
        kError() << "ERROR: could not get declaration data, not executing completion item!";
        return;
    }
    kDebug() << "declaration data: " << decl.data();
    const QString suffix = "()";
    int skip = 2; // place cursor behind bracktes
    if ( decl.data()->defaultParametersSize() != 0 ) {
        skip = 1; // place cursor in brackets if there's parameters
    }
    document->replaceText(word, decl.data()->identifier().toString() + suffix);
    if ( View* view = document->activeView() ) {
        view->setCursorPosition( Cursor(word.end().line(), word.end().column() + skip) );
    }
}

FunctionDeclarationCompletionItem::~FunctionDeclarationCompletionItem() { }

}