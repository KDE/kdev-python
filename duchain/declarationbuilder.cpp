/*
    SPDX-FileCopyrightText: 2007 Piyush verma <piyush.verma@gmail.com>
    SPDX-FileCopyrightText: 2007 Andreas Pakulat <apaku@gmx.de>
    SPDX-FileCopyrightText: 2010-2016 Sven Brauch <svenbrauch@googlemail.com>
    SPDX-FileCopyrightText: 2016 Francis Herne <mail@flherne.uk>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#include "declarationbuilder.h"
#include "duchain/declarations/functiondeclaration.h"

#include "types/hintedtype.h"
#include "types/unsuretype.h"
#include "types/nonetype.h"
#include "types/indexedcontainer.h"
#include "contextbuilder.h"
#include "expressionvisitor.h"
#include "pythoneditorintegrator.h"
#include "helpers.h"
#include "assistants/missingincludeassistant.h"
#include "correctionhelper.h"

#include <language/duchain/classdeclaration.h>
#include <language/duchain/functiondeclaration.h>
#include <language/duchain/declaration.h>
#include <language/duchain/duchain.h>
#include <language/duchain/types/alltypes.h>
#include <language/duchain/builders/abstracttypebuilder.h>
#include <language/duchain/aliasdeclaration.h>
#include <language/duchain/duchainutils.h>
#include <language/backgroundparser/backgroundparser.h>
#include <language/backgroundparser/parsejob.h>
#include <interfaces/ilanguagecontroller.h>

#include <QByteArray>
#include <QtGlobal>

#include <QDebug>
#include "duchaindebug.h"

#include <functional>

using namespace KTextEditor;
using namespace KDevelop;

namespace Python
{

DeclarationBuilder::DeclarationBuilder(Python::PythonEditorIntegrator* editor, int ownPriority)
    : DeclarationBuilderBase()
    , m_ownPriority(ownPriority)
{
    setEditor(editor);
}

DeclarationBuilder:: ~DeclarationBuilder()
{
    if ( ! m_scheduledForDeletion.isEmpty() ) {
        DUChainWriteLocker lock;
        for ( DUChainBase* d : m_scheduledForDeletion ) {
            delete d;
        }
        m_scheduledForDeletion.clear();
    }
}

void DeclarationBuilder::setPrebuilding(bool prebuilding)
{
    m_prebuilding = prebuilding;
}

ReferencedTopDUContext DeclarationBuilder::build(const IndexedString& url, Ast* node,
                                                 const ReferencedTopDUContext& updateContext_)
{
    ReferencedTopDUContext updateContext(updateContext_);
    m_correctionHelper.reset(new CorrectionHelper(url, this));

    // The declaration builder needs to run twice, so it can resolve uses of e.g. functions
    // which are called before they are defined (which is easily possible, due to python's dynamic nature).
    if ( ! m_prebuilding ) {
        DeclarationBuilder* prebuilder = new DeclarationBuilder(editor(), m_ownPriority);
        prebuilder->m_currentlyParsedDocument = currentlyParsedDocument();
        prebuilder->setPrebuilding(true);
        prebuilder->m_futureModificationRevision = m_futureModificationRevision;
        updateContext = prebuilder->build(url, node, updateContext);
        delete prebuilder;
        qCDebug(KDEV_PYTHON_DUCHAIN) << "Second declarationbuilder pass";
    }
    else {
        qCDebug(KDEV_PYTHON_DUCHAIN) << "Prebuilding declarations";
    }
    return DeclarationBuilderBase::build(url, node, updateContext);
}

int DeclarationBuilder::jobPriority() const
{
    return m_ownPriority;
}

void DeclarationBuilder::closeDeclaration()
{
    if ( lastContext() ) {
        DUChainReadLocker lock(DUChain::lock());
        currentDeclaration()->setKind(Declaration::Type);
    }
    
    Q_ASSERT(currentDeclaration()->alwaysForceDirect());

    eventuallyAssignInternalContext();

    DeclarationBuilderBase::closeDeclaration();
}

template<typename T> T* DeclarationBuilder::eventuallyReopenDeclaration(Identifier* name, FitDeclarationType mustFitType)
{
    QList<Declaration*> existingDeclarations = existingDeclarationsForNode(name);

    Declaration* dec = nullptr;
    reopenFittingDeclaration<T>(existingDeclarations, mustFitType, editorFindRange(name, name), &dec);
    bool declarationOpened = (bool) dec;
    if ( ! declarationOpened ) {
        dec = openDeclaration<T>(name);
    }
    Q_ASSERT(dynamic_cast<T*>(dec));
    return static_cast<T*>(dec);
}

template<typename T> T* DeclarationBuilder::visitVariableDeclaration(Ast* node, Declaration* previous,
                                                                     AbstractType::Ptr type, VisitVariableFlags flags)
{
    if ( node->astType == Ast::NameAstType ) {
        NameAst* currentVariableDefinition = static_cast<NameAst*>(node);
        // those contexts can invoke a variable declaration
        // this prevents "bar" from being declared in something like "foo = bar"
        // This is just a sanity check, the code should never request creation of a variable
        // in such cases.
        if ( currentVariableDefinition->context != ExpressionAst::Context::Store ) {
            return nullptr;
        }
        return visitVariableDeclaration<T>(currentVariableDefinition->identifier, previous, type, flags);
    }
    else if ( node->astType == Ast::IdentifierAstType ) {
        return visitVariableDeclaration<T>(static_cast<Identifier*>(node), previous, type, flags);
    }
    else {
        qCWarning(KDEV_PYTHON_DUCHAIN) << "cannot create variable declaration for non-(name|identifier) AST, this is a programming error";
        return static_cast<T*>(nullptr);
    }
}

QList< Declaration* > DeclarationBuilder::existingDeclarationsForNode(Identifier* node)
{
    return currentContext()->findDeclarations(
        identifierForNode(node).last(), CursorInRevision::invalid(), nullptr,
        (DUContext::SearchFlag) (DUContext::DontSearchInParent | DUContext::DontResolveAliases)
    );
}

DeclarationBuilder::FitDeclarationType DeclarationBuilder::kindForType(AbstractType::Ptr type, bool isAlias)
{
    if ( type ) {
        if ( type->whichType() == AbstractType::TypeFunction ) {
            return FunctionDeclarationType;
        }
    }
    if ( isAlias ) {
        return AliasDeclarationType;
    }
    return InstanceDeclarationType;
}

template<typename T> QList<Declaration*> DeclarationBuilder::reopenFittingDeclaration(
    QList<Declaration*> declarations, FitDeclarationType mustFitType,
    RangeInRevision updateRangeTo, Declaration** ok )
{
    // Search for a declaration from a previous parse pass which should be re-used
    QList<Declaration*> remainingDeclarations;
    *ok = nullptr;
    for ( Declaration* d : declarations ) {
        Declaration* fitting = dynamic_cast<T*>(d);
        if ( ! fitting ) {
            // Only use a declaration if the type matches
            qCDebug(KDEV_PYTHON_DUCHAIN) << "skipping" << d->toString() << "which could not be cast to the requested type";
            continue;
        }
        // Do not use declarations which have been encountered previously;
        // this function only handles declarations from previous parser passes which have not
        // been encountered yet in this pass
        bool reallyEncountered = wasEncountered(d) && ! m_scheduledForDeletion.contains(d);
        bool invalidType = false;
        if ( d->abstractType() && mustFitType != NoTypeRequired ) {
            invalidType = ( ( d->isFunctionDeclaration() ) != ( mustFitType == FunctionDeclarationType ) );
            if ( ! invalidType ) {
                invalidType = ( ( dynamic_cast<AliasDeclaration*>(d) != nullptr ) != ( mustFitType == AliasDeclarationType ) );
            }
        }
        if ( fitting && ! reallyEncountered && ! invalidType ) {
            if ( d->topContext() == currentContext()->topContext() ) {
                openDeclarationInternal(d);
                d->setRange(updateRangeTo);
                *ok = d;
                setEncountered(d);
                break;
            }
            else {
                qCDebug(KDEV_PYTHON_DUCHAIN) << "Not opening previously existing declaration because it's in another top context";
            }
        }
        else if ( ! invalidType ) {
            remainingDeclarations << d;
        }
    }
    return remainingDeclarations;
}

template<typename T> T* DeclarationBuilder::visitVariableDeclaration(Identifier* node, Declaration* previous,
                                                                     AbstractType::Ptr type, VisitVariableFlags flags)
{
    DUChainWriteLocker lock;
    RangeInRevision range = editorFindRange(node, node);
    // ask the correction file library if there's a user-specified type for this object
    if ( AbstractType::Ptr hint = m_correctionHelper->hintForLocal(node->value) ) {
        type = hint;
    }

    // If no type is known, display "mixed".
    if ( ! type ) {
        type = AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed));
    }
    
    QList<Declaration*> existingDeclarations;
    if ( previous ) {
        existingDeclarations << previous;
    }
    else {
        // declarations declared at an earlier range in this top-context
        existingDeclarations = existingDeclarationsForNode(node);
    }
    
    // declaration existing in a previous version of this top-context
    Declaration* dec = nullptr;
    existingDeclarations = reopenFittingDeclaration<T>(existingDeclarations, kindForType(type), range, &dec);
    bool declarationOpened = (bool) dec;
    if ( flags & AbortIfReopenMismatch && previous && ! declarationOpened ) {
        return nullptr;
    }
    
    // tells whether the declaration found for updating is in the same top context
    bool inSameTopContext = true;
    // tells whether there's fitting declarations to update (update is not the same as re-open! one is for
    // code which uses the same variable twice, the other is for multiple passes of the parser)
    bool haveFittingDeclaration = false;
    if ( ! existingDeclarations.isEmpty() && existingDeclarations.last() ) {
        Declaration* d = Helper::resolveAliasDeclaration(existingDeclarations.last());
        DUChainReadLocker lock;
        if ( d && d->topContext() != topContext() ) {
            inSameTopContext = false;
        }
        if ( dynamic_cast<T*>(existingDeclarations.last()) ) {
            haveFittingDeclaration = true;
        }
    }
    if ( currentContext() && currentContext()->type() == DUContext::Class && ! haveFittingDeclaration ) {
        // If the current context is a class, then this is a class member variable.
        if ( ! dec ) {
            dec = openDeclaration<ClassMemberDeclaration>(node);
            Q_ASSERT(! declarationOpened);
            declarationOpened = true;
        }
        if ( declarationOpened ) {
            DeclarationBuilderBase::closeDeclaration();
        }
        dec->setType(AbstractType::Ptr(type));
        dec->setKind(KDevelop::Declaration::Instance);
    } else if ( ! haveFittingDeclaration ) {
        // This name did not previously appear in the user code, so a new variable is declared
        // check whether a declaration from a previous parser pass must be updated
        if ( ! dec ) {
            dec = openDeclaration<T>(node);
            Q_ASSERT(! declarationOpened);
            declarationOpened = true;
        }
        if ( declarationOpened ) {
            DeclarationBuilderBase::closeDeclaration();
        }
        
        AbstractType::Ptr newType;
        if ( currentContext()->type() == DUContext::Function ) {
            // check for argument type hints (those are created when calling functions)
            AbstractType::Ptr hints = Helper::extractTypeHints(dec->abstractType());
            if ( hints.dynamicCast<IndexedContainer>() || hints.dynamicCast<ListType>() ) {
                // This only happens when the type hint is a tuple, which means the vararg/kwarg of a function is being processed.
                newType = hints;
            }
            else {
                newType = Helper::mergeTypes(hints, type);
            }
        }
        else {
            newType = type;
        }
        dec->setType(newType);
        dec->setKind(KDevelop::Declaration::Instance);
    }
    else if ( inSameTopContext ) {
        // The name appeared previously in the user code, so no new variable is declared, but just
        // the type is modified accordingly.
        dec = existingDeclarations.last();
        AbstractType::Ptr currentType = dec->abstractType();
        AbstractType::Ptr newType = type;
        if ( newType ) {
            if ( currentType && currentType->indexed() != newType->indexed() ) {
                // If the previous and new type are different, use an unsure type
                dec->setType(Helper::mergeTypes(currentType, newType));
            }
            else {
                // If no type was set previously, use only the new one.
                dec->setType(AbstractType::Ptr(type));
            }
        }
    }

    T* result = dynamic_cast<T*>(dec);
    if ( ! result ) qCWarning(KDEV_PYTHON_DUCHAIN) << "variable declaration does not have the expected type";
    return result;
}

void DeclarationBuilder::visitCode(CodeAst* node)
{
    Q_ASSERT(currentlyParsedDocument().toUrl().isValid());
    m_unresolvedImports.clear();
    DeclarationBuilderBase::visitCode(node);
}

void DeclarationBuilder::visitExceptionHandler(ExceptionHandlerAst* node)
{
    if ( node->name ) {
        // Python allows to assign the caught exception to a variable; create that variable if required.
        ExpressionVisitor v(currentContext());
        v.visitNode(node->type);
        visitVariableDeclaration<Declaration>(node->name, nullptr, v.lastType());
    }
    DeclarationBuilderBase::visitExceptionHandler(node);
}

void DeclarationBuilder::visitWithItem(WithItemAst* node)
{
    if ( node->optionalVars ) {
        // For statements like "with open(f) as x", a new variable must be created; do this here.
        ExpressionVisitor v(currentContext());
        v.visitNode(node->contextExpression);
        auto mgrType = v.lastType();
        auto enterType = mgrType; // If we can't find __enter__(), assume it returns `self` like file objects.

        static const IndexedIdentifier enterId(KDevelop::Identifier("__enter__"));

        DUChainReadLocker lock;
        if ( auto enterFunc = dynamic_cast<FunctionDeclaration*>(
                Helper::accessAttribute(mgrType, enterId, topContext()))) {
            if ( auto enterFuncType = enterFunc->type<FunctionType>() ) {
                enterType = enterFuncType->returnType();
            }
        }
        lock.unlock();
        // This may be any assignable expression, e.g. `with foo() as bar[3]: ...`
        assignToUnknown(node->optionalVars, enterType);
    }
    Python::AstDefaultVisitor::visitWithItem(node);
}

void DeclarationBuilder::visitFor(ForAst* node)
{
    if ( node->iterator ) {
        ExpressionVisitor v(currentContext());
        v.visitNode(node->iterator);
        assignToUnknown(node->target, Helper::contentOfIterable(v.lastType(), topContext()));
    }
    Python::ContextBuilder::visitFor(node);
}

Declaration* DeclarationBuilder::findDeclarationInContext(QStringList dottedNameIdentifier, TopDUContext* ctx) const
{
    DUChainReadLocker lock(DUChain::lock());
    DUContext* currentContext = ctx;
    // TODO make this a bit faster, it wastes time
    Declaration* lastAccessedDeclaration = nullptr;
    int i = 0;
    int identifierCount = dottedNameIdentifier.length();
    for ( const QString& currentIdentifier : dottedNameIdentifier ) {
        Q_ASSERT(currentContext);
        i++;
        QList<Declaration*> declarations = currentContext->findDeclarations(QualifiedIdentifier(currentIdentifier).first(),
                                                                            CursorInRevision::invalid(), nullptr, DUContext::NoFiltering);
        // break if the list of identifiers is not yet totally worked through and no
        // declaration with an internal context was found
        if ( declarations.isEmpty() || ( !declarations.last()->internalContext() && identifierCount != i ) ) {
            qCDebug(KDEV_PYTHON_DUCHAIN) << "Declaration not found: " << dottedNameIdentifier << "in top context" << ctx->url().toUrl().path();
            return nullptr;
        }
        else {
            lastAccessedDeclaration = declarations.last();
            currentContext = lastAccessedDeclaration->internalContext();
        }
    }
    return lastAccessedDeclaration;
}

QString DeclarationBuilder::buildModuleNameFromNode(ImportFromAst* node, AliasAst* alias, const QString& intermediate) const
{
    QString moduleName = alias->name->value;
    if ( ! intermediate.isEmpty() ) {
        moduleName.prepend('.').prepend(intermediate);
    }
    if ( node->module ) {
        moduleName.prepend('.').prepend(node->module->value);
    }
    // To handle relative imports correctly, add node level in the beginning of the path
    // This will allow findModulePath to deduce module search direcotry properly
    moduleName.prepend(QString(node->level, '.'));
    return moduleName;
}

void DeclarationBuilder::visitImportFrom(ImportFromAst* node)
{
    Python::AstDefaultVisitor::visitImportFrom(node);
    QString moduleName;
    QString declarationName;
    for ( AliasAst* name : node->names ) {
        // iterate over all the names that are imported, like "from foo import bar as baz, bang as asdf"
        Identifier* declarationIdentifier = nullptr;
        declarationName.clear();
        if ( name->asName ) {
            // use either the alias ("as foo"), or the object name itself if no "as" is given
            declarationIdentifier = name->asName;
            declarationName = name->asName->value;
        }
        else {
            declarationIdentifier = name->name;
            declarationName = name->name->value;
        }
        // This is a bit hackish, it tries to find the specified object twice twice -- once it tries to
        // import the name from a module's __init__.py file, and once from a "real" python file
        // TODO improve this code-wise
        ProblemPointer problem(nullptr);
        QString intermediate;
        moduleName = buildModuleNameFromNode(node, name, intermediate);
        Declaration* success = createModuleImportDeclaration(moduleName, declarationName, declarationIdentifier, problem);
        if ( ! success && (node->module || node->level) ) {
            ProblemPointer problem_init(nullptr);
            intermediate = QString("__init__");
            moduleName = buildModuleNameFromNode(node, name, intermediate);
            success = createModuleImportDeclaration(moduleName, declarationName, declarationIdentifier, problem_init);
        }
        if ( ! success && problem ) {
            DUChainWriteLocker lock;
            topContext()->addProblem(problem);
        }
    }
}

void DeclarationBuilder::visitComprehension(ComprehensionAst* node)
{
    Python::AstDefaultVisitor::visitComprehension(node);
    ExpressionVisitor v(currentContext());
    v.visitNode(node->iterator);
    assignToUnknown(node->target, Helper::contentOfIterable(v.lastType(), topContext()));
}

void DeclarationBuilder::visitImport(ImportAst* node)
{
    Python::ContextBuilder::visitImport(node);
    DUChainWriteLocker lock;
    for ( AliasAst* name : node->names ) {
        QString moduleName = name->name->value;
        // use alias if available, name otherwise
        Identifier* declarationIdentifier = name->asName ? name->asName : name->name;
        ProblemPointer problem(nullptr);
        createModuleImportDeclaration(moduleName, declarationIdentifier->value, declarationIdentifier, problem);
        if ( problem ) {
            DUChainWriteLocker lock;
            topContext()->addProblem(problem);
        }
    }
}

void DeclarationBuilder::scheduleForDeletion(DUChainBase* d, bool doschedule)
{
    if ( doschedule ) {
        m_scheduledForDeletion.append(d);
    }
    else {
        m_scheduledForDeletion.removeAll(d);
    }
}


Declaration* DeclarationBuilder::createDeclarationTree(const QStringList& nameComponents, Identifier* declarationIdentifier,
                                       const ReferencedTopDUContext& innerCtx, Declaration* aliasDeclaration,
                                       const RangeInRevision& range)
{
    // This actually handles two use cases which are very similar -- thus this check:
    // There might be either one declaration which should be imported from another module,
    // or there might be a whole context. In "import foo.bar", the "bar" might be either
    // a single class/function/whatever, or a whole file to import.
    // NOTE: The former case can't actually happen in python, it's not allowed. However,
    // it is still handled here, because it's very useful for documentation files (pyQt for example
    // makes heavy use of that feature).
    Q_ASSERT( ( innerCtx.data() || aliasDeclaration ) && "exactly one of innerCtx or aliasDeclaration must be provided");
    Q_ASSERT( ( !innerCtx.data() || !aliasDeclaration ) && "exactly one of innerCtx or aliasDeclaration must be provided");
    
    qCDebug(KDEV_PYTHON_DUCHAIN) << "creating declaration tree for" << nameComponents;
    
    Declaration* lastDeclaration = nullptr;
    int depth = 0;
    
    // check for already existing trees to update
    for ( int i = nameComponents.length() - 1; i >= 0; i-- ) {
        QStringList currentName;
        for ( int j = 0; j < i; j++ ) {
            currentName.append(nameComponents.at(j));
        }
        lastDeclaration = findDeclarationInContext(currentName, topContext());
        if ( lastDeclaration && (!range.isValid() || lastDeclaration->range() < range) ) {
            depth = i;
            break;
        }
    }
    
    DUContext* extendingPreviousImportCtx = nullptr;
    QStringList remainingNameComponents;
    bool injectingContext = false;
    if ( lastDeclaration && lastDeclaration->internalContext() ) {
        qCDebug(KDEV_PYTHON_DUCHAIN) << "Found existing import statement while creating declaration for " << declarationIdentifier->value;
        for ( int i = depth; i < nameComponents.length(); i++ ) {
            remainingNameComponents.append(nameComponents.at(i));
        }
        extendingPreviousImportCtx = lastDeclaration->internalContext();
        injectContext(extendingPreviousImportCtx);
        injectingContext = true;
        qCDebug(KDEV_PYTHON_DUCHAIN) << "remaining identifiers:" << remainingNameComponents;
    }
    else {
        remainingNameComponents = nameComponents;
        extendingPreviousImportCtx = topContext();
    }
    
    // now, proceed in creating the declaration tree with whatever context
    QList<Declaration*> openedDeclarations;
    QList<StructureType::Ptr> openedTypes;
    QList<DUContext*> openedContexts;
    
    RangeInRevision displayRange = RangeInRevision::invalid();
    
    DUChainWriteLocker lock;
    for ( int i = 0; i < remainingNameComponents.length(); i++ ) {
        // Iterate over all the names, and create a declaration + sub-context for each of them
        const QString& component = remainingNameComponents.at(i);
        Identifier temporaryIdentifier(component);
        Declaration* d = nullptr;
        temporaryIdentifier.copyRange(declarationIdentifier);
        temporaryIdentifier.endCol = temporaryIdentifier.startCol;
        temporaryIdentifier.startCol += 1;
        displayRange = editorFindRange(&temporaryIdentifier, &temporaryIdentifier); // TODO fixme
        
        bool done = false;
        if ( aliasDeclaration && i == remainingNameComponents.length() - 1 ) {
            // it's the last level, so if we have an alias declaration create it and stop
            if (    aliasDeclaration->isFunctionDeclaration() 
                 || dynamic_cast<ClassDeclaration*>(aliasDeclaration) 
                 || dynamic_cast<AliasDeclaration*>(aliasDeclaration) 
               ) {
                aliasDeclaration = Helper::resolveAliasDeclaration(aliasDeclaration);
                AliasDeclaration* adecl = eventuallyReopenDeclaration<AliasDeclaration>(&temporaryIdentifier,
                                                                                        AliasDeclarationType);
                if ( adecl ) {
                    adecl->setAliasedDeclaration(aliasDeclaration);
                }
                d = adecl;
                closeDeclaration();
            }
            else {
                d = visitVariableDeclaration<Declaration>(&temporaryIdentifier);
                d->setAbstractType(aliasDeclaration->abstractType());
            }
            openedDeclarations.append(d);
            done = true;
        }
        
        if ( ! done ) {
            // create the next level of the tree hierarchy if not done yet.
            d = visitVariableDeclaration<Declaration>(&temporaryIdentifier);
        }
        if ( d ) {
            if ( topContext() != currentContext() ) {
                d->setRange(RangeInRevision(currentContext()->range().start, currentContext()->range().start));
            }
            else {
                d->setRange(displayRange);
            }
            d->setAutoDeclaration(true);
            currentContext()->createUse(d->ownIndex(), d->range());
            qCDebug(KDEV_PYTHON_DUCHAIN) << "really encountered:" << d << "; scheduled:" << m_scheduledForDeletion;
            qCDebug(KDEV_PYTHON_DUCHAIN) << d->toString();
            scheduleForDeletion(d, false);
            qCDebug(KDEV_PYTHON_DUCHAIN) << "scheduled:" << m_scheduledForDeletion;
        }
        if ( done ) break;

        qCDebug(KDEV_PYTHON_DUCHAIN) << "creating context for " << component;

        // otherwise, create a new "level" entry (a pseudo type + context + declaration which contains all imported items)
        StructureType::Ptr moduleType = StructureType::Ptr(new StructureType());
        openType(moduleType);

        // the identifier is needed so the context does not get re-opened if
        // more contexts are opened for other files with the same range
        Python::Identifier contextIdentifier(component);
        auto moduleContext = openContext(declarationIdentifier, KDevelop::DUContext::Other, &contextIdentifier);
        openedContexts.append(moduleContext);

        for ( Declaration* local : currentContext()->localDeclarations() ) {
            // keep all the declarations until the builder finished
            // kdevelop would otherwise delete them as soon as the context is closed
            if ( ! wasEncountered(local) ) {
                setEncountered(local);
                scheduleForDeletion(local, true);
            }
        }

        openedDeclarations.append(d);
        openedTypes.append(moduleType);
        if ( i == remainingNameComponents.length() - 1 ) {
            if ( innerCtx ) {
                qCDebug(KDEV_PYTHON_DUCHAIN) << "adding imported context to inner declaration";
                currentContext()->addImportedParentContext(innerCtx);
            }
            else if ( aliasDeclaration ) {
                qCDebug(KDEV_PYTHON_DUCHAIN) << "setting alias declaration on inner declaration";
            }
        }
    }
    for ( int i = openedContexts.length() - 1; i >= 0; i-- ) {
        // Close all the declarations and contexts opened previosly, and assign the types.
        qCDebug(KDEV_PYTHON_DUCHAIN) << "closing context";
        closeType();
        closeContext();
        auto d = openedDeclarations.at(i);
        // because no context will be opened for an alias declaration, this will not happen if there's one
        if ( d ) {
            openedTypes[i]->setDeclaration(d);
            d->setType(openedTypes.at(i));
            d->setInternalContext(openedContexts.at(i));
        }
    }
    
    if ( injectingContext ) {
        closeInjectedContext();
    }
    
    if ( ! openedDeclarations.isEmpty() ) {
        // return the lowest-level element in the tree, for the caller to do stuff with
        return openedDeclarations.last();
    }
    else return nullptr;
}

Declaration* DeclarationBuilder::createModuleImportDeclaration(QString moduleName, QString declarationName,
                                                               Identifier* declarationIdentifier,
                                                               ProblemPointer& problemEncountered, Ast* rangeNode)
{
    // Search the disk for a python file which contains the requested declaration
    auto moduleInfo = findModulePath(moduleName, currentlyParsedDocument().toUrl());
    RangeInRevision range(RangeInRevision::invalid());
    if ( rangeNode ) {
        range = rangeForNode(rangeNode, false);
    }
    else {
        range = rangeForNode(declarationIdentifier, false);
    }
    Q_ASSERT(range.isValid());
    
    qCDebug(KDEV_PYTHON_DUCHAIN) << "Found module path [path/path in file]: " << moduleInfo;
    qCDebug(KDEV_PYTHON_DUCHAIN) << "Declaration identifier:" << declarationIdentifier->value;
    DUChainWriteLocker lock;
    const IndexedString modulePath = IndexedString(moduleInfo.first);
    ReferencedTopDUContext moduleContext = DUChain::self()->chainForDocument(modulePath);
    lock.unlock();
    Declaration* resultingDeclaration = nullptr;
    if ( ! moduleInfo.first.isValid() ) {
        // The file was not found -- this is either an error in the user's code,
        // a missing module, or a C module (.so) which is unreadable for kdevelop
        // TODO imrpove error handling in case the module exists as a shared object or .pyc file only
        qCDebug(KDEV_PYTHON_DUCHAIN) << "invalid or non-existent URL:" << moduleInfo;
        KDevelop::Problem *p = new Python::MissingIncludeProblem(moduleName, currentlyParsedDocument());
        p->setFinalLocation(DocumentRange(currentlyParsedDocument(), range.castToSimpleRange()));
        p->setSource(KDevelop::IProblem::SemanticAnalysis);
        p->setSeverity(KDevelop::IProblem::Warning);
        p->setDescription(i18n("Module \"%1\" not found", moduleName));
        m_missingModules.append(IndexedString(moduleName));
        problemEncountered = p;
        return nullptr;
    }
    if ( ! moduleContext ) {
        // schedule the include file for parsing, and schedule the current one for reparsing after that is done
        qCDebug(KDEV_PYTHON_DUCHAIN) << "No module context, recompiling";
        m_unresolvedImports.append(modulePath);
        Helper::scheduleDependency(modulePath, m_ownPriority);
        // parseDocuments() must *not* be called from a background thread!
        // KDevelop::ICore::self()->languageController()->backgroundParser()->parseDocuments();
        return nullptr;
    }
    if ( moduleInfo.second.isEmpty() ) {
        // import the whole module
        resultingDeclaration = createDeclarationTree(declarationName.split("."),
                                                     declarationIdentifier, moduleContext, nullptr, range);
        auto initFile = QStringLiteral("/__init__.py");
        auto path = moduleInfo.first.path();
        if ( path.endsWith(initFile) ) {
            // if the __init__ file is imported, import all the other files in that directory as well
            QDir dir(path.left(path.size() - initFile.size()));
            dir.setNameFilters({"*.py"});
            dir.setFilter(QDir::Files);
            auto files = dir.entryList();
            for ( const auto& file : files ) {
                if ( file == QStringLiteral("__init__.py") ) {
                    continue;
                }
                const auto filePath = declarationName.split(".") << file.left(file.lastIndexOf(".py"));
                const auto fileUrl = QUrl::fromLocalFile(dir.path() + "/" + file);
                ReferencedTopDUContext fileContext;
                {
                    DUChainReadLocker lock;
                    fileContext = DUChain::self()->chainForDocument(IndexedString(fileUrl));
                }
                if ( fileContext ) {
                    Identifier id = *declarationIdentifier;
                    id.value.append(".").append(filePath.last());
                    createDeclarationTree(filePath,
                                          &id, fileContext, nullptr);
                }
                else {
                    m_unresolvedImports.append(IndexedString(fileUrl));
                    Helper::scheduleDependency(IndexedString(fileUrl), m_ownPriority);
                }
            }
        }
    }
    else {
        // import a specific declaration from the given file
        lock.lock();
        if ( declarationIdentifier->value == "*" ) {
            qCDebug(KDEV_PYTHON_DUCHAIN) << "Importing * from module";
            currentContext()->addImportedParentContext(moduleContext);
        }
        else {
            qCDebug(KDEV_PYTHON_DUCHAIN) << "Got module, importing declaration: " << moduleInfo.second;
            Declaration* originalDeclaration = findDeclarationInContext(moduleInfo.second, moduleContext);
            if ( originalDeclaration ) {
                DUChainWriteLocker lock(DUChain::lock());
                resultingDeclaration = createDeclarationTree(declarationName.split("."), declarationIdentifier,
                                                             ReferencedTopDUContext(nullptr), originalDeclaration,
                                                             editorFindRange(declarationIdentifier, declarationIdentifier));
            }
            else {
                KDevelop::Problem *p = new Python::MissingIncludeProblem(moduleName, currentlyParsedDocument());
                p->setFinalLocation(DocumentRange(currentlyParsedDocument(), range.castToSimpleRange())); // TODO ok?
                p->setSource(KDevelop::IProblem::SemanticAnalysis);
                p->setSeverity(KDevelop::IProblem::Warning);
                p->setDescription(i18n("Declaration for \"%1\" not found in specified module", moduleInfo.second.join(".")));
                problemEncountered = p;
            }
        }
    }
    return resultingDeclaration;
}

void DeclarationBuilder::visitYield(YieldAst* node)
{
    // Functions containing "yield" statements will return lists in our abstraction.
    // The content type of that list can be guessed from the yield statements.
    AstDefaultVisitor::visitYield(node);
    
    // Determine the type of the argument to "yield", like "int" in "yield 3"
    ExpressionVisitor v(currentContext());
    v.visitNode(node->value);
    AbstractType::Ptr encountered = v.lastType();
    
    // In some obscure (or wrong) cases, "yield" might appear outside of a function body,
    // so check for that here.
    if ( ! node->value || ! hasCurrentType() ) {
        return;
    }

    TypePtr<FunctionType> t = currentType<FunctionType>();
    if ( ! t ) {
        return;
    }
    if ( auto previous = t->returnType().dynamicCast<ListType>() ) {
        // If the return type of the function already is set to a list, *add* the encountered type
        // to its possible content types.
        DUChainWriteLocker lock;
        previous->addContentType<Python::UnsureType>(encountered);
        t->setReturnType(previous);
    }
    else {
        // Otherwise, create a new container type, and set it as the function's return type.
        DUChainWriteLocker lock;
        auto container = ExpressionVisitor::typeObjectForIntegralType<ListType>("list");
        if ( container ) {
            openType(container);
            container->addContentType<Python::UnsureType>(encountered);
            t->setReturnType(Helper::mergeTypes(t->returnType(), container));
            closeType();
        }
    }
}

void DeclarationBuilder::visitLambda(LambdaAst* node)
{
    DUChainWriteLocker lock;
    // A context must be opened, because the lamdba's arguments are local to the lambda:
    // d = lambda x: x*2; print x # <- gives an error
    openContext(node, editorFindRange(node, node->body), DUContext::Other);
    for ( ArgAst* argument : node->arguments->arguments ) {
        visitVariableDeclaration<Declaration>(argument->argumentName);
    }
    visitNodeList(node->arguments->defaultValues);
    if (node->arguments->vararg) {
        visitVariableDeclaration<Declaration>(node->arguments->vararg->argumentName);
    }
    if (node->arguments->kwarg) {
        visitVariableDeclaration<Declaration>(node->arguments->kwarg->argumentName);
    }
    visitNode(node->body);
    closeContext();
}

void DeclarationBuilder::applyDocstringHints(CallAst* node, FunctionDeclaration::Ptr function)
{
    ExpressionVisitor v(currentContext());
    v.visitNode(static_cast<AttributeAst*>(node->function)->value);

    // Don't do anything if the object the function is being called on is not a container.
    auto container = v.lastType().dynamicCast<ListType>();
    if ( ! container || ! function ) {
        return;
    }
    // Don't do updates to pre-defined functions.
    if ( ! v.lastDeclaration() || v.lastDeclaration()->topContext()->url() == Helper::getDocumentationFile() ) {
        return;
    }
    // Check for the different types of modifiers such a function can have
    QStringList args;
    QHash< QString, std::function<void()> > items;
    items["addsTypeOfArg"] = [&]() {
        const int offset = ! args.isEmpty() ? (int) args.at(0).toUInt() : 0;
        if ( node->arguments.length() <= offset ) {
            return;
        }
        // Check which type should be added to the list
        ExpressionVisitor argVisitor(currentContext());
        argVisitor.visitNode(node->arguments.at(offset));
        // Actually add that type
        if ( ! argVisitor.lastType() ) {
            return;
        }
        DUChainWriteLocker wlock;
        qCDebug(KDEV_PYTHON_DUCHAIN) << "Adding content type: " << argVisitor.lastType()->toString();
        container->addContentType<Python::UnsureType>(argVisitor.lastType());
        v.lastDeclaration()->setType(container);
    };
    items["addsTypeOfArgContent"] = [&]() {
        const int offset = ! args.isEmpty() ? (int) args.at(0).toUInt() : 0;
        if ( node->arguments.length() <= offset ) {
            return;
        }
        ExpressionVisitor argVisitor(currentContext());
        argVisitor.visitNode(node->arguments.at(offset));
        if ( argVisitor.lastType() ) {
            DUChainWriteLocker wlock;
            auto contentType = Helper::contentOfIterable(argVisitor.lastType(), topContext());
            container->addContentType<Python::UnsureType>(contentType);
            v.lastDeclaration()->setType(container);
        }
    };
    auto docstring = function->comment();
    if ( ! docstring.isEmpty() ) {
        for ( const auto& key : items.keys() ) {
            if ( Helper::docstringContainsHint(docstring, key, &args) ) {
                items[key]();
            }
        }
    }
}

void DeclarationBuilder::addArgumentTypeHints(CallAst* node, DeclarationPointer called)
{
    DUChainReadLocker lock;
    auto funcInfo = Helper::functionForCalled(called.data());
    auto function = funcInfo.declaration;

    if ( ! function ) {
        return;
    }
    if ( function->topContext()->url() == Helper::getDocumentationFile() ) {
        return;
    }
    // Note: within this function:
    // - 'parameters' refers to the parameters of the function definition.
    // - 'arguments' refers to the arguments of the function call.

    DUContext* parameterContext = DUChainUtils::argumentContext(function);
    FunctionType::Ptr functionType = function->type<FunctionType>();
    if ( ! parameterContext || ! functionType ) {
        return;
    }
    QVector<Declaration*> parameters = parameterContext->localDeclarations();
    if ( parameters.isEmpty() ) {
        return;
    }
    const int specialParamsCount = (function->vararg() != -1) + (function->kwarg() != -1);

    // Look for the "self" in the argument list, the type of that should not be updated.
    bool hasSelfParam = false;
    if ( ( function->context()->type() == DUContext::Class || funcInfo.isConstructor )
            && ! function->isStatic() )
    {
        // ... unless for some reason the function only has *vararg, **kwarg as parameters
        // (this could happen for example if the method is static but kdev-python does not know,
        // or if the user just made a mistake in his code)
        if ( specialParamsCount < parameters.size() ) {
            hasSelfParam = true;
        }
    }

    lock.unlock();

    bool explicitSelfArgument = false;
    if ( hasSelfParam && ! function->isClassMethod() && node->function->astType == Ast::AttributeAstType ) {
        // Calling an attribute, e.g. `instance.foo(arg)` or `MyClass.foo(instance, arg)`.
        ExpressionVisitor valueVisitor(currentContext());
        valueVisitor.visitNode(static_cast<AttributeAst*>(node->function)->value);
        if ( valueVisitor.lastDeclaration().dynamicCast<ClassDeclaration>() && valueVisitor.isAlias() ) {
            // Function is attribute of a class _type_ (not instance), so first arg is used as `self`.
            explicitSelfArgument = true;
        }
    }

    int currentParamIndex = hasSelfParam;
    int currentArgumentIndex = explicitSelfArgument;
    int indexInVararg = -1;
    int paramsAvailable = qMin(functionType->arguments().length(), parameters.size());
    int argsAvailable = node->arguments.size();
    bool atVararg = false;

    // Iterate over all the arguments, trying to guess the type of the object being
    // passed as an argument, and update the parameter accordingly.
    // Stop if more parameters supplied than possible, and we're not at the vararg.
    for ( ; ( atVararg || currentParamIndex < paramsAvailable ) && currentArgumentIndex < argsAvailable;
            currentArgumentIndex++ )
    {
        atVararg = atVararg || currentParamIndex == function->vararg(); // Not >=, nonexistent vararg is -1.

        ExpressionAst* arg = node->arguments.at(currentArgumentIndex);

        ExpressionVisitor argumentVisitor(currentContext());
        argumentVisitor.visitNode(arg);
        AbstractType::Ptr argumentType = argumentVisitor.lastType();

        // Update the parameter type: change both the type of the function argument,
        // and the type of the declaration which belongs to that argument
        HintedType::Ptr addType = HintedType::Ptr(new HintedType());
        openType(addType);
        addType->setType(argumentVisitor.lastType());
        addType->setCreatedBy(topContext(), m_futureModificationRevision);
        closeType();

        DUChainWriteLocker wlock;
        if ( atVararg ) {
            indexInVararg++;
            Declaration* parameter = parameters.at(function->vararg());
            IndexedContainer::Ptr varargContainer = parameter->type<IndexedContainer>();
            if ( ! varargContainer ) continue;
            if ( varargContainer->typesCount() > indexInVararg ) {
                AbstractType::Ptr oldType = varargContainer->typeAt(indexInVararg).abstractType();
                AbstractType::Ptr newType = Helper::mergeTypes(oldType, addType);
                varargContainer->replaceType(indexInVararg, newType);
            }
            else {
                varargContainer->addEntry(addType);
            }
            parameter->setAbstractType(varargContainer);
        }
        else {
            if ( ! argumentType ) continue;
            AbstractType::Ptr newType = Helper::mergeTypes(parameters.at(currentParamIndex)->abstractType(),
                                                           addType);
            // TODO this does not correctly update the types in quickopen! Investigate why.
            functionType->removeArgument(currentParamIndex);
            functionType->addArgument(newType, currentParamIndex);
            function->setAbstractType(functionType);
            parameters.at(currentParamIndex)->setType(newType);
            currentParamIndex++;
        }
    }

    // **kwargs is always the last parameter
    MapType::Ptr kwargsDict;
    if ( function->kwarg() != -1 ) {
        kwargsDict = parameters.last()->abstractType().dynamicCast<MapType>();
    }
    lock.unlock();
    DUChainWriteLocker wlock;
    for ( KeywordAst* keyword : node->keywords ) {
        wlock.unlock();
        ExpressionVisitor argumentVisitor(currentContext());
        argumentVisitor.visitNode(keyword->value);
        if ( ! argumentVisitor.lastType() ) {
            continue;
        }
        wlock.lock();
        bool matchedNamedParam = false;
        HintedType::Ptr addType = HintedType::Ptr(new HintedType());
        if ( keyword->argumentName ) {
            openType(addType);
            addType->setType(argumentVisitor.lastType());
            addType->setCreatedBy(topContext(), m_futureModificationRevision);
            closeType();
            for (int ip = currentParamIndex; ip < paramsAvailable; ++ip ) {
                if ( parameters.at(ip)->identifier().toString() != keyword->argumentName->value ) {
                    continue;
                }
                matchedNamedParam = true;
                auto newType = Helper::mergeTypes(parameters.at(ip)->abstractType(), addType);
                functionType->removeArgument(ip);
                functionType->addArgument(newType, ip);
                parameters.at(ip)->setType(newType);
            }
        }
        else if ( auto unpackedDict = argumentVisitor.lastType().dynamicCast<MapType>() ) {
            // 'keyword is actually an unpacked dict: `foo(**{'a': 12}).
            openType(addType);
            addType->setType(unpackedDict->contentType().abstractType());
            addType->setCreatedBy(topContext(), m_futureModificationRevision);
            closeType();
        }
        else { // Maybe the dict type wasn't loaded yet, or something else happened.
            continue;
        }
        if ( ! matchedNamedParam && kwargsDict ) {
            DUChainWriteLocker lock;
            kwargsDict->addContentType<Python::UnsureType>(addType);
            parameters.last()->setAbstractType(kwargsDict);
        }
    }
    function->setAbstractType(functionType);
}

void DeclarationBuilder::visitMatch(MatchAst* node)
{
    // What are we matching?
    ExpressionVisitor subjectVisitor(currentContext());
    subjectVisitor.visitNode(node->subject);

    for (auto* matchCase: node->cases) {
        if (!matchCase || !matchCase->pattern) {
            continue;
        }
        DUChainWriteLocker lock;
        // We only support some forms for now.
        switch (matchCase->pattern->astType) {
            case Ast::MatchSequenceAstType: {
                auto* seq = static_cast<MatchSequenceAst*>(matchCase->pattern);
                for (auto* element: seq->patterns) {
                    if (element->astType != Ast::MatchAsAstType) {
                        continue;
                    }
                    auto* asElement = static_cast<MatchAsAst*>(element);
                    auto type = Helper::contentOfIterable(subjectVisitor.lastType(), topContext());
                    visitVariableDeclaration<Declaration>(asElement->name, nullptr, type);
                }
                break;
            }

            case Ast::MatchAsAstType: {
                auto* as = static_cast<MatchAsAst*>(matchCase->pattern);
                if (!as->name) {
                    break;
                }
                visitVariableDeclaration<Declaration>(as->name, nullptr, subjectVisitor.lastType());
                break;
            }

            default:
                break;
        }
    }

    Python::AstDefaultVisitor::visitMatch(node);
}

void DeclarationBuilder::visitCall(CallAst* node)
{
    Python::AstDefaultVisitor::visitCall(node);
    // Find the function being called; this code also handles cases where non-names
    // are called, for example:
    //     class myclass():
    //         def myfun(self): return 3
    //     l = [myclass()]
    //     x = l[0].myfun() # the called object is actually l[0].myfun
    // In the above example, this call will be evaluated to "myclass.myfun" in the following statement.
    ExpressionVisitor functionVisitor(currentContext());
    functionVisitor.visitNode(node);

    if ( node->function && node->function->astType == Ast::AttributeAstType && functionVisitor.lastDeclaration() ) {
        // Some special functions, like "append", update the content of the object they operate on.
        // Find the object the function is called on, like for d = [1, 2, 3]; d.append(5), this will give "d"
        FunctionDeclaration::Ptr function = functionVisitor.lastDeclaration().dynamicCast<FunctionDeclaration>();
        applyDocstringHints(node, function);
    }
    if ( ! m_prebuilding ) {
        return;
    }

    // The following code will try to update types of function parameters based on what is passed
    // for those when the function is used.
    // In case of this code:
    //     def foo(arg): print arg
    //     foo(3)
    // the following will change the type of "arg" to be "int" when it processes the second line.
    addArgumentTypeHints(node, functionVisitor.lastDeclaration());
}

void DeclarationBuilder::assignToName(NameAst* target, const DeclarationBuilder::SourceType& element)
{
    if ( element.isAlias ) {
        DUChainWriteLocker lock;
        AliasDeclaration* decl = eventuallyReopenDeclaration<AliasDeclaration>(target->identifier, AliasDeclarationType);
        decl->setAliasedDeclaration(element.declaration.data());
        closeDeclaration();
    }
    else {
        DUChainWriteLocker lock;
        Declaration* dec = visitVariableDeclaration<Declaration>(target, nullptr, element.type);
        if ( dec && m_lastComment && ! m_lastComment->usedAsComment ) {
            dec->setComment(m_lastComment->value);
            m_lastComment->usedAsComment = true;
        }
        /** DEBUG **/
        if ( element.type && dec ) {
            Q_ASSERT(dec->abstractType());
        }
        /** END DEBUG **/
    }
}

