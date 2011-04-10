#include "helpers.h"

#include <QList>
#include <KUrl>
#include <interfaces/iproject.h>
#include <interfaces/icore.h>
#include <interfaces/iprojectcontroller.h>
#include <KDebug>

#include <pythoninterpreter.h>

using namespace KDevelop;

namespace Python {

QList<KUrl> Helper::getSearchPaths(KUrl workingOnDocument)
{
    QList<KUrl> searchPaths;
    // search in the projects, as they're packages and likely to be installed or added to PYTHONPATH later
    foreach  (IProject* project, ICore::self()->projectController()->projects() ) {
        searchPaths.append(KUrl(project->folder().url()));
    }

    kDebug() << "Python path";
    QStringList tmp = PythonInterpreter::instance()->getPythonPath();
    foreach(QString item, tmp) {
        kDebug() << item;
        searchPaths.append(KUrl(item));
    }

    searchPaths.append(KUrl(DOC_DIR));
    
    // search in the current packages
    searchPaths.append(KUrl(workingOnDocument.directory()));
    
    kDebug() << "Search paths: " << searchPaths;
    kDebug() << workingOnDocument;
    return searchPaths;
}

}
