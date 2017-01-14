/*
 * Copyright 2016  Sven Brauch <mail@svenbrauch.de>
 * 
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License as
 * published by the Free Software Foundation; either version 2 of
 * the License or (at your option) version 3 or any later version
 * accepted by the membership of KDE e.V. (or its successor approved
 * by the membership of KDE e.V.), which shall act as a proxy
 * defined in Section 14 of version 3 of the license.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * 
 */

#include "pythonstylechecking.h"

#include <QTimer>
#include <QStandardPaths>
#include <QRegularExpression>

#include <language/duchain/problem.h>
#include <interfaces/icore.h>
#include <shell/documentcontroller.h>

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
    auto config = KSharedConfig::openConfig("kdevpythonsupportrc");
    m_pep8Group = config->group("pep8");
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
        auto serverPath = QStandardPaths::locate(QStandardPaths::GenericDataLocation, "kdevpythonsupport/codestyle.py");
        if ( serverPath.isEmpty() ) {
            qWarning() << "setup problem: codestyle.py not found";
            return;
        }
        m_checkerProcess.start(python, {serverPath});
        m_checkerProcess.waitForStarted(30);
        if ( m_checkerProcess.state() != QProcess::Running ) {
            qWarning() << "failed to start code checker process";
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
    header.insert(0, QString::number(header.size() + data.size()).leftJustified(10));
    m_checkerProcess.write(header);
    m_checkerProcess.write(data);
}

void StyleChecking::addErrorsToContext(const QVector<QString>& errors)
{
    static QRegularExpression errorFormat("(.*):(\\d*):(\\d*): (.*)", QRegularExpression::CaseInsensitiveOption);
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
            p->setFinalLocation(DocumentRange(document, KTextEditor::Range(lineno - 1, qMax(colno - 4, 0),
                                                                           lineno - 1, colno + 4)));
            p->setSource(KDevelop::IProblem::Preprocessor);
            p->setSeverity(error.startsWith('W') ? KDevelop::IProblem::Hint : KDevelop::IProblem::Warning);
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
    // read output size
    QByteArray size_d;
    size_d = m_checkerProcess.read(10);
    bool ok;
    auto size = size_d.toInt(&ok);
    if ( !ok || size < 0 ) {
        addSetupErrorToContext("Got invalid size: " + size_d);
        m_mutex.unlock();
        return;
    }

    // read actual output
    QByteArray buf;
    QTimer t;
    t.start(100);
    while ( size > 0 && t.isActive() ) {
        auto d = m_checkerProcess.read(size);
        buf.append(d);
        size -= d.size();
    }

    // process it
    QVector<QString> errors;
    auto ofs = -1;
    auto prev = ofs;
    while ( prev = ofs, (ofs = buf.indexOf('\n', ofs+1)) != -1 ) {
        errors.append(buf.mid(prev+1, ofs-prev));
    }
    if ( !t.isActive() ) {
        addSetupErrorToContext("Output took longer than 100 ms.");
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
        return;
    }
    m_currentlyChecking = top;

    // default empty is ok, it will never be used, because the config has to be written at least once
    // to even enable this feature.
    auto select = m_pep8Group.readEntry<QString>("enableErrors", "");
    auto ignore = m_pep8Group.readEntry<QString>("disableErrors", "");
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
    p->setDescription(i18n("The PEP8 syntax checker does not seem to work correctly.") + "\n" + error);
    ProblemPointer ptr(p);
    m_currentlyChecking->addProblem(ptr);
}

};
