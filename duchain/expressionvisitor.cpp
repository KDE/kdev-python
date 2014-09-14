/*****************************************************************************
 * This file is part of KDevelop                                             *
 * Copyright 2010 Miquel Canes Gonzalez <miquelcanes@gmail.com>              *
 * Copyright 2011-2013 by Sven Brauch <svenbrauch@googlemail.com>            *
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

#include "expressionvisitor.h"
#include "types/indexedcontainer.h"
#include "declarations/functiondeclaration.h"
#include "pythonduchainexport.h"
#include "pythoneditorintegrator.h"
#include "helpers.h"

#include <language/duchain/types/containertypes.h>
#include <language/duchain/types/unsuretype.h>
#include <language/duchain/types/integraltype.h>
#include <language/duchain/types/typeregister.h>
#include <language/duchain/types/typesystemdata.h>
#include <language/duchain/types/functiontype.h>
#include <language/duchain/declaration.h>
#include <language/duchain/functiondeclaration.h>
#include <language/duchain/classdeclaration.h>
#include <language/duchain/aliasdeclaration.h>
#include <language/duchain/ducontext.h>

#include <QDebug>
#include "duchaindebug.h"

#include <KLocalizedString>

#include <functional>

using namespace KDevelop;
using namespace Python;
using namespace KTextEditor;

namespace Python {

QHash<NameConstantAst::NameConstantTypes, KDevelop::AbstractType::Ptr> ExpressionVisitor::m_defaultTypes;

AbstractType::Ptr ExpressionVisitor::encounterPreprocess(AbstractType::Ptr type)
{
    return Helper::resolveAliasType(type);
}

ExpressionVisitor::ExpressionVisitor(const DUContext* ctx)
    : DynamicLanguageExpressionVisitor(ctx)
{
    ENSURE_CHAIN_NOT_LOCKED
    if ( m_defaultTypes.isEmpty() ) {
        m_defaultTypes.insert(NameConstantAst::True, AbstractType::Ptr(new IntegralType(IntegralType::TypeBoolean)));
        m_defaultTypes.insert(NameConstantAst::False, AbstractType::Ptr(new IntegralType(IntegralType::TypeBoolean)));
        m_defaultTypes.insert(NameConstantAst::None, AbstractType::Ptr(new IntegralType(IntegralType::TypeVoid)));
    }
    Q_ASSERT(context());
    Q_ASSERT(context()->topContext());
}

ExpressionVisitor::ExpressionVisitor(ExpressionVisitor* parent, const DUContext* overrideContext)
    : DynamicLanguageExpressionVisitor(parent)
    , m_forceGlobalSearching(parent->m_forceGlobalSearching)
    , m_reportUnknownNames(parent->m_reportUnknownNames)
    , m_scanUntilCursor(parent->m_scanUntilCursor)
{
    ENSURE_CHAIN_NOT_LOCKED
    if ( overrideContext ) {
        m_context = overrideContext;
    }
    Q_ASSERT(context());
}

void ExpressionVisitor::encounter(AbstractType::Ptr type, DeclarationPointer declaration, bool alias)
{
    setLastIsAlias(alias);
    DynamicLanguageExpressionVisitor::encounter(type, declaration);
}

void ExpressionVisitor::visitAttribute(AttributeAst* node)
{
    ExpressionAst* accessingAttributeOf = node->value;

    ExpressionVisitor v(this);
    v.visitNode(accessingAttributeOf);
    AbstractType::Ptr accessedType = v.lastType();
    QList<StructureType::Ptr> accessingAttributeOfType = Helper::filterType<StructureType>(accessedType,
        [](AbstractType::Ptr type) {
            auto resolved = Helper::resolveAliasType(type);
            return resolved && resolved->whichType() == AbstractType::TypeStructure;
        },
        [](AbstractType::Ptr type) {
            return Helper::resolveAliasType(type).cast<StructureType>();
        }
    );

    // Step 1: Find all matching declarations which are made inside the type of which the accessed object is.
    // Like, for A.B.C where B is an instance of foo, when processing C, find all properties of foo which are called C.
    bool haveOneUsefulType = false;
    Declaration* foundDeclaration = nullptr;
    DUChainReadLocker lock;
    foreach ( StructureType::Ptr current, accessingAttributeOfType ) {
        if ( Helper::isUsefulType(current.cast<AbstractType>()) ) {
            haveOneUsefulType = true;
        }
        foundDeclaration = Helper::accessAttribute(current->declaration(context()->topContext()),
                                                   node->attribute->value, context());
        if ( foundDeclaration ) {
            break;
        }
    }
    if ( ! haveOneUsefulType ) {
        setConfident(false);
    }

    // Step 2: Construct the type of the declaration which was found.
    if ( foundDeclaration ) {
        auto d = Helper::resolveAliasDeclaration(foundDeclaration);
        if ( ! d ) {
            return encounterUnknown();
        }
        bool isAlias =     dynamic_cast<AliasDeclaration*>(foundDeclaration) || d->isFunctionDeclaration()
                        || dynamic_cast<ClassDeclaration*>(d);
        encounter(foundDeclaration->abstractType(), DeclarationPointer(foundDeclaration));
        setLastIsAlias(isAlias);
    }
    else {
        return encounterUnknown();
    }
}

void ExpressionVisitor::visitCall(CallAst* node)
{
    foreach ( ExpressionAst* c, node->arguments ) {
        AstDefaultVisitor::visitNode(c);
    }
    AstDefaultVisitor::visitNode(node->keywordArguments);
    AstDefaultVisitor::visitNode(node->starArguments);
    
    ExpressionVisitor v(this);
    v.visitNode(node->function);
    Declaration* actualDeclaration = 0;
    FunctionType::Ptr unidentifiedFunctionType;
    if ( ! v.m_isAlias && v.lastType() && v.lastType()->whichType() == AbstractType::TypeFunction ) {
        unidentifiedFunctionType = v.lastType().cast<FunctionType>();
    }
    else {
        actualDeclaration = v.lastDeclaration().data();
    }
    
    if ( unidentifiedFunctionType ) {
        encounter(unidentifiedFunctionType->returnType());
        return;
    }
    else if ( !actualDeclaration ) {
        setConfident(false);
        return encounterUnknown();
    }

    DUChainReadLocker lock;
    actualDeclaration = Helper::resolveAliasDeclaration(actualDeclaration);
    ClassDeclaration* classDecl = dynamic_cast<ClassDeclaration*>(actualDeclaration);
    QPair<FunctionDeclarationPointer, bool> d = Helper::functionDeclarationForCalledDeclaration(
                                                DeclarationPointer(actualDeclaration));
    FunctionDeclaration* funcDecl = d.first.data();
    bool isConstructor = d.second;
    lock.unlock();

    if ( funcDecl && funcDecl->type<FunctionType>() ) {
        // try to deduce type from a decorator
        checkForDecorators(node, funcDecl, classDecl, isConstructor);
    }
    else if ( classDecl ) {
        return encounter(classDecl->abstractType(), DeclarationPointer(classDecl));
    }
    else {
        if ( actualDeclaration ) {
            qCDebug(KDEV_PYTHON_DUCHAIN) << "Declaraton is not a class or function declaration";
        }
        return encounterUnknown();
    }
}

void ExpressionVisitor::checkForDecorators(CallAst* node, FunctionDeclaration* funcDecl, ClassDeclaration* classDecl, bool isConstructor)
{
    AbstractType::Ptr type;
    Declaration* useDeclaration = nullptr;
    if ( isConstructor && classDecl ) {
        type = classDecl->abstractType();
        useDeclaration = classDecl;
    }
    else {
        type = funcDecl->type<FunctionType>()->returnType();
        useDeclaration = funcDecl;
    }

    auto listOfTuples = [&](AbstractType::Ptr key, AbstractType::Ptr value) {
        auto newType = typeObjectForIntegralType<ListType>("list", context());
        IndexedContainer::Ptr newContents = typeObjectForIntegralType<IndexedContainer>("tuple", context());
        if ( ! newType || ! newContents ) {
            return AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed));
        }
        if ( ! key ) {
            key = AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed));
        }
        if ( ! value ) {
            value = AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed));
        }
        newContents->addEntry(key);
        newContents->addEntry(value);
        newType->addContentType<Python::UnsureType>(AbstractType::Ptr::staticCast(newContents));
        AbstractType::Ptr resultingType = AbstractType::Ptr::staticCast(newType);
        return resultingType;
    };

    QHash< QString, std::function<bool(QStringList, QString)> > knownDecoratorHints;
    qCDebug(KDEV_PYTHON_DUCHAIN) << "Got function declaration with decorators, checking for list content type...";
    knownDecoratorHints["getsType"] = [&](QStringList /*arguments*/, QString /*currentHint*/) {
        if ( node->function->astType != Ast::AttributeAstType ) {
            return false;
        }
        ExpressionVisitor baseTypeVisitor(this);
        // when calling foo.bar[3].baz.iteritems(), find the type of "foo.bar[3].baz"
        baseTypeVisitor.visitNode(static_cast<AttributeAst*>(node->function)->value);
        if ( auto t = baseTypeVisitor.lastType().cast<ListType>() ) {
            qCDebug(KDEV_PYTHON_DUCHAIN) << "Found container, using type";
            AbstractType::Ptr newType = t->contentType().abstractType();
            encounter(newType, DeclarationPointer(useDeclaration));
            return true;
        }
        return false;
    };

    knownDecoratorHints["getsList"] = [&](QStringList /*arguments*/, QString currentHint) {
        if ( node->function->astType != Ast::AttributeAstType ) {
            return false;
        }
        ExpressionVisitor baseTypeVisitor(this);
        // when calling foo.bar[3].baz.iteritems(), find the type of "foo.bar[3].baz"
        baseTypeVisitor.visitNode(static_cast<AttributeAst*>(node->function)->value);
        DUChainWriteLocker lock;
        if ( auto t = baseTypeVisitor.lastType().cast<ListType>() ) {
            qCDebug(KDEV_PYTHON_DUCHAIN) << "Got container:" << t->toString();
            auto newType = typeObjectForIntegralType<ListType>("list", context());
            if ( ! newType ) {
                return false;
            }
            AbstractType::Ptr contentType;
            if ( currentHint == "getsList" ) {
                contentType = t->contentType().abstractType();
            }
            else if ( auto map = MapType::Ptr::dynamicCast(t) ) {
                contentType = map->keyType().abstractType();
            }
            newType->addContentType<Python::UnsureType>(contentType);
            AbstractType::Ptr resultingType = newType.cast<AbstractType>();
            encounter(resultingType, DeclarationPointer(useDeclaration));
            return true;
        }
        return false;
    };
    knownDecoratorHints["getListOfKeys"] = knownDecoratorHints["getsList"];

    knownDecoratorHints["enumerate"] = [&](QStringList /*arguments*/, QString /*currentHint*/) {
        if ( node->function->astType != Ast::NameAstType || node->arguments.size() < 1 ) {
            return false;
        }
        ExpressionVisitor enumeratedTypeVisitor(this);
        enumeratedTypeVisitor.visitNode(node->arguments.first());

        DUChainWriteLocker lock;
        auto intType = typeObjectForIntegralType<AbstractType>("int", context());
        auto enumerated = enumeratedTypeVisitor.lastType();
        auto result = listOfTuples(intType, Helper::contentOfIterable(enumerated));
        encounter(result, DeclarationPointer(useDeclaration));
        return true;
    };

    knownDecoratorHints["getsListOfBoth"] = [&](QStringList /*arguments*/, QString /*currentHint*/) {
        qCDebug(KDEV_PYTHON_DUCHAIN) << "Got getsListOfBoth decorator, checking container";
        if ( node->function->astType != Ast::AttributeAstType ) {
            return false;
        }
        ExpressionVisitor baseTypeVisitor(this);
        // when calling foo.bar[3].baz.iteritems(), find the type of "foo.bar[3].baz"
        baseTypeVisitor.visitNode(static_cast<AttributeAst*>(node->function)->value);
        DUChainWriteLocker lock;
        if ( auto t = baseTypeVisitor.lastType().cast<MapType>() ) {
            qCDebug(KDEV_PYTHON_DUCHAIN) << "Got container:" << t->toString();
            auto resultingType = listOfTuples(t->keyType().abstractType(), t->contentType().abstractType());
            encounter(resultingType, DeclarationPointer(useDeclaration));
            return true;
        }
        return false;
    };

    knownDecoratorHints["returnContentEqualsContentOf"] = [&](QStringList arguments, QString /*currentHint*/) {
        int argNum = ! arguments.isEmpty() ? arguments.at(0).toInt() : 0;
        qCDebug(KDEV_PYTHON_DUCHAIN) << "Found argument dependent decorator, checking argument type" << argNum;
        if ( argNum >= node->arguments.length() ) {
            return false;
        }
        ExpressionAst* relevantArgument = node->arguments.at(argNum);
        ExpressionVisitor v(this);
        v.visitNode(relevantArgument);
        if ( ! v.lastType() ) {
            return false;
        }
        ListType::Ptr realTarget;
        if ( auto target = ListType::Ptr::dynamicCast(type) ) {
            realTarget = target;
        }
        if ( auto source = ListType::Ptr::dynamicCast(v.lastType()) ) {
            if ( ! realTarget ) {
                // if the function does not force a return type, just copy the source (like for reversed())
                realTarget = source;
            }
            auto newType = ListType::Ptr::staticCast(AbstractType::Ptr(realTarget->clone()));
            Q_ASSERT(newType);
            newType->addContentType<Python::UnsureType>(source->contentType().abstractType());
            encounter(AbstractType::Ptr::staticCast(newType), DeclarationPointer(useDeclaration));
            return true;
        }
        return false;
    };

    foreach ( const QString& currentHint, knownDecoratorHints.keys() ) {
        QStringList arguments;
        if ( ! Helper::docstringContainsHint(funcDecl, currentHint, &arguments) ) {
            continue;
        }
        // If the hint word appears in the docstring, run the evaluation function.
        if ( knownDecoratorHints[currentHint](arguments, currentHint) ) {
            // We indeed found something, so we're done.
            return;
        }
    }

    // if none of the above decorator-finding methods worked, just use the ordinary return type.
    return encounter(type, DeclarationPointer(useDeclaration));
}

