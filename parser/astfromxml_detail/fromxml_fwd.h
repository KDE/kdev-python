/*
 *  SPDX-FileCopyrightText: 2022 Sven Brauch <mail@svenbrauch.de>
 *
 *  SPDX-License-Identifier: LGPL-2.0-or-later
 */

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
