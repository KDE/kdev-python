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
    ExpressionVisitor v(this);
    v.visitNode(node->value);
    setConfident(false);

    // Find a matching declaration which is made inside the type of the accessed object.
    // Like, for B.C where B is an instance of foo, find a property of foo called C.
    DUChainReadLocker lock;
    auto attribute = Helper::accessAttribute(v.lastType(), node->attribute->value, topContext());

    if ( auto resolved = Helper::resolveAliasDeclaration(attribute) ) {
        encounter(attribute->abstractType(), DeclarationPointer(attribute));
        setLastIsAlias(dynamic_cast<AliasDeclaration*>(attribute) ||
                        resolved->isFunctionDeclaration() ||
                        dynamic_cast<ClassDeclaration*>(resolved));
    } else {
        encounterUnknown();
    }
}

void ExpressionVisitor::visitCall(CallAst* node)
{
    foreach ( ExpressionAst* c, node->arguments ) {
        AstDefaultVisitor::visitNode(c);
    }
    ExpressionVisitor v(this);
    v.visitNode(node->function);
    auto declaration = Helper::resolveAliasDeclaration(v.lastDeclaration().data());
    if ( ! v.isAlias() && v.lastType() ) {
        if ( auto functionType = v.lastType().cast<FunctionType>() ) {
            encounter(functionType->returnType());
            return;
        }
        if ( auto classType = v.lastType().cast<StructureType>() ) {
            declaration = classType->declaration(topContext());
        }
    }
    if ( ! declaration ) {
        encounterUnknown();
        return;
    }
    ClassDeclaration* classDecl = dynamic_cast<ClassDeclaration*>(declaration);
    DUChainReadLocker lock;
    auto function = Helper::functionForCalled(declaration, v.isAlias());
    lock.unlock();

    AbstractType::Ptr type;
    Declaration* decl;

    if ( function.isConstructor && classDecl ) {
        // Don't use return type from constructor.
        // It's wrong for builtins, or classes without their own __init__ methods().
        type = classDecl->abstractType();
        decl = classDecl;
    }
    else if ( function.declaration && function.declaration->type<FunctionType>() ) {
        // But do use the return value of normal functions or __call__().
        type = function.declaration->type<FunctionType>()->returnType();
        decl = function.declaration;
    }
    else {
        qCDebug(KDEV_PYTHON_DUCHAIN) << "Declaration is not a class or function declaration";
        encounterUnknown();
        return;
    }
    if ( function.declaration ) {
        auto docstring = function.declaration->comment();
        if ( ! docstring.isEmpty() ) {
            // Our documentation data uses special docstrings that override the return type
            //  of some functions (including constructors).
            type = docstringTypeOverride(node, type, docstring);
        }
    }
    encounter(type, DeclarationPointer(decl));
}