void ExpressionVisitor::visitSubscript(SubscriptAst* node)
{
    AstDefaultVisitor::visitNode(node->value);
    if ( node->slice && node->slice->astType == Ast::IndexAstType ) {
        DUChainReadLocker lock;
        auto indexedTypes = Helper::filterType<IndexedContainer>(lastType(), [](AbstractType::Ptr toFilter) {
            return toFilter.cast<IndexedContainer>();
        });
        for ( IndexedContainer::Ptr indexed: indexedTypes ) {
            // TODO This loop currently only uses the first result, it could construct
            // an unsure from all the matches.
            IndexAst* sliceIndexAst = static_cast<IndexAst*>(node->slice);
            NumberAst* number = nullptr;
            bool invert = false;
            if ( sliceIndexAst->value && sliceIndexAst->value->astType == Ast::UnaryOperationAstType ) {
                // might be -3
                UnaryOperationAst* unary = static_cast<UnaryOperationAst*>(sliceIndexAst->value);
                if ( unary->type == Ast::UnaryOperatorSub && unary->operand->astType == Ast::NumberAstType ) {
                    number = static_cast<NumberAst*>(unary->operand);
                    invert = true;
                }
            }
            else if ( sliceIndexAst->value->astType == Ast::NumberAstType ) {
                number = static_cast<NumberAst*>(sliceIndexAst->value);
            }
            if ( number ) {
                int sliceIndex = number->value * ( invert ? -1 : 1 );
                if ( sliceIndex < 0 && sliceIndex + indexed->typesCount() > 0 ) {
                    sliceIndex += indexed->typesCount();
                }
                if ( sliceIndex < indexed->typesCount() && sliceIndex >= 0 ) {
                    return encounter(indexed->typeAt(sliceIndex).abstractType());
                }
            }
            // the exact index is unknown, use unsure
            return encounter(indexed->asUnsureType().cast<AbstractType>());
        }
        auto variableTypes = Helper::filterType<ListType>(lastType(), [](AbstractType::Ptr toFilter) {
            return toFilter.cast<ListType>();
        });
        if ( ! variableTypes.isEmpty() ) {
            AbstractType::Ptr result(new IntegralType(IntegralType::TypeMixed));
            for ( auto variable: variableTypes ) {
                result = Helper::mergeTypes(result, variable->contentType().abstractType());
            }
            return encounter(result);
        }
    }

    // If that does not work and we have a slice like [3:5], guess it will remain the same type.
    // That is an approximation we have to make now, should optimally be corrected later.
    // The reason is that we'd need to parse decorators from the __getitem__ method to support
    // list/dict/etc properly otherwise, which requires a bit of refactoring first. TODO do this
    if ( node->slice && node->slice->astType != Ast::IndexAstType ) {
        return;
    }

    // Otherwise, try to use __getitem__.
    ExpressionVisitor v(context());
    v.visitNode(node->value);
    DUChainReadLocker lock;
    Declaration* function = Helper::accessAttribute(v.lastDeclaration().data(), "__getitem__", context());
    if ( function && function->isFunctionDeclaration() ) {
        if ( FunctionType::Ptr functionType = function->type<FunctionType>() ) {
            return encounter(functionType->returnType());
        }
    }

    // Otherwise, give up
    return encounterUnknown();
}

