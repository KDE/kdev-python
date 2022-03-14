#pragma once

#include "nodereader.h"
#include "fromxml_fwd.h"

template<>
struct NodeReader<FunctionDefinitionAst> : public BaseNodeReader<FunctionDefinitionAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Attributes = enum { name };
    static auto constexpr AttributeNames = {"name"};

    using Children = enum { arguments, decorators, body, returns };
    static auto constexpr ChildNames = {"arguments", "decorators", "body", "returns"};

    void readAttribute(AttributeTag<name>, QStringRef const& value) {
        result->name = new Identifier(value.toString());
    }

    void readChild(ChildTag<arguments>, Stream& s) {
        singleFromXml(result, result->arguments, s);
    }

    void readChild(ChildTag<decorators>, Stream& s) {
        listFromXml(result, result->decorators, s);
    }

    void readChild(ChildTag<body>, Stream& s) {
        listFromXml(result, result->body, s);
    }

    void readChild(ChildTag<returns>, Stream& s) {
        singleFromXml(result, result->returns, s);
    }
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
};

template<>
struct NodeReader<AssignmentAst> : public BaseNodeReader<AssignmentAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { targets, value };
    static auto constexpr ChildNames = {"targets", "value"};

    void readChild(ChildTag<targets>, Stream& s) {
        listFromXml(result, result->targets, s);
    }

    void readChild(ChildTag<value>, Stream& s) {
        singleFromXml(result, result->value, s);
    }
};

template<>
struct NodeReader<CodeAst> : public BaseNodeReader<CodeAst>
{
    using BaseNodeReader::BaseNodeReader;

    using Children = enum { body };
    static auto constexpr ChildNames = {"body"};

    void readChild(ChildTag<body>, Stream& s) {
        listFromXml(result, result->body, s);
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
