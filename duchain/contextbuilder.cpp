/*****************************************************************************
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 * Copyright 2007 Andreas Pakulat <apaku@gmx.de>                           *
 * Copyright 2010-2011 Sven Brauch <svenbrauch@googlemail.com>               *
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
#include <ktexteditor/smartrange.h>
#include <ktexteditor/smartinterface.h>
#include <ktexteditor/document.h>

#include <language/duchain/ducontext.h>
#include <language/duchain/declaration.h>
#include <language/duchain/duchainlock.h>
#include <language/duchain/topducontext.h>
#include <language/duchain/parsingenvironment.h>
#include <language/backgroundparser/backgroundparser.h>
#include <language/editor/rangeinrevision.h>
#include <language/editor/cursorinrevision.h>
#include <interfaces/icore.h>
#include <interfaces/idocumentcontroller.h>
#include <interfaces/ilanguagecontroller.h>
#include <interfaces/iprojectcontroller.h>
#include <interfaces/iproject.h>
#include <project/projectmodel.h>

#include <KStandardDirs>

#include "pythonlanguagesupport.h"
#include "pythoneditorintegrator.h"
#include "dumpchain.h"
#include "usebuilder.h"
#include "contextbuilder.h"
#include "pythonducontext.h"
#include "pythonparsejob.h"
#include "declarationbuilder.h"
#include "helpers.h"

using namespace KDevelop;

using namespace KTextEditor;

namespace Python
{

ContextBuilder::ContextBuilder() : m_indentInformationCache(0)
{

}

ReferencedTopDUContext ContextBuilder::build(const IndexedString& url, Ast* node, ReferencedTopDUContext updateContext)
{
    if (!updateContext) {
        DUChainReadLocker lock(DUChain::lock());
        updateContext = DUChain::self()->chainForDocument(url);
        if ( updateContext ) {
            Q_ASSERT(updateContext->type() == DUContext::Global);
        }
    }
    if (updateContext) {
        qDebug() << " ====> DUCHAIN ====>     rebuilding duchain for" << url.str() << "(was built before)";
        DUChainWriteLocker lock(DUChain::lock());
        Q_ASSERT(updateContext->type() == DUContext::Global);
        updateContext->clearImportedParentContexts();
        updateContext->parsingEnvironmentFile()->clearModificationRevisions();
        updateContext->clearProblems();
    } else {
        qDebug() << " ====> DUCHAIN ====>     building duchain for" << url.str();
    }
    m_isScheduledForReparsing = false;
    return ContextBuilderBase::build(url, node, updateContext);
}

PythonEditorIntegrator* ContextBuilder::editor() const
{
    return m_editor;
}

IndexedString ContextBuilder::currentlyParsedDocument() const
{
    return m_currentlyParsedDocument;
}

RangeInRevision ContextBuilder::rangeForNode(Ast* node, bool moveRight)
{
    return RangeInRevision(node->startLine, node->startCol, node->endLine, node->endCol + (int) moveRight);
}

RangeInRevision ContextBuilder::rangeForNode(Identifier* node, bool moveRight)
{
    return rangeForNode(static_cast<Ast*>(node), moveRight);
}

SimpleRange ContextBuilder::simpleRangeForNode(Ast* node, bool moveRight)
{
    return SimpleRange(node->startLine, node->startCol, node->endLine, node->endCol + (int) moveRight);
}

TopDUContext* ContextBuilder::newTopContext(const RangeInRevision& range, ParsingEnvironmentFile* file) 
{
    IndexedString currentDocumentUrl = currentlyParsedDocument();
    if ( !file ) {
        file = new ParsingEnvironmentFile(currentDocumentUrl);
        file->setLanguage(IndexedString("python"));
    }
    TopDUContext* top = new PythonTopDUContext(currentDocumentUrl, range, file);
    ReferencedTopDUContext ref(top);
    m_topContext = ref;
    return top;
}

DUContext* ContextBuilder::newContext(const RangeInRevision& range)
{
    return new PythonNormalDUContext(range, currentContext());
}

void ContextBuilder::setEditor(PythonEditorIntegrator* editor)
{
    m_editor = editor;
}

void ContextBuilder::startVisiting(Ast* node)
{
    visitNode(node);
}

void ContextBuilder::setContextOnNode(Ast* node, DUContext* context)
{
    node->context = context;
}

DUContext* ContextBuilder::contextFromNode(Ast* node)
{
    return node->context;
}

RangeInRevision ContextBuilder::editorFindRange(Ast* fromNode, Ast* toNode)
{
    return editor()->findRange(fromNode, toNode);
}

CursorInRevision ContextBuilder::editorFindPositionSafe(Ast* node) {
    if ( not node ) {
        return CursorInRevision::invalid();
    }
    return editor()->findPosition(node);
}

CursorInRevision ContextBuilder::startPos( Ast* node )
{
    return m_editor->findPosition(node, PythonEditorIntegrator::FrontEdge);
}

QualifiedIdentifier ContextBuilder::identifierForNode( Python::Identifier* node )
{
    return QualifiedIdentifier(node->value);
}

void ContextBuilder::addImportedContexts()
{
    if ( compilingContexts() && !m_importedParentContexts.isEmpty() )
    {
        DUChainWriteLocker lock( DUChain::lock() );
        foreach( DUContext* imported, m_importedParentContexts )
            currentContext()->addImportedParentContext( imported );

        m_importedParentContexts.clear();
    }
}

void ContextBuilder::closeAlreadyOpenedContext(DUContextPointer context)
{
    Q_ASSERT(currentContext() == context.data());
    while ( ! m_temporarilyClosedContexts.isEmpty() ) {
        openContext(m_temporarilyClosedContexts.last().data());
        m_temporarilyClosedContexts.removeLast();
    }
}

void ContextBuilder::activateAlreadyOpenedContext(DUContextPointer context)
{
    Q_ASSERT(m_temporarilyClosedContexts.isEmpty());
    Q_ASSERT(contextAlreayOpen(context));
    DUContext* current = currentContext();
    bool reallyCompilingContexts = compilingContexts();
    setCompilingContexts(false); // TODO this is very hackish.
    while ( current ) {
        if ( current == context.data() ) {
            setCompilingContexts(reallyCompilingContexts);
            return;
        }
        m_temporarilyClosedContexts.append(DUContextPointer(current));
        closeContext();
        current = currentContext();
    }
    setCompilingContexts(reallyCompilingContexts);
}

bool ContextBuilder::contextAlreayOpen(DUContextPointer context)
{
    DUContext* current = currentContext();
    while ( current ) {
        if ( context.data() == current ) return true;
        current = current->parentContext();
    }
    return false;
}

void ContextBuilder::visitListComprehension(ListComprehensionAst* node)
{
    visitComprehensionCommon(node);
}

void ContextBuilder::visitDictionaryComprehension(DictionaryComprehensionAst* node)
{
    visitComprehensionCommon(node);
}

void ContextBuilder::visitGeneratorExpression(GeneratorExpressionAst* node)
{
    visitComprehensionCommon(node);
}

RangeInRevision ContextBuilder::comprehensionRange(Ast* node)
{
    return editorFindRange(node, node);
}

void ContextBuilder::visitComprehensionCommon(Ast* node)
{
    RangeInRevision range = comprehensionRange(node);
    Q_ASSERT(range.isValid());
    if ( range.isValid() ) {
        range.start.column -= 1;
        DUChainWriteLocker lock(DUChain::lock());
        openContext(node, RangeInRevision(range.start, range.end), KDevelop::DUContext::Other);
//         currentContext()->setLocalScopeIdentifier(QualifiedIdentifier("<generator>"));
        lock.unlock();
        if ( node->astType == Ast::DictionaryComprehensionAstType )
            Python::AstDefaultVisitor::visitDictionaryComprehension(static_cast<DictionaryComprehensionAst*>(node));
        if ( node->astType == Ast::ListComprehensionAstType )
            Python::AstDefaultVisitor::visitListComprehension(static_cast<ListComprehensionAst*>(node));
        if ( node->astType == Ast::GeneratorExpressionAstType )
            Python::AstDefaultVisitor::visitGeneratorExpression(static_cast<GeneratorExpressionAst*>(node));
        if ( node->astType == Ast::SetComprehensionAstType )
            Python::AstDefaultVisitor::visitSetComprehension(static_cast<SetComprehensionAst*>(node));
        lock.lock();
        closeContext();
    }
}

void ContextBuilder::openContextForStatementList( const QList<Ast*>& l, DUContext::ContextType /*type*/)
{
    if ( l.count() > 0 ) {
        Ast* first = l.first();
        Ast* last = l.last();
        Q_ASSERT(first->hasUsefulRangeInformation); // TODO remove this
        RangeInRevision range(RangeInRevision(first->startLine - 1, first->startCol, last->endLine + 1, 10000));
        openContext(first, range, DUContext::Other );
        addImportedContexts();
        visitNodeList( l );
        closeContext();
    }
}