void ExpressionVisitor::visitList(ListAst* node)
{
    AstDefaultVisitor::visitList(node);
    DUChainReadLocker lock;
    auto type = typeObjectForIntegralType<ListType>("list", context());
    lock.unlock();
    ExpressionVisitor contentVisitor(this);
    if ( type ) {
        foreach ( ExpressionAst* content, node->elements ) {
            contentVisitor.visitNode(content);
            type->addContentType<Python::UnsureType>(contentVisitor.lastType());
        }
    }
    else {
        encounterUnknown();
        kWarning() << " [ !!! ] did not get a typetrack container object when expecting one! Fix code / setup.";
    }
    encounter(AbstractType::Ptr::staticCast(type));
}

void ExpressionVisitor::visitDictionaryComprehension(DictionaryComprehensionAst* node)
{
    AstDefaultVisitor::visitDictionaryComprehension(node);
    DUChainReadLocker lock;
    auto type = typeObjectForIntegralType<MapType>("dict", context());
    if ( type ) {
        DUContext* comprehensionContext = context()->findContextAt(CursorInRevision(node->startLine, node->startCol + 1));
        lock.unlock();
        Q_ASSERT(comprehensionContext);
        DUContext* ctx = m_forceGlobalSearching ? context()->topContext() : comprehensionContext;
        ExpressionVisitor v(this, ctx);
        v.visitNode(node->value);
        if ( v.lastType() ) {
            type->addContentType<Python::UnsureType>(v.lastType());
        }
        ExpressionVisitor k(this, ctx);
        k.visitNode(node->key);
        if ( k.lastType() ) {
            type->addKeyType<Python::UnsureType>(k.lastType());
        }
    }
    else {
        return encounterUnknown();
    }
    encounter(AbstractType::Ptr::staticCast(type));
}

