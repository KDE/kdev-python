/*
 *  SPDX-FileCopyrightText: 2022 Sven Brauch <mail@svenbrauch.de>
 *
 *  SPDX-License-Identifier: LGPL-2.0-or-later
 */

#pragma once

#include <QXmlStreamReader>
#include <QMap>

#include "ast.h"

namespace Python
{

CodeAst* astFromXml(QString const& data);

}

