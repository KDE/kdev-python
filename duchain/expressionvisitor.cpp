/*
    SPDX-FileCopyrightText: 2010 Miquel Canes Gonzalez <miquelcanes@gmail.com>
    SPDX-FileCopyrightText: 2011-2013 Sven Brauch <svenbrauch@googlemail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#include "expressionvisitor.h"
#include "types/nonetype.h"
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
    if ( m_defaultTypes.isEmpty() ) {
        m_defaultTypes.insert(NameConstantAst::True, AbstractType::Ptr(new IntegralType(IntegralType::TypeBoolean)));
        m_defaultTypes.insert(NameConstantAst::False, AbstractType::Ptr(new IntegralType(IntegralType::TypeBoolean)));
        m_defaultTypes.insert(NameConstantAst::None, AbstractType::Ptr(new NoneType()));
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
    auto resolved = Helper::resolveAliasDeclaration(attribute);
    if ( ! resolved ) {
        encounterUnknown();
        return;
    }
    auto function = dynamic_cast<FunctionDeclaration*>(resolved);
    if ( function && function->type<FunctionType>() &&
          function->isProperty() ) {
        encounter(function->type<FunctionType>()->returnType(), DeclarationPointer(function));
        return;
    }
    encounter(attribute->abstractType(), DeclarationPointer(attribute));
    setLastIsAlias(function ||
                    dynamic_cast<AliasDeclaration*>(attribute) ||
                    dynamic_cast<ClassDeclaration*>(resolved) );
}

void ExpressionVisitor::visitCall(CallAst* node)
{
    visitNodeList(node->arguments);
    ExpressionVisitor v(this);
    v.visitNode(node->function);
    auto declaration = Helper::resolveAliasDeclaration(v.lastDeclaration().data());
    if ( ! v.isAlias() && v.lastType() ) {
        if ( auto functionType = v.lastType().dynamicCast<FunctionType>() ) {
            encounter(functionType->returnType());
            return;
        }
        if ( auto classType = v.lastType().dynamicCast<StructureType>() ) {
            DUChainReadLocker lock;
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
            type = docstringTypeOverride(node, type, QString::fromUtf8(docstring));
        }
    }
    encounter(type, DeclarationPointer(decl));
}

AbstractType::Ptr ExpressionVisitor::docstringTypeOverride(
    CallAst* node, const AbstractType::Ptr normalType, const QString& docstring)
{
    auto docstringType = normalType;
    auto listOfTuples = [&](AbstractType::Ptr key, AbstractType::Ptr value) {
        auto newType = typeObjectForIntegralType<ListType>(QStringLiteral("list"));
        IndexedContainer::Ptr newContents = typeObjectForIntegralType<IndexedContainer>(QStringLiteral("tuple"));
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
        newType->addContentType<Python::UnsureType>(newContents);
        return newType.staticCast<AbstractType>();
    };

    QHash< QString, std::function<bool(QStringList, QString)> > knownDocstringHints;
    knownDocstringHints[QStringLiteral("getsType")] = [&](QStringList /*arguments*/, QString /*currentHint*/) {
        if ( node->function->astType != Ast::AttributeAstType ) {
            return false;
        }
        ExpressionVisitor baseTypeVisitor(this);
        // when calling foo.bar[3].baz.iteritems(), find the type of "foo.bar[3].baz"
        baseTypeVisitor.visitNode(static_cast<AttributeAst*>(node->function)->value);
        if ( auto t = baseTypeVisitor.lastType().dynamicCast<ListType>() ) {
            docstringType = t->contentType().abstractType();
            return true;
        }
        return false;
    };

    knownDocstringHints[QStringLiteral("getsList")] = [&](QStringList /*arguments*/, QString currentHint) {
        if ( node->function->astType != Ast::AttributeAstType ) {
            return false;
        }
        ExpressionVisitor baseTypeVisitor(this);
        // when calling foo.bar[3].baz.iteritems(), find the type of "foo.bar[3].baz"
        baseTypeVisitor.visitNode(static_cast<AttributeAst*>(node->function)->value);
        DUChainReadLocker lock;
        if ( auto t = baseTypeVisitor.lastType().dynamicCast<ListType>() ) {
            auto newType = typeObjectForIntegralType<ListType>(QStringLiteral("list"));
            if ( ! newType ) {
                return false;
            }
            AbstractType::Ptr contentType;
            if ( currentHint == QStringLiteral("getsList") ) {
                contentType = t->contentType().abstractType();
            }
            else if ( auto map = t.dynamicCast<MapType>() ) {
                contentType = map->keyType().abstractType();
            }
            newType->addContentType<Python::UnsureType>(contentType);
            docstringType = newType;
            return true;
        }
        return false;
    };
    knownDocstringHints[QStringLiteral("getListOfKeys")] = knownDocstringHints[QStringLiteral("getsList")];

    knownDocstringHints[QStringLiteral("enumerate")] = [&](QStringList /*arguments*/, QString /*currentHint*/) {
        if ( node->function->astType != Ast::NameAstType || node->arguments.size() < 1 ) {
            return false;
        }
        ExpressionVisitor enumeratedTypeVisitor(this);
        enumeratedTypeVisitor.visitNode(node->arguments.first());

        DUChainReadLocker lock;
        auto intType = typeObjectForIntegralType<AbstractType>(QStringLiteral("int"));
        auto enumerated = enumeratedTypeVisitor.lastType();
        docstringType = listOfTuples(intType, Helper::contentOfIterable(enumerated, topContext()));
        return true;
    };

    knownDocstringHints[QStringLiteral("getsListOfBoth")] = [&](QStringList /*arguments*/, QString /*currentHint*/) {
        if ( node->function->astType != Ast::AttributeAstType ) {
            return false;
        }
        ExpressionVisitor baseTypeVisitor(this);
        // when calling foo.bar[3].baz.iteritems(), find the type of "foo.bar[3].baz"
        baseTypeVisitor.visitNode(static_cast<AttributeAst*>(node->function)->value);
        DUChainReadLocker lock;
        if ( auto t = baseTypeVisitor.lastType().dynamicCast<MapType>() ) {
            docstringType = listOfTuples(t->keyType().abstractType(), t->contentType().abstractType());
            return true;
        }
        return false;
    };

    knownDocstringHints[QStringLiteral("returnContentEqualsContentOf")] = [&](QStringList arguments, QString /*currentHint*/) {
        const int argNum = ! arguments.isEmpty() ? (int) arguments.at(0).toUInt() : 0;
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
        if ( auto targetContainer = normalType.dynamicCast<ListType>() ) {
            // Copy the return type, to set contents for this call only.
            docstringType = AbstractType::Ptr(targetContainer->clone());
            // Add content type of the source.
            auto sourceContentType = Helper::contentOfIterable(v.lastType(), topContext());
            docstringType.staticCast<ListType>()->addContentType<Python::UnsureType>(sourceContentType);
        }
        else if ( auto sourceContainer = v.lastType().dynamicCast<ListType>() ) {
            // if the function does not force a return type, just copy the source (like for reversed())
            docstringType = AbstractType::Ptr(sourceContainer->clone());
        }
        else {
            return false; // No target container type
        }
        Q_ASSERT(docstringType);
        return true;
    };

    const auto hints = knownDocstringHints.keys();
    for (const QString& currentHint : hints) {
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

long integerValue(ExpressionAst* node, long wrapTo=0) {
    bool invert = false;
    if ( node->astType == Ast::UnaryOperationAstType ) {
        auto unaryOp = static_cast<UnaryOperationAst*>(node);
        if ( unaryOp->type == Ast::UnaryOperatorSub ) {
            node = unaryOp->operand;
            invert = true;
        }
    }
    if ( node->astType == Ast::NumberAstType ) {
        auto number = static_cast<NumberAst*>(node);
        if ( number->isInt ) {
            // Clamp in case of `a[-9999999:9999999]` or similar.
            // -1 is just as out-of-range as -99999999, but doesn't cause a huge loop.
            long upperBound = wrapTo ? wrapTo : LONG_MAX;
            if (invert) {
                return qBound(-1L, wrapTo - number->value, upperBound);
            }
            return qBound(-1L, number->value, upperBound);
        }
    }
    return LONG_MIN;
}

void ExpressionVisitor::visitSubscript(SubscriptAst* node)
{
    AstDefaultVisitor::visitNode(node->value);

    auto valueTypes = Helper::filterType<AbstractType>(lastType(), [](AbstractType::Ptr) { return true; });
    AbstractType::Ptr result(new IntegralType(IntegralType::TypeMixed));

    for (const auto& type : std::as_const(valueTypes)) {
        if ( node->slice->astType == Ast::SliceAstType ) {
            auto slice = static_cast<SliceAst*>(node->slice);
            if ( auto tupleType = type.dynamicCast<IndexedContainer>() ) {
                DUChainReadLocker lock;
                auto newTuple = typeObjectForIntegralType<IndexedContainer>(QStringLiteral("tuple"));
                if ( ! newTuple ) {
                    continue;
                }
                long step = slice->step ? integerValue(slice->step) : 1;
                int len = tupleType->typesCount();
                long lower = slice->lower ? integerValue(slice->lower, len) : ((step > 0) ? 0 : len - 1);
                long upper = slice->upper ? integerValue(slice->upper, len) : ((step > 0) ? len : -1);
                if ( step != LONG_MIN && lower != LONG_MIN && upper != LONG_MIN) {
                    long ii = lower;
                    while ( (upper - ii) * step > 0 ) {
                        if ( 0 <= ii && ii < len ) {
                            newTuple->addEntry(tupleType->typeAt(ii).abstractType());
                        }
                        ii += step;
                    }
                }
                result = Helper::mergeTypes(result, newTuple);
                continue;
            }
        }
        if ( (node->slice->astType == Ast::SliceAstType) && type.dynamicCast<ListType>() ) {
            if ( type.dynamicCast<MapType>() ) {
                continue; // Can't slice dicts.
            }
            // Assume that slicing (e.g. foo[3:5]) a list returns the same type.
            result = Helper::mergeTypes(result, type);
        }
        else if ( const auto& indexed = type.dynamicCast<IndexedContainer>() ) {
            long sliceIndex = integerValue(node->slice, indexed->typesCount());
            if ( 0 <= sliceIndex && sliceIndex < indexed->typesCount() ) {
                result = Helper::mergeTypes(result, indexed->typeAt(sliceIndex).abstractType());
                continue;
            }
            // Index is unknown or invalid, could be returning any of the content types.
            result = Helper::mergeTypes(result, indexed->asUnsureType());
        }
        else if ( const auto& listType = type.dynamicCast<ListType>() ) {
            result = Helper::mergeTypes(result, listType->contentType().abstractType());
        }
        else {
            // Type wasn't one with custom handling, so use return type of __getitem__().
            DUChainReadLocker lock;
            static const IndexedIdentifier getitemIdentifier(KDevelop::Identifier(QStringLiteral("__getitem__")));
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
    auto type = typeObjectForIntegralType<ListType>(QStringLiteral("list"));
    lock.unlock();
    ExpressionVisitor contentVisitor(this);
    if ( type ) {
        for (ExpressionAst* content : std::as_const(node->elements)) {
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
    encounter(type);
}

void ExpressionVisitor::visitDictionaryComprehension(DictionaryComprehensionAst* node)
{
    DUChainReadLocker lock;
    auto type = typeObjectForIntegralType<MapType>(QStringLiteral("dict"));
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
    encounter(type);
}

void ExpressionVisitor::visitSetComprehension(SetComprehensionAst* node)
{
    Python::AstDefaultVisitor::visitSetComprehension(node);
    DUChainReadLocker lock;
    auto type = typeObjectForIntegralType<ListType>(QStringLiteral("set"));
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
    encounter(type);
}

void ExpressionVisitor::visitListComprehension(ListComprehensionAst* node)
{
    AstDefaultVisitor::visitListComprehension(node);
    DUChainReadLocker lock;
    auto type = typeObjectForIntegralType<ListType>(QStringLiteral("list"));
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
    encounter(type);
}

void ExpressionVisitor::visitTuple(TupleAst* node) {
    DUChainReadLocker lock;
    IndexedContainer::Ptr type = typeObjectForIntegralType<IndexedContainer>(QStringLiteral("tuple"));
    if ( type ) {
        lock.unlock();
        for (ExpressionAst* expr : std::as_const(node->elements)) {
            ExpressionVisitor v(this);
            v.visitNode(expr);
            if ( expr->astType == Ast::StarredAstType ) {
                // foo = a, *b, c
                if ( auto unpackedType = v.lastType().dynamicCast<IndexedContainer>() ) {
                    for ( int ii = 0; ii < unpackedType->typesCount(); ++ii ) {
                        type->addEntry(unpackedType->typeAt(ii).abstractType());
                    }
                } // Unpacking something else, do nothing (i.e. assume it was empty).
            } else {
                type->addEntry(v.lastType());
            }
        }
        encounter(type);
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
    auto type = typeObjectForIntegralType<ListType>(QStringLiteral("set"));
    lock.unlock();
    ExpressionVisitor contentVisitor(this);
    if ( type ) {
        for (ExpressionAst* content : std::as_const(node->elements)) {
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
    encounter(type);
}

void ExpressionVisitor::visitDict(DictAst* node)
{
    DUChainReadLocker lock;
    auto type = typeObjectForIntegralType<MapType>(QStringLiteral("dict"));
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
            else if ( auto unpackedType = contentVisitor.lastType().dynamicCast<MapType>() ) {
                // Key is null for `{**foo}`
                type->addContentType<Python::UnsureType>(unpackedType->contentType().abstractType());
                type->addKeyType<Python::UnsureType>(unpackedType->keyType().abstractType());
            }
        }
    }
    encounter(type);
}

void ExpressionVisitor::visitNumber(Python::NumberAst* number)
{
    AbstractType::Ptr type;
    DUChainReadLocker lock;
    if ( number->isInt ) {
        type = typeObjectForIntegralType<AbstractType>(QStringLiteral("int"));
    }
    else {
        type = typeObjectForIntegralType<AbstractType>(QStringLiteral("float"));
    }
    encounter(type);
}

void ExpressionVisitor::visitString(Python::StringAst* )
{
    DUChainReadLocker lock;
    StructureType::Ptr type = typeObjectForIntegralType<StructureType>(QStringLiteral("str"));
    encounter(type);
}

void ExpressionVisitor::visitBytes(Python::BytesAst* ) {
    DUChainReadLocker lock;
    auto type = typeObjectForIntegralType<StructureType>(QStringLiteral("bytes"));
    encounter(type);
}

void ExpressionVisitor::visitFormattedValue(Python::FormattedValueAst* node) {
    AstDefaultVisitor::visitFormattedValue(node);
    DUChainReadLocker lock;
    StructureType::Ptr type = typeObjectForIntegralType<StructureType>(QStringLiteral("str"));
    encounter(type);
}

void ExpressionVisitor::visitJoinedString(Python::JoinedStringAst* node)
{
    AstDefaultVisitor::visitJoinedString(node);
    DUChainReadLocker lock;
    StructureType::Ptr type = typeObjectForIntegralType<StructureType>(QStringLiteral("str"));
    encounter(type);
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
    CursorInRevision findNameBefore;
    if ( m_scanUntilCursor.isValid() ) {
        findNameBefore = m_scanUntilCursor;
    }
    else if ( m_forceGlobalSearching ) {
        findNameBefore = CursorInRevision::invalid();
    }
    else {
        findNameBefore = CursorInRevision(node->endLine, node->endCol);
    }
    DUChainReadLocker lock;
    Declaration* d = Helper::declarationForName(node, findNameBefore,
                                                DUChainPointer<const DUContext>(context()));

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
        auto type = p.dynamicCast<StructureType>();
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
            auto object_decl = context->findDeclarations(QualifiedIdentifier(QStringLiteral("object")));
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
        auto unsure = lhsVisitor.lastType().staticCast<KDevelop::UnsureType>();
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
    ExpressionVisitor v(this);
    AbstractType::Ptr result;

    for (const auto& expr : std::as_const(node->values)) {
        v.visitNode(expr);
        result = Helper::mergeTypes(result, v.lastType());
    }

    encounter(result);
}

void ExpressionVisitor::visitAssignmentExpression(Python::AssignmentExpressionAst* node) {
    visitNode(node->value);
}

}

