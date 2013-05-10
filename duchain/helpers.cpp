/*****************************************************************************
 * This file is part of KDevelop                                             *
 * Copyright 2011-2013 Sven Brauch <svenbrauch@googlemail.com>               *
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

#include "helpers.h"

#include <QList>
#include <KUrl>
#include <KDebug>
#include <KStandardDirs>
#include <QProcess>

#include <language/duchain/types/unsuretype.h>
#include <language/duchain/types/integraltype.h>
#include <language/duchain/duchainlock.h>
#include <language/duchain/duchain.h>
#include <language/duchain/classdeclaration.h>
#include <language/duchain/aliasdeclaration.h>
#include <interfaces/iproject.h>
#include <interfaces/icore.h>
#include <interfaces/iprojectcontroller.h>

#include "ast.h"
#include "types/hintedtype.h"
#include "types/unsuretype.h"
#include "types/variablelengthcontainer.h"
#include "types/indexedcontainer.h"

using namespace KDevelop;

namespace Python {

QList<KUrl> Helper::cachedSearchPaths;
QString Helper::dataDir;
QString Helper::documentationFile;
DUChainPointer<TopDUContext> Helper::documentationFileContext = DUChainPointer<TopDUContext>(0);

AbstractType::Ptr Helper::resolveType(AbstractType::Ptr type)
{
    if ( type && type->whichType() == AbstractType::TypeAlias ) {
        return type.cast<TypeAliasType>()->type();
    }
    else
        return type;
}

AbstractType::Ptr Helper::extractTypeHints(AbstractType::Ptr type, TopDUContext* current)
{
    if ( type ) {
        kDebug() << type->toString();
    }
    else {
        kDebug();
    }
    UnsureType::Ptr result(new UnsureType());
    unsigned short maxHints = 7;
    if ( HintedType::Ptr hinted = type.cast<HintedType>() ) {
        if ( hinted->isValid(current) && isUsefulType(hinted.cast<AbstractType>()) ) {
            kDebug() << "Adding type hint: " << hinted->toString();
            result->addType(type->indexed());
        }
        else {
            kDebug() << "Discarding type hint: " << hinted->toString();
        }
    }
    else if ( UnsureType::Ptr unsure = type.cast<UnsureType>() ) {
        int len = unsure->typesSize();
        kDebug() << "Extracting hints from " << len << "types";
        for ( int i = 0; i < len and i < maxHints; i++ ) {
            if ( HintedType::Ptr hinted = unsure->types()[i].abstractType().cast<HintedType>() ) {
                if ( hinted->isValid(current) ) {
                    kDebug() << "Adding type hint (multi): " << hinted->toString();
                    result->addType(hinted->indexed());
                }
                else {
                    kDebug() << "Discarding type hint (multi): " << hinted->toString();
                    maxHints += 1;
                }
            }
            else {
                maxHints += 1;
            }
        }
    }
    else if ( IndexedContainer::Ptr indexed = type.cast<IndexedContainer>() ) {
        // TODO this is bad because it is slow. Make it faster!
        // TODO this would really be an important thing, as it will be called quite often.
        // TODO "how" is simple, just avoid cloning stuff if nothing needs to be changed (i.e. no hints exist).
        IndexedContainer::Ptr edit = IndexedContainer::Ptr(static_cast<IndexedContainer*>(indexed->clone()));
        for ( int i = 0; i < indexed->typesCount(); i++ ) {
            if ( HintedType::Ptr p = indexed->typeAt(i).abstractType().cast<HintedType>() ) {
                if ( ! p->isValid(current) ) {
                    edit->replaceType(i, AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed)));
                }
            }
        }
        return edit.cast<AbstractType>();
    }
    else if ( VariableLengthContainer::Ptr variable = type.cast<VariableLengthContainer>() ) {
        VariableLengthContainer::Ptr edit = VariableLengthContainer::Ptr(static_cast<VariableLengthContainer*>(variable->clone()));
        UnsureType::Ptr newContentType(new UnsureType());
        AbstractType::Ptr oldContentType = edit->contentType().abstractType();
        bool isHint = false;
        if ( oldContentType ) {
            if ( UnsureType::Ptr oldUnsure = oldContentType.cast<UnsureType>() ) {
                for ( unsigned int i = 0; i < oldUnsure->typesSize(); i++ ) {
                    if ( HintedType::Ptr hinted = oldUnsure->types()[i].abstractType().cast<HintedType>() ) {
                        isHint = true;
                        if ( ! hinted->isValid(current) ) {
                            continue;
                        }
                    }
                    newContentType->addType(oldUnsure->types()[i]);
                }
            }
            else if ( HintedType::Ptr hinted = oldContentType.cast<HintedType>() ) {
                isHint = true;
                if ( hinted->isValid(current) ) {
                    newContentType->addType(hinted->indexed());
                }
            }
            if ( ! isHint ) {
                return result.cast<AbstractType>();
            }
            edit->replaceContentType(newContentType.cast<AbstractType>());
            edit->replaceKeyType(variable->keyType().abstractType());
        }
        return edit.cast<AbstractType>();
    }
    return result.cast<AbstractType>();
}

QPair<FunctionDeclarationPointer, bool> Helper::functionDeclarationForCalledDeclaration(DeclarationPointer ptr)
{
    bool isConstructor = false;
    DeclarationPointer lastCalledDeclaration = ptr;
    if ( lastCalledDeclaration and not lastCalledDeclaration->isFunctionDeclaration() )
    {
        kDebug() << "No function declaration, looking for class constructor";
        kDebug() << "Class declaration: " << lastCalledDeclaration;
        if ( lastCalledDeclaration && lastCalledDeclaration->internalContext() ) {
            kDebug() << "ok, looking for constructor";
            QList<Declaration*> constructors = lastCalledDeclaration->internalContext()
                                               ->findDeclarations(KDevelop::Identifier("__init__"));
            kDebug() << "Found constructors: " << constructors;
            if ( ! constructors.isEmpty() ) {
                lastCalledDeclaration = dynamic_cast<FunctionDeclaration*>(constructors.first());
                isConstructor = true;
                kDebug() << "new function declaration: " << lastCalledDeclaration;
            }
        }
    }
    FunctionDeclarationPointer lastFunctionDeclaration;
    if ( lastCalledDeclaration ) {
        lastFunctionDeclaration = FunctionDeclarationPointer(dynamic_cast<FunctionDeclaration*>(lastCalledDeclaration.data()));
    }
    else lastFunctionDeclaration = FunctionDeclarationPointer(dynamic_cast<FunctionDeclaration*>(ptr.data()));
    return QPair<FunctionDeclarationPointer, bool>(lastFunctionDeclaration, isConstructor);
}

Declaration* Helper::declarationForName(NameAst* /*ast*/, const QualifiedIdentifier& identifier, const RangeInRevision& nodeRange, DUContextPointer context)
{
    QList<Declaration*> declarations;
    QList<Declaration*> localDeclarations;
    QList<Declaration*> importedLocalDeclarations;
    kDebug() << "Finding declaration for name" << identifier.toString() << " before " << nodeRange.end << ", in context" << context->range();
    {
        DUChainReadLocker lock(DUChain::lock());
        if ( context.data() == context->topContext() and nodeRange.isValid() ) {
            declarations = context->topContext()->findDeclarations(identifier, nodeRange.end);
        }
        else {
            declarations = context->topContext()->findDeclarations(identifier, CursorInRevision::invalid());
        }
        localDeclarations = context->findLocalDeclarations(identifier.last(), nodeRange.end, 0,
                                                           AbstractType::Ptr(0), DUContext::DontResolveAliases);
        importedLocalDeclarations = context->findDeclarations(identifier.last(), nodeRange.end);
    }
    Declaration* declaration;
    if ( localDeclarations.length() ) {
        declaration = localDeclarations.last();
        kDebug() << "Using local declaration";
    }
    else if ( importedLocalDeclarations.length() ) {
        // don't use declarations from class decls, they must be referenced through "self.<foo>"
        do {
            declaration = importedLocalDeclarations.last();
            importedLocalDeclarations.pop_back();
            if ( not declaration or declaration->context()->type() == DUContext::Class ) {
                declaration = 0;
            }
            if ( importedLocalDeclarations.isEmpty() ) {
                break;
            }
        } while ( not importedLocalDeclarations.isEmpty() );
        kDebug() << "Using imported local declaration (i.e., argument)";
    }
    else if ( declarations.length() ) {
        declaration = declarations.last();
        kDebug() << "Using global declaration";
    }
    else declaration = 0;
    return declaration;
}

