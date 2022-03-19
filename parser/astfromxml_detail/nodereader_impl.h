/*
 *  SPDX-FileCopyrightText: 2022 Sven Brauch <mail@svenbrauch.de>
 *
 *  SPDX-License-Identifier: LGPL-2.0-or-later
 */

#pragma once

#include "nodereader.h"
#include "fromxml_fwd.h"
#include "operators.h"

#define READ_CHILD_IMPL(name) \
    void readChild(ChildTag<name>, Stream& s) { singleFromXml(result, result->name, s); }
#define READ_CHILD_LIST_IMPL(name) \
    void readChild(ChildTag<name>, Stream& s) { listFromXml(result, result->name, s); }
#define READ_IDENTIFIER_IMPL(name) \
    void readAttribute(AttributeTag<name>, QStringRef const& value) { \
        result->name = new Identifier(value.toString()); \
    } \
    ~NodeReader() { \
        if (result->name) \
            result->name->rangeFrom(result); \
    }
#define IGNORE_CHILD(name) \
    void readChild(ChildTag<name>, Stream& s) { [[maybe_unused]] Ast* r; singleFromXml(result, r, s); }
#define IGNORE_CHILD_LIST(name) \
    void readChild(ChildTag<name>, Stream& s) { [[maybe_unused]] QList<Ast*> r; listFromXml(result, r, s); }

template<>
struct NodeReader<FunctionDefinitionAst> : public BaseNodeReader<FunctionDefinitionAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Attributes = enum { name };
    static auto constexpr AttributeNames = {"name"};

    using Children = enum { arguments, decorators, body, returns };
    static auto constexpr ChildNames = {"args", "decorator_list", "body", "returns"};

    READ_CHILD_IMPL(arguments)
    READ_CHILD_IMPL(returns)
    READ_CHILD_LIST_IMPL(body)
    READ_CHILD_LIST_IMPL(decorators)
    READ_IDENTIFIER_IMPL(name)
};

template<>
struct NodeReader<ArgumentsAst> : public BaseNodeReader<ArgumentsAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum {
        arguments, kwonlyargs, posonlyargs, defaultValues, vararg, kwarg, kw_defaults
    };
    static auto constexpr ChildNames = {
        "args", "kwonlyargs", "posonlyargs", "defaults", "vararg", "kwarg", "kw_defaults"
    };

    READ_CHILD_LIST_IMPL(arguments)
    READ_CHILD_LIST_IMPL(kwonlyargs)
    READ_CHILD_LIST_IMPL(posonlyargs)
    READ_CHILD_LIST_IMPL(defaultValues)
    READ_CHILD_LIST_IMPL(kw_defaults)
    READ_CHILD_IMPL(vararg)
    READ_CHILD_IMPL(kwarg)
};

template<>
struct NodeReader<ArgAst> : public BaseNodeReader<ArgAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { annotation };
    static auto constexpr ChildNames = {"annotation"};

    using Attributes = enum { argumentName };
    static auto constexpr AttributeNames = {"arg"};

    READ_CHILD_IMPL(annotation)

    void readAttribute(AttributeTag<argumentName>, QStringRef const& value) {
        result->argumentName = new Identifier(value.toString());
    }

    ~NodeReader() {
        result->argumentName->rangeFrom(result);
        result->copyRange(result->argumentName);
    };
};

template<>
struct NodeReader<PassAst> : public BaseNodeReader<PassAst>
{
    using BaseNodeReader::BaseNodeReader;
};

template<>
struct NodeReader<ReturnAst> : public BaseNodeReader<ReturnAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { value };
    static auto constexpr ChildNames = {"value"};

    READ_CHILD_IMPL(value);
};

template<>
struct NodeReader<NameAst> : public BaseNodeReader<NameAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Attributes = enum { identifier };
    static auto constexpr AttributeNames = {"id"};

    READ_IDENTIFIER_IMPL(identifier)
};

template<>
struct NodeReader<AssignmentAst> : public BaseNodeReader<AssignmentAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { targets, value };
    static auto constexpr ChildNames = {"targets", "value"};

    READ_CHILD_LIST_IMPL(targets)
    READ_CHILD_IMPL(value)
};

