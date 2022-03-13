#pragma once

#include <QXmlStreamReader>
#include <QMap>

#include "ast.h"

namespace Python
{

CodeAst* astFromXml(QString const& data);

}