void ExpressionVisitor::visitSetComprehension(SetComprehensionAst* node)
{
    Python::AstDefaultVisitor::visitSetComprehension(node);
    DUChainReadLocker lock;
    auto type = typeObjectForIntegralType<ListType>("set", context());
    if ( type ) {
        DUContext* comprehensionContext = context()->findContextAt(CursorInRevision(node->startLine, node->startCol+1), true);
        lock.unlock();
        auto ctx = m_forceGlobalSearching ? context()->topContext() : comprehensionContext;
        ExpressionVisitor v(this, ctx);
        v.visitNode(node->element);
        if ( v.lastType() ) {
            type->addContentType<Python::UnsureType>(v.lastType());
        }
    }
    encounter(AbstractType::Ptr::staticCast(type));
}

void ExpressionVisitor::visitListComprehension(ListComprehensionAst* node)
{
    AstDefaultVisitor::visitListComprehension(node);
    DUChainReadLocker lock;
    auto type = typeObjectForIntegralType<ListType>("list", context());
    if ( type && ! m_forceGlobalSearching ) { // TODO fixme
        DUContext* comprehensionContext = context()->findContextAt(CursorInRevision(node->startLine, node->startCol + 1), true);
        lock.unlock();
        ExpressionVisitor v(this, comprehensionContext);
        Q_ASSERT(comprehensionContext);
        v.visitNode(node->element);
        if ( v.lastType() ) {
            type->addContentType<Python::UnsureType>(v.lastType());
        }
    }
    else {
        return encounterUnknown();
    }
    encounter(AbstractType::Ptr::staticCast(type));
}