template<>
struct NodeReader<CodeAst> : public BaseNodeReader<CodeAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { body, type_ignores };
    static auto constexpr ChildNames = {"body", "type_ignores"};

    READ_CHILD_LIST_IMPL(body)
    READ_CHILD_LIST_IMPL(type_ignores)
};

template<>
struct NodeReader<BinaryOperationAst> : public BaseNodeReader<BinaryOperationAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { lhs, rhs };
    static auto constexpr ChildNames = {"left", "right"};

    using Attributes = enum { op };
    static auto constexpr AttributeNames = {"op"};

    READ_CHILD_IMPL(lhs)
    READ_CHILD_IMPL(rhs)

    void readAttribute(AttributeTag<op>, QStringRef const& value) {
        result->type = operatorType(value);
    }
};

template<>
struct NodeReader<ConstantAst> : public BaseNodeReader<ConstantAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Attributes = enum { value, constant_type };
    static auto constexpr AttributeNames = {"value", "constant_type"};

    void readAttribute(AttributeTag<value>, QStringRef const& value) {
        result->value = value.toString();
    }

    void readAttribute(AttributeTag<constant_type>, QStringRef const& value) {
        if (value == "float") {
            result->value = std::get<QString>(result->value).toFloat();
        }
        else if (value == "int") {
            result->value = std::get<QString>(result->value).toInt();
        }
        else if (value == "bytes") {
            result->value = std::get<QString>(result->value).toUtf8();
        }
    }
};

template<>
struct NodeReader<ClassDefinitionAst> : public BaseNodeReader<ClassDefinitionAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Attributes = enum { name };
    static auto constexpr AttributeNames = { "name" };

    using Children = enum { baseClasses, body, decorators, keywords };
    static auto constexpr ChildNames = { "bases", "body", "decorator_list", "keywords" };

    READ_CHILD_LIST_IMPL(baseClasses)
    READ_CHILD_LIST_IMPL(body)
    READ_CHILD_LIST_IMPL(decorators)
    IGNORE_CHILD_LIST(keywords)
    READ_IDENTIFIER_IMPL(name)
};

template<>
struct NodeReader<CallAst> : public BaseNodeReader<CallAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { function, arguments, keywords };
    static auto constexpr ChildNames = { "func", "args", "keywords" };

    READ_CHILD_IMPL(function)
    READ_CHILD_LIST_IMPL(arguments)
    READ_CHILD_LIST_IMPL(keywords)
};

template<>
struct NodeReader<ExpressionAst> : public BaseNodeReader<ExpressionAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { value };
    static auto constexpr ChildNames = { "value" };

    READ_CHILD_IMPL(value)
};

template<>
struct NodeReader<ListAst> : public BaseNodeReader<ListAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { elements };
    static auto constexpr ChildNames = { "elts" };

    READ_CHILD_LIST_IMPL(elements)
};

template<>
struct NodeReader<DictAst> : public BaseNodeReader<DictAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { keys, values };
    static auto constexpr ChildNames = { "keys", "values" };

    READ_CHILD_LIST_IMPL(keys)
    READ_CHILD_LIST_IMPL(values)
};

template<>
struct NodeReader<TupleAst> : public BaseNodeReader<TupleAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { elements };
    static auto constexpr ChildNames = { "elts" };

    READ_CHILD_LIST_IMPL(elements)
};

template<>
struct NodeReader<SetAst> : public BaseNodeReader<SetAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { elements };
    static auto constexpr ChildNames = { "elts" };

    READ_CHILD_LIST_IMPL(elements)
};

template<>
struct NodeReader<SubscriptAst> : public BaseNodeReader<SubscriptAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { value, slice };
    static auto constexpr ChildNames = { "value", "slice" };

    READ_CHILD_IMPL(value)
    READ_CHILD_IMPL(slice)
};

template<>
struct NodeReader<SliceAst> : public BaseNodeReader<SliceAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { lower, upper, step };
    static auto constexpr ChildNames = { "lower", "upper", "step" };

    READ_CHILD_IMPL(lower)
    READ_CHILD_IMPL(upper)
    READ_CHILD_IMPL(step)
};

