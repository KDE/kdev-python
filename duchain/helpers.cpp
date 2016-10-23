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
#include <QProcess>
#include <QSettings>
#include <QStandardPaths>

#include <QDebug>
#include "duchaindebug.h"

#include <language/duchain/types/unsuretype.h>
#include <language/duchain/types/integraltype.h>
#include <language/duchain/types/containertypes.h>
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
#include <interfaces/ipartcontroller.h>
#include <util/path.h>

#include <shell/partcontroller.h>

#include <KTextEditor/View>
#include <KConfigGroup>

#include "ast.h"
#include "types/hintedtype.h"
#include "types/unsuretype.h"
#include "types/indexedcontainer.h"
#include "kdevpythonversion.h"
#include "expressionvisitor.h"

using namespace KDevelop;

namespace Python {

QMap<IProject*, QVector<QUrl>> Helper::cachedCustomIncludes;
QMap<IProject*, QVector<QUrl>> Helper::cachedSearchPaths;
QVector<QUrl> Helper::projectSearchPaths;
QStringList Helper::dataDirs;
QString Helper::documentationFile;
DUChainPointer<TopDUContext> Helper::documentationFileContext = DUChainPointer<TopDUContext>(0);
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
                              0, ParseJob::FullSequentialProcessing);
    }
}

