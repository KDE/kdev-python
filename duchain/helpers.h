#ifndef GLOBALHELPERS_H
#define GLOBALHELPERS_H

#include <interfaces/iproject.h>
#include <language/duchain/types/unsuretype.h>
#include <language/editor/simplerange.h>

#include <QList>
#include <KUrl>
#include <KDebug>

#include "pythonduchainexport.h"

using namespace KDevelop;

namespace Python {

class KDEVPYTHONDUCHAIN_EXPORT Helper {
public:
    // get search paths for python files
    static QList<KUrl> getSearchPaths(KUrl workingOnDocument);
    static QList<KUrl> cachedSearchPaths;
    // merge two types into one unsure type
    static AbstractType::Ptr mergeTypes(AbstractType::Ptr type, AbstractType::Ptr newType);
    // check whether the argument is a null, mixed, or none integral type
    static bool isUsefulType(AbstractType::Ptr type);
};

}

#endif