/*
    SPDX-FileCopyrightText: 2024 Jarmo Tiitto <jarmo.tiitto@gmail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/
#include <QMetaObject>
#include <QMetaMethod>

#include "pdbdebuggerinstance.h"
#include "pdbprocess.h"
#include "debuggerdebug.h"

namespace Python {

PdbDebuggerInstance::PdbDebuggerInstance(QObject* parent)
    : QObject(parent)
    , m_instance(new PdbProcess(this))
    , m_currentSeqnro(-PdbProcess::FRAMES_BEFORE_READY)
{
    connect(m_instance, &PdbProcess::dataReceived, this, &PdbDebuggerInstance::decodeResponse);
}

PdbDebuggerInstance::~PdbDebuggerInstance()
{
}

int PdbDebuggerInstance::currentSeqnro() const
{
    return m_currentSeqnro;
}

void PdbDebuggerInstance::setMethod(int seqnro, CmdCallback callback)
{
    if (callback) {
        m_callbacks.emplace(seqnro).value() = std::move(callback);
    } else {
        // Try erase instead of inserting.
        auto itr = m_callbacks.find(seqnro);
        if (itr != m_callbacks.end()) {
            m_callbacks.erase(itr);
        }
    }
}

void PdbDebuggerInstance::request(std::initializer_list<QJsonValue> command_and_args, CmdCallback callback)
{
    // Assemble the request body.
    QJsonObject cmd;
    cmd.insert(QStringLiteral("seq"), QJsonValue(m_currentSeqnro));
    const auto itr = cmd.insert(QStringLiteral("input"), QJsonArray(command_and_args));

    // Register the callback object.
    setMethod(m_currentSeqnro, callback);
    qCDebug(KDEV_PYTHON_DEBUGGER).noquote()
        << "seqnro" << m_currentSeqnro << "assigned for request(" << itr.value() << ")";
    ++m_currentSeqnro;

    // Encode and send.
    m_instance->sendCommand(QJsonDocument(cmd).toJson(QJsonDocument::JsonFormat::Compact));
}

void PdbDebuggerInstance::defer(CmdCallback callback)
{
    Q_ASSERT(callback);

    // Assemble a request body without "input".
    QJsonObject cmd{std::make_pair(QStringLiteral("seq"), QJsonValue(m_currentSeqnro))};

    // Register the callback object.
    m_callbacks.emplace(m_currentSeqnro).value() = std::move(callback);
    qCDebug(KDEV_PYTHON_DEBUGGER).noquote() << "seqnro" << m_currentSeqnro << "assigned for defer()";
    ++m_currentSeqnro;

    // Encode and send.
    m_instance->sendCommand(QJsonDocument(cmd).toJson(QJsonDocument::JsonFormat::Compact));
}

void PdbDebuggerInstance::decodeResponse(const QByteArray& data)
{
    QJsonParseError error;
    const auto body = QJsonDocument::fromJson(data, &error);
    if (error.error != QJsonParseError::NoError) {
        // Malformed JSON response.
        qCCritical(KDEV_PYTHON_DEBUGGER) << "Received bad response data-frame! Error:" << error.errorString();
        return;
    }

    // Decode the response up to the individual fields it can contain.
    if (!body.isObject()) {
        qCCritical(KDEV_PYTHON_DEBUGGER) << "Received an invalid response! (not an object)!";
        return;
    }
    const auto obj = body.object();
    const int responseSeqnro = obj.value(QStringLiteral("seq")).toInt(-1);
    // Ensure next request has a greater seqnro than this response's seqnro.
    m_currentSeqnro = std::max(m_currentSeqnro, responseSeqnro + 1);

    qCDebug(KDEV_PYTHON_DEBUGGER) << "seqnro" << responseSeqnro << "completed";

    /*
     * Defer rest of the work to a later point, so we don't hog the main thread for too long. The
     * debugger process can also send a responses before the all of the handlers have been invoked,
     * which improves parallelization.
     */
    m_queue.emplace_back(Response{obj.value(QStringLiteral("data")).toArray(), responseSeqnro});
    QMetaObject::invokeMethod(this, &PdbDebuggerInstance::process, Qt::QueuedConnection);
}

void PdbDebuggerInstance::process()
{
    Q_ASSERT(!m_queue.empty());
    const auto& item = m_queue.front();

    // TODO: item.fields should perhaps be transformed into a list of pair<QString, QJsonValue>?
    ResponseData response;
    static const auto messageKey = QStringLiteral("message");
    static const auto errorKey = QStringLiteral("error");

    for (const auto& item : item.fields) {
        const auto& obj = response.emplace_back(item.toObject());
        // Log "message" and "error" response fields, if they exist.
        if (obj.contains(messageKey)) {
            qCDebug(KDEV_PYTHON_DEBUGGER) << "message:" << obj.value(messageKey).toString();
        } else if (obj.contains(errorKey)) {
            // Log as an warning, since this usually means the request failed.
            qCWarning(KDEV_PYTHON_DEBUGGER) << "error:" << obj.value(errorKey).toString();
        }
    }

    // Forward the data into the callback currently assigned for the seqnro, or ignore the response.
    CmdCallback handler;
    auto itr = m_callbacks.find(item.seqnro);
    if (itr != m_callbacks.end()) {
        handler = std::move(itr.value());
        m_callbacks.erase(itr);
    }

    if (handler) {
        qCDebug(KDEV_PYTHON_DEBUGGER) << "invoking seqnro" << item.seqnro << "handler with:" << response;
        // Invoke the method.
        handler(std::as_const(response));
    } else {
        // No callback was assigned.
        qCDebug(KDEV_PYTHON_DEBUGGER) << "discarding seqnro" << item.seqnro << "result:" << response;
    }

    m_queue.pop_front();
    if (m_queue.empty()) {
        m_instance->signalSuspended();
    }
}

QJsonValue responseValue(const ResponseData& data, QStringView field)
{
    for (const auto& item : data) {
        if (item.contains(field)) {
            return item.value(field);
        }
    }
    return QJsonValue(QJsonValue::Undefined);
}

QJsonObject responseObject(const ResponseData& data, QStringView field)
{
    auto value = responseValue(data, field);
    if (value.isObject()) {
        return value.toObject();
    } else {
        return QJsonObject();
    }
}

QJsonArray responseArray(const ResponseData& data, QStringView field)
{
    auto value = responseValue(data, field);
    if (value.isArray()) {
        return value.toArray();
    } else {
        return QJsonArray();
    }
}

}

#include "moc_pdbdebuggerinstance.cpp"
