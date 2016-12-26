/*
 * <one line to give the program's name and a brief idea of what it does.>
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
    ~StyleChecking();
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
