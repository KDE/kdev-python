#pragma once
#include "python_header.h"

#include <optional>

#include <QByteArray>
#include <QString>

namespace Python {

struct ParseError {
    QString file;
    int line, column;
    QString message;
};

struct ParseResult {
    std::optional<ParseError> error;
    QByteArray xmlOut;
};

std::optional<ParseResult> parsePythonCode(QByteArray const& code);

}