IndexedDeclaration Helper::declarationUnderCursor(bool allowUse)
{
    KDevelop::IDocument* doc = ICore::self()->documentController()->activeDocument();
    const auto view = static_cast<KDevelop::PartController*>(ICore::self()->partController())->activeView();
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

Declaration* Helper::accessAttribute(Declaration* accessed, const QString& attribute, const DUContext* current)
{
    if ( ! accessed || ! accessed->abstractType() ) {
        return 0;
    }
    // if the type is unsure, search all the possibilities
    auto structureTypes = Helper::filterType<StructureType>(accessed->abstractType(),
        [](AbstractType::Ptr toFilter) {
            auto type = Helper::resolveAliasType(toFilter);
            return type && type->whichType() == AbstractType::TypeStructure;
        }
    );
    for ( auto type: structureTypes ) {
        QList<DUContext*> searchContexts = Helper::internalContextsForClass(type, current->topContext());
        for ( DUContext* c: searchContexts ) {
            auto found = c->findDeclarations(KDevelop::Identifier(attribute),
                                             CursorInRevision::invalid(),
                                             current->topContext(), DUContext::DontSearchInParent);
            std::reverse(found.begin(), found.end());
            // never consider decls from the builtins
            if ( ! found.isEmpty() && (
                   found.first()->topContext() != Helper::getDocumentationFileContext() ||
                   c->topContext() == Helper::getDocumentationFileContext() ) )
            {
                return found.first();
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
        auto hint = t.cast<HintedType>();
        return !hint || hint->isValid();
    }));
}

Helper::FuncInfo Helper::functionDeclarationForCalledDeclaration(DeclarationPointer ptr)
{
    if ( ! ptr ) {
        return FuncInfo();
    }
    bool isConstructor = false;
    DeclarationPointer calledDeclaration = ptr;
    if ( ! calledDeclaration->isFunctionDeclaration() ) {
        // not a function -- try looking for a constructor
        StructureType::Ptr classType = calledDeclaration->type<StructureType>();
        auto contexts = Helper::internalContextsForClass(classType, ptr->topContext());
        for ( DUContext* context: contexts ) {
            static KDevelop::Identifier initIdentifier("__init__");
            QList<Declaration*> constructors = context->findDeclarations(initIdentifier);
            if ( ! constructors.isEmpty() ) {
                calledDeclaration = dynamic_cast<FunctionDeclaration*>(constructors.first());
                isConstructor = true;
                break;
            }
        }
    }
    FunctionDeclarationPointer lastFunctionDeclaration;
    if ( calledDeclaration ) {
        // It was a class -- use the constructor
        lastFunctionDeclaration = calledDeclaration.dynamicCast<FunctionDeclaration>();
    }
    else {
        // Use the original declaration
        lastFunctionDeclaration = ptr.dynamicCast<FunctionDeclaration>();
    }
    return QPair<FunctionDeclarationPointer, bool>(lastFunctionDeclaration, isConstructor);
}

Declaration* Helper::declarationForName(const QualifiedIdentifier& identifier, const RangeInRevision& nodeRange,
                                        KDevelop::DUChainPointer<const DUContext> context)
{
    QList<Declaration*> declarations;
    QList<Declaration*> localDeclarations;
    QList<Declaration*> importedLocalDeclarations;
    {
        DUChainReadLocker lock(DUChain::lock());
        if ( context.data() == context->topContext() && nodeRange.isValid() ) {
            declarations = context->topContext()->findDeclarations(identifier, nodeRange.end);
        }
        else {
            declarations = context->topContext()->findDeclarations(identifier, CursorInRevision::invalid());
        }
        localDeclarations = context->findLocalDeclarations(identifier.last(), nodeRange.end, 0,
                                                           AbstractType::Ptr(0), DUContext::DontResolveAliases);
        importedLocalDeclarations = context->findDeclarations(identifier.last(), nodeRange.end);
    }
    Declaration* declaration = 0;
    if ( localDeclarations.length() ) {
        declaration = localDeclarations.last();
    }
    else if ( importedLocalDeclarations.length() ) {
        // don't use declarations from class decls, they must be referenced through "self.<foo>"
        do {
            declaration = importedLocalDeclarations.last();
            importedLocalDeclarations.pop_back();
            if ( !declaration || (declaration->context()->type() == DUContext::Class && context->type() != DUContext::Function) ) {
                declaration = 0;
            }
            if ( importedLocalDeclarations.isEmpty() ) {
                break;
            }
        } while ( ! importedLocalDeclarations.isEmpty() );
    }

    if ( !declaration && declarations.length() ) {
        declaration = declarations.last();
    }
    return declaration;
}

QList< DUContext* > Helper::internalContextsForClass(StructureType::Ptr klassType, TopDUContext* context, ContextSearchFlags flags, int depth)
{
    QList<DUContext*> searchContexts;
    if ( ! klassType ) {
        return searchContexts;
    }
    if ( auto c = klassType->internalContext(context) ) {
        searchContexts << c;
    }
    Declaration* decl = Helper::resolveAliasDeclaration(klassType->declaration(context));
    ClassDeclaration* klass = dynamic_cast<ClassDeclaration*>(decl);
    if ( klass ) {
        FOREACH_FUNCTION ( const BaseClassInstance& base, klass->baseClasses ) {
            if ( flags == PublicOnly && base.access == KDevelop::Declaration::Private ) {
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

QString Helper::getDocumentationFile() {
    if ( Helper::documentationFile.isNull() ) {
        Helper::documentationFile = QStandardPaths::locate(QStandardPaths::GenericDataLocation, "kdevpythonsupport/documentation_files/builtindocumentation.py");
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
        auto file = IndexedString(Helper::getDocumentationFile());
        ReferencedTopDUContext ctx = ReferencedTopDUContext(DUChain::self()->chainForDocument(file));
        Helper::documentationFileContext = DUChainPointer<TopDUContext>(ctx.data());
        return ctx;
    }
    return ReferencedTopDUContext(0); // c++...
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

   const QStringList list1 = _base_dir.split(QLatin1Char('/'), QString::SkipEmptyParts);
   const QStringList list2 = _path.split(QLatin1Char('/'), QString::SkipEmptyParts);

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
        foreach ( const QUrl& basePath, Helper::getSearchPaths(QUrl()) ) {
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
    foreach ( const auto& basePath, Helper::getSearchPaths(QUrl()) ) {
        if ( ! basePath.isParentOf(document) ) {
            continue;
        }
        auto path = QDir(basePath.path()).relativeFilePath(document.path());
        absolutePath = QUrl::fromLocalFile(Helper::localCorrectionFileDir + path);
        break;
    }
    return absolutePath;
}

QString getPythonExecutablePath(IProject* project)
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
    auto result = QStandardPaths::findExecutable("python" PYTHON_VERSION_MAJOR "." PYTHON_VERSION_MINOR);
    if ( ! result.isEmpty() ) {
        return result;
    }
    result = QStandardPaths::findExecutable("python" PYTHON_VERSION_MAJOR);
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
    auto version = QString(PYTHON_VERSION_MAJOR) + "." + PYTHON_VERSION_MINOR;
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
    
    foreach ( const QString& path, getDataDirs() ) {
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
        auto paths = pythonpath.split("$|$");
        paths.removeAll("");
        
        if ( ! pythonpath.isEmpty() ) {
            foreach ( const QString& path, paths ) {
                cachedForProject.append(QUrl::fromLocalFile(path));
            }
        }
        else {
            qCWarning(KDEV_PYTHON_DUCHAIN) << "Could not get search paths! Defaulting to stupid stuff.";
            searchPaths.append(QUrl::fromLocalFile("/usr/lib/python3.5"));
            searchPaths.append(QUrl::fromLocalFile("/usr/lib/python3.5/site-packages"));
            QString path = qgetenv("PYTHONPATH");
            QStringList paths = path.split(':');
            foreach ( const QString& path, paths ) {
                cachedForProject.append(QUrl::fromLocalFile(path));
            }
        }
        qCDebug(KDEV_PYTHON_DUCHAIN) << " *** Done. Got search paths: " << cachedSearchPaths;
        cachedSearchPaths.insert(project, cachedForProject);
    }
    else {
        qCDebug(KDEV_PYTHON_DUCHAIN) << " --- Search paths from cache: " << cachedSearchPaths;
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

AbstractType::Ptr Helper::contentOfIterable(const AbstractType::Ptr iterable)
{
    auto items = filterType<AbstractType>(iterable,
        [](AbstractType::Ptr t) {
            return ListType::Ptr::dynamicCast(t) || IndexedContainer::Ptr::dynamicCast(t);
        },
        [](AbstractType::Ptr t) {
            if ( auto variable = ListType::Ptr::dynamicCast(t) ) {
                return AbstractType::Ptr(variable->contentType().abstractType());
            }
            else {
                auto indexed = t.cast<IndexedContainer>();
                return indexed->asUnsureType();
            }
        }
    );

    if ( items.size() == 1 ) {
        return items.first();
    }
    auto unsure = AbstractType::Ptr(new UnsureType);
    for ( auto type: items ) {
        Helper::mergeTypes(unsure, type);
    }
    return unsure;
}

AbstractType::Ptr Helper::mergeTypes(AbstractType::Ptr type, const AbstractType::Ptr newType)
{
    UnsureType::Ptr ret;
    return TypeUtils::mergeTypes<Python::UnsureType>(type, newType);
}

}