QList< DUContext* > Helper::internalContextsForClass(StructureType::Ptr klassType, TopDUContext* context, ContextSearchFlags flags, int depth)
{
    QList<DUContext*> searchContexts;
    if ( ! klassType ) {
        return searchContexts;
    }
    searchContexts << klassType->internalContext(context);
    Declaration* decl = Helper::resolveAliasDeclaration(klassType->declaration(context));
    ClassDeclaration* klass = dynamic_cast<ClassDeclaration*>(decl);
    if ( klass ) {
        FOREACH_FUNCTION ( const BaseClassInstance& base, klass->baseClasses ) {
            if ( flags == PublicOnly and base.access == KDevelop::Declaration::Private ) {
                continue;
            }
            StructureType::Ptr baseClassType = base.baseClass.type<StructureType>();
            // recursive call, because the base class will have more base classes eventually
            if ( depth < 10 ) {
                searchContexts.append(Helper::internalContextsForClass(baseClassType, context, flags, depth + 1));
            }
        }
    }
    return searchContexts;
}

Declaration* Helper::resolveAliasDeclaration(Declaration* decl)
{
    AliasDeclaration* alias = dynamic_cast<AliasDeclaration*>(decl);
    if ( alias ) {
        return alias->aliasedDeclaration().data();
    }
    else
        return decl;
}