void DeclarationBuilder::assignToSubscript(SubscriptAst* subscript, const DeclarationBuilder::SourceType& element)
{
    ExpressionAst* v = subscript->value;
    if ( ! element.type ) {
        return;
    }
    ExpressionVisitor targetVisitor(currentContext());
    targetVisitor.visitNode(v);
    auto list = targetVisitor.lastType().dynamicCast<ListType>();
    if ( list ) {
        DUChainWriteLocker lock;
        list->addContentType<Python::UnsureType>(element.type);
    }
    auto map = list.dynamicCast<MapType>();
    if ( map ) {
        if ( subscript->slice && subscript->slice->astType != Ast::SliceAstType) {
            ExpressionVisitor keyVisitor(currentContext());
            keyVisitor.visitNode(subscript->slice);
            AbstractType::Ptr key = keyVisitor.lastType();
            if ( key ) {
                map->addKeyType<Python::UnsureType>(key);
            }
        }
    }
    DeclarationPointer lastDecl = targetVisitor.lastDeclaration();
    if ( list && lastDecl ) {
        DUChainWriteLocker lock;
        lastDecl->setAbstractType(list);
    }
}

void DeclarationBuilder::assignToAttribute(AttributeAst* attrib, const DeclarationBuilder::SourceType& element)
{
    // visit the base expression before the dot
    ExpressionVisitor checkPreviousAttributes(currentContext());
    checkPreviousAttributes.visitNode(attrib->value);
    DeclarationPointer parentObjectDeclaration = checkPreviousAttributes.lastDeclaration();

    DUContextPointer internal(nullptr);

    if ( ! parentObjectDeclaration ) {
        qCDebug(KDEV_PYTHON_DUCHAIN) << "No declaration for attribute base, aborting creation of attribute";
        return;
    }
    // if foo is a class, this is like foo.bar = 3
    if ( parentObjectDeclaration->internalContext() ) {
        internal = parentObjectDeclaration->internalContext();
    }
    // while this is like A = foo(); A.bar = 3
    else {
        DUChainReadLocker lock;
        auto structure = parentObjectDeclaration->abstractType().dynamicCast<StructureType>();
        if ( ! structure || ! structure->declaration(topContext()) ) {
            return;
        }
        parentObjectDeclaration = structure->declaration(topContext());
        internal = parentObjectDeclaration->internalContext();
    }
    if ( ! internal ) {
        qCDebug(KDEV_PYTHON_DUCHAIN) << "No internal context for structure type, aborting creation of attribute declaration";
        return;
    }

    Declaration* attributeDeclaration = nullptr;
    {
        DUChainReadLocker lock;
        attributeDeclaration = Helper::accessAttribute(parentObjectDeclaration->abstractType(),
                                                       attrib->attribute->value, topContext());
    }

    if ( ! attributeDeclaration || ! wasEncountered(attributeDeclaration) ) {
        // inject a new attribute into the class type
        DUContext* previousContext = currentContext();
        bool isAlreadyOpen = contextAlreadyOpen(internal);
        if ( isAlreadyOpen ) {
            activateAlreadyOpenedContext(internal);
            visitVariableDeclaration<ClassMemberDeclaration>(
                attrib->attribute, attributeDeclaration, element.type, AbortIfReopenMismatch
            );
            closeAlreadyOpenedContext(internal);
        }
        else {
            injectContext(internal.data());

            Declaration* dec = visitVariableDeclaration<ClassMemberDeclaration>(
                attrib->attribute, attributeDeclaration, element.type, AbortIfReopenMismatch
            );
            if ( dec ) {
                dec->setRange(RangeInRevision(internal->range().start, internal->range().start));
                dec->setAutoDeclaration(true);
                DUChainWriteLocker lock;
                previousContext->createUse(dec->ownIndex(), editorFindRange(attrib, attrib));
            }

            closeInjectedContext();
        }
    }
    else {
        DUChainWriteLocker lock;
        // the declaration is already there, just update the type
        if ( ! attributeDeclaration->type<FunctionType>() ) {
            auto newType = Helper::mergeTypes(attributeDeclaration->abstractType(), element.type);
            attributeDeclaration->setAbstractType(newType);
        }
    }
}

