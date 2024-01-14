/*
    SPDX-FileCopyrightText: 2016 Sven Brauch <mail@svenbrauch.de>

    SPDX-License-Identifier: GPL-2.0-only OR GPL-3.0-only OR LicenseRef-KDE-Accepted-GPL
*/

#include "pythonstylechecking.h"

#include <QTimer>
#include <QStandardPaths>
#include <QRegularExpression>

#include <language/duchain/problem.h>
#include <language/editor/documentrange.h>
#include <interfaces/icore.h>

#include <shell/documentcontroller.h>

#include <KTextEditor/Document>

#include "pythondebug.h"
#include "pythonparsejob.h"
#include "helpers.h"

namespace Python {

StyleChecking::StyleChecking(QObject* parent)
    : QObject(parent)
{
    qRegisterMetaType<KDevelop::ReferencedTopDUContext>("KDevelop::ReferencedTopDUContext");
    connect(&m_checkerProcess, &QProcess::readyReadStandardOutput,
            this, &StyleChecking::processOutputStarted);
    connect(&m_checkerProcess, &QProcess::readyReadStandardError,
            [this]() {
                qWarning() << "python code checker error:" << m_checkerProcess.readAllStandardError();
            });
    auto config = KSharedConfig::openConfig(QStringLiteral("kdevpythonsupportrc"));
    m_pep8Group = config->group(QStringLiteral("pep8"));
}

StyleChecking::~StyleChecking()
{
    if ( m_checkerProcess.state() == QProcess::Running ) {
        m_checkerProcess.terminate();
        m_checkerProcess.waitForFinished(100);
    }
}

void StyleChecking::startChecker(const QString& text, const QString& select,
                                 const QString& ignore, const int maxLineLength)
{
    // start up the server
    if ( m_checkerProcess.state() == QProcess::NotRunning ) {
        auto python = Helper::getPythonExecutablePath(nullptr);
        auto serverPath = QStandardPaths::locate(QStandardPaths::GenericDataLocation, QStringLiteral("kdevpythonsupport/codestyle.py"));
        if ( serverPath.isEmpty() ) {
            qWarning() << "setup problem: codestyle.py not found";
            m_mutex.unlock();
            return;
        }
        m_checkerProcess.start(python, {serverPath});
        m_checkerProcess.waitForStarted(30);
        if ( m_checkerProcess.state() != QProcess::Running ) {
            qWarning() << "failed to start code checker process";
            m_mutex.unlock();
            return;
        }
    }

    // send input
    QByteArray data = text.toUtf8();
    QByteArray header;
    header.append(select.toUtf8());
    header.append("\n");
    header.append(ignore.toUtf8());
    header.append("\n");
    header.append(QByteArray::number(maxLineLength));
    header.append("\n");
    // size, always 10 bytes
    header.insert(0, QByteArray::number(header.size() + data.size()).leftJustified(10));
    m_checkerProcess.write(header);
    m_checkerProcess.write(data);
}

void StyleChecking::addErrorsToContext(const QVector<QString>& errors)
{
    static QRegularExpression errorFormat(QStringLiteral("(.*):(\\d*):(\\d*): (.*)"), QRegularExpression::CaseInsensitiveOption);
    DUChainWriteLocker lock;
    auto document = m_currentlyChecking->url();
    for ( const auto& error : errors ) {
        QRegularExpressionMatch match;
        if ( (match = errorFormat.match(error)).hasMatch() ) {
            bool lineno_ok = false;
            bool colno_ok = false;
            int lineno = match.captured(2).toInt(&lineno_ok);
            int colno = match.captured(3).toInt(&colno_ok);
            if ( ! lineno_ok || ! colno_ok ) {
                qCDebug(KDEV_PYTHON) << "invalid line / col number";
                continue;
            }
            QString error = match.captured(4);
            KDevelop::Problem* p = new KDevelop::Problem();
            p->setFinalLocation(DocumentRange(document, KTextEditor::Range(lineno - 1, qMax(colno - 1, 0),
                                                                           lineno - 1, colno)));
            p->setSource(KDevelop::IProblem::Preprocessor);
            p->setSeverity(error.startsWith(QLatin1Char('W')) ? KDevelop::IProblem::Hint : KDevelop::IProblem::Warning);
            p->setDescription(i18n("PEP8 checker error: %1", error));
            ProblemPointer ptr(p);
            m_currentlyChecking->addProblem(ptr);
        }
        else {
            qCDebug(KDEV_PYTHON) << "invalid pep8 error line:" << error;
        }
    }

    m_currentlyChecking->setFeatures((TopDUContext::Features) ( m_currentlyChecking->features() | ParseJob::PEP8Checking ));
}

void StyleChecking::processOutputStarted()
{
    if (m_mutex.try_lock()) {
        // The m_mutex (which is *not* recursive) was not locked!!
        // This probably means there is some problem with the
        // checker server, which is sending us more data than
        // we expected (or consumed). The only way we can deal
        // with this situation is to kill the server and start it
        // again, when needed
        if ( m_checkerProcess.state() == QProcess::Running ) {
            m_checkerProcess.terminate();
            m_checkerProcess.waitForFinished(100);
        }
        m_mutex.unlock();
        return;
    }

    // read output size
    QByteArray size_d;
    size_d = m_checkerProcess.read(10);
    bool ok;
    auto size = size_d.toInt(&ok);
    if ( !ok || size < 0 ) {
        addSetupErrorToContext(QStringLiteral("Got invalid size: ") + QString::fromLatin1(size_d));
        m_mutex.unlock();
        return;
    }

    // read actual output
    QByteArray buf;
    QTimer t;
    t.setSingleShot(true);
    t.start(100);
    while ( size > 0 && t.remainingTime() > 0 ) {
        auto d = m_checkerProcess.read(qMin(4096, size));
        buf.append(d);
        size -= d.size();
        qDebug() << "remaining:" << size << d.size();
    }

    // process it
    QVector<QString> errors;
    auto ofs = -1;
    auto prev = ofs;
    while ( prev = ofs, (ofs = buf.indexOf('\n', ofs+1)) != -1 ) {
        errors.append(QString::fromLatin1(buf.mid(prev+1, ofs-prev)));
    }
    if ( !t.isActive() ) {
        addSetupErrorToContext(QStringLiteral("Output took longer than 100 ms."));
    }
    addErrorsToContext(errors);

    // done, unlock mutex
    m_currentlyChecking = nullptr;
    m_mutex.unlock();
}

void StyleChecking::updateStyleChecking(const KDevelop::ReferencedTopDUContext& top)
{
    if ( !top ) {
        return;
    }
    auto url = top->url();
    IDocument* idoc = ICore::self()->documentController()->documentForUrl(url.toUrl());
    if ( !idoc || !idoc->textDocument() || top->features() & ParseJob::PEP8Checking ) {
        return;
    }
    auto text = idoc->textDocument()->text();

    if ( !m_mutex.tryLock(1000) ) {
        qWarning() << "timed out waiting for the style checker mutex";
        return;
    }
    m_currentlyChecking = top;

    // default empty is ok, it will never be used, because the config has to be written at least once
    // to even enable this feature.
    auto select = m_pep8Group.readEntry<QString>("enableErrors", QString());
    auto ignore = m_pep8Group.readEntry<QString>("disableErrors",QString());
    auto maxLineLength = m_pep8Group.readEntry<int>("maxLineLength", 80);
    startChecker(text, select, ignore, maxLineLength);
}

void StyleChecking::addSetupErrorToContext(const QString& error)
{
    DUChainWriteLocker lock;
    KDevelop::Problem *p = new KDevelop::Problem();
    p->setFinalLocation(DocumentRange(m_currentlyChecking->url(), KTextEditor::Range(0, 0, 0, 0)));
    p->setSource(KDevelop::IProblem::Preprocessor);
    p->setSeverity(KDevelop::IProblem::Warning);
    p->setDescription(i18n("The PEP8 syntax checker does not seem to work correctly.") + QStringLiteral("\n") + error);
    ProblemPointer ptr(p);
    m_currentlyChecking->addProblem(ptr);
}

};

#include "moc_pythonstylechecking.cpp"