QString Helper::getDataDir() {
    if ( Helper::dataDir.isNull() ) {
        KStandardDirs d;
        Helper::dataDir = d.findDirs("data", "kdevpythonsupport/documentation_files").first();
    }
    return Helper::dataDir;
}

QString Helper::getDocumentationFile() {
    if ( Helper::documentationFile.isNull() ) {
        Helper::documentationFile = KStandardDirs::locate("data", "kdevpythonsupport/documentation_files/builtindocumentation.py");
    }
    return Helper::documentationFile;
}

ReferencedTopDUContext Helper::getDocumentationFileContext()
{
    if ( Helper::documentationFileContext ) {
        return ReferencedTopDUContext(Helper::documentationFileContext.data());
    }
    else {
        DUChainReadLocker lock;
        ReferencedTopDUContext ctx = ReferencedTopDUContext(DUChain::self()->chainForDocument(Helper::getDocumentationFile()));
        Helper::documentationFileContext = DUChainPointer<TopDUContext>(ctx.data());
        return ctx;
    }
    return ReferencedTopDUContext(0); // c++...
}
    
QList<KUrl> Helper::getSearchPaths(KUrl workingOnDocument)
{
    QList<KUrl> searchPaths;
    // search in the projects, as they're packages and likely to be installed or added to PYTHONPATH later
    foreach  (IProject* project, ICore::self()->projectController()->projects() ) {
        searchPaths.append(KUrl(project->folder().url()));
    }
    
    searchPaths.append(KUrl(getDataDir()));
    
    if ( cachedSearchPaths.isEmpty() ) {
        KStandardDirs d;
        kDebug() << "*** Gathering search paths...";
        QStringList getpath;
        getpath << "python" << "-c" << "import sys; sys.stdout.write(':'.join(sys.path))";
        
        QProcess python;
        python.start("/usr/bin/env", getpath);
        python.waitForFinished(1000);
        QByteArray pythonpath = python.readAllStandardOutput();
        QList<QByteArray> paths = pythonpath.split(':');
        paths.removeAll("");
        
        if ( ! pythonpath.isEmpty() ) {
            foreach ( const QString& path, paths ) {
                cachedSearchPaths.append(path);
            }
        }
        else {
            kWarning() << "Could not get search paths! Defaulting to stupid stuff.";
            searchPaths.append(KUrl("/usr/lib/python2.7"));
            searchPaths.append(KUrl("/usr/lib/python2.7/site-packages"));
            QString path = qgetenv("PYTHONPATH");
            QStringList paths = path.split(':');
            foreach ( const QString& path, paths ) {
                cachedSearchPaths.append(path);
            }
        }
        kDebug() << " *** Done. Got search paths: " << cachedSearchPaths;
    }
    else {
        kDebug() << " --- Search paths from cache: " << cachedSearchPaths;
    }
    
    searchPaths.append(cachedSearchPaths);
    
    // search in the current packages
    searchPaths.append(KUrl(workingOnDocument.directory()));
    
    kDebug() << "Search paths: " << searchPaths;
    kDebug() << workingOnDocument;
    return searchPaths;
}

