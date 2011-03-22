/*****************************************************************************
 * Copyright (c) 2011 Sven Brauch <svenbrauch@googlemail.com>                *
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

#include <qprocess.h>
#include <QtCore/QRegExp>

#include <language/duchain/duchainpointer.h>
#include <language/duchain/declaration.h>
#include <language/duchain/functiondeclaration.h>
#include <language/codecompletion/codecompletionitem.h>
#include <language/codecompletion/normaldeclarationcompletionitem.h>
#include <language/codecompletion/abstractincludefilecompletionitem.h>
#include <language/codecompletion/codecompletionitem.h>
#include <language/util/includeitem.h>

#include <interfaces/icore.h>
#include <interfaces/iprojectcontroller.h>
#include <interfaces/iproject.h>
#include <project/projectmodel.h>

#include "keyworditem.h"
#include "pythoncodecompletionworker.h"
#include "astbuilder.h"
#include "expressionvisitor.h"
#include "navigation/navigationwidget.h"
#include "importfileitem.h"
#include "functiondeclarationcompletionitem.h"
#include "pythoncodecompletioncontext.h"
#include "pythoneditorintegrator.h"
#include "duchain/declarationbuilder.h"
#include "parser/parserConfig.h"
#include "implementfunctioncompletionitem.h"

using namespace KTextEditor;
using namespace KDevelop;

typedef QStringList implementFunctionDescription;

namespace Python {

QList<CompletionTreeItemPointer> PythonCodeCompletionContext::completionItems(bool& abort, bool fullCompletion)
{
    if ( abort ) 
        return QList<CompletionTreeItemPointer>();
    
    QList<CompletionTreeItemPointer> items;
    DUChainReadLocker lock(DUChain::lock());
    
    kDebug() << "Line: " << m_position.line;
    if ( m_position.line == 0 ) { // TODO group those correctly so they appear at the top
        items << CompletionTreeItemPointer(new KeywordItem(KDevelop::CodeCompletionContext::Ptr(this), "#!/usr/bin/env python"));
        items << CompletionTreeItemPointer(new KeywordItem(KDevelop::CodeCompletionContext::Ptr(this), "#!/usr/bin/env python2.6"));
        items << CompletionTreeItemPointer(new KeywordItem(KDevelop::CodeCompletionContext::Ptr(this), "#!/usr/bin/env python2.7"));
    }
    
    if ( m_operation == PythonCodeCompletionContext::NoCompletion ) {
            
    }
    else if ( m_operation == PythonCodeCompletionContext::DefineCompletion ) {
        QList<implementFunctionDescription> funcs;
        // well, duh. I didn't think it's that many functions.
        {
        funcs << ( implementFunctionDescription() << "__init__" << "self" << "self" );
        funcs << ( implementFunctionDescription() << "__new__" << "self" << "self" );
        funcs << ( implementFunctionDescription() << "__del__" << "self" << "self" );
        funcs << ( implementFunctionDescription() << "__repr__" << "self" << "self" );
        funcs << ( implementFunctionDescription() << "__str__" << "self" << "self" );
        funcs << ( implementFunctionDescription() << "__lt__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__gt__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__le__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__eq__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__ne__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__gt__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__ge__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__cmp__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__hash__" << "self" << "self" );
        funcs << ( implementFunctionDescription() << "__nonzero__" << "self" << "self" );
        funcs << ( implementFunctionDescription() << "__unicode__" << "self" << "self" );
        funcs << ( implementFunctionDescription() << "__getattr__" << "self, <string> name" << "self, name" );
        funcs << ( implementFunctionDescription() << "__setattr__" << "self, <string> name, <any object> value" << "self, name, value" );
        funcs << ( implementFunctionDescription() << "__delattr__" << "self, <string> name" << "self, name" );
        funcs << ( implementFunctionDescription() << "__getattribute__" << "self, <string> name" << "self, name" );
        funcs << ( implementFunctionDescription() << "__get__" << "self, <any object> instance, <class> owner" << "self, instance, owner" );
        funcs << ( implementFunctionDescription() << "__set__" << "self, <any object> instance, <any object> value" << "self, instance, value" );
        funcs << ( implementFunctionDescription() << "__delete__" << "self, <any object> instance" << "self, instance" );
        funcs << ( implementFunctionDescription() << "__instancecheck__" << "self, <any object> instance" << "self, instance" );
        funcs << ( implementFunctionDescription() << "__subclasscheck__" << "self, <any object> subclass" << "self, subclass" );
        funcs << ( implementFunctionDescription() << "__call__" << "self, [...args]" << "self" );
        funcs << ( implementFunctionDescription() << "__len__" << "self" << "self" );
        funcs << ( implementFunctionDescription() << "__getitem__" << "self, <string> key" << "self, key" );
        funcs << ( implementFunctionDescription() << "__setitem__" << "self, <string> key, <any object> value" << "self, key, value" );
        funcs << ( implementFunctionDescription() << "__delitem__" << "self, <string> key" << "self, key" );
        funcs << ( implementFunctionDescription() << "__iter__" << "self" << "self" );
        funcs << ( implementFunctionDescription() << "__reversed__" << "self" << "self" );
        funcs << ( implementFunctionDescription() << "__contains__" << "self, <any object> item" << "self, item" );
        funcs << ( implementFunctionDescription() << "__getslice__" << "self, <int> i, <int> j" << "self, i, j" );
        funcs << ( implementFunctionDescription() << "__delslice__" << "self, <int> i, <int> j" << "self, i, j" );
        funcs << ( implementFunctionDescription() << "__add__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__sub__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__mul__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__floordiv__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__mod__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__divmod__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__pow__" << "self, <any object> other, [modulo]" << "self, other" );
        funcs << ( implementFunctionDescription() << "__lshift__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__rshift__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__and__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__xor__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__or__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__div__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__truediv__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__radd__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__rsub__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__rmul__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__rtruediv__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__rfloordiv__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__rmod__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__rdivmod__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__rpow__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__rlshift__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__rrshift__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__rand__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__rxor__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__ror__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__iadd__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__isub__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__imul__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__idiv__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__itruediv__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__ifloordiv__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__imod__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__ipow__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__ilshift__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__irshift__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__iand__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__ixor__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__ior__" << "self, <any object> other" << "self, other" );
        funcs << ( implementFunctionDescription() << "__neg__" << "self" << "self" );
        funcs << ( implementFunctionDescription() << "__pos__" << "self" << "self" );
        funcs << ( implementFunctionDescription() << "__abs__" << "self" << "self" );
        funcs << ( implementFunctionDescription() << "__invert__" << "self" << "self" );
        funcs << ( implementFunctionDescription() << "__complex__" << "self" << "self" );
        funcs << ( implementFunctionDescription() << "__int__" << "self" << "self" );
        funcs << ( implementFunctionDescription() << "__long__" << "self" << "self" );
        funcs << ( implementFunctionDescription() << "__float__" << "self" << "self" );
        funcs << ( implementFunctionDescription() << "__oct__" << "self" << "self" );
        funcs << ( implementFunctionDescription() << "__hex__" << "self" << "self" );
        funcs << ( implementFunctionDescription() << "__index__" << "self" << "self" );
        funcs << ( implementFunctionDescription() << "__coerce__" << "self, <any object> other" << "self, other" );
        }

        foreach ( implementFunctionDescription func, funcs ) {
            items << CompletionTreeItemPointer(new ImplementFunctionCompletionItem(func.at(0), func.at(1), func.at(2), m_indent));
        }
    }
    else if ( m_operation == PythonCodeCompletionContext::ImportFileCompletion ) {
        kDebug() << "Preparing to do autocompletion for import...";
        m_maxFolderScanDepth = 1;
        foreach ( ImportFileItem* item, includeFileItems(getSearchPaths(m_workingOnDocument)) ) {
            Q_ASSERT(item);
            item->includeItem.name = QString(item->moduleName + " (from " + KUrl::relativeUrl(m_workingOnDocument, item->includeItem.basePath) + ")");
            items << CompletionTreeItemPointer( item );
        }
    }
    else if ( m_operation == PythonCodeCompletionContext::ImportSubCompletion ) {
        foreach ( ImportFileItem* item, includeFileItemsForSubmodule(m_subForModule) ) {
            Q_ASSERT(item);
            item->includeItem.name = QString(item->moduleName + " (from " + KUrl::relativeUrl(m_workingOnDocument, item->includeItem.basePath) + ")");
            items << CompletionTreeItemPointer( item );
        }
    }
    else if ( m_operation == PythonCodeCompletionContext::MemberAccessCompletion ) {
        AstBuilder* builder = new AstBuilder();
        CodeAst* tmpAst = builder->parse(KUrl(), m_guessTypeOfExpression);
        if ( tmpAst ) {
            PythonEditorIntegrator* ed = new PythonEditorIntegrator();
            ExpressionVisitor* v = new ExpressionVisitor(m_context.data(), ed);
            v->visitCode(tmpAst);
            if ( v->lastType() ) {
                kDebug() << v->lastType()->toString();
                items = getCompletionItemsForType(v->lastType(), v->lastDeclaration());
            }
            else {
                kWarning() << "Did not receive a type from expression visitor! Not offering autocompletion.";
            }
        }
        else {
            kWarning() << "Completion requested for syntactically invalid expression, not offering anything";
        }
    }
    else {
        // it's stupid to display a 3-letter completion item on manually invoked code completion and makes everything look crowded
        if ( m_operation == PythonCodeCompletionContext::NewStatementCompletion && ! fullCompletion ) {
            QStringList keywordItems;
            keywordItems << "def" << "class" << "lambda" << "global" << "print" << "import" << "from" << "while" << "for";
            foreach ( const QString& current, keywordItems ) {
                items << CompletionTreeItemPointer(new KeywordItem(KDevelop::CodeCompletionContext::Ptr(this), current));
            }
        }
        if ( abort ) {
            return QList<CompletionTreeItemPointer>();
        }
        QList<DeclarationDepthPair> declarations = m_duContext->allDeclarations(m_position, m_duContext->topContext());
        items.append(declarationListToItemList(declarations));
    }
    
    m_searchingForModule.clear();
    m_subForModule.clear();
    
    return items;
}

QList<CompletionTreeItemPointer> PythonCodeCompletionContext::declarationListToItemList(QList<DeclarationDepthPair> declarations, int maxDepth)
{
    QList<CompletionTreeItemPointer> items;
    
    DeclarationPointer currentDeclaration;
    int count = declarations.length();
    for ( int i = 0; i < count; i++ ) {
        if ( maxDepth && maxDepth > declarations.at(i).second ) {
            kDebug() << "Skipped completion item because of its depth";
            continue;
        }
        currentDeclaration = DeclarationPointer(declarations.at(i).first);
        m_keepalive.append(currentDeclaration);
        
//         kDebug() << "Adding item: " << currentDeclaration.data()->identifier().identifier().str();
        NormalDeclarationCompletionItem* item;
        if ( currentDeclaration.data()->abstractType() && currentDeclaration.data()->abstractType().constData()->whichType() == AbstractType::TypeFunction ) {
//             kDebug() << "Adding function declaration item";
            item = new FunctionDeclarationCompletionItem(currentDeclaration);
        }
        else {
            item = new NormalDeclarationCompletionItem(currentDeclaration, KDevelop::CodeCompletionContext::Ptr(this));
        }
        kDebug() << item->declaration().data()->identifier().identifier().str();
        items << CompletionTreeItemPointer(item);
    }
    return items;
}

QList<CompletionTreeItemPointer> PythonCodeCompletionContext::getCompletionItemsForType(AbstractType::Ptr type, DeclarationPointer declaration)
{
    if ( type->whichType() == AbstractType::TypeStructure ) {
        // find properties of class declaration
        TypePtr<StructureType> cls = StructureType::Ptr::dynamicCast(type);
        kDebug() << "Finding completion items for class type";
//         kDebug() << cls->internalContext(m_context->topContext()) << cls->internalContext(declaration->context()->topContext());
        if ( ! cls || ! cls->internalContext(m_context->topContext()) ) {
            kWarning() << "No class type available, no completion offered";
            kDebug() << cls;
            return QList<CompletionTreeItemPointer>();
        }
        QList<DeclarationDepthPair> declarations = cls->internalContext(m_context->topContext())->allDeclarations(CursorInRevision::invalid(), m_context->topContext(), false);
        QList<DeclarationDepthPair> keepDeclarations;
        // filter out those which are builtin functions, and those which were imported; we don't want those here
        // TODO rework this, it's maybe not the most elegant solution possible
        foreach ( DeclarationDepthPair current, declarations ) {
            if ( current.first->context() != DUChain::self()->chainForDocument(QString(DOCFILE_PATH)) ) {
                kDebug() << "Keeping declaration" << current.first->toString();
                keepDeclarations.append(current);
            }
            else {
                kDebug() << "Discarding declaration " << current.first->toString();
            }
        }
        return declarationListToItemList(keepDeclarations);
    }
    
    if ( type->whichType() == AbstractType::TypeIntegral ) {
        kDebug() << "Finding completion items for integral type";
    }
    
    QList<CompletionTreeItemPointer> items;
    return items;
}

QList< ImportFileItem* > PythonCodeCompletionContext::includeFileItemsForSubmodule(QString submodule)
{
    QList<ImportFileItem*> items;
    QList<KUrl> searchPaths = getSearchPaths(m_workingOnDocument);
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
        kDebug() << "Processing path: " << currentPath;
        QDir currentDir(currentPath.path());
        QFileInfoList files = currentDir.entryInfoList();
        foreach (QFileInfo file, files) {
            kDebug() << "Scanning file: " << file.absoluteFilePath();
            if ( file.fileName() == "." || file.fileName() == ".." ) continue;
            if ( file.fileName().endsWith(".py") || file.fileName().endsWith(".pyc") || file.isDir() ) {
                IncludeItem includeItem;
                includeItem.basePath = file.baseName();
                includeItem.name = file.fileName();
                includeItem.isDirectory = file.isDir();
                ImportFileItem* item = new ImportFileItem(includeItem);
                item->moduleName = file.fileName().replace(".pyc", "").replace(".pyo", "").replace(".py", "");
                items.append(item);
                kDebug() << "FOUND: " << file.absoluteFilePath();
            }
        }
    }
    
    return items;
}

// decide what kind of completion will be offered based on the code before the current cursor position
// lazy as we are, we use regular expression matching for this
PythonCodeCompletionContext::PythonCodeCompletionContext(DUContextPointer context, const QString& text, const KDevelop::CursorInRevision& position, 
                                                         int depth, const PythonCodeCompletionWorker* parent): CodeCompletionContext(context, text, position, depth),
                                                         parent(parent), m_context(context), m_position(position), m_operation(PythonCodeCompletionContext::DefaultCompletion)
{
    m_workingOnDocument = parent->parent->m_currentDocument;
    QString currentLine = "\n" + text.split("\n").last(); // we'll only look at the last line, as 99% of python statements are limited to one line
    int atLine = position.line;
    kDebug() << "Doing auto-completion context scan for: " << currentLine << "@line" << atLine << "@context" << context->range().castToSimpleRange();
    
    bool currentLineIsEmpty = true;
    {
        QChar c;
        for ( int i = currentLine.length() - 1; i >= 0; i-- ) {
            c = currentLine.at(i);
            if ( ! c.isSpace() ) {
                currentLineIsEmpty = false;
                break;
            }
        }
    }
    
    // okay, so our contexts end too early. They end at the last valid token of a function or such,
    // but not at the DEDENT token. This means, if a function ends with 5 empty but indented lines, and you
    // place your cursor in the 3rd one and start typing, there's no completion for variables local to the function.
    // Thus, we walk back in the text line-by-line, searching for some context which has the same
    // indent like the current one and is directly before it in the code.
    DUContext* currentlyChecked = context.data();
    int currentlyCheckedLine = atLine;
    {
        DUChainReadLocker lock(DUChain::lock());
        while ( currentlyChecked == context.data() && currentlyCheckedLine >= 0 ) {
            currentlyChecked = context->topContext()->findContextAt(CursorInRevision(currentlyCheckedLine, 0));
            currentlyCheckedLine -= 1;
        }
    }
    
    // cool, we found something. Now we need to compare its indent to the current one; if they don't match, then 
    // we ignore it and use the one provided as an argument to this function. Otherwise, we use what we found.
    if ( currentlyChecked ) {
        int previousEndsAtLine = currentlyChecked->range().castToSimpleRange().end.line;
        kDebug() << "Previous context ends at line" << previousEndsAtLine;
        kDebug() << "Previous / Current context ranges: " << currentlyChecked->range().castToSimpleRange() << context->range().castToSimpleRange();
        int skipLinesBack = atLine - previousEndsAtLine; // how many lines to skip backwards
        int i = text.length();
        QChar newline = QString("\n").at(0);
        
        // init indents array
        QMap<int, int> indentForLine;
        const int invalid = -1;
        indentForLine[atLine] = invalid; indentForLine[previousEndsAtLine] = invalid;
        
        int currentIndent = 0;
        int skippedLines = 0;
        QChar c;
        while ( i > 0 ) {
            i -= 1;
            c = text.at(i);
            if ( c == newline ) {
                skippedLines += 1;
                indentForLine[atLine - skippedLines + 1] = currentIndent;
                kDebug() << "Indent for line" << atLine - skippedLines + 1 << " : " << currentIndent;
                currentIndent = 0;
            }
            else if ( c.isSpace() ) {
                currentIndent += 1;
            }
            else {
                // reset if non-space, so we don't count whitespaces within the line
                currentIndent = 0;
            }
            if ( skippedLines > ( skipLinesBack + 2 ) ) {
                break;
            }
        }
        kDebug() << indentForLine << skipLinesBack << skippedLines << "Previous ends at: " << previousEndsAtLine  << "- 1";
        
        // if the indents match, use the context which was found.
        // if those are still "invalid", then the scanner has not reached them, meaning it aborted scanning because
        // even a match would not have meant that the context has to be replaced
        if (   previousEndsAtLine-1 != atLine && ( indentForLine[previousEndsAtLine - 2] != invalid ) && 
             ( indentForLine[atLine] != invalid ) && ( indentForLine[previousEndsAtLine - 2] == indentForLine[atLine] ) ) {
            kDebug() << "Indents match, replacing context by" << currentlyChecked;
            context = DUContextPointer(currentlyChecked);
            m_duContext = context;
            DUChainReadLocker lock(DUChain::lock()); // TODO remove debug
            kDebug() << "New context: " << context->scopeIdentifier().toString() << context->range().castToSimpleRange();
        }
        else {
            kDebug() << "Indents mismatch, so the given context is correct.";
        }
    }

        
    QRegExp importsub("(.*)\n[\\s]*from(.*)import[\\s]*$");
    importsub.setMinimal(true);
    bool is_importSub = importsub.exactMatch(currentLine);
    QRegExp importsub2("(.*)\n[\\s]*(from(.*)|import(.*))\\.$");
    importsub2.setMinimal(true);
    bool is_importSub2 = importsub2.exactMatch(currentLine);
    if ( is_importSub || is_importSub2 ) {
        QStringList for_module_match;
        if ( is_importSub ) for_module_match = importsub.capturedTexts();
        else for_module_match = importsub2.capturedTexts();
        
        kDebug() << for_module_match;
        
        QString for_module;
        if ( is_importSub ) for_module = for_module_match.last().replace(" ", "");
        else for_module = for_module_match[3].replace(" ", "");
            
        kDebug() << "Matching against module name: " << for_module_match;
        m_operation = PythonCodeCompletionContext::ImportSubCompletion;
        m_subForModule = for_module;
        kDebug() << "submodule: " << for_module;
        return;
    }
    
    QRegExp newStatementCompletion("(.*)\n[\\s]*$");
    newStatementCompletion.setMinimal(true);
    bool isNewStatementCompletion = newStatementCompletion.exactMatch(currentLine);
    if ( isNewStatementCompletion ) {
        m_operation = PythonCodeCompletionContext::NewStatementCompletion;
        return;
    }
    
    QRegExp importfile("(.*)\n[\\s]*import[\\s]*$");
    importfile.setMinimal(true);
    bool is_importfile = importfile.exactMatch(currentLine);
    QRegExp fromimport("(.*)\n[\\s]*from[\\s]*$");
    fromimport.setMinimal(true);
    bool is_fromimport = fromimport.exactMatch(currentLine);
    if ( is_importfile || is_fromimport ) {
        kDebug() << "Autocompletion type: import completion";
        m_operation = PythonCodeCompletionContext::ImportFileCompletion;
        return;
    }
    
    QString line = currentLine.replace(QRegExp("\"(.*)\""), "\"S\""); // we don't need strings, cut them out
    // go back the current line, and kill everything except an eventual AttributeAccessAst
    // there's two cases in which the search will stop: a space without a dot (for "while foo.bar.")
    // or an unmatched left parenthesis (for "foo(bar.baz.").
    int i = line.length() - 1;
    bool is_attributeAccess = false;
    bool atEnd = true;
    bool previousWasSpace = false;
    QChar c;
    QChar colon('.'); QChar lbrace('('); QChar rbrace(')'); QChar lbracket('['); QChar rbracket(']'); QChar ldic('{'); QChar rdic('}');
    QList<QChar> openingBrackets; QList<QChar> closingBrackets;
    openingBrackets << lbrace << lbracket << ldic;
    closingBrackets << rbrace << rbracket << rdic;
    QChar searchingForMatching('!');
    QChar invalid('!');
    QString scanned = "";
    while ( i > 0 ) {
        c = line.at(i);
        scanned.insert(0, c);
        if ( atEnd && ! c.isSpace() ) {
            if ( c == colon ) is_attributeAccess = true;
            else is_attributeAccess = false;
            atEnd = false;
        }
        if ( searchingForMatching != invalid && c == searchingForMatching ) {
            kDebug() << "Found matching " << c << "token";
            searchingForMatching = invalid;
        }
        else if ( closingBrackets.contains(c) ) {
            kDebug() << "Searching for opening " << c << "token";
            searchingForMatching = openingBrackets.at(closingBrackets.indexOf(c));
        }
        else if ( openingBrackets.contains(c) ) {
            scanned[0] = ' ';
            break;
        }
        if ( previousWasSpace && ! c.isSpace() && c != colon ) {
            kDebug() << "Previous char was space, current is no colon -- break";
            scanned[0] = ' ';
            break;
        }
        if ( c.isSpace() ) previousWasSpace = true;
        i -= 1;
    }
    if ( is_attributeAccess ) {
        m_guessTypeOfExpression = '\n' + scanned;
        // remove spaces at the beginning of the expression, they are treated as an INDENT token by the parser
        // and are thus a syntax error; also remove trailing dot
        m_guessTypeOfExpression.replace(QRegExp("\n[\\s]*"), "").replace(QRegExp("\\.[\\s]*$"), "");
        kDebug() << "Guess type of this expression: " << m_guessTypeOfExpression;
        m_operation = PythonCodeCompletionContext::MemberAccessCompletion;
        return;
    }
    
    if ( context->type() == DUContext::Class ) {
        QRegExp defcompletion("(.*)\n([\\s]*)(def)[\\s]*$");
        defcompletion.setMinimal(true);
        bool is_defcompletion = defcompletion.exactMatch(currentLine);
        if ( is_defcompletion ) {
            m_indent = defcompletion.capturedTexts().at(2);
            m_operation = PythonCodeCompletionContext::DefineCompletion;
            return;
        }
    }
    
    QRegExp nocompletion("(.*)\n[\\s]*(class|def)[\\s]*$");
    nocompletion.setMinimal(true);
    bool is_nocompletion = nocompletion.exactMatch(currentLine);
    if ( is_nocompletion ) {
        m_operation = PythonCodeCompletionContext::NoCompletion;
        return;
    }
    
    QRegExp memberaccess("");
    kDebug() << "Is import file: " << is_importfile;
//     Q_ASSERT(false);
}

PythonCodeCompletionContext::~PythonCodeCompletionContext()
{
    m_keepalive.clear();
}


}