AbstractType::Ptr ExpressionVisitor::docstringTypeOverride(
    CallAst* node, const AbstractType::Ptr normalType, const QString& docstring)
{
    auto docstringType = normalType;
    auto listOfTuples = [&](AbstractType::Ptr key, AbstractType::Ptr value) {
        auto newType = typeObjectForIntegralType<ListType>("list");
        IndexedContainer::Ptr newContents = typeObjectForIntegralType<IndexedContainer>("tuple");
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

    QHash< QString, std::function<bool(QStringList, QString)> > knownDocstringHints;
    qCDebug(KDEV_PYTHON_DUCHAIN) << "Got function declaration with docstring hint, checking for type...";
    knownDocstringHints["getsType"] = [&](QStringList /*arguments*/, QString /*currentHint*/) {
        if ( node->function->astType != Ast::AttributeAstType ) {
            return false;
        }
        ExpressionVisitor baseTypeVisitor(this);
        // when calling foo.bar[3].baz.iteritems(), find the type of "foo.bar[3].baz"
        baseTypeVisitor.visitNode(static_cast<AttributeAst*>(node->function)->value);
        if ( auto t = baseTypeVisitor.lastType().cast<ListType>() ) {
            qCDebug(KDEV_PYTHON_DUCHAIN) << "Found container, using type";
            docstringType = t->contentType().abstractType();
            return true;
        }
        return false;
    };

    knownDocstringHints["getsList"] = [&](QStringList /*arguments*/, QString currentHint) {
        if ( node->function->astType != Ast::AttributeAstType ) {
            return false;
        }
        ExpressionVisitor baseTypeVisitor(this);
        // when calling foo.bar[3].baz.iteritems(), find the type of "foo.bar[3].baz"
        baseTypeVisitor.visitNode(static_cast<AttributeAst*>(node->function)->value);
        DUChainWriteLocker lock;
        if ( auto t = baseTypeVisitor.lastType().cast<ListType>() ) {
            qCDebug(KDEV_PYTHON_DUCHAIN) << "Got container:" << t->toString();
            auto newType = typeObjectForIntegralType<ListType>("list");
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
            docstringType = newType.cast<AbstractType>();
            return true;
        }
        return false;
    };
    knownDocstringHints["getListOfKeys"] = knownDocstringHints["getsList"];

    knownDocstringHints["enumerate"] = [&](QStringList /*arguments*/, QString /*currentHint*/) {
        if ( node->function->astType != Ast::NameAstType || node->arguments.size() < 1 ) {
            return false;
        }
        ExpressionVisitor enumeratedTypeVisitor(this);
        enumeratedTypeVisitor.visitNode(node->arguments.first());

        DUChainWriteLocker lock;
        auto intType = typeObjectForIntegralType<AbstractType>("int");
        auto enumerated = enumeratedTypeVisitor.lastType();
        docstringType = listOfTuples(intType, Helper::contentOfIterable(enumerated, topContext()));
        return true;
    };

    knownDocstringHints["getsListOfBoth"] = [&](QStringList /*arguments*/, QString /*currentHint*/) {
        qCDebug(KDEV_PYTHON_DUCHAIN) << "Got getsListOfBoth hint, checking container";
        if ( node->function->astType != Ast::AttributeAstType ) {
            return false;
        }
        ExpressionVisitor baseTypeVisitor(this);
        // when calling foo.bar[3].baz.iteritems(), find the type of "foo.bar[3].baz"
        baseTypeVisitor.visitNode(static_cast<AttributeAst*>(node->function)->value);
        DUChainWriteLocker lock;
        if ( auto t = baseTypeVisitor.lastType().cast<MapType>() ) {
            qCDebug(KDEV_PYTHON_DUCHAIN) << "Got container:" << t->toString();
            docstringType = listOfTuples(t->keyType().abstractType(), t->contentType().abstractType());
            return true;
        }
        return false;
    };

    knownDocstringHints["returnContentEqualsContentOf"] = [&](QStringList arguments, QString /*currentHint*/) {
        const int argNum = ! arguments.isEmpty() ? (int) arguments.at(0).toUInt() : 0;
        qCDebug(KDEV_PYTHON_DUCHAIN) << "Found argument dependent hint, checking argument type" << argNum;
        if ( argNum >= node->arguments.length() ) {
            return false;
        }
        ExpressionAst* relevantArgument = node->arguments.at(argNum);
        ExpressionVisitor v(this);
        v.visitNode(relevantArgument);
        if ( ! v.lastType() ) {
            return false;
        }
        AbstractType::Ptr newType;
        if ( auto targetContainer = ListType::Ptr::dynamicCast(normalType) ) {
            // Copy the return type, to set contents for this call only.
            docstringType = AbstractType::Ptr(targetContainer->clone());
            // Add content type of the source.
            auto sourceContentType = Helper::contentOfIterable(v.lastType(), topContext());
            ListType::Ptr::staticCast(docstringType)->addContentType<Python::UnsureType>(sourceContentType);
        }
        else if ( auto sourceContainer = ListType::Ptr::dynamicCast(v.lastType()) ) {
            // if the function does not force a return type, just copy the source (like for reversed())
            docstringType = AbstractType::Ptr(sourceContainer->clone());
        }
        else {
            return false; // No target container type
        }
        Q_ASSERT(docstringType);
        return true;
    };

    foreach ( const QString& currentHint, knownDocstringHints.keys() ) {
        QStringList arguments;
        if ( ! Helper::docstringContainsHint(docstring, currentHint, &arguments) ) {
            continue;
        }
        // If the hint word appears in the docstring, run the evaluation function.
        if ( knownDocstringHints[currentHint](arguments, currentHint) ) {
            // We indeed found something, so we're done.
            break;
        }
    }
    return docstringType;
}

void ExpressionVisitor::visitSubscript(SubscriptAst* node)
{
    AstDefaultVisitor::visitNode(node->value);

    auto valueTypes = Helper::filterType<AbstractType>(lastType(), [](AbstractType::Ptr) { return true; });
    AbstractType::Ptr result(new IntegralType(IntegralType::TypeMixed));

    foreach (const auto& type, valueTypes) {
        if ( (node->slice->astType != Ast::IndexAstType) &&
             (type.cast<IndexedContainer>() || type.cast<ListType>()) ) {
            if ( type.cast<MapType>() ) {
                continue; // Can't slice dicts.
            }
            // Assume that slicing (e.g. foo[3:5]) a tuple/list returns the same type.
            // TODO: we could do better for some tuple slices.
            result = Helper::mergeTypes(result, type);
        }
        else if ( const auto& indexed = type.cast<IndexedContainer>() ) {
            IndexAst* sliceIndexAst = static_cast<IndexAst*>(node->slice);
            NumberAst* number = nullptr;
            bool invert = false;
            if ( sliceIndexAst->value->astType == Ast::UnaryOperationAstType ) {
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
                    result = Helper::mergeTypes(result, indexed->typeAt(sliceIndex).abstractType());
                    continue;
                }
            }
            result = Helper::mergeTypes(result, indexed->asUnsureType());
        }
        else if ( const auto& listType = type.cast<ListType>() ) {
            result = Helper::mergeTypes(result, listType->contentType().abstractType());
        }
        else {
            // Type wasn't one with custom handling, so use return type of __getitem__().
            DUChainReadLocker lock;
            static const IndexedIdentifier getitemIdentifier(KDevelop::Identifier("__getitem__"));
            auto function = Helper::accessAttribute(type, getitemIdentifier, topContext());
            if ( function && function->isFunctionDeclaration() ) {
                if ( FunctionType::Ptr functionType = function->type<FunctionType>() ) {
                    result = Helper::mergeTypes(result, functionType->returnType());
                }
            }
        }
    }
    encounter(result);
}

