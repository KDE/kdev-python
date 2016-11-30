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

#include <interfaces/iproject.h>
#include <language/duchain/declaration.h>
#include <language/duchain/types/unsuretype.h>
#include <language/duchain/topducontext.h>
#include <language/duchain/types/structuretype.h>
#include <language/duchain/types/integraltype.h>
#include <language/duchain/functiondeclaration.h>
#include <duchain/declarations/decorator.h>

#include <QList>

#include <functional>

#include "pythonduchainexport.h"
#include "types/unsuretype.h"
#include "declarations/functiondeclaration.h"
#include "ast.h"

using namespace KDevelop;

namespace Python {

class KDEVPYTHONDUCHAIN_EXPORT Helper {
public:
    /** get search paths for python files **/
    static QVector<QUrl> getSearchPaths(const QUrl& workingOnDocument);
    static QStringList dataDirs;
    static QString documentationFile;
    static QStringList correctionFileDirs;
    static QString localCorrectionFileDir;
    static DUChainPointer<TopDUContext> documentationFileContext;

    static QStringList getDataDirs();
    static QString getDocumentationFile();
    static ReferencedTopDUContext getDocumentationFileContext();

    static QUrl getCorrectionFile(const QUrl& document);
    static QUrl getLocalCorrectionFile(const QUrl& document);

    static QMutex cacheMutex;
    static QMap<IProject*, QVector<QUrl>> cachedCustomIncludes;
    static QMap<IProject*, QVector<QUrl>> cachedSearchPaths;

    static QMutex projectPathLock;
    static QVector<QUrl> projectSearchPaths;

    static AbstractType::Ptr extractTypeHints(AbstractType::Ptr type);

    /**
     * @brief Get the declaration of 'accessed.attribute', or return null.
     *
     * @param accessed Type (Structure or Unsure) that should have this attribute.
     * @param attribute Which attribute to look for.
     * @param topContext Top context (for this file?)
     * @return Declaration* of the attribute, or null.
     *  If UnsureType with >1 matching attributes, returns an arbitrary choice.
     **/
    static KDevelop::Declaration* accessAttribute(const KDevelop::AbstractType::Ptr accessed,
                                                  const KDevelop::IndexedIdentifier& attribute,
                                                  const KDevelop::TopDUContext* topContext);

    static KDevelop::Declaration* accessAttribute(const KDevelop::AbstractType::Ptr accessed,
        const QString& attribute, const KDevelop::TopDUContext* topContext) {
        return accessAttribute(accessed, IndexedIdentifier(KDevelop::Identifier(attribute)), topContext);
    }

    static AbstractType::Ptr resolveAliasType(const AbstractType::Ptr eventualAlias);

    /**
     * @brief Get the content type(s) of something that is an iterable.
     *
     * @param iterable Type to get the contents of. Can be an unsure.
     * @return KDevelop::AbstractType::Ptr Content type. Might be an unsure.
     */
    static AbstractType::Ptr contentOfIterable(const AbstractType::Ptr iterable, const TopDUContext* topContext);

    /**
     * @brief Get a list of types inside the passed type which match the specified filter.
     * The filter will be matched against the type only if it is not an unsure type,
     * or else against all types inside that unsure type.
     * @param type The type to search
     * @param accept Filter function, return true if you want the type.
     * @return QList< KDevelop::AbstractType::Ptr > list of types accepted by the filter.
     */
    template <typename T>
    static QList<typename T::Ptr> filterType(AbstractType::Ptr type, std::function<bool(AbstractType::Ptr)> accept,
                                             std::function<typename T::Ptr(AbstractType::Ptr)> map =
                                             std::function<typename T::Ptr(AbstractType::Ptr)>())
    {
        QList<typename T::Ptr> types;
        if ( ! type ) {
            return types;
        }
        if ( type->whichType() == KDevelop::AbstractType::TypeUnsure ) {
            UnsureType::Ptr unsure(type.cast<UnsureType>());
            for ( unsigned int i = 0; i < unsure->typesSize(); i++ ) {
                AbstractType::Ptr t = unsure->types()[i].abstractType();
                if ( accept(t) ) {
                    types << ( map ? map(t) : t.cast<T>() );
                }
            }
        }
        else if ( accept(type) ) {
            types << ( map ? map(type) : type.cast<T>() );
        }
        return types;
    }

