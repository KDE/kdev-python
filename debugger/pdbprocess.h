/*
    SPDX-FileCopyrightText: 2024 Jarmo Tiitto <jarmo.tiitto@gmail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef KDEVPDBPROCESS_H
#define KDEVPDBPROCESS_H

#include <KProcess>

#include <QByteArray>
#include <QList>
#include <QLocalSocket>
#include <QMutex>
#include <QObject>
#include <QString>
#include <QTemporaryDir>
#include <QUrl>

Q_DECLARE_METATYPE(QLocalSocket::LocalSocketError);

namespace Python {

/**
 * A Manager for kdevpdb.py child process which handles:
 * - Launching and quitting of the server kdevpdb.py process.
 * - Passes in the inferior command line.
 * - Handles the stdout/stderr output from the inferior.
 * - Socket I/O and queuing of to-be-sent data-frames.
 */
class PdbProcess : public QObject
{
    Q_OBJECT
public:
    PdbProcess(QObject* parent = nullptr);
    ~PdbProcess();

    /**
     * Create the process and setup the I/O to it.
     * @param arguments the inferior program and it's arguments. (and any additional arguments for Pdb)
     */
    void initialize(QString interpreter, QStringList arguments, QString workingdir, QProcessEnvironment env);

    /**
     * How many data-frames the server will send once we initialize() it. @see kdevpdb.py __init__()
     * method, this value must be kept in-sync with the number pre-inserted frames.
     */
    static constexpr int FRAMES_BEFORE_READY = 1;

    /**
     * Enqueue a data-frame to the debugger.
     * @param data a data-frame to be queued.
     * @note kdevpdb.py only accepts the commands in the following format:
     *       JSON: { "seq": < number>, "input": "string terminated by '\\n'" }
     *       The entire payload must be utf8 encoded.
     */
    void sendCommand(const QByteArray data);

    enum ControlCommand : int32_t { Terminate = -1, DoNothing = 0 };
    /**
     * Enqueue a escape frame.
     * @note Since escape frames are currently immediately processed by the kdevpdb.py's receiver
     *       thread, the escape frame is queued with synchronizeFirst = true.
     */
    void sendControlCommand(ControlCommand code);

    /**
     * Get the process.
     */
    KProcess* process() const
    {
        return m_debuggerProcess;
    }

    /**
     * Kill the debugger process ungracefully.
     */
    void killNow();

    /**
     * Ask the debugger to stop running the inferior's code or break out of processing a command.
     * @note Only interrupts the process if we are currently waiting for a response.
     * @return true, if an interrupt was made.
     * @warn The debugger may stop at an arbitrary point.
     */
    bool tryInterrupt();

    /**
     * Check if the debugger is busy: until all (queued) commands are actually sent, and their
     * responses have been received, returns true.
     */
    bool isBusy() const;

    /**
     * Emit suspended() if the debugger is not busy.
     */
    void signalSuspended();

Q_SIGNALS:
    /**
     * Emitted when a non-empty data-frame has been received.
     * @note The payload data is utf8 encoded. JSON: {"seq": < number>, "data": [objects]} The
     *       response "data" is a list of objects in a unspecified order. The listed objects are
     *       dictionaries with a single key such as "frames", "message", "error", etc.
     */
    void dataReceived(const QByteArray& data);

    /**
     * Standard output data available.
     */
    void stdoutAvailable(QByteArray data);

    /**
     * Standard error data available.
     */
    void stderrAvailable(QByteArray data);

    /**
     * Emitted once the connection is up and I/O can happen.
     */
    void ready();

    /**
     * Emitted when we have pending commands that cannot be sent yet.
     */
    void running();

    /**
     * Emitted when all commands processed and their responses have arrived.
     */
    void suspended();

    /**
     * Emitted when the connection has stopped/failed for any reason.
     */
    void socketStatus(QLocalSocket::LocalSocketError reason);

    /**
     * Emitted once the PdbWorker has completed all of its tasks:
     * - The process has terminated.
     * - All necessary data has been read from the process.
     * - Connection has stopped/failed.
     */
    void finished();

private Q_SLOTS:
    // Launched process terminated.
    void processEnded(int exitCode, QProcess::ExitStatus exitStatus);
    void processError(QProcess::ProcessError error);
    // Error happened on the socket.
    void error(QLocalSocket::LocalSocketError reason);
    // Try to read more data from the socket.
    void tryRecvFrame();
    // Possible to read more data from the process stdout/stderr.
    void processIoReady(int channel);

private:
    /// How large a received data-frame can be before we warn.
    static constexpr int32_t WARN_TOO_BIG_FRAMESIZE = 1024 * 1024 * 128;
    /// How large a received data-frame can be before we kill the connection.
    static constexpr int32_t DIE_TOO_BIG_FRAMESIZE = 1024 * 1024 * 512;
    /// Inferior/debug server process.
    QString m_debuggerDir;
    QTemporaryDir m_socketdir;
    KProcess* m_debuggerProcess = nullptr;
    int m_exitCode = -1;
    QProcess::ExitStatus m_exitStatus = QProcess::ExitStatus::NormalExit;
    /// The socket.
    QLocalSocket* m_socket = nullptr;
    /// Data-frame receiving.
    QByteArray m_frameBuf;
    int32_t m_frameRecv = -1;
    /// Data-frame send FIFO.
    struct DataFrame
    {
        /// Payload length (bytes) or if less or equal to zero a escape-code.
        int32_t hdr;
        QByteArray data;
        bool synchronizeFirst = true;
    };
    QList<DataFrame> m_sendQueue;
    /// Debugger synchronization state.
    int m_recvFrames = 0;
    int m_sentFrames = FRAMES_BEFORE_READY;
    bool m_debuggerBusy = true;

    void connectToServer();
    void trySendFrame();
};

} // namespace Python

#endif