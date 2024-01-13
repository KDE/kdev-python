/*
    SPDX-FileCopyrightText: 2007 Piyush verma <piyush.verma@gmail.com>
    SPDX-FileCopyrightText: 2007 Andreas Pakulat <apaku@gmx.de>
    SPDX-FileCopyrightText: 2010-2013 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#include "pythonlanguagesupport.h"
#include "pythoneditorintegrator.h"
#include "dumpchain.h"
#include "usebuilder.h"
#include "contextbuilder.h"
#include "pythonducontext.h"
#include "pythonparsejob.h"
#include "declarationbuilder.h"
#include "helpers.h"
#include "duchaindebug.h"

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

using namespace KDevelop;

using namespace KTextEditor;

namespace Python
{

ReferencedTopDUContext ContextBuilder::build(const IndexedString& url, Ast* node,
                                             const ReferencedTopDUContext& updateContext_)
{
    ReferencedTopDUContext updateContext(updateContext_);
    if (!updateContext) {
        DUChainReadLocker lock(DUChain::lock());
        updateContext = DUChain::self()->chainForDocument(url);
        if ( updateContext ) {
            Q_ASSERT(updateContext->type() == DUContext::Global);
        }
    }
    if (updateContext) {
        qCDebug(KDEV_PYTHON_DUCHAIN) << " ====> DUCHAIN ====>     rebuilding duchain for" << url.str() << "(was built before)";
        DUChainWriteLocker lock(DUChain::lock());
        Q_ASSERT(updateContext->type() == DUContext::Global);
        updateContext->clearImportedParentContexts();
        updateContext->parsingEnvironmentFile()->clearModificationRevisions();
        updateContext->clearProblems();
    } else {
        qCDebug(KDEV_PYTHON_DUCHAIN) << " ====> DUCHAIN ====>     building duchain for" << url.str();
    }
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

void ContextBuilder::setCurrentlyParsedDocument(const IndexedString &document)
{
    m_currentlyParsedDocument = document;
}

void ContextBuilder::setFutureModificationRevision(const ModificationRevision &rev)
{
    m_futureModificationRevision = rev;
}

RangeInRevision ContextBuilder::rangeForNode(Ast* node, bool moveRight)
{
    return RangeInRevision(node->startLine, node->startCol, node->endLine, node->endCol + (int) moveRight);
}

RangeInRevision ContextBuilder::rangeForNode(Identifier* node, bool moveRight)
{
    return rangeForNode(static_cast<Ast*>(node), moveRight);
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

void ContextBuilder::addUnresolvedImport(const IndexedString &module)
{
    m_unresolvedImports.append(module);
}

QList<IndexedString> ContextBuilder::unresolvedImports() const
{
    return m_unresolvedImports;
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
    if ( !node ) {
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
        for ( DUContext* imported : m_importedParentContexts )
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
    Q_ASSERT(contextAlreadyOpen(context));
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

bool ContextBuilder::contextAlreadyOpen(DUContextPointer context)
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
    RangeInRevision range = editorFindRange(node, node);
    return range;
}

void ContextBuilder::visitComprehensionCommon(Ast* node)
{
    RangeInRevision range = comprehensionRange(node);
    Q_ASSERT(range.isValid());
    if ( range.isValid() ) {
        DUChainWriteLocker lock;
        openContext(node, range, KDevelop::DUContext::Other);
        qCDebug(KDEV_PYTHON_DUCHAIN) << "creating comprehension context" << node << range;
        Q_ASSERT(currentContext());
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

void ContextBuilder::openContextForClassDefinition(ClassDefinitionAst* node)
{
    // make sure the contexts ends at the next DEDENT token, not at the last statement.
    // also, make the context begin *after* the parent list and class name.
    int endLine = editor()->indent()->nextChange(node->endLine, FileIndentInformation::Dedent);
    CursorInRevision start = CursorInRevision(node->body.first()->startLine, node->body.first()->startCol);
    if ( start.line > node->startLine ) {
        start = CursorInRevision(node->startLine + 1, 0);
    }
    RangeInRevision range(start, CursorInRevision(endLine, 0));
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
    IndexedString doc = Helper::getDocumentationFile();
    Q_ASSERT(currentlyParsedDocument().toUrl().isValid());
    if ( currentlyParsedDocument() != doc ) {
        // Search for the python built-in functions file, and dump its contents into the current file.
        auto internal = Helper::getDocumentationFileContext();
        if ( ! internal ) {
            // If the built-in functions file is not yet parsed, schedule it with a high priority.
            m_unresolvedImports.append(doc);
            KDevelop::ICore::self()->languageController()->backgroundParser()
                                   ->addDocument(doc, KDevelop::TopDUContext::ForceUpdate,
                                                 BackgroundParser::BestPriority*2, nullptr, ParseJob::FullSequentialProcessing);
            // This must NOT be called from parse threads! It's only meant to be used from the foreground thread, and will
            // cause thread starvation if called from here.
            // KDevelop::ICore::self()->languageController()->backgroundParser()->parseDocuments();
        }
        else {
            DUChainWriteLocker wlock;
            currentContext()->addImportedParentContext(internal);
        }
    }
    AstDefaultVisitor::visitCode(node);
}

QPair<QUrl, QStringList> ContextBuilder::findModulePath(const QString& name, const QUrl& currentDocument)
{
    QStringList nameComponents = name.split(".");
    QVector<QUrl> searchPaths;
    if ( name.startsWith('.') ) {
        /* To take care for imports like "from ....xxxx.yyy import zzz"
         * we need to take current doc path and run "cd .." enough times
         */
        nameComponents.removeFirst();
        QString tname = name.mid(1); // remove first dot
        QDir curPathDir = QDir(currentDocument.adjusted(QUrl::RemoveFilename).toLocalFile());
        for (QString c : tname) {
            if (c != ".")
                break;
            curPathDir.cdUp();
            nameComponents.removeFirst();
        }
        searchPaths << QUrl::fromLocalFile(curPathDir.path());
    }
    else {
        // If this is not a relative import, use the project directory,
        // the current directory, and all system include paths.
        // FIXME: If absolute imports enabled, don't add curently parsed doc path
        searchPaths = Helper::getSearchPaths(currentDocument);
    }
    // Loop over all the name components, and find matching folders or files.
    QDir tmp;
    QStringList leftNameComponents;
    for ( const QUrl& currentPath : searchPaths ) {
        tmp.setPath(currentPath.toLocalFile());
        leftNameComponents = nameComponents;
        for ( QString component : nameComponents ) {
            if ( component == "*" ) {
                // For "from ... import *", if "..." is a directory, use the "__init__.py" file
                component = QStringLiteral("__init__");
            }
            else {
                // only empty the list if not importing *, this is convenient later on
                leftNameComponents.removeFirst();
            }
            QString testFilename = tmp.path() + "/" + component;

            bool can_continue = tmp.cd(component);
            QFileInfo sourcedir(testFilename);
            const bool dir_exists = sourcedir.exists() && sourcedir.isDir();

            // we can only parse those, so we don't care about anything else for now.
            // Any C modules (.so, .dll) will be ignored, and highlighted as "not found". TODO fix this
            static QStringList valid_extensions{".py", ".pyx"};
            for ( const auto& extension : valid_extensions ) {
                QFile sourcefile(testFilename + extension);
                if ( ! dir_exists || leftNameComponents.isEmpty() ) {
                    // If the search cannot continue further down into a hierarchy of directories,
                    // the file matching the next name component will be returned,
                    // toegether with a list of names which must be resolved inside that file.
                    if ( sourcefile.exists() ) {
                        auto sourceUrl = QUrl::fromLocalFile(testFilename + extension);
                        // TODO QUrl: cleanPath?
                        return qMakePair(sourceUrl, leftNameComponents);
                    }
                    else if ( dir_exists ) {
                        auto path = QUrl::fromLocalFile(testFilename + "/__init__.py");
                        // TODO QUrl: cleanPath?
                        return qMakePair(path, leftNameComponents);
                    }
                }
            }
            if ( ! can_continue ) {
                // if not returned yet and the cd into the next component failed,
                // abort and try the next search path.
                break;
            }
        }
    }
    return {};
}

