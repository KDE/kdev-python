#include "helpers.h"

#include <QList>
#include <KUrl>
#include <interfaces/iproject.h>
#include <interfaces/icore.h>
#include <interfaces/iprojectcontroller.h>
#include <KDebug>
#include <KStandardDirs>

using namespace KDevelop;

namespace Python {
    
QList<KUrl> Helper::getSearchPaths(KUrl workingOnDocument)
{
    QList<KUrl> searchPaths;
    // search in the projects, as they're packages and likely to be installed or added to PYTHONPATH later
    foreach  (IProject* project, ICore::self()->projectController()->projects() ) {
        searchPaths.append(KUrl(project->folder().url()));
    }
    
    KStandardDirs d;
    searchPaths.append(KUrl(d.findDirs("data", "kdevpythonsupport/documentation_files").first()));
    kDebug() << "SEARCH PATHS:" << searchPaths;
    searchPaths.append(KUrl("/usr/lib/python2.7"));
    searchPaths.append(KUrl("/usr/lib/python2.7/site-packages"));
    QString path = getenv("PYTHONPATH");
    QStringList paths = path.split(':');
    foreach ( const QString& path, paths ) {
        searchPaths.append(path);
    }
    
    // search in the current packages
    searchPaths.append(KUrl(workingOnDocument.directory()));
    
    kDebug() << "Search paths: " << searchPaths;
    kDebug() << workingOnDocument;
    return searchPaths;
}

}