template<>
struct NodeReader<BooleanOperationAst> : public BaseNodeReader<BooleanOperationAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Attributes = enum { op };
    static auto constexpr AttributeNames = { "op" };

    using Children = enum { values };
    static auto constexpr ChildNames = { "values" };

    READ_CHILD_LIST_IMPL(values)

    void readAttribute(AttributeTag<op>, QStringRef const& value) {
        result->type = booleanOperatorType(value);
    }
};

template<>
struct NodeReader<AttributeAst> : public BaseNodeReader<AttributeAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Attributes = enum { attribute };
    static auto constexpr AttributeNames = { "attr" };

    using Children = enum { value };
    static auto constexpr ChildNames = { "value" };

    READ_CHILD_IMPL(value)

    void readAttribute(AttributeTag<value>, QStringRef const& value) {
        result->attribute = new Identifier(value.toString());
    }

    ~NodeReader() {
        if (!result->attribute) {
            return;
        }
        result->attribute->copyRange(result);
        result->attribute->startCol = result->endCol - result->attribute->value.length() + 1;
        result->attribute->startLine = result->attribute->endLine;
        result->copyRange(result->attribute);
    }
};

template<>
struct NodeReader<ImportAst> : public BaseNodeReader<ImportAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { names };
    static auto constexpr ChildNames = { "names" };

    READ_CHILD_LIST_IMPL(names)
};

template<>
struct NodeReader<ImportFromAst> : public BaseNodeReader<ImportFromAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { names };
    static auto constexpr ChildNames = { "names" };

    using Attributes = enum { level, module };
    static auto constexpr AttributeNames = { "name", "module" };

    READ_CHILD_LIST_IMPL(names)

    void readAttribute(AttributeTag<module>, QStringRef const& value) {
        result->module = new Identifier(value.toString());
    };

    void readAttribute(AttributeTag<level>, QStringRef const& value) {
        result->level = value.toInt();
    }
};

template<>
struct NodeReader<AliasAst> : public BaseNodeReader<AliasAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Attributes = enum { name, asName };
    static auto constexpr AttributeNames = { "name", "asname" };

    void readAttribute(AttributeTag<name>, QStringRef const& value) {
        result->name = new Identifier(value.toString());
    }

    void readAttribute(AttributeTag<asName>, QStringRef const& value) {
        if (value != "None") {
            result->asName = new Identifier(value.toString());
        }
    }

    ~NodeReader() {
        if (result->name) {
            result->name->copyRange(result);
        }
        if (result->asName) {
            result->asName->copyRange(result);
        }
    }
};

template<>
struct NodeReader<ListComprehensionAst> : public BaseNodeReader<ListComprehensionAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { element, generators };
    static auto constexpr ChildNames = { "elt", "generators" };

    READ_CHILD_IMPL(element)
    READ_CHILD_LIST_IMPL(generators)
};

template<>
struct NodeReader<SetComprehensionAst> : public BaseNodeReader<SetComprehensionAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { element, generators };
    static auto constexpr ChildNames = { "elt", "generators" };

    READ_CHILD_IMPL(element)
    READ_CHILD_LIST_IMPL(generators)
};

template<>
struct NodeReader<DictionaryComprehensionAst> : public BaseNodeReader<DictionaryComprehensionAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { key, value, generators };
    static auto constexpr ChildNames = { "key", "value", "generators" };

    READ_CHILD_IMPL(key)
    READ_CHILD_IMPL(value)
    READ_CHILD_LIST_IMPL(generators)
};

template<>
struct NodeReader<ComprehensionAst> : public BaseNodeReader<ComprehensionAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { target, iterator, conditions };
    static auto constexpr ChildNames = { "target", "iter", "ifs" };

    READ_CHILD_IMPL(target)
    READ_CHILD_IMPL(iterator)
    READ_CHILD_LIST_IMPL(conditions)
};

template<>
struct NodeReader<UnaryOperationAst> : public BaseNodeReader<UnaryOperationAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { operand };
    static auto constexpr ChildNames = { "operand" };

    using Attributes = enum { op };
    static auto constexpr AttributeNames = {"op"};

    READ_CHILD_IMPL(operand)

    void readAttribute(AttributeTag<op>, QStringRef const& value) {
        result->type = unaryOperatorType(value);
    }
};