void DeclarationBuilder::tryUnpackType(AbstractType::Ptr sourceType, QVector<AbstractType::Ptr>& outTypes, int starred) {
    if ( const auto indexed = sourceType.dynamicCast<IndexedContainer>() ) {
        int spare = indexed->typesCount() - outTypes.length();
        if ( spare < -1 || (starred == -1 && spare != 0) ) {
            return; // Wrong number of elements to unpack.
        }
        for ( int i_out = 0, i_in = 0; i_out < outTypes.length(); ++i_out ) {
            if ( i_out == starred ) { // PEP-3132. Made into list in assignToTuple().
                for (; spare >= 0; --spare, ++i_in ) {
                    auto content = indexed->typeAt(i_in).abstractType();
                    outTypes[i_out] = Helper::mergeTypes(outTypes.at(i_out), content);
                }
            } else {
                auto content = indexed->typeAt(i_in).abstractType();
                outTypes[i_out] = Helper::mergeTypes(outTypes.at(i_out), content);
                ++i_in;
            }
        }
    } else {
        auto content = Helper::contentOfIterable(sourceType, topContext());
        if ( !Helper::isUsefulType(content) ) {
            return;
        }
        for (auto out = outTypes.begin(); out != outTypes.end(); ++out) {
            *out = Helper::mergeTypes(*out, content);
        }
    }
}

