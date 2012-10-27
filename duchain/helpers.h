/*****************************************************************************
 * This file is part of KDevelop                                             *
 * Copyright 2011-2012 Sven Brauch <svenbrauch@googlemail.com>               *
 *                                                                           *
 * Permission is hereby granted, free of charge, to any person obtaining     *
 * a copy of this software and associated documentation files (the           *
 * "Software"), to deal in the Software without restriction, including       *
 * without limitation the rights to use, copy, modify, merge, publish,       *
 * distribute, sublicense, and/or sell copies of the Software, and to        *
 * permit persons to whom the Software is furnished to do so, subject to     *
 * the following conditions:                                                 *
 *                                                                           *
 * The above copyright notice and this permission notice shall be            *
 * included in all copies or substantial portions of the Software.           *
 *                                                                           *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,           *
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF        *
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND                     *
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE    *
 * LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION    *
 * OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION     *
 * WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.           *
 *****************************************************************************/

#ifndef GLOBALHELPERS_H
#define GLOBALHELPERS_H

#include "declarations/classdeclaration.h"
#include "pythonduchainexport.h"
#include "types/unsuretype.h"
#include "ast.h"

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

#include "pythonduchainexport.h"
#include "types/unsuretype.h"
#include "declarations/functiondeclaration.h"
#include "ast.h"

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
    
    /**
     * @brief Finds whether the specified called declaration is a function declaration, and, if not, checks for a class declaration; then returns the constructor
     *
     * @param ptr the declaration to check
     * @return the function pointer which was found, or an invalid pointer
     **/
    static QPair<FunctionDeclarationPointer, bool> functionDeclarationForCalledDeclaration(DeclarationPointer ptr);
    
    template<typename T> static const Decorator* findDecoratorByName(T* inDeclaration, const QString& name) {
        const int count = inDeclaration->decoratorsSize();
        const IndexedString indexedName = IndexedString(name);
        for ( int i = 0; i < count; i++ ) {
            if ( inDeclaration->decorators()[i].fastName() == indexedName )
                return &(inDeclaration->decorators()[i]);
        }
        return 0;
    };
    
    static bool docstringContainsHint(Declaration* declaration, const QString& hintName, QStringList* args = 0) {
        // TODO cache types! this is horribly inefficient
        const QString& comment = declaration->comment();
        kDebug() << "COMMENT:" << comment << hintName;
        int index = comment.indexOf("! " + hintName);
        if ( index >= 0 ) {
            if ( args ) {
                int eol = comment.indexOf('\n', index);
                QString decl = comment.mid(index, eol);
                *args = decl.split(' ');
                kDebug() << *args;
            }
            return true;
        }
        return false;
    }
    
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