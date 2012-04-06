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
        KSharedPtr< CodeCompletionContext > p = KDevelop::CodeCompletionContext::Ptr(this);
        KeywordItem::Flags f = KeywordItem::ForceLineBeginning;
        // TODO group those correctly so they appear at the top
        if ( m_position.line == 0 ) {
            resultingItems << CompletionTreeItemPointer(new KeywordItem(p, "#!/usr/bin/env python", f));
            resultingItems << CompletionTreeItemPointer(new KeywordItem(p, "#!/usr/bin/env python2.7", f));
            resultingItems << CompletionTreeItemPointer(new KeywordItem(p, "#!/usr/bin/env python3", f));
        }
        else if ( m_position.line == 1 ) {
            resultingItems << CompletionTreeItemPointer(new KeywordItem(p, "# -*- Coding:utf-8 -*-", f));
        }
    }
    
    
    if ( m_operation == PythonCodeCompletionContext::NoCompletion ) {
        
    }
    else if ( m_operation == PythonCodeCompletionContext::GeneratorVariableCompletion ) {
        QList<KeywordItem*> completionItems;
        KDevPG::MemoryPool pool;
        AstBuilder* builder = new AstBuilder(&pool);
        CodeAst* tmpAst = builder->parse(KUrl(), m_remainingExpression);
        if ( tmpAst ) {
            ExpressionVisitor* v = new ExpressionVisitor(m_context.data());
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
    else if ( m_operation == PythonCodeCompletionContext::DefineCompletion ) {
        // Find all base classes of the current class context
        if ( m_context->type() != DUContext::Class ) {
            kWarning() << "current context is not a class context, not offering define completion";
        }
        else if ( ClassDeclaration* klass = dynamic_cast<ClassDeclaration*>(m_context->owner()) ) {
            QList<DUContext*> baseClassContexts = Helper::internalContextsForClass(
                klass->type<StructureType>(), m_context->topContext()
            );
            baseClassContexts.removeAll(m_context.data()); // remove the class' own context
            Q_ASSERT(baseClassContexts.size() >= 1);
            foreach ( DUContext* c, baseClassContexts ) {
                QList<DeclarationDepthPair> declarations = c->allDeclarations(CursorInRevision::invalid(), m_context->topContext(), false);
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
            foreach ( DeclarationDepthPair d, m_context->topContext()->allDeclarations(CursorInRevision::invalid(), m_context->topContext()) ) {
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
            ExpressionVisitor* v = new ExpressionVisitor(m_context.data());
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
        if ( m_operation == PythonCodeCompletionContext::FunctionCallCompletion ) {
            // gather additional items to show above the real ones (for parameters, and stuff)
            QList<Declaration*> calltips;
            KDevPG::MemoryPool pool;
            AstBuilder* builder = new AstBuilder(&pool);
            CodeAst* tmpAst = builder->parse(KUrl(), m_guessTypeOfExpression);
            if ( tmpAst ) {
                ExpressionVisitor* v = new ExpressionVisitor(m_context.data());
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
        if ( ! cls || ! cls->internalContext(m_context->topContext()) ) {
            kWarning() << "No class type available, no completion offered";
            kDebug() << cls;
            return QList<CompletionTreeItemPointer>();
        }
        // the PublicOnly will filter out non-explictly defined __get__ etc. functions inherited from object
        QList<DUContext*> searchContexts = Helper::internalContextsForClass(cls, m_context->topContext(), Helper::PublicOnly);
        QList<DeclarationDepthPair> keepDeclarations;
        foreach ( const DUContext* currentlySearchedContext, searchContexts ) {
            kDebug() << "searching context " << currentlySearchedContext->scopeIdentifier() << "for autocompletion items";
            QList<DeclarationDepthPair> declarations = currentlySearchedContext->allDeclarations(CursorInRevision::invalid(), m_context->topContext(), false);
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

// decide what kind of completion will be offered based on the code before the current cursor position
PythonCodeCompletionContext::PythonCodeCompletionContext(DUContextPointer context, const QString& text,
                                                         const KDevelop::CursorInRevision& position, 
                                                         int depth, const PythonCodeCompletionWorker* parent)
    : CodeCompletionContext(context, text, position, depth)
    , m_operation(PythonCodeCompletionContext::DefaultCompletion)
    , parent(parent)
    , m_position(position)
    , m_context(context)
{
    m_workingOnDocument = context->topContext()->url().toUrl();
    int atLine = position.line;
    QString textWithoutStrings = CodeHelpers::killStrings(text);
    
    // check if the current position is inside a multi-line comment / string -> no completion if this is the case
    if ( CodeHelpers::endsInsideCommend(text) ) {
        m_operation = PythonCodeCompletionContext::NoCompletion;
        return;
    }
    
    // The expression parser used to determine the type of completion required.
    ExpressionParser parser(text);
    ExpressionParser::Status firstStatus;
    parser.popExpression(&firstStatus);
    
    if ( firstStatus == ExpressionParser::RaiseFound ) {
        m_operation = PythonCodeCompletionContext::RaiseExceptionCompletion;
        return;
    }

    if ( firstStatus == ExpressionParser::NothingFound ) {
        m_operation = PythonCodeCompletionContext::NewStatementCompletion;
        return;
    }
    
    if ( firstStatus == ExpressionParser::MemberAccessFound ) {
        bool ok;
        m_guessTypeOfExpression = parser.popExpression(&ok);
        if ( ok ) {
            m_operation = PythonCodeCompletionContext::MemberAccessCompletion;
        }
        else {
            m_operation = PythonCodeCompletionContext::NoCompletion;
        }
        return;
    }
    
    kDebug() << context->type() << DUContext::Class << context->localScopeIdentifier().toString();
    
    if ( context->type() == DUContext::Class ) {
        QRegExp defcompletion("(.*)\n([\\s]*)(def)[\\s]*[\\D]*$");
        defcompletion.setMinimal(true);
        bool is_defcompletion = defcompletion.exactMatch(currentLine);
        if ( is_defcompletion ) {
            m_indent = defcompletion.capturedTexts().at(2);
            m_operation = PythonCodeCompletionContext::DefineCompletion;
            return;
        }
    }
    
    QRegExp inheritanceCompletion("(.*)\n[\\s]*class[\\s]*(.*)[\\s]*\\([\\s]*$");
    inheritanceCompletion.setMinimal(true);
    bool is_inheritance = inheritanceCompletion.exactMatch(currentLine);
    if ( is_inheritance ) {
        m_operation = PythonCodeCompletionContext::InheritanceCompletion;
        return;
    }
    
    kDebug() << "Scanning for function call";
    bool is_FunctionCall = scanExpressionBackwards(textWithoutStrings, QStringList(), QStringList() << "." << ",", QStringList() << "," << "(", QStringList());
    if ( is_FunctionCall ) {
        m_operation = PythonCodeCompletionContext::FunctionCallCompletion;
        // TODO this is wrong. Example: foo(bar(baz, bang), foo, bar, I)
        m_alreadyGivenParametersCount = m_guessTypeOfExpression.count(',');
        
        scanExpressionBackwards(m_remainingExpression, QStringList(), QStringList() << "." << ",", QStringList(), QStringList() << "("); // get the next item in a chain of calls
                // for "a(b(c(), d, e" (we want autocompletion for b) the first call will give us "a(b" and "c(), d, e", but we want "b". so we call it again on the first result.
        kDebug() << "Found function call completion item, called function is " << m_guessTypeOfExpression << ", currently at parameter: " << m_alreadyGivenParametersCount;
    }
    
    QRegExp nocompletion("(.*)\n[\\s]*(class|def)[\\s]*$");
    nocompletion.setMinimal(true);
    bool is_nocompletion = nocompletion.exactMatch(currentLine);
    if ( is_nocompletion ) {
        m_operation = PythonCodeCompletionContext::NoCompletion;
        return;
    }
    
    QRegExp couldBeGeneratorCompletion("(.*)[\\[\\{](.*)[\\s]*for[\\s]*$");
    couldBeGeneratorCompletion.setMinimal(true);
    bool is_couldBeGeneratorCompletion = couldBeGeneratorCompletion.exactMatch(currentLine);
    if ( is_couldBeGeneratorCompletion ) {
        bool is_generatorCompletion = scanExpressionBackwards(textWithoutStrings, QStringList(), QStringList(), QStringList(), QStringList() << "{" << "[" << "(", true);
        if ( is_generatorCompletion ) {
            kDebug() << "remaining expression for GeneratorVariableCompletion: " << m_remainingExpression;
            m_remainingExpression = textWithoutStrings.remove(0, m_remainingExpression.length());
            if ( m_remainingExpression.length() >= 3 ) {
                m_remainingExpression = m_remainingExpression.trimmed();
                m_remainingExpression.remove(m_remainingExpression.length()-3, 3);
            }
            m_remainingExpression = '{' + m_remainingExpression + '}';
            kDebug() << "use unknown names in: " << m_remainingExpression;
            m_operation = PythonCodeCompletionContext::GeneratorVariableCompletion;
            return;
        }
    }
    
    //                                          v   v   v   v   v allow comma seperated list of imports
    QRegExp importfile("^[\\s]*import[\\s]*(.*[\\s]*,[\\s]*)*$");
    importfile.setMinimal(true);
    bool is_importfile = importfile.exactMatch(currentLine);
    QRegExp fromimport("^[\\s]*from[\\s]*$");
    fromimport.setMinimal(true);
    bool is_fromimport = fromimport.exactMatch(currentLine);
    if ( is_importfile || is_fromimport ) {
        kDebug() << "Autocompletion type: import completion";
        m_operation = PythonCodeCompletionContext::ImportFileCompletion;
        return;
    }
    
    //                                                 v   v   v   v   v allow comma seperated list of imports
    QRegExp importsub("^[\\s]*from(.*)import[\\s]*(.*[\\s]*,[\\s]*)*$");
    importsub.setMinimal(true);
    bool is_importSub = importsub.exactMatch(currentLine);
    QRegExp importsub2("^[\\s]*(from|import)[\\s]*(.*)\\.$");
    importsub2.setMinimal(true);
    bool is_importSub2 = importsub2.exactMatch(currentLine);
    if ( is_importSub || is_importSub2 ) {
        QStringList for_module_match;
        if ( is_importSub ) for_module_match = importsub.capturedTexts();
        else for_module_match = importsub2.capturedTexts();
        
        kDebug() << for_module_match;
        
        QString for_module;
        if ( is_importSub ) for_module = for_module_match[1].replace(" ", "");
        else for_module = for_module_match[2].replace(" ", "");
        
        kDebug() << "Matching against module name: " << for_module << is_importSub << is_importSub2;
        m_operation = PythonCodeCompletionContext::ImportSubCompletion;
        m_subForModule = for_module;
        kDebug() << "submodule: " << for_module;
        return;
    }
}

bool PythonCodeCompletionContext::scanExpressionBackwards(QString line, QStringList stopTokens, QStringList stopAtSpaceWithout, QStringList mustEndWithToken, QStringList ignoreAtEnd, bool ignoreWhitespace)
{
    int i = line.length() - 1;
    bool success = false;
    bool atEnd = true;
    bool previousWasSpace = false;
    QChar c;
    QChar colon('.'); QChar lbrace('('); QChar rbrace(')'); QChar lbracket('['); QChar rbracket(']'); QChar ldic('{'); QChar rdic('}');
    QList<QChar> openingBrackets; QList<QChar> closingBrackets;
    openingBrackets << lbrace << lbracket << ldic;
    closingBrackets << rbrace << rbracket << rdic;
    QStack<QChar> searchingForMatching;
    QString scanned = "";
    while ( i > 0 ) {
        c = line.at(i);
        if ( atEnd && ignoreAtEnd.contains(c) ) {
            i -= 1;
            continue;
        }
        scanned.insert(0, c);
        if ( atEnd ) previousWasSpace = false; // ignore trailing spaces
        if ( atEnd && ! c.isSpace() ) {
            if ( ! mustEndWithToken.count() || mustEndWithToken.contains(c) ) success = true;
            else success = false;
            atEnd = false;
        }
        if ( ! searchingForMatching.isEmpty() && c == searchingForMatching.top() ) {
            kDebug() << "Found matching " << c << "token";
            searchingForMatching.pop();
        }
        else if ( closingBrackets.contains(c) ) {
            kDebug() << "Searching for opening " << c << "token";
            searchingForMatching.push(openingBrackets.at(closingBrackets.indexOf(c)));
        }
        else if ( ! searchingForMatching.isEmpty() ) {
            // do nothing, this is in another expression, we don't care about it
        }
        else if ( openingBrackets.contains(c) ) {
            scanned[0] = ' ';
            break;
        }
        else if ( ! ignoreWhitespace && previousWasSpace && ! c.isSpace() && ! stopAtSpaceWithout.contains(c) ) {
            kDebug() << "Previous char was space, current is " << c << " -- break";
            scanned[0] = ' ';
            break;
        }
        else if ( stopTokens.contains(c) ) break;
        if ( c.isSpace() ) previousWasSpace = true;
        else previousWasSpace = false;
        i -= 1;
    }
    if ( success ) {
        m_guessTypeOfExpression = '\n' + scanned;
        // remove spaces at the beginning of the expression, they are treated as an INDENT token by the parser
        // and are thus a syntax error; also remove trailing dot
        m_guessTypeOfExpression.replace(QRegExp("\n[\\s]*"), "").replace(QRegExp("\\.[\\s]*$"), "");
        kDebug() << "Guess type of this expression: " << m_guessTypeOfExpression;
        m_remainingExpression = line.remove(i, line.length() - 1 - i);
        kDebug() << "Remaining expression: " << m_remainingExpression;
    }
    return success;
}

}