void DeclarationBuilder::assignToTuple(TupleAst* tuple, const SourceType& element) {
    int starred = -1;  // Index (if any) of PEP-3132 starred assignment.
    for (int ii = 0; ii < tuple->elements.length(); ++ii) {
         if (tuple->elements.at(ii)->astType == Ast::StarredAstType) {
            starred = ii;
            break;
        }
    }

    QVector<AbstractType::Ptr> outTypes(tuple->elements.length());

    if ( auto unsure = element.type.dynamicCast<UnsureType>() ) {
        FOREACH_FUNCTION ( const auto& type, unsure->types ) {
            tryUnpackType(type.abstractType(), outTypes, starred);
        }
    } else {
        tryUnpackType(element.type, outTypes, starred);
    }

    for (int ii = 0; ii < outTypes.length(); ++ii) {
        const auto sourceType = outTypes.at(ii);
        auto target = tuple->elements.at(ii);
        if ( target->astType == Ast::StarredAstType ) {
            DUChainReadLocker lock;
            auto listType = ExpressionVisitor::typeObjectForIntegralType<ListType>("list");
            lock.unlock();
            if (listType) {
                listType->addContentType<Python::UnsureType>(sourceType);
                assignToUnknown(static_cast<StarredAst*>(target)->value, listType);
            }
        } else {
            assignToUnknown(target, sourceType);
        }
    }
}

