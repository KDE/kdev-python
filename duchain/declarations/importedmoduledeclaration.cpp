#include "importedmoduledeclaration.h"
#include "parser/parserConfig.h"
#include <QProcess>

namespace Python {

QString importedModuleDeclaration::generateDocumentationForModule()
{
    QProcess* parser = new QProcess();
    parser->start("/usr/bin/env", QStringList() << "python" << QString(INSTALL_PATH) + QString("/pydoc.py") << QString("-w") << QString(m_moduleIdentifier));
    parser->waitForFinished();
    kDebug() << " ** Reading results...";
    
    // TODO this is not clean
    if ( parser->exitStatus() != QProcess::NormalExit ) {
        kError() << "Error parsing file: " << parser->errorString();
        return "0";
    }
    
    QString result = parser->readAllStandardOutput();
    
    return result;
}
    
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