    static void scheduleDependency(const IndexedString& dependency, int betterThanPriority);

    static KDevelop::IndexedDeclaration declarationUnderCursor(bool allowUse = true);

    struct FuncInfo { FunctionDeclaration* declaration; bool isConstructor; };
    /**
     * @brief Finds whether the specified called declaration is a function declaration, and if not,
     *        checks for a class declaration; then returns the constructor
     *
     * @param called the declaration to check
     * @param isAlias whether the called declaration aliases a class or function definition.
     * @return the function pointer which was found, or an invalid pointer, and a bool
     *         which is true when it is a constructor
     **/
    static FuncInfo functionForCalled(Declaration* called, bool isAlias=true);

    template<typename T> static const Decorator* findDecoratorByName(T* inDeclaration, const QString& name) {
        const int count = inDeclaration->decoratorsSize();
        const IndexedString indexedName = IndexedString(name);
        for ( int i = 0; i < count; i++ ) {
            if ( inDeclaration->decorators()[i].fastName() == indexedName )
                return &(inDeclaration->decorators()[i]);
        }
        return 0;
    };

    static bool docstringContainsHint(const QString& comment, const QString& hintName, QStringList* args = 0) {
        // TODO cache types! this is horribly inefficient
        const QString search = "! " + hintName + " !";
        int index = comment.indexOf(search);
        if ( index >= 0 ) {
            if ( args ) {
                int eol = comment.indexOf('\n', index);
                int start = index+search.size()+1;
                QString decl = comment.mid(start, eol-start);
                *args = decl.split(' ');
            }
            return true;
        }
        return false;
    }

    /**
     * @copydoc TypeUtils::mergeTypes
     */
    static AbstractType::Ptr mergeTypes(AbstractType::Ptr type, const AbstractType::Ptr newType);

    /**
     * @brief Like mergeTypes(), but merges a list of types into a newly allocated type.
     * Returns mixed if the list is empty.
     * @return KDevelop::AbstractType::Ptr an unsure type consisting of all types in the list.
     */
    template <typename T>
    static AbstractType::Ptr foldTypes(QList<T> types, std::function<AbstractType::Ptr(const T&)> transform
                                                     = std::function<AbstractType::Ptr(const T&)>())
    {
        AbstractType::Ptr result(new IntegralType(IntegralType::TypeMixed));
        for ( T type : types ) {
            result = Helper::mergeTypes(result, transform ? transform(type) : AbstractType::Ptr::staticCast(type));
        }
        return result;
    };

    /** check whether the argument is a null, mixed, or none integral type **/
    static bool isUsefulType(AbstractType::Ptr type);

    enum ContextSearchFlags {
        NoFlags,
        PublicOnly
    };

    /**
    * @brief Find all internal contexts for this class and its base classes recursively
    *
    * @param classType Type object for the class to search contexts
    * @param context TopContext for finding the declarations for types
    * @return list of contexts which were found
    **/
    static QVector<DUContext*> internalContextsForClass(const KDevelop::StructureType::Ptr classType,
                                                        const TopDUContext* context,
                                                        ContextSearchFlags flags = NoFlags, int depth = 0);
    /**
      * @brief Resolve the given declaration if it is an alias declaration.
      *
      * @param decl the declaration to resolve
      * @return :Declaration* decl if not an alias declaration, decl->aliasedDeclaration().data otherwise
      * DUChain must be read locked
      **/
    static Declaration* resolveAliasDeclaration(Declaration* decl);

    static Declaration* declarationForName(const QualifiedIdentifier& identifier, const RangeInRevision& nodeRange,
                                           DUChainPointer<const DUContext> context);
};

}

#endif

