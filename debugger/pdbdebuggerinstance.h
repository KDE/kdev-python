/*
    SPDX-FileCopyrightText: 2024 Jarmo Tiitto <jarmo.tiitto@gmail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef KDEVPDBINSTANCE_H
#define KDEVPDBINSTANCE_H

#include <QJsonArray>
#include <QJsonDocument>
#include <QJsonObject>
#include <QObject>
#include <QPointer>
#include <QString>
#include <QList>

#include <deque>
#include <functional>

namespace Python {

class PdbProcess;

using ResponseData = QList<QJsonObject>;

/**
 * Find a response field and return it as an value.
 * @return a JSON value or QJsonValue(Undefined) if the field did not exist.
 */
QJsonValue responseValue(const ResponseData& data, QStringView field);

/**
 * Find a response field and return it as an object.
 * @return a non-empty JSON object if the field was found.
 */
QJsonObject responseObject(const ResponseData& data, QStringView field);

/**
 * Find a response field and return it as an array.
 * @return a non-empty JSON array if the field was found.
 */
QJsonArray responseArray(const ResponseData& data, QStringView field);

/**
 * Provides the high-level request - response interface for the PdbProcess class.
 */
class PdbDebuggerInstance : public QObject
{
    Q_OBJECT
public:
    using CmdCallback = std::function<void(const ResponseData&)>;

    /**
     * Construct a PdbProcess instance.
     * @note PdbDebuggerInstance only handles the PdbProcess::dataReceived() signal,
     *       and leaves further configuration of the PdbProcess to the caller.
     */
    PdbDebuggerInstance(QObject* parent = nullptr);
    ~PdbDebuggerInstance();

    /**
     * Get the underlying PdbProcess.
     */
    PdbProcess* instance() const
    {
        return m_instance;
    }

    /**
     * Get the command sequence number that request() would use next.
     */
    int currentSeqnro() const;

    /**
     * Replace existing or assign a new callback for an sequence number.
     */
    void setMethod(int seqnro, CmdCallback callback);

    /**
     * Send a request to the Pdb debugger process.
     * @param command_and_args a command followed by its arguments.
     * @brief
     *   The @p callback is invoked if it has a target, when
     *   the response JSON data has been received and decoded.
     */
    void request(std::initializer_list<QJsonValue> command_and_args, CmdCallback callback = {});

    /**
     * Queue a callback.
     * @brief
     *   The callback is queued and it is invoked once all earlier request handlers have run.
     *   The response JSON data is always empty.
     *   The @p callback to be invoked. It must have a target.
     */
    void defer(CmdCallback callback);

private Q_SLOTS:
    /// Internal slot to handle responses from the debugger.
    void decodeResponse(const QByteArray& data);

private:
    PdbProcess* m_instance = nullptr;

    QHash<int, CmdCallback> m_callbacks;
    int m_currentSeqnro;

    struct Response
    {
        QJsonArray fields;
        int seqnro;
    };
    std::deque<Response> m_queue;

    void process();
};

}

#endif