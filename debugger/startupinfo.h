/*
    SPDX-FileCopyrightText: 2025 Jarmo Tiitto <jarmo.tiito@gmail.com>

    SPDX-License-Identifier: GPL-2.0-or-later
*/

#ifndef STARTUPINFOSTRUCT_H
#define STARTUPINFOSTRUCT_H

#include <QProcessEnvironment>
#include <QString>
#include <QStringList>
#include <QUrl>

namespace Python {

struct StartupInfo
{
    QString scriptPath;
    QString debuggerPath;
    QStringList interpreter;
    QStringList args;
    QUrl workingDirectory;
    QProcessEnvironment environment;
};

}
#endif