template<>
struct NodeReader<LambdaAst> : public BaseNodeReader<LambdaAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { arguments, body };
    static auto constexpr ChildNames = { "args", "body" };

    READ_CHILD_IMPL(arguments)
    READ_CHILD_IMPL(body)
};

template<>
struct NodeReader<JoinedStringAst> : public BaseNodeReader<JoinedStringAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { values };
    static auto constexpr ChildNames = { "values" };

    READ_CHILD_LIST_IMPL(values)
};

template<>
struct NodeReader<AugmentedAssignmentAst> : public BaseNodeReader<AugmentedAssignmentAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { target, value };
    static auto constexpr ChildNames = { "target", "value" };

    using Attributes = enum { op };
    static auto constexpr AttributeNames = {"op"};

    READ_CHILD_IMPL(target)
    READ_CHILD_IMPL(value)

    void readAttribute(AttributeTag<op>, QStringRef const& value) {
        result->op = operatorType(value);
    }
};

template<>
struct NodeReader<DeleteAst> : public BaseNodeReader<DeleteAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { targets };
    static auto constexpr ChildNames = { "targets" };

    READ_CHILD_LIST_IMPL(targets)
};

template<>
struct NodeReader<ForAst> : public BaseNodeReader<ForAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { target, iterator, body, orelse };
    static auto constexpr ChildNames = { "target", "iter", "body", "orelse" };

    READ_CHILD_IMPL(target)
    READ_CHILD_IMPL(iterator)
    READ_CHILD_LIST_IMPL(body)
    READ_CHILD_LIST_IMPL(orelse)
};

template<>
struct NodeReader<WhileAst> : public BaseNodeReader<WhileAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { condition, body, orelse };
    static auto constexpr ChildNames = { "test", "body", "orelse" };

    READ_CHILD_IMPL(condition)
    READ_CHILD_LIST_IMPL(body)
    READ_CHILD_LIST_IMPL(orelse)
};

template<>
struct NodeReader<IfAst> : public BaseNodeReader<IfAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { condition, body, orelse };
    static auto constexpr ChildNames = { "test", "body", "orelse" };

    READ_CHILD_IMPL(condition)
    READ_CHILD_LIST_IMPL(body)
    READ_CHILD_LIST_IMPL(orelse)
};

template<>
struct NodeReader<IfExpressionAst> : public BaseNodeReader<IfExpressionAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { condition, body, orelse };
    static auto constexpr ChildNames = { "test", "body", "orelse" };

    READ_CHILD_IMPL(condition)
    READ_CHILD_IMPL(body)
    READ_CHILD_IMPL(orelse)
};

template<>
struct NodeReader<WithAst> : public BaseNodeReader<WithAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { body, items };
    static auto constexpr ChildNames = { "items", "body" };

    READ_CHILD_LIST_IMPL(body)
    READ_CHILD_LIST_IMPL(items)
};

template<>
struct NodeReader<WithItemAst> : public BaseNodeReader<WithItemAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { contextExpression, optionalVars };
    static auto constexpr ChildNames = { "context_expr", "optional_vars" };

    READ_CHILD_IMPL(contextExpression)
    READ_CHILD_IMPL(optionalVars)
};

template<>
struct NodeReader<CompareAst> : public BaseNodeReader<CompareAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { leftmostElement, operators, comparands };
    static auto constexpr ChildNames = { "left", "ops", "comparators" };

    READ_CHILD_IMPL(leftmostElement)
    READ_CHILD_LIST_IMPL(comparands)

    void readChild(ChildTag<operators>, Stream& s) {
        while (s.readNextStartElement()) {
            result->operators << comparisonOperatorType(s.name());
            s.readNext();
        }
    }
};

template<>
struct NodeReader<GeneratorExpressionAst> : public BaseNodeReader<GeneratorExpressionAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { element, generators };
    static auto constexpr ChildNames = { "elt", "generators" };

    READ_CHILD_IMPL(element)
    READ_CHILD_LIST_IMPL(generators)
};

template<>
struct NodeReader<RaiseAst> : public BaseNodeReader<RaiseAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { type };
    static auto constexpr ChildNames = { "exc" };

    READ_CHILD_IMPL(type)
};

