#include "helpers.h"

#include <QList>
#include <KUrl>
#include <interfaces/iproject.h>
#include <interfaces/icore.h>
#include <interfaces/iprojectcontroller.h>
#include <KDebug>
#include <KStandardDirs>
#include <QProcess>
#include <language/duchain/types/unsuretype.h>
#include <language/duchain/types/integraltype.h>
#include <language/duchain/duchainlock.h>
#include <language/duchain/duchain.h>
#include <language/duchain/classdeclaration.h>
#include <language/duchain/aliasdeclaration.h>
#include <ast.h>

using namespace KDevelop;

namespace Python {

QList<KUrl> Helper::cachedSearchPaths;
QString Helper::dataDir = QString::null;
QString Helper::documentationFile = QString::null;

Declaration* Helper::declarationForName(NameAst* ast, const QualifiedIdentifier& identifier, const RangeInRevision& nodeRange, DUContextPointer context)
{
    QList<Declaration*> declarations;
    QList<Declaration*> localDeclarations;
    QList<Declaration*> importedLocalDeclarations;
    {
        DUChainReadLocker lock(DUChain::lock());
        declarations = context->topContext()->findDeclarations(identifier, CursorInRevision::invalid());
        localDeclarations = context->findLocalDeclarations(identifier.last(), nodeRange.end);
        importedLocalDeclarations = context->findDeclarations(identifier.last(), nodeRange.end);
    }
    Declaration* declaration;
    if ( localDeclarations.length() ) {
        declaration = localDeclarations.last();
        kDebug() << "Using local declaration";
    }
    else if ( importedLocalDeclarations.length() ) {
        declaration = importedLocalDeclarations.last();
        kDebug() << "Using imported local declaration (i.e., argument)";
    }
    else if ( declarations.length() ) {
        declaration = declarations.last();
        kDebug() << "Using global declaration";
    }
    else declaration = 0;
    return declaration;
}

QList< DUContext* > Helper::inernalContextsForClass(StructureType::Ptr klassType, TopDUContext* context, int depth)
{
    QList<DUContext*> searchContexts;
    if ( ! klassType ) {
        return searchContexts;
    }
    searchContexts << klassType->internalContext(context);
    Declaration* decl = klassType->declaration(context);
    ClassDeclaration* klass = dynamic_cast<ClassDeclaration*>(decl);
    kDebug() << "Got class Declaration:" << klass;
    if ( klass ) {
        kDebug() << "Base classes: " << klass->baseClassesSize();
        FOREACH_FUNCTION ( const BaseClassInstance& base, klass->baseClasses ) {
            StructureType::Ptr baseClassType = base.baseClass.type<StructureType>();
            kDebug() << "Base class type: " << baseClassType;
            // recursive call, because the base class will have more base classes eventually
            if ( depth < 10 ) {
                searchContexts.append(Helper::inernalContextsForClass(baseClassType, context, depth + 1));
            }
        }
    }
    return searchContexts;
}

Declaration* Helper::resolveAliasDeclaration(Declaration* decl)
{
    AliasDeclaration* alias = dynamic_cast<AliasDeclaration*>(decl);
    if ( alias ) {
        return alias->aliasedDeclaration().data();
    }
    else
        return decl;
}

QString Helper::getDataDir() {
    if ( Helper::dataDir.isNull() ) {
        KStandardDirs d;
        Helper::dataDir = d.findDirs("data", "kdevpythonsupport/documentation_files").first();
    }
    return Helper::dataDir;
}

QString Helper::getDocumentationFile() {
    if ( Helper::documentationFile.isNull() ) {
        Helper::documentationFile = KStandardDirs::locate("data", "kdevpythonsupport/documentation_files/builtindocumentation.py");
    }
    return Helper::documentationFile;
}
    
QList<KUrl> Helper::getSearchPaths(KUrl workingOnDocument)
{
    QList<KUrl> searchPaths;
    // search in the projects, as they're packages and likely to be installed or added to PYTHONPATH later
    foreach  (IProject* project, ICore::self()->projectController()->projects() ) {
        searchPaths.append(KUrl(project->folder().url()));
    }
    
    searchPaths.append(KUrl(getDataDir()));
    
    if ( cachedSearchPaths.isEmpty() ) {
        KStandardDirs d;
        kDebug() << "*** Gathering search paths...";
        QStringList getpath;
        getpath << "python" << "-c" << "import sys; sys.stdout.write(':'.join(sys.path))";
        
        QProcess python;
        python.start("/usr/bin/env", getpath);
        python.waitForFinished(1000);
        QByteArray pythonpath = python.readAllStandardOutput();
        QList<QByteArray> paths = pythonpath.split(':');
        paths.removeAll("");
        
        if ( ! pythonpath.isEmpty() ) {
            foreach ( const QString& path, paths ) {
                cachedSearchPaths.append(path);
            }
        }
        else {
            kWarning() << "Could not get search paths! Defaulting to stupid stuff.";
            searchPaths.append(KUrl("/usr/lib/python2.7"));
            searchPaths.append(KUrl("/usr/lib/python2.7/site-packages"));
            QString path = getenv("PYTHONPATH");
            QStringList paths = path.split(':');
            foreach ( const QString& path, paths ) {
                cachedSearchPaths.append(path);
            }
        }
        kDebug() << " *** Done. Got search paths: " << cachedSearchPaths;
    }
    else {
        kDebug() << " --- Search paths from cache: " << cachedSearchPaths;
    }
    
    searchPaths.append(cachedSearchPaths);
    
    // search in the current packages
    searchPaths.append(KUrl(workingOnDocument.directory()));
    
    kDebug() << "Search paths: " << searchPaths;
    kDebug() << workingOnDocument;
    return searchPaths;
}

bool Helper::isUsefulType(AbstractType::Ptr type)
{
    if ( ! type ) {
        return false;
    }
    QList<uint> skipTypes;
    skipTypes << IntegralType::TypeMixed << IntegralType::TypeNone << IntegralType::TypeNull;
    if ( type->whichType() != AbstractType::TypeIntegral ) {
        return true;
    }
    if ( ! skipTypes.contains(type.cast<IntegralType>()->dataType()) ) {
        return true;
    }
    return false;
}

AbstractType::Ptr Helper::mergeTypes(AbstractType::Ptr type, AbstractType::Ptr newType)
{
    UnsureType::Ptr unsure = UnsureType::Ptr::dynamicCast(type);
    UnsureType::Ptr newUnsure = UnsureType::Ptr::dynamicCast(newType);
    UnsureType::Ptr ret;
    // both types are unsure, so join the list of possible types.
    if ( unsure && newUnsure ) {
        int len = newUnsure->typesSize();
        for ( int i = 0; i < len; i++ ) {
            unsure->addType(newUnsure->types()[i]);
        }
        ret = unsure;
    }
    // one of them is unsure, use that and add the other one
    else if ( unsure ) {
        if ( isUsefulType(newType) ) {
            unsure->addType(newType->indexed());
        }
        ret = unsure;
    }
    else if ( newUnsure ) {
        AbstractType::Ptr createdType = AbstractType::Ptr(newUnsure->clone());
        UnsureType::Ptr createdUnsureType = UnsureType::Ptr::dynamicCast(newType);
        if ( isUsefulType(type) ) {
            createdUnsureType->addType(type->indexed());
        }
        ret = createdUnsureType;
    }
    else {
        unsure = UnsureType::Ptr(new UnsureType());
        if ( isUsefulType(newType) ) {
            unsure->addType(newType->indexed());
        }
        if ( isUsefulType(type) ) {
            unsure->addType(type->indexed());
        }
        if ( ! unsure.count() ) {
            return AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed));
        }
        ret = unsure;
    }
#warning remove me: lock
    DUChainReadLocker lock(DUChain::lock());
    if ( ret->typesSize() == 1 && ret->types()[0].abstractType() ) {
        kDebug() << "Returning merged type:" << ret->types()[0].abstractType()->toString();
        return ret->types()[0].abstractType();
    }
    kDebug() << "Returning real merged type:" << ret->toString();
    return AbstractType::Ptr::staticCast(ret);
}

}
