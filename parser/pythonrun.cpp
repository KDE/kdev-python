#include "pythonrun.h"
#include "python_header.h"
#include "parserdebug.h"

#include <QStringList>
#include <QFile>

namespace {

using namespace Python;

std::optional<ParseError> parseErrorFromString(QByteArray const& data) {
    auto const lineData = QString::fromUtf8(data);
    auto const& lines = lineData.split("\n");
    if (lines.size() < 5) {
        return std::nullopt;
    }

    ParseError ret;
    bool ok;
    ret.file = lines[1];
    ret.line = lines[2].toInt(&ok);
    if (!ok) {
        return std::nullopt;
    }
    ret.column = lines[3].toInt(&ok);
    if (!ok) {
        return std::nullopt;
    }
    ret.message = lines.mid(4, -1).join("\n");

    return ret;
}

class ParserModule {
public:
    ParserModule() {
        Py_Initialize();

        m_module = PyModule_New("parser");
        auto* localVars = PyModule_GetDict(m_module);

        auto codeFile = QFile(":/ast2xml.py");
        codeFile.open(QIODevice::ReadOnly);
        auto const& code = codeFile.readAll();
        auto* ret = PyRun_String(code.data(), Py_file_input, localVars, localVars);
        if (!ret) {
            return;
        }
        Py_DECREF(ret);

        m_func = PyObject_GetAttrString(m_module, "doParse");
    }

    ~ParserModule() {
        Py_DECREF(m_func);
        Py_DECREF(m_module);
        Py_Finalize();
    }

    bool isInitialized() const {
        return m_func != nullptr;
    }

    std::optional<ParseResult> parse(QByteArray const& in) {
        if (!isInitialized()) {
            qCWarning(KDEV_PYTHON_PARSER) << "Failed to initialize";
            return std::nullopt;
        }

        auto* args = PyTuple_New(1);
        auto* value = PyUnicode_FromString(in.data());
        PyTuple_SetItem(args, 0, value);

        value = PyObject_CallObject(m_func, args);
        Py_DECREF(args);
        if (!value) {
            qCWarning(KDEV_PYTHON_PARSER) << "Failed to call function";
            return std::nullopt;
        }
        ssize_t size;
        const auto* result = PyUnicode_AsUTF8AndSize(value, &size);
        const auto resultBytes = QByteArray(result, size);

        std::optional<ParseResult> ret;
        if (size > 0 && result[0] == '<') {
            ret = ParseResult{std::nullopt, resultBytes};
        }
        else if (auto const error = parseErrorFromString(resultBytes)) {
            ret = ParseResult{error, {}};
        }
        else {
            qCWarning(KDEV_PYTHON_PARSER) << "Invalid result:" << result;
        }
        Py_DECREF(value);

        return ret;
    }

    PyObject* m_module = nullptr;
    PyObject* m_func = nullptr;
};

}

namespace Python {

std::optional<ParseResult> parsePythonCode(QByteArray const& code)
{
    static ParserModule parserTool;
    return parserTool.parse(code);
}

}
