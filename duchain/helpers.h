/*****************************************************************************
 * This file is part of KDevelop                                             *
 * Copyright 2011-2012 Sven Brauch <svenbrauch@googlemail.com>               *
 *                                                                           *
 * This program is free software; you can redistribute it and/or             *
 * modify it under the terms of the GNU General Public License as            *
 * published by the Free Software Foundation; either version 2 of            *
 * the License, or (at your option) any later version.                       *
 *                                                                           *
 * This program is distributed in the hope that it will be useful,           *
 * but WITHOUT ANY WARRANTY; without even the implied warranty of            *
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             *
 * GNU General Public License for more details.                              *
 *                                                                           *
 * You should have received a copy of the GNU General Public License         *
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.     *
 *****************************************************************************
 */

#ifndef GLOBALHELPERS_H
#define GLOBALHELPERS_H

#include "declarations/classdeclaration.h"
#include "pythonduchainexport.h"
#include "types/unsuretype.h"
#include "ast.h"
#include "expressionvisitor.h"

#include <interfaces/iproject.h>
#include <language/duchain/declaration.h>
#include <language/duchain/types/unsuretype.h>
#include <language/editor/simplerange.h>
#include <language/duchain/topducontext.h>
#include <language/duchain/types/structuretype.h>
#include <language/duchain/functiondeclaration.h>
#include <duchain/declarations/decorator.h>

#include <QList>
#include <KUrl>
#include <KDebug>

using namespace KDevelop;

namespace Python {

class KDEVPYTHONDUCHAIN_EXPORT Helper {
public:
    /** get search paths for python files **/
    static QList<KUrl> getSearchPaths(KUrl workingOnDocument);
    static QStringList dataDirs;
    static QString documentationFile;
    static DUChainPointer<TopDUContext> documentationFileContext;
    
    static QStringList getDataDirs();
    static QString getDocumentationFile();
    static ReferencedTopDUContext getDocumentationFileContext();
    
    static QList<KUrl> cachedSearchPaths;
    
    static AbstractType::Ptr extractTypeHints(AbstractType::Ptr type, TopDUContext* current);
    
    static AbstractType::Ptr resolveType(AbstractType::Ptr type);

    static Declaration* accessAttribute(Declaration* accessed, const QString& attribute, DUContext* current);
    
    /**
     * @brief Finds whether the specified called declaration is a function declaration, and, if not, checks for a class declaration; then returns the constructor
     *
     * @param ptr the declaration to check
     * @return the function pointer which was found, or an invalid pointer
     **/
    static QPair<FunctionDeclarationPointer, bool> functionDeclarationForCalledDeclaration(DeclarationPointer ptr);
    
    template<typename T> static const Decorator* findDecoratorByName(T* inDeclaration, const QString& name) {
        register int count = inDeclaration->decoratorsSize();
        const IndexedString indexedName = IndexedString(name);
        for ( int i = 0; i < count; i++ ) {
            if ( inDeclaration->decorators()[i].fastName() == indexedName )
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
    
    enum ContextSearchFlags {
        NoFlags,
        PublicOnly
    };
    
    /**
    * @brief Find all internal contexts for this class and its base classes recursively
    *
    * @param klass Type object for the class to search contexts
    * @param context TopContext for finding the declarations for types
    * @return list of contexts which were found
    **/
    static QList<DUContext*> internalContextsForClass(KDevelop::StructureType::Ptr klassType,
                                                      TopDUContext* context, ContextSearchFlags flags = NoFlags, int depth = 0);
    /**
        * @brief Resolve the given declaration if it is an alias declaration.
        *
        * @param decl the declaration to resolve
        * @return :Declaration* decl if not an alias declaration, decl->aliasedDeclaration().data otherwise
        * DUChain must be read locked
        **/
    static Declaration* resolveAliasDeclaration(Declaration* decl);
    
    static Declaration* declarationForName(NameAst* ast, const QualifiedIdentifier& identifier,
                                           const RangeInRevision& nodeRange, DUContextPointer context);
};

}

#endif