void ExpressionVisitor::visitLambda(LambdaAst* node)
{
    AstDefaultVisitor::visitLambda(node);
    FunctionType::Ptr type(new FunctionType());
    AbstractType::Ptr mixed(new IntegralType(IntegralType::TypeMixed));
    for (int ii = 0; ii < node->arguments->arguments.length(); ++ii) {
        type->addArgument(mixed);
    }
    type->setReturnType(lastType());
    encounter(type);
}

void ExpressionVisitor::visitList(ListAst* node)
{
    DUChainReadLocker lock;
    auto type = typeObjectForIntegralType<ListType>("list");
    lock.unlock();
    ExpressionVisitor contentVisitor(this);
    if ( type ) {
        foreach ( ExpressionAst* content, node->elements ) {
            contentVisitor.visitNode(content);
            if ( content->astType == Ast::StarredAstType ) {
                auto contentType = Helper::contentOfIterable(contentVisitor.lastType(), topContext());
                type->addContentType<Python::UnsureType>(contentType);
            }
            else {
                type->addContentType<Python::UnsureType>(contentVisitor.lastType());
            }
        }
    }
    else {
        encounterUnknown();
        qCWarning(KDEV_PYTHON_DUCHAIN) << " [ !!! ] did not get a typetrack container object when expecting one! Fix code / setup.";
    }
    encounter(AbstractType::Ptr::staticCast(type));
}