bool Helper::isUsefulType(AbstractType::Ptr type)
{
    type = resolveType(type);
    if ( ! type ) {
        return false;
    }
    QList<uint> skipTypes;
    skipTypes << IntegralType::TypeMixed << IntegralType::TypeNone << IntegralType::TypeNull;
    if ( type->whichType() != AbstractType::TypeIntegral ) {
        return true;
    }
    if ( ! skipTypes.contains(type.cast<IntegralType>()->dataType()) ) {
        return true;
    }
    return false;
}

AbstractType::Ptr Helper::mergeTypes(AbstractType::Ptr type, AbstractType::Ptr newType, TopDUContext* ctx)
{
    UnsureType::Ptr unsure = UnsureType::Ptr::dynamicCast(type);
    UnsureType::Ptr newUnsure = UnsureType::Ptr::dynamicCast(newType);
    UnsureType::Ptr ret;
    
    if ( unsure ) {
        int len = unsure->typesSize();
        for ( int i = len; i > 0; i-- ) {
            HintedType::Ptr hinted = unsure.cast<HintedType>();
            if ( hinted and ! hinted->isValid(ctx) ) {
                unsure->removeType(hinted->indexed());
            }
        }
    }
    
    // both types are unsure, so join the list of possible types.
    if ( unsure && newUnsure ) {
        int len = newUnsure->typesSize();
        for ( int i = 0; i < len; i++ ) {
            unsure->addType(newUnsure->types()[i]);
        }
        ret = unsure;
    }
    // one of them is unsure, use that and add the other one
    else if ( unsure ) {
        if ( isUsefulType(newType) ) {
            unsure->addType(newType->indexed());
        }
        ret = unsure;
    }
    else if ( newUnsure ) {
        UnsureType::Ptr createdUnsureType = UnsureType::Ptr(static_cast<UnsureType*>(newUnsure->clone()));
        if ( isUsefulType(type) ) {
            createdUnsureType->addType(type->indexed());
        }
        ret = createdUnsureType;
    }
    else {
        unsure = UnsureType::Ptr(new UnsureType());
        if ( isUsefulType(type) ) {
            unsure->addType(type->indexed());
        }
        if ( isUsefulType(newType) ) {
            unsure->addType(newType->indexed());
        }
        if ( ! unsure.count() ) {
            return AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed));
        }
        ret = unsure;
    }
    if ( ret->typesSize() == 1 ) {
        return ret->types()[0].abstractType();
    }
    else {
        return AbstractType::Ptr::staticCast(ret);
    }
}

}
