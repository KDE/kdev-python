/*
    SPDX-FileCopyrightText: 2011-2013 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#include "helpers.h"

#include <QList>
#include <QProcess>
#include <QSettings>
#include <QStandardPaths>

#include <QDebug>
#include "duchaindebug.h"

#include <language/duchain/types/unsuretype.h>
#include <language/duchain/types/integraltype.h>
#include <language/duchain/types/containertypes.h>
#include <language/duchain/types/functiontype.h>
#include <language/duchain/duchainutils.h>
#include <language/duchain/duchainlock.h>
#include <language/duchain/duchain.h>
#include <language/duchain/classdeclaration.h>
#include <language/duchain/aliasdeclaration.h>
#include <language/duchain/types/typeutils.h>
#include <language/backgroundparser/backgroundparser.h>
#include <interfaces/iproject.h>
#include <interfaces/iprojectcontroller.h>
#include <interfaces/icore.h>
#include <interfaces/ilanguagecontroller.h>
#include <interfaces/idocumentcontroller.h>
#include <util/path.h>

#include <KTextEditor/View>
#include <KConfigGroup>

#include "ast.h"
#include "types/hintedtype.h"
#include "types/unsuretype.h"
#include "types/indexedcontainer.h"
#include "kdevpythonversion.h"
#include "expressionvisitor.h"

#if QT_VERSION >= QT_VERSION_CHECK(5, 15, 0)
#define SkipEmptyParts Qt::SkipEmptyParts
#else
#define SkipEmptyParts QString::SkipEmptyParts
#endif

using namespace KDevelop;

namespace Python {

QMap<IProject*, QVector<QUrl>> Helper::cachedCustomIncludes;
QMap<IProject*, QVector<QUrl>> Helper::cachedSearchPaths;
QVector<QUrl> Helper::projectSearchPaths;
QStringList Helper::dataDirs;
IndexedString Helper::documentationFile;
DUChainPointer<TopDUContext> Helper::documentationFileContext = DUChainPointer<TopDUContext>(nullptr);
QStringList Helper::correctionFileDirs;
QString Helper::localCorrectionFileDir;
QMutex Helper::cacheMutex;
QMutex Helper::projectPathLock;

void Helper::scheduleDependency(const IndexedString& dependency, int betterThanPriority)
{
    BackgroundParser* bgparser = KDevelop::ICore::self()->languageController()->backgroundParser();
    bool needsReschedule = true;
    if ( bgparser->isQueued(dependency) ) {
        const auto priority= bgparser->priorityForDocument(dependency);
        if ( priority > betterThanPriority - 1 ) {
            bgparser->removeDocument(dependency);
        }
        else {
            needsReschedule = false;
        }
    }
    if ( needsReschedule ) {
        bgparser->addDocument(dependency, TopDUContext::ForceUpdate, betterThanPriority - 1,
                              nullptr, ParseJob::FullSequentialProcessing);
    }
}

IndexedDeclaration Helper::declarationUnderCursor(bool allowUse)
{
    KDevelop::IDocument* doc = ICore::self()->documentController()->activeDocument();
    const auto view = ICore::self()->documentController()->activeTextDocumentView();
    if ( doc && doc->textDocument() && view ) {
        DUChainReadLocker lock;
        const auto cursor = view->cursorPosition();
        if ( allowUse ) {
            return IndexedDeclaration(DUChainUtils::itemUnderCursor(doc->url(), cursor).declaration);
        }
        else {
            return DUChainUtils::declarationInLine(cursor, DUChainUtils::standardContextForUrl(doc->url()));
        }
    }

    return KDevelop::IndexedDeclaration();
}

Declaration* Helper::accessAttribute(const AbstractType::Ptr accessed,
                                     const IndexedIdentifier& attribute,
                                     const TopDUContext* topContext)
{
    if ( ! accessed ) {
        return nullptr;
    }
    // if the type is unsure, search all the possibilities (but return the first match)
    auto structureTypes = Helper::filterType<StructureType>(accessed,
        [](AbstractType::Ptr toFilter) {
            auto type = Helper::resolveAliasType(toFilter);
            return type && type->whichType() == AbstractType::TypeStructure;
        },
        [](AbstractType::Ptr toMap) {
            return Helper::resolveAliasType(toMap).staticCast<StructureType>();
        }
    );
    auto docFileContext = Helper::getDocumentationFileContext();

    for ( const auto& type: structureTypes ) {
        auto searchContexts = Helper::internalContextsForClass(type, topContext);
        for ( const auto ctx: searchContexts ) {
            auto found = ctx->findDeclarations(attribute, CursorInRevision::invalid(),
                                               topContext, DUContext::DontSearchInParent);
            if ( !found.isEmpty() && (
                   found.last()->topContext() != docFileContext ||
                   ctx->topContext() == docFileContext) ) {
                // never consider decls from the builtins
                return found.last();
            }
        }
    }
    return nullptr;
}

AbstractType::Ptr Helper::resolveAliasType(const AbstractType::Ptr eventualAlias)
{
    return TypeUtils::resolveAliasType(eventualAlias);
}

AbstractType::Ptr Helper::extractTypeHints(AbstractType::Ptr type)
{
    return Helper::foldTypes(Helper::filterType<AbstractType>(type, [](AbstractType::Ptr t) -> bool {
        auto hint = t.dynamicCast<HintedType>();
        return !hint || hint->isValid();
    }));
}

Helper::FuncInfo Helper::functionForCalled(Declaration* called, bool isAlias)
{
    if ( ! called ) {
        return { nullptr, false };
    }
    else if ( called->isFunctionDeclaration() ) {
        return { static_cast<FunctionDeclaration*>( called ), false };
    }
    // If we're calling a type object (isAlias == true), look for a constructor.
    static const IndexedIdentifier initId(KDevelop::Identifier("__init__"));

    // Otherwise look for a `__call__()` method.
    static const IndexedIdentifier callId(KDevelop::Identifier("__call__"));

    auto attr = accessAttribute(called->abstractType(), (isAlias ? initId : callId), called->topContext());
    return { dynamic_cast<FunctionDeclaration*>(attr), isAlias };
}

Declaration* Helper::declarationForName(const QString& name, const CursorInRevision& location,
                                        KDevelop::DUChainPointer<const DUContext> context)
{
    DUChainReadLocker lock(DUChain::lock());
    auto identifier = KDevelop::Identifier(name);
    auto localDeclarations = context->findLocalDeclarations(identifier, location, nullptr,
                                                            AbstractType::Ptr(), DUContext::DontResolveAliases);
    if ( !localDeclarations.isEmpty() ) {
        return localDeclarations.last();
    }

    QList<Declaration*> declarations;
    const DUContext* currentContext = context.data();
    bool findInNext = true, findBeyondUse = false;
    do {
        if (findInNext) {
            CursorInRevision findUntil = findBeyondUse ? currentContext->topContext()->range().end : location;
            declarations = currentContext->findDeclarations(identifier, findUntil);

            for (Declaration* declaration: declarations) {
                if (declaration->context()->type() != DUContext::Class ||
                    (currentContext->type() == DUContext::Function && declaration->context() == currentContext->parentContext())) {
                     // Declarations from class decls must be referenced through `self.<foo>`, except
                     //  in their local scope (handled above) or when used as default arguments for methods of the same class.
                     // Otherwise, we're done!
                    return declaration;
                }
            }
            if (!declarations.isEmpty()) {
                // If we found declarations but rejected all of them (i.e. didn't return), we need to keep searching.
                findInNext = true;
                declarations.clear();
            }
        }

        if (!findBeyondUse && currentContext->owner() && currentContext->owner()->isFunctionDeclaration()) {
            // Names in the body may be defined after the function definition, before the function is called.
            // Note: only the parameter list has type DUContext::Function, so we have to do this instead.
            findBeyondUse = findInNext = true;
        }
    } while ((currentContext = currentContext->parentContext()));

    return nullptr;
}


Declaration* Helper::declarationForName(const Python::NameAst* name, CursorInRevision location,
                                        KDevelop::DUChainPointer<const DUContext> context)
{
    const Ast* checkNode = name;
    while ((checkNode = checkNode->parent)) {
        switch (checkNode->astType) {
          default:
            continue;
          case Ast::ListComprehensionAstType:
          case Ast::SetComprehensionAstType:
          case Ast::DictionaryComprehensionAstType:
          case Ast::GeneratorExpressionAstType:
            // Variables in comprehensions are used before their definition. `[foo for foo in bar]`
            auto cmpEnd = CursorInRevision(checkNode->endLine, checkNode->endCol);
            if (cmpEnd > location) {
                location = cmpEnd;
            }
        }
    }
    return declarationForName(name->identifier->value, location, context);
}

QVector<DUContext*> Helper::internalContextsForClass(const StructureType::Ptr classType,
                        const TopDUContext* context, ContextSearchFlags flags, int depth)
{
    QVector<DUContext*> searchContexts;
    if ( ! classType ) {
        return searchContexts;
    }
    if ( auto c = classType->internalContext(context) ) {
        searchContexts << c;
    }
    auto decl = Helper::resolveAliasDeclaration(classType->declaration(context));
    if ( auto classDecl = dynamic_cast<ClassDeclaration*>(decl) ) {
        FOREACH_FUNCTION ( const auto& base, classDecl->baseClasses ) {
            if ( flags == PublicOnly && base.access == KDevelop::Declaration::Private ) {
                continue;
            }
            auto baseClassType = base.baseClass.type<StructureType>();
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
        DUChainReadLocker lock;
        return alias->aliasedDeclaration().data();
    }
    else
        return decl;
}

QStringList Helper::getDataDirs() {
    if ( Helper::dataDirs.isEmpty() ) {
        Helper::dataDirs = QStandardPaths::locateAll(QStandardPaths::GenericDataLocation, "kdevpythonsupport/documentation_files", QStandardPaths::LocateDirectory);
    }
    return Helper::dataDirs;
}

KDevelop::IndexedString Helper::getDocumentationFile()
{
    if ( Helper::documentationFile.isEmpty() ) {
        auto path = QStandardPaths::locate(QStandardPaths::GenericDataLocation, "kdevpythonsupport/documentation_files/builtindocumentation.py");
        Helper::documentationFile = IndexedString(path);
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
        auto file = Helper::getDocumentationFile();
        ReferencedTopDUContext ctx = ReferencedTopDUContext(DUChain::self()->chainForDocument(file));
        Helper::documentationFileContext = DUChainPointer<TopDUContext>(ctx.data());
        return ctx;
    }
}

// stolen from KUrl. duh.
static QString _relativePath(const QString &base_dir, const QString &path)
{
   QString _base_dir(QDir::cleanPath(base_dir));
   QString _path(QDir::cleanPath(path.isEmpty() || QDir::isRelativePath(path) ? _base_dir+QLatin1Char('/')+path : path));

   if (_base_dir.isEmpty())
      return _path;

   if (_base_dir[_base_dir.length()-1] != QLatin1Char('/'))
      _base_dir.append(QLatin1Char('/') );

   const QStringList list1 = _base_dir.split(QLatin1Char('/'), SkipEmptyParts);
   const QStringList list2 = _path.split(QLatin1Char('/'), SkipEmptyParts);

   // Find where they meet
   int level = 0;
   int maxLevel = qMin(list1.count(), list2.count());
   while((level < maxLevel) && (list1[level] == list2[level])) level++;

   QString result;
   // Need to go down out of the first path to the common branch.
   for(int i = level; i < list1.count(); i++)
      result.append(QLatin1String("../"));

   // Now up up from the common branch to the second path.
   for(int i = level; i < list2.count(); i++)
      result.append(list2[i]).append(QLatin1Char('/'));

   if ((level < list2.count()) && (path[path.length()-1] != QLatin1Char('/')))
      result.truncate(result.length()-1);

   return result;
}

QUrl Helper::getCorrectionFile(const QUrl& document)
{
    if ( Helper::correctionFileDirs.isEmpty() ) {
        Helper::correctionFileDirs = QStandardPaths::locateAll(QStandardPaths::GenericDataLocation,
                                                               "kdevpythonsupport/correction_files/",
                                                               QStandardPaths::LocateDirectory);
    }

    foreach (QString correctionFileDir, correctionFileDirs) {
        for ( const QUrl& basePath : Helper::getSearchPaths(QUrl()) ) {
            if ( ! basePath.isParentOf(document) ) {
                continue;
            }
            auto base = basePath.path();
            auto doc = document.path();
            auto relative = _relativePath(base, doc);
            auto fullPath = correctionFileDir + "/" + relative;
            if ( QFile::exists(fullPath) ) {
                return QUrl::fromLocalFile(fullPath).adjusted(QUrl::NormalizePathSegments);
            }
        }
    }
    return {};
}

QUrl Helper::getLocalCorrectionFile(const QUrl& document)
{
    if ( Helper::localCorrectionFileDir.isNull() ) {
        Helper::localCorrectionFileDir = QStandardPaths::writableLocation(QStandardPaths::GenericDataLocation) + QLatin1Char('/') + "kdevpythonsupport/correction_files/";
    }

    auto absolutePath = QUrl();
    for ( const auto& basePath : Helper::getSearchPaths(QUrl()) ) {
        if ( ! basePath.isParentOf(document) ) {
            continue;
        }
        auto path = QDir(basePath.path()).relativeFilePath(document.path());
        absolutePath = QUrl::fromLocalFile(Helper::localCorrectionFileDir + path);
        break;
    }
    return absolutePath;
}

QString Helper::getPythonExecutablePath(IProject* project)
{
    if ( project ) {
        auto interpreter = project->projectConfiguration()->group("pythonsupport").readEntry("interpreter");
        if ( !interpreter.isEmpty() ) {
            // we have a user-configured interpreter, try using it
            QFile f(interpreter);
            if ( f.exists() ) {
                return interpreter;
            }
            qCWarning(KDEV_PYTHON_DUCHAIN) << "Custom python interpreter" << interpreter << "configured for project" << project->name() << "is invalid, using default";
        }
    }

    // Find python 3 (https://www.python.org/dev/peps/pep-0394/)
    auto result = QStandardPaths::findExecutable("python" PYTHON_VERSION_STR);
    if ( ! result.isEmpty() ) {
        return result;
    }
    result = QStandardPaths::findExecutable("python" PYTHON_VERSION_MAJOR_STR);
    if ( ! result.isEmpty() ) {
        return result;
    }
    result = QStandardPaths::findExecutable("python");
    if ( ! result.isEmpty() ) {
        return result;
    }

#ifdef Q_OS_WIN
    QStringList extraPaths;
    // Check for default CPython installation path, because the
    // installer does not add the path to $PATH.
    QStringList keys = {
        "HKEY_LOCAL_MACHINE\\Software\\Python\\PythonCore\\PYTHON_VERSION\\InstallPath",
        "HKEY_LOCAL_MACHINE\\Software\\Python\\PythonCore\\PYTHON_VERSION-32\\InstallPath",
        "HKEY_CURRENT_USER\\Software\\Python\\PythonCore\\PYTHON_VERSION\\InstallPath",
        "HKEY_CURRENT_USER\\Software\\Python\\PythonCore\\PYTHON_VERSION-32\\InstallPath"
    };
    auto version = QString(PYTHON_VERSION_STR);
    foreach ( QString key, keys ) {
        key.replace("PYTHON_VERSION", version);
        QSettings base(key.left(key.indexOf("Python")), QSettings::NativeFormat);
        if ( ! base.childGroups().contains("Python") ) {
            continue;
        }
        QSettings keySettings(key, QSettings::NativeFormat);
        auto path = keySettings.value("Default").toString();
        if ( ! path.isEmpty() ) {
            extraPaths << path;
            break;
        }
    }
    result = QStandardPaths::findExecutable("python", extraPaths);
    if ( ! result.isEmpty() ) {
        return result;
    }
#endif
    // fallback
    return PYTHON_EXECUTABLE;
}

QVector<QUrl> Helper::getSearchPaths(const QUrl& workingOnDocument)
{
    QMutexLocker lock(&Helper::cacheMutex);
    QVector<QUrl> searchPaths;
    // search in the projects, as they're packages and likely to be installed or added to PYTHONPATH later
    // and also add custom include paths that are defined in the projects

    auto project = ICore::self()->projectController()->findProjectForUrl(workingOnDocument);
    {
        QMutexLocker lock(&Helper::projectPathLock);
        searchPaths << Helper::projectSearchPaths;
        searchPaths << Helper::cachedCustomIncludes.value(project);
    }
    
    for ( const QString& path : getDataDirs() ) {
        searchPaths.append(QUrl::fromLocalFile(path));
    }

    if ( !cachedSearchPaths.contains(project) ) {
        QVector<QUrl> cachedForProject;
        qCDebug(KDEV_PYTHON_DUCHAIN) << "*** Collecting search paths...";
        QStringList getpath;
        getpath << "-c" << "import sys; sys.stdout.write('$|$'.join(sys.path))";
        
        QProcess python;
        python.start(getPythonExecutablePath(project), getpath);
        python.waitForFinished(1000);
        QString pythonpath = QString::fromUtf8(python.readAllStandardOutput());

        if ( ! pythonpath.isEmpty() ) {
            const auto paths = pythonpath.split("$|$", SkipEmptyParts);
            for ( const QString& path : paths ) {
                cachedForProject.append(QUrl::fromLocalFile(path));
            }
        }
        else {
            qCWarning(KDEV_PYTHON_DUCHAIN) << "Could not get search paths! Defaulting to stupid stuff.";
            searchPaths.append(QUrl::fromLocalFile("/usr/lib/python" PYTHON_VERSION_STR));
            searchPaths.append(QUrl::fromLocalFile("/usr/lib/python" PYTHON_VERSION_STR "/site-packages"));
            QString path = qgetenv("PYTHONPATH");
            QStringList paths = path.split(':');
            for ( const QString& path : paths ) {
                cachedForProject.append(QUrl::fromLocalFile(path));
            }
        }
        qCDebug(KDEV_PYTHON_DUCHAIN) << " *** Done. Got search paths: " << cachedSearchPaths;
        cachedSearchPaths.insert(project, cachedForProject);
    }
    
    searchPaths.append(cachedSearchPaths.value(project));
    
    auto dir = workingOnDocument.adjusted(QUrl::RemoveFilename);
    if ( ! dir.isEmpty() ) {
        // search in the current packages
        searchPaths.append(dir);
    }
    
    return searchPaths;
}

bool Helper::isUsefulType(AbstractType::Ptr type)
{
    return TypeUtils::isUsefulType(type);
}

AbstractType::Ptr Helper::contentOfIterable(const AbstractType::Ptr iterable, const TopDUContext* topContext)
{
    auto types = filterType<StructureType>(iterable,
        [](AbstractType::Ptr t) { return t->whichType() == AbstractType::TypeStructure; } );

    static const IndexedIdentifier iterId(KDevelop::Identifier("__iter__"));
    static const IndexedIdentifier nextId(KDevelop::Identifier("__next__"));
    AbstractType::Ptr content(new IntegralType(IntegralType::TypeMixed));

    for ( const auto& type: types ) {
        if ( auto map = type.dynamicCast<MapType>() ) {
            // Iterating over dicts gets keys, not values
            content = mergeTypes(content, map->keyType().abstractType());
            continue;
        }
        else if ( auto list = type.dynamicCast<ListType>() ) {
            content = mergeTypes(content, list->contentType().abstractType());
            continue;
        }
        else if ( auto indexed = type.dynamicCast<IndexedContainer>() ) {
            content = mergeTypes(content, indexed->asUnsureType());
            continue;
        }
        DUChainReadLocker lock;
        // Content of an iterable object is iterable.__iter__().__next__().
        if ( auto iterFunc = dynamic_cast<FunctionDeclaration*>(accessAttribute(type, iterId, topContext)) ) {
            if ( auto iterator = iterFunc->type<FunctionType>()->returnType().dynamicCast<StructureType>() ) {
                if ( auto nextFunc = dynamic_cast<FunctionDeclaration*>(accessAttribute(iterator, nextId, topContext)) ) {
                    content = mergeTypes(content, nextFunc->type<FunctionType>()->returnType());
                }
            }
        }
    }
    return content;
}

AbstractType::Ptr Helper::mergeTypes(AbstractType::Ptr type, const AbstractType::Ptr newType)
{
    UnsureType::Ptr ret;
    return TypeUtils::mergeTypes<Python::UnsureType>(type, newType);
}

}