void DeclarationBuilder::assignToUnknown(ExpressionAst* target, const AbstractType::Ptr type) {
    auto source = SourceType{
        type,
        DeclarationPointer(),
        false
    };
    assignToUnknown(target, source);
}

void DeclarationBuilder::assignToUnknown(ExpressionAst* target, const DeclarationBuilder::SourceType& element) {
    // Must be a nicer way to do this.
    if ( target->astType == Ast::TupleAstType ) {
        // Assignments of the form "a, b = 1, 2" or "a, b = c"
        assignToTuple(static_cast<TupleAst*>(target), element);
    }
    else if ( target->astType == Ast::NameAstType ) {
        // Assignments of the form "a = 3"
        assignToName(static_cast<NameAst*>(target), element);
    }
    else if ( target->astType == Ast::SubscriptAstType ) {
        // Assignments of the form "a[0] = 3"
        assignToSubscript(static_cast<SubscriptAst*>(target), element);
    }
    else if ( target->astType == Ast::AttributeAstType ) {
        // Assignments of the form "a.b = 3"
        assignToAttribute(static_cast<AttributeAst*>(target), element);
    }
}

void DeclarationBuilder::visitAssignment(AssignmentAst* node)
{
    AstDefaultVisitor::visitAssignment(node);

    ExpressionVisitor v(currentContext());
    v.visitNode(node->value);
    auto sourceType = SourceType{
        v.lastType(),
        DeclarationPointer(Helper::resolveAliasDeclaration(v.lastDeclaration().data())),
        v.isAlias()
    };

    for (ExpressionAst* target : node->targets) {
        assignToUnknown(target, sourceType);
    }
}