void ContextBuilder::openContextForClassDefinition(ClassDefinitionAst* node)
{
    // make sure the contexts ends at the next DEDENT token, not at the last statement.
    // also, make the context begin *after* the parent list and class name.
    int endLine = editor()->indent()->nextChange(node->endLine, FileIndentInformation::Dedent);
    CursorInRevision start = CursorInRevision(node->body.first()->startLine, node->body.first()->startCol);
    if ( start.line > node->startLine ) {
        start = CursorInRevision(node->startLine + 1, 0);
    }
    RangeInRevision range(start, CursorInRevision(endLine + 1, 0));
    DUChainWriteLocker lock;
    openContext(node, range, DUContext::Class, node->name);
    currentContext()->setLocalScopeIdentifier(identifierForNode(node->name));
    lock.unlock();
    addImportedContexts();
}

void ContextBuilder::visitClassDefinition( ClassDefinitionAst* node )
{
    openContextForClassDefinition(node);
    Python::AstDefaultVisitor::visitClassDefinition(node);
    closeContext();
}

void ContextBuilder::visitCode(CodeAst* node) {
    KUrl doc_url = KUrl(Helper::getDocumentationFile());
    IndexedString doc = IndexedString(doc_url.path());
    Q_ASSERT(currentlyParsedDocument().toUrl().isValid());
    if ( currentlyParsedDocument() != doc ) {
        // Search for the python built-in functions file, and dump its contents into the current file.
        TopDUContext* internal = 0;
        {
            DUChainReadLocker lock(DUChain::lock());
            internal = DUChain::self()->chainForDocument(doc); // TODO add startup-check and error message, this must exist
        }
        
        if ( ! internal ) {
            // If the built-in functions file is not yet parsed, schedule it with a high priority and abort.
            m_unresolvedImports.append(doc_url);
            KDevelop::ICore::self()->languageController()->backgroundParser()
                                   ->addDocument(doc, KDevelop::TopDUContext::ForceUpdate,
                                                 BackgroundParser::BestPriority, 0, ParseJob::FullSequentialProcessing);
            // This must NOT be called from parse threads! It's only meant to be used from the foreground thread, and will
            // cause thread starvation if called from here.
            // KDevelop::ICore::self()->languageController()->backgroundParser()->parseDocuments();
            return;
        }
        else {
            DUChainWriteLocker wlock(DUChain::lock());
            currentContext()->addImportedParentContext(internal);
            m_builtinFunctionsContext = TopDUContextPointer(internal);
        }
    }
    AstDefaultVisitor::visitCode(node);
}

