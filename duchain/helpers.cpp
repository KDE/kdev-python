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

using namespace KDevelop;

namespace Python {

QList<KUrl> Helper::cachedSearchPaths;
    
QList<KUrl> Helper::getSearchPaths(KUrl workingOnDocument)
{
    QList<KUrl> searchPaths;
    // search in the projects, as they're packages and likely to be installed or added to PYTHONPATH later
    foreach  (IProject* project, ICore::self()->projectController()->projects() ) {
        searchPaths.append(KUrl(project->folder().url()));
    }
    
    KStandardDirs d;
    searchPaths.append(KUrl(d.findDirs("data", "kdevpythonsupport/documentation_files").first()));
    
    if ( cachedSearchPaths.isEmpty() ) {
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

UnsureType::Ptr Helper::mergeTypes(AbstractType::Ptr type, AbstractType::Ptr newType)
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
        unsure->addType(newType->indexed());
        ret = unsure;
    }
    else if ( newUnsure ) {
        AbstractType::Ptr createdType = AbstractType::Ptr(newUnsure->clone());
        UnsureType::Ptr createdUnsureType = UnsureType::Ptr::dynamicCast(newType);
        createdUnsureType->addType(type->indexed());
        ret = createdUnsureType;
    }
    else {
        unsure = UnsureType::Ptr(new UnsureType());
        unsure->addType(newType->indexed());
        unsure->addType(type->indexed());
        ret = unsure;
    }
    return ret;
}

}
