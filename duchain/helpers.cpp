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

using namespace KDevelop;

namespace Python {

QList<KUrl> Helper::cachedSearchPaths;
QString Helper::dataDir = QString::null;
QString Helper::documentationFile = QString::null;
DUChainPointer<TopDUContext> Helper::documentationFileContext = DUChainPointer<TopDUContext>(0);

AbstractType::Ptr Helper::resolveType(AbstractType::Ptr type)
{
    if ( type && type->whichType() == AbstractType::TypeAlias ) {
        return type.cast<TypeAliasType>()->type();
    }
    else
        return type;
}

UnsureType::Ptr Helper::extractTypeHints(AbstractType::Ptr type, TopDUContext* current)
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
    return result;
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
            QString path = getenv("PYTHONPATH");
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
