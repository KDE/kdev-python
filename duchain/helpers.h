#ifndef GLOBALHELPERS_H
#define GLOBALHELPERS_H

#include <interfaces/iproject.h>
#include <language/duchain/types/unsuretype.h>
#include <language/editor/simplerange.h>
#include <language/duchain/topducontext.h>
#include <language/duchain/types/structuretype.h>

#include <QList>
#include <KUrl>
#include <KDebug>

#include "pythonduchainexport.h"

using namespace KDevelop;

namespace Python {

class KDEVPYTHONDUCHAIN_EXPORT Helper {
public:
    /** get search paths for python files **/
    static QList<KUrl> getSearchPaths(KUrl workingOnDocument);
    
    static QList<KUrl> cachedSearchPaths;
    
    /**
     * @brief merge two types into one unsure type
     *
     * @param type old type
     * @param newType new type
     * @return :AbstractType::Ptr the merged type, always valid
     * 
     * @warning Although this looks symmetrical, it is NOT: the first argument might be modified, the second one won't be.
     * So if you do something like a = mergeTypes(a, b) make sure you pass "a" as first argument.
     **/
    static AbstractType::Ptr mergeTypes(AbstractType::Ptr type, AbstractType::Ptr newType);
    
    /** check whether the argument is a null, mixed, or none integral type **/
    static bool isUsefulType(AbstractType::Ptr type);
    
    /**
    * @brief Find all internal contexts for this class and its base classes recursively
    *
    * @param klass Type object for the class to search contexts
    * @param context TopContext for finding the declarations for types
    * @return list of contexts which were found
    **/
    static QList<DUContext*> inernalContextsForClass(KDevelop::StructureType::Ptr klassType, TopDUContext* context);
};

}

#endif