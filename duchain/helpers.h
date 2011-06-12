#ifndef GLOBALHELPERS_H
#define GLOBALHELPERS_H

#include <QList>
#include <KUrl>
#include <interfaces/iproject.h>
#include <KDebug>
#include <language/editor/simplerange.h>

#include "pythonduchainexport.h"

using namespace KDevelop;

namespace Python {

class KDEVPYTHONDUCHAIN_EXPORT Helper {
public:
    static QList<KUrl> getSearchPaths(KUrl workingOnDocument);
    static QList<KUrl> cachedSearchPaths;
};

}

#endif