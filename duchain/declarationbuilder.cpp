/*****************************************************************************
 * Copyright (c) 2007 Piyush verma <piyush.verma@gmail.com>                  *
 * Copyright 2007 Andreas Pakulat <apaku@gmx.de>                             *
 * Copyright 2010-2013 Sven Brauch <svenbrauch@googlemail.com>               *
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

#include "declarationbuilder.h"
#include "duchain/declarations/decorator.h"
#include "duchain/declarations/functiondeclaration.h"
#include "duchain/declarations/classdeclaration.h"

#include "types/hintedtype.h"
#include "types/unsuretype.h"
#include "types/indexedcontainer.h"
#include "contextbuilder.h"
#include "expressionvisitor.h"
#include "pythoneditorintegrator.h"
#include "helpers.h"
#include "assistants/missingincludeassistant.h"
#include "correctionhelper.h"

#include <language/duchain/functiondeclaration.h>
#include <language/duchain/declaration.h>
#include <language/duchain/duchain.h>
#include <language/duchain/types/alltypes.h>
#include <language/duchain/classdeclaration.h>
#include <language/duchain/declaration.h>
#include <language/duchain/builders/abstracttypebuilder.h>
#include <language/duchain/aliasdeclaration.h>
#include <language/duchain/duchainutils.h>
#include <language/backgroundparser/backgroundparser.h>
#include <language/backgroundparser/parsejob.h>
#include <interfaces/ilanguagecontroller.h>

#include <QByteArray>
#include <QtGlobal>
#include <KUrl>

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
    kDebug() << "Building Declarations";
}

DeclarationBuilder:: ~DeclarationBuilder()
{
    if ( ! m_scheduledForDeletion.isEmpty() ) {
        DUChainWriteLocker lock;
        foreach ( DUChainBase* d, m_scheduledForDeletion ) {
            delete d;
        }
        m_scheduledForDeletion.clear();
    }
}

void DeclarationBuilder::setPrebuilding(bool prebuilding)
{
    m_prebuilding = prebuilding;
}

ReferencedTopDUContext DeclarationBuilder::build(const IndexedString& url, Ast* node, ReferencedTopDUContext updateContext)
{
    m_correctionHelper.reset(new CorrectionHelper(url, this));

    // The declaration builder needs to run twice, so it can resolve uses of e.g. functions
    // which are called before they are defined (which is easily possible, due to python's dynamic nature).
    if ( ! m_prebuilding ) {
        kDebug() << "building, but running pre-builder first";
        DeclarationBuilder* prebuilder = new DeclarationBuilder(editor());
        prebuilder->m_ownPriority = m_ownPriority;
        prebuilder->m_currentlyParsedDocument = currentlyParsedDocument();
        prebuilder->setPrebuilding(true);
        prebuilder->m_futureModificationRevision = m_futureModificationRevision;
        updateContext = prebuilder->build(url, node, updateContext);
        kDebug() << "pre-builder finished";
        delete prebuilder;
    }
    else {
        kDebug() << "prebuilding";
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

template<typename T> T* DeclarationBuilder::eventuallyReopenDeclaration(Identifier* name, Ast* range, FitDeclarationType mustFitType)
{
    QList<Declaration*> existingDeclarations = existingDeclarationsForNode(name);
    
    Declaration* dec = 0;
    reopenFittingDeclaration<T>(existingDeclarations, mustFitType, editorFindRange(range, range), &dec);
    bool declarationOpened = (bool) dec;
    if ( ! declarationOpened ) {
        dec = openDeclaration<T>(name, range);
    }
    Q_ASSERT(dynamic_cast<T*>(dec));
    return static_cast<T*>(dec);
}

template<typename T> T* DeclarationBuilder::visitVariableDeclaration(Ast* node, Declaration* previous, AbstractType::Ptr type)
{
    if ( node->astType == Ast::NameAstType ) {
        NameAst* currentVariableDefinition = static_cast<NameAst*>(node);
        // those contexts can invoke a variable declaration
        // this prevents "bar" from being declared in something like "foo = bar"
        // This is just a sanity check, the code should never request creation of a variable
        // in such cases.
        QList<ExpressionAst::Context> declaringContexts;
        declaringContexts << ExpressionAst::Store << ExpressionAst::Parameter << ExpressionAst::AugStore;
        if ( ! declaringContexts.contains(currentVariableDefinition->context) ) {
            return 0;
        }
        Identifier* id = currentVariableDefinition->identifier;
        return visitVariableDeclaration<T>(id, currentVariableDefinition, previous, type);
    }
    else if ( node->astType == Ast::IdentifierAstType ) {
        return visitVariableDeclaration<T>(static_cast<Identifier*>(node), 0, previous, type);
    }
    else {
        kWarning() << "cannot create variable declaration for non-(name|identifier) AST, this is a programming error";
        return static_cast<T*>(0);
    }
}

template<typename T> T* DeclarationBuilder::visitVariableDeclaration(Identifier* node, RangeInRevision range,
                                                                     AbstractType::Ptr type)
{
    Ast pseudo;
    pseudo.startLine = range.start.line; pseudo.startCol = range.start.column;
    pseudo.endLine = range.end.line; pseudo.endCol = range.end.column;
    T* result = visitVariableDeclaration<T>(node, &pseudo, 0, type);
    return result;
}

QList< Declaration* > DeclarationBuilder::existingDeclarationsForNode(Identifier* node)
{
    QList<Declaration*> existingDeclarations = currentContext()->findDeclarations(
        identifierForNode(node).last(), CursorInRevision::invalid(), 0,
        (DUContext::SearchFlag) (DUContext::DontSearchInParent | DUContext::DontResolveAliases)
    );
    // append arguments context
    if ( m_mostRecentArgumentsContext ) {
        QList<Declaration*> args = m_mostRecentArgumentsContext->findDeclarations(
            identifierForNode(node).last(), CursorInRevision::invalid(), 0, DUContext::DontSearchInParent
        );
        existingDeclarations.append(args);
    }
    return existingDeclarations;
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
    *ok = 0;
    foreach ( Declaration* d, declarations ) {
        Declaration* fitting = dynamic_cast<T*>(d);
        if ( ! fitting ) {
            // Only use a declaration if the type matches
            kDebug() << "skipping" << d->toString() << "which could not be cast to the requested type";
            continue;
        }
        // Do not use declarations which have been encountered previously;
        // this function only handles declarations from previous parser passes which have not
        // been encountered yet in this pass
        bool reallyEncountered = wasEncountered(d) && ! m_scheduledForDeletion.contains(d);
        bool invalidType = false;
        if ( d && d->abstractType() && mustFitType != NoTypeRequired ) {
            invalidType = ( ( d->isFunctionDeclaration() ) != ( mustFitType == FunctionDeclarationType ) );
            if ( ! invalidType ) {
                invalidType = ( ( dynamic_cast<AliasDeclaration*>(d) != 0 ) != ( mustFitType == AliasDeclarationType ) );
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
                kDebug() << "Not opening previously existing declaration because it's in another top context";
            }
        }
        else if ( ! invalidType ) {
            remainingDeclarations << d;
        }
    }
    return remainingDeclarations;
}

typedef QPair<Declaration*, int> p;
template<typename T> T* DeclarationBuilder::visitVariableDeclaration(Identifier* node, Ast* originalAst, Declaration* previous, AbstractType::Ptr type)
{
    DUChainWriteLocker lock;
    Ast* rangeNode = originalAst ? originalAst : node;
    RangeInRevision range = editorFindRange(rangeNode, rangeNode);
    
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
    Declaration* dec = 0;
    existingDeclarations = reopenFittingDeclaration<T>(existingDeclarations, kindForType(type), range, &dec);
    bool declarationOpened = (bool) dec;
    
    // tells whether the declaration found for updating is in the same top context
    bool inSameTopContext = true;
    // tells whether there's fitting declarations to update (update is not the same as re-open! one is for
    // code which uses the same variable twice, the other is for multiple passes of the parser)
    bool haveFittingDeclaration = false;
    if ( ! existingDeclarations.isEmpty() and existingDeclarations.last() ) {
        Declaration* d = Helper::resolveAliasDeclaration(existingDeclarations.last());
        DUChainReadLocker lock;
        if ( d and d->topContext() != topContext() ) {
            inSameTopContext = false;
        }
        if ( dynamic_cast<T*>(existingDeclarations.last()) ) {
            haveFittingDeclaration = true;
        }
    }
    if ( currentContext() && currentContext()->type() == DUContext::Class && ! haveFittingDeclaration ) {
        // If the current context is a class, then this is a class member variable.
        if ( ! dec ) {
            dec = openDeclaration<ClassMemberDeclaration>(identifierForNode(node), range);
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
            dec = openDeclaration<T>(identifierForNode(node), range);
            Q_ASSERT(! declarationOpened);
            declarationOpened = true;
        }
        if ( declarationOpened ) {
            DeclarationBuilderBase::closeDeclaration();
        }
        
        AbstractType::Ptr newType;
        if ( currentContext()->type() == DUContext::Function ) {
            // check for argument type hints (those are created when calling functions)
            AbstractType::Ptr hints = Helper::extractTypeHints(dec->abstractType(), topContext());
            kDebug() << hints->toString();
            if ( hints.cast<IndexedContainer>() || hints.cast<ListType>() ) {
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
    if ( ! result ) kWarning() << "variable declaration does not have the expected type";
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
        visitVariableDeclaration<Declaration>(node->name, 0, v.lastType());
    }
    DeclarationBuilderBase::visitExceptionHandler(node);
}

void DeclarationBuilder::visitWithItem(WithItemAst* node)
{
    if ( node->optionalVars ) {
        // For statements like "with open(f) as x", a new variable must be created; do this here.
        ExpressionVisitor v(currentContext());
        v.visitNode(node->contextExpression);
        visitVariableDeclaration<Declaration>(node->optionalVars, 0, v.lastType());
    }
    Python::AstDefaultVisitor::visitWithItem(node);
}

void DeclarationBuilder::visitFor(ForAst* node)
{
    ExpressionVisitor v(currentContext());
    v.visitNode(node->iterator);
    auto possibleIterators = Helper::filterType<ListType>(v.lastType(),
        [](AbstractType::Ptr type) {
            auto container = type.cast<ListType>();
            return container && container->contentType();
        }
    );
    if ( node->target->astType == Ast::NameAstType ) {
        // In case the iterator variable is a Name ("for x in range(3)"), just create a declaration for it.
        // The following code tries to figure out the type of "x" from the object that is being iterated over.
        auto iteratorType = Helper::foldTypes<ListType::Ptr>(possibleIterators,
            [](const ListType::Ptr& p) {
                return p->contentType().abstractType();
            }
        );
        // otherwise, no list type whatsoever was available for the iterator list, so just display "mixed".

        // Create the variable declaration for the iterator variable with the type that has been determined.
        visitVariableDeclaration<Declaration>(node->target, 0, iteratorType);
    }
    else if ( node->target->astType == Ast::TupleAstType ) {
        // If the target is a tuple ("for x, y, z in ..."), multiple variables must be declared.
        // For now, types of those variables will only be determined if the iterator is a list of tuples.
        QList<ExpressionAst*> targetElements = targetsOfAssignment(QList<ExpressionAst*>() << node->target);
        int targetElementsCount = targetElements.count();
        QList<IndexedContainer::Ptr> gatherFromTuples;
        for ( auto container : possibleIterators ) {
            AbstractType::Ptr contentType = container->contentType().abstractType();
            gatherFromTuples = Helper::filterType<IndexedContainer>(contentType,
                // find all IndexedContainer entries which have the right number of entries
                [targetElementsCount](AbstractType::Ptr type) {
                    IndexedContainer::Ptr indexed = type.cast<IndexedContainer>();
                    return indexed && indexed->typesCount() == targetElementsCount;
                }
            );
        }

        // Now, iterate over all possible tuples, and extract their types
        int i = 0;
        QList<AbstractType::Ptr> targetTypes;
        foreach ( IndexedContainer::Ptr tuple, gatherFromTuples ) {
            for ( int j = 0; j < tuple->typesCount(); j++ ) {
                if ( i == 0 ) {
                    targetTypes.append(tuple->typeAt(j).abstractType());
                }
                else {
                    targetTypes[j] = Helper::mergeTypes(targetTypes[j], tuple->typeAt(j).abstractType());
                }
            }
            i++;
        }

        short atElement = 0;
        bool haveTypeInformation = ! targetTypes.isEmpty();
        Q_ASSERT( ! haveTypeInformation || targetTypes.length() == targetElementsCount );
        foreach ( ExpressionAst* tupleMember, targetElements ) {
            if ( tupleMember->astType == Ast::NameAstType ) {
                AbstractType::Ptr newType;
                if ( haveTypeInformation ) {
                    newType = targetTypes.at(atElement);
                }
                else {
                    newType = AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed));
                }
                visitVariableDeclaration<Declaration>(tupleMember, 0, newType);
            }
            ++atElement;
        }
    }
    Python::ContextBuilder::visitFor(node);
}

Declaration* DeclarationBuilder::findDeclarationInContext(QStringList dottedNameIdentifier, TopDUContext* ctx) const
{
    DUChainReadLocker lock(DUChain::lock());
    DUContext* currentContext = ctx;
    // TODO make this a bit faster, it wastes time
    Declaration* lastAccessedDeclaration = 0;
    int i = 0;
    int identifierCount = dottedNameIdentifier.length();
    foreach ( const QString& currentIdentifier, dottedNameIdentifier ) {
        Q_ASSERT(currentContext);
        i++;
        QList<Declaration*> declarations = currentContext->findDeclarations(QualifiedIdentifier(currentIdentifier).first(),
                                                                            CursorInRevision::invalid(), 0, DUContext::NoFiltering);
        // break if the list of identifiers is not yet totally worked through and no
        // declaration with an internal context was found
        if ( declarations.isEmpty() or ( not declarations.last()->internalContext() and identifierCount != i ) ) {
            kDebug() << "Declaration not found: " << dottedNameIdentifier << "in top context" << ctx->url().toUrl().path();
            return 0;
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
    foreach ( AliasAst* name, node->names ) {
        // iterate over all the names that are imported, like "from foo import bar as baz, bang as asdf"
        Identifier* declarationIdentifier = 0;
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
        ProblemPointer problem(0);
        QString intermediate;
        moduleName = buildModuleNameFromNode(node, name, intermediate);
        Declaration* success = createModuleImportDeclaration(moduleName, declarationName, declarationIdentifier, problem);
        if ( ! success && (node->module || node->level) ) {
            ProblemPointer problem_init(0);
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
    // make the declaration zero chars long; it must appear at the beginning of the context,
    // because it is actually used *before* its real declaration: [foo for foo in bar]
    // The DUChain doesn't like this, so for now, the declaration is at the opening bracket,
    // and both other occurences are uses of that declaration.
    // TODO add a special case to the usebuilder to display the second occurence as a declaration
    RangeInRevision declarationRange(currentContext()->range().start, currentContext()->range().start);
    declarationRange.end.column -= 1;
    
    AbstractType::Ptr targetType(new IntegralType(IntegralType::TypeMixed));
    if ( node->iterator ) {
        // try to find the type of the object being iterated over, for guessing the
        // type of the iterator variable
        ExpressionVisitor v(currentContext());
        v.visitNode(node->iterator);
        if ( auto container = ListType::Ptr::dynamicCast(v.lastType()) ) {
            targetType = container->contentType().abstractType();
        }
    }
    
    // create variable declarations for the iterator variable(s)
    if ( node->target->astType == Ast::NameAstType ) {
        visitVariableDeclaration<Declaration>(static_cast<NameAst*>(node->target)->identifier, declarationRange, targetType);
    }
    if ( node->target->astType == Ast::TupleAstType ) {
        foreach ( ExpressionAst* tupleElt, static_cast<TupleAst*>(node->target)->elements ) {
            if ( tupleElt->astType == Ast::NameAstType ) {
                NameAst* n = static_cast<NameAst*>(tupleElt);
                visitVariableDeclaration<Declaration>(n->identifier, declarationRange);
            }
        }
    }
}

void DeclarationBuilder::visitImport(ImportAst* node)
{
    Python::ContextBuilder::visitImport(node);
    DUChainWriteLocker lock;
    foreach ( AliasAst* name, node->names ) {
        QString moduleName = name->name->value;
        // use alias if available, name otherwise
        Identifier* declarationIdentifier = name->asName ? name->asName : name->name;
        ProblemPointer problem(0);
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
    
    kDebug() << "creating declaration tree for" << nameComponents;
    
    Declaration* lastDeclaration = 0;
    int depth = 0;
    
    // check for already existing trees to update
    for ( int i = nameComponents.length() - 1; i >= 0; i-- ) {
        QStringList currentName;
        for ( int j = 0; j < i; j++ ) {
            currentName.append(nameComponents.at(j));
        }
        lastDeclaration = findDeclarationInContext(currentName, topContext());
        if ( lastDeclaration and lastDeclaration->range() < range ) {
            depth = i;
            break;
        }
    }
    
    DUContext* extendingPreviousImportCtx = 0;
    QStringList remainingNameComponents;
    bool injectingContext = false;
    if ( lastDeclaration and lastDeclaration->internalContext() ) {
        kDebug() << "Found existing import statement while creating declaration for " << declarationIdentifier->value;
        for ( int i = depth; i < nameComponents.length(); i++ ) {
            remainingNameComponents.append(nameComponents.at(i));
        }
        extendingPreviousImportCtx = lastDeclaration->internalContext();
        injectContext(extendingPreviousImportCtx);
        injectingContext = true;
        kDebug() << "remaining identifiers:" << remainingNameComponents;
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
        Declaration* d = 0;
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
                                                                                        &temporaryIdentifier,
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
            currentContext()->createUse(d->ownIndex(), displayRange);
            kDebug() << "really encountered:" << d << "; scheduled:" << m_scheduledForDeletion;
            kDebug() << d->toString();
            scheduleForDeletion(d, false);
            kDebug() << "scheduled:" << m_scheduledForDeletion;
        }
        if ( done ) break;
        
        kDebug() << "creating context for " << component;
        // otherwise, create a new "level" entry (a pseudo type + context + declaration which contains all imported items)
        StructureType::Ptr moduleType = StructureType::Ptr(new StructureType());
        openType(moduleType);
        
        openedContexts.append(openContext(declarationIdentifier, KDevelop::DUContext::Other));
        
        foreach ( Declaration* local, currentContext()->localDeclarations() ) {
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
                kDebug() << "adding imported context to inner declaration";
                currentContext()->addImportedParentContext(innerCtx);
            }
            else if ( aliasDeclaration ) {
                kDebug() << "setting alias declaration on inner declaration";
            }
        }
    }
    for ( int i = openedContexts.length() - 1; i >= 0; i-- ) {
        // Close all the declarations and contexts opened previosly, and assign the types.
        kDebug() << "closing context";
        closeType();
        closeContext();
        Declaration* d = openedDeclarations.at(i);
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
    else return 0;
}

Declaration* DeclarationBuilder::createModuleImportDeclaration(QString moduleName, QString declarationName,
                                                               Identifier* declarationIdentifier,
                                                               ProblemPointer& problemEncountered, Ast* rangeNode)
{
    // Search the disk for a python file which contains the requested declaration
    QPair<KUrl, QStringList> moduleInfo = findModulePath(moduleName, currentlyParsedDocument().toUrl());
    RangeInRevision range(RangeInRevision::invalid());
    if ( rangeNode ) {
        range = rangeForNode(rangeNode, false);
    }
    else {
        range = rangeForNode(declarationIdentifier, false);
    }
    Q_ASSERT(range.isValid());
    
    kDebug() << "Found module path [path/path in file]: " << moduleInfo;
    kDebug() << "Declaration identifier:" << declarationIdentifier->value;
    DUChainWriteLocker lock;
    const IndexedString modulePath = IndexedString(moduleInfo.first);
    ReferencedTopDUContext moduleContext = DUChain::self()->chainForDocument(modulePath);
    lock.unlock();
    Declaration* resultingDeclaration = 0;
    if ( ! moduleInfo.first.isValid() ) {
        // The file was not found -- this is either an error in the user's code,
        // a missing module, or a C module (.so) which is unreadable for kdevelop
        // TODO imrpove error handling in case the module exists as a shared object or .pyc file only
        kDebug() << "invalid or non-existent URL:" << moduleInfo;
        KDevelop::Problem *p = new Python::MissingIncludeProblem(moduleName, currentlyParsedDocument());
        p->setFinalLocation(DocumentRange(currentlyParsedDocument(), range.castToSimpleRange()));
        p->setSource(KDevelop::ProblemData::SemanticAnalysis);
        p->setSeverity(KDevelop::ProblemData::Warning);
        p->setDescription(i18n("Module \"%1\" not found", moduleName));
        problemEncountered = p;
        return 0;
    }
    if ( ! moduleContext ) {
        // schedule the include file for parsing, and schedule the current one for reparsing after that is done
        kDebug() << "No module context, recompiling";
        m_unresolvedImports.append(modulePath);
        Helper::scheduleDependency(modulePath, m_ownPriority);
        // parseDocuments() must *not* be called from a background thread!
        // KDevelop::ICore::self()->languageController()->backgroundParser()->parseDocuments();
        return 0;
    }
    if ( moduleInfo.second.isEmpty() ) {
        // import the whole module
        resultingDeclaration = createDeclarationTree(declarationName.split("."),
                                                     declarationIdentifier, moduleContext, 0, range);
    }
    else {
        // import a specific declaration from the given file
        lock.lock();
        if ( declarationIdentifier->value == "*" ) {
            kDebug() << "Importing * from module";
            currentContext()->addImportedParentContext(moduleContext);
        }
        else {
            kDebug() << "Got module, importing declaration: " << moduleInfo.second;
            Declaration* originalDeclaration = findDeclarationInContext(moduleInfo.second, moduleContext);
            if ( originalDeclaration ) {
                DUChainWriteLocker lock(DUChain::lock());
                resultingDeclaration = createDeclarationTree(declarationName.split("."), declarationIdentifier,
                                                             ReferencedTopDUContext(0), originalDeclaration,
                                                             editorFindRange(declarationIdentifier, declarationIdentifier));
            }
            else {
                KDevelop::Problem *p = new Python::MissingIncludeProblem(moduleName, currentlyParsedDocument());
                p->setFinalLocation(DocumentRange(currentlyParsedDocument(), range.castToSimpleRange())); // TODO ok?
                p->setSource(KDevelop::ProblemData::SemanticAnalysis);
                p->setSeverity(KDevelop::ProblemData::Warning);
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
    if ( auto previous = t->returnType().cast<ListType>() ) {
        // If the return type of the function already is set to a list, *add* the encountered type
        // to its possible content types.
        previous->addContentType<Python::UnsureType>(encountered);
        t->setReturnType(previous.cast<AbstractType>());
    }
    else {
        // Otherwise, create a new container type, and set it as the function's return type.
        DUChainWriteLocker lock;
        auto container = ExpressionVisitor::typeObjectForIntegralType<ListType>("list", currentContext());
        if ( container ) {
            openType<ListType>(container);
            container->addContentType<Python::UnsureType>(encountered);
            t->setReturnType(Helper::mergeTypes(t->returnType(), container.cast<AbstractType>()));
            closeType();
        }
    }
}

void DeclarationBuilder::visitLambda(LambdaAst* node)
{
    Python::AstDefaultVisitor::visitLambda(node);
    DUChainWriteLocker lock;
    // A context must be opened, because the lamdba's arguments are local to the lambda:
    // d = lambda x: x*2; print x # <- gives an error
    openContext(node, editorFindRange(node, node->body), DUContext::Other);
    foreach ( ArgAst* argument, node->arguments->arguments ) {
        visitVariableDeclaration<Declaration>(argument->argumentName);
    }
    closeContext();
}

void DeclarationBuilder::applyDocstringHints(CallAst* node, FunctionDeclaration::Ptr function)
{
    ExpressionVisitor v(currentContext());
    v.visitNode(static_cast<AttributeAst*>(node->function)->value);

    // Don't do anything if the object the function is being called on is not a container.
    auto container = v.lastType().cast<ListType>();
    if ( ! container || ! function ) {
        return;
    }
    // Don't to updates to pre-defined functions.
    if ( ! v.lastDeclaration() || v.lastDeclaration()->topContext()->url() == IndexedString(Helper::getDocumentationFile()) ) {
        return;
    }
    // Check for the different types of modifiers such a function can have
    QStringList args;
    QHash< QString, std::function<void()> > items;
    items["addsTypeOfArg"] = [&]() {
        const int offset = ! args.isEmpty() ? args.at(0).toInt() : 0;
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
        kDebug() << "Adding content type: " << argVisitor.lastType()->toString();
        container->addContentType<Python::UnsureType>(argVisitor.lastType());
        v.lastDeclaration()->setType(container);
    };
    items["addsTypeOfArgContent"] = [&]() {
        const int offset = ! args.isEmpty() ? args.at(0).toInt() : 0;
        if ( node->arguments.length() <= offset ) {
            return;
        }
        ExpressionVisitor argVisitor(currentContext());
        argVisitor.visitNode(node->arguments.at(offset));
        DUChainWriteLocker wlock;
        if ( ! argVisitor.lastType() ) {
            return;
        }
        auto sources = Helper::filterType<ListType>(
            argVisitor.lastType(), [](AbstractType::Ptr type) {
                return type.cast<ListType>();
            }
        );
        for ( auto sourceContainer : sources ) {
            if ( ! sourceContainer->contentType() ) {
                continue;
            }
            container->addContentType<Python::UnsureType>(sourceContainer->contentType().abstractType());
            v.lastDeclaration()->setType(container);
        }
    };

    foreach ( const QString& key, items.keys() ) {
        if ( Helper::docstringContainsHint(function.data(), key, &args) ) {
            items[key]();
        }
    }
}

void DeclarationBuilder::addArgumentTypeHints(CallAst* node, DeclarationPointer function)
{
    DUChainReadLocker lock;
    QPair<FunctionDeclaration::Ptr, bool> called = Helper::functionDeclarationForCalledDeclaration(function);
    FunctionDeclaration::Ptr lastFunctionDeclaration = called.first;
    bool isConstructor = called.second;

    if ( ! lastFunctionDeclaration ) {
        return;
    }
    if ( lastFunctionDeclaration->topContext()->url() == IndexedString(Helper::getDocumentationFile()) ) {
        return;
    }
    DUContext* args = DUChainUtils::getArgumentContext(lastFunctionDeclaration.data());
    FunctionType::Ptr functiontype = lastFunctionDeclaration->type<FunctionType>();
    if ( ! args || ! functiontype ) {
        return;
    }
    // The declaration which was found is a function declaration, and has a valid arguments list assigned.
    QVector<Declaration*> parameters = args->localDeclarations();
    const int specialParamsCount = (lastFunctionDeclaration->vararg() > 0) + (lastFunctionDeclaration->kwarg() > 0);

    // Look for the "self" in the argument list, the type of that should not be updated.
    bool hasSelfArgument = false;
    if ( ( lastFunctionDeclaration->context()->type() == DUContext::Class || isConstructor )
            && ! parameters.isEmpty() && ! lastFunctionDeclaration->isStatic() )
    {
        // ... unless for some reason the function only has *vararg, **kwarg as arguments
        // (this could happen for example if the method is static but kdev-python does not know,
        // or if the user just made a mistake in his code)
        if ( specialParamsCount < parameters.size() ) {
            hasSelfArgument = true;
        }
    }
    int currentParamIndex = hasSelfArgument;
    int currentArgumentIndex = 0;
    int indexInVararg = -1;
    int paramsAvailable = qMin(functiontype->arguments().length() + hasSelfArgument, parameters.size());
    int argsAvailable = node->arguments.size();
    bool atVararg = false;

    lock.unlock();

    // Iterate over all the arguments, trying to guess the type of the object being
    // passed as an argument, and update the parameter accordingly.
    // Stop if more parameters supplied than possible, and we're not at the vararg.
    for ( ; ( atVararg || currentParamIndex < paramsAvailable ) && currentArgumentIndex < argsAvailable;
            currentParamIndex++, currentArgumentIndex++ )
    {
        if ( ! atVararg && currentArgumentIndex == lastFunctionDeclaration->vararg() ) {
            atVararg = true;
        }

        kDebug() << currentParamIndex << currentArgumentIndex << atVararg << lastFunctionDeclaration->vararg();

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

        // Update the parameter type: change both the type of the function argument,
        // and the type of the declaration which belongs to that argument
        DUChainWriteLocker wlock;
        if ( atVararg ) {
            indexInVararg++;
            Declaration* parameter = parameters.at(lastFunctionDeclaration->vararg()+hasSelfArgument);
            IndexedContainer::Ptr varargContainer = parameter->type<IndexedContainer>();
            kDebug() << "adding" << addType->toString() << "at position" << indexInVararg;
            if ( ! varargContainer ) continue;
            if ( varargContainer->typesCount() > indexInVararg ) {
                AbstractType::Ptr oldType = varargContainer->typeAt(indexInVararg).abstractType();
                AbstractType::Ptr newType = Helper::mergeTypes(oldType, addType.cast<AbstractType>());
                varargContainer->replaceType(indexInVararg, newType);
            }
            else {
                varargContainer->addEntry(addType.cast<AbstractType>());
            }
            parameter->setAbstractType(varargContainer.cast<AbstractType>());
        }
        else {
            if ( ! argumentType ) continue;
            AbstractType::Ptr newType = Helper::mergeTypes(parameters.at(currentParamIndex)->abstractType(),
                                                            addType.cast<AbstractType>());
            // TODO this does not correctly update the types in quickopen! Investigate why.
            functiontype->removeArgument(currentArgumentIndex + hasSelfArgument);
            functiontype->addArgument(newType, currentArgumentIndex + hasSelfArgument);
            lastFunctionDeclaration->setAbstractType(functiontype.cast<AbstractType>());
            parameters.at(currentParamIndex)->setType(newType);
        }
    }

    lock.unlock();
    DUChainWriteLocker wlock;
    if ( lastFunctionDeclaration->kwarg() < 0 || parameters.isEmpty() ) {
        // no kwarg, stop here.
        return;
    }
    foreach ( KeywordAst* keyword, node->keywords ) {
        AbstractType::Ptr param = parameters.last()->abstractType();
        auto list = param.cast<ListType>();
        if ( ! list ) {
            continue;
        }
        wlock.unlock();
        ExpressionVisitor argumentVisitor(currentContext());
        argumentVisitor.visitNode(keyword->value);
        if ( ! argumentVisitor.lastType() ) {
            continue;
        }
        wlock.lock();
        HintedType::Ptr addType = HintedType::Ptr(new HintedType());
        openType(addType);
        addType->setType(argumentVisitor.lastType());
        addType->setCreatedBy(topContext(), m_futureModificationRevision);
        closeType();
        list->addContentType<Python::UnsureType>(addType.cast<AbstractType>());
        parameters.last()->setAbstractType(list.cast<AbstractType>());
    }
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

QList<ExpressionAst*> DeclarationBuilder::targetsOfAssignment(QList<ExpressionAst*> targets) const
{
    QList<ExpressionAst*> lhsExpressions;
    foreach ( ExpressionAst* target, targets ) {
        if ( target->astType == Ast::TupleAstType ) {
            TupleAst* tuple = static_cast<TupleAst*>(target);
            foreach ( ExpressionAst* ast, tuple->elements ) {
                // eventually recursive call, to handle e.g. a, (b, c) = 1, 2, 3 correctly
                if ( ast->astType == Ast::TupleAstType ) {
                    lhsExpressions << targetsOfAssignment(QList<ExpressionAst*>() << ast);
                }
                else {
                    // shortcut
                    lhsExpressions << ast;
                }
            }
        }
        else {
            lhsExpressions << target;
        }
    }
    return lhsExpressions;
}

QList<DeclarationBuilder::SourceType> DeclarationBuilder::sourcesOfAssignment(ExpressionAst* items,
                                                                              int fillWhenLengthMissing) const
{
    QList<SourceType> sources;
    QList<ExpressionAst*> values;

    if ( items && items->astType == Ast::TupleAstType ) {
        values = static_cast<TupleAst*>(items)->elements;
    }
    else {
        // This handles the a, b, c = [1, 2, 3] case. Since the assignment can also be like
        // d = [1, 2, 3]; a, b, c = d we can't don't generally know the amount of elements
        // in the right operand; so all elements are treated to have the same type.
        if ( fillWhenLengthMissing > 0 ) {
            ExpressionVisitor v(currentContext());
            v.visitNode(items);
            auto container = ListType::Ptr::dynamicCast(v.lastType());
            if ( container ) {
                AbstractType::Ptr content = container->contentType().abstractType();
                for ( ; fillWhenLengthMissing != 0; fillWhenLengthMissing-- ) {
                    sources << SourceType{ content, KDevelop::DeclarationPointer(), false };
                }
                return sources;
            }
        }

        // Otherwise, proceed normally.
        values << items;
    }

    foreach ( ExpressionAst* value, values ) {
        ExpressionVisitor v(currentContext());
        v.visitNode(value);

        sources << SourceType{
            v.lastType(),
            DeclarationPointer(Helper::resolveAliasDeclaration(v.lastDeclaration().data())),
            v.isAlias()
        };
    }
    return sources;
}

DeclarationBuilder::SourceType DeclarationBuilder::selectSource(const QList<ExpressionAst*>& targets,
                                                                const QList<DeclarationBuilder::SourceType>& sources,
                                                                int index, ExpressionAst* rhs) const
{
    bool canUnpack = targets.length() == sources.length();
    SourceType element;
    // If the length of the right and the left side matches, exact unpacking can be done.
    // example code: a, b, c = 3, 4, 5
    // If the left side only contains one entry, unpacking never happens, and the left side
    // is instead assigned a container type if applicable
    // example code: a = 3, 4, 5
    if ( canUnpack ) {
        element = sources.at(index);
    }
    else if ( targets.length() == 1 ) {
        ExpressionVisitor v(currentContext());
        v.visitNode(rhs);
        element = SourceType{
            v.lastType(),
            DeclarationPointer(Helper::resolveAliasDeclaration(v.lastDeclaration().data())),
            v.isAlias()
        };
    }
    else if ( ! sources.isEmpty() ) {
        // the assignment is of the form "foo, bar, ... = ..." (tuple unpacking)
        // this one is for the case that the tuple unpacking is not written down explicitly, for example
        // a = (1, 2, 3); b, c, d = a
        // the other case (b, c, d = 1, 2, 3) is handled above.
        if ( const IndexedContainer::Ptr container = sources.first().type.cast<IndexedContainer>() ) {
            if ( container->typesCount() == targets.length() ) {
                element.type = container->typeAt(index).abstractType();
                element.isAlias = false;
            }
        }
    }
    if ( ! element.type ) {
        // use mixed if none of the previous ways of determining the type worked.
        element.type = AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed));
        element.declaration = nullptr;
        element.isAlias = false;
    }
    return element;
}

void DeclarationBuilder::assignToName(NameAst* target, const DeclarationBuilder::SourceType& element)
{
    if ( element.isAlias ) {
        DUChainWriteLocker lock;
        Python::Identifier* identifier = target->identifier;
        AliasDeclaration* decl = eventuallyReopenDeclaration<AliasDeclaration>(identifier, target, AliasDeclarationType);
        decl->setAliasedDeclaration(element.declaration.data());
        closeDeclaration();
    }
    else {
        DUChainWriteLocker lock;
        Declaration* dec = visitVariableDeclaration<Declaration>(target, 0, element.type);
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
    auto list = ListType::Ptr::dynamicCast(targetVisitor.lastType());
    if ( list ) {
        list->addContentType<Python::UnsureType>(element.type);
    }
    auto map = MapType::Ptr::dynamicCast(list);
    if ( map ) {
        if ( subscript->slice && subscript->slice->astType == Ast::IndexAstType ) {
            ExpressionVisitor keyVisitor(currentContext());
            keyVisitor.visitNode(static_cast<IndexAst*>(subscript->slice)->value);
            AbstractType::Ptr key = keyVisitor.lastType();
            if ( key ) {
                map->addKeyType<Python::UnsureType>(key);
            }
        }
    }
    DeclarationPointer lastDecl = targetVisitor.lastDeclaration();
    if ( list && lastDecl ) {
        DUChainWriteLocker lock;
        lastDecl->setAbstractType(list.cast<AbstractType>());
    }
}

void DeclarationBuilder::assignToAttribute(AttributeAst* attrib, const DeclarationBuilder::SourceType& element)
{
    // check whether the current attribute is undeclared, but the previos ones known
    // like in X.Y.Z = 3 where X and Y are defined, but Z isn't; then declare Z.
    ExpressionVisitor checkForUnknownAttribute(currentContext());
    checkForUnknownAttribute.visitNode(attrib);
    Declaration* haveDeclaration = 0;
    {
        DUChainReadLocker lock;
        haveDeclaration = checkForUnknownAttribute.lastDeclaration().data();
    }

    // declare the attribute.
    // however, if there's an earlier declaration which does not match the current position
    // (so it's really a different declaration) we skip this.
    ExpressionVisitor checkPreviousAttributes(currentContext());
    // go "down one level", so only visit "X.Y"
    checkPreviousAttributes.visitNode(attrib->value);

    DUContextPointer internal(0);
    DeclarationPointer parentObjectDeclaration = checkPreviousAttributes.lastDeclaration();

    if ( ! parentObjectDeclaration ) {
        kDebug() << "No declaration for attribute base, aborting creation of attribute";
        return;
    }
    // if foo is a class, this is like foo.bar = 3
    if ( parentObjectDeclaration->internalContext() ) {
        internal = parentObjectDeclaration->internalContext();
    }
    // while this is like A = foo(); A.bar = 3
    else {
        StructureType::Ptr structure(parentObjectDeclaration->abstractType().cast<StructureType>());
        if ( ! structure || ! structure->declaration(topContext()) ) {
            return;
        }
        parentObjectDeclaration = structure->declaration(topContext());
        internal = parentObjectDeclaration->internalContext();
    }
    if ( ! internal ) {
        kDebug() << "No internal context for structure type, aborting creation of attribute declaration";
        return;
    }

    DUContext* previousContext = currentContext();
    bool isAlreadyOpen = contextAlreayOpen(internal);
    if ( isAlreadyOpen ) {
        activateAlreadyOpenedContext(internal);
        visitVariableDeclaration<ClassMemberDeclaration>(
            attrib->attribute, attrib, haveDeclaration, element.type
        );
        closeAlreadyOpenedContext(internal);
    }
    else {
        injectContext(internal.data());

        Declaration* dec = visitVariableDeclaration<ClassMemberDeclaration>(
            attrib->attribute, attrib, haveDeclaration, element.type
        );
        if ( dec ) {
            dec->setRange(RangeInRevision(internal->range().start, internal->range().start));
            dec->setAutoDeclaration(true);
            DUChainWriteLocker lock;
            previousContext->createUse(dec->ownIndex(), editorFindRange(attrib, attrib));
        }
        else kWarning() << "No declaration created for " << attrib->attribute << "as parent is not a class";

        closeInjectedContext();
    }
}

void DeclarationBuilder::visitAssignment(AssignmentAst* node)
{
    AstDefaultVisitor::visitAssignment(node);
    // Because of tuple unpacking, it is required to gather the left- and right hand side
    // expressions / types first, then match them together in a second step.
    const QList<ExpressionAst*>& targets = targetsOfAssignment(node->targets);
    const QList<SourceType>& sources = sourcesOfAssignment(node->value, targets.size() > 1 ? targets.size() : -1);

    // Now all the information about left- and right hand side entries is ready,
    // and creation / updating of variables can start.
    int i = 0;
    foreach ( ExpressionAst* target, targets ) {
        SourceType element = std::move(selectSource(targets, sources, i, node->value));

        // Handling the tuple unpacking stuff is done now, and we can proceed as if there was no tuple unpacking involved.
        if ( target->astType == Ast::NameAstType ) {
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
        i += 1;
    }
}

void DeclarationBuilder::visitClassDefinition( ClassDefinitionAst* node )
{
    const CorrectionHelper::Recursion r(m_correctionHelper->enterClass(node->name->value));

    StructureType::Ptr type(new StructureType());
    
    DUChainWriteLocker lock;
    ClassDeclaration* dec = eventuallyReopenDeclaration<ClassDeclaration>(node->name, node->name, NoTypeRequired);
    lock.unlock();
    visitDecorators<ClassDeclaration>(node->decorators, dec);
    lock.lock();
    eventuallyAssignInternalContext();
    
    dec->setKind(KDevelop::Declaration::Type);
    dec->clearBaseClasses();
    dec->setClassType(ClassDeclarationData::Class);
    
    // check whether this is a type container (list, dict, ...) or just a "normal" class
    if ( Helper::docstringContainsHint(dec, "TypeContainer") ) {
        ListType* container = nullptr;
        if ( Helper::docstringContainsHint(dec, "hasTypedKeys") ) {
            container = new MapType();
        }
        else {
            container = new ListType();
        }
        type = StructureType::Ptr(container);
    }
    if ( Helper::docstringContainsHint(dec, "IndexedTypeContainer") ) {
        IndexedContainer* container = new IndexedContainer();
        type = StructureType::Ptr(container);
    }
    
    lock.unlock();
    foreach ( ExpressionAst* c, node->baseClasses ) {
        // Iterate over all the base classes, and add them to the duchain.
        ExpressionVisitor v(currentContext());
        v.visitNode(c);
        if ( v.lastType() && v.lastType()->whichType() == AbstractType::TypeStructure ) {
            StructureType::Ptr baseClassType = v.lastType().cast<StructureType>();
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
    if ( dec->baseClassesSize() == 0 and node->name->value != "object" ) {
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
    m_currentClassType = type;

    // needs to be done here, so the assignment of the internal context happens before visiting the body
    openContextForClassDefinition(node);
    dec->setInternalContext(currentContext());

    lock.unlock();
    foreach ( Ast* node, node->body ) {
        AstDefaultVisitor::visitNode(node);
    }
    lock.lock();
    
    closeContext();
    closeType();
    closeDeclaration();
    
    dec->setComment(getDocstring(node->body));
}

template<typename T> void DeclarationBuilder::visitDecorators(QList< Python::ExpressionAst* > decorators, T* addTo) {
    foreach ( ExpressionAst* decorator, decorators ) {
        AstDefaultVisitor::visitNode(decorator);
        if ( decorator->astType == Ast::CallAstType ) {
            CallAst* call = static_cast<CallAst*>(decorator);
            Decorator d;
            if ( call->function->astType != Ast::NameAstType ) {
                continue;
            }
            d.setName(*static_cast<NameAst*>(call->function)->identifier);
            foreach ( ExpressionAst* arg, call->arguments ) {
                if ( arg->astType == Ast::NumberAstType ) {
                    d.setAdditionalInformation(QString::number(static_cast<NumberAst*>(arg)->value));
                }
                else if ( arg->astType == Ast::StringAstType ) {
                    d.setAdditionalInformation(static_cast<StringAst*>(arg)->value);
                }
                break; // we only need the first argument for documentation analysis
            }
            addTo->addDecorator(d);
        }
        else if ( decorator->astType == Ast::NameAstType ) {
            NameAst* name = static_cast<NameAst*>(decorator);
            Decorator d;
            d.setName(*(name->identifier));
            addTo->addDecorator(d);
        }
    }
}

void DeclarationBuilder::visitFunctionDefinition( FunctionDefinitionAst* node )
{
    const CorrectionHelper::Recursion r(m_correctionHelper->enterFunction(node->name->value));

    // Search for an eventual containing class declaration;
    // if that exists, then this function is a member function
    DeclarationPointer eventualParentDeclaration(currentDeclaration());
    FunctionType::Ptr type(new FunctionType());

    DUChainWriteLocker lock;
    FunctionDeclaration* dec = eventuallyReopenDeclaration<FunctionDeclaration>(node->name, node->name,
                                                                                FunctionDeclarationType);

    Q_ASSERT(dec->isFunctionDeclaration());
    
    // check for documentation
    dec->setComment(getDocstring(node->body));
    
    openType(type);
    dec->setInSymbolTable(false);
    dec->setType(type);
    
    lock.unlock();
    visitDecorators<FunctionDeclaration>(node->decorators, dec);
    visitFunctionArguments(node);
    
    lock.lock();
    const bool isStatic = Helper::findDecoratorByName<FunctionDeclaration>(dec, "staticmethod");
    const bool isClassMethod = Helper::findDecoratorByName<FunctionDeclaration>(dec, "classmethod");
    
    // If this is a member function, set the type of the first argument (the "self") to be
    // an instance of the class.
    // this must be done here, because the type of self must be known when parsing the body
    if ( eventualParentDeclaration && currentType<FunctionType>()->arguments().length()
            && currentContext()->type() == DUContext::Class && ! isStatic )
    {
        if ( dec->vararg() != -1 ) {
            dec->setVararg(dec->vararg() - 1);
        }
        if ( dec->kwarg() != -1 ) {
            dec->setKwarg(dec->kwarg() - 1);
        }
    }

    lock.unlock();
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
            type->setReturnType(AbstractType::Ptr(new IntegralType(IntegralType::TypeVoid)));
        }
        dec->setType(type);
    }

    if ( ! isStatic ) {
        DUContext* args = DUChainUtils::getArgumentContext(dec);
        if ( args )  {
            QVector<Declaration*> parameters = args->localDeclarations();
            static IndexedString newMethodName("__new__");
            static IndexedString selfArgumentName("self");
            static IndexedString clsArgumentName("cls");
            if ( currentContext()->type() == DUContext::Class && ! parameters.isEmpty() && ! isClassMethod ) {
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
                    p->setSource(KDevelop::ProblemData::SemanticAnalysis);
                    p->setSeverity(KDevelop::ProblemData::Warning);
                    ProblemPointer ptr(p);
                    topContext()->addProblem(ptr);
                }
            }
            else if ( currentContext()->type() == DUContext::Class && parameters.isEmpty() ) {
                DUChainWriteLocker lock;
                KDevelop::Problem *p = new KDevelop::Problem();
                 // only mark first line
                p->setFinalLocation(DocumentRange(currentlyParsedDocument(), KTextEditor::Range(node->startLine, node->startCol, node->startLine, 10000)));
                p->setSource(KDevelop::ProblemData::SemanticAnalysis);
                p->setSeverity(KDevelop::ProblemData::Warning);
                p->setDescription(i18n("Non-static class method without arguments, must have at least one (self)"));
                ProblemPointer ptr(p);
                topContext()->addProblem(ptr);
            }
        }
    }
    else {
        dec->setStatic(true);
    }

    if ( AbstractType::Ptr hint = m_correctionHelper->returnTypeHint() ) {
        type->setReturnType(hint);
        dec->setType<FunctionType>(type);
    }
    
    // check for (python3) function annotations
    if ( node->returns ) {
        lock.unlock();
        ExpressionVisitor v(currentContext());
        v.visitNode(node->returns);
        lock.lock();
        if ( v.lastType() && v.isAlias() ) {
            type->setReturnType(Helper::mergeTypes(type->returnType(), v.lastType()));
            kDebug() << "updated function return type to " << type->toString();
            dec->setType(type);
        }
        else if ( ! v.isAlias()) {
            kDebug() << "not updating function return type because expression is not a type object";
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
    // Find the type of the object being "return"ed
    ExpressionVisitor v(currentContext());
    v.visitNode(node->value);
    
    if ( node->value ) {
        if ( ! hasCurrentType() ) {
            DUChainWriteLocker lock(DUChain::lock());
            KDevelop::Problem *p = new KDevelop::Problem();
            p->setFinalLocation(DocumentRange(currentlyParsedDocument(), node->range())); // only mark first line
            p->setSource(KDevelop::ProblemData::SemanticAnalysis);
            p->setDescription(i18n("Return statement not within function declaration"));
            ProblemPointer ptr(p);
            topContext()->addProblem(ptr);
            return;
        }
        TypePtr<FunctionType> t = currentType<FunctionType>();
        AbstractType::Ptr encountered = v.lastType();
        DUChainWriteLocker lock;
        if ( t ) {
            // Update the containing function's return type
            t->setReturnType(Helper::mergeTypes(t->returnType(), encountered));
        }
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
    int currentIndex = 0;
    kDebug() << "arguments:" << node->arguments.size();
    foreach ( ArgAst* arg, node->arguments ) {
        // Iterate over all the function's arguments, create declarations, and add the arguments
        // to the functions FunctionType.
        currentIndex += 1;

        if ( ! arg->argumentName ) {
            continue;
        }

        kDebug() << "visiting argument:" << arg->argumentName->value;

        // Create a variable declaration for the parameter, to be used in the function body.
        Declaration* paramDeclaration = visitVariableDeclaration<Declaration>(arg->argumentName);
        if ( ! paramDeclaration ) {
            kDebug() << "could not create parameter declaration!";
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
        else if ( currentIndex > firstDefaultParameterOffset ) {
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

        kDebug() << "is first:" << isFirst << hasCurrentDeclaration() << currentDeclaration();
        if ( isFirst && hasCurrentDeclaration() && currentContext() && currentContext()->parentContext() ) {
            DUChainReadLocker lock;
            if ( currentContext()->parentContext()->type() == DUContext::Class ) {
                argumentType = m_currentClassType.cast<AbstractType>();
                isFirst = false;
            }
        }

        DUChainWriteLocker lock;
        paramDeclaration->setAbstractType(Helper::mergeTypes(paramDeclaration->abstractType(), argumentType));
        type->addArgument(argumentType);
        if ( argumentType ) {
            kDebug() << "creating argument with type" << argumentType->toString();
        }
    }
    // Handle *args, **kwargs, and assign them a list / dictionary type.
    if ( node->vararg ) {
        // inject the vararg at the correct place
        int atIndex = 0;
        int useIndex = -1;
        foreach ( ArgAst* arg, node->arguments ) {
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
        IndexedContainer::Ptr tupleType = ExpressionVisitor::typeObjectForIntegralType
                                                            <IndexedContainer>("tuple", currentContext());
        lock.unlock();
        if ( tupleType ) {
            visitVariableDeclaration<Declaration>(node->vararg->argumentName, 0, tupleType.cast<AbstractType>());
            workingOnDeclaration->setVararg(atIndex);
            type->addArgument(tupleType.cast<AbstractType>(), useIndex);
        }
    }

    if ( node->kwarg ) {
        DUChainReadLocker lock;
        AbstractType::Ptr stringType = ExpressionVisitor::typeObjectForIntegralType
                                                        <AbstractType>("str", currentContext());
        auto dictType = ExpressionVisitor::typeObjectForIntegralType
                                                        <MapType>("dict", currentContext());
        lock.unlock();
        if ( dictType && stringType ) {
            dictType->addKeyType<Python::UnsureType>(stringType);
            visitVariableDeclaration<Declaration>(node->kwarg->argumentName, 0, dictType.cast<AbstractType>());
            type->addArgument(dictType.cast<AbstractType>());
            workingOnDeclaration->setKwarg(type->arguments().size() - 1);
        }
    }
}

void DeclarationBuilder::visitGlobal(GlobalAst* node)
{
    TopDUContext* top = topContext();
    foreach ( Identifier *id, node->names ) {
        QualifiedIdentifier qid = identifierForNode(id);
        DUChainWriteLocker lock;
        QList< Declaration* > existing = top->findLocalDeclarations(qid.first());
        if ( ! existing.empty() ) {
            AliasDeclaration* ndec = openDeclaration<AliasDeclaration>(id, node);
            ndec->setAliasedDeclaration(existing.first());
            closeDeclaration();
        }
        else {
            injectContext(top);
            Declaration* dec = visitVariableDeclaration<Declaration>(id);
            dec->setRange(editorFindRange(id, id));
            dec->setAutoDeclaration(true);
            closeContext();
            AliasDeclaration* ndec = openDeclaration<AliasDeclaration>(id, node);
            ndec->setAliasedDeclaration(dec);
            closeDeclaration();
        }
    }
}

}


