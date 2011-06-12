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
    static QList<KUrl> getSearchPaths(KUrl workingOnDocument);
    static QList<KUrl> cachedSearchPaths;
    static UnsureType::Ptr mergeTypes(AbstractType::Ptr type, AbstractType::Ptr newType);
};

}

#endif