void DeclarationBuilder::visitAnnotationAssignment(AnnotationAssignmentAst* node) {
    AstDefaultVisitor::visitAnnotationAssignment(node);

    ExpressionVisitor v(currentContext());
    v.visitNode(node->target);
    v.visitNode(node->value);
    auto assignType = v.lastType(); // Never mind aliasing, why annotate that?
    v.visitNode(node->annotation);
    assignType = Helper::mergeTypes(assignType, v.lastType());
    assignToUnknown(node->target, assignType);
}

void DeclarationBuilder::visitAssignmentExpression(AssignmentExpressionAst* node) {
    AstDefaultVisitor::visitAssignmentExpression(node);

    ExpressionVisitor v(currentContext());
    v.visitNode(node->value);
    assignToUnknown(node->target, v.lastType());
}

void DeclarationBuilder::visitClassDefinition( ClassDefinitionAst* node )
{
    visitNodeList(node->decorators);
    visitNodeList(node->baseClasses);
    const CorrectionHelper::Recursion r(m_correctionHelper->enterClass(node->name->value));

    StructureType::Ptr type(new StructureType());

    DUChainWriteLocker lock;
    ClassDeclaration* dec = eventuallyReopenDeclaration<ClassDeclaration>(node->name, NoTypeRequired);
    eventuallyAssignInternalContext();

    dec->setKind(KDevelop::Declaration::Type);
    dec->clearBaseClasses();
    dec->setClassType(ClassDeclarationData::Class);

    auto docstring = getDocstring(node->body);
    dec->setComment(docstring);
    if ( ! docstring.isEmpty() ) {
        // check whether this is a type container (list, dict, ...) or just a "normal" class
        if ( Helper::docstringContainsHint(docstring, "TypeContainer") ) {
            ListType* container = nullptr;
            if ( Helper::docstringContainsHint(docstring, "hasTypedKeys") ) {
                container = new MapType();
            }
            else {
                container = new ListType();
            }
            type = StructureType::Ptr(container);
        }
        if ( Helper::docstringContainsHint(docstring, "IndexedTypeContainer") ) {
            IndexedContainer* container = new IndexedContainer();
            type = StructureType::Ptr(container);
        }
    }
    lock.unlock();
    for ( ExpressionAst* c : node->baseClasses ) {
        // Iterate over all the base classes, and add them to the duchain.
        ExpressionVisitor v(currentContext());
        v.visitNode(c);
        if ( v.lastType() && v.lastType()->whichType() == AbstractType::TypeStructure ) {
            auto baseClassType = v.lastType().staticCast<StructureType>();
            BaseClassInstance base;
            base.baseClass = baseClassType->indexed();
            base.access = KDevelop::Declaration::Public;
            lock.lock();
            dec->addBaseClass(base);
            lock.unlock();
        }
    }
    lock.lock();
    // every python class inherits from "object".
    // We use this to add all the __str__, __get__, ... methods.
    if ( dec->baseClassesSize() == 0 && node->name->value != "object" ) {
        DUChainWriteLocker wlock;
        ReferencedTopDUContext docContext = Helper::getDocumentationFileContext();
        if ( docContext ) {
            QList<Declaration*> object = docContext->findDeclarations(
                QualifiedIdentifier("object")
            );
            if ( ! object.isEmpty() && object.first()->abstractType() ) {
                Declaration* objDecl = object.first();
                BaseClassInstance base;
                base.baseClass = objDecl->abstractType()->indexed();
                // this can be queried from autocompletion or elsewhere to hide the items, if required;
                // of course, it's not private strictly speaking
                base.access = KDevelop::Declaration::Private;
                dec->addBaseClass(base);
            }
        }
    }
    
    type->setDeclaration(dec);
    dec->setType(type);

    openType(type);
    m_currentClassTypes.append(type);

    // needs to be done here, so the assignment of the internal context happens before visiting the body
    openContextForClassDefinition(node);
    dec->setInternalContext(currentContext());

    lock.unlock();
    visitNodeList(node->body);
    lock.lock();

    closeContext();
    m_currentClassTypes.removeLast();
    closeType();
    closeDeclaration();
}

