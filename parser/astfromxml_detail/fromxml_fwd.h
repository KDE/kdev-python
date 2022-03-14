#pragma once

#include <QXmlStreamReader>
#include "ast.h"

using namespace Python;

using Stream = QXmlStreamReader;

Ast* getSingleElement(Stream& s);

template<typename AstT>
void listFromXml(Ast* parent, QList<AstT*>& ret, Stream& s);

template<typename AstT>
void singleFromXml(Ast* parent, AstT*& ret, Stream& s);
