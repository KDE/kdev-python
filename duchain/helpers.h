#ifndef GLOBALHELPERS_H
#define GLOBALHELPERS_H

#include "parser/parserConfig.h"

#include <QList>
#include <KUrl>
#include <interfaces/iproject.h>
#include <KDebug>

#include "pythonduchainexport.h"

namespace Python {

class KDEVPYTHONDUCHAIN_EXPORT Helper {
public:
    static QList<KUrl> getSearchPaths(KUrl workingOnDocument);
};

}

#endif