void ContextBuilder::visitLambda(LambdaAst* node)
{
    openContext(node, editorFindRange(node, node->body), DUContext::Other);
    AstDefaultVisitor::visitLambda(node);
    closeContext();
}

RangeInRevision ContextBuilder::rangeForArgumentsContext(FunctionDefinitionAst* node)
{
    auto start = node->name->range().end();
    auto end = start;
    auto args = node->arguments;
    if ( args->kwarg ) {
        end = args->kwarg->range().end();
    }
    else if ( args->vararg &&
         ( args->arguments.isEmpty() ||
           ! args->vararg->appearsBefore(args->arguments.last())) ) {
        end = args->vararg->range().end();
    }
    else if ( ! args->arguments.isEmpty() ) {
        end = args->arguments.last()->range().end();
    }

    if ( ! args->defaultValues.isEmpty() ) {
        end = qMax<KTextEditor::Cursor>(args->defaultValues.last()->range().end(), end);
    }

    RangeInRevision range(start.line(), start.column(), end.line(), end.column());
    range.start.column += 1; // Don't include end of name.
    range.end.column += 1; // Include end parenthesis (unless spaces...)
    return range;
}

void ContextBuilder::visitFunctionArguments(FunctionDefinitionAst* node)
{
    RangeInRevision range = rangeForArgumentsContext(node);

    // The DUChain expects the context containing a function's arguments to be of type Function.
    // The function body will have DUContext::Other as type, as it contains only code.
    DUContext* funcctx = openContext(node->arguments, range, DUContext::Function, node->name);
    AstDefaultVisitor::visitArguments(node->arguments);
    visitArguments(node->arguments);
    closeContext();
    // the parameters should be visible in the function body, so import that context there
    m_importedParentContexts.append(funcctx);
}

void ContextBuilder::visitFunctionDefinition(FunctionDefinitionAst* node)
{
    visitNodeList(node->decorators);
    visitNode(node->returns);
    visitFunctionArguments(node);
    visitFunctionBody(node);
}

void ContextBuilder::visitFunctionBody(FunctionDefinitionAst* node)
{
    // The function should end at the next DEDENT token, not at the body's last statement
    int endLine = node->endLine;
    if ( ! node->body.isEmpty() ) {
        endLine = node->body.last()->startLine;
    }
    if ( node->endLine != node->startLine ) {
        endLine = editor()->indent()->nextChange(endLine, FileIndentInformation::Dedent);
        if ( ! node->body.isEmpty() ) {
            endLine = qMax<int>(endLine, node->body.last()->endLine + 1);
        }
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
    {
        DUChainWriteLocker lock;
        currentContext()->setLocalScopeIdentifier(identifierForNode(node->name));
    }
    // import the parameters into the function body
    addImportedContexts();
    
    visitNodeList(node->body);
    
    closeContext();
}

}
