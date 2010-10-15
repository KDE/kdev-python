#include "importfileitem.h"

namespace Python {

ImportFileItem::~ImportFileItem()
{

}

void ImportFileItem::execute(KTextEditor::Document* document, const KTextEditor::Range& word)
{
    kDebug() << "ImportFileItem executed";
}


}