#pragma once

#include "nodereader.h"
#include "fromxml_fwd.h"
#include "operators.h"

#define READ_CHILD_IMPL(name) \
    void readChild(ChildTag<name>, Stream& s) { singleFromXml(result, result->name, s); }
#define READ_CHILD_LIST_IMPL(name) \
    void readChild(ChildTag<name>, Stream& s) { listFromXml(result, result->name, s); }

template<>
struct NodeReader<FunctionDefinitionAst> : public BaseNodeReader<FunctionDefinitionAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Attributes = enum { name };
    static auto constexpr AttributeNames = {"name"};

    using Children = enum { arguments, decorators, body, returns };
    static auto constexpr ChildNames = {"args", "decorator_list", "body", "returns"};

    void readAttribute(AttributeTag<name>, QStringRef const& value) {
        result->name = new Identifier(value.toString());
    }

    READ_CHILD_IMPL(arguments)
    READ_CHILD_IMPL(returns)
    READ_CHILD_LIST_IMPL(body)
    READ_CHILD_LIST_IMPL(decorators)

    ~NodeReader() {
        result->name->rangeFrom(result);
    }
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

    void readAttribute(AttributeTag<identifier>, QStringRef const& value) {
        result->identifier = new Identifier(value.toString());
    }

    ~NodeReader() {
        result->identifier->rangeFrom(result);
    }
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
    }
};
