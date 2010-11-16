#include "importedmoduledeclaration.h"

namespace Python {

importedModuleDeclaration::importedModuleDeclaration(DeclarationData& dd): Declaration(dd)
{

}

importedModuleDeclaration::importedModuleDeclaration(const KDevelop::RangeInRevision& range, DUContext* parentContext): Declaration(range, parentContext)
{

}

importedModuleDeclaration::importedModuleDeclaration(const KDevelop::Declaration& rhs): Declaration(rhs)
{

}

importedModuleDeclaration::importedModuleDeclaration(DeclarationData& dd, const KDevelop::RangeInRevision& range): Declaration(dd, range)
{

}

}

