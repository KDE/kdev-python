/*****************************************************************************
 * Copyright (c) 2011-2012 Sven Brauch <svenbrauch@googlemail.com>           *
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

#include <QProcess>
#include <QRegExp>
#include <KStandardDirs>
#include <KTextEditor/View>

#include <language/duchain/functiondeclaration.h>
#include <language/duchain/classdeclaration.h>
#include <language/duchain/aliasdeclaration.h>
#include <language/duchain/duchainutils.h>
#include <language/util/includeitem.h>
#include <language/codecompletion/normaldeclarationcompletionitem.h>
#include <language/codecompletion/codecompletionitem.h>
#include <language/codecompletion/codecompletionitemgrouper.h>
#include <interfaces/icore.h>
#include <interfaces/iprojectcontroller.h>
#include <interfaces/iproject.h>
#include <interfaces/idocumentcontroller.h>
#include <project/projectmodel.h>

#include "parser/astbuilder.h"
#include "duchain/pythoneditorintegrator.h"
#include "duchain/expressionvisitor.h"
#include "duchain/declarationbuilder.h"
#include "duchain/helpers.h"
#include "duchain/types/unsuretype.h"
#include "duchain/navigation/navigationwidget.h"

#include "worker.h"
#include "context.h"
#include "items/keyword.h"
#include "items/importfile.h"
#include "items/functiondeclaration.h"
#include "items/implementfunction.h"
#include "helpers.h"

using namespace KTextEditor;
using namespace KDevelop;

namespace Python {

QList<CompletionTreeItemPointer> PythonCodeCompletionContext::completionItems(bool& abort, bool fullCompletion)
{
    QList<CompletionTreeItemPointer> resultingItems;
    DUChainReadLocker lock;
    
    kDebug() << "Line: " << m_position.line;
    
    {
        KeywordItem::Flags f = KeywordItem::ForceLineBeginning;
        // TODO group those correctly so they appear at the top
        if ( m_position.line == 0 ) {
            resultingItems << CompletionTreeItemPointer(new KeywordItem(KDevelop::CodeCompletionContext::Ptr(this), "#!/usr/bin/env python", f));
            resultingItems << CompletionTreeItemPointer(new KeywordItem(KDevelop::CodeCompletionContext::Ptr(this), "#!/usr/bin/env python2.7", f));
            resultingItems << CompletionTreeItemPointer(new KeywordItem(KDevelop::CodeCompletionContext::Ptr(this), "#!/usr/bin/env python3", f));
        }
        else if ( m_position.line == 1 ) {
            resultingItems << CompletionTreeItemPointer(new KeywordItem(KDevelop::CodeCompletionContext::Ptr(this), "# -*- Coding:utf-8 -*-", f));
        }
    }
    
    if ( m_operation == PythonCodeCompletionContext::NoCompletion ) {
        kDebug() << "no code completion";
    }
    else if ( m_operation == PythonCodeCompletionContext::GeneratorVariableCompletion ) {
        QList<KeywordItem*> completionItems;
        KDevPG::MemoryPool pool;
        AstBuilder* builder = new AstBuilder(&pool);
        CodeAst* tmpAst = builder->parse(KUrl(), m_guessTypeOfExpression);
        if ( tmpAst ) {
            ExpressionVisitor* v = new ExpressionVisitor(m_duContext.data());
            v->m_forceGlobalSearching = true;
            v->m_scanUntilCursor = m_position;
            v->m_reportUnknownNames = true;
            v->visitCode(tmpAst);
            if ( not v->m_unknownNames.isEmpty() ) {
                if ( v->m_unknownNames.size() >= 2 ) {
                    // we only take the first two, and only two. It gets too much items otherwise.
                    QStringList combinations;
                    combinations << v->m_unknownNames.at(0) + ", " + v->m_unknownNames.at(1);
                    combinations << v->m_unknownNames.at(1) + ", " + v->m_unknownNames.at(0);
                    foreach ( const QString& c, combinations ) {
                        completionItems << new KeywordItem(KDevelop::CodeCompletionContext::Ptr(this), "" + c + " in ");
                    }
                }
                foreach ( const QString& n, v->m_unknownNames ) {
                    completionItems << new KeywordItem(KDevelop::CodeCompletionContext::Ptr(this), "" + n + " in ");
                }
            }
            else {
                kWarning() << "No unknown names in generator completion; nothing to do.";
            }
            delete v;
        }
        delete builder;
        
        foreach ( KeywordItem* item, completionItems ) {
            resultingItems << CompletionTreeItemPointer(item);
        }
        
    }
    else if ( m_operation == PythonCodeCompletionContext::FunctionCallCompletion ) {
            // gather additional items to show above the real ones (for parameters, and stuff)
            QList<Declaration*> calltips;
            KDevPG::MemoryPool pool;
            AstBuilder* builder = new AstBuilder(&pool);
            CodeAst* tmpAst = builder->parse(KUrl(), m_guessTypeOfExpression);
            if ( tmpAst ) {
                ExpressionVisitor* v = new ExpressionVisitor(m_duContext.data());
                v->m_forceGlobalSearching = true;
                v->visitCode(tmpAst);
                if ( v->lastDeclaration() ) {
                    calltips << v->lastDeclaration().data();
                }
                else {
                    kWarning() << "Did not receive a function declaration from expression visitor! Not offering call tips.";
                }
                delete v;
            }
            delete tmpAst;
            
            QList<DeclarationDepthPair> realCalltips_withDepth;
            foreach ( Declaration* current, calltips ) {
                if ( ! dynamic_cast<FunctionDeclaration*>(current) ) {
                    kDebug() << "Not a function declaration: " << current->toString();
                    continue;
                }
                realCalltips_withDepth.append(DeclarationDepthPair(current, 0));
            }
            
            QList<CompletionTreeItemPointer> calltipItems = declarationListToItemList(realCalltips_withDepth);
            foreach ( CompletionTreeItemPointer current, calltipItems ) {
                kDebug() << "Adding calltip item, at argument:" << m_alreadyGivenParametersCount+1; 
                static_cast<FunctionDeclarationCompletionItem*>(current.data())->setAtArgument(m_alreadyGivenParametersCount + 1);
            }
            
            resultingItems.append(calltipItems);
        }
    else if ( m_operation == PythonCodeCompletionContext::DefineCompletion ) {
        // Find all base classes of the current class context
        if ( m_duContext->type() != DUContext::Class ) {
            kWarning() << "current context is not a class context, not offering define completion";
        }
        else if ( ClassDeclaration* klass = dynamic_cast<ClassDeclaration*>(m_duContext->owner()) ) {
            QList<DUContext*> baseClassContexts = Helper::internalContextsForClass(
                klass->type<StructureType>(), m_duContext->topContext()
            );
            baseClassContexts.removeAll(m_duContext.data()); // remove the class' own context
            Q_ASSERT(baseClassContexts.size() >= 1);
            foreach ( DUContext* c, baseClassContexts ) {
                QList<DeclarationDepthPair> declarations = c->allDeclarations(CursorInRevision::invalid(), m_duContext->topContext(), false);
                foreach ( DeclarationDepthPair d, declarations ) {
                    if ( FunctionDeclaration* funcDecl = dynamic_cast<FunctionDeclaration*>(d.first) ) {
                        QStringList argumentNames;
                        DUContext* argumentsContext = DUChainUtils::getArgumentContext(funcDecl);
                        foreach ( Declaration* argument, argumentsContext->localDeclarations() ) {
                            argumentNames << argument->identifier().toString();
                        }
                        resultingItems << CompletionTreeItemPointer(new ImplementFunctionCompletionItem(
                            funcDecl->identifier().toString(), argumentNames, m_indent)
                        );
                    }
                }
            }
        }
    }
    else if ( m_operation == PythonCodeCompletionContext::ImportFileCompletion ) {
        kDebug() << "Preparing to do autocompletion for import...";
        m_maxFolderScanDepth = 1;
        foreach ( ImportFileItem* item, includeFileItems(Helper::getSearchPaths(m_workingOnDocument)) ) {
            Q_ASSERT(item);
            QString relativeUrl = KUrl::relativeUrl(m_workingOnDocument, item->includeItem.basePath);
            QString absoluteUrl = item->includeItem.basePath.path();
            // use whichever one is shorter
            QString useUrl = relativeUrl.length() < absoluteUrl.length() ? relativeUrl : absoluteUrl;
            item->includeItem.name = QString(item->moduleName + " (from " + useUrl + ")");
            resultingItems << CompletionTreeItemPointer( item );
        }
    }
    else if ( m_operation == PythonCodeCompletionContext::RaiseExceptionCompletion ) {
        kDebug() << "Finding items for raise statement";
        ReferencedTopDUContext ctx = Helper::getDocumentationFileContext();
        QList< Declaration* > declarations = ctx->findDeclarations(QualifiedIdentifier("BaseException"));
        if ( declarations.isEmpty() || ! declarations.first()->abstractType() ) {
            kDebug() << "No valid exception classes found, aborting";
        }
        else {
            Declaration* base = declarations.first();
            IndexedType baseType = base->abstractType()->indexed();
            QList<DeclarationDepthPair> validDeclarations;
            ClassDeclaration* current = 0;
            StructureType::Ptr type;
            foreach ( DeclarationDepthPair d, m_duContext->topContext()->allDeclarations(CursorInRevision::invalid(), m_duContext->topContext()) ) {
                if ( ( current = dynamic_cast<ClassDeclaration*>(d.first) ) ) {
                    if ( current->baseClassesSize() ) {
                        FOREACH_FUNCTION( const BaseClassInstance& base, current->baseClasses ) {
                            if ( base.baseClass == baseType ) {
                                validDeclarations << d;
                            }
                        }
                    }
                }
            }
            resultingItems.append(declarationListToItemList(validDeclarations));
        }
    }
    else if ( m_operation == PythonCodeCompletionContext::ImportSubCompletion ) {
        kDebug() << "Finding items for submodule: " << m_subForModule;
        foreach ( ImportFileItem* item, includeFileItemsForSubmodule(m_subForModule) ) {
            Q_ASSERT(item);
            item->includeItem.name = QString(item->moduleName + " (from " + KUrl::relativeUrl(m_workingOnDocument, item->includeItem.basePath) + ")");
            resultingItems << CompletionTreeItemPointer( item );
        }
    }
    else if ( m_operation == PythonCodeCompletionContext::InheritanceCompletion ) {
        kDebug() << "InheritanceCompletion";
        QList<DeclarationDepthPair> declarations = m_duContext->allDeclarations(m_position, m_duContext->topContext());
        QList<DeclarationDepthPair> remainingDeclarations;
        foreach ( DeclarationDepthPair d, declarations ) {
            Declaration* r = Helper::resolveAliasDeclaration(d.first);
            if ( r and r->identifier().identifier().str().contains("__kdevpythondocumentation_builtin") ) {
                continue;
            }
            if ( r && dynamic_cast<ClassDeclaration*>(r) ) {
                remainingDeclarations << d;
            }
        }
        resultingItems.append(declarationListToItemList(remainingDeclarations));
    }
    else if ( m_operation == PythonCodeCompletionContext::MemberAccessCompletion ) {
        KDevPG::MemoryPool pool;
        AstBuilder* builder = new AstBuilder(&pool);
        CodeAst* tmpAst = builder->parse(KUrl(), m_guessTypeOfExpression);
        if ( tmpAst ) {
            ExpressionVisitor* v = new ExpressionVisitor(m_duContext.data());
            v->m_forceGlobalSearching = true;
            v->visitCode(tmpAst);
            if ( v->lastType() ) {
                kDebug() << v->lastType()->toString();
                resultingItems = getCompletionItemsForType(v->lastType());
            }
            else {
                kWarning() << "Did not receive a type from expression visitor! Not offering autocompletion.";
            }
            delete v;
        }
        else {
            kWarning() << "Completion requested for syntactically invalid expression, not offering anything";
        }
        delete builder;
    }
    else {
        // it's stupid to display a 3-letter completion item on manually invoked code completion and makes everything look crowded
        if ( m_operation == PythonCodeCompletionContext::NewStatementCompletion && ! fullCompletion ) {
            QStringList keywordItems;
            keywordItems << "def" << "class" << "lambda" << "global" << "print" << "import" << "from" << "while" << "for" << "yield" << "return";
            foreach ( const QString& current, keywordItems ) {
                KeywordItem* k = new KeywordItem(KDevelop::CodeCompletionContext::Ptr(this), current + " ");
                resultingItems << CompletionTreeItemPointer(k);
            }
        }
        if ( abort ) {
            return QList<CompletionTreeItemPointer>();
        }
        QList<DeclarationDepthPair> declarations = m_duContext->allDeclarations(m_position, m_duContext->topContext());
        foreach ( DeclarationDepthPair d, declarations ) {
            if ( d.first and d.first->context()->type() == DUContext::Class ) {
                declarations.removeAll(d);
            }
            if ( d.first and d.first->identifier().identifier().str().contains("__kdevpythondocumentation_builtin") ) {
                declarations.removeAll(d);
            }
        }
        resultingItems.append(declarationListToItemList(declarations));
    }
    
    m_searchingForModule.clear();
    m_subForModule.clear();
    
    return resultingItems;
}

QList<CompletionTreeItemPointer> PythonCodeCompletionContext::declarationListToItemList(QList<DeclarationDepthPair> declarations, int maxDepth)
{
    QList<CompletionTreeItemPointer> items;
    
    DeclarationPointer currentDeclaration;
    DUChainPointer<Declaration> checkDeclaration;
    int count = declarations.length();
    for ( int i = 0; i < count; i++ ) {
        if ( maxDepth && maxDepth > declarations.at(i).second ) {
            kDebug() << "Skipped completion item because of its depth";
            continue;
        }
        currentDeclaration = DeclarationPointer(declarations.at(i).first);
        
        PythonDeclarationCompletionItem* item = 0;
        AliasDeclaration* alias = dynamic_cast<AliasDeclaration*>(currentDeclaration.data());
        if ( alias ) {
            checkDeclaration = DUChainPointer<Declaration>(alias->aliasedDeclaration().declaration());
        }
        else {
            checkDeclaration = currentDeclaration;
        }
        if ( checkDeclaration ) {
            AbstractType::Ptr type = checkDeclaration->abstractType();
            if ( type && ( type->whichType() == AbstractType::TypeFunction || type->whichType() == AbstractType::TypeStructure ) ) {
                item = new FunctionDeclarationCompletionItem(currentDeclaration);
            }
            else {
                item = new PythonDeclarationCompletionItem(currentDeclaration, KDevelop::CodeCompletionContext::Ptr(this));
            }
            items << CompletionTreeItemPointer(item);
        }
    }
    return items;
}

QList< CompletionTreeItemPointer > PythonCodeCompletionContext::getCompletionItemsForType(AbstractType::Ptr type)
{
    QList<CompletionTreeItemPointer> result;
    type = Helper::resolveType(type);
    if ( type->whichType() == AbstractType::TypeUnsure ) {
        UnsureType::Ptr unsure = type.cast<UnsureType>();
        int count = unsure->typesSize();
        kDebug() << "Getting completion items for " << count << "types of unsure type " << unsure;
        for ( int i = 0; i < count; i++ ) {
            result.append(getCompletionItemsForOneType(unsure->types()[i].abstractType()));
        }
    }
    else {
        result = getCompletionItemsForOneType(type);
    }
    return result;
}

QList<CompletionTreeItemPointer> PythonCodeCompletionContext::getCompletionItemsForOneType(AbstractType::Ptr type)
{
    type = Helper::resolveType(type);
    ReferencedTopDUContext builtinTopContext = Helper::getDocumentationFileContext();
    if ( type->whichType() == AbstractType::TypeStructure ) {
        // find properties of class declaration
        TypePtr<StructureType> cls = StructureType::Ptr::dynamicCast(type);
        kDebug() << "Finding completion items for class type";
        if ( ! cls || ! cls->internalContext(m_duContext->topContext()) ) {
            kWarning() << "No class type available, no completion offered";
            kDebug() << cls;
            return QList<CompletionTreeItemPointer>();
        }
        // the PublicOnly will filter out non-explictly defined __get__ etc. functions inherited from object
        QList<DUContext*> searchContexts = Helper::internalContextsForClass(cls, m_duContext->topContext(), Helper::PublicOnly);
        QList<DeclarationDepthPair> keepDeclarations;
        foreach ( const DUContext* currentlySearchedContext, searchContexts ) {
            kDebug() << "searching context " << currentlySearchedContext->scopeIdentifier() << "for autocompletion items";
            QList<DeclarationDepthPair> declarations = currentlySearchedContext->allDeclarations(CursorInRevision::invalid(), m_duContext->topContext(), false);
            kDebug() << "found" << declarations.length() << "declarations";
            
            // filter out those which are builtin functions, and those which were imported; we don't want those here
            // TODO rework this, it's maybe not the most elegant solution possible
            foreach ( DeclarationDepthPair current, declarations ) {
                if ( current.first->context() != builtinTopContext ) {
                    keepDeclarations.append(current);
                }
                else {
                    kDebug() << "Discarding declaration " << current.first->toString();
                }
            }
        }
        return declarationListToItemList(keepDeclarations);
    }
    
    return QList<CompletionTreeItemPointer>();
}

QList< ImportFileItem* > PythonCodeCompletionContext::includeFileItemsForSubmodule(QString submodule)
{
    QList<ImportFileItem*> items;
    QList<KUrl> searchPaths = Helper::getSearchPaths(m_workingOnDocument);
    QStringList subdirs = submodule.split(".");
    QList<KUrl> foundPaths;
    
    // this is a bit tricky. We need to find every path formed like /.../foo/bar for
    // a query string ("submodule" variable) like foo.bar
    // we also need paths like /foo.py, because then bar is probably a module in that file.
    // Thus, we first generate a list of possible paths, then match them against those which actually exist
    // and then gather all the items in those paths.
    
    foreach (KUrl currentPath, searchPaths) {
        bool exists = true;
        kDebug() << "Searching: " << currentPath;
        foreach ( QString subdir, subdirs ) {
            exists = currentPath.cd(subdir);
            kDebug() << currentPath;
            if ( ! exists ) break;
        }
        if ( exists ) {
            foundPaths.append(currentPath);
            kDebug() << "Found path: exists";
        }
    }
    return includeFileItems(foundPaths);
}

QList<ImportFileItem*> PythonCodeCompletionContext::includeFileItems(QList<KUrl> searchPaths) {
    QList<ImportFileItem*> items;
    
    kDebug() << "Gathering include file autocompletions...";
    
    foreach (KUrl currentPath, searchPaths) {
        currentPath.cleanPath();
        if ( currentPath.path(KUrl::AddTrailingSlash).startsWith(Helper::getDataDir()) ) {
            // don't suggest stuff from the docfiles directory
            continue;
        }
        kDebug() << "Processing path: " << currentPath;
        QDir currentDir(currentPath.path());
        QFileInfoList files = currentDir.entryInfoList();
        QStringList alreadyFound;
        foreach (QFileInfo file, files) {
            kDebug() << "Scanning file: " << file.absoluteFilePath();
            if ( file.fileName() == "." || file.fileName() == ".." ) continue;
            if ( file.fileName().endsWith(".py") || file.fileName().endsWith(".pyc") || file.isDir() ) {
                IncludeItem newItem;
                newItem.basePath = currentPath.path(KUrl::AddTrailingSlash) + file.baseName();
                newItem.name = file.fileName();
                newItem.isDirectory = file.isDir();
                ImportFileItem* item = new ImportFileItem(newItem);
                item->moduleName = file.fileName().replace(".pyc", "").replace(".pyo", "").replace(".py", "");
                if ( alreadyFound.contains(item->moduleName) ) {
                    continue;
                }
                else {
                    alreadyFound << item->moduleName;
                }
                items.append(item);
                kDebug() << "FOUND: " << file.absoluteFilePath();
            }
        }
    }
    
    return items;
}

PythonCodeCompletionContext::PythonCodeCompletionContext(DUContextPointer context, const QString& remainingText, int depth)
    : CodeCompletionContext(context, remainingText, CursorInRevision::invalid(), depth)
    , m_operation(FunctionCallCompletion)
{
    ExpressionParser p(remainingText);
    summonParentForEventualCall(p.popAll(), remainingText);
}

void PythonCodeCompletionContext::summonParentForEventualCall(const TokenList& allExpressions, const QString& text)
{
    QPair<int, int> nextCall = allExpressions.nextIndexOfStatus(ExpressionParser::CallFound);
    if ( nextCall.first != -1 ) {
        m_parentContext = new PythonCodeCompletionContext(m_duContext, text.mid(0, nextCall.second), depth() + 1);
        m_alreadyGivenParametersCount = nextCall.first;
    }
}

// decide what kind of completion will be offered based on the code before the current cursor position
PythonCodeCompletionContext::PythonCodeCompletionContext(DUContextPointer context, const QString& text,
                                                         const KDevelop::CursorInRevision& position, 
                                                         int depth, const PythonCodeCompletionWorker* parent)
    : CodeCompletionContext(context, text, position, depth)
    , m_operation(PythonCodeCompletionContext::DefaultCompletion)
    , worker(parent)
    , m_position(position)
{
    m_workingOnDocument = context->topContext()->url().toUrl();
    QString textWithoutStrings = CodeHelpers::killStrings(text);
    
    kDebug() << text;
    
    // check if the current position is inside a multi-line comment / string -> no completion if this is the case
    if ( CodeHelpers::endsInsideCommend(text) ) {
        m_operation = PythonCodeCompletionContext::NoCompletion;
        return;
    }
    
    // The expression parser used to determine the type of completion required.
    ExpressionParser parser(text);
    TokenList allExpressions = parser.popAll();
    allExpressions.reset(1);
    allExpressions.length();
    ExpressionParser::Status firstStatus = allExpressions.last().status;
    
    if ( firstStatus == ExpressionParser::MeaninglessKeywordFound ) {
        m_operation = DefaultCompletion;
        return;
    }
    
    if ( firstStatus == ExpressionParser::RaiseFound || firstStatus == ExpressionParser::ExceptFound ) {
        m_operation = RaiseExceptionCompletion;
        return;
    }

    if ( firstStatus == ExpressionParser::NothingFound ) {
        m_operation = NewStatementCompletion;
        return;
    }
    
    if ( firstStatus == ExpressionParser::MemberAccessFound ) {
        TokenListEntry item = allExpressions.weakPop();
        if ( item.status == ExpressionParser::ExpressionFound ) {
            m_guessTypeOfExpression = item.expression;
            m_operation = MemberAccessCompletion;
        }
        else {
            m_operation = NoCompletion;
        }
        return;
    }
    
    if ( firstStatus == ExpressionParser::DefFound ) {
        if ( context->type() == DUContext::Class ) {
            // TODO get and save current indentation level
            m_indent = "";
            m_operation = DefineCompletion;
        }
        else {
            m_operation = NoCompletion;
        }
        return;
    }
    
    QList<ExpressionParser::Status> defKeywords;
    defKeywords << ExpressionParser::DefFound << ExpressionParser::ClassFound;
    
    if ( firstStatus == ExpressionParser::CallFound ) {
        // 2 is always the case for "def foo(" or class foo(": one names the function, the other is the keyword
        if ( allExpressions.length() == 2 ) {
            if ( defKeywords.contains(allExpressions.first().status) ) {
                // The next thing the user probably wants to type are parameters for his function.
                // We cannot offer completion for this.
                m_operation = NoCompletion;
                return;
            }
        }
    }
    
    // For something like "func1(3, 5, func2(7, ", we want to show all calltips recursively
    // This happens after the previous "if", because the patterns are the same for "foo(..." and "def foo(...",
    // and the latter must be filtered out first (we don't want calltips for defining a function, that makes no sense).
    summonParentForEventualCall(allExpressions, text);
    
    // The "def in class context" case is handled above already
    if ( defKeywords.contains(firstStatus) ) {
        m_operation = NoCompletion;
        return;
    }
    
    if ( firstStatus == ExpressionParser::ForFound ) {
        int offset = allExpressions.length() - 2;
        QPair<int, int> nextInitializer = allExpressions.nextIndexOfStatus(ExpressionParser::InitializerFound);
        if ( nextInitializer.first == -1 ) {
            // no opening bracket, so no generator completion.
            m_operation = NoCompletion;
            return;
        }
        // check that all statements in between are part of a generator initializer list
        bool ok = true;
        QString text;
        while ( ok && offset > nextInitializer.first ) {
            ok = allExpressions.at(offset).status == ExpressionParser::ExpressionFound;
            if ( ! ok ) break;
            text.prepend(allExpressions.at(offset).status);
            offset -= 1;
            ok = allExpressions.at(offset).status == ExpressionParser::CommaFound;
            // the last expression must *not* have a comma
            if ( ! ok && nextInitializer.first == offset ) {
                ok = true;
            }
            offset -= 1;
        }
        if ( ok ) {
            m_remainingExpression = text;
            m_operation = GeneratorVariableCompletion;
            return;
        }
        else {
            m_operation = NoCompletion;
            return;
        }
    }
    
    int importIndex = allExpressions.nextIndexOfStatus(ExpressionParser::ImportFound).first;
    int fromIndex = allExpressions.nextIndexOfStatus(ExpressionParser::FromFound).first;
    
    if ( ( importIndex != -1 && fromIndex != -1 ) &&
         ( fromIndex == allExpressions.length() || importIndex == allExpressions.length() ) )
    {
        // it's either "import ... from" or "from ... import"
        if ( fromIndex > importIndex ) {
            // import ... from
            m_operation = ImportFileCompletion;
            return;
        }
        else {
            // from ... import
            m_operation = ImportSubCompletion;
            return;
        }
    }
    
    if ( fromIndex != -1 || importIndex != -1 ) {
        // it's either "from ..." or "import ...", which both come down to the same completion offered
        m_operation = ImportFileCompletion;
        return;
    }
}

}
