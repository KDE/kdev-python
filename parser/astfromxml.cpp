#include "astfromxml.h"

#include <initializer_list>
#include <type_traits>

#include <QList>

using namespace Python;

using StringList = std::initializer_list<const char*>;
template<int Attr> using AttributeTag = std::integral_constant<int, Attr>;
template<int Child> using ChildTag = std::integral_constant<int, Child>;

using Stream = QXmlStreamReader;

enum global_attributes {col_offset = -1, lineno = -2, last_global_attribute = lineno};
StringList global_attribute_names = {"col_offset", "lineno"};

template<typename Attributes, int AttributeCount, typename Children, int ChildCount, typename Reader>
struct NodeReadHelper {
    constexpr NodeReadHelper(Reader* r, StringList attributeNames, StringList childNames)
        : r(r)
        , attributeNames(attributeNames)
        , childNames(childNames)
    {
    }

    template<int N>
    void tryReadAttributes(QStringRef const& attributeName, QStringRef const& attributeValue) {
        if constexpr (N >= 0) {
            if (attributeName == *(r->AttributeNames.begin() + N)) {
                r->readAttribute(AttributeTag<N>{}, attributeValue);
                return;
            }
        }
        else {
            if (attributeName == *(global_attribute_names.begin() - (N+1))) {
                r->readGlobalAttribute(AttributeTag<N>{}, attributeValue);
                return;
            }
        }

        if constexpr (N > last_global_attribute)
            tryReadAttributes<N-1>(attributeName, attributeValue);
        if constexpr (N == last_global_attribute)
            qWarning() << "failed to match xml attribute name:" << attributeName;
    }

    void readAttributes(Stream& s) {
        if constexpr (AttributeCount > 0) {
            auto const& attributes = s.attributes();
            for (auto const& attr: attributes) {
                qDebug() << "read attribute:" << attr.name() << attr.value();
                tryReadAttributes<AttributeCount - 1>(attr.name(), attr.value());
            }
        }
    }

    template<int N>
    void readSingleChild(QStringRef const& childName, Stream& s) {
        auto const nameMatches = childName == *(r->ChildNames.begin() + N);
        qDebug() << "checking child name:" << nameMatches << childName << *(r->ChildNames.begin() + N) << N;
        if (nameMatches) {
            r->readChild(ChildTag<N>{}, s);
        }
        else {
            if constexpr (N > 0)
                readSingleChild<N-1>(childName, s);
            if constexpr (N == 0)
                qWarning() << "failed to match xml child attribute:" << childName;
        }
    }

    void readChildren(Stream& s) {
        if constexpr (ChildCount > 0) {
            qDebug() << " >> starting read list";
            while (s.readNextStartElement()) {
                qDebug() << "read node attribute child:" << s.name();
                readSingleChild<ChildCount - 1>(s.name(), s);
            }
            qDebug() << " << finished read list:" << s.name();
        }
    };

    Reader* r;
    const StringList attributeNames, childNames;
};

template<typename Derived>
void doReadNode(Derived* r, Stream& s)
{
    using ThisReader = NodeReadHelper<
        typename Derived::Attributes, Derived::AttributeNames.size(),
        typename Derived::Children, Derived::ChildNames.size(),
        Derived
    >;

    ThisReader reader(r, r->AttributeNames, r->ChildNames);
    reader.readAttributes(s);
    reader.readChildren(s);
}

template<typename AstT>
struct NodeReader
{
};

template<typename AstT>
struct BaseNodeReader
{
    using Children = enum {};
    using Attributes = enum {};

    static constexpr StringList ChildNames = {};
    static constexpr StringList AttributeNames = {};

    AstT* read(Stream& s) {
        using Derived = NodeReader<AstT>;
        auto* derivedInstance = static_cast<Derived*>(this);
        doReadNode<Derived>(derivedInstance, s);
        return derivedInstance->result;
    }

    void readGlobalAttribute(AttributeTag<col_offset>, QStringRef const& value) {
        result->startCol = value.toInt();
    }

    void readGlobalAttribute(AttributeTag<lineno>, QStringRef const& value) {
        result->startLine = value.toInt();
    }

    AstT* result;

    BaseNodeReader(Ast* parent) {
        result = new AstT(parent);
    }
};


Ast* getSinglElement(Stream& s);

template<typename AstT>
void listFromXml(Ast* parent, QList<AstT*>& ret, Stream& s);

template<typename AstT>
void singleFromXml(Ast* parent, AstT*& ret, Stream& s);

/////////////////////////////////////

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

/////////////////////////////////////

QMap<QString, Ast::AstType> astTypes = {
    {QStringLiteral("Constant"), Ast::ConstantAstType},
    {QStringLiteral("Module"), Ast::CodeAstType},
    {QStringLiteral("Assign"), Ast::AssignmentAstType},
    {QStringLiteral("Name"), Ast::NameAstType}
};

Ast::AstType astTypeFromString(QString const& name)
{
    return astTypes[name];
}

struct ToEndElement {
    ToEndElement(Stream& s) : s(s) {};
    ~ToEndElement() { while (s.readNext() != QXmlStreamReader::EndElement) {} }
    Stream& s;
};

Ast* getSingleElement(Ast* parent, Stream& s)
{
    auto ok = s.readNextStartElement();
    qDebug() << "read element:" << s.name() << "at end" << s.atEnd() << "error" << s.errorString();
    if (!ok) {
        return nullptr;
    }

    auto const& name = s.name();
    auto const astType = astTypeFromString(name.toString());

    ToEndElement toEnd(s);

    switch (astType) {
        case Ast::NameAstType:
            return NodeReader<NameAst>(parent).read(s);
        case Ast::AssignmentAstType:
            return NodeReader<AssignmentAst>(parent).read(s);
        case Ast::CodeAstType:
            return NodeReader<CodeAst>(parent).read(s);
        case Ast::ConstantAstType:
            return NodeReader<ConstantAst>(parent).read(s);
    };

    qWarning() << "Invalid AST type encountered:" << astType << "name" << name.toString();
    return nullptr;
}

template<typename AstT>
void listFromXml(Ast* parent, QList<AstT*>& ret, Stream& s)
{
    while (auto* ast = getSingleElement(parent, s)) {
        ret.push_back(static_cast<AstT*>(ast));
    }
    qDebug() << "read:" << ret.size() << "list items";
}

template<typename AstT>
void singleFromXml(Ast* parent, AstT*& ret, Stream& s)
{
    auto* ast = getSingleElement(parent, s);
    ret = static_cast<AstT*>(ast);
}

CodeAst* Python::astFromXml(QString const& data)
{
    QXmlStreamReader s(data);
    if (s.readNext() != QXmlStreamReader::StartDocument) {
        return nullptr;
    }
    return static_cast<CodeAst*>(getSingleElement(nullptr, s));
}

