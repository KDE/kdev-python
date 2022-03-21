/*
 *  SPDX-FileCopyrightText: 2022 Sven Brauch <mail@svenbrauch.de>
 *
 *  SPDX-License-Identifier: LGPL-2.0-or-later
 */

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
    ~ToEndElement() { while (!s.atEnd() && s.readNext() != QXmlStreamReader::EndElement) {} }
    Stream& s;
};

Ast* getSingleElement(Ast* parent, Stream& s)
{
    auto ok = s.readNextStartElement();
    if (s.name() == "vararg")
        Q_ASSERT(false);
    if (!ok) {
        return nullptr;
    }

    auto const& name = s.name();
    auto const astType = astTypeFromString(name.toString());

    auto* ast = readTyped(parent, astType, s);
    if (ast)
        return ast;

    qWarning() << "Invalid AST type encountered:" << astType << "name" << name.toString();
    Q_ASSERT(false);
    return nullptr;
}

template<typename AstT>
void listFromXml(Ast* parent, QList<AstT*>& ret, Stream& s)
{
    while (auto* ast = getSingleElement(parent, s)) {
        ret.push_back(static_cast<AstT*>(ast));
    }
}

template<typename AstT>
void singleFromXml(Ast* parent, AstT*& ret, Stream& s)
{
    auto* ast = getSingleElement(parent, s);
    ret = static_cast<AstT*>(ast);
    [[maybe_unused]] auto end = s.readNextStartElement();
    Q_ASSERT(!end && s.tokenType() == QXmlStreamReader::EndElement);
}

CodeAst* Python::astFromXml(QString const& data)
{
    QXmlStreamReader s(data);
    if (s.readNext() != QXmlStreamReader::StartDocument) {
        return nullptr;
    }
    return static_cast<CodeAst*>(getSingleElement(nullptr, s));
}

