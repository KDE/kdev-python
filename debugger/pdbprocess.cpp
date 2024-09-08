/*
    SPDX-FileCopyrightText: 2024 Jarmo Tiitto <jarmo.tiitto@gmail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/
#include "pdbprocess.h"
#include "startupinfo.h"

#include <QDebug>
#include <QString>

#include "debuggerdebug.h"

namespace Python {

/// @see pdbinterrupt.cpp
extern void interruptProcess(KProcess* process);

PdbProcess::PdbProcess(QObject* parent)
    : QObject(parent)
{
}

PdbProcess::~PdbProcess()
{
}

void PdbProcess::start(const StartupInfo& info)
{
    if (!m_socketdir.isValid() || info.scriptPath.isEmpty() || info.debuggerPath.isEmpty()) {
        Q_EMIT finished();
        return;
    }

    // Launch the debugger process.
    m_debuggerProcess = new KProcess(this);
    // Add required arguments for the kdevpdb.py server process.
    // TODO: Pass arguments (-m) which we can support to the kdevpdb.py script and accept
    //       interpreter arguments that don't interfere with debugging.
    *m_debuggerProcess << info.interpreter.constFirst() << QStringLiteral("-u") // Need unbuffered stdout/stderr
                       << info.debuggerPath << QStringLiteral("-s") << m_socketdir.path() + QStringLiteral("/")
                       << QStringLiteral("--") << info.scriptPath << info.args;
    m_debuggerProcess->setOutputChannelMode(KProcess::SeparateChannels);
    m_debuggerProcess->setWorkingDirectory(info.workingDirectory.path());
    m_debuggerProcess->setProcessEnvironment(info.environment);

    connect(m_debuggerProcess, qOverload<int, QProcess::ExitStatus>(&QProcess::finished), this,
            &PdbProcess::processEnded);
    connect(m_debuggerProcess, &QProcess::errorOccurred, this, &PdbProcess::processError);
    // Must be queued or we may fail to read the data.
    connect(m_debuggerProcess, &QProcess::channelReadyRead, this, &PdbProcess::processIoReady, Qt::QueuedConnection);

    qCDebug(KDEV_PYTHON_DEBUGGER) << "creating debugger process:" << m_debuggerProcess->program();

    // The Pdb server/inferior initialization is split into a few phases:
    // 0. After constructor: m_socket == null, m_sentFrames > 0, m_recvFrames == 0, isBusy() returns true.
    // 1. Launch the process.
    // 2. A start-up synchronization is done by reading a "socket:" line from the kdevpdb.py stdout before
    //    we create our socket and connect. (otherwise we could race and get ConnectionRefusedError)
    // 3. Once the socket is connected, the server sends initial response(s).
    //    Receiving the response(s) brings the system into a full sync, where m_sentFrames == m_recvFrames.
    // 4. ready() signal is finally emitted by tryRecvFrame(), along with bunch of other signals.
    //    At the point of the ready() signal, the debugger is fully operational.
    m_debuggerProcess->start();
}

void PdbProcess::sendCommand(const QByteArray data)
{
    m_sendQueue.emplaceBack(DataFrame{static_cast<int32_t>(data.size()), std::move(data), false});
    QMetaObject::invokeMethod(this, &PdbProcess::trySendFrame, Qt::QueuedConnection);
}

void PdbProcess::sendControlCommand(ControlCommand code)
{
    m_sendQueue.emplaceBack(DataFrame{static_cast<int32_t>(code), {}, true});
    QMetaObject::invokeMethod(this, &PdbProcess::trySendFrame, Qt::QueuedConnection);
}

void PdbProcess::killNow()
{
    if (m_exitWait || !m_debuggerProcess || m_debuggerProcess->state() == KProcess::NotRunning) {
        return;
    }
    // Inhibit all of our signals first and kill the debugger process.
    m_exitWait = new QEventLoop(this);
    m_sendQueue.clear();
    m_debuggerProcess->kill();
    // Process events until the process is terminated.
    while (m_debuggerProcess->state() != KProcess::NotRunning) {
        m_exitWait->processEvents(QEventLoop::WaitForMoreEvents);
    }
}

bool PdbProcess::tryInterrupt()
{
    // Interrupting the debugger process is only possible when we are missing responses,
    // and the debugger has explicitly allowed the interruption.
    if (m_allowInterrupt && m_recvFrames < m_sentFrames) {
        interruptProcess(m_debuggerProcess);
        return true;
    } else {
        return false;
    }
}

bool PdbProcess::isBusy() const
{
    // PdbProcess remains is busy while we are missing responses to any sent data-frames
    // or if we haven't sent all of the data-frames yet.
    return m_recvFrames < (m_sentFrames + m_sendQueue.size());
}

void PdbProcess::connectToServer()
{
    qCDebug(KDEV_PYTHON_DEBUGGER).noquote()
        << "debugger process ready, connecting to" << m_socketdir.filePath(QStringLiteral("kdevpdb.socket"));
    m_socket = new QLocalSocket(this);
    // Signals from the socket must be queued/deferred for the slots to work.
    connect(m_socket, &QLocalSocket::errorOccurred, this, &PdbProcess::error, Qt::QueuedConnection);
    connect(m_socket, &QLocalSocket::readyRead, this, &PdbProcess::tryRecvFrame, Qt::QueuedConnection);
    m_socket->connectToServer(m_socketdir.filePath(QStringLiteral("kdevpdb.socket")));
}

void PdbProcess::processEnded(int exitCode, QProcess::ExitStatus exitStatus)
{
    // TODO: Read all remaining data out from the process device.
    m_exitCode = exitCode;
    m_exitStatus = exitStatus;

    qCDebug(KDEV_PYTHON_DEBUGGER) << "process exited with code:" << m_exitCode;

    if (m_socket && m_socket->state() == QLocalSocket::ConnectedState) {
        // Somehow not disconnected yet.
        m_socket->disconnectFromServer();
    }

    if (!m_exitWait) {
        // Process exited voluntarily.
        Q_EMIT finished();
    }
}

void PdbProcess::processError(QProcess::ProcessError error)
{
    qCWarning(KDEV_PYTHON_DEBUGGER) << "process error:" << error;
}

void PdbProcess::error(QLocalSocket::LocalSocketError reason)
{
    qCWarning(KDEV_PYTHON_DEBUGGER) << "socket error:" << reason;

    if (!m_exitWait) {
        Q_EMIT socketStatus(reason);
    }

    if (m_socket && m_socket->state() == QLocalSocket::ConnectedState) {
        m_socket->disconnectFromServer();
    }
}

void PdbProcess::trySendFrame()
{
    if (m_exitWait || m_sendQueue.isEmpty() || !m_socket) {
        return;
    }

    // Escape codes must wait for previous commands to complete before they are sent.
    // E.g. sending ControlCommand::Terminate would close the connection *immediately*,
    // because this is processed by the kdevpdb.py's receiver thread.
    if (m_recvFrames < m_sentFrames && m_sendQueue.first().synchronizeFirst) {
        qCDebug(KDEV_PYTHON_DEBUGGER) << "not sending until synchronized:" << m_sendQueue.size()
                                      << "data-frames are waiting";
        return;
    }

    if (!m_debuggerBusy) {
        m_debuggerBusy = true;
        Q_EMIT running();
    }

    if (m_socket && m_socket->state() != QLocalSocket::ConnectedState) {
        qCCritical(KDEV_PYTHON_DEBUGGER) << "Socket not in connected state!";
        return;
    }

    const auto frame = m_sendQueue.takeFirst();

    // Send the data-frame header.
    qint64 ret = m_socket->write(reinterpret_cast<const char*>(&frame.hdr), sizeof(DataFrame::hdr));
    if (ret != sizeof(DataFrame::hdr)) {
        qCCritical(KDEV_PYTHON_DEBUGGER) << "Got" << m_socket->error() << "while writing header!";
    }

    if (frame.hdr > 0) {
        // Send the data-frame payload.
        qint64 written = 0;
        while (written < frame.hdr) {
            ret = m_socket->write(frame.data.data() + written, frame.hdr - written);
            if (ret < 1) {
                qCCritical(KDEV_PYTHON_DEBUGGER) << "Got" << m_socket->error() << "while writing data!";
                break;
            }
            written += ret;
        }
        if (written != frame.hdr) {
            qCCritical(KDEV_PYTHON_DEBUGGER) << "Failed to send a complete data-frame!";
        }
    }

    m_socket->flush();
    m_sentFrames++;
    qCDebug(KDEV_PYTHON_DEBUGGER) << "sent a data-frame: need" << (m_sentFrames - m_recvFrames)
                                  << "received frames to synchronize";

    if (!m_sendQueue.isEmpty() && (m_recvFrames >= m_sentFrames || !m_sendQueue.first().synchronizeFirst)) {
        // Can send the next frame immediately.
        QMetaObject::invokeMethod(this, &PdbProcess::trySendFrame, Qt::QueuedConnection);
    }
}

void PdbProcess::tryRecvFrame()
{
    if (m_exitWait || (m_socket && m_socket->state() != QLocalSocket::ConnectedState)) {
        qCCritical(KDEV_PYTHON_DEBUGGER) << "Socket not in connected state or process is about to exit!";
        return;
    }

    if (m_frameRecv < 0) {
        // No frame length or escape code received yet.
        if (m_socket->bytesAvailable() < qint64(sizeof(DataFrame::hdr))) {
            return; // Not enough data. (read() would fail)
        }
        int32_t frameHdr = 0;
        qint64 ret = m_socket->read(reinterpret_cast<char*>(&frameHdr), sizeof(DataFrame::hdr));
        if (ret != sizeof(DataFrame::hdr)) {
            // Shouldn't happen...
            qCCritical(KDEV_PYTHON_DEBUGGER) << "Reading frame header failed!";
            return;
        }

        // Check for an escape frame:
        switch (frameHdr) {
        case ControlCommand::DoNothing:
            qCDebug(KDEV_PYTHON_DEBUGGER) << "received empty frame";
            QMetaObject::invokeMethod(this, &PdbProcess::tryRecvFrame, Qt::QueuedConnection);
            return;
        case ControlCommand::Terminate:
            // End connection. Since the connection will be dead soon don't bother scheduling a further read.
            m_socket->disconnectFromServer();
            return;
        case ControlCommand::InterruptDisallowed:
            // Notification from the debugger that we are forbidden to interrupt it.
            qCDebug(KDEV_PYTHON_DEBUGGER) << "interrupting was disabled";
            m_allowInterrupt = false;
            QMetaObject::invokeMethod(this, &PdbProcess::tryRecvFrame, Qt::QueuedConnection);
            return;
        case ControlCommand::InterruptAllowed:
            // Notification from the debugger that it is possible to interrupt it.
            qCDebug(KDEV_PYTHON_DEBUGGER) << "interrupting possible";
            m_allowInterrupt = true;
            QMetaObject::invokeMethod(this, &PdbProcess::tryRecvFrame, Qt::QueuedConnection);
            return;
        default:
            break;
        }

        // Limit the size of a received data-frames.
        if (frameHdr > WARN_TOO_BIG_FRAMESIZE) {
            qCWarning(KDEV_PYTHON_DEBUGGER) << "Received data-frame size" << frameHdr << "is greater than"
                                            << WARN_TOO_BIG_FRAMESIZE << "bytes. This is likely a bug!";
        } else if (frameHdr > DIE_TOO_BIG_FRAMESIZE) {
            qCCritical(KDEV_PYTHON_DEBUGGER) << "Received data-frame size" << frameHdr << "is greater than"
                                             << DIE_TOO_BIG_FRAMESIZE << "bytes. This is a bug!";
            // End the connection.
            m_socket->disconnectFromServer();
            return;
        }
        // Prepare receiving the data-frame payload.
        m_frameRecv = 0;
        m_frameBuf.resize(frameHdr);
    }

    Q_ASSERT(m_frameRecv >= 0);
    Q_ASSERT(m_frameBuf.size() > m_frameRecv);
    qint64 ret = m_socket->read(m_frameBuf.data() + m_frameRecv, m_frameBuf.size() - m_frameRecv);
    if (ret > 0) {
        m_frameRecv += ret;
        if (m_socket->bytesAvailable() > 0) {
            // Multiple frames can arrive at once, so continue processing until no more data can be read.
            QMetaObject::invokeMethod(this, &PdbProcess::tryRecvFrame, Qt::QueuedConnection);
        }
    }
    if (m_frameRecv != m_frameBuf.size()) {
        // Received a partial data-frame.
        // Since m_frameRecv >= 0, just return now and continue reading on the next tryRecvFrame() invocation.
        return;
    }
    // Received a complete data-frame.
    m_frameRecv = -1;
    m_recvFrames++;

    // Is the server fully booted up yet?
    if (m_recvFrames == FRAMES_BEFORE_READY) {
        Q_EMIT ready();
    } else if (m_recvFrames == m_sentFrames) {
        // Reached a synchronized state, reset counts to FRAMES_BEFORE_READY+1 so that we'll never overflow them.
        m_recvFrames = FRAMES_BEFORE_READY + 1;
        m_sentFrames = FRAMES_BEFORE_READY + 1;
        qCDebug(KDEV_PYTHON_DEBUGGER) << "synchronized state was reached";
    }

    // Report the data-frame.
    Q_EMIT dataReceived(m_frameBuf);

    // Schedule sending the next request, if any.
    if (!m_sendQueue.isEmpty()) {
        QMetaObject::invokeMethod(this, &PdbProcess::trySendFrame, Qt::QueuedConnection);
    }
}

void PdbProcess::signalSuspended()
{
    if (!isBusy()) {
        // Not busy and send queue empty => suspended.
        m_debuggerBusy = false;
        Q_EMIT suspended();
    }
}

void PdbProcess::processIoReady(int channel)
{
    if (m_exitWait) {
        return;
    }
    // the process produced some output.
    QByteArray data;
    switch (channel) {
    case QProcess::StandardOutput:
        if (!m_socket) {
            // the debugger process should be listening now.
            data = m_debuggerProcess->readLine();
            if (data.startsWith("socket:")) {
                connectToServer();
            } else {
                qCWarning(KDEV_PYTHON_DEBUGGER) << "Unexpected output from the debugger process";
            }
        }

        data = m_debuggerProcess->readAllStandardOutput();
        if (!data.isEmpty()) {
            Q_EMIT stdoutAvailable(data);
        }
        return;
    case QProcess::StandardError:
        data = m_debuggerProcess->readAllStandardError();
        if (!data.isEmpty()) {
            Q_EMIT stderrAvailable(data);
        }
        return;
    }
}

} // namespace Python

#include "moc_pdbprocess.cpp"