#ifndef GLOBALHELPERS_H
#define GLOBALHELPERS_H

#include <QList>
#include <KUrl>
#include <KDebug>

#include <interfaces/iproject.h>
#include <language/duchain/declaration.h>
#include <language/duchain/types/unsuretype.h>
#include <language/editor/simplerange.h>
#include <language/duchain/topducontext.h>
#include <language/duchain/types/structuretype.h>
#include <language/duchain/functiondeclaration.h>
#include <duchain/declarations/decorator.h>

#include "pythonduchainexport.h"
#include "types/unsuretype.h"
#include "ast.h"

using namespace KDevelop;

namespace Python {

class KDEVPYTHONDUCHAIN_EXPORT Helper {
public:
    /** get search paths for python files **/
    static QList<KUrl> getSearchPaths(KUrl workingOnDocument);
    static QString dataDir;
    static QString documentationFile;
    
    static QString getDataDir();
    static QString getDocumentationFile();
    static ReferencedTopDUContext getDocumentationFileContext();
    
    static QList<KUrl> cachedSearchPaths;
    
    static UnsureType::Ptr extractTypeHints(AbstractType::Ptr type, TopDUContext* current);
    
    static AbstractType::Ptr resolveType(AbstractType::Ptr type);
    
    /**
     * @brief Finds whether the specified called declaration is a function declaration, and, if not, checks for a class declaration; then returns the constructor
     *
     * @param ptr the declaration to check
     * @return the function pointer which was found, or an invalid pointer
     **/
    static QPair<FunctionDeclarationPointer, bool> functionDeclarationForCalledDeclaration(DeclarationPointer ptr);
    
    template<typename T> static const Decorator* findDecoratorByName(T* inDeclaration, const QString& name) {
        register int count = inDeclaration->decoratorsSize();
        for ( int i = 0; i < count; i++ ) {
            if ( inDeclaration->decorators()[i].name() == name )
                return &(inDeclaration->decorators()[i]);
        }
        return 0;
    };
    
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
    static AbstractType::Ptr mergeTypes(AbstractType::Ptr type, AbstractType::Ptr newType, TopDUContext* ctx = 0);
    
    /** check whether the argument is a null, mixed, or none integral type **/
    static bool isUsefulType(AbstractType::Ptr type);
    
    /**
    * @brief Find all internal contexts for this class and its base classes recursively
    *
    * @param klass Type object for the class to search contexts
    * @param context TopContext for finding the declarations for types
    * @return list of contexts which were found
    **/
    static QList<DUContext*> internalContextsForClass(KDevelop::StructureType::Ptr klassType, TopDUContext* context, int depth = 0);
    
    /**
        * @brief Resolve the given declaration if it is an alias declaration.
        *
        * @param decl the declaration to resolve
        * @return :Declaration* decl if not an alias declaration, decl->aliasedDeclaration().data otherwise
        * DUChain must be read locked
        **/
    static Declaration* resolveAliasDeclaration(Declaration* decl);
    
    static Declaration* declarationForName(NameAst* ast, const QualifiedIdentifier& identifier, const RangeInRevision& nodeRange, DUContextPointer context);
};

}

#endif