QPair<KUrl, QStringList> ContextBuilder::findModulePath(const QString& name)
{
    QStringList nameComponents = name.split(".");
    QList<KUrl> searchPaths;
    if ( name.startsWith('.') ) {
        // This is used for "from .foo import" or similar (relative imports)
        nameComponents.removeFirst();
        searchPaths << currentlyParsedDocument().toUrl().directory();
    }
    else {
        // If this is not a relative import, use the project directory,
        // the current directory, and all system include paths.
        searchPaths = Helper::getSearchPaths(currentlyParsedDocument().toUrl());
    }
    // Loop over all the name components, and find matching folders or files.
    KUrl tmp;
    QStringList leftNameComponents;
    foreach ( KUrl currentPath, searchPaths ) {
        tmp = currentPath;
        leftNameComponents = nameComponents;
        foreach ( QString component, nameComponents ) {
            if ( component == "*" ) {
                // For "from ... import *", if "..." is a directory, use the "__init__.py" file
                component = "__init__";
            }
            else {
                // only empty the list if not importing *, this is convenient later on
                leftNameComponents.removeFirst();
            }
            QString testFilename = tmp.path(KUrl::AddTrailingSlash) + component;
            KUrl sourceUrl = testFilename + ".py";
            // we can only parse those, so we don't care about anything else for now.
            // Any C modules (.so, .dll) will be ignored, and highlighted as "not found". TODO fix this
            QFile sourcefile(testFilename + ".py");
            QFileInfo sourcedir(testFilename);
            tmp.cd(component);
            kDebug() << testFilename << "exists: [file/dir]" << sourcefile.exists() << sourcedir.exists();
            if ( ! sourcedir.exists() || ! sourcedir.isDir() || leftNameComponents.isEmpty() ) {
                // If the search cannot continue further down into a hierarchy of directories,
                // the file matching the next name component will be returned,
                // toegether with a list of names which must be resolved inside that file.
                if ( sourcefile.exists() ) {
                    sourceUrl.cleanPath();
                    return QPair<KUrl, QStringList>(sourceUrl, leftNameComponents);
                }
                else if ( sourcedir.exists() && sourcedir.isDir() ) {
                    KUrl path(testFilename + "/__init__.py");
                    path.cleanPath();
                    return QPair<KUrl, QStringList>(path, leftNameComponents);
                }
                kDebug() << "RESULT:" << "No module path found.";
                break;
            }
        }
    }
    return QPair<KUrl, QStringList>(KUrl(), QStringList());
}

