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

#include <language/duchain/duchainlock.h>
#include <language/duchain/topducontext.h>
#include <language/duchain/parsingenvironment.h>
#include <language/editor/rangeinrevision.h>
#include <interfaces/foregroundlock.h>
#include <interfaces/icore.h>
#include <interfaces/idocumentcontroller.h>
#include <interfaces/iprojectcontroller.h>
#include <interfaces/iproject.h>
#include <project/projectmodel.h>

#include "pythoneditorintegrator.h"
#include "dumpchain.h"
#include "usebuilder.h"
#include "contextbuilder.h"
#include "pythonducontext.h"
#include "codecompletion/pythoncodecompletioncontext.h"
#include "pythonparsejob.h"
#include "declarationbuilder.h"
#include "parser/parserConfig.h"
#include "helpers.h"
#include <pythonlanguagesupport.h>
#include <interfaces/ilanguagecontroller.h>
#include <language/backgroundparser/backgroundparser.h>

using namespace KDevelop;

using namespace KTextEditor;

Python::PythonEditorIntegrator* Python::ContextBuilder::m_editor;

namespace Python
{
    
TopDUContext* ParseJob::m_internalFunctions;

ReferencedTopDUContext ContextBuilder::build(const IndexedString& url, Ast* node, ReferencedTopDUContext updateContext)
{
    if (!updateContext) {
        DUChainReadLocker lock(DUChain::lock());
        updateContext = DUChain::self()->chainForDocument(url);
    }
    if (updateContext) {
        qDebug() << "re-compiling" << url.str();
        qDebug() << "*******************************************";
        DUChainWriteLocker lock(DUChain::lock());
        updateContext->clearImportedParentContexts();
        updateContext->parsingEnvironmentFile()->clearModificationRevisions();
        updateContext->clearProblems();
    } else {
        kDebug() << "compiling" << url.str();
//         DUChain::self()->updateContextForUrl(currentlyParsedDocument(), TopDUContext::AllDeclarationsContextsAndUses, 0, 5);
    }
    m_isScheduledForReparsing = false;
    return ContextBuilderBase::build(url, node, updateContext);
}

PythonEditorIntegrator* ContextBuilder::editor() const
{
    return ContextBuilder::m_editor;
}

IndexedString ContextBuilder::currentlyParsedDocument() const
{
    return m_currentlyParsedDocument;
}

TopDUContext* ContextBuilder::newTopContext(const RangeInRevision& range, ParsingEnvironmentFile* file) 
{
    IndexedString currentDocumentUrl = ContextBuilder::m_editor->parseSession()->currentDocument();
    kDebug() << currentDocumentUrl.str();
    
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
    //m_identifierCompiler = new IdentifierCompiler(editor->parseSession());
    ContextBuilder::m_editor = editor;
}

void ContextBuilder::setEditor(ParseSession* /*session*/)
{
    PythonEditorIntegrator* e = new PythonEditorIntegrator(/*session*/);
    //m_identifierCompiler = new IdentifierCompiler(e->parseSession());
    setEditor(e);
}

void ContextBuilder::startVisiting( Ast* node )
{
    visitNode( node );
}

void ContextBuilder::setContextOnNode( Ast* node, DUContext* context )
{
    node->context = context;
}

DUContext* ContextBuilder::contextFromNode( Ast* node )
{
    return node->context;
}

RangeInRevision ContextBuilder::editorFindRange( Ast* fromNode, Ast* toNode )
{
    return editor()->findRange(fromNode, toNode);
}

CursorInRevision ContextBuilder::startPos( Ast* node )
{
    return m_editor->findPosition(node, PythonEditorIntegrator::FrontEdge);
}

QualifiedIdentifier ContextBuilder::identifierForNode( Python::Identifier* node )
{
    return QualifiedIdentifier( node->value );
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
    while ( current ) {
        if ( current == context.data() ) {
            return;
        }
        m_temporarilyClosedContexts.append(DUContextPointer(current));
        closeContext();
        current = currentContext();
    }
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

void ContextBuilder::openContextForStatementList( const QList<Ast*>& l, DUContext::ContextType /*type*/)
{
    if ( l.count() > 0 )
    {
        Ast* first = l.first();
        Ast* last = l.last();
        Q_ASSERT(first->hasUsefulRangeInformation); // TODO remove this
        RangeInRevision range(RangeInRevision(first->startLine - 1, first->startCol, last->endLine + 1, 10000));
        DUContext* rangectx = openContext(first, range, DUContext::Other );
        kDebug() << " +++ opening context (stmlist): " << range.castToSimpleRange();
        addImportedContexts();
        visitNodeList( l );
        closeContext();
        kDebug() << " --- closed context (stmlist): line " << rangectx->range().castToSimpleRange();
    }
}

void ContextBuilder::openContextForClassDefinition(ClassDefinitionAst* node)
{
    RangeInRevision range(node->startLine, node->startCol, node->body.last()->endLine + 1, 0);
    DUChainWriteLocker lock(DUChain::lock());
    openContext( node, range, DUContext::Class, node->name);
    currentContext()->setLocalScopeIdentifier(identifierForNode(node->name));
    lock.unlock();
    kDebug() << " +++ opening CLASS context: " << range.castToSimpleRange() << node->name;
    addImportedContexts();
}

void ContextBuilder::visitClassDefinition( ClassDefinitionAst* node )
{
    openContextForClassDefinition(node);
    Python::AstDefaultVisitor::visitClassDefinition(node);
    closeContext();
}

void ContextBuilder::visitCode(CodeAst* node) {
    KUrl doc_url = KUrl(DOCFILE_PATH);
    doc_url.cleanPath(KUrl::SimplifyDirSeparators);
    IndexedString doc = IndexedString(doc_url.path());
    Q_ASSERT(currentlyParsedDocument().toUrl().isValid());
    kDebug() << "Internal functions file: " << currentlyParsedDocument().toUrl().path() << doc.toUrl().path();
    if ( currentlyParsedDocument() != doc ) {
        TopDUContext* internal;
        {
            DUChainReadLocker lock(DUChain::lock());
            internal = DUChain::self()->chainForDocument(doc); // TODO add startup-check and error message, this must exist
            // ICore::languageController()->backgroundParser()->parseJobForDocument();
        }
        
        if ( ! internal ) {
            m_hasUnresolvedImports = true;
            DUChain::self()->updateContextForUrl(doc, TopDUContext::AllDeclarationsContextsAndUses);
        }
        else {
            kDebug() << "Adding builtin function context...";
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
    QList<KUrl> searchPaths = Helper::getSearchPaths(currentlyParsedDocument().toUrl());
    KUrl tmp;
    QStringList leftNameComponents;
    QString dirFound("<invalid>");
    foreach ( KUrl currentPath, searchPaths ) {
        tmp = currentPath;
        leftNameComponents = nameComponents;
        foreach ( QString component, nameComponents ) {
            leftNameComponents.removeFirst();
            QString testFilename = tmp.path(KUrl::AddTrailingSlash) + component;
            kDebug() << testFilename;
            KUrl sourceUrl = testFilename + ".py";
            QFile sourcefile(testFilename + ".py"); // we can only parse those, so we don't care about anything else for now.
            QFileInfo sourcedir(testFilename);
            if ( sourcefile.exists() ) {
                return QPair<KUrl, QStringList>(sourceUrl, leftNameComponents);
            }
            else if ( sourcedir.exists() && sourcedir.isDir() ) {
                return QPair<KUrl, QStringList>(KUrl(testFilename.append("/__init__.py")), leftNameComponents);
            }
            bool can_continue = tmp.cd(component);
            if ( ! can_continue ) {
                break;
            }
        }
    }
    return QPair<KUrl, QStringList>(KUrl(), QStringList());
}

void ContextBuilder::scheduleForReparsing() {
    if ( ! m_isScheduledForReparsing ) {
        DUChain::self()->updateContextForUrl(document(), TopDUContext::AllDeclarationsContextsAndUses, 0, 5);
    }
}

void ContextBuilder::visitImport(ImportAst* node)
{
    foreach ( AliasAst* name, node->names ) {
        // for "import ... as", use the as thingy, use the module name otherwise
        Identifier* moduleName = name->asName ? name->asName : name->name;
        
        QPair<KUrl, QStringList> moduleFilePath = findModulePath(name->name->value);
        kDebug() << "Module path: " << moduleFilePath.first.path();
        if ( ! moduleFilePath.first.isValid() || ! QFileInfo(moduleFilePath.first.path()).exists() ) {
            kWarning() << "Malformed or nonexistent path, skipping";
            continue;
        }
        ReferencedTopDUContext moduleChain;
        
        moduleFilePath.first.cleanPath(KUrl::SimplifyDirSeparators);
        IndexedString doc = IndexedString(moduleFilePath.first.path());
        {
            DUChainReadLocker lock(DUChain::lock());
            moduleChain = DUChain::self()->chainForDocument(doc);
        }
        
        bool featuresSatisfied = false;
        if ( moduleChain.data() ) {
            if ( moduleChain->features() >= TopDUContext::AllDeclarationsContextsAndUses ) featuresSatisfied = true;
        }
        kDebug() << "Chain: " << moduleChain.data() << ";" << "Features satisfied: " << featuresSatisfied;
        if ( ! featuresSatisfied ) {
            m_hasUnresolvedImports = true;
            DUChain::self()->updateContextForUrl(doc, TopDUContext::AllDeclarationsContextsAndUses);
        }
        else {
            contextsForModules.insert(moduleName->value, moduleChain);
            kDebug() << moduleFilePath.first.path();
            kDebug() << "Added " << name->name->value << " to the module chain map" << moduleChain.data();
        }
    }
    Python::AstDefaultVisitor::visitImport(node);
}

void ContextBuilder::visitFunctionArguments(FunctionDefinitionAst* node)
{
    if ( node->arguments && node->arguments->arguments.count() ) {
        int sline, eline, scol, ecol;
        sline = node->arguments->arguments.first()->startLine;
        scol = node->arguments->arguments.first()->startCol;
        eline = node->arguments->arguments.last()->endLine;
        ecol = node->arguments->arguments.last()->endCol;
        RangeInRevision range(sline, scol, eline, ecol);
        
        Q_ASSERT(range.isValid());
        DUContext* funcctx = openContext( node->arguments, range, DUContext::Function, node->name);
        kDebug() << funcctx;
        kDebug() << " +++ opening FUNCTION ARGUMENTS context: " << funcctx->range().castToSimpleRange();
        visitNode(node->arguments);
        closeContext();
        m_importedParentContexts.append( funcctx );
    }
}

void ContextBuilder::visitFunctionDefinition(FunctionDefinitionAst* node)
{
    kDebug() << " Building function definition context: " << node->name->value;
    DUChainWriteLocker lock(DUChain::lock());
    
    visitNodeList( node->decorators );
    
    visitFunctionArguments(node);
    
    visitFunctionBody(node);
}

void ContextBuilder::visitFunctionBody(FunctionDefinitionAst* node)
{
    RangeInRevision range(RangeInRevision(node->startLine, node->startCol, node->endLine + 1, 0));
    // Done building the function declaration, start building the body now
    DUContext* ctx = openContext(node, range, DUContext::Function, identifierForNode( node->name ) );
    currentContext()->setLocalScopeIdentifier(identifierForNode(node->name));
    kDebug() << " +++ opening context (function definition): " << range.castToSimpleRange();
    kDebug() << currentContext()->type() << DUContext::Function;
    addImportedContexts();
    
    visitNodeList(node->body);
    
    closeContext();
    kDebug() << " --- closed context (function definition): " << ctx->range().castToSimpleRange();
}

void ContextBuilder::visitWith( WithAst * node )
{
    m_importedParentContexts = QList<DUContext*>() << openContext( node->contextExpression, DUContext::Other );
    kDebug() << " +++ opening context: " << node->startLine - 1 << ":" << node->startCol << " -- " << node->endLine + 1 << "inf";
    visitNode( node->contextExpression );
    closeContext();

    openContextForStatementList( node->body );
    m_importedParentContexts.clear();
}

}