void DeclarationBuilder::visitFunctionDefinition( FunctionDefinitionAst* node )
{
    const CorrectionHelper::Recursion r(m_correctionHelper->enterFunction(node->name->value));

    // Search for an eventual containing class declaration;
    // if that exists, then this function is a member function
    DeclarationPointer eventualParentDeclaration(currentDeclaration());
    FunctionType::Ptr type(new FunctionType());

    DUChainWriteLocker lock;
    FunctionDeclaration* dec = eventuallyReopenDeclaration<FunctionDeclaration>(node->name,
                                                                                FunctionDeclarationType);

    Q_ASSERT(dec->isFunctionDeclaration());

    // check for documentation
    dec->setComment(getDocstring(node->body));

    openType(type);
    dec->setInSymbolTable(false);
    dec->setType(type);

    lock.unlock();
    dec->setStatic(false);
    dec->setClassMethod(false);
    dec->setProperty(false);
    for ( auto decorator : node->decorators) {
        visitNode(decorator);
        switch (decorator->astType) {
          case Ast::AttributeAstType: {
            auto attr = static_cast<AttributeAst*>(decorator)->attribute->value;
            if ( attr == QStringLiteral("setter") ||
                 attr == QStringLiteral("getter") ||
                 attr == QStringLiteral("deleter") )
                dec->setProperty(true);
            break;
          }
          case Ast::NameAstType: {
            auto name = static_cast<NameAst*>(decorator)->identifier->value;
            if ( name == QStringLiteral("staticmethod") )
                dec->setStatic(true);
            else if ( name == QStringLiteral("classmethod") )
                dec->setClassMethod(true);
            else if ( name == QStringLiteral("property") )
                dec->setProperty(true);
            break;
          }
          default: {}
        }
    }
    visitFunctionArguments(node);
    visitFunctionBody(node);
    lock.lock();

    closeDeclaration();
    eventuallyAssignInternalContext();

    closeType();

    // python methods don't have their parents attributes directly inside them
    if ( eventualParentDeclaration && eventualParentDeclaration->internalContext() && dec->internalContext() ) {
        dec->internalContext()->removeImportedParentContext(eventualParentDeclaration->internalContext());
    }
    
    {
        static IndexedString constructorName("__init__");
        DUChainWriteLocker lock(DUChain::lock());
        if ( dec->identifier().identifier() == constructorName ) {
            // the constructor returns an instance of the object,
            // nice to display it in tooltips etc.
            type->setReturnType(currentType<AbstractType>());
        }
        if ( ! type->returnType() ) {
            type->setReturnType(AbstractType::Ptr(new NoneType()));
        }
        dec->setType(type);
    }

    if ( ! dec->isStatic() ) {
        DUContext* args = DUChainUtils::argumentContext(dec);
        if ( args )  {
            QVector<Declaration*> parameters = args->localDeclarations();
            static IndexedString newMethodName("__new__");
            static IndexedString selfArgumentName("self");
            static IndexedString clsArgumentName("cls");
            if ( currentContext()->type() == DUContext::Class && ! parameters.isEmpty() && ! dec->isClassMethod() ) {
                QString description;
                if ( dec->identifier().identifier() == newMethodName
                     && parameters[0]->identifier().identifier() != clsArgumentName )
                {
                    description = i18n("First argument of __new__ method is not called cls, this is deprecated");
                }
                else if ( dec->identifier().identifier() != newMethodName
                          && parameters[0]->identifier().identifier() != selfArgumentName )
                {
                    description = i18n("First argument of class method is not called self, this is deprecated");
                }
                if ( ! description.isEmpty() ) {
                    DUChainWriteLocker lock;
                    KDevelop::Problem *p = new KDevelop::Problem();
                    p->setDescription(description);
                    p->setFinalLocation(DocumentRange(currentlyParsedDocument(), parameters[0]->range().castToSimpleRange()));
                    p->setSource(KDevelop::IProblem::SemanticAnalysis);
                    p->setSeverity(KDevelop::IProblem::Warning);
                    ProblemPointer ptr(p);
                    topContext()->addProblem(ptr);
                }
            }
            else if ( currentContext()->type() == DUContext::Class && parameters.isEmpty() ) {
                DUChainWriteLocker lock;
                KDevelop::Problem *p = new KDevelop::Problem();
                 // only mark first line
                p->setFinalLocation(DocumentRange(currentlyParsedDocument(), KTextEditor::Range(node->startLine, node->startCol, node->startLine, 10000)));
                p->setSource(KDevelop::IProblem::SemanticAnalysis);
                p->setSeverity(KDevelop::IProblem::Warning);
                p->setDescription(i18n("Non-static class method without arguments, must have at least one (self)"));
                ProblemPointer ptr(p);
                topContext()->addProblem(ptr);
            }
        }
    }

    if ( AbstractType::Ptr hint = m_correctionHelper->returnTypeHint() ) {
        type->setReturnType(hint);
        dec->setType(type);
    }
    
    // check for (python3) function annotations
    if ( node->returns ) {
        lock.unlock();
        ExpressionVisitor v(currentContext());
        v.visitNode(node->returns);
        lock.lock();
        if ( v.lastType() && v.isAlias() ) {
            type->setReturnType(Helper::mergeTypes(type->returnType(), v.lastType()));
            dec->setType(type);
        }
        else if ( ! v.isAlias()) {
            qCDebug(KDEV_PYTHON_DUCHAIN) << "not updating function return type because expression is not a type object";
        }
    }
    
    lock.lock();
    dec->setInSymbolTable(true);
}

QString DeclarationBuilder::getDocstring(QList< Python::Ast* > body) const
{
    if ( ! body.isEmpty() && body.first()->astType == Ast::ExpressionAstType 
            && static_cast<ExpressionAst*>(body.first())->value->astType == Ast::StringAstType )
    {
        // If the first statement in a function/class body is a string, then that is the docstring.
        StringAst* docstring = static_cast<StringAst*>(static_cast<ExpressionAst*>(body.first())->value);
        docstring->usedAsComment = true;
        return docstring->value.trimmed();
    }
    return QString();
}

void DeclarationBuilder::visitAssertion(AssertionAst* node)
{
    adjustForTypecheck(node->condition, false);
    Python::AstDefaultVisitor::visitAssertion(node);
}

void DeclarationBuilder::visitIf(IfAst* node)
{
    adjustForTypecheck(node->condition, true);
    Python::AstDefaultVisitor::visitIf(node);
}

void DeclarationBuilder::adjustForTypecheck(Python::ExpressionAst* check, bool useUnsure)
{
    if ( ! check ) return;
    if ( check->astType == Ast::UnaryOperationAstType
         && static_cast<UnaryOperationAst*>(check)->type == Ast::UnaryOperatorNot )
    {
        // It could be something like " if not isinstance(foo, Bar): return None ".
        check = static_cast<UnaryOperationAst*>(check)->operand;
    }
    if ( check->astType == Ast::CallAstType ) {
        // Is this a call of the form "isinstance(foo, bar)"?
        CallAst* call = static_cast<CallAst*>(check);
        if ( ! call->function ) {
            return;
        }
        if ( call->function->astType != Ast::NameAstType ) {
            return;
        }
        const QString functionName = static_cast<Python::NameAst*>(call->function)->identifier->value;
        if ( functionName != QLatin1String("isinstance") ) {
            return;
        }
        if ( call->arguments.length() != 2 ) {
            return;
        }
        adjustExpressionsForTypecheck(call->arguments.at(0), call->arguments.at(1), useUnsure);
    }
    else if ( check->astType == Ast::CompareAstType ) {
        // Is this a call of the form "type(ainstance) == a"?
        CompareAst* compare = static_cast<CompareAst*>(check);
        if ( compare->operators.size() != 1 || compare->comparands.size() != 1 ) {
            return;
        }
        if ( compare->operators.first() != Ast::ComparisonOperatorEquals ) {
            return;
        }
        ExpressionAst* c1 = compare->comparands.first();
        ExpressionAst* c2 = compare->leftmostElement;
        if ( ! ( (c1->astType == Ast::CallAstType) ^ (c2->astType == Ast::CallAstType) ) ) {
            // Exactly one of the two must be a call. TODO: support adjusting function return types
            return;
        }
        CallAst* typecall = static_cast<CallAst*>(c1->astType == Ast::CallAstType ? c1 : c2);
        if ( ! typecall->function || typecall->function->astType != Ast::NameAstType || typecall->arguments.length() != 1 ) {
            return;
        }
        const QString functionName = static_cast<Python::NameAst*>(typecall->function)->identifier->value;
        if ( functionName != QLatin1String("type") ) {
            return;
        }
        adjustExpressionsForTypecheck(typecall->arguments.at(0), c1->astType == Ast::CallAstType ? c2 : c1, useUnsure);
    }
}