void ExpressionVisitor::visitTuple(TupleAst* node) {
    DUChainReadLocker lock;
    IndexedContainer::Ptr type = typeObjectForIntegralType<IndexedContainer>("tuple", context());
    if ( type ) {
        lock.unlock();
        foreach ( ExpressionAst* expr, node->elements ) {
            ExpressionVisitor v(this);
            v.visitNode(expr);
            if ( v.lastType() ) {
                type->addEntry(v.lastType());
            }
            else {
                type->addEntry(AbstractType::Ptr(new IntegralType(IntegralType::TypeMixed)));
            }
        }
        encounter(AbstractType::Ptr::staticCast(type));
    }
    else {
        kWarning() << "tuple type object is not available";
        return encounterUnknown();
    }
}

void ExpressionVisitor::visitIfExpression(IfExpressionAst* node)
{
    AstDefaultVisitor::visitIfExpression(node);
    if ( node->body && node->orelse ) {
        ExpressionVisitor v(this);
        v.visitNode(node->body);
        AbstractType::Ptr first = v.lastType();
        v.visitNode(node->orelse);
        AbstractType::Ptr second = v.lastType();
        encounter(Helper::mergeTypes(first, second));
    }
}

void ExpressionVisitor::visitSet(SetAst* node)
{
    DUChainReadLocker lock;
    auto type = typeObjectForIntegralType<ListType>("set", context());
    lock.unlock();
    ExpressionVisitor contentVisitor(this);
    if ( type ) {
        foreach ( ExpressionAst* content, node->elements ) {
            contentVisitor.visitNode(content);
            type->addContentType<Python::UnsureType>(contentVisitor.lastType());
        }
    }
    encounter(AbstractType::Ptr::staticCast(type));
}

