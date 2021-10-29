/*
    SPDX-FileCopyrightText: 2016 Sven Brauch <mail@svenbrauch.de>

    SPDX-License-Identifier: GPL-2.0-only OR GPL-3.0-only OR LicenseRef-KDE-Accepted-GPL
*/

#ifndef PYTHONSTYLECHECKING_H
#define PYTHONSTYLECHECKING_H

#include <QObject>
#include <QProcess>
#include <KConfig>
#include <KConfigGroup>

#include <language/duchain/topducontext.h>

namespace Python {

class StyleChecking : public QObject
{
Q_OBJECT
public:
    StyleChecking(QObject* parent=nullptr);
    ~StyleChecking() override;
    void startChecker(const QString& text, const QString& select={},
                      const QString& ignore={}, const int maxLineLength=80);

public Q_SLOTS:
    void updateStyleChecking(const KDevelop::ReferencedTopDUContext& top);
    void addErrorsToContext(const QVector<QString>& errors);

private Q_SLOTS:
    void processOutputStarted();

private:
    void addSetupErrorToContext(const QString& error);

private:
    QProcess m_checkerProcess;
    KDevelop::ReferencedTopDUContext m_currentlyChecking;
    QMutex m_mutex;
    KConfigGroup m_pep8Group;
};

};

#endif // PYTHONSTYLECHECKING_H