template<>
struct NodeReader<KeywordAst> : public BaseNodeReader<KeywordAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { value };
    static auto constexpr ChildNames = { "value" };

    using Attributes = enum { argumentName };
    static auto constexpr AttributeNames = { "arg" };

    READ_CHILD_IMPL(value)
    READ_IDENTIFIER_IMPL(argumentName)
};

template<>
struct NodeReader<StarredAst> : public BaseNodeReader<StarredAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { value };
    static auto constexpr ChildNames = { "value" };

    READ_CHILD_IMPL(value)
};

template<>
struct NodeReader<TryAst> : public BaseNodeReader<TryAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { body, handlers, orelse, finally };
    static auto constexpr ChildNames = { "body", "handlers", "orelse", "finalbody" };

    READ_CHILD_LIST_IMPL(body)
    READ_CHILD_LIST_IMPL(handlers)
    READ_CHILD_LIST_IMPL(orelse)
    READ_CHILD_LIST_IMPL(finally)
};

template<>
struct NodeReader<ExceptionHandlerAst> : public BaseNodeReader<ExceptionHandlerAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Attributes = enum { name };
    static auto constexpr AttributeNames = { "name" };

    using Children = enum { type, body };
    static auto constexpr ChildNames = { "type", "body" };

    READ_CHILD_IMPL(type)
    READ_CHILD_LIST_IMPL(body)
    READ_IDENTIFIER_IMPL(name)
};

template<>
struct NodeReader<FormattedValueAst> : public BaseNodeReader<FormattedValueAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { value, formatSpec };
    static auto constexpr ChildNames = { "value", "format_spec" };

    using Attributes = enum { conversion };
    static auto constexpr AttributeNames = { "conversion" };

    READ_CHILD_IMPL(value)
    READ_CHILD_IMPL(formatSpec)

    void readAttribute(AttributeTag<conversion>, QStringRef const& value) {
        result->conversion = value.toInt();
    }
};

template<>
struct NodeReader<AnnotationAssignmentAst> : public BaseNodeReader<AnnotationAssignmentAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { target, value, annotation };
    static auto constexpr ChildNames = { "target", "annotation", "value" };

    READ_CHILD_IMPL(target)
    READ_CHILD_IMPL(value)
    READ_CHILD_IMPL(annotation)
};

template<>
struct NodeReader<AssertionAst> : public BaseNodeReader<AssertionAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { condition, message };
    static auto constexpr ChildNames = { "test", "msg" };

    READ_CHILD_IMPL(condition)
    READ_CHILD_IMPL(message)
};

template<>
struct NodeReader<BreakAst> : public BaseNodeReader<BreakAst>
{
    using BaseNodeReader::BaseNodeReader;
};

template<>
struct NodeReader<ContinueAst> : public BaseNodeReader<ContinueAst>
{
    using BaseNodeReader::BaseNodeReader;
};

template<>
struct NodeReader<NonlocalAst> : public BaseNodeReader<NonlocalAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { names };
    static auto constexpr ChildNames = { "names" };

    void readChild(ChildTag<names>, Stream& s) {
        while (s.readNextStartElement()) {
            result->names << new Identifier(s.name().toString()); // FIXME this isn't serialized properly
            s.readNext();
        }
    }
};

template<>
struct NodeReader<GlobalAst> : public BaseNodeReader<GlobalAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { names };
    static auto constexpr ChildNames = { "names" };

    void readChild(ChildTag<names>, Stream& s) {
        while (s.readNextStartElement()) {
            result->names << new Identifier(s.name().toString()); // FIXME this isn't serialized properly
            s.readNext();
        }
    }
};

template<>
struct NodeReader<YieldAst> : public BaseNodeReader<YieldAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { value };
    static auto constexpr ChildNames = { "value" };

    READ_CHILD_IMPL(value)
};

template<>
struct NodeReader<AssignmentExpressionAst> : public BaseNodeReader<AssignmentExpressionAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { target, value };
    static auto constexpr ChildNames = { "target", "value" };

    READ_CHILD_IMPL(target)
    READ_CHILD_IMPL(value)
};
