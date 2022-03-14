#include "astfromxml.h"

#include "astfromxml_detail/typemap.h"
#include "astfromxml_detail/typeswitch.h"
#include "astfromxml_detail/nodereader.h"
#include "astfromxml_detail/nodereader_impl.h"

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

    auto* ast = readTyped(parent, astType, s);
    if (ast)
        return ast;

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