void ExpressionVisitor::visitDict(DictAst* node)
{
    DUChainReadLocker lock;
    auto type = typeObjectForIntegralType<MapType>("dict", context());
    lock.unlock();
    ExpressionVisitor contentVisitor(this);
    ExpressionVisitor keyVisitor(this);
    if ( type ) {
        foreach ( ExpressionAst* content, node->values ) {
            contentVisitor.visitNode(content);
            type->addContentType<Python::UnsureType>(contentVisitor.lastType());
        }
        foreach ( ExpressionAst* key, node->keys ) {
            keyVisitor.visitNode(key);
            type->addKeyType<Python::UnsureType>(keyVisitor.lastType());
        }
    }
    encounter(AbstractType::Ptr::staticCast(type));
}

void ExpressionVisitor::visitNumber(Python::NumberAst* number)
{
    AbstractType::Ptr type;
    DUChainReadLocker lock;
    if ( number->isInt ) {
        type = typeObjectForIntegralType<AbstractType>("int", context());
    }
    else {
        type = typeObjectForIntegralType<AbstractType>("float", context());
    }
    encounter(type);
}

void ExpressionVisitor::visitString(Python::StringAst* )
{
    DUChainReadLocker lock;
    StructureType::Ptr type = typeObjectForIntegralType<StructureType>("str", context());
    encounter(AbstractType::Ptr::staticCast(type));
}

RangeInRevision nodeRange(Python::Ast* node)
{
    return RangeInRevision(node->startLine, node->startCol, node->endLine,node->endCol);
}

void ExpressionVisitor::addUnknownName(const QString& name)
{
    if ( m_parentVisitor ) {
        static_cast<ExpressionVisitor*>(m_parentVisitor)->addUnknownName(name);
    }
    else if ( ! m_unknownNames.contains(name) ) {
        m_unknownNames.insert(name);
    }
}

void ExpressionVisitor::visitNameConstant(NameConstantAst* node)
{
    // handles "True", "False", "None"
    auto defId = m_defaultTypes.constFind(node->value);
    if ( defId != m_defaultTypes.constEnd() ) {
        return encounter(*defId);
    }
}