void ContextBuilder::visitLambda(LambdaAst* node)
{
    // Lambda functions need their own context for parameters
    DUChainWriteLocker lock(DUChain::lock());
    openContext(node, editorFindRange(node, node->body), DUContext::Other);
    lock.unlock();
    Python::AstDefaultVisitor::visitLambda(node);
    lock.lock();
    closeContext();
}

RangeInRevision ContextBuilder::rangeForArgumentsContext(FunctionDefinitionAst* node)
{
    // The python parser has extra syntax features for *args and **kwargs. 
    // We need to know where the function arguments context ends (the location of the closing ")" paren would
    // be optimal), so this does some pretty ugly checks whether the * or ** arguments are present,
    // and adjusts the range as needed.
    RangeInRevision range;
    CursorInRevision start, end;
    if ( node->arguments->arguments.count() ) {
        Ast* first = node->arguments->arguments.first();
        start = CursorInRevision(first->startLine, first->startCol);
    }
    else if ( node->arguments->vararg )
        start = CursorInRevision(node->arguments->vararg_lineno, node->arguments->vararg_col_offset);
    else if ( node->arguments->kwarg ) 
        start = CursorInRevision(node->arguments->arg_lineno, node->arguments->arg_col_offset);
    
    if ( node->arguments->kwarg )
        end = CursorInRevision(node->arguments->arg_lineno, node->arguments->arg_col_offset + node->arguments->kwarg->value.length() + 1);
    else if ( node->arguments->vararg )
        end = CursorInRevision(node->arguments->vararg_lineno, node->arguments->vararg_col_offset + node->arguments->vararg->value.length() + 1);
    else if ( node->arguments->arguments.count() ) {
        Ast* last = node->arguments->arguments.last();
        end = CursorInRevision(last->endLine, last->endCol + 1);
    }
    
    if ( node->arguments->arguments.isEmpty() && ! node->arguments->kwarg && ! node->arguments->vararg ) {
        start = CursorInRevision(node->startLine, node->startCol + node->name->value.length());
        end = start;
    }
    
    range = RangeInRevision(start, end);
    Q_ASSERT(range.isValid());
    return range;
}

void ContextBuilder::visitFunctionArguments(FunctionDefinitionAst* node)
{
    RangeInRevision range = rangeForArgumentsContext(node);
    
    // The DUChain expects the context containing a function's arguments to be of type Function.
    // The function body will have DUContext::Other as type, as it contains only code.
    DUContext* funcctx = openContext(node->arguments, range, DUContext::Function, node->name);
    kDebug() << funcctx;
    visitNode(node->arguments);
    closeContext();
    // the parameters should be visible in the function body, so import that context there
    m_importedParentContexts.append(funcctx);
    m_mostRecentArgumentsContext = DUContextPointer(funcctx);
}

void ContextBuilder::visitFunctionDefinition(FunctionDefinitionAst* node)
{
    DUChainWriteLocker lock(DUChain::lock());
    visitNodeList(node->decorators);
    visitFunctionArguments(node);
    visitFunctionBody(node);
}

void ContextBuilder::visitFunctionBody(FunctionDefinitionAst* node)
{
    // The function should end at the next DEDENT token, not at the body's last statement
    int endLine = node->endLine;
    if ( node->endLine != node->startLine ) {
        endLine = editor()->indent()->nextChange(endLine, FileIndentInformation::Dedent);
    }
    CursorInRevision end = CursorInRevision(endLine, node->startLine == node->endLine ? INT_MAX : 0);
    CursorInRevision start = rangeForArgumentsContext(node).end;
    if ( start.line < node->body.first()->startLine ) {
        start = CursorInRevision(node->startLine + 1, 0);
    }
    RangeInRevision range(start, end);
    
    // Open the context for the function body (the list of statements)
    // It's of type Other, as it contains only code
    openContext(node, range, DUContext::Other, identifierForNode(node->name));
    currentContext()->setLocalScopeIdentifier(identifierForNode(node->name));
    // import the parameters into the function body
    addImportedContexts();
    
    visitNodeList(node->body);
    
    closeContext();
    m_mostRecentArgumentsContext = DUContextPointer(0);
}

}