void DeclarationBuilder::adjustExpressionsForTypecheck(Python::ExpressionAst* adjustExpr, Python::ExpressionAst* from, bool useUnsure)
{
    // Find types of the two arguments
    ExpressionVisitor first(currentContext());
    ExpressionVisitor second(currentContext());
    first.visitNode(adjustExpr);
    second.visitNode(from);
    AbstractType::Ptr hint;
    DeclarationPointer adjust;
    if ( second.isAlias() && second.lastType() ) {
        hint = second.lastType();
        adjust = first.lastDeclaration();
    }
    if ( ! adjust || adjust->isFunctionDeclaration() ) {
        // no declaration for the thing to verify, can't adjust it.
        return;
    }
    else if ( adjust->topContext() == Helper::getDocumentationFileContext() ) {
        // do not motify types in the doc context
        return;
    }
    DUChainWriteLocker lock;
    if ( useUnsure ) {
        adjust->setAbstractType(Helper::mergeTypes(adjust->abstractType(), hint));
    }
    else {
        adjust->setAbstractType(hint);
    }
}

void DeclarationBuilder::visitReturn(ReturnAst* node)
{
    static auto noneType = AbstractType::Ptr(new NoneType());

    if ( auto function = currentType<FunctionType>() ) {
        // Statements with no explicit value return `None`.
        auto encountered = noneType;
        if ( node->value ) {
            // Find the type of the object being "return"ed
            ExpressionVisitor v(currentContext());
            v.visitNode(node->value);
            encountered = v.lastType();
        }
        // Update the containing function's return type
        DUChainWriteLocker lock;
        function->setReturnType(Helper::mergeTypes(function->returnType(), encountered));
    } else {
        DUChainWriteLocker lock;
        KDevelop::Problem *p = new KDevelop::Problem();
        p->setFinalLocation(DocumentRange(currentlyParsedDocument(), node->range())); // only mark first line
        p->setSource(KDevelop::IProblem::SemanticAnalysis);
        p->setDescription(i18n("Return statement not within function declaration"));
        ProblemPointer ptr(p);
        topContext()->addProblem(ptr);
    }
    DeclarationBuilderBase::visitReturn(node);
}

void DeclarationBuilder::visitArguments( ArgumentsAst* node )
{
    if ( ! currentDeclaration() || ! currentDeclaration()->isFunctionDeclaration() ) {
        return;
    }
    FunctionDeclaration* workingOnDeclaration = static_cast<FunctionDeclaration*>(Helper::resolveAliasDeclaration(currentDeclaration()));
    workingOnDeclaration->clearDefaultParameters();
    if ( ! hasCurrentType() || ! currentType<FunctionType>() ) {
        return;
    }
    FunctionType::Ptr type = currentType<FunctionType>();
    bool isFirst = true;
    int defaultParametersCount = node->defaultValues.length();
    int parametersCount = node->arguments.length();
    int firstDefaultParameterOffset = parametersCount - defaultParametersCount;

    int defaultKwParametersCount = node->defaultKwValues.length();
    int kwonlyCount = node->kwonlyargs.length();
    int posonlyCount = node->posonlyargs.length();
    int totalArgCount = parametersCount + posonlyCount + kwonlyCount;
    int firstDefaultKwParameterOffset = totalArgCount - defaultKwParametersCount;
    int currentIndex = 0;
    for ( ArgAst* arg : node->posonlyargs + node->arguments + node->kwonlyargs ) {
        // Iterate over all the function's arguments, create declarations, and add the arguments
        // to the functions FunctionType.
        currentIndex += 1;

        if ( ! arg->argumentName ) {
            continue;
        }

        // Create a variable declaration for the parameter, to be used in the function body.
        Declaration* paramDeclaration = nullptr;
        if ( currentIndex == 1 && workingOnDeclaration->isClassMethod() ) {
            DUChainWriteLocker lock;
            AliasDeclaration* decl = eventuallyReopenDeclaration<AliasDeclaration>(arg->argumentName,
                                                                                   AliasDeclarationType);
            if ( ! m_currentClassTypes.isEmpty() ) {
                auto classDecl = m_currentClassTypes.last()->declaration(topContext());

                decl->setAliasedDeclaration(classDecl);
            }
            closeDeclaration();
            paramDeclaration = decl;
        }
        else {
            paramDeclaration = visitVariableDeclaration<Declaration>(arg->argumentName);
        }
        if ( ! paramDeclaration ) {
            qCDebug(KDEV_PYTHON_DUCHAIN) << "could not create parameter declaration!";
            continue;
        }

        AbstractType::Ptr argumentType(new IntegralType(IntegralType::TypeMixed));
        if ( arg->annotation ) {
            ExpressionVisitor v(currentContext());
            v.visitNode(arg->annotation);
            if ( v.lastType() && v.isAlias() ) {
                DUChainWriteLocker lock;
                argumentType = Helper::mergeTypes(paramDeclaration->abstractType(), v.lastType());
            }
        }
        else if ( currentIndex > firstDefaultParameterOffset && currentIndex <= node->arguments.size() ) {
            // Handle arguments with default values, like def foo(bar = 3): pass
            // Find type of given default value, and assign it to the declaration
            ExpressionVisitor v(currentContext());
            v.visitNode(node->defaultValues.at(currentIndex - firstDefaultParameterOffset - 1));
            if ( v.lastType() ) {
                argumentType = v.lastType();
            }
            // TODO add the real expression from the document here as default value
            workingOnDeclaration->addDefaultParameter(IndexedString("..."));
        }
        else if ( currentIndex > firstDefaultKwParameterOffset && currentIndex <= totalArgCount ) {
            // Handle kw only arguments with default values, like def foo(*, bar = 3): pass
            // Find type of given default value, and assign it to the declaration
            ExpressionVisitor v(currentContext());
            v.visitNode(node->defaultKwValues.at(currentIndex - firstDefaultKwParameterOffset - 1));
            if ( v.lastType() ) {
                argumentType = v.lastType();
            }
            // TODO add the real expression from the document here as default value
            workingOnDeclaration->addDefaultParameter(IndexedString("..."));
        }


        if ( isFirst && ! workingOnDeclaration->isStatic() && currentContext() && currentContext()->parentContext() ) {
            DUChainReadLocker lock;
            if ( currentContext()->parentContext()->type() == DUContext::Class ) {
                argumentType = m_currentClassTypes.last();
                isFirst = false;
            }
        }

        DUChainWriteLocker lock;
        paramDeclaration->setAbstractType(Helper::mergeTypes(paramDeclaration->abstractType(), argumentType));
        type->addArgument(argumentType);
    }
    // Handle *args, **kwargs, and assign them a list / dictionary type.
    if ( node->vararg ) {
        // inject the vararg at the correct place
        int atIndex = 0;
        int useIndex = -1;
        for ( ArgAst* arg : node->arguments ) {
            if ( node->vararg && workingOnDeclaration->vararg() == -1 && node->vararg->appearsBefore(arg) ) {
                useIndex = atIndex;
            }
            atIndex += 1;
        }
        if ( useIndex == -1 ) {
            // if the vararg does not appear in the middle of the params, place it at the end.
            // this is new in python3, you can do like def fun(a, b, *c, z): pass
            useIndex = type->arguments().size();
        }
        DUChainReadLocker lock;
        IndexedContainer::Ptr tupleType = ExpressionVisitor::typeObjectForIntegralType<IndexedContainer>("tuple");
        lock.unlock();
        if ( tupleType ) {
            visitVariableDeclaration<Declaration>(node->vararg->argumentName, nullptr, tupleType);
            workingOnDeclaration->setVararg(atIndex);
            type->addArgument(tupleType, useIndex);
        }
    }

    if ( node->kwarg ) {
        DUChainReadLocker lock;
        AbstractType::Ptr stringType = ExpressionVisitor::typeObjectForIntegralType<AbstractType>("str");
        auto dictType = ExpressionVisitor::typeObjectForIntegralType<MapType>("dict");
        lock.unlock();
        if ( dictType && stringType ) {
            dictType->addKeyType<Python::UnsureType>(stringType);
            visitVariableDeclaration<Declaration>(node->kwarg->argumentName, nullptr, dictType);
            type->addArgument(dictType);
            workingOnDeclaration->setKwarg(type->arguments().size() - 1);
        }
    }
}

void DeclarationBuilder::visitString(StringAst* node) {
    if ( node->parent && node->parent->astType == Ast::ExpressionAstType ) {
        m_lastComment = node;
    }
    DeclarationBuilderBase::visitString(node);
}

void DeclarationBuilder::visitNode(Ast* node) {
    DeclarationBuilderBase::visitNode(node);
    if ( node && node->astType >= Ast::StatementAstType && node->astType <= Ast::LastStatementType) {
        m_lastComment = nullptr;
    }
}

void DeclarationBuilder::visitGlobal(GlobalAst* node)
{
    TopDUContext* top = topContext();
    for ( Identifier *id : node->names ) {
        QualifiedIdentifier qid = identifierForNode(id);
        DUChainWriteLocker lock;
        QList< Declaration* > existing = top->findLocalDeclarations(qid.first());
        if ( ! existing.empty() ) {
            AliasDeclaration* ndec = openDeclaration<AliasDeclaration>(id);
            ndec->setAliasedDeclaration(existing.first());
            closeDeclaration();
        }
        else {
            injectContext(top);
            Declaration* dec = visitVariableDeclaration<Declaration>(id);
            dec->setRange(editorFindRange(id, id));
            dec->setAutoDeclaration(true);
            closeContext();
            AliasDeclaration* ndec = openDeclaration<AliasDeclaration>(id);
            ndec->setAliasedDeclaration(dec);
            closeDeclaration();
        }
    }
}

}


