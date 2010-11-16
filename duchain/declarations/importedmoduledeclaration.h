#ifndef IMPORTEDMODULEDECLARATION_H
#define IMPORTEDMODULEDECLARATION_H
#include <language/duchain/declaration.h>
#include "pythonduchainexport.h"

using namespace KDevelop;

namespace Python {

class KDEVPYTHONDUCHAIN_EXPORT importedModuleDeclaration : public Declaration
{

public:
    importedModuleDeclaration(DeclarationData& dd);
    importedModuleDeclaration(const KDevelop::RangeInRevision& range, DUContext* parentContext);
    importedModuleDeclaration(DeclarationData& dd, const KDevelop::RangeInRevision& range);
    importedModuleDeclaration(const KDevelop::Declaration& rhs);
    QString m_moduleIdentifier;
    QString generateDocumentationForModule();
};

}

#endif // IMPORTEDMODULEDECLARATION_H