void ExpressionVisitor::visitDictionaryComprehension(DictionaryComprehensionAst* node)
{
    DUChainReadLocker lock;
    auto type = typeObjectForIntegralType<MapType>("dict");
    if ( type ) {
        DUContext* comprehensionContext = context()->findContextAt(CursorInRevision(node->startLine, node->startCol));
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
    auto type = typeObjectForIntegralType<ListType>("set");
    if ( type ) {
        DUContext* comprehensionContext = context()->findContextAt(CursorInRevision(node->startLine, node->startCol), true);
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
    auto type = typeObjectForIntegralType<ListType>("list");
    if ( type && ! m_forceGlobalSearching ) { // TODO fixme
        DUContext* comprehensionContext = context()->findContextAt(CursorInRevision(node->startLine, node->startCol), true);
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
    IndexedContainer::Ptr type = typeObjectForIntegralType<IndexedContainer>("tuple");
    if ( type ) {
        lock.unlock();
        foreach ( ExpressionAst* expr, node->elements ) {
            ExpressionVisitor v(this);
            v.visitNode(expr);
            if ( expr->astType == Ast::StarredAstType ) {
                // foo = a, *b, c
                if ( auto unpackedType = v.lastType().cast<IndexedContainer>() ) {
                    for ( int ii = 0; ii < unpackedType->typesCount(); ++ii ) {
                        type->addEntry(unpackedType->typeAt(ii).abstractType());
                    }
                } // Unpacking something else, do nothing (i.e. assume it was empty).
            } else {
                type->addEntry(v.lastType());
            }
        }
        encounter(AbstractType::Ptr::staticCast(type));
    }
    else {
        qCWarning(KDEV_PYTHON_DUCHAIN) << "tuple type object is not available";
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
    auto type = typeObjectForIntegralType<ListType>("set");
    lock.unlock();
    ExpressionVisitor contentVisitor(this);
    if ( type ) {
        foreach ( ExpressionAst* content, node->elements ) {
            contentVisitor.visitNode(content);
            if ( content->astType == Ast::StarredAstType ) {
                auto contentType = Helper::contentOfIterable(contentVisitor.lastType(), topContext());
                type->addContentType<Python::UnsureType>(contentType);
            }
            else {
                type->addContentType<Python::UnsureType>(contentVisitor.lastType());
            }
        }
    }
    encounter(AbstractType::Ptr::staticCast(type));
}

void ExpressionVisitor::visitDict(DictAst* node)
{
    DUChainReadLocker lock;
    auto type = typeObjectForIntegralType<MapType>("dict");
    lock.unlock();
    ExpressionVisitor contentVisitor(this);
    ExpressionVisitor keyVisitor(this);
    if ( type ) {
        Q_ASSERT(node->keys.length() == node->values.length());
        for ( int ii = 0; ii < node->values.length(); ++ii ) {
            contentVisitor.visitNode(node->values.at(ii));
            if ( node->keys.at(ii) ) {
                type->addContentType<Python::UnsureType>(contentVisitor.lastType());
                keyVisitor.visitNode(node->keys.at(ii));
                type->addKeyType<Python::UnsureType>(keyVisitor.lastType());
            }
            else if ( auto unpackedType = contentVisitor.lastType().cast<MapType>() ) {
                // Key is null for `{**foo}`
                type->addContentType<Python::UnsureType>(unpackedType->contentType().abstractType());
                type->addKeyType<Python::UnsureType>(unpackedType->keyType().abstractType());
            }
        }
    }
    encounter(AbstractType::Ptr::staticCast(type));
}

void ExpressionVisitor::visitNumber(Python::NumberAst* number)
{
    AbstractType::Ptr type;
    DUChainReadLocker lock;
    if ( number->isInt ) {
        type = typeObjectForIntegralType<AbstractType>("int");
    }
    else {
        type = typeObjectForIntegralType<AbstractType>("float");
    }
    encounter(type);
}

void ExpressionVisitor::visitString(Python::StringAst* )
{
    DUChainReadLocker lock;
    StructureType::Ptr type = typeObjectForIntegralType<StructureType>("str");
    encounter(AbstractType::Ptr::staticCast(type));
}

void ExpressionVisitor::visitBytes(Python::BytesAst* ) {
    DUChainReadLocker lock;
    auto type = typeObjectForIntegralType<StructureType>("bytes");
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
        auto func = Helper::accessAttribute(type, op, topContext());
        if ( ! func ) {
            return AbstractType::Ptr();
        }
        auto operatorFunctionType = func->type<FunctionType>();
        DUChainReadLocker lock;
        auto context = Helper::getDocumentationFileContext();
        if ( context ) {
            auto object_decl = context->findDeclarations(QualifiedIdentifier("object"));
            if ( ! object_decl.isEmpty() && object_decl.first()->internalContext() == func->context() ) {
                // if the operator is only declared in object(), do not include its type (which is void).
                return AbstractType::Ptr();
            }
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

