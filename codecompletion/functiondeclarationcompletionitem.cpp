
#include <language/codecompletion/normaldeclarationcompletionitem.h>
#include <language/duchain/declaration.h>
#include <language/duchain/functiondeclaration.h>
#include <ktexteditor/document.h>

#include "functiondeclarationcompletionitem.h"
#include "navigation/navigationwidget.h"

using namespace KDevelop;

namespace Python {

FunctionDeclarationCompletionItem::FunctionDeclarationCompletionItem(DeclarationPointer decl) : NormalDeclarationCompletionItem(decl) { }

void FunctionDeclarationCompletionItem::executed(KTextEditor::Document* document, const KTextEditor::Range& word)
{
    kDebug() << "FunctionDeclarationCompletionItem executed";
    DUChainPointer<FunctionDeclaration> decl = declaration().dynamicCast<FunctionDeclaration>();
    Q_ASSERT(decl.data());
    kDebug() << "declaration data: " << decl.data();
    const QString suffix = "()";
    document->replaceText(word, decl.data()->identifier().toString() + suffix);
}

FunctionDeclarationCompletionItem::~FunctionDeclarationCompletionItem() { }

}