void ExpressionVisitor::visitName(Python::NameAst* node)
{
    RangeInRevision range;
    if ( m_scanUntilCursor.isValid() ) {
        range = RangeInRevision(CursorInRevision(0, 0), m_scanUntilCursor);
    }
    else if ( m_forceGlobalSearching ) {
        range = RangeInRevision::invalid();
    }
    else {
        range = RangeInRevision(0, 0, node->endLine, node->endCol);
    }
    DUChainReadLocker lock;
    Declaration* d = Helper::declarationForName(QualifiedIdentifier(node->identifier->value),
                                                range, DUChainPointer<const DUContext>(context()));

    if ( d ) {
        bool isAlias = dynamic_cast<AliasDeclaration*>(d) || d->isFunctionDeclaration() || dynamic_cast<ClassDeclaration*>(d);
        return encounter(d->abstractType(), DeclarationPointer(d), isAlias);
    }
    else {
        if ( m_reportUnknownNames ) {
            addUnknownName(node->identifier->value);
        }
        return encounterUnknown();
    }
}

void ExpressionVisitor::visitCompare(CompareAst* node)
{
    Python::AstDefaultVisitor::visitCompare(node);
    encounter(AbstractType::Ptr(new IntegralType(IntegralType::TypeBoolean)));
}

AbstractType::Ptr ExpressionVisitor::fromBinaryOperator(AbstractType::Ptr lhs, AbstractType::Ptr rhs, const QString& op) {
    DUChainReadLocker lock;
    auto operatorReturnType = [&op, this](const AbstractType::Ptr& p) {
        StructureType::Ptr type = p.cast<StructureType>();
        if ( ! type ) {
            return AbstractType::Ptr();
        }
        Declaration* func = Helper::accessAttribute(type->declaration(context()->topContext()), op, context());
        if ( ! func ) {
            return AbstractType::Ptr();
        }
        auto operatorFunctionType = func->type<FunctionType>();
        DUChainReadLocker lock;
        auto object_decl = Helper::getDocumentationFileContext()->findDeclarations(QualifiedIdentifier("object"));
        if ( ! object_decl.isEmpty() && object_decl.first()->internalContext() == func->context() ) {
            // if the operator is only declared in object(), do not include its type (which is void).
            return AbstractType::Ptr();
        }
        return operatorFunctionType ? operatorFunctionType->returnType() : AbstractType::Ptr();
    };

    return Helper::mergeTypes(operatorReturnType(lhs), operatorReturnType(rhs));
}

void ExpressionVisitor::visitBinaryOperation(Python::BinaryOperationAst* node)
{
    ExpressionVisitor lhsVisitor(this);
    ExpressionVisitor rhsVisitor(this);
    AbstractType::Ptr result;

    lhsVisitor.visitNode(node->lhs);
    rhsVisitor.visitNode(node->rhs);

    if ( lhsVisitor.lastType() && lhsVisitor.lastType()->whichType() == AbstractType::TypeUnsure ) {
        KDevelop::UnsureType::Ptr unsure = lhsVisitor.lastType().cast<KDevelop::UnsureType>();
        const IndexedType* types = unsure->types();
        for( uint i = 0; i < unsure->typesSize(); i++ ) {
            result = Helper::mergeTypes(result, fromBinaryOperator(types[i].abstractType(),
                                                                   rhsVisitor.lastType(), node->methodName()));
        }
    } else {
        result = fromBinaryOperator(lhsVisitor.lastType(), rhsVisitor.lastType(), node->methodName());
    }
    if ( ! Helper::isUsefulType(result) ) {
        result = Helper::mergeTypes(lhsVisitor.lastType(), rhsVisitor.lastType());
    }
    return encounter(result);
}

void ExpressionVisitor::visitUnaryOperation(Python::UnaryOperationAst* node)
{
    // Only visit the value, and use that as the result. Unary operators usually
    // don't change the type of the object (i.e. -a has the same type as a)
    visitNode(node->operand);
}

void ExpressionVisitor::visitBooleanOperation(Python::BooleanOperationAst* node)
{
    foreach (ExpressionAst* expression, node->values) {
        visitNode(expression);
    }

    encounter(AbstractType::Ptr(new IntegralType(IntegralType::TypeBoolean)));